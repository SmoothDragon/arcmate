#!/usr/bin/env bash
# Create .venv and install dependencies with uv (https://docs.astral.sh/uv/).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if ! command -v uv >/dev/null 2>&1; then
  echo "uv not found. Install with:"
  echo "  curl -LsSf https://astral.sh/uv/install.sh | sh"
  echo "Then ensure ~/.local/bin is on your PATH."
  exit 1
fi

uv sync
echo ""
echo "Done. Run scripts with:"
echo "  uv run python scripts/sync_json_to_sheet.py --dry-run"
echo ""
echo "Credentials:"
echo "  export GOOGLE_APPLICATION_CREDENTIALS=\"\$PWD/scripts/secrets/service-account.json\""
