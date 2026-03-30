#!/usr/bin/env bash
# Run gmail-get-decoded.py locally (Mac) for recursive testing.
# Ensure gog is installed and OAuth is done for your Gmail.
# See docs/GMAIL_SETUP.md for auth.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PY="${SCRIPT_DIR}/gmail-get-decoded.py"

export GMAIL_SCRIPT_LOCAL=1
export GOG_ACCOUNT="${GOG_ACCOUNT:-sangyoon.park@appier.com}"
export GOG_KEYRING_PASSWORD="${GOG_KEYRING_PASSWORD:-openclaw-gmail}"

# Use project-installed gog if available
if [[ -f "${SCRIPT_DIR}/.local/bin/gog" ]]; then
  export GOG_BIN="${SCRIPT_DIR}/.local/bin/gog"
  export GOG_HOME="${SCRIPT_DIR}/.local"
fi

MAX="${1:-5}"
echo "=== Local Gmail test: --max $MAX --verbose ==="
exec python3 "$PY" --search 'in:inbox category:primary newer_than:2d' --max "$MAX" --verbose 2>&1

