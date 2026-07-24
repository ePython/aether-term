"""Allow ``python -m aetherterm`` to launch the GUI."""

from __future__ import annotations

from aetherterm.gui import main

if __name__ == "__main__":
    raise SystemExit(main())
