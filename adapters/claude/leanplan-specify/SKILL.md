---
name: leanplan-specify
description: LeanPlan — derive a Spec (externally-observable contract) from an existing Requirements. Generic-category tech only; split episodic Behavior items from continuous Constraints.
argument-hint: "<feature-key>"
allowed-tools: Read, Write, Edit, Grep, Glob, AskUserQuestion, Agent, Bash(ls *), Bash(mkdir *), Bash(*/scripts/leanplan-validate *), WebFetch, WebSearch
---

# leanplan specify

LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work. This skill drives the Spec stage (Requirements → Spec edge).

Resolve `<LEANPLAN_ROOT>` as the LeanPlan checkout containing this adapter: follow the real path of this `SKILL.md` from the installed skill symlink when present, then walk up three directories from `adapters/claude/<skill>/`. Substitute that absolute path wherever commands below use `<LEANPLAN_ROOT>`.

Load `<LEANPLAN_ROOT>/references/specify.md` — it is authoritative for the procedure ("what a Spec is NOT" test, generic-category tech guard, Research archive rule). Load these on demand, not up front (context-engineering: jit-loading):

- `<LEANPLAN_ROOT>/references/artifact-contract.md` — **before writing or editing an artifact's structure or anchors**: feature layout, anchor patterns (`B-<N>: <slug>` / `C-<N>: <slug>`), drift guards, traceability rules including `**GAP**` semantics.
- `<LEANPLAN_ROOT>/references/philosophy.md` — **when a principle's intent or grounding is in question**: the framework principles shaping what "good" looks like.

Runtime glue:

- **Missing input** — if `<cwd>/docs/features/<KEY>/requirements.md` is absent, stop and point the user to `/leanplan-requirements` (see `specify.md` Inputs).
- **Validate** — `<LEANPLAN_ROOT>/scripts/leanplan-validate <cwd>/docs/features/<KEY> --stage spec`.
- **Hand off** — next edge is `/leanplan-design <KEY>`.
