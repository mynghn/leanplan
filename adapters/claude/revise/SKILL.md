---
name: revise
description: LeanPlan — inject a justified drift into committed artifacts at any in-flight stage and propagate it downstream-only via intake-Delta → identify corrected artifact → edit in place (re-derive on structural change) preserving anchor IDs → re-validate. The repair half that consumes what /sharpen emits; edits artifacts, but only against a recorded justification.
argument-hint: "<KEY> [Delta-N | what drifted]"
allowed-tools: Read, Edit, Write, AskUserQuestion, Bash(python3 ~/.local/share/leanplan/scripts/validate.py *), Bash(~/.local/share/leanplan/scripts/leanplan-new *)
---

# revise

LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work in monorepos. This skill runs the revise move — the single sanctioned, any-stage entry for editing committed artifacts: it injects a justified drift and propagates it downstream-only.

Load `~/.local/share/leanplan/references/revise.md` — it is authoritative for the procedure (intake-Delta → identify corrected artifact → edit in place / re-derive on structural change → propagate downstream-only → re-validate), the justified-or-nothing and downstream-only boundaries, and the repair-vs-cognitive split with `/sharpen`. Load these on demand, not up front (CE: jit-loading):

- `~/.local/share/leanplan/references/artifact-contract.md` — **before editing an artifact's structure or anchors**: anchor patterns, the `(retired)` retire-by-note form, traceability, and the `understanding.md` / `Delta-<N>: <slug>` shape.
- `~/.local/share/leanplan/references/philosophy.md` — **when a principle's intent or grounding is in question**: the framework principles shaping what "good" looks like.

Runtime glue:

- **Target** — `$ARGUMENTS` names the feature `<KEY>` and, optionally, the `Delta-<N>` to consume or the drift to inject. The move engages on `<cwd>/docs/features/<KEY>/`'s committed artifacts at whatever stage is in flight, including mid-task during impl.
- **Justification** — the only mutation-authorizing input is a `Delta-<N>` block in `docs/features/<KEY>/understanding.md`. Consume the named one, or record one from the planner's asserted drift before any edit. With none and nothing recordable, make no edit.
- **Edit targets** — the artifact the drift corrects and every downstream artifact it implicates; artifacts upstream of the corrected one stay byte-unchanged.
- **Validate** — after propagating, run `python3 ~/.local/share/leanplan/scripts/validate.py docs/features/<KEY>` (scope `--stage` to the in-flight stage if downstream artifacts are not yet authored) to confirm the committed set is consistent and references no superseded content.
