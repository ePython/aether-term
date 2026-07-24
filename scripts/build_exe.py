"""Cross-platform helper to build the single-file GUI executable.

Equivalent to ``uv run poe build-exe``; kept as a script for CI reuse and for
contributors who prefer ``uv run python scripts/build_exe.py``.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

SPEC = Path(__file__).resolve().parent.parent / "aetherterm.spec"


def main() -> int:
    return subprocess.call(
        [sys.executable, "-m", "PyInstaller", str(SPEC), "--noconfirm", "--clean"]
    )


if __name__ == "__main__":
    raise SystemExit(main())
