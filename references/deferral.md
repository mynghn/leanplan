# LeanPlan Deferral Lane

This doc carries the capture and drain procedures for the forward-deferral lane — the on-demand companion behind the one-line hooks in the stage docs. It loads JIT at two moments: when a stage *captures* a deferred decision, and when a stage *drains* the deferrals addressed to it. The structural shape (anchor, citation, layering) is owned by `artifact-contract.md` → Deferrals; this doc is the procedure.

A deferral is a deliberately-deferred cross-stage decision — a genuine decision that surfaces at the wrong stage. Park it off the review surface so the spark is not lost, the review surface is not bloated, and the later stage is not pinned. The lane lives in `deferrals.md` as append-only `Defer-<N>` blocks, each addressed to the stage that owns the decision.

## Capture — park it, don't discard it

Each stage already has a disposal point where it sets off-altitude content aside: Requirements strips upstream solution suggestions; Spec pushes specifics to Design; Design pushes work-ordering to Tasks; Tasks pushes tech-realization back to Design. At that point, judge what you are setting aside:

- **Noise** — discard it as before. Most set-aside content is noise; capture is the exception, not the rule.
- **A genuine decision another stage owns** — append a `Defer-<N>` block addressed to that stage, instead of discarding it.

Capture is opt-in planner judgment — never auto-detected, never required, never a gate on proceeding. It is a lightweight aside during ordinary stage work, not a ceremony.

The block records the *question*, never an answer — this is what keeps it non-binding:

```markdown
## Defer-1: <slug>

**Owning stage**: <Requirements | Spec | Design | Tasks>

<the open question + why it surfaced now — one or two lines>

Forces: <what pulls on the decision — the tension glimpsed>.

Option seen (not chosen): <at most one candidate noticed, explicitly marked not chosen — omit the line if none>.
```

There is deliberately **no decision field**. A recorded answer would arrive at the owning stage as a fait accompli and pin it — the exact harm the lane exists to prevent. Carry the question and the forces forward; withhold the conclusion.

## Drain — re-examine, decide freshly

At a stage's entry, after loading its inputs, load `deferrals.md` (if it exists) and surface every unresolved `Defer-<N>` addressed to **this** stage — those whose heading carries no `(resolved -> …)` marker. The consultation is load-bearing: it must happen, and a skipped drain is catchable at close-out.

For each surfaced deferral, **re-derive — do not replay**:

1. Read the parked question and forces — the spark, so you do not rebuild it from zero.
2. Re-examine the question against this stage's **full current option space** — richer now than when the spark first appeared, because the upstream artifacts it depends on now exist.
3. Decide freshly. The parked "option seen" is a *candidate to weigh*, never a default to apply — you are free to choose it, choose differently, or judge the question moot.

The drain is high-freedom by design. A low-freedom "apply the deferred option" drain would replay the deferred choice and re-introduce the very pinning the lane prevents. Freedom in the reasoning; rigor only in the fact that the re-examination happened.

## Resolve in place

When you have drained a deferral, retire it in place: append `(resolved -> <Spec#… | Design#… | Tasks#…>)` to its block heading, citing where the decision actually landed. The `Defer-<N>` id keeps resolving in its resolved state — the same retire-in-place convention as ` (retired)`. Append-only; never renumber. If a deferral's question turns out moot, resolve it the same way, citing where the matter is settled or noting it resolved with no downstream change.

## No deferral is lost

A captured deferral is accounted for — drained at its owning stage, or surfaced as an omission — never silently dropped:

- **Structural** — `validate.py` raises an advisory warning for an unresolved `Defer-<N>` whose owning stage's artifact already exists (escalating under `--strict`). An unresolved deferral for a stage not yet authored is legitimate and unflagged.
- **Substance** — Close-Out Reconciliation (`implement-closeout.md`) carries deferrals as an obligation set: a reviewer judges whether a "resolved" deferral genuinely landed where it cites, the half the validator cannot see.
