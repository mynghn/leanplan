---
name: design
description: LeanPlan — realize a Spec into a Design (chosen components, stack, decisions). Architecture diagram + per-decision blocks; archive rationale for non-trivial decisions.
argument-hint: "<feature-key>"
allowed-tools: Read, Write, Edit, Grep, Glob, AskUserQuestion, Agent, Bash(ls *), Bash(mkdir *), Bash(git *), Bash(*/scripts/leanplan-validate *), WebFetch, WebSearch, mcp__atlassian__getJiraIssue, mcp__atlassian__searchJiraIssuesUsingJql
---

# design

LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work. This skill drives the Design stage (Spec → Design edge).

Resolve `<LEANPLAN_ROOT>` as the LeanPlan checkout containing this adapter: follow the real path of this `SKILL.md` from the installed skill symlink when present, then walk up three directories from `adapters/claude/<skill>/`. Substitute that absolute path wherever commands below use `<LEANPLAN_ROOT>`.

Load `<LEANPLAN_ROOT>/references/design.md` — it is authoritative for the procedure + template (Architecture-first rule, non-trivial-only rationale anchoring, Spec B/C coverage check with Tasks-direct realization path for trivial items). Load these on demand, not up front (context-engineering: jit-loading):

- `<LEANPLAN_ROOT>/references/artifact-contract.md` — **before writing or editing an artifact's structure or anchors**: Design shape, `D-<N>: <slug>` anchor pattern, free-form Rationale rule, Research-as-evidence rule.
- `<LEANPLAN_ROOT>/references/philosophy.md` — **when a principle's intent or grounding is in question**: the framework principles shaping what "good" looks like.

Runtime glue:

- **Missing input** — if `<cwd>/docs/features/<KEY>/spec.md` is absent, stop and point the user to `/specify` (see `design.md` Inputs).
- **Validate** — `<LEANPLAN_ROOT>/scripts/leanplan-validate <cwd>/docs/features/<KEY> --stage design`.
- **Hand off** — next edge is `/tasks <KEY>`.
