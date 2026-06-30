# 260630-item-orthogonality — Each stated item asserts a distinct, non-overlapping concern

## Problem

Two items in a LeanPlan round can sit on the same surface artifact while asserting overlapping concerns, and nothing in the framework catches it.

The framework guarantees *placement* orthogonality — each fact has one home artifact and section, derived from the stage coordinate model and held by "One Prose Home Per Fact."
It does not guarantee *item-set* orthogonality — that any two stated items, both correctly placed, still assert disjoint concerns.
The gap is widest across the Behavior↔Constraint boundary, where a Constraint can quietly restate a Behavior's claim, but it spans every section pair (Behavior↔Behavior, Constraint↔Constraint, Design decision↔decision, Task↔Task) and the whole round.

Who feels it:

- **Authors** carry an unstated rule.
  The one adjacent instruction they are given — "one item per behavior; don't fold two into one" — points *toward* splitting, and the Behavior-vs-Constraint type split breeds false confidence that type-disjoint means content-disjoint.
  Nothing names the opposite failure: two items sharing one concern.
- **Reviewers and implementation agents** inherit overlapping items as near-miss distractors.
  The framework's own leanness bet rests on the finding that near-relevant content measurably degrades retrieval and lifts hallucination — overlapping items are exactly that noise, on the artifact the agent reasons from.
  A reviewer also cannot tell whether two similar items are deliberately distinct or an accidental duplicate.
- The framework's **leanness / low-distraction lever weakens silently** — redundant overlapping claims re-inflate the surface while passing every existing structural check.

Observed directly: a Behavior item and a Constraint item carrying overlapping content reached an outcome artifact, undetected.

## Outcome

Item-set orthogonality is a first-class property of LeanPlan artifacts: any two stated items in a round assert distinct, non-overlapping concerns — within a section, across sections, and across the round — and authors are guided to produce such item sets while writing.

The property holds for every item kind a round produces, not just the boundary where it was first noticed.

User stories:

- **Author has an affirmative target** — when writing items, the author knows each item must assert exactly one concern that no sibling item asserts, stated as a goal to hit, not only a failure to avoid.
- **Author can resolve the hard boundary** — when a Behavior and a Constraint derive from the same subject, the author can tell a legitimate pair (each asserting a distinct claim about that subject) from an illegitimate overlap (one merely restating the other), without guessing.
- **Author checks orthogonality before the artifact is done** — drafting an artifact includes a moment that surfaces any two items sharing a concern, so overlap is caught at authoring time rather than at review or never.
- **Reviewer reads a clean item set** — scanning a finished artifact, no two items restate or partially cover each other's concern; each pair names a distinct concern.

Success signal: on a representative feature, every pair of items resolves to a distinct concern; the Behavior-vs-Constraint case that motivated this (an episodic occurrence vs. a standing property over the same subject) is distinguished correctly; and no item can be folded into another without losing a distinct piece of meaning.
The previously-undetected overlap pattern is one an author or reviewer now names and removes while authoring.

## Non-goals

- **Mechanical detection of overlap.** Catching item overlap by tooling is out of scope; content overlap is not reliably machine-detectable, and the framework's stance is to guide at write-time, not to police.
  Success is author/agent-applied guidance, not a validator gate.
- **Re-solving placement orthogonality.** Which artifact and section a fact belongs in is already handled by the coordinate model and One Prose Home Per Fact; this feature adds the missing item-level companion, it does not revisit placement.
- **Changing the Requirements↔Spec altitude split.** A Requirements intent and its Spec observable form are co-referential by design and governed by cite-don't-restate; that pairing is not an orthogonality violation and is not in scope to reframe.
- **Replacing the anti-conflation rule.** "Don't fold two into one" already forbids one item carrying two concerns; this feature supplies its missing dual (two items must not carry one concern), not a replacement for it.
