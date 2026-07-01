# LeanPlan Deferral Lane

This doc carries the block shape plus the capture and drain procedures for the forward-deferral lane — the on-demand companion behind the one-line hooks in the stage docs. It loads JIT at two moments: when a stage *captures* a deferred decision, and when a stage *drains* the deferrals addressed to it. The `Defer-<N>` anchor grammar stays in `artifact-contract.md` → Anchors; the block shape (below) and both procedures live here.

A deferral is a deliberately-deferred cross-stage decision — a genuine decision that surfaces too early, at a stage that doesn't own it. Park it off the review surface so the spark is not lost, the review surface is not bloated, and the owning stage is not pinned. The lane lives in `deferrals.md` as append-only `Defer-<N>` blocks, each addressed **forward** to the later stage that owns the decision (a decision owned by an *earlier*, already-run stage is a drift — that is `revise`/stop-the-line, not a deferral).

## Deferral block shape

A deferral is a *sibling* to the understanding-shift archive, never a blend: an understanding delta is a *committed* change to propagate; a deferral is an *open* question to re-decide.

Each `Defer-<N>: <slug>` block is shaped so it cannot read as a settled decision (conclusion-first):

- **Owning stage** — one of Spec / Design / Tasks; the stage the deferral is addressed to.
- the open **question** + why it surfaced now.
- **forces** glimpsed.
- at most an **option seen** — explicitly marked *not chosen*. There is no "decision" field.

IDs are stable; append, never renumber — duplicate `Defer-<N>` anchors are validator-caught.

## Capture — park it, don't discard it

Each stage that has a *later* stage already has a disposal point where it sets off-altitude content aside for it: Requirements strips upstream solution suggestions; Spec pushes specifics to Design; Design pushes work-ordering to Tasks. (Tasks, the last planning stage, has no forward target — what it would "push back to Design" is a drift for `revise`, not a deferral.) At that point, judge what you are setting aside:

- **Noise** — discard it as before. Most set-aside content is noise; capture is the exception, not the rule.
- **A genuine decision another stage owns** — append a `Defer-<N>` block, in the **Deferral block shape** above, addressed to that stage, instead of discarding it.

Capture is opt-in planner judgment — never auto-detected, never required, never a gate on proceeding. It is a lightweight aside during ordinary stage work, not a ceremony.

The capture stance is what matters here: record the *question* and the forces behind it, never an answer. The shape has no decision field by design — a recorded answer would reach the owning stage as a fait accompli and pin it, the exact harm the lane prevents — so carry the question forward and withhold the conclusion.

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

A captured deferral is accounted for — drained at its owning stage, or surfaced as an omission — never silently dropped. `leanplan-validate` raises an advisory warning for an unresolved `Defer-<N>` whose owning stage's artifact already exists (escalating under `--strict`); an unresolved deferral for a stage not yet authored is legitimate and unflagged. Once drained, the `(resolved -> …)` marker cites where the decision landed — a `Spec#` / `Design#` / `Tasks#` anchor that is itself resolution-checked and tracked by that stage's normal coverage, so a resolved deferral needs no separate hunt: follow the decision it became, not the deferral.
