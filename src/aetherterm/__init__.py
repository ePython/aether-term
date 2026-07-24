"""aetherterm — cross-platform serial / socket / telnet / SSH terminal.

Its distinctive feature (to be built) is a configurable frame of paged button
grids beneath the terminal, each button launching an automation script against
network or serial devices.
"""

from __future__ import annotations

try:
    # Written by hatch-vcs at build time; present after `uv sync`.
    from aetherterm._version import __version__
except ImportError:  # pragma: no cover - source checkout before first build
    from importlib.metadata import PackageNotFoundError, version

    try:
        __version__ = version("aetherterm")
    except PackageNotFoundError:
        __version__ = "0.0.0.dev0+unknown"

__all__ = ["__version__"]
