---
name: leanplan-revise
description: LeanPlan — inject a justified change into already-committed artifacts at any in-flight stage and propagate it only to downstream stages, editing in place against a recorded justification. The repair counterpart to /leanplan-sharpen (which only diagnoses); never edits without a recorded reason.
argument-hint: "<KEY> [what drifted | a recorded delta]"
allowed-tools: Read, Edit, Write, AskUserQuestion, Bash(*/scripts/leanplan-validate *), Bash(*/scripts/leanplan-new *)
---

# leanplan revise

LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work. This skill runs the revise move — the single sanctioned, any-stage entry for editing committed artifacts: it injects a justified drift and propagates it downstream-only.

Resolve `LP_ROOT` as the LeanPlan checkout containing this adapter: follow the real path of this `SKILL.md` from the installed skill symlink when present, then walk up three directories from `adapters/claude/<skill>/`. Later `references/...` and `scripts/...` paths are relative to `LP_ROOT`; when running a command, use the shell form `"$LP_ROOT/..."`.

Load `references/revise.md` from `LP_ROOT` — it is authoritative for the procedure (intake-Delta → identify corrected artifact → edit in place / re-derive on structural change → propagate downstream-only → re-validate), the justified-or-nothing and downstream-only boundaries, and the repair-vs-cognitive split with `/leanplan-sharpen`. Load these on demand, not up front (context-engineering: jit-loading):

- `references/artifact-contract.md` from `LP_ROOT` — **before editing an artifact's structure or anchors**: anchor patterns, the `(retired)` retire-by-note form, traceability, and the `understanding-shifts.md` / `Delta-<N>: <slug>` shape.
- `references/philosophy.md` from `LP_ROOT` — **when a principle's intent or grounding is in question**: the framework principles shaping what "good" looks like.

Runtime glue:

- **Target** — `$ARGUMENTS` names the feature `<KEY>` and, optionally, the `Delta-<N>` to consume or the drift to inject. The move engages on `<cwd>/docs/features/<KEY>/`'s committed artifacts at whatever stage is in flight, including mid-task during implementation.
- **Justification** — the only mutation-authorizing input is a `Delta-<N>` block in `docs/features/<KEY>/understanding-shifts.md`. Consume the named one, or record one from the planner's asserted drift before any edit. With none and nothing recordable, make no edit.
- **Edit targets** — the artifact the drift corrects and every downstream artifact it implicates; artifacts upstream of the corrected one stay byte-unchanged.
- **Validate** — after propagating, run `"$LP_ROOT/scripts/leanplan-validate" docs/features/<KEY>` (scope `--stage` to the in-flight stage if downstream artifacts are not yet authored) to confirm the committed set is consistent and references no superseded content.
