# 260620-lean-review-surfaces — Spec

## Behavior
### B-1: surface-graspable-at-skim-depth
When a reviewer skims any surface artifact (Requirements, Spec, Design, Tasks) — reading only headings and each block's lead line — its bottom line is recoverable: what it decides and what to check, without reading any block to its end. Design and Tasks reach the bar Requirements and Spec already hold. One-shot test: skim-read a surface; its decisions and check-points are recoverable.

### B-2: one-canonical-home-per-fact
When any cross-cutting fact — a property, policy, or invariant — is searched across the chain, it surfaces as one authored prose statement plus bare `…#…` anchors; no other occurrence re-paraphrases it. The artifact contract makes that ownership unambiguous, including the currently-blurred seam where a continuous property could read as either a Requirements system-policy or a Spec invariant. (Which artifact owns each kind of fact is Design's concern.) One-shot test: grep the fact → one prose home + bare anchors; a reviewer confirms no occurrence restates it in different words (a paraphrase shares no keyword, so the grep finds the anchors, not the semantic equivalence).

## Constraint
### C-1: functional-identity-preserved
Across the legibility and de-dup changes, every surface stays a valid interim SDD artifact: all anchors resolve, traceability holds (Spec B/C ↔ Tasks coverage, and every citation), and each artifact's stage ownership is unchanged. Verified by the structural validator.

### C-2: leanness-not-regressed
No change increases a surface's prose reading load: each surface stays within its prose budget, and de-dup plus conclusion-first net-reduce or hold it — never inflate. The absolute-budget half is backstopped by the surface-budget guard; non-inflation is a *delta* the stateless guard cannot see (it checks size, not change), so it is verified by inspecting the diff.

## Non-goals
- New automated conformance checks (a conclusion-first or de-dup linter) are not required by this contract — conformance is verifiable by inspection; whether any is automated is Design's concern.
- Re-deriving what each artifact contains or its stage role is excluded; this contract sharpens surface legibility and de-dup alongside the existing per-stage contracts, not in place of them.
- The already-orthogonal seams (Rationale vs Research vs Design; Design vs Tasks tech-realization) stay out of scope.
