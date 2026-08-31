---
slug: my-feature-slug
mode: feature
date: 2026-01-01
status: draft
---

<!--
  Brief template — the input contract for a design (plan-mode) session.
  Produced by the /kickoff interview skill; consumed by whoever designs the feature next.

  Copy this file to docs/architecture/briefs/<slug>.md and fill every section, then delete this
  comment. Frontmatter: slug is kebab-case; mode is `kickoff` or `feature`; date is today
  (YYYY-MM-DD). Keep it tight (1-2 pages). Record genuinely unresolved items under Open
  Questions rather than inventing answers. Do NOT make architecture/stack decisions here —
  capture constraints and preferences; the design session decides the design.
-->

# Brief: short title

## 1. Executive summary & goals (the "Why")

_2-4 sentences: the problem being solved and the user value. State the MVP success
metrics — how we will know this succeeded._

## 2. User personas & workflows

_Who benefits, and the specific journey each takes through the system. Bullet
persona-to-workflow mappings._

## 3. Scope & non-goals

- **In scope:** _what this work covers_
- **Explicit non-goals:** _what this work deliberately does NOT cover — the most valuable
  section for preventing scope creep in the design_

## 4. Functional requirements

| ID   | Feature | Description | Priority | Dependencies |
| ---- | ------- | ----------- | -------- | ------------ |
| FR-1 | ...     | ...         | P0       | —            |
| FR-2 | ...     | ...         | P1       | FR-1         |

_Priority is P0 (must-have for this increment) or P1 (nice-to-have). Dependencies
reference other FR IDs — useful if the design session needs to sequence the work._

## 5. Non-functional requirements & constraints

- **Performance / scale:** _latency, throughput, data-volume targets, or "not a concern"_
- **Deployment target:** _Windows, Linux, or both — and any packaging implications for the
  PyInstaller build_
- **Security / privacy / compliance:** _auth, data handling, or "none"_
- **Stack constraints & preferences (captured, not decided):** _e.g. "must stay in the
  standard library plus what's already a dependency", "must work headless for tests".
  Leave actual architecture/library choices to the design session._

## 6. Edge cases & error states (the "What if")

- _Failure / offline behavior (e.g. lost serial/socket/SSH connection)_
- _Fault tolerance and fallbacks_
- _Malicious inputs, race conditions, or abuse cases_

## 7. Risks & mitigations

- **Risk:** _description_ — **Mitigation:** _how we reduce or accept it_

## 8. Acceptance criteria (mandatory)

_Concrete, testable statements that define "done" for this work. Prefer checklist form._

- [ ] _criterion_
- [ ] _criterion_

## 9. Open questions / assumptions

_Anything unresolved at the end of the interview, and any assumptions made. If the
interview ended early, list what is missing here so the design session knows the gaps._
