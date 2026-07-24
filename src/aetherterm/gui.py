"""GUI entry point.

Intentionally a minimal stub: no widgets, terminal emulation, or scripting
engine yet — only the single launch surface that the installed ``aetherterm``
gui-script, ``python -m aetherterm``, and the frozen PyInstaller executable all
call. The real Tkinter application will be constructed inside :func:`main`.
"""

from __future__ import annotations

from aetherterm import __version__


def main() -> int:
    """Launch the aetherterm GUI. Returns a process exit code."""
    # Placeholder — the Tkinter root window and button-grid frame go here.
    print(f"aetherterm {__version__} — GUI entry point (stub).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
