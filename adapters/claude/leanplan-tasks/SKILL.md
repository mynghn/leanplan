---
name: leanplan-tasks
description: LeanPlan — produce a Tasks tasks.md from a Design. Track subgraphs, prefixed task IDs, bidirectional verification against Spec + Design.
argument-hint: "<feature-key>"
allowed-tools: Read, Write, Edit, Grep, Glob, AskUserQuestion, Bash(ls *), Bash(mkdir *), Bash(git *), Bash(*/scripts/leanplan-validate *)
---

# leanplan tasks
LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work. This skill drives the Tasks stage (Design → `tasks.md` edge).

Resolve `LP_ROOT` as the LeanPlan checkout containing this adapter: follow the real path of this `SKILL.md` from the installed skill symlink when present, then walk up three directories from `adapters/claude/<skill>/`. Later `references/...` and `scripts/...` paths are relative to `LP_ROOT`; when running a command, use the shell form `"$LP_ROOT/..."`.

Load `references/tasks.md` from `LP_ROOT` — it is authoritative for the procedure + template (track-prefixed task IDs P/A/D/I, enabler-not-gate dependency wording, bidirectional verification, advisory one-deployment guardrail). Load these on demand, not up front (context-engineering: jit-loading):

- `references/artifact-contract.md` from `LP_ROOT` — **before writing or editing an artifact's structure or anchors**: Tasks shape (Guidelines, Dependency DAG, task cards), `T: <id>` anchor pattern, traceability rules with `**GAP**` ack semantics.
- `references/philosophy.md` from `LP_ROOT` — **when a principle's intent or grounding is in question**: the framework principles shaping what "good" looks like.

Runtime glue:

- **Output** — `<cwd>/docs/features/<KEY>/tasks.md` (the filename is `tasks.md`, not `task.md`).
- **Validate** — `"$LP_ROOT/scripts/leanplan-validate" <cwd>/docs/features/<KEY> --stage tasks`.
- **Hand off** — for each independently startable task, `/leanplan-implement <KEY> <task-id>`.
