"""Smoke tests: the package imports, is versioned, and exposes the GUI entry."""

from __future__ import annotations

import aetherterm


def test_package_importable() -> None:
    assert aetherterm is not None


def test_version_is_readable() -> None:
    assert isinstance(aetherterm.__version__, str)
    assert aetherterm.__version__


def test_gui_entry_point_callable() -> None:
    from aetherterm.gui import main

    assert callable(main)
