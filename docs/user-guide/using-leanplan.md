# Using LeanPlan

This page is for returning users who want to understand the full LeanPlan flow and the places where human judgment matters.

LeanPlan has five stages: four planning stages, then implementation:

1. **Requirements** captures the problem, scope, and success shape.
2. **Spec** derives observable behavior and constraints.
3. **Design** chooses the implementation approach.
4. **Tasks** breaks the design into a dependency-ordered implementation DAG.
5. **Implementation** lands one task at a time in current code.

The plan artifacts are temporary feature scaffolding. They should make implementation and review better, but they are not meant to become permanent product documentation. Important decisions and constraints should migrate into code, tests, types, PR text, or other durable project surfaces as the feature lands.

## Requirements

Purpose: establish what problem this feature solves, what is in scope, what is out of scope, and what success looks like.

User decision points:

- Confirm the feature is one deployment-sized change.
- Name the users, outcomes, and constraints that matter.
- Challenge vague goals before they become downstream design assumptions.

Artifact responsibility: `requirements.md` owns the feature intent. It should be compact enough to load repeatedly and specific enough that later stages can derive behavior from it.

Hand-off: move to Spec when the problem, scope, and success shape are clear enough to derive observable behavior.

## Spec

Purpose: translate Requirements into user-visible behavior and constraints without choosing the implementation.

User decision points:

- Confirm the behavior is observable.
- Decide how edge cases should behave.
- Separate hard constraints from preferences.

Artifact responsibility: `spec.md` owns behavior and constraints. It should say what must be true from the user's or system's point of view, not how the code will achieve it.

Hand-off: move to Design when the behavior and constraints are concrete enough to support implementation tradeoffs.

## Design

Purpose: choose the implementation approach that satisfies the Spec in the current codebase.

User decision points:

- Choose among meaningful implementation alternatives.
- Confirm tradeoffs, boundaries, and non-goals.
- Push back if the design changes observable behavior rather than implementing the agreed behavior.

Artifact responsibility: `design.md` owns the selected approach and the rationale needed for review. It should connect decisions to behavior and constraints without restating the full Spec.

Hand-off: move to Tasks when the implementation approach is clear enough to split into ordered work.

## Tasks

Purpose: turn the Design into a dependency-ordered set of implementation cards.

User decision points:

- Confirm the task split is reviewable.
- Check that each task has observable completion criteria.
- Challenge task cards that are too broad, too mechanical, or missing verification signals.

Artifact responsibility: `tasks.md` owns the implementation DAG, task goals, dependencies, completion criteria, and load-bearing citations back to the plan.

Hand-off: move to implementation when the first unblocked task is clear and its completion criteria are testable or otherwise observable.

## Implementation

Purpose: land one task against current code or documentation.

User decision points:

- Resolve ambiguity when current code contradicts the plan.
- Decide whether scope expansion should be split into a new feature.
- Review the durable rationale that remains after transient plan artifacts stop mattering.

Artifact responsibility: implementation consumes `tasks.md` and the cited plan anchors, but the delivered repository must carry the important WHYs in stronger places: code shape, tests, annotations, comments when justified, commit messages, or PR text.

Hand-off: continue to the next unblocked task, revise the plan if implementation discovers drift, or close the feature when every task is complete.

## Off-pipeline moves

When the plan and reality disagree, LeanPlan has two off-pipeline moves — **sharpen** (record a shift in understanding without editing artifacts yet) and **revise** (update the highest affected artifact, then re-evaluate downstream). Reach for them instead of silently patching around upstream wrongness in the current task. See [`mechanisms.md` → Sharpen and revise](./mechanisms.md#sharpen-and-revise) for how each works and when to challenge their use.

## Deferred decisions

Sometimes a real decision surfaces at a stage that does not own it — Requirements hits a solution idea, Spec hits an implementation specific. Rather than deciding early (which pins the owning stage) or discarding it (which loses the spark), the planner can park it as a **forward deferral**: a `Defer-N` entry in `deferrals.md`, addressed to the later stage that owns it. That stage drains the entries addressed to it at its entry and decides freshly.

- Capture is opt-in judgment, not a gate — record the *question* and the forces behind it, never a pre-baked answer.
- It only ever points forward. A decision an *earlier*, already-run stage owns is drift, not a deferral — that is sharpen/revise.
- `leanplan-validate` surfaces an unresolved deferral once its owning stage's artifact exists, so a parked decision is never silently dropped.

## Next

- Read [`mechanisms.md`](./mechanisms.md) for the framework behavior behind the workflow.
- Read [`reference.md`](./reference.md) for quick command and artifact lookup.
- Back to [`USER_GUIDE.md`](../../USER_GUIDE.md) for the entry path and Quickstart.
