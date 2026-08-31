# Briefs

A **brief** is the artifact that seeds a design session for a new feature or change. It is
produced by the `/kickoff` interview skill and consumed by whoever designs the feature next
— a human, or Claude in plan mode, working from the brief's path. It is the **seam**
between the human and the design work.

## Why briefs exist

Design quality depends on the prompt that seeds it. A vague request produces a vague plan.
The `/kickoff` interview fixes this by forcing the right detail out of the user up front,
and recording it here as a structured contract, so the design session can focus on
architecture instead of interrogating the user about scope.

## How the seam works

1. **Interview (its own session).** The user runs `/kickoff`. The interview is
   conversational and can be long; keeping it in a separate session preserves whatever
   session designs the feature from having to wade through the back-and-forth.
2. **Brief (this directory).** The interview writes `docs/architecture/briefs/<slug>.md` from
   [`TEMPLATE.md`](TEMPLATE.md). The user reviews and edits it — **gate 1**.
3. **Design (fresh session).** Start a new session and design against the brief's
   **path** — plan mode is a good fit here. Significant or irreversible decisions from that
   session get written up as an ADR under `../adr/` (see its template). If this is the
   first real feature, this is also when `docs/srs/software-requirements-specification.md`
   gets filled in from its `[TBD]` placeholder. The user reviews the design — **gate 2**.
4. **Implementation.** Build against the reviewed design.

## Modes

Each brief declares a `mode`:

- `kickoff` — a new project or a large new capability.
- `feature` — a smaller change (often surfaced during manual testing).

The distinction matters less here than it would with a phased roadmap — aetherterm doesn't
run one — but it's still useful context for the design session about how big a swing this
is.

## Conventions

- One brief per file, named `docs/architecture/briefs/<slug>.md` with a short kebab-case
  slug.
- Briefs are internal working contracts, not published documentation. They live under
  `docs/architecture/` alongside the ADRs and overview (so mkdocs can serve those as real
  pages), but `mkdocs.yml`'s `exclude_docs` keeps this specific folder out of the built
  site.
- Keep a brief tight — a 1-2 page contract, not a full PRD.
