# Adopting LeanPlan

LeanPlan is most useful when a team wants better collaboration with an agent on bounded feature work, not when it wants a heavyweight permanent specification system.

## Good first projects

Choose a first project that has:

- A visible user or maintainer outcome.
- A deployable slice that can land in one reviewable change set.
- Enough ambiguity to benefit from structured thinking.
- Clear current code or documentation that implementation can inspect.

Avoid starting with broad platform rewrites, open-ended research, or work whose success cannot be observed. Split those into a first concrete slice before using LeanPlan.

## Gradual adoption path

You do not need to adopt every discipline at once.

1. Start by using LeanPlan for Requirements through Tasks, then implement normally.
2. Add validation once the team is comfortable with the artifact shapes.
3. Use implementation-stage discipline when task cards and citations are proving useful.
4. Add sharpen and revise when the team starts catching drift mid-feature.

The goal is better decisions and handoffs, not ceremony. If a step does not improve implementation or review, inspect whether the feature is too small, too broad, or being forced into the wrong artifact.

## Collaboration expectations

The human owns intent, tradeoffs, and acceptance of behavior. The agent owns careful derivation, consistency checks, code investigation, and scoped implementation. LeanPlan works when both sides treat artifacts as shared working memory, not as paperwork.

Expect the agent to ask when:

- Scope may exceed one deployment-sized feature.
- The current code contradicts the plan.
- A completion criterion has no observable verification path.
- A decision would change externally visible behavior.

## Misuse signals

LeanPlan is probably being used outside its intended shape when:

- The feature plan becomes a permanent canonical spec.
- The task list reads like a script rather than intent plus constraints.
- The agent implements downstream artifacts after discovering upstream drift.
- The same rationale is copied into multiple artifacts.
- Validation is treated as a substitute for product or code review.
- The feature cannot be explained as one deployable slice.
