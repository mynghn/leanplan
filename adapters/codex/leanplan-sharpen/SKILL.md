---
name: leanplan-sharpen
description: LeanPlan — sharpen a disturbed understanding mid-round in Codex. Use for `leanplan sharpen <what shifted>`; reads artifacts and emits a delta, never edits surface artifacts.
---

# leanplan sharpen

LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work. This skill runs the off-pipeline sharpen move.

Load `~/.local/share/leanplan/references/sharpen.md` — it is authoritative for the reflect -> verify -> re-derive -> decide -> emit procedure and the read-never-edit boundary. Load these on demand, not up front (context-engineering: jit-loading):

- `~/.local/share/leanplan/references/artifact-contract.md` — before writing the understanding delta: `understanding-shifts.md` shape and `Delta-<N>` anchors.
- `~/.local/share/leanplan/references/philosophy.md` — when a principle's intent or grounding is in question.

Runtime glue:

- **Disturbance** — the argument is what shifted or a claim to check.
- **Write target** — append only to `<cwd>/docs/features/<KEY>/understanding-shifts.md`; do not edit committed surface artifacts.
- **Validate** — after emitting a delta, run `python3 ~/.local/share/leanplan/scripts/validate.py docs/features/<KEY>` or scope `--stage` to the in-flight stage if downstream artifacts do not yet exist.
- **Hand off** — return to the interrupted move; use `leanplan-revise` only when artifacts need repair.
