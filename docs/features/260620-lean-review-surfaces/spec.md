# 260620-lean-review-surfaces — SPEC

## Outcome

### O-1: surface-graspable-at-skim-depth
Every surface artifact (REQUIREMENT, SPEC, DESIGN, PLAN) yields its bottom line — what it decides and what a reviewer must check — from its headings and the lead line of each block alone, without reading any block to its end. DESIGN and PLAN meet the same bar REQUIREMENT and SPEC already hold. Verifiable by inspection: read only headings + first lines, and the artifact's decisions and check-points are recoverable.

### O-2: one-canonical-home-per-fact
Any cross-cutting fact — a property, policy, or invariant — is authored as prose in exactly one owning location; every other occurrence references it by anchor instead of re-paraphrasing. The artifact contract makes that ownership unambiguous, including the currently-blurred seam where a continuous property could read as either a REQUIREMENT system-policy or a SPEC invariant. (Which artifact owns each kind of fact is DESIGN's concern.) Verifiable: a search for any such fact returns one prose statement plus bare `…#…` references — zero re-paraphrases.

## Invariants

### INV-1: functional-identity-preserved
Across the legibility and de-dup changes, every surface stays a valid interim SDD artifact: all anchors resolve, traceability holds (SPEC O/INV ↔ TASK coverage, and every citation), and each artifact's stage ownership is unchanged. Verified by the structural validator.

### INV-2: leanness-not-regressed
No change increases a surface's prose reading load: each surface stays within its prose budget, and de-dup plus conclusion-first net-reduce or hold it — never inflate. Verified by the existing surface-budget guard.

## Non-goals
- New automated conformance checks (a conclusion-first or de-dup linter) are not required by this contract — conformance is verifiable by inspection; whether any is automated is DESIGN's concern.
- Re-deriving what each artifact contains or its stage role is excluded; this contract sharpens surface legibility and de-dup alongside the existing per-stage contracts, not in place of them.
- The already-orthogonal seams (RATIONALE vs RESEARCH vs DESIGN; DESIGN vs TASK tech-realization) stay out of scope.
