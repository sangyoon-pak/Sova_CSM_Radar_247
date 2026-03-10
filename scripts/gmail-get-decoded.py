#!/usr/bin/env python3
"""
Gmail message getter with proper charset decoding for Korean and other encodings.
Uses gog's raw format and decodes MIME parts with correct charset (EUC-KR, UTF-8, etc.).
Fixes garbled text from emails sent with non-UTF-8 encodings (e.g. from Korean Outlook).

Usage:
  gmail-get-decoded.py [--search QUERY] [--max N]   # Probe inbox (default: in:inbox category:primary newer_than:2d)
  gmail-get-decoded.py <message_id> [thread]        # Single message or full thread

Local testing (Mac): GMAIL_SCRIPT_LOCAL=1 python3 gmail-get-decoded.py --max 5 --verbose
"""

import argparse
import base64
import email
import json
import os
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from email import policy
from email.utils import parsedate_to_datetime

# Encodings to try for Korean/international email (in order)
FALLBACK_ENCODINGS = ("utf-8", "cp949", "euc-kr", "iso-2022-kr", "latin1")

# Max body chars to avoid raw JSON/HTML dumps (calendar invites, etc.)
MAX_BODY_CHARS = 4000


def decode_body(part):
    """Decode a MIME part's payload with proper charset handling."""
    charset = part.get_content_charset()
    payload = part.get_payload(decode=True)
    if not payload:
        return ""

    for enc in ([charset] if charset else []) + list(FALLBACK_ENCODINGS):
        if not enc:
            continue
        try:
            return payload.decode(enc, errors="strict")
        except (LookupError, UnicodeDecodeError):
            continue
    return payload.decode("utf-8", errors="replace")


def extract_text_from_msg(msg):
    """Extract plain text and HTML from email.message, decoded."""
    plain_parts = []
    html_parts = []

    for part in msg.walk():
        ct = part.get_content_type()
        if ct == "text/plain":
            plain_parts.append(decode_body(part))
        elif ct == "text/html":
            html_parts.append(decode_body(part))

    if plain_parts:
        text = "\n".join(plain_parts)
    elif html_parts:
        text = " ".join(html_parts)
        text = re.sub(r"<[^>]+>", " ", text)
        text = re.sub(r"\s+", " ", text).strip()
    else:
        return ""

    # Truncate to avoid raw JSON/HTML/card dumps (calendar invites, Teams, etc.)
    if len(text) > MAX_BODY_CHARS:
        text = text[:MAX_BODY_CHARS].rstrip() + "\n\n[... truncated ...]"
    return text


def _is_local():
    """True when running outside container (Mac/local). Set GMAIL_SCRIPT_LOCAL=1 to enable."""
    return os.environ.get("GMAIL_SCRIPT_LOCAL") == "1"


def gog_env():
    """Env for gog CLI. Uses local paths when GMAIL_SCRIPT_LOCAL=1 or /data missing."""
    if _is_local():
        home = os.environ.get("GOG_HOME", os.environ.get("HOME", os.path.expanduser("~")))
        gog_bin = os.environ.get("GOG_BIN", "gog")
        path = os.path.join(home, ".local", "bin") if home else ""
        path = f"{path}:{os.environ.get('PATH', '')}" if path else os.environ.get("PATH", "")
        return {
            "HOME": home,
            "PATH": path,
            "GOG_KEYRING_BACKEND": os.environ.get("GOG_KEYRING_BACKEND", "file"),
            "GOG_KEYRING_PASSWORD": os.environ.get("GOG_KEYRING_PASSWORD", "openclaw-gmail"),
            "GOG_ACCOUNT": os.environ.get("GOG_ACCOUNT", "sangyoon.park@appier.com"),
            "XDG_CONFIG_HOME": os.environ.get("XDG_CONFIG_HOME", os.path.join(home, ".config")),
        }
    return {
        "HOME": "/data",
        "PATH": "/data/.local/bin:" + os.environ.get("PATH", ""),
        "GOG_KEYRING_BACKEND": "file",
        "GOG_KEYRING_PASSWORD": os.environ.get("GOG_KEYRING_PASSWORD", "openclaw-gmail"),
        "GOG_ACCOUNT": os.environ.get("GOG_ACCOUNT", "sangyoon.park@appier.com"),
        "XDG_CONFIG_HOME": "/data/.config",
    }


def gog_bin():
    """Path to gog binary."""
    if _is_local():
        return os.environ.get("GOG_BIN", "gog")
    return "/data/.local/bin/gog"


def fetch_raw(message_id):
    """Fetch message in raw format via gog."""
    cmd = [
        gog_bin(), "gmail", "get", message_id,
        "--format", "raw", "--json"
    ]
    result = subprocess.run(cmd, env=gog_env(), capture_output=True, text=True, timeout=60)
    if result.returncode != 0:
        print(result.stderr, file=sys.stderr)
        sys.exit(result.returncode)
    return json.loads(result.stdout)


def fetch_thread_messages(thread_id):
    """Fetch messages in a thread via gog. Returns list of (message_id, internal_date_ms)."""
    cmd = [
        gog_bin(), "gmail", "thread", "get", thread_id, "--json"
    ]
    result = subprocess.run(cmd, env=gog_env(), capture_output=True, text=True, timeout=60)
    if result.returncode != 0:
        print(result.stderr, file=sys.stderr)
        sys.exit(result.returncode)
    data = json.loads(result.stdout)
    thread = data.get("thread", data)
    messages = thread.get("messages", [])
    if isinstance(messages, dict):
        messages = [messages]
    # Return (id, internalDate) - use 0 if internalDate missing (treat as oldest)
    out = []
    for m in messages:
        mid = m.get("id")
        if not mid:
            continue
        try:
            ts = int(m.get("internalDate", 0))
        except (ValueError, TypeError):
            ts = 0
        out.append((mid, ts))
    return out


def latest_message_in_thread(thread_id):
    """Return the message ID of the newest message in the thread (by internalDate)."""
    msgs = fetch_thread_messages(thread_id)
    if not msgs:
        return None
    # Pick by internalDate (newest); if gog omits internalDate (all 0), use last (Gmail returns oldest-first)
    best = max(msgs, key=lambda x: x[1])
    if best[1] == 0 and len(msgs) > 1:
        return msgs[-1][0]
    return best[0]


def latest_in_thread_with_date(thread_id):
    """Return (message_id, internal_date_ms) for newest message, or None."""
    msgs = fetch_thread_messages(thread_id)
    if not msgs:
        return None
    best = max(msgs, key=lambda x: x[1])
    if best[1] == 0 and len(msgs) > 1:
        return (msgs[-1][0], 0)
    return best


def thread_message_ids(thread_id):
    """Return all message IDs in thread (for full-thread mode). Gmail returns oldest-first."""
    return [m[0] for m in fetch_thread_messages(thread_id)]


def fetch_search_ids(query, max_results=10, page_token=None):
    """Run gog search and return (thread_ids, next_page_token)."""
    cmd = [
        gog_bin(), "gmail", "search", query,
        "--max", str(max_results), "--json"
    ]
    if page_token:
        cmd.extend(["--page", page_token])
    result = subprocess.run(cmd, env=gog_env(), capture_output=True, text=True, timeout=60)
    if result.returncode != 0:
        print(result.stderr, file=sys.stderr)
        sys.exit(result.returncode)
    data = json.loads(result.stdout)
    threads = data.get("threads", [])
    thread_ids = [t.get("id") for t in threads if t.get("id")]
    return thread_ids, data.get("nextPageToken", "")


def format_message(msg, msg_data):
    """Format a single message for output."""
    lines = []
    lines.append(f"id\t{msg_data.get('id', '')}")
    lines.append(f"thread_id\t{msg_data.get('threadId', '')}")
    lines.append(f"label_ids\t{','.join(msg_data.get('labelIds', []))}")
    lines.append(f"from\t{msg_data.get('from', '')}")
    lines.append(f"to\t{msg_data.get('to', '')}")
    lines.append(f"subject\t{msg_data.get('subject', '')}")
    lines.append(f"date\t{msg_data.get('date', '')}")
    lines.append("")

    for att in msg_data.get("attachments", []):
        name = att.get("name", att.get("filename", "attachment"))
        size = att.get("size", 0)
        mime = att.get("mimeType", "")
        lines.append(f"attachment\t{name}\t{size}\t{mime}")

    body = extract_text_from_msg(msg)
    if body:
        lines.append("")
        lines.append(body)
    return "\n".join(lines)


def _parse_sort_date(msg_obj, msg):
    """Return datetime for sorting (newest first). Prefer internalDate, else Date header."""
    internal = msg_obj.get("internalDate")
    if internal:
        try:
            return datetime.fromtimestamp(int(internal) / 1000, tz=timezone.utc)
        except (ValueError, TypeError):
            pass
    dh = msg.get("Date")
    if dh:
        try:
            return parsedate_to_datetime(dh)
        except (ValueError, TypeError):
            pass
    return datetime.min.replace(tzinfo=timezone.utc)


def process_message(message_id):
    """Fetch, decode, and format a single message. Returns (sort_date, formatted_str) or None."""
    data = fetch_raw(message_id)
    msg_obj = data.get("message", data)
    raw_b64 = msg_obj.get("raw")
    if not raw_b64:
        return None

    raw_bytes = base64.urlsafe_b64decode(raw_b64 + "==")
    msg = email.message_from_bytes(raw_bytes, policy=policy.default)

    msg_data = {
        "id": msg_obj.get("id", message_id),
        "threadId": msg_obj.get("threadId", message_id),
        "labelIds": msg_obj.get("labelIds", []),
        "from": str(msg.get("From", "")),
        "to": str(msg.get("To", "")),
        "subject": str(msg.get("Subject", "")),
        "date": str(msg.get("Date", "")),
        "attachments": [],
    }

    for part in msg.walk():
        if part.get_content_disposition() == "attachment":
            msg_data["attachments"].append({
                "name": part.get_filename() or "attachment",
                "size": len(part.get_payload(decode=True) or b""),
                "mimeType": part.get_content_type(),
            })

    out = format_message(msg, msg_data)
    sort_date = _parse_sort_date(msg_obj, msg)
    return (sort_date, out)


def run_search_mode(query, max_results, page_token, verbose=False):
    """Search inbox, sort by date (newest first), then output top max_results."""
    # Progress to stderr so agent sees activity (avoids kill-restart loop)
    def progress(msg):
        print(msg, file=sys.stderr, flush=True)

    # Reduced over-fetch: max_results*2 + small buffer, cap at 20 (was 50)
    # Gmail search is roughly date-ordered; we need enough to sort, not 50 threads
    fetch_count = min(max(max_results * 2, 10), 20)
    progress("Fetching inbox...")
    thread_ids, next_token = fetch_search_ids(query, fetch_count, page_token)
    if next_token:
        print(f"# Next page: --page {next_token}\n")

    progress("Sorting threads...")
    # Parallelize thread metadata fetches (was sequential, ~1s each)
    candidates = []
    with ThreadPoolExecutor(max_workers=8) as ex:
        futures = {ex.submit(latest_in_thread_with_date, tid): tid for tid in thread_ids}
        for fut in as_completed(futures):
            info = fut.result()
            if info:
                msg_id, ts = info
                candidates.append((msg_id, ts))
                if verbose:
                    tid = futures[fut]
                    print(f"# thread {tid} -> msg {msg_id} ts={ts}", file=sys.stderr)

    candidates.sort(key=lambda x: x[1], reverse=True)

    # Parallelize message fetches (was sequential, ~1s each)
    progress("Decoding messages...")
    to_fetch = [(i, msg_id) for i, (msg_id, _) in enumerate(candidates[:max_results])]
    results = []
    with ThreadPoolExecutor(max_workers=6) as ex:
        futures = {ex.submit(process_message, msg_id): (i, msg_id) for i, msg_id in to_fetch}
        for fut in as_completed(futures):
            parsed = fut.result()
            if parsed:
                i, _ = futures[fut]
                results.append((i, parsed))

    # Output in original order
    results.sort(key=lambda x: x[0])
    for i, (_, (_, out)) in enumerate(results):
        if i > 0:
            print("\n" + "=" * 60 + "\n")
        print(out, flush=True)
    progress("Done.")


def run_thread_mode(thread_id):
    """Fetch and decode full thread."""
    msg_ids = thread_message_ids(thread_id)
    for i, mid in enumerate(msg_ids):
        if i > 0:
            print("\n\n=== Message", i + 1, "/", len(msg_ids), "===\n")
        parsed = process_message(mid)
        if parsed:
            _, out = parsed
            print(out)


def main():
    parser = argparse.ArgumentParser(
        description="Fetch Gmail messages with proper charset decoding (Korean, Japanese, etc.)"
    )
    parser.add_argument("--search", nargs="?", const="in:inbox category:primary newer_than:2d",
        metavar="QUERY", help="Search (default: in:inbox category:primary newer_than:2d)")
    parser.add_argument("--max", type=int, default=10, help="Max results for --search (default: 10)")
    parser.add_argument("--page", default=None, help="Page token for --search pagination")
    parser.add_argument("--verbose", "-v", action="store_true", help="Print thread/msg debug to stderr")
    parser.add_argument("message_id", nargs="?", help="Message or thread ID (when not using --search)")
    parser.add_argument("thread", nargs="?", help="Literal 'thread' to fetch full thread")
    args = parser.parse_args()

    if args.search is not None:
        query = args.search
    else:
        query = None
    if query is not None:
        run_search_mode(query, args.max, args.page, verbose=args.verbose)
        return

    if not args.message_id:
        parser.error("message_id required (or use --search)")
        return

    if args.thread and args.thread.lower() == "thread":
        run_thread_mode(args.message_id)
    else:
        parsed = process_message(args.message_id)
        if parsed:
            _, out = parsed
            print(out)
        else:
            print("No message found", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
