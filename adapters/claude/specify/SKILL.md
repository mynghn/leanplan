---
name: specify
description: LeanPlan — derive a SPEC (externally-observable contract) from an existing REQUIREMENT. Generic-category tech only; split episodic Outcome items from continuous Invariants.
argument-hint: "<feature-key>"
allowed-tools: Read, Write, Edit, Grep, Glob, AskUserQuestion, Bash(ls *), Bash(mkdir *), WebFetch, WebSearch
---

# specify

LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work in monorepos. This skill drives the SPEC stage (REQUIREMENT → SPEC edge).

Before writing the artifact, load:

- `~/.local/share/leanplan/references/philosophy.md` — framework principles shaping what "good" looks like across all stages.
- `~/.local/share/leanplan/references/artifact-contract.md` — feature layout, anchor patterns (`O-<N>: <slug>` / `INV-<N>: <slug>`), drift guards, traceability rules including `**GAP**` semantics.
- `~/.local/share/leanplan/references/specify.md` — stage-specific procedure, "what a SPEC is NOT" test, generic-category tech guard, RESEARCH archive rule.

If `<cwd>/docs/features/<KEY>/requirement.md` is missing, stop and tell the user to run `/requirement <feature-title>` first (it allocates and prints the `<KEY>` = `NNNN-slug` dir). Validate after writing with `python3 ~/.local/share/leanplan/scripts/validate.py <cwd>/docs/features/<KEY> --stage spec`.

After writing, hand off: next edge is `/design <KEY>`.
