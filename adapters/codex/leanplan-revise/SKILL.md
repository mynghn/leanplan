---
name: leanplan-revise
description: LeanPlan — inject a justified drift into committed artifacts in Codex and propagate downstream only. Use for `leanplan-revise <KEY> [Delta-N | what drifted]`.
---

# leanplan-revise

LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work. This skill runs the off-pipeline revise move.

Load `~/.local/share/leanplan/references/revise.md` — it is authoritative for intake, justified mutation, highest-affected-layer selection, downstream-only propagation, and validation. Load these on demand, not up front (context-engineering: jit-loading):

- `~/.local/share/leanplan/references/artifact-contract.md` — before editing artifact structure or anchors: anchor patterns, retire-by-note, traceability, and `Delta-<N>` shape.
- `~/.local/share/leanplan/references/philosophy.md` — when a principle's intent or grounding is in question.

Runtime glue:

- **Target** — the argument names `<KEY>` and optionally a recorded `Delta-<N>` or drift text.
- **Justification** — mutate only against a `Delta-<N>` block in `docs/features/<KEY>/understanding-shifts.md`; record one from the planner's asserted drift before any edit when needed.
- **Edit scope** — edit the corrected artifact and implicated downstream artifacts only; upstream artifacts stay unchanged.
- **Validate** — after propagation, run `python3 ~/.local/share/leanplan/scripts/validate.py docs/features/<KEY>` or stage-scope if downstream artifacts are not authored yet.
