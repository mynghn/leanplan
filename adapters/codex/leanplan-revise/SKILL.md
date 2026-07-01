---
name: leanplan-revise
description: LeanPlan — inject a justified drift into committed artifacts in Codex and propagate downstream only. Use for `leanplan-revise <KEY> [Delta-N | what drifted]`.
---

# leanplan-revise

LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work. This skill runs the off-pipeline revise move.

Resolve `LP_ROOT` as the LeanPlan checkout containing this adapter: follow the real path of this `SKILL.md` from the installed skill symlink when present, then walk up three directories from `adapters/codex/<skill>/`. Later `references/...` and `scripts/...` paths are relative to `LP_ROOT`; when running a command, use the shell form `"$LP_ROOT/..."`.

Load `references/revise.md` from `LP_ROOT` — it is authoritative for intake, justified mutation, highest-affected-layer selection, downstream-only propagation, and validation. Load these on demand, not up front (context-engineering: jit-loading):

- `references/artifact-contract.md` from `LP_ROOT` — before editing artifact structure or anchors: anchor patterns and retire-by-note (traceability lives in `references/tasks.md`; the `Delta-<N>` shape in `references/rethink.md`).
- `references/philosophy.md` from `LP_ROOT` — when a principle's intent or grounding is in question.

Runtime glue:

- **Target** — the argument names `<KEY>` and optionally a recorded `Delta-<N>` or drift text.
- **Justification** — mutate only against a `Delta-<N>` block in `docs/features/<KEY>/understanding-shifts.md`; record one from the planner's asserted drift before any edit when needed.
- **Edit scope** — edit the corrected artifact and implicated downstream artifacts only; upstream artifacts stay unchanged.
- **Validate** — after propagation, run `"$LP_ROOT/scripts/leanplan-validate" docs/features/<KEY>` or stage-scope if downstream artifacts are not authored yet.
