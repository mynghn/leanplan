---
name: leanplan-tasks
description: LeanPlan — produce a Tasks artifact from a Design in Codex. Use for `leanplan-tasks <KEY>` or when asked to run the LeanPlan Tasks stage; also accepts routed `leanplan tasks <KEY>`.
---

# leanplan-tasks

LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work. This skill drives the Tasks stage (Design -> tasks.md edge).

Load `~/.local/share/leanplan/references/tasks.md` — it is authoritative for the procedure, DAG shape, task-card fields, bidirectional verification, and one-deployment guardrail. Load these on demand, not up front (context-engineering: jit-loading):

- `~/.local/share/leanplan/references/artifact-contract.md` — before writing or editing an artifact's structure or anchors: Tasks shape, `T: <id>` anchors, traceability, `**GAP**` semantics.
- `~/.local/share/leanplan/references/philosophy.md` — when a principle's intent or grounding is in question.

Runtime glue:

- **Input** — `<cwd>/docs/features/<KEY>/design.md`; if absent, stop and point the user to `leanplan-design`.
- **Output** — `<cwd>/docs/features/<KEY>/tasks.md`.
- **Validate** — `python3 ~/.local/share/leanplan/scripts/validate.py <cwd>/docs/features/<KEY> --stage tasks`.
- **Hand off** — for each independently startable task: `leanplan-implement <KEY> <task-id>`; compatibility router form is `leanplan implement <KEY> <task-id>`.
