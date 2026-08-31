# Contributing

Thank you for your interest in contributing!

Key points:

- Follow the environment/tooling conventions in [CLAUDE.md](CLAUDE.md) —
  everything goes through `uv`; there is no other supported way to install,
  test, lint, or build this project.
- Ensure `uv run poe check` passes before opening a pull request.
- Update `CHANGELOG.md` under `[Unreleased]` for any user-facing change.
- Do not hand-edit version numbers or `src/aetherterm/_version.py` — versions
  come from Git tags via `hatch-vcs` (see the Versioning section of
  [CLAUDE.md](CLAUDE.md)).

By contributing you agree that your contributions will be licensed under the
[Apache License, Version 2.0](LICENSE).
