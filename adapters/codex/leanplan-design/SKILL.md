---
name: leanplan-design
description: LeanPlan — realize a Spec into a Design in Codex. Use for `leanplan-design <KEY>` or when asked to run the LeanPlan Design stage.
---

# leanplan-design

LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work. This skill drives the Design stage (Spec -> Design edge).

Resolve `LP_ROOT` as the LeanPlan checkout containing this adapter: follow the real path of this `SKILL.md` from the installed skill symlink when present, then walk up three directories from `adapters/codex/<skill>/`. Later `references/...` and `scripts/...` paths are relative to `LP_ROOT`; when running a command, use the shell form `"$LP_ROOT/..."`.

Load `references/design.md` from `LP_ROOT` — it is authoritative for the procedure, architecture rule, decision blocks, rationale anchoring, and Spec coverage check. Load these on demand, not up front (context-engineering: jit-loading):

- `references/artifact-contract.md` from `LP_ROOT` — before writing or editing an artifact's structure or anchors: Design shape, `D-<N>` anchors, rationale shape, Research-as-evidence rule.
- `references/philosophy.md` from `LP_ROOT` — when a principle's intent or grounding is in question.

Runtime glue:

- **Input** — `<cwd>/docs/features/<KEY>/spec.md`; if absent, stop and point the user to `leanplan-specify`.
- **Validate** — `"$LP_ROOT/scripts/leanplan-validate" <cwd>/docs/features/<KEY> --stage design`.
- **Hand off** — next move is `leanplan-tasks <KEY>`.
