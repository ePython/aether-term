---
name: kickoff
description: Conduct an interactive requirements-discovery interview and synthesize the result into a structured brief for the design phase. Use at the start of a new aetherterm feature (the button-grid GUI, a terminal I/O backend, the scripting engine, etc.) or a smaller change surfaced during manual testing. Run this in its own session before designing — it produces docs/architecture/briefs/<slug>.md, which the next session (typically plan mode) designs from.
---

# Feature kickoff interview for `aetherterm`

This skill runs an **interactive discovery interview** with the user and turns it into a
single reviewable artifact — a **brief** at `docs/architecture/briefs/<slug>.md` — that seeds
the design work that follows. The brief is the design session's **input contract**:
everything it needs to plan, and nothing it must guess.

## When and where to run this

- **Invoked explicitly** by the user typing `/kickoff`. Never auto-activate — aetherterm is
  deliberately scaffold-only right now (see `CLAUDE.md`), so don't suggest running this
  unless the user is actually about to start real feature work.
- **In its own session, before the design session.** Interviews are conversational and can
  be long; keeping them separate preserves the design session's context for the actual
  architecture work. See `docs/architecture/briefs/README.md` for the full seam.
- **Two modes**, recorded in the brief's `mode` field:
  - `kickoff` — a large new capability (e.g. the button-grid GUI, a terminal I/O backend).
  - `feature` — a smaller feature or change, typically surfaced while the user is manually
    testing an existing build.

## Your role during the interview

You are acting as a **requirements analyst** — not a designer and not an implementer. Your
job is to *elicit and pin down requirements*, then write them down. You do **not** design
the system, choose libraries/frameworks, or write code here.

- **Capture** stack constraints and preferences ("must stay cross-platform Windows+Linux",
  "must work headless in CI", "no new heavyweight GUI dependency") as *inputs*.
- **Do not decide** the architecture, module layout, or which library implements a given
  transport (serial/socket/telnet/SSH) — that's the design session's job.

## Interview rules (enforce these)

1. **One topic at a time.** Ask a single focused question per turn; batched questions
   dilute the answers. The exception is *confirming defaults* — it's fine to say "here's
   what I'm assuming, correct anything" and let the user react to several at once. Use
   `AskUserQuestion` when offering concrete choices with a recommended default.
1. **Challenge assumptions.** Do not passively transcribe. If an answer introduces a
   security flaw, a scaling bottleneck, hidden scope, or a contradiction, say so and offer
   an alternative. Front-loading this here means the design session can focus on
   architecture instead of re-litigating scope.
1. **Propose sensible defaults; don't interrogate.** Prefer "I'd default to X — ok?" over
   an open question the user has to answer cold. Aim for enough fidelity to design against,
   not an interrogation.
1. **No code, no architecture.** If the user asks for code or a design during the
   interview, remind them the brief must be locked first, then a fresh session designs.
1. **Show progress.** Begin each turn with a lightweight status marker, e.g.
   `[Pillar 3/5 · Constraints]`, so the user knows where you are.

## Discovery pillars

Guide the user through these five pillars in order, advancing only when the current one
has enough fidelity. They map directly onto the brief template sections.

1. **Intent & core value (the "Why")** — the problem being solved, the user personas who
   benefit, and the MVP success metrics.
1. **Functional requirements & workflows (the "What")** — the happy-path journey, critical
   integrations (serial/socket/telnet/SSH devices, the button-grid frame, the scripting
   engine), and data in/out. Capture these as discrete features in the FR matrix (each gets
   an ID, a priority, and dependencies).
1. **Non-functional & constraints (the "How well")** — performance/latency targets,
   Windows/Linux deployment target, security/privacy considerations, and any stack
   constraints/preferences (captured, not decided).
1. **Edge cases & error states (the "What if")** — lost-connection behavior, fault
   tolerance and fallbacks, malicious inputs, and race conditions.
1. **Scope alignment** — confirm explicit **non-goals**, and nail down **acceptance
   criteria** that define "done". Acceptance criteria are mandatory — they are what let
   the design session and reviewer define completion meaningfully.

## Knowing when to stop

Track coverage against the template. When every section can be filled with real content
(acceptance criteria included), **proactively offer to wrap**: "I think we have enough to
write the brief — shall I generate it?" The user may also end early at any time by saying
**"GENERATE BRIEF"** (or "STOP INTERVIEW"). If they stop before coverage is complete, still
generate the brief but record what's missing under **Open Questions**.

## Producing the brief

1. Read the template at `docs/architecture/briefs/TEMPLATE.md`.
1. Choose a short kebab-case `<slug>` for the work (e.g. `button-grid-gui`, `serial-backend`).
1. Write the completed brief to `docs/architecture/briefs/<slug>.md`, following the template
   exactly. Set the `mode` field (`kickoff` or `feature`) and today's date. Leave genuinely
   unresolved items under **Open Questions / Assumptions** rather than inventing answers.
1. Keep it tight — a 1-2 page contract, not a full PRD.

## Hand-off (do this at the end)

The brief is the seam; you do not design from it here. Tell the user, in plain terms:

- The brief is written to `docs/architecture/briefs/<slug>.md` — review and edit it before
  proceeding.
- To design it, **start a fresh session** and design against the **brief's path** (not its
  inlined contents) — plan mode is a good fit. Significant/irreversible decisions from that
  session should become an ADR under `docs/architecture/adr/` (copy `template.md`). If this is
  the first real feature, that's also the point to fill in
  `docs/srs/software-requirements-specification.md` from its placeholder.

Do not start designing or implementing from within this interview session.
