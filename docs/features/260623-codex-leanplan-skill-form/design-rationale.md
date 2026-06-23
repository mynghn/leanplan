# 260623-codex-leanplan-skill-form — Design Rationale

## D-1: codex-move-skills

Split Codex into move-specific skills because LeanPlan moves have different activation conditions and different terminations. `requirements` starts from intent and writes Requirements; `specify` requires Requirements and writes Spec; `design` requires Spec and writes Design; `implement` starts from one task card and lands code; `sharpen` and `revise` are off-pipeline moves with opposite write boundaries. That is not one capability with different reference files; it is several capabilities sharing one framework.

The rejected design was the current single dispatcher as the only Codex surface. It is compact, but it makes one description advertise unrelated triggers and makes the dispatcher carry the burden of stage selection every time. That is exactly where activation drift hides: the model can enter "LeanPlan mode" without having selected a move with its own input and done condition.

The other rejected design was bare Codex names (`requirements`, `design`, `tasks`). That would mirror Claude more literally, but Codex's skill registry is a general agent surface; bare names are too likely to collide with ordinary requests. Prefixing with `leanplan-` is invocation glue, not semantic drift: the move names and references stay the same.

Invalidation trigger: if Codex later supports namespaced subcommands under a single skill with first-class metadata per subcommand, the split can collapse into that native structure. The invariant is not file count; it is one activation trigger and one termination per LeanPlan move.

## D-2: leanplan-front-door

Keep `leanplan` because users already invoke the framework as `$leanplan <move>` in Codex, and deleting that front door would make the better internal shape worse at the user boundary. The front door is acceptable only if it is reduced to routing glue. If it keeps full stage instructions, it recreates the original dispatcher drift in parallel with the new move skills.

This gives Codex two entry shapes but one semantic path: direct `leanplan-design` activation and `$leanplan design` both read the same move wrapper before acting. That preserves backward compatibility without preserving the old ambiguity.

Invalidation trigger: if the front door begins accumulating per-stage procedure again, remove it or regenerate it from the adapter map. Its job is dispatch, not authorship.

## D-3: adapter-move-map

Add a small adapter map because "same as Claude" is otherwise an assertion spread across two adapter trees, install docs, and stage references. A reviewer needs one table that says which vendor surface maps to which LeanPlan move and where a surface difference is intentional.

The map deliberately lives under `adapters/`, not `references/`: it is not framework procedure and should not be loaded during normal stage execution. It is review metadata for the runtime shells. That keeps shared stage behavior in `references/*.md` while making vendor drift visible.

The one awkward row is `validate`. Codex already exposes validation through the front door; Claude validation is stage-local runtime glue. Recording that as an explicit divergence is better than either pretending the surfaces are identical or adding a Claude validation command solely for symmetry. Both vendors still share the same validator script and flags.
