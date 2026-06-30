# 260630-item-orthogonality — Design Rationale

## D-1: principle-home-and-form

Forces: the rule must be reachable when an author writes items, stated once (C-2), worded so it composes rather than collides (C-3), and grounded in why it matters — the CE distractor argument is the framework's own thesis.

Placement alternatives weighed:

- **`philosophy.md` as a new behavior-shaping principle.**
  Rejected: philosophy's P1–P9 are meta-stance principles (JIT-loaded on challenge), so a structural rule about item shape is miscategorized there and would dilute that list.
  One Prose Home Per Fact — the fact-level twin of this rule — already lives in `artifact-contract.md`, not philosophy, so the parallel home is the consistent one.
- **`framework-design.md` §2/§3 (the orthogonality model).**
  Rejected, and the rejection is load-bearing: item-set orthogonality is **not derivable** from the World↔Machine / Contract↔Realization / Product↔Process coordinate model.
  Those axes adjudicate *placement* (which cell a fact occupies) and say nothing about whether two facts in one cell overlap.
  Putting the rule there would imply the model generates it; it does not — the rule is a companion to the model, authored in the structural contract.
- **Chosen: `artifact-contract.md`, as the named dual of One Prose Home Per Fact.**
  One Prose Home says each *fact* has one home (no fact restated across homes); One Concern Per Item says each *item* asserts one concern no sibling asserts (no concern spread across items).
  Stated together they make a round's item set a partition.
  The contract already binds "every seam"; this binds "every item pair."

Form: affirmative ("each item asserts exactly one concern no sibling asserts"), not a prohibition — a named target steers better than "don't overlap", and avoids priming the banned behavior.
The scope carve-out is explicit so the rule never fires on the two structures that *look* like overlap but are intended: a Requirements-intent / Spec-observable altitude pair (governed by cite-don't-restate), and a correct Behavior + Constraint split over one subject.

Invalidation: if a future model rework ever made item-orthogonality derivable from the stage axes, this would fold back into framework-design.md; until then it stands alone.

## D-2: bc-discriminator-in-specify

Forces: the B↔C boundary is where overlap was actually observed, because the episodic-vs-continuous *type* split feels like it already separates the items — masking that they can still assert the same predicate.

Chosen: extend the **existing** worked example (the 1-B-plus-2-C anomaly case) rather than open a standalone "orthogonality" section.
The example already sits exactly where an author decides B-vs-C, so adding the subject-vs-predicate test and one ❌ overlap case (a Constraint that only re-asserts "the event is published") teaches the discriminator in the place the confusion arises.
A standalone section would split the lesson from its trigger and cost more surface.

Rejected: a separate worked example elsewhere — it would duplicate the anomaly framing and add surface for no locality gain.

Invalidation: if the B/C example is ever relocated or the episodic/continuous split is redefined, this discriminator moves with it.

## D-3: write-time-check-as-stage-self-check-pointer

Forces: the check must fire *while authoring* (B-3), in the stage the author is in, but must not bloat the always-loaded stage references (C-2) or harden into a rote procedure (C-1).

Degrees-of-freedom call (skill-design): adjudicating whether two items share a concern is an *open-field* judgment — multiple valid resolutions (merge, cut, re-scope), context-dependent.
That is the high-freedom tier: state the goal, trust the model's reasoning.
A low-freedom mandated N×N pairwise sweep would be the wrong tier — and the SkillsBench evidence (curated skills +16.6 pp, over-specified −1.3 pp) says over-specifying procedure actively degrades, so the rigid form is not a safe default.

Token-tier call (progressive-disclosure): the stage references are always-loaded when their stage runs, while `artifact-contract.md` is JIT.
So only the *trigger + goal* (one line) goes in each stage self-check, and the *full rule + discriminator + grounding* stays in D-1's JIT home.
The four self-check bullets are pointers (cite-don't-restate), not four copies — which is itself the C-2 discipline applied to this feature's own edits.

Which stages: all four item-producing pipeline stages — frame (Outcome / Guarantee items), specify (B/C), design (D), tasks (T).
`rethink` / `revise` are off-pipeline and re-derive against committed artifacts, so they inherit the rule through the artifacts, not a new bullet.

Invalidation: if a stage stops producing first-class items, drop its bullet.

## D-4: no-mechanical-enforcement

Forces: a validator catch is tempting as a backstop, and the validator already has a duplicate-anchor check, so a slug-near-duplicate advisory is a small reach.

Chosen: add nothing to the validator, for two reasons.
First, content overlap is not reliably machine-detectable — two items can overlap in concern with no lexical signal, while a slug-similarity heuristic both misses those and false-positives on legitimately-adjacent items (e.g. `publish-latency` vs `publish-completeness`), and a checker that cries wolf trains authors to ignore it.
Second, a gate would pull the rule toward the low-freedom tier that D-3 deliberately rejected, contradicting C-1.

Rejected (road-not-taken, recorded because it will be proposed again): the cheap deterministic advisory that flags two anchors sharing a slug under different numbers.
It is genuinely catchable and currently is not caught — but it targets an accidental copy-paste, not the conceptual overlap this feature is about, so it is out of scope here.
If it is ever wanted, it belongs to a separate "validator hygiene" change, advisory-only, not to this rule.

Invalidation: revisit only if a low-false-positive overlap signal emerges (e.g. a reliable semantic check) — then a strictly-advisory warning could be reconsidered without touching the write-time rule.
