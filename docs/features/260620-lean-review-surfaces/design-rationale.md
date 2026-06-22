# 260620-lean-review-surfaces — Design Rationale

## D-1: one-prose-home-per-fact

Forces. Duplication inflates every surface (the arch-enemy) and, worse, the restated copies drift apart with no canonical source — a reviewer can't tell which is authoritative. The framework already had a clean single-seam guard (Design→Spec "no duplicate Invariants") — prose-only, never machine-enforced — but it was never generalized; the Requirements↔Spec seam was the worst offender because the recently-added System-policies sub-group was *defined in Spec vocabulary* ("cross-cutting invariants…"), so authors restated the same property as both a policy and an INV. Evidence in `research.md`.

Alternatives considered.
- **Spec sole home** (delete the Requirements System-policies group; continuous properties live only in Spec). Leanest and most orthogonal — the seam can't blur because one side is gone. Rejected: it removes a first-class home for biz-level cross-cutting mandates (regulatory rules, product values) that aren't a single observable contract, and it forces re-deriving the requirement template. We chose to preserve that expressiveness.
- **Route by testability** (a concern is a Spec C iff it has a single observable test, else a Requirements policy; mutually exclusive). Clean partition, but the "is it testable?" criterion is fuzzy at authoring time and would itself become a recurring judgment call. Rejected as harder to apply consistently than an altitude rule.

Chosen path. Altitude split + a general anchor rule: Requirements system-policy states the biz *why*; Spec `B`/`C` states the observable *what* (the canonical home); every other artifact cites the anchor. Keeps both homes, sharpens their roles, and generalizes that single-seam (prose-only) guard to all seams (including the two within-artifact cases). Least disruptive to the existing structure.

Invalidation trigger. If authors keep collapsing the altitude line in practice — system-policies that still read as observable INVs after this lands — the distinction isn't carrying its weight; revisit toward **Spec sole home**, which removes the seam outright.

## D-2: conclusion-first-on-prose-shaped-fields

Forces. The conclusion-first/lists rule already exists in `artifact-contract.md` Prose Style and applies to every artifact — so this is a conformance gap, not a missing principle. Requirements and Spec obey it because their *templates are list-shaped* (user-story bullets; atomic B/C items). Design and Tasks don't, because their central fields are left as free prose — the Design `Decision` body ("one-line WHAT then prose WHY") and the Tasks `Goal` (a process-framed statement with inline anchors) both collapse into a single dense paragraph or run-on. A size cap can't fix this: an artifact can sit under budget and still be a blob, because budget caps *size*, not *structure*. Evidence in `research.md`.

Alternatives considered.
- **Add an automated conformance check** (a conclusion-first / de-dup linter). Rejected for conclusion-first: it is a semantic property, not reliably machine-checkable, and a brittle heuristic would raise false failures that erode trust in the validator. De-dup is partially grep-checkable (Spec#B-2's own test), but the rule plus inspection suffices for a first deployment.

Chosen path. Strengthen the per-stage templates and guidance for the two named fields, each with one good/bad example, and bind Prose Style explicitly to them. Lean on the already-landed surface-budget guard for raw verbosity. Guidance over enforcement, consistent with the Spec Non-goal.

Invalidation trigger. If Design/Tasks instances keep regressing into blobs despite the strengthened guidance, reconsider a *targeted* heuristic check (e.g., a lead-line presence cue) — deferred until there's evidence guidance alone fails.
