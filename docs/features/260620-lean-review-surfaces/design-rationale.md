# 260620-lean-review-surfaces — DESIGN RATIONALE

## Decision-1: one-prose-home-per-fact

Forces. Duplication inflates every surface (the arch-enemy) and, worse, the restated copies drift apart with no canonical source — a reviewer can't tell which is authoritative. The framework already proved a seam can be guarded cleanly (DESIGN→SPEC "no duplicate Invariants"), but that guard was never generalized; the REQUIREMENT↔SPEC seam was the worst offender because the recently-added System-policies sub-group was *defined in SPEC vocabulary* ("cross-cutting invariants…"), so authors restated the same property as both a policy and an INV. Evidence in `research.md`.

Alternatives considered.
- **SPEC sole home** (delete the REQUIREMENT System-policies group; continuous properties live only in SPEC). Leanest and most orthogonal — the seam can't blur because one side is gone. Rejected: it removes a first-class home for biz-level cross-cutting mandates (regulatory rules, product values) that aren't a single observable contract, and it forces re-deriving the requirement template. We chose to preserve that expressiveness.
- **Route by testability** (a concern is a SPEC INV iff it has a single observable test, else a REQUIREMENT policy; mutually exclusive). Clean partition, but the "is it testable?" criterion is fuzzy at authoring time and would itself become a recurring judgment call. Rejected as harder to apply consistently than an altitude rule.

Chosen path. Altitude split + a general anchor rule: REQUIREMENT system-policy states the biz *why*; SPEC `O`/`INV` states the observable *what* (the canonical home); every other artifact cites the anchor. Keeps both homes, sharpens their roles, and generalizes the proven DESIGN→SPEC guard to all seams (including the two within-artifact cases). Least disruptive to the existing structure.

Invalidation trigger. If authors keep collapsing the altitude line in practice — system-policies that still read as observable INVs after this lands — the distinction isn't carrying its weight; revisit toward **SPEC sole home**, which removes the seam outright.

## Decision-2: conclusion-first-on-prose-shaped-fields

Forces. The conclusion-first/lists rule already exists in `artifact-contract.md` Prose Style and applies to every artifact — so this is a conformance gap, not a missing principle. REQUIREMENT and SPEC obey it because their *templates are list-shaped* (user-story bullets; atomic O/INV items). DESIGN and PLAN don't, because their central fields are left as free prose — the DESIGN `Decision` body ("one-line WHAT then prose WHY") and the TASK `Goal` (a process-framed statement with inline anchors) both collapse into a single dense paragraph or run-on. A size cap can't fix this: an artifact can sit under budget and still be a blob, because budget caps *size*, not *structure*. Evidence in `research.md`.

Alternatives considered.
- **Add an automated conformance check** (a conclusion-first / de-dup linter). Rejected for conclusion-first: it is a semantic property, not reliably machine-checkable, and a brittle heuristic would raise false failures that erode trust in the validator. De-dup is partially grep-checkable (SPEC#O-2's own test), but the rule plus inspection suffices for a first deployment.

Chosen path. Strengthen the per-stage templates and guidance for the two named fields, each with one good/bad example, and bind Prose Style explicitly to them. Lean on the already-landed surface-budget guard for raw verbosity. Guidance over enforcement, consistent with the SPEC Non-goal.

Invalidation trigger. If DESIGN/PLAN instances keep regressing into blobs despite the strengthened guidance, reconsider a *targeted* heuristic check (e.g., a lead-line presence cue) — deferred until there's evidence guidance alone fails.
