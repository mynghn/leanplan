# 260701-design-decision-legibility — Spec

*The system under contract is LeanPlan's Design stage; the observer is a reviewer reading a `design.md` it produces.*

## Behavior

### B-1: complex-decision-graspable-in-place

When a Decision's mechanism is complex enough that prose alone would leave a reviewer re-deriving it — a non-obvious algorithm, a state transition, a control- or data-flow sequence, or a field mapping — the produced `design.md` presents that mechanism so the reviewer grasps it where it is read, without reconstructing it externally.
The aid that achieves this — a worked example, a local diagram, a small table — is the author's choice; the observable contract is the reviewer's in-place grasp, not the presence of any particular aid.

## Constraint

### C-1: resolution-proportional-to-complexity

Resolution is spent in proportion to each decision's complexity, never as a uniform per-decision tax.
A trivial decision keeps its one-line form and gains no aid; depth or illustration appears only where a decision's genuine complexity requires it, and no Decision carries an example, diagram, or expansion a reviewer would read as redundant.
This is the concise-not-compressed guard: the feature raises resolution where it is missing without inflating decisions that were already clear.

### C-2: decision-asserts-one-separable-point

Each Decision block asserts a single non-separable design point: a block that fuses two separable choices — each carrying its own alternative or tradeoff — is split, so a reviewer can evaluate each on its own.
The separability test bounds the split: facets of one choice (its schema, its rejected alternative, its invalidation cue) stay together, so this never devolves into over-splitting one decision into many.
This is inner-item atomicity, the converse of One Concern Per Item's cross-item non-redundancy — a distinct concern, not a restatement; today it is operationalized only for Behaviors (`one item per behavior`), not for Decisions.

## Non-goals

- Prose-resolution (a single point written as a wall) and realization-completeness of a decision are not re-contracted here — they already ride on existing operationalized rules (Prose Style plus the Decision-body worked example; "realization specifics live here in full").
  This feature makes those land at the Design decision for a reviewer; it does not restate them as new `B`/`C` (One Prose Home Per Fact).
  Atomicity is *not* on this list — it is genuinely uncontracted for Decisions, so `C-2` above establishes it.
- Scoped to the Design stage's per-Decision unit — not the Requirements/Spec/Tasks stages, and not the Architecture diagram or rationale archive as artifacts.
