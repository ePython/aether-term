"""Smoke tests: the package imports, is versioned, and exposes the GUI entry."""

from __future__ import annotations

from typing import TYPE_CHECKING

import aetherterm

if TYPE_CHECKING:
    import pytest


def test_package_importable() -> None:
    assert aetherterm is not None


def test_version_is_readable() -> None:
    assert isinstance(aetherterm.__version__, str)
    assert aetherterm.__version__


def test_gui_entry_point_callable() -> None:
    from aetherterm.gui import main

    assert callable(main)


def test_gui_main_returns_success_exit_code(
    capsys: pytest.CaptureFixture[str],
) -> None:
    from aetherterm.gui import main

    assert main() == 0
    assert aetherterm.__version__ in capsys.readouterr().out


def test_dunder_main_module_imports() -> None:
    import aetherterm.__main__ as dunder_main

    assert dunder_main is not None
