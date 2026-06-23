---
name: leanplan-design
description: LeanPlan — realize a Spec into a Design in Codex. Use for `leanplan-design <KEY>` or when asked to run the LeanPlan Design stage.
---

# leanplan-design

LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work. This skill drives the Design stage (Spec -> Design edge).

Resolve `<LEANPLAN_ROOT>` as the LeanPlan checkout containing this adapter: follow the real path of this `SKILL.md` from the installed skill symlink when present, then walk up three directories from `adapters/codex/<skill>/`. Substitute that absolute path wherever commands below use `<LEANPLAN_ROOT>`.

Load `<LEANPLAN_ROOT>/references/design.md` — it is authoritative for the procedure, architecture rule, decision blocks, rationale anchoring, and Spec coverage check. Load these on demand, not up front (context-engineering: jit-loading):

- `<LEANPLAN_ROOT>/references/artifact-contract.md` — before writing or editing an artifact's structure or anchors: Design shape, `D-<N>` anchors, rationale shape, Research-as-evidence rule.
- `<LEANPLAN_ROOT>/references/philosophy.md` — when a principle's intent or grounding is in question.

Runtime glue:

- **Input** — `<cwd>/docs/features/<KEY>/spec.md`; if absent, stop and point the user to `leanplan-specify`.
- **Validate** — `<LEANPLAN_ROOT>/scripts/leanplan-validate <cwd>/docs/features/<KEY> --stage design`.
- **Hand off** — next move is `leanplan-tasks <KEY>`.
