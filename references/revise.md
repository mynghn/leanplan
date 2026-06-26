# LeanPlan Revise Move

This doc carries the procedure for the revise move — the single sanctioned, any-stage entry for injecting a *justified* drift into committed artifacts and propagating it downstream-only. Not a stage edge: it is invoked in place at any in-flight occasion — a stage boundary, between tasks, or mid-task during implementation — edits the corrected artifact plus the downstream it implicates, and returns control to the stage it paused.

**Move stance.** You are repairing committed artifacts against a drift that has already been justified — not re-judging whether the drift is real, and not rewriting from a blank slate. A `Delta` records *that* the understanding moved and *why*; revise trusts it and propagates the correction. revise is the **repair** half of a pair whose **cognitive** half is `leanplan-rethink` (`rethink.md`): rethink decides the understanding moved and emits the Delta, never editing; revise consumes the Delta and edits. The two characteristic failures are **mutating without justification** (editing committed work on an unrecorded whim — the silent drift the move exists to prevent, now in your own hand) and **rippling upstream** (repairing a spec error by also rewriting the requirement that was never wrong). The discipline: edit only downstream of the artifact the drift corrects, preserve every surviving anchor ID, and re-validate before done.

Companion: `philosophy.md` (principles), `artifact-contract.md` (shape rules — anchors, retire-by-note, traceability).

## Inputs

- `<cwd>/docs/features/<KEY>/` — the feature's committed artifacts. The corrected artifact and its downstream are edited; everything upstream is read-only.
- The justification — a `Delta-<N>` block in `understanding-shifts.md` (`artifact-contract.md` → Understanding Shifts). Either named at invocation (the `leanplan-rethink` handoff, or a hand-up from an implementation stop-the-line) or recorded at intake from the planner's asserted drift before any edit. With no Delta and no recordable justification, stop without mutating.
- The Delta's scope-of-impact — its bare `Spec#` / `Design#` / `Tasks#` citations name the committed work the drift bears on. JIT-load only those anchors. (context-engineering: jit-loading)

## Output

- The corrected artifact and every downstream artifact the drift implicates, revised in place — surviving anchor IDs preserved, superseded items retired-by-note, the committed set re-validated and carrying no reference to superseded content.
- A durable `Delta-<N>` in `understanding-shifts.md` justifying the change (recorded at intake when not already present), which the revised artifacts may cite as `Understanding#Delta-N-slug`.
- Zero edits to any artifact upstream of the corrected one.

## Procedure

*Default flow, not a rigid script — re-reason against the actual artifacts. Load-bearing (don't skip or reorder): justification before any edit (step 1), inject at the corrected artifact and stay downstream (step 2), preserve IDs (step 3), re-validate (step 5).*

1. **Intake the justification.** Consume the named `Delta-<N>`, or record one from the planner's asserted drift *before* touching any artifact. No justification → stop: revise never mutates committed work on an unrecorded whim. The move is **cause-agnostic** — a reality shift, a change of mind, or a latent error caught late all enter the same way, distinguished only by what the Delta records. Do not re-adjudicate a *contested* drift; verifying that the understanding truly moved belongs to `leanplan-rethink`, not this move.
2. **Identify the corrected artifact, and stay downstream of it.** From the Delta's scope-of-impact, find the *highest* artifact the drift actually corrects — Requirements for problem scope, Spec for the contract, Design for realization, Tasks for sequencing. Inject the correction there and leave every upstream artifact byte-unchanged. A drift detected late but rooted earlier is injected at its root, never rippled upward.
3. **Edit, preserving identity.** Re-evaluate the corrected artifact **in place** by default — a local edit that keeps stable anchor IDs. Escalate to **re-derivation** (re-run the stage skill from the corrected upstream) only when the change is *structural*: the anchor set itself must change, not just prose inside stable anchors. Either way, surviving IDs are never renumbered, and superseded items are retired-by-note `(retired)`, not deleted (`artifact-contract.md` → Anchors).
4. **Propagate downstream-only.** Walk each downstream artifact whose content depends on the change, in stage order, applying the same in-place-default / re-derive-on-structural rule. Leave no downstream artifact citing or restating the superseded content.
5. **Re-validate.** Run `leanplan-validate` on the feature; the committed set must pass and carry no surviving reference to superseded content. A revised artifact's `Understanding#Delta-N-slug` citation of its justifying Delta is resolution-checked.
6. **Scope-gate.** If the correction would push Requirements past one-deployment size, stop and split rather than grow — the structural path, not an inline edit (see **Structural operations**).

## Structural operations

A feature **rename** or **split** is a first-class revise operation, not improvised dir surgery — both route through the single allocator (`leanplan-new`) so nothing is left stranded.

- **Rename is mechanical.** Run `leanplan-new --rename <old> <new>`: it moves the dir, rewrites every intra-repo reference to the old path, refreshes the moved artifacts' identity, and re-validates — the reference-rewrite + re-validate is exactly the step a raw `mv` skips. revise's part is only to invoke it; identity changed, not content, so there is nothing further to propagate.
- **Split is judgment-driven** — the response when the scope-gate fires: a justified drift has grown the feature past one-deployment size, or two separable concerns are found tangled in one feature.
  1. **Allocate** the second feature through `leanplan-new` — dir creation stays in the one allocator; never hand-make a feature dir.
  2. **Partition** the anchors and artifact content between the two features. Items that stay keep their IDs — survivors are never renumbered; items that move are re-homed in the new feature's artifacts. Anything superseded in place retires-by-note as usual.
  3. **Propagate** within each resulting feature per the downstream-only / in-place-default rule above.
  4. **Re-validate both** feature dirs; each must pass `leanplan-validate` independently, with no artifact or citation pointing at the other's content unless a cross-reference is intended.

Both operations end where every revise ends — a re-validated committed set. A rename or split that leaves a dangling path, an unread artifact, or a renumbered survivor is not complete.

## Guardrails

- **Justified or nothing.** No Delta, no recordable justification → zero mutation. Recording an *asserted* justification is intake; adjudicating a *contested* one is `leanplan-rethink`.
- **Downstream-only.** Inject at the corrected artifact; never edit upstream of it. Late detection rooted earlier is injected at the root, not rippled upward.
- **Preserve, don't overwrite.** Surviving anchor IDs still resolve and are not renumbered; superseded items retire-by-note so prior review and traceability history stays reconstructable.
- **In-place by default; re-derive only on an anchor-set change.** This is the implementation loop's existing default, generalized to every stage — effort proportional to how far the drift actually reshapes the artifact.
- **Repair, don't re-judge.** revise trusts the Delta it is handed and propagates it; it never re-verifies whether the understanding moved.
- **Re-validate before done.** A revise that leaves the feature failing `leanplan-validate`, or with a surviving reference to superseded content, is not complete.
- **Any stage, including mid-implementation.** The one entry serves a stage boundary, a between-task pause, and a mid-task drift during implementation alike. implementation's stop-the-line triggers *detect* the drift; they delegate the edit-and-propagate to this move (`implement.md`).

## Hand-off

Return control to the stage or task that invoked the move — for a mid-implementation drift, implementation resumes from where it paused, now against a re-validated artifact set. There is no next edge: revise leaves the committed artifacts consistent and the justifying Delta archived for retrieval.
