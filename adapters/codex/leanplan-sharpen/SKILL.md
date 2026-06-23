---
name: leanplan-sharpen
description: LeanPlan — sharpen a disturbed understanding mid-round in Codex. Use for `leanplan-sharpen <what shifted>`; reads artifacts and emits a delta, never edits surface artifacts.
---

# leanplan-sharpen

LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work. This skill runs the off-pipeline sharpen move.

Resolve `<LEANPLAN_ROOT>` as the LeanPlan checkout containing this adapter: follow the real path of this `SKILL.md` from the installed skill symlink when present, then walk up three directories from `adapters/codex/<skill>/`. Substitute that absolute path wherever commands below use `<LEANPLAN_ROOT>`.

Load `<LEANPLAN_ROOT>/references/sharpen.md` — it is authoritative for the reflect -> verify -> re-derive -> decide -> emit procedure and the read-never-edit boundary. Load these on demand, not up front (context-engineering: jit-loading):

- `<LEANPLAN_ROOT>/references/artifact-contract.md` — before writing the understanding delta: `understanding.md` shape and `Delta-<N>` anchors.
- `<LEANPLAN_ROOT>/references/philosophy.md` — when a principle's intent or grounding is in question.

Runtime glue:

- **Disturbance** — the argument is what shifted or a claim to check.
- **Write target** — append only to `<cwd>/docs/features/<KEY>/understanding.md`; do not edit committed surface artifacts.
- **Validate** — after emitting a delta, run `<LEANPLAN_ROOT>/scripts/leanplan-validate docs/features/<KEY>` or scope `--stage` to the in-flight stage if downstream artifacts do not yet exist.
- **Hand off** — return to the interrupted move; use `leanplan-revise` only when artifacts need repair.
