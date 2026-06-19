---
name: specify
description: LeanPlan — derive a SPEC (externally-observable contract) from an existing REQUIREMENT. Generic-category tech only; split episodic Outcome items from continuous Invariants.
argument-hint: "<feature-key>"
allowed-tools: Read, Write, Edit, Grep, Glob, AskUserQuestion, Agent, Bash(ls *), Bash(mkdir *), WebFetch, WebSearch
---

# specify

LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work in monorepos. This skill drives the SPEC stage (REQUIREMENT → SPEC edge).

Load `~/.local/share/leanplan/references/specify.md` — it is authoritative for the procedure ("what a SPEC is NOT" test, generic-category tech guard, RESEARCH archive rule). Load these on demand, not up front (CE: jit-loading):

- `~/.local/share/leanplan/references/artifact-contract.md` — **before writing or editing an artifact's structure or anchors**: feature layout, anchor patterns (`O-<N>: <slug>` / `INV-<N>: <slug>`), drift guards, traceability rules including `**GAP**` semantics.
- `~/.local/share/leanplan/references/philosophy.md` — **when a principle's intent or grounding is in question**: the framework principles shaping what "good" looks like.

Runtime glue:

- **Missing input** — if `<cwd>/docs/features/<KEY>/requirement.md` is absent, stop and point the user to `/requirement` (see `specify.md` Inputs).
- **Validate** — `python3 ~/.local/share/leanplan/scripts/validate.py <cwd>/docs/features/<KEY> --stage spec`.
- **Hand off** — next edge is `/design <KEY>`.
