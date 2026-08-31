---
name: ship
description: Land a completed change on aetherterm's main branch — branch, Conventional-Commit + changelog entry, push, open a PR, and (once approved) squash-merge, delete the branch, and verify it actually landed. Use when the user asks to commit/push/open a PR for finished work, or says "ship this" / "land this change".
---

# Landing a change on `aetherterm`

This is a manual checklist, not an autonomous process — every push, PR, and
merge is outward-facing, so **confirm with the user before each of those
three actions** rather than running the whole sequence unattended. The remote
is plain GitHub (`github.com/ePython/aether-term`); the `gh` CLI is assumed
installed and authenticated.

## The one rule that prevents messes: never stack

Branch every change from a fresh `main`, and land it into `main` before
starting the next one. Never branch off another in-flight branch, and never
have two PRs open against `main` at once for related work.

## Lifecycle

1. **Sync & branch.** `git fetch origin`; confirm you're branching from
   `origin/main`: `git switch -c <type>/<slug> origin/main` (prefixes:
   `feature/`, `fix/`, `docs/`, `chore/`). If a branch or open PR for this
   work already exists, stop and use that instead of creating a duplicate.

1. **Commit.** Inspect `git status` / `git diff --staged` — stage specific
   files, not `-A`. Write a Conventional Commit subject + body (`feat:`,
   `fix:`, `docs:`, `refactor:`, `test:`, `chore:`). Add a matching
   `## [Unreleased]` entry to `CHANGELOG.md` (Keep a Changelog: Added /
   Changed / Fixed / Removed) if the change is user-facing. **Confirm with
   the user before committing.** Pre-commit hooks run on commit — if one
   fails, fix the underlying issue and re-stage; never `--no-verify`.

1. **Push.** `git push -u origin <type>/<slug>`. **Confirm with the user
   first** — this is the first point the change becomes visible to others.

1. **Verify gates green.** Run `uv run poe check`. If anything is red, stop
   and fix it (or hand off to debugging) before opening a PR — never open or
   merge a PR on red gates.

1. **Open PR.** `gh pr create --base main --head <type>/<slug> --title "…"
   --body "…"`. **Confirm with the user first.**

1. **Merge — only after the user says to.** This repo has no auto-merge
   policy; wait for explicit approval (a review, or the user saying "merge
   it") before running:

   ```bash
   gh pr merge <n> --squash --delete-branch
   ```

   Squash keeps `main` linear — one commit per change. Never use a merge
   commit or rebase-merge here.

1. **Verify it actually landed** — a PR showing "MERGED" is not proof by
   itself:

   ```bash
   git fetch origin --prune
   git log --oneline origin/main -5
   ```

   Confirm the branch is gone locally and remotely, and
   `gh pr list --state open` doesn't show it anymore.

1. **Report** the merge commit on `main` and the verification result.

## Hard stops — surface to the user, do not improvise

- Merge conflict, non-fast-forwardable state, or a PR that isn't mergeable.
- A gate failure you can't resolve quickly.
- Any push/merge rejection (branch protection, required reviews, auth).
- Anything that would require a **force-push** or **rewriting `main`
  history** — never do this.
- Deleting a branch not confirmed merged into `main` — never do this.

## Boundaries

- Only ever operate on `<type>/* → main` in **this** repo. Never touch `main`
  directly, other branches, or other repositories.
- Keep secrets out of commit messages, PR bodies, and history.
- Tagging a release is the `/release` skill's job, not this one.
