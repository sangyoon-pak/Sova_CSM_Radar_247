#!/usr/bin/env python3
"""Clear all values saved via Configure (app_settings keys in RUNTIME_CONFIGURE_KEYS).

After this, runtime uses built-in defaults from ``src/config.py`` plus any variables
exported in the process environment.

Usage (from repo root, venv active):
  .venv/bin/python scripts/reset_configure_overrides.py
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.runtime_config import (  # noqa: E402
    clear_gog_local_oauth_files,
    clear_runtime_configure_overrides,
)


def main() -> None:
    gc = clear_gog_local_oauth_files()
    clear_runtime_configure_overrides()
    n = len(gc.get("removed") or [])
    print("Configure database overrides cleared. Restart the server if it is running.")
    if gc.get("home"):
        print(f"gog OAuth files under {gc['home']}: removed {n} path(s).")
        for err in gc.get("errors") or []:
            print(f"  warning: {err}")


if __name__ == "__main__":
    main()
