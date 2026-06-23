---
name: leanplan-design
description: LeanPlan — realize a Spec into a Design (chosen components, stack, decisions). Architecture diagram + per-decision blocks; archive rationale for non-trivial decisions.
argument-hint: "<feature-key>"
allowed-tools: Read, Write, Edit, Grep, Glob, AskUserQuestion, Agent, Bash(ls *), Bash(mkdir *), Bash(git *), Bash(python3 ~/.local/share/leanplan/scripts/validate.py *), WebFetch, WebSearch, mcp__atlassian__getJiraIssue, mcp__atlassian__searchJiraIssuesUsingJql
---

# leanplan design

LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work. This skill drives the Design stage (Spec → Design edge).

Load `~/.local/share/leanplan/references/design.md` — it is authoritative for the procedure + template (Architecture-first rule, non-trivial-only rationale anchoring, Spec B/C coverage check with Tasks-direct realization path for trivial items). Load these on demand, not up front (context-engineering: jit-loading):

- `~/.local/share/leanplan/references/artifact-contract.md` — **before writing or editing an artifact's structure or anchors**: Design shape, `D-<N>: <slug>` anchor pattern, free-form Rationale rule, Research-as-evidence rule.
- `~/.local/share/leanplan/references/philosophy.md` — **when a principle's intent or grounding is in question**: the framework principles shaping what "good" looks like.

Runtime glue:

- **Missing input** — if `<cwd>/docs/features/<KEY>/spec.md` is absent, stop and point the user to `/leanplan-specify` (see `design.md` Inputs).
- **Validate** — `python3 ~/.local/share/leanplan/scripts/validate.py <cwd>/docs/features/<KEY> --stage design`.
- **Hand off** — next edge is `/leanplan-tasks <KEY>`.
