---
name: requirement
description: LeanPlan — author a REQUIREMENT artifact for a feature. Interactive extraction of world-only Problem + Outcome (no implementation); standalone edge.
argument-hint: "[brief problem intent | PROJ-123 | --date intent | id to revise]"
allowed-tools: Read, Write, Edit, AskUserQuestion, Bash(~/.local/share/leanplan/scripts/leanplan-new *), Bash(python3 ~/.local/share/leanplan/scripts/validate.py *), Bash(ls *), mcp__atlassian__getJiraIssue, mcp__atlassian__searchJiraIssuesUsingJql, mcp__claude_ai_Slack__slack_read_thread, mcp__claude_ai_Slack__slack_read_channel
---

# requirement

LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work. This skill drives the REQUIREMENT stage.

Load `~/.local/share/leanplan/references/requirement.md` — it is authoritative for the procedure, guardrails, and template. Load these on demand, not up front (context-engineering: jit-loading):

- `~/.local/share/leanplan/references/artifact-contract.md` — **before writing or editing an artifact's structure or anchors**: feature layout, anchor patterns, drift guards, traceability rules.
- `~/.local/share/leanplan/references/philosophy.md` — **when a principle's intent or grounding is in question**: the framework principles shaping what "good" looks like.

Runtime glue:

- **Allocator** — `~/.local/share/leanplan/scripts/leanplan-new` is the single directory allocator: capture its stdout path, stop on non-zero, never `mkdir`. The id-form choice (sequence / tracker-key / date) lives in `requirement.md` Procedure step 1.
- **Upstream MCP tools** — the granted Jira / Slack tools fetch upstream context per Procedure step 2.
- **Validate** — `python3 ~/.local/share/leanplan/scripts/validate.py <captured-path> --stage requirement`.
- **Hand off** — next edge is `/specify <KEY>`.
