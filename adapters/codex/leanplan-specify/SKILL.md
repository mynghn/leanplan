---
name: leanplan-specify
description: LeanPlan — derive a Spec from existing Requirements in Codex. Use for `leanplan-specify <KEY>` or when asked to run the LeanPlan Spec stage.
---

# leanplan-specify

LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work. This skill drives the Spec stage (Requirements -> Spec edge).

Resolve `LP_ROOT` as the LeanPlan checkout containing this adapter: follow the real path of this `SKILL.md` from the installed skill symlink when present, then walk up three directories from `adapters/codex/<skill>/`. Later `references/...` and `scripts/...` paths are relative to `LP_ROOT`; when running a command, use the shell form `"$LP_ROOT/..."`.

Load `references/specify.md` from `LP_ROOT` — it is authoritative for the procedure, generic-category tech guard, B/C split, Research archive rule, and opt-in contract-boundary probe. Load these on demand, not up front (context-engineering: jit-loading):

- `references/artifact-contract.md` from `LP_ROOT` — before writing or editing an artifact's structure or anchors: feature layout, `B-<N>` / `C-<N>` anchors, and the cross-cutting authoring principles (the Spec shape + drift guard live in `references/specify.md`).
- `references/philosophy.md` from `LP_ROOT` — when a principle's intent or grounding is in question.

Runtime glue:

- **Input** — `<cwd>/docs/features/<KEY>/requirements.md`; if absent, stop and point the user to `leanplan-frame`.
- **Validate** — `"$LP_ROOT/scripts/leanplan-validate" <cwd>/docs/features/<KEY> --stage spec`.
- **Hand off** — next move is `leanplan-design <KEY>`.
