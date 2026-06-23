---
name: leanplan-design
description: LeanPlan — realize a Spec into a Design in Codex. Use for `leanplan-design <KEY>` or when asked to run the LeanPlan Design stage; also accepts routed `leanplan design <KEY>`.
---

# leanplan-design

LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work. This skill drives the Design stage (Spec -> Design edge).

Load `~/.local/share/leanplan/references/design.md` — it is authoritative for the procedure, architecture rule, decision blocks, rationale anchoring, and Spec coverage check. Load these on demand, not up front (context-engineering: jit-loading):

- `~/.local/share/leanplan/references/artifact-contract.md` — before writing or editing an artifact's structure or anchors: Design shape, `D-<N>` anchors, rationale shape, Research-as-evidence rule.
- `~/.local/share/leanplan/references/philosophy.md` — when a principle's intent or grounding is in question.

Runtime glue:

- **Input** — `<cwd>/docs/features/<KEY>/spec.md`; if absent, stop and point the user to `leanplan-specify`.
- **Validate** — `python3 ~/.local/share/leanplan/scripts/validate.py <cwd>/docs/features/<KEY> --stage design`.
- **Hand off** — next move is `leanplan-tasks <KEY>`; compatibility router form is `leanplan tasks <KEY>`.
