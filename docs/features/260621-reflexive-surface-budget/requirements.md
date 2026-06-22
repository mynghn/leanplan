# 260621-reflexive-surface-budget — apply the framework's own surface/JIT discipline to its always-loaded stage references

## Problem

The framework's signature claim — that it is *designed the way it tells you to design* — has a hole on its own hot path. It caps user artifacts with a Surface Budget and preaches surface-the-essential, archive-the-rest, load-the-rest-on-demand; yet every stage invocation loads a stage reference (the `requirement`…`impl` docs, 45–106 lines) that bundles stance, full procedure, guardrails, worked examples, and template into one always-resident block, with no internal load-on-demand tier — the close-out reference is even larger than the artifact whose size cap it polices. The one body of text that never gets the surface-and-archive treatment the framework prescribes is the framework's own. This is the sharpest self-conformance miss a full-framework adversarial review surfaced: whoever weighs the framework against its central thesis sees it break its own rule, and at runtime the planner carries that reference bloat in-window on every stage call — taxing the very attention budget the framework warns about.

## Outcome

The framework holds its own always-loaded references to the same surface-budget-and-load-on-demand discipline it enforces on user artifacts. Each stage reference is audited — content needed on every call vs. content needed only when a later step arrives — and resolved *honestly*; trimming is an option, never an obligation. Scope is the always-loaded hot path (the stage references and their thin adapter), not what the stages themselves do.

User stories:

- **Leaner always-loaded surface where deferral wins** — when the audit judges reference content needed only at a later step (e.g. close-out distillation), that content is loaded when the step is reached instead of carried in-window on every stage call.
- **A recorded verdict on every reference** — each always-loaded stage reference ends resolved: trimmed to genuinely always-needed content, or kept inline with a written context-engineering rationale. Some content is correctly inline — a worked example that *is* the author-time calibration — and the verdict records that judgment instead of forcing a deferral.

Success holds when an adversarial re-read of the always-loaded hot path finds no always-resident content lacking a recorded verdict: every reference is either leaner or justified, closing the reflexive gap whichever way each call lands.

## Non-goals

- **Not shrinking references for their own sake.** The win is the recorded decision, not a lower line count; a reference may legitimately end unchanged.
- **Not changing what the stages do.** Only how each reference's content is tiered and loaded — the procedures, guardrails, and stances themselves are untouched.

## Upstream

- [Backlog "I" — issue #25](https://github.com/mynghn/leanplan/issues/25) — origin tracker for this feature.
- Source: full-framework adversarial-review verdict ([PR #24](https://github.com/mynghn/leanplan/pull/24) comment) — the reflexive gap this feature closes.
