---
name: release
description: Execute the aetherterm release process — verify gates, roll the changelog, create the vX.Y.Z git tag that drives the version, and verify it resolves. Use when cutting a release or when the user asks to release/tag a version.
---

# Release process for `aetherterm`

Versions are **derived from git tags** by `hatch-vcs`, which generates
`src/aetherterm/_version.py` at build time. That file is git-ignored and must
never be hand-edited — there is no version string in `pyproject.toml` to
bump. Follow [SemVer](https://semver.org/): `MAJOR.MINOR.PATCH`.

## Preconditions (check first)

- On `main` with a clean working tree (`git status`).
- `## [Unreleased]` in `CHANGELOG.md` describes the changes to ship.
- Decide the new version `X.Y.Z` from the nature of the unreleased changes
  (SemVer).

## Steps

1. **Verify gates — must be green before anything else.**

   ```bash
   uv run poe check
   ```

   If red, stop and fix the underlying issue (see the failing gate's output)
   before continuing. Do not release on failing gates.

1. **Roll the changelog.** Move the `## [Unreleased]` entries under a new
   heading with today's date, and leave a fresh empty `## [Unreleased]` at
   the top:

   ```markdown
   ## [X.Y.Z] - YYYY-MM-DD
   ```

1. **Commit the changelog** — confirm with the user before committing, since
   this is the start of an outward-facing release sequence:

   ```bash
   git commit -am "chore: release vX.Y.Z"
   ```

1. **Tag the release** (the tag is the version):

   ```bash
   git tag vX.Y.Z
   ```

1. **Verify the version resolves** against the tag. There is no
   `scripts/check_version.py` in this repo (yet) — verify manually:

   ```bash
   uv sync --reinstall-package aetherterm
   uv run python -c "import aetherterm; print(aetherterm.__version__)"
   ```

   Confirm the printed version matches `X.Y.Z` exactly. See CLAUDE.md's
   Versioning section for why the `--reinstall-package` flag is needed here —
   plain `uv sync` doesn't always regenerate `_version.py` after tagging.

1. **Push — pause for confirmation first.** Pushing is outward-facing;
   confirm with the user before running:

   ```bash
   git push origin main --follow-tags
   ```

1. **Build the executable** as needed:

   ```bash
   uv run poe build-exe
   ```

   (`dist/aetherterm.exe` on Windows, `dist/aetherterm` on Linux.) CI also
   builds this automatically on `v*` tag pushes and uploads it as a workflow
   artifact — a local build is only needed if you want the artifact sooner
   than CI produces it.

## Notes

- Never push or tag without green gates and a matching changelog section.
- Commit messages follow Conventional Commits; the release commit is
  `chore: release vX.Y.Z`.
- If `docs/` tooling (`poe docs`) is wired in later, consider adding a docs
  build to this checklist too — it isn't part of the release process yet.
