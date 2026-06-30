# 260630-item-orthogonality — Spec

## Behavior

### B-1: item-overlap-named-as-defect

Applying the framework to two items that assert overlapping concerns yields a verdict of "overlap" plus a named resolution.
The rule binds any item pair in a round — within one section, across the Behavior↔Constraint boundary, and across the whole round — and across every item kind (Behavior, Constraint, Design decision, Task).
Resolution is one of merge, cut, or re-scope, so each surviving item asserts a concern no sibling asserts.
Verifiable by a one-shot test: feed an overlapping pair and a clean pair; the overlapping one is flagged with a resolution, the clean one passes.

### B-2: same-subject-behavior-constraint-pair-adjudicated

Given a Behavior and a Constraint that share a subject, the framework's discriminator returns whether they are a legitimate distinct pair or an overlap.
Legitimate: the Behavior asserts the occurrence (the episode — "when X, Y happens") and the Constraint asserts a standing property over the same subject (rate, completeness, bound); they share a subject but not a predicate.
Overlap: the Constraint merely restates the Behavior's occurrence claim as a continuous one, adding no distinct predicate.
Verifiable by a one-shot test: an episodic publish behavior paired with latency and completeness constraints returns legitimate; a constraint that only re-asserts "the event is published" returns overlap.

### B-3: authoring-surfaces-an-orthogonality-check

Drafting an item-producing artifact surfaces an explicit moment that checks each item pair — including the round's upstream items — for a distinct concern before the artifact is considered done.
The check is reachable from the stage's own authoring procedure, not a separate tool the author must remember to run.
Verifiable by a one-shot test: the procedure for an item-producing stage contains the verification step, and running it over a drafted artifact reports per-pair distinctness or flags a shared concern.

## Constraint

### C-1: orthogonality-guidance-stays-high-freedom

The guidance is stated as a goal the author reasons toward — name each item's one concern, resolve any shared concern — never as a rigid enumerated procedure such as a mandated N×N pairwise sweep.
Continuous: holds wherever the guidance appears.

### C-2: additions-hold-the-surface-budget

The guidance is authored as prose once, in a single home, and referenced from any other point of use, so surface artifacts and always-loaded references stay within their existing size budgets.
Continuous integrity property of the change as a whole.

### C-3: rule-flags-no-legitimately-distinct-pairing

Applying the item-orthogonality rule never reports a legitimately-distinct structure as overlap: not a Requirements-intent / Spec-observable pair (co-referential across an altitude by design), and not a correctly-split Behavior + Constraint from one subject.
It also does not reverse the anti-conflation rule ("don't fold two into one") — it supplies that rule's missing dual rather than contradicting it.
Continuous.
