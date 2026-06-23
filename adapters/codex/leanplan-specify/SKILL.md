---
name: leanplan-specify
description: LeanPlan — derive a Spec from existing Requirements in Codex. Use for `leanplan specify <KEY>` or when asked to run the LeanPlan Spec stage.
---

# leanplan specify

LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work. This skill drives the Spec stage (Requirements -> Spec edge).

Load `~/.local/share/leanplan/references/specify.md` — it is authoritative for the procedure, generic-category tech guard, B/C split, and Research archive rule. Load these on demand, not up front (context-engineering: jit-loading):

- `~/.local/share/leanplan/references/artifact-contract.md` — before writing or editing an artifact's structure or anchors: feature layout, `B-<N>` / `C-<N>` anchors, drift guards, traceability.
- `~/.local/share/leanplan/references/philosophy.md` — when a principle's intent or grounding is in question.

Runtime glue:

- **Input** — `<cwd>/docs/features/<KEY>/requirements.md`; if absent, stop and point the user to `leanplan-requirements` or `$leanplan requirements`.
- **Validate** — `python3 ~/.local/share/leanplan/scripts/validate.py <cwd>/docs/features/<KEY> --stage spec`.
- **Hand off** — next move is `leanplan-design <KEY>` or `$leanplan design <KEY>`.
