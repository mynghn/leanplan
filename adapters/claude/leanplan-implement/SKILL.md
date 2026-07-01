---
name: leanplan-implement
description: LeanPlan — implement one task card from tasks.md against current code. Re-reason at task entry, enforce stop-the-line triggers, distill non-obvious WHYs into durable code forms at close-out.
argument-hint: "<feature-key> <task-id>"
allowed-tools: Read, Write, Edit, Grep, Glob, AskUserQuestion, Agent, Bash(git *), Bash(./gradlew *), Bash(mise *), Bash(ls *), Bash(mkdir *), Bash(gh *), Bash(*/scripts/leanplan-validate *), Bash(*/scripts/scan-leaks *), mcp__atlassian__getJiraIssue, mcp__atlassian__addCommentToJiraIssue
---

# leanplan implement
LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work. This skill drives the implementation stage (one task card → landed code).

Resolve `LP_ROOT` as the LeanPlan checkout containing this adapter: follow the real path of this `SKILL.md` from the installed skill symlink when present, then walk up three directories from `adapters/claude/<skill>/`. Later `references/...` and `scripts/...` paths are relative to `LP_ROOT`; when running a command, use the shell form `"$LP_ROOT/..."`.

Load `references/implement.md` from `LP_ROOT` — it is authoritative for the procedure (the 6 stop-the-line triggers, artifact update loop walk-up, distillation hierarchy types → tests → annotations → commit → PR body → inline, squash-safe PR-body promotion rule). Load these on demand, not up front (context-engineering: jit-loading):

- `references/artifact-contract.md` from `LP_ROOT` — **before writing or editing an artifact's structure or anchors** (e.g. in the artifact update loop): anchor patterns and the cross-cutting authoring principles (traceability lives in `references/tasks.md`).
- `references/philosophy.md` from `LP_ROOT` — **when a principle's intent or grounding is in question**: framework principles shaping what "good" looks like.

Runtime glue:

- **Inputs** — `<cwd>/docs/features/<KEY>/tasks.md` and the chosen `T: <task-id>` card; JIT-load only the card's cited `B-<N>` / `C-<N>` / `D-<N>` blocks, not the whole Spec / Design.
- **Project comment discipline** — `CLAUDE.md` "default no comments" composes with the distillation hierarchy: rare comments come from distilled WHYs, never invented fresh.
