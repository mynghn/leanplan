# 260701-design-decision-legibility — Design Rationale

## D-1: promote-inner-atomicity-to-cross-cutting

Forces.
The framework's own pattern is home-once-apply-per-stage: `artifact-contract.md` owns each cross-cutting authoring rule and stage docs carry operational instances (`artifact-contract.md` → One Concern Per Item closing note).
One Concern Per Item (the cross-item direction) follows this pattern.
Its converse — inner-item atomicity, the anti-conflation rule — does not: it lives stage-local in `specify.md`, phrased for Behaviors only, while `artifact-contract.md` merely *references* it.
This feature needs inner-atomicity for Decisions, which exposes the asymmetry.

Alternatives.
- Stage-local (design.md only) — add the Decision guard to `design.md`, leave `specify.md`'s behavior rule as-is.
  Minimal blast radius, strictly Spec-scoped, but creates a *third* ad-hoc application with still no canonical home — an asymmetry a reviewer of these very docs would notice, undercutting the feature's own legibility goal.
- Promote to cross-cutting (chosen, planner call) — give inner-atomicity a canonical home paired with its converse; stage docs become instances.

Chosen path.
Promote.
The edit is small because the One Concern Per Item headline *already* encodes both directions ("exactly one concern that no sibling asserts"); the change mostly reframes the passage that attributes the inner direction away to `specify.md`.
Fixing the root asymmetry beats patching one more instance onto a rootless rule.

Invalidation.
Revisit the single-home choice if promoting bloats `artifact-contract.md`'s always-loaded surface materially, or if a future item kind ever needs a *divergent* inner-atomicity rule (which would break the one-rule-all-kinds premise).

## D-2: decision-atomicity-instance

Forces.
Atomicity for Decisions must de-blur — split a block that fuses separable choices — without becoming its own flat prescription by over-splitting one choice into many trivial blocks (the failure mode symmetric to the one `C-1` guards).

Chosen path.
A separability test is the bound: split only when two *separable* choices are fused, each carrying its own alternative or tradeoff.
Facets of a single choice (its schema, its rejected alternative, its invalidation cue) stay folded together, consistent with `design.md`'s existing "schemas fold inline within the relevant Decision."
The operational lever is a worked good/bad example, not a validator rule: atomicity is semantic and not regex-detectable, so it is enforced the way LeanPlan enforces most write-time guards (`framework-design.md` §7: validator-checked only where regex-detectable).

Alternatives.
A `leanplan-validate` check for decision atomicity — rejected as semantic and un-regexable; a false-precise gate would fire on legitimate folded facets.

Invalidation.
If reviewers report Decisions still blurring despite the guard + example, escalate to a stronger self-check probe or a trigger list.

## D-4: proportionality-guard

Forces.
The feature adds surface pressure — illustration (`D-3`) and splitting (`D-2`).
Left ungated, that pressure *is* a flat prescription: the P2/P3 harm the planner flagged — a verbose `design.md`, over-specific detail leaking into implementation, degraded agent reasoning.

Chosen path.
Gate both new affordances on genuine complexity and extend the existing trivial/non-trivial guard so a trivial Decision gains neither.
concise-not-compressed governs: raise resolution where it is missing, never inflate a decision that is already clear.

Road not taken.
A uniform mandate — every Decision carries a diagram + example and is split — rejected as the exact flat prescription `C-1` forbids; it would tax simple decisions and bloat the review surface, harming the implement side.

Invalidation.
If gating proves too soft — decisions still under-resolved because authors under-judge "complex enough" — consider a lightweight trigger list (relationship / sequence / state / mapping) rather than a uniform mandate.
