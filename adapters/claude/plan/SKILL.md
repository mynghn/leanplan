---
name: plan
description: LeanPlan — produce a TASK plan.md from a DESIGN. Track subgraphs, prefixed task IDs, bidirectional verification against SPEC + DESIGN.
argument-hint: "<feature-key>"
allowed-tools: Read, Write, Edit, Grep, Glob, AskUserQuestion, Bash(ls *), Bash(mkdir *), Bash(git *)
---

# plan

LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work in monorepos. This skill drives the TASK stage (DESIGN → `plan.md` edge).

Load `~/.local/share/leanplan/references/plan.md` — the stage procedure + template (track-prefixed task IDs P/A/D/I, enabler-not-gate dependency wording, bidirectional verification, advisory one-deployment guardrail). Load these on demand, not up front (CE: jit-loading):

- `~/.local/share/leanplan/references/artifact-contract.md` — **before writing or editing an artifact's structure or anchors**: TASK shape (Guidelines, Dependency DAG, Task cards), `Task: <id>` anchor pattern, traceability rules with `**GAP**` ack semantics.
- `~/.local/share/leanplan/references/philosophy.md` — **when a principle's intent or grounding is in question**: the framework principles shaping what "good" looks like.

Output: `<cwd>/docs/features/<KEY>/plan.md` (filename is `plan.md`, not `task.md`). Validate after writing with `python3 ~/.local/share/leanplan/scripts/validate.py <cwd>/docs/features/<KEY> --stage plan`.

After writing, hand off: for each independently startable task, `/impl <KEY> <task-id>`.
