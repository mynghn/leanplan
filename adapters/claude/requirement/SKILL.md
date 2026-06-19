---
name: requirement
description: LeanPlan — author a REQUIREMENT artifact for a feature. Interactive extraction of biz-only Problem + Outcome; standalone edge.
argument-hint: "[brief biz intent | PROJ-123 | --date intent | id to revise]"
allowed-tools: Read, Write, Edit, AskUserQuestion, Bash(~/.local/share/leanplan/scripts/leanplan-new *), Bash(ls *), mcp__atlassian__getJiraIssue, mcp__atlassian__searchJiraIssuesUsingJql, mcp__claude_ai_Slack__slack_read_thread, mcp__claude_ai_Slack__slack_read_channel
---

# requirement

LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work in monorepos. This skill drives the REQUIREMENT stage.

Load `~/.local/share/leanplan/references/requirement.md` — the stage procedure, guardrails, and template. Load these on demand, not up front (CE: jit-loading):

- `~/.local/share/leanplan/references/artifact-contract.md` — **before writing or editing an artifact's structure or anchors**: feature layout, anchor patterns, drift guards, traceability rules.
- `~/.local/share/leanplan/references/philosophy.md` — **when a principle's intent or grounding is in question**: the framework principles shaping what "good" looks like.

Tools above are Claude Code-specific. Resolve the feature by running `~/.local/share/leanplan/scripts/leanplan-new` (capture the path it prints on stdout; stop if it exits non-zero), then write `requirement.md` there — do not `mkdir` yourself. The id form follows `requirement.md` Procedure step 1: `leanplan-new "<slug-or-title>"` for a sequence `NNNN-slug` (default), `leanplan-new "<PROJ-123>"` for a bare tracker-key dir when the feature is anchored to a tracker item, or `leanplan-new --date "<slug-or-title>"` for a `YYMMDD-slug` date id. Jira / Slack MCP tools remain for *upstream context* per step 2 — when the tracker is only context, record it under `## Upstream`; when it is the feature id, that key is the identity. Validate at any time against the captured path, e.g. `python3 ~/.local/share/leanplan/scripts/validate.py docs/features/0007-anomaly-publisher --stage requirement`.

After writing, hand off: next edge is `/specify <KEY>`.
