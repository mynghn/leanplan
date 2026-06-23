---
name: leanplan-implement
description: LeanPlan — implement one Tasks card against current code in Codex. Use for `leanplan-implement <KEY> <task-id>`.
---

# leanplan-implement

LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work. This skill drives implementation (one task card -> working software).

Resolve `LP_ROOT` as the LeanPlan checkout containing this adapter: follow the real path of this `SKILL.md` from the installed skill symlink when present, then walk up three directories from `adapters/codex/<skill>/`. Later `references/...` and `scripts/...` paths are relative to `LP_ROOT`; when running a command, use the shell form `"$LP_ROOT/..."`.

Load `references/implement.md` from `LP_ROOT` — it is authoritative for task entry, stop-the-line triggers, artifact update loop delegation, verification, close-out distillation, and leak scanning. Load these on demand, not up front (context-engineering: jit-loading):

- `references/artifact-contract.md` from `LP_ROOT` — before writing or editing artifact structure or anchors, including the artifact update loop.
- `references/philosophy.md` from `LP_ROOT` — when a principle's intent or grounding is in question.

Runtime glue:

- **Inputs** — `<cwd>/docs/features/<KEY>/tasks.md` and the selected `T: <task-id>` card.
- **Load-bearing citations** — JIT-load the card's cited Spec B/C and Design D blocks before coding; archive citations remain load-on-challenge.
- **Stop-the-line** — if current code contradicts the plan, record the drift and invoke `leanplan-revise <KEY>` before coding.
- **Close out** — load `references/implement-closeout.md` from `LP_ROOT`, verify completion criteria explicitly, distill WHYs into durable code/test/commit/PR forms, and run `scan-leaks`.
