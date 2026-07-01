# 260701-reference-doc-boundaries — Spec

Terms used below:

- **concern** — a coherent block of reference content (e.g. anchor grammar, prose style).
- **load-occasion** — a point in an agent's workflow where content is needed.
- **unit** — an independently-loadable piece of the reference set (a doc, or an explicitly-referenced section).

The contract holds for whatever units a Design chooses; swapping the specific split must not change a line here.

## Behavior

### B-1: occasion-load-is-sufficient

The unit(s) an agent loads for a given load-occasion contain every concern that occasion needs to act, so the agent completes the step without pulling a second unit.
No concern is fragmented across units such that an occasion must assemble it from more than one load.
Verifiable one-shot: for a chosen occasion, enumerate the concerns it needs, load its designated target, and confirm all are present without gathering from another unit.

### B-2: occasion-load-is-clean

The unit(s) loaded for a load-occasion carry no concern whose load-occasion profile excludes that occasion, so the agent reasons over no unrelated concern.
B-2 is the precision dual of B-1's completeness — the same load, a distinct predicate — so the two are a legitimate pair, not one concern stated twice.
Verifiable one-shot: load the occasion's target and confirm every concern present belongs to that occasion's profile.

## Constraint

### C-1: one-authored-home-per-concern

Each concern is authored as prose in exactly one unit; every other mention is a reference to it, never a re-paraphrase.
This is One Prose Home Per Fact at the doc level, and it removes the current duplication where Required Shapes live in both the contract and each stage's Template.
Continuous; verified by a duplication audit over the scoped docs.

### C-2: references-resolve-one-hop

Every cross-unit reference points to a real target and reaches it in a single hop, with no dangling pointer and no multi-hop chain an agent must chase.
Continuous; verified by a link check.

### C-3: content-preserved-losslessly

Every rule and concern present in the scoped docs before the re-derivation is present after it, relocated but unchanged in meaning.
The re-derivation moves content between units; it does not drop a rule or rewrite what a rule says.
Continuous integrity property of the change as a whole.

### C-4: scope-stays-in-workflow-refs

The re-boundarying happens only in the `references/` workflow docs; no other doc is restructured or re-boundaried.
`framework-design.md` (the challenge-time archive) keeps its design content, role, and boundaries unchanged, but its citations to relocated `references/` sections are repaired to the new homes so no reference dangles — meaning-preserving follow-through, licensed by the Requirements' pointer-repair non-goal, not a re-boundarying.
`README.md` (the human entry point) is fully untouched.
Continuous scope boundary.

Refined during Design (warm fold): the original wording said `framework-design.md` was "untouched", but it cites the relocated sections, so leaving its pointers to dangle would break C-2; the intent (do not re-boundary it) is preserved, its pointers are repaired.

## Non-goals

- **One unit per load-occasion.** B-1 and B-2 hold when each occasion's load matches its need; a single unit serving several occasions is not a violation, and forcing a unit per occasion is out of contract.
- **A mechanical occasion-alignment gate.** Nothing here requires a validator to enforce these properties; they are review-verifiable, consistent with the framework's write-time-guidance stance.
