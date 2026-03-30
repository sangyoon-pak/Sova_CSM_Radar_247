#!/usr/bin/env bash
# Install gog (gogcli) on Mac for local Gmail testing.
# Run once, then do OAuth (read-only Gmail): gog auth add YOUR_EMAIL --services gmail --readonly --manual

set -e

GOG_VERSION="0.11.0"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BIN_DIR="${SCRIPT_DIR}/.local/bin"

mkdir -p "$BIN_DIR"

ARCH=$(uname -m)
case "$ARCH" in
  arm64|aarch64) GOG_ARCH="darwin_arm64" ;;
  x86_64)        GOG_ARCH="darwin_amd64" ;;
  *)             echo "Unsupported arch: $ARCH"; exit 1 ;;
esac

GOG_URL="https://github.com/steipete/gogcli/releases/download/v${GOG_VERSION}/gogcli_${GOG_VERSION}_${GOG_ARCH}.tar.gz"
echo "Installing gog v${GOG_VERSION} ($GOG_ARCH) to $BIN_DIR"
curl -sL "$GOG_URL" | tar xzf - -C /tmp
mv /tmp/gog "$BIN_DIR/gog"
chmod +x "$BIN_DIR/gog"
echo "✓ Installed to $BIN_DIR"
echo ""
echo "Next: OAuth (use credentials.json with gmail.readonly scope):"
echo "  $BIN_DIR/gog auth credentials /path/to/credentials.json"
echo "  $BIN_DIR/gog auth add YOUR_EMAIL --services gmail --readonly --manual"
echo ""
echo "Then run a quick local test:"
echo "  GMAIL_SCRIPT_LOCAL=1 GOG_BIN=$BIN_DIR/gog ./test-gmail-local.sh 5"

