# aetherterm

Cross-platform (Windows + Linux) serial / socket / telnet / SSH terminal
application. Its distinguishing feature is a configurable frame of paged
button grids beneath the main terminal window, where each button launches an
automation script against network or serial devices.

> **Status:** early scaffold. No business logic, GUI widgets, terminal
> emulation, or scripting engine has been implemented yet — this repository
> currently provides the packaging, tooling, and launch-surface skeleton only.

## Requirements

- Python 3.12.x
- [`uv`](https://docs.astral.sh/uv/) for environment and dependency management
- Linux only: the system Tk package (e.g. `sudo apt install python3-tk`) for
  the stdlib Tkinter GUI toolkit

## Installation

Install as a library/tool into your own environment:

```bash
uv tool install .
aetherterm
```

Or, as an editable dependency inside another `uv` project:

```bash
uv add --editable /path/to/aether-term
```

## Development

Clone the repo, then set up the environment:

```bash
uv sync                    # creates .venv, installs the package + dev tools
uv run pre-commit install  # wires up the pre-commit hooks
```

Run the app from source:

```bash
uv run aetherterm      # via the installed gui-script
uv run python -m aetherterm  # equivalent, via module execution
```

### Quality gates

All tooling is configured in `pyproject.toml` and invoked through
[`poethepoet`](https://poethepoet.natn.io/) tasks:

| Command                   | What it does                                 |
| ------------------------- | -------------------------------------------- |
| `uv run poe lint`         | Ruff lint                                    |
| `uv run poe format`       | Ruff format (writes changes)                 |
| `uv run poe format-check` | Ruff format check (no writes)                |
| `uv run poe typecheck`    | Mypy, strict mode                            |
| `uv run poe test`         | Pytest                                       |
| `uv run poe cov`          | Pytest with coverage (terminal + XML report) |
| `uv run poe md`           | mdformat (writes changes)                    |
| `uv run poe md-check`     | mdformat check (no writes)                   |
| `uv run poe check`        | All of the above gates, in sequence          |

## Building the executable

A single-file, windowed GUI executable is built with PyInstaller via the
checked-in `aetherterm.spec`:

```bash
uv run poe build-exe
```

This is equivalent to:

```bash
uv run pyinstaller aetherterm.spec --noconfirm --clean
```

The output is written to `dist/aetherterm.exe` (Windows) or `dist/aetherterm`
(Linux). Double-clicking / running the executable launches the GUI directly —
no console window is attached.

On Linux, make sure the system Tk package is installed in the build
environment before freezing (`sudo apt install python3-tk` or your
distribution's equivalent).

## Releasing

Versioning is dynamic, derived from Git tags via `hatch-vcs` — there is no
version string to bump by hand. To cut a release:

```bash
git tag v0.2.0
git push --tags
```

A fresh clone, CI run, or `uv run poe build-exe` picks up `0.2.0` automatically
(readable at runtime as `aetherterm.__version__`, and baked into the frozen
executable). In an **existing local checkout**, `uv sync` alone may not
notice the new tag if no source files changed since the last sync — force a
rebuild with:

```bash
uv sync --reinstall-package aetherterm
```

See [CLAUDE.md](CLAUDE.md) for the full contributor/agent workflow reference.

## License

Apache License 2.0 — see [LICENSE](LICENSE).
