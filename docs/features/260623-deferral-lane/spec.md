# 260623-deferral-lane — Spec

## Behavior

### B-1: deferral-captured-on-set-aside
When a planner deliberately sets a decision aside during a stage — because it belongs to a later one — the decision is recorded outside the active working context: the spark that raised it, why it surfaced, and the stage that owns it. Capture is available at any point in ordinary stage work, as a lightweight aside.

### B-2: deferrals-surfaced-at-owning-stage
When a stage begins, the deferrals addressed to it are surfaced to the planner for re-examination, each carrying its original spark and any options already seen.

### B-3: undrained-deferral-flagged-at-close-out
When a stage or round closes, a deferral addressed to it that was never picked up is surfaced as an unresolved omission — not silently dropped.

## Constraint

### C-1: no-deferral-silently-lost
Every captured deferral is accounted for: it is surfaced at its owning stage (B-2) or reported as an omission (B-3). None vanishes between capture and resolution.

### C-2: capture-off-the-review-surface
Capturing deferrals never enlarges the review-surface artifacts (Requirements, Spec, Design, Tasks). What a reviewer reads to review or implement is unchanged by how many deferrals exist.

### C-3: surfaced-deferral-is-non-binding
A surfaced deferral presents as a question to re-decide — the original tension plus any options seen, offered as candidates — never as a settled choice. The owning stage stays free to decide otherwise; the deferral constrains nothing.

### C-4: deferral-and-understanding-records-single-role
The deferral capture and the existing record of mid-round understanding shifts are each single-role and mutually exclusive: any item belongs unambiguously to one — an *open* item to revisit, or a *committed* change to propagate — never plausibly both, and neither record is a catch-all whose scope a reader must guess.

### C-5: capture-durable-across-resets
A captured deferral persists beyond the working session that produced it and stays retrievable by its owning stage, surviving a context reset or compaction.

### C-6: capture-is-opt-in-judgment
Deferring a decision is the planner's write-time judgment: never auto-detected, never required, and never a precondition that blocks a stage from proceeding.

## Non-goals

- A general-purpose notes or scratchpad surface — only deliberately-deferred cross-stage decisions are in scope; arbitrary thoughts, reminders, and open questions are not.
