---
name: requirements
description: LeanPlan — author a Requirements artifact for a feature. Interactive extraction of a feature's Problem + Outcome (no implementation choices); the entry stage — no upstream artifact required.
argument-hint: "[brief intent | PROJ-123 | --date intent | id to revise]"
allowed-tools: Read, Write, Edit, AskUserQuestion, Bash(*/scripts/leanplan-new *), Bash(*/scripts/leanplan-validate *), Bash(ls *), mcp__atlassian__getJiraIssue, mcp__atlassian__searchJiraIssuesUsingJql, mcp__claude_ai_Slack__slack_read_thread, mcp__claude_ai_Slack__slack_read_channel
---

# requirements
LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work. This skill drives the Requirements stage.

Resolve `<LEANPLAN_ROOT>` as the LeanPlan checkout containing this adapter: follow the real path of this `SKILL.md` from the installed skill symlink when present, then walk up three directories from `adapters/claude/<skill>/`. Substitute that absolute path wherever commands below use `<LEANPLAN_ROOT>`.

Load `<LEANPLAN_ROOT>/references/requirements.md` — it is authoritative for the procedure, guardrails, and template. Load these on demand, not up front (context-engineering: jit-loading):

- `<LEANPLAN_ROOT>/references/artifact-contract.md` — **before writing or editing an artifact's structure or anchors**: feature layout, anchor patterns, drift guards, traceability rules.
- `<LEANPLAN_ROOT>/references/philosophy.md` — **when a principle's intent or grounding is in question**: the framework principles shaping what "good" looks like.

Runtime glue:

- **Allocator** — `<LEANPLAN_ROOT>/scripts/leanplan-new` is the single directory allocator: capture its stdout path, stop on non-zero, never `mkdir`. The id-form choice (sequence / tracker-key / date) lives in `requirements.md` Procedure step 1.
- **Upstream MCP tools** — the granted Jira / Slack tools fetch upstream context per Procedure step 2.
- **Validate** — `<LEANPLAN_ROOT>/scripts/leanplan-validate <captured-path> --stage requirements`.
- **Hand off** — next edge is `/specify <KEY>`.
