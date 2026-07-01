---
name: leanplan-rethink
description: LeanPlan — rethink a disturbed understanding mid-round in Codex. Use for `leanplan-rethink <what shifted>`; reads artifacts and emits a delta, never edits surface artifacts.
---

# leanplan-rethink

LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work. This skill runs the off-pipeline rethink move.

Resolve `LP_ROOT` as the LeanPlan checkout containing this adapter: follow the real path of this `SKILL.md` from the installed skill symlink when present, then walk up three directories from `adapters/codex/<skill>/`. Later `references/...` and `scripts/...` paths are relative to `LP_ROOT`; when running a command, use the shell form `"$LP_ROOT/..."`.

Load `references/rethink.md` from `LP_ROOT` — it is authoritative for the reflect -> verify -> re-derive -> decide -> emit procedure and the read-never-edit boundary. Load these on demand, not up front (context-engineering: jit-loading):

- `references/artifact-contract.md` from `LP_ROOT` — before writing the understanding delta: `Delta-<N>` anchor pattern (the delta shape now lives in `references/rethink.md`).
- `references/philosophy.md` from `LP_ROOT` — when a principle's intent or grounding is in question.

Runtime glue:

- **Disturbance** — the argument is what shifted or a claim to check.
- **Write target** — append only to `<cwd>/docs/features/<KEY>/understanding-shifts.md`; do not edit committed surface artifacts.
- **Validate** — after emitting a delta, run `"$LP_ROOT/scripts/leanplan-validate" docs/features/<KEY>` or scope `--stage` to the in-flight stage if downstream artifacts do not yet exist.
- **Hand off** — return to the interrupted move; use `leanplan-revise` only when artifacts need repair.
