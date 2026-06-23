---
name: leanplan-requirements
description: LeanPlan — author a Requirements artifact for a feature in Codex. Use for `leanplan-requirements <intent>` or when asked to run the LeanPlan Requirements stage.
---

# leanplan-requirements

LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work. This skill drives the Requirements stage.

Resolve `<LEANPLAN_ROOT>` as the LeanPlan checkout containing this adapter: follow the real path of this `SKILL.md` from the installed skill symlink when present, then walk up three directories from `adapters/codex/<skill>/`. Substitute that absolute path wherever commands below use `<LEANPLAN_ROOT>`.

Load `<LEANPLAN_ROOT>/references/requirements.md` — it is authoritative for the procedure, guardrails, and template. Load these on demand, not up front (context-engineering: jit-loading):

- `<LEANPLAN_ROOT>/references/artifact-contract.md` — before writing or editing an artifact's structure or anchors: feature layout, anchor patterns, drift guards, traceability rules.
- `<LEANPLAN_ROOT>/references/philosophy.md` — when a principle's intent or grounding is in question.

Runtime glue:

- **Intent forms** — brief feature intent, tracker key, `--date` intent, or an existing feature id to revise.
- **Allocator** — `<LEANPLAN_ROOT>/scripts/leanplan-new` is the single directory allocator: capture stdout path, stop on non-zero, never `mkdir`.
- **Validate** — `<LEANPLAN_ROOT>/scripts/leanplan-validate <captured-path> --stage requirements`.
- **Hand off** — next move is `leanplan-specify <KEY>`.
