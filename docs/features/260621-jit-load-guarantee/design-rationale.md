# 260621-jit-load-guarantee — Design Rationale

Decision record: among three enforcement weights — pure review (lightest), a greppable floor (middle), a validator-gated receipt (heaviest) — the **middle** was chosen (2026-06-22). It buys a structured, enumerable obligation against the rubber-stamp failure mode without standing up new framework machinery. A late constraint — *no round-local identifier may leak into the product* (`implement-closeout.md` "substance, not the key") — relocated the floor from a commit/PR marker to an in-round reconciliation, which turned out lighter than the marker it replaced.

## D-1: mandatory-substance-distillation

**Forces.** `Spec#B-1-load-bearing-consultation-observable` needs the act of consulting a load-bearing anchor to leave an observable trace. Two constraints squeeze the trace's form: it must not stamp a round-local handle into the durable product (the "substance, not the key" rule), and it must not add standing prose to the review surface (`Spec#C-2-surface-no-less-lean`).

**Alternatives considered.**
- *A new consultation marker that names the anchor in the product* (e.g. a code annotation or commit line `satisfies D-2`). Rejected: it carries the handle, not the reason — the precise failure `implement-closeout.md` warns of. It also *feels* like proof while being forgeable by copying the slug, the very gap M exists to close.
- *Eager-load the cited content onto the card.* Rejected: abandons the leanness bet (a requirement non-goal); defeats the deferral the surface depends on.

**Chosen path.** Reuse the distillation already mandated at close-out and make it load-bearing for the load-bearing class: the consulted constraint must land in the product **as substance**. This needs no new signal — the substance *is* the signal. It is leak-free by construction: the reason in words ("at-least-once; duplicates tolerated") cannot be written without consulting the anchor, whereas the handle can be copied blind. The rule that forbids the handle is the same rule that makes the proof load-bearing — a reflexive fit with the framework rather than a bolt-on.

**Invalidation triggers.** If a future change made round-local handles durably resolvable (a permanent spec registry that does not dangle when a plan is discarded), the "substance, not the key" premise weakens and a resolvable reference could legitimately serve as the signal. If implementation stopped migrating WHYs into code/commit/PR (a process change), the signal's home would disappear and the mechanism would need a new tier.

## D-2: in-round-reconciliation

**Forces.** `Spec#B-2-skipped-needed-load-surfaceable` needs a skip to be catchable at review rather than passing as silently compliant. The chosen form must be a genuine *floor* against rubber-stamping — a charitable reviewer waves through exactly this silent gap — yet must not leak handles into the product, add a new artifact, or grow the surface.

**Alternatives considered.**
- *A `Consulted: Spec#…` trailer in the commit or PR body.* This was the initial middle-weight design. Rejected on review: a commit/PR is permanent history — the product side — so the trailer stamps round-local handles into exactly the place the "substance, not the key" rule protects. The leak the design otherwise avoids.
- *A new archive-tier consultation ledger, validator-enforced.* Rejected: it duplicates the load-bearing citations the plan card already lists; it introduces an artifact kind with no precedent across the existing features; and the validator reads only artifacts, so it could assert a ledger entry is *present* but never that it is *genuine* — presence-only theater at real maintenance cost.
- *Pure review with no enumerated obligation.* Rejected: it is the lightest, but offers no floor — the reviewer is asked for a gestalt judgment, and the skip is precisely what gestalt review misses.

**Chosen path.** Reconcile the card's already-enumerated load-bearing citations against the substance that landed, at close-out (self-check) and on the review path. The obligation set is derivable from the plan card — a concrete checklist of constraints to find in the diff, far harder to wave through than "looks fine." The handles are read in-round, where tasks.md is still live at review; the product is checked only for substance. No product marker, no new artifact, no surface prose — the floor is the *procedure*, reusing structure that already exists.

**Invalidation triggers.** If plan cards stopped carrying per-task load-bearing citations (a model change), the obligation set would lose its home. If review tooling gained the ability to read code and judge substance mechanically, the discharge could move from review judgment to an automated check — promoting this from middle to heavy weight deliberately.

## D-3: scope-by-citation-prefix

**Forces.** `Spec#C-1-archive-citation-never-force-loaded` requires the guarantee to fire on the always-needed class and never on the archive tier, and the requirement mandates reusing the existing surface/archive boundary rather than inventing a new tag.

**Alternatives considered.**
- *A new "load-bearing" tag on citations.* Rejected: invents the tag the requirement explicitly forbids, when the citation grammar already encodes the distinction.
- *Keying the check on the target kind (`D-N`).* Rejected: `Rationale#D-N` shares the `D-N` target with `Design#D-N` but is archive-tier; keying on the bare target would wrongly sweep archive rationale into the obligation set.

**Chosen path.** Scope the obligation set to the citation **file prefix** — `Spec#(B|C)-…` and `Design#D-…` — which is already first-class in the grammar and in `validate.py`'s `_task_has_reason`. C-1 then holds by construction: `Rationale#` and `Research#` citations are never in scope, so they are never forced to load.

**Invalidation triggers.** If the citation grammar were restructured so the file prefix no longer separated surface from archive (e.g. a unified citation namespace), the discriminator would need to be re-grounded on whatever new signal carries the surface/archive distinction.
