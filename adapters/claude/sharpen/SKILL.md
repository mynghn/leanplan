---
name: sharpen
description: LeanPlan — sharpen a disturbed understanding mid-round via reflect → verify → re-derive → decide → emit, logging a durable delta. Off-pipeline and opt-in; reads committed artifacts, never edits them.
argument-hint: "[what shifted | a claim to check]"
allowed-tools: Read, AskUserQuestion, WebSearch, WebFetch, Write, Bash(python3 ~/.local/share/leanplan/scripts/validate.py *)
---

# sharpen

LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work. This skill runs the sharpen move — a mid-round, off-pipeline re-derivation of a disturbed understanding (not a stage edge).

Load `~/.local/share/leanplan/references/sharpen.md` — it is authoritative for the procedure (reflect → verify → re-derive → decide → emit), the two honest stances (adversarial claim-verification, legitimate no-op), and the read-never-edit boundary. Load these on demand, not up front (context-engineering: jit-loading):

- `~/.local/share/leanplan/references/artifact-contract.md` — **before writing the understanding delta**: the `understanding-shifts.md` archive shape and `Delta-<N>: <slug>` anchor.
- `~/.local/share/leanplan/references/philosophy.md` — **when a principle's intent or grounding is in question**: the framework principles shaping what "good" looks like.

Runtime glue:

- **Disturbance** — `$ARGUMENTS` is what shifted, or the external claim to check. The move engages within the in-flight stage and returns control to it; it never gates the stage.
- **Write target** — the only write is an appended `Delta-<N>: <slug>` block in `<cwd>/docs/features/<KEY>/understanding-shifts.md`. No committed surface artifact is edited.
- **Validate** — after emitting a delta, run `python3 ~/.local/share/leanplan/scripts/validate.py docs/features/<KEY>` to confirm its scope-of-impact citations resolve. If you paused **before all surface artifacts exist** (mid-requirements/spec/design), scope `--stage` to the in-flight stage so validation fails on the delta, not on not-yet-authored downstream files; mid-tasks or mid-implementation the full surface exists, so omit `--stage` (there is no `implement` stage value).
