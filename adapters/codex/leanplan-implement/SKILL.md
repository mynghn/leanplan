---
name: leanplan-implement
description: LeanPlan — implement one Tasks card against current code in Codex. Use for `leanplan implement <KEY> <task-id>`.
---

# leanplan implement

LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work. This skill drives implementation (one task card -> working software).

Load `~/.local/share/leanplan/references/implement.md` — it is authoritative for task entry, stop-the-line triggers, artifact update loop delegation, verification, close-out distillation, and leak scanning. Load these on demand, not up front (context-engineering: jit-loading):

- `~/.local/share/leanplan/references/artifact-contract.md` — before writing or editing artifact structure or anchors, including the artifact update loop.
- `~/.local/share/leanplan/references/philosophy.md` — when a principle's intent or grounding is in question.

Runtime glue:

- **Inputs** — `<cwd>/docs/features/<KEY>/tasks.md` and the selected `T: <task-id>` card.
- **Load-bearing citations** — JIT-load the card's cited Spec B/C and Design D blocks before coding; archive citations remain load-on-challenge.
- **Stop-the-line** — if current code contradicts the plan, record the drift and invoke `leanplan-revise <KEY>` or `$leanplan revise <KEY>` before coding.
- **Close out** — load `~/.local/share/leanplan/references/implement-closeout.md`, verify completion criteria explicitly, distill WHYs into durable code/test/commit/PR forms, and run `scan-leaks`.
