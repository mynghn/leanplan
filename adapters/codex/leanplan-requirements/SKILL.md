---
name: leanplan-requirements
description: LeanPlan — author a Requirements artifact for a feature in Codex. Use for `leanplan-requirements <intent>` or when asked to run the LeanPlan Requirements stage; also accepts routed `leanplan requirements <intent>`.
---

# leanplan-requirements

LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work. This skill drives the Requirements stage.

Load `~/.local/share/leanplan/references/requirements.md` — it is authoritative for the procedure, guardrails, and template. Load these on demand, not up front (context-engineering: jit-loading):

- `~/.local/share/leanplan/references/artifact-contract.md` — before writing or editing an artifact's structure or anchors: feature layout, anchor patterns, drift guards, traceability rules.
- `~/.local/share/leanplan/references/philosophy.md` — when a principle's intent or grounding is in question.

Runtime glue:

- **Intent forms** — brief feature intent, tracker key, `--date` intent, or an existing feature id to revise.
- **Allocator** — `~/.local/share/leanplan/scripts/leanplan-new` is the single directory allocator: capture stdout path, stop on non-zero, never `mkdir`.
- **Validate** — `python3 ~/.local/share/leanplan/scripts/validate.py <captured-path> --stage requirements`.
- **Hand off** — next move is `leanplan-specify <KEY>`; compatibility router form is `leanplan specify <KEY>`.
