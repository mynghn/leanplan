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

## Non-goals

- Atomicity, prose-resolution, and realization-completeness of a decision are not re-contracted here — they already ride on existing cross-cutting rules (One Concern Per Item; Prose Style; "realization specifics live here in full").
  This feature makes those rules land at the Design decision for a reviewer; it does not restate them as new `B`/`C` (One Prose Home Per Fact).
- Scoped to the Design stage's per-Decision unit — not the Requirements/Spec/Tasks stages, and not the Architecture diagram or rationale archive as artifacts.
