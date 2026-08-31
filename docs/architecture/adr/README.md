# Architecture Decision Records

This directory records the significant architectural decisions made on `aetherterm`.

An **Architecture Decision Record (ADR)** captures a single decision, its context, and its
consequences. ADRs are immutable once accepted: if a decision changes, write a new ADR that
supersedes the old one rather than editing history.

There are no ADRs yet — `aetherterm` is still a scaffold (see the project's `CLAUDE.md`).
The first ones will come out of the design session for the first real feature (the
button-grid GUI, a terminal I/O backend, or the scripting engine), typically following a
`/kickoff` interview brief (see `../briefs/`).

## Format

Each ADR follows the [template](template.md) and is named `NNNN-short-title.md`, where `NNNN` is a
zero-padded sequential number.

## Status values

| Status     | Meaning                                 |
| ---------- | --------------------------------------- |
| Proposed   | Under discussion, not yet agreed        |
| Accepted   | Agreed and in effect                    |
| Deprecated | No longer recommended, but not replaced |
| Superseded | Replaced by a later ADR (link to it)    |

## Index

_Empty — no decisions recorded yet._

## Creating a new ADR

1. Copy [template.md](template.md) to `NNNN-short-title.md` with the next number.
2. Fill in the sections; set the status to **Proposed**.
3. Once agreed, change the status to **Accepted** and add a row to the index above.
4. Use the `/docs-sync` skill afterward to check `../overview.md` and other docs are still
   consistent with the decision.
