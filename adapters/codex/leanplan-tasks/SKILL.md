---
name: leanplan-tasks
description: LeanPlan — produce a Tasks artifact from a Design in Codex. Use for `leanplan-tasks <KEY>` or when asked to run the LeanPlan Tasks stage.
---

# leanplan-tasks

LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work. This skill drives the Tasks stage (Design -> tasks.md edge).

Resolve `<LEANPLAN_ROOT>` as the LeanPlan checkout containing this adapter: follow the real path of this `SKILL.md` from the installed skill symlink when present, then walk up three directories from `adapters/codex/<skill>/`. Substitute that absolute path wherever commands below use `<LEANPLAN_ROOT>`.

Load `<LEANPLAN_ROOT>/references/tasks.md` — it is authoritative for the procedure, DAG shape, task-card fields, bidirectional verification, and one-deployment guardrail. Load these on demand, not up front (context-engineering: jit-loading):

- `<LEANPLAN_ROOT>/references/artifact-contract.md` — before writing or editing an artifact's structure or anchors: Tasks shape, `T: <id>` anchors, traceability, `**GAP**` semantics.
- `<LEANPLAN_ROOT>/references/philosophy.md` — when a principle's intent or grounding is in question.

Runtime glue:

- **Input** — `<cwd>/docs/features/<KEY>/design.md`; if absent, stop and point the user to `leanplan-design`.
- **Output** — `<cwd>/docs/features/<KEY>/tasks.md`.
- **Validate** — `python3 <LEANPLAN_ROOT>/scripts/validate.py <cwd>/docs/features/<KEY> --stage tasks`.
- **Hand off** — for each independently startable task: `leanplan-implement <KEY> <task-id>`.
