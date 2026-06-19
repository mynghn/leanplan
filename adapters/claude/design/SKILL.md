---
name: design
description: LeanPlan — realize a SPEC into a DESIGN (chosen components, stack, decisions). Architecture diagram + per-decision blocks; archive rationale for non-trivial decisions.
argument-hint: "<feature-key>"
allowed-tools: Read, Write, Edit, Grep, Glob, AskUserQuestion, Agent, Bash(ls *), Bash(mkdir *), Bash(git *), WebFetch, WebSearch, mcp__atlassian__getJiraIssue, mcp__atlassian__searchJiraIssuesUsingJql
---

# design

LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work in monorepos. This skill drives the DESIGN stage (SPEC → DESIGN edge).

Load `~/.local/share/leanplan/references/design.md` — the stage procedure + template (Architecture-first rule, non-trivial-only rationale anchoring, SPEC O/INV coverage check with TASK-direct realization path for trivial items). Load these on demand, not up front (CE: jit-loading):

- `~/.local/share/leanplan/references/artifact-contract.md` — **before writing or editing an artifact's structure or anchors**: DESIGN shape, `Decision-<N>: <slug>` anchor pattern, free-form RATIONALE rule, RESEARCH-as-evidence rule.
- `~/.local/share/leanplan/references/philosophy.md` — **when a principle's intent or grounding is in question**: the framework principles shaping what "good" looks like.

If `<cwd>/docs/features/<KEY>/spec.md` is missing, stop and tell the user to run `/specify <KEY>` first. Inspect current code before choosing architecture — reality is authoritative. Validate after writing with `python3 ~/.local/share/leanplan/scripts/validate.py <cwd>/docs/features/<KEY> --stage design`.

After writing, hand off: next edge is `/plan <KEY>`.
