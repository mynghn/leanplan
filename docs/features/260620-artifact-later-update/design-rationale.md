# 260620-artifact-later-update — DESIGN RATIONALE

## Decision-1: revise-unified-editing-entry

The editing capability C needs already exists — it is just trapped inside impl. The impl Artifact Update Loop walks up and edits artifacts; `/sharpen` deliberately stops at emitting a delta. So rather than build a second editing mechanism, C lifts the existing one out of impl into a stage-agnostic skill.

Alternatives weighed:
- **Leave the impl loop in place; add a separate editing path for the other stages.** Rejected: two editing engines drift apart — the exact silent inconsistency C exists to prevent, now in the framework's own machinery. "How an artifact gets revised" must have one home (One-Prose-Home at the mechanism level).
- **Make revise a deterministic script.** Rejected: deciding which downstream items are implicated, and in-place vs re-derive, is judgment — LLM work, like every LeanPlan stage. A script would be too crude or would re-implement an LLM.

Chosen: one editing engine, expressed as a skill; impl's six stop-the-line *triggers* remain impl's (they are impl-time detections) but call `/revise`. This is what makes "during impl" not a special case — it is the same entry as every other occasion.

Invalidation trigger: if impl's triggers come to need editing behavior that genuinely diverges from the other stages', the single-engine bet is wrong and the loop should re-fork.

Scope note (not work-ordering): the target shape is impl delegating to revise; *when* `impl.md` is re-pointed (this feature or a follow-up) is the plan's call and does not change the shape.

## Decision-2: in-place-default-re-derive-on-threshold

This resolves the issue's explicitly-open "re-derive vs re-evaluate-in-place" conflict — and the codebase already leans the answer.

Forces:
- O-3 requires surviving anchor IDs to still resolve and review history to remain after a revision.
- O-2 requires the change to actually reach every implicated downstream artifact.
- Full re-derivation (re-run the stage skill from the corrected upstream) maximizes internal consistency but renumbers/loses anchors and erases history — a direct O-3 violation.
- Pure in-place editing preserves IDs but cannot absorb a change that reshapes an artifact's anchor set.

Chosen: in-place re-evaluation is the default — the same default the impl loop already runs (`impl.md:61`, "re-evaluate in place, not fully re-derive") — escalating to re-derivation only when the anchor set itself must change, and even then preserving surviving IDs and retiring removed ones by note (Decision-3). This is also the operational form of the REQUIREMENT's "effort proportional to volatility": a content-only change stays a cheap local edit; a structural change at a foundational upstream artifact may re-derive — but ID preservation binds both ends of the gradient.

Alternative weighed: always re-derive for guaranteed consistency. Rejected on O-3 (cannot preserve IDs/history) and because it contradicts the framework's existing in-place bet.

Invalidation trigger: validate.py is structural, not semantic (`research.md`), so it will not catch an in-place edit that leaves an artifact semantically inconsistent. If that failure recurs in practice, flip the default toward re-derivation and give the validator a consistency check (the direction Decision-6 opens).

## Decision-4: justified-input-is-a-delta

C must not fire without a justification (INV-1), yet the entry point is *manual* — a planner often brings a drift with no prior `/sharpen` session. The resolution is to make the justification a uniform artifact (a Delta block) regardless of entry path, not to force a sharpen ceremony every time.

Chosen: the justification is always a `Delta-<N>` in `understanding.md`. Either it already exists (the sharpen handoff) or revise records one at intake from the planner's asserted drift before touching any artifact. A durable, uniform audit trail results either way.

The boundary that keeps C from absorbing B (#8): recording an *asserted* justification is not adjudicating a *contested* one. When the planner is unsure the understanding truly moved, or the drift is an external claim to verify, that cognition is `/sharpen`'s — it verifies and emits the delta. revise trusts the delta it is handed and never re-judges it. This is also why C is cause-agnostic: a reality shift, a change of mind, or a latent error caught late all enter the same way, distinguished only by what the Delta records — never by a branch in revise's logic.

Invalidation trigger: if intake-recorded Deltas routinely prove wrong (drifts that did not really move the understanding), the manual path is too loose and should route through sharpen's verification first.

## Decision-5: structural-ops-via-allocator

O-4 wants split/rename to strand nothing; the grounding shows the failure mode (a raw `mv` left design stubs unread at the new path). `leanplan-new` is the framework's single directory allocator but today only allocates.

Chosen split of mechanism:
- **Rename is mechanical** → `leanplan-new --rename <old> <new>`: move the dir, rewrite intra-repo path references, re-validate. The reference-rewrite + re-validate is precisely the step the raw-`mv` improvisation skipped, so "no dangling path, nothing stranded" holds by construction.
- **Split is judgment-heavy** → an LLM-driven revise sub-procedure that allocates the second feature *through* `leanplan-new` (dir creation stays in the one allocator), partitions anchors/artifacts, then propagates per Decision-2. `framework-design.md` §14 already lists divide-and-conquer for oversized work as open; this lands its in-flight half.

Alternative weighed: a standalone `leanplan-mv` separate from the allocator. Rejected — the REQUIREMENT names `leanplan-new` as *the* single allocator to route through; a second dir-touching tool reintroduces the two-homes problem Decision-1 avoids.

Invalidation trigger: if reference-rewrite proves unreliable across the monorepo's reference forms (relative paths, anchors, external docs), move more of rename into the judgment-driven procedure.
