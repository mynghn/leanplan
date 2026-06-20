# 260620-lean-review-surfaces — SPEC

## Outcome

### O-1: surface-graspable-at-skim-depth
When a reviewer skims any surface artifact (REQUIREMENT, SPEC, DESIGN, PLAN) — reading only headings and each block's lead line — its bottom line is recoverable: what it decides and what to check, without reading any block to its end. DESIGN and PLAN reach the bar REQUIREMENT and SPEC already hold. One-shot test: skim-read a surface; its decisions and check-points are recoverable.

### O-2: one-canonical-home-per-fact
When any cross-cutting fact — a property, policy, or invariant — is searched across the chain, it surfaces as one authored prose statement plus bare `…#…` anchors; no other occurrence re-paraphrases it. The artifact contract makes that ownership unambiguous, including the currently-blurred seam where a continuous property could read as either a REQUIREMENT system-policy or a SPEC invariant. (Which artifact owns each kind of fact is DESIGN's concern.) One-shot test: grep the fact → one prose home + bare anchors; a reviewer confirms no occurrence restates it in different words (a paraphrase shares no keyword, so the grep finds the anchors, not the semantic equivalence).

## Invariants

### INV-1: functional-identity-preserved
Across the legibility and de-dup changes, every surface stays a valid interim SDD artifact: all anchors resolve, traceability holds (SPEC O/INV ↔ TASK coverage, and every citation), and each artifact's stage ownership is unchanged. Verified by the structural validator.

### INV-2: leanness-not-regressed
No change increases a surface's prose reading load: each surface stays within its prose budget, and de-dup plus conclusion-first net-reduce or hold it — never inflate. The absolute-budget half is backstopped by the surface-budget guard; non-inflation is a *delta* the stateless guard cannot see (it checks size, not change), so it is verified by inspecting the diff.

## Non-goals
- New automated conformance checks (a conclusion-first or de-dup linter) are not required by this contract — conformance is verifiable by inspection; whether any is automated is DESIGN's concern.
- Re-deriving what each artifact contains or its stage role is excluded; this contract sharpens surface legibility and de-dup alongside the existing per-stage contracts, not in place of them.
- The already-orthogonal seams (RATIONALE vs RESEARCH vs DESIGN; DESIGN vs TASK tech-realization) stay out of scope.
