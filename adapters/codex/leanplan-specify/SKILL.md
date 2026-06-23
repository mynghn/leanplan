---
name: leanplan-specify
description: LeanPlan — derive a Spec from existing Requirements in Codex. Use for `leanplan-specify <KEY>` or when asked to run the LeanPlan Spec stage.
---

# leanplan-specify

LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work. This skill drives the Spec stage (Requirements -> Spec edge).

Resolve `<LEANPLAN_ROOT>` as the LeanPlan checkout containing this adapter: follow the real path of this `SKILL.md` from the installed skill symlink when present, then walk up three directories from `adapters/codex/<skill>/`. Substitute that absolute path wherever commands below use `<LEANPLAN_ROOT>`.

Load `<LEANPLAN_ROOT>/references/specify.md` — it is authoritative for the procedure, generic-category tech guard, B/C split, and Research archive rule. Load these on demand, not up front (context-engineering: jit-loading):

- `<LEANPLAN_ROOT>/references/artifact-contract.md` — before writing or editing an artifact's structure or anchors: feature layout, `B-<N>` / `C-<N>` anchors, drift guards, traceability.
- `<LEANPLAN_ROOT>/references/philosophy.md` — when a principle's intent or grounding is in question.

Runtime glue:

- **Input** — `<cwd>/docs/features/<KEY>/requirements.md`; if absent, stop and point the user to `leanplan-requirements`.
- **Validate** — `python3 <LEANPLAN_ROOT>/scripts/validate.py <cwd>/docs/features/<KEY> --stage spec`.
- **Hand off** — next move is `leanplan-design <KEY>`.
