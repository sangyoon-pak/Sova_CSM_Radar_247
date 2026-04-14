#!/usr/bin/env bash
# Run gmail-get-decoded.py locally (Mac) for recursive testing.
# Ensure gog is installed and OAuth is done for your Gmail.
# See docs/GMAIL_SETUP.md for auth.
#
# Optional: if you keep a local ``.env`` file for shell convenience, this script
# sources it. The Sova server does not read ``.env``; use Configure or export vars.
# Otherwise set GOG_ACCOUNT and GOG_KEYRING_PASSWORD in the environment.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
PY="${SCRIPT_DIR}/gmail-get-decoded.py"

if [[ -f "${REPO_ROOT}/.env" ]]; then
  set -a
  # shellcheck disable=SC1091
  source "${REPO_ROOT}/.env"
  set +a
fi

export GMAIL_SCRIPT_LOCAL=1

if [[ -z "${GOG_ACCOUNT:-}" ]]; then
  echo "GOG_ACCOUNT is not set. Export GOG_ACCOUNT (or source a local .env for this script only)." >&2
  exit 1
fi

# Use project-installed gog if available
if [[ -f "${SCRIPT_DIR}/.local/bin/gog" ]]; then
  export GOG_BIN="${SCRIPT_DIR}/.local/bin/gog"
  export GOG_HOME="${SCRIPT_DIR}/.local"
fi

MAX="${1:-5}"
echo "=== Local Gmail test: --max $MAX --verbose ==="
exec python3 "$PY" --search 'in:inbox category:primary newer_than:2d' --max "$MAX" --verbose 2>&1
