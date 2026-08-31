---
name: docs-sync
description: Check and update aetherterm's documentation so it stays consistent with the code after a change lands — README, CLAUDE.md, docs/, docs/architecture/, and the CHANGELOG. Use after implementing a feature or fix, or when asked to sync/update the docs.
---

# Keeping `aetherterm`'s docs in sync

This is an on-demand checklist, not something to run automatically after every edit —
invoke it deliberately once a change is otherwise done (tests passing, `uv run poe check`
green), before landing it.

## What to check

- **`README.md`** — still describes what the project does and how to get started. Update
  if the change adds a real capability (this repo is scaffold-only today, so most changes
  won't touch this yet).
- **`CLAUDE.md`** — the **folder conventions** listing and the **task table** are the two
  sections most likely to drift: a new file/directory or a new `poe` task needs an entry
  here. Also check the "What this project is" / "What NOT to do" sections still describe
  reality once real features start landing.
- **`docs/index.md`** — the mkdocs site home page. Update once there's real user-facing
  content to point to (see its own note about populating `docs/` as features land).
- **`mkdocs.yml`** nav — if a new `docs/` page is added, it needs a nav entry or it won't
  be reachable in the built site (`uv run poe docs` after `uv sync --group docs` will still
  build it, but readers won't find it without a nav entry — mkdocs doesn't error on an
  orphan page).
- **`docs/architecture/overview.md`** — update when a design change affects the big
  picture; it's a real page in the site (`Architecture > Overview` in the nav).
- **`docs/architecture/adr/README.md`** — its index table should list every ADR once
  accepted; check it's not missing a recent one.
- **`docs/srs/software-requirements-specification.md`** — still a placeholder until the
  first real feature's design phase (see its banner). Once real requirements exist, keep
  its functional/non-functional sections in sync with what's actually been built, the same
  way you'd keep any other doc in sync.
- **`CHANGELOG.md`** `## [Unreleased]` — add an entry (Added / Changed / Fixed / Removed)
  for any user-facing change, if the `/ship` skill hasn't already added one.

## Boundaries

- Documentation and context files only — do not edit `src/` or `tests/` from this skill.
- Do not invent behavior; document only what the code actually does. If docs and code
  disagree, fix the doc to match the code (or flag the discrepancy to the user if it's
  unclear which one is wrong).
- If `uv sync --group docs` and `uv run poe docs` are available, run them after a nav
  change to confirm the site still builds clean.

## Method

1. Read the diff (`git diff`, `git status`) or the summary of what changed.
1. Walk the checklist above; edit only what's actually stale — don't pad out documentation
   for its own sake.
1. If `mkdocs.yml` nav changed, run `uv run poe docs` (after `uv sync --group docs` if not
   already synced) and confirm it builds without warnings.
