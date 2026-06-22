# 260621-reflexive-surface-budget — Spec

## Behavior
### B-1: hot-path-fully-adjudicated

Every block of always-resident content in the hot path — each stage reference plus the thin adapter that loads it — carries a recorded verdict: *keep* (genuinely needed on every stage invocation) or *defer* (needed only once a later step in the stage is reached). Each non-obvious *keep* verdict records the context-engineering rationale for staying inline. Verifiable by a one-shot read of the hot path: no always-resident block is left without a verdict.

### B-2: deferred-content-not-always-loaded

For every block carrying a *defer* verdict, that block is absent from the always-loaded surface — it is not loaded when the stage is invoked. Verifiable: the always-loaded reference no longer carries the deferred block.

## Constraint
### C-1: deferral-preserves-guidance

Re-tiering changes only *when* content loads, never *whether* the planner receives it. Content with a *keep* verdict stays in the always-loaded surface; every *deferred* block stays reachable and is delivered to the planner by the step that consumes it. No re-tiering drops or alters the guidance a stage delivered before this feature. A deferred block with no resolvable load-point at its consuming step is a violation.

## Non-goals

- **One-time resolution, not a standing gate.** This contract is satisfied by adjudicating the hot path and realizing its verdicts once; it does not require a new always-on validator rule that caps or polices stage-reference content on every future change. Whether to add such enforcement is left open to a later decision.
