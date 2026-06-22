# LeanPlan User Guide

LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work. This guide is for humans using LeanPlan with an agent. It explains how to start, what to expect from each stage, and where to look next.

Canonical agent procedure still lives in `references/*.md` and the runtime adapters. This guide explains that procedure for human readers; it does not replace the agent-facing instructions.

## How to use this guide

Read only as deep as you need:

1. **Quickstart** gives the shortest complete first-use path.
2. **Using LeanPlan** is the workflow guide for returning users.
3. **Reference** is the compact lookup area for commands, artifacts, validation, and troubleshooting.

If this is your first LeanPlan run, start with Quickstart and stop when your first feature plan is validated and ready to implement.

## Part 1: Quickstart

### What you need before starting

- LeanPlan installed in `~/.local/share/leanplan/`.
- A repository where feature plans live under `docs/features/`.
- A supported agent runtime with the LeanPlan skill or commands installed.
- A feature small enough to fit one deployment-sized change.

LeanPlan works best when the feature has real implementation value, visible review value, and clear boundaries. If the work is really a product area, split out the first deployment-sized slice.

### First-use path

#### 1. Create the feature directory

From the repository where you will plan the feature:

```bash
~/.local/share/leanplan/scripts/leanplan-new "short feature title"
```

The script prints the new feature path, usually under `docs/features/<KEY>`. Keep that path visible; later commands use the `<KEY>`.

What you do: name the feature in human terms.

What LeanPlan produces: a feature directory with the standard artifact files.

How you know this step is complete: the feature directory exists and you know its `<KEY>`.

#### 2. Capture Requirements

Ask your agent to run the LeanPlan Requirements stage for the feature:

```text
$leanplan requirements "short feature title"
```

In Claude Code, use the installed LeanPlan slash command for the same stage, for example:

```text
/requirements "short feature title"
```

What you do: explain the user problem, boundaries, desired outcome, and any constraints the agent should preserve.

What the agent does: turns that input into a compact Requirements artifact plus any archive notes needed to keep rationale without bloating the surface artifact.

What LeanPlan produces: `requirements.md`, and possibly supporting archive material in the feature directory.

How you know this step is complete: the Requirements artifact states the problem, scope, and success shape clearly enough that the next stage can derive behavior from it.

#### 3. Derive the Spec

Ask the agent to run the Spec stage for the same `<KEY>`:

```text
$leanplan specify <KEY>
```

What you do: answer product-behavior questions and correct anything that does not match the intended user-visible behavior.

What the agent does: derives behavioral requirements and constraints from Requirements without turning them into implementation design.

What LeanPlan produces: `spec.md`.

How you know this step is complete: the Spec names the observable behavior and constraints reviewers will care about.

#### 4. Derive the Design

Ask the agent to run the Design stage:

```text
$leanplan design <KEY>
```

What you do: choose between important implementation approaches when the agent surfaces tradeoffs.

What the agent does: maps the Spec to implementation decisions while preserving traceability back to the behavior and constraints.

What LeanPlan produces: `design.md`.

How you know this step is complete: the Design explains the chosen approach, rejected alternatives where relevant, and the boundaries implementation must preserve.

#### 5. Derive Tasks

Ask the agent to run the Tasks stage:

```text
$leanplan tasks <KEY>
```

What you do: review the dependency order and confirm the task split still represents one deployment-sized feature.

What the agent does: turns the Design into task cards with goals, completion criteria, dependencies, and load-bearing citations.

What LeanPlan produces: `tasks.md`.

How you know this step is complete: the task DAG is reviewable, every task has observable completion criteria, and the next unblocked task is clear.

#### 6. Validate the plan

Run the validator on the feature directory:

```bash
python3 ~/.local/share/leanplan/scripts/validate.py docs/features/<KEY>
```

What you do: treat validation failures as plan defects, not formatting annoyances.

What the validator does: checks the LeanPlan artifact contract, including required sections, traceability, and coverage.

What LeanPlan produces: validator output.

How you know this step is complete: validation exits successfully, or you have a specific issue to fix before implementation.

#### 7. Implement the first task

Ask the agent to implement the first unblocked task from `tasks.md`:

```text
$leanplan implement <KEY> <task-id>
```

What you do: stay available for decision points, especially ambiguous behavior, scope expansion, or changes that would affect users.

What the agent does: reads the task card, load-bearing citations, and current code, then implements the smallest meaningful change for that task.

What LeanPlan produces: code or documentation changes in the repository, with the important rationale moved out of the temporary plan and into durable project surfaces when needed.

How you know the first LeanPlan flow is complete: the first task's completion criteria are satisfied, and any important WHY from the plan has a durable home outside the transient feature artifacts.

### Where to go next

After the first-use path, continue based on what you need:

- For the full stage-by-stage workflow, continue to [Part 2: Using LeanPlan](#part-2-using-leanplan).
- For command and artifact lookup, jump to [Part 3: Reference](#part-3-reference).
- For framework internals, read [`framework-design.md`](./framework-design.md).
- For agent procedure, read the canonical files under [`references/`](./references/).

## Part 2: Using LeanPlan

This part is for returning users who want to understand the full LeanPlan flow and the places where human judgment matters.

LeanPlan has five planned stages followed by task implementation:

1. **Requirements** captures the problem, scope, and success shape.
2. **Spec** derives observable behavior and constraints.
3. **Design** chooses the implementation approach.
4. **Tasks** breaks the design into a dependency-ordered implementation DAG.
5. **Implementation** lands one task at a time in current code.

The plan artifacts are temporary feature scaffolding. They should make implementation and review better, but they are not meant to become permanent product documentation. Important decisions and constraints should migrate into code, tests, types, PR text, or other durable project surfaces as the feature lands.

### Requirements

Purpose: establish what problem this feature solves, what is in scope, what is out of scope, and what success looks like.

User decision points:

- Confirm the feature is one deployment-sized change.
- Name the users, outcomes, and constraints that matter.
- Challenge vague goals before they become downstream design assumptions.

Artifact responsibility: `requirements.md` owns the feature intent. It should be compact enough to load repeatedly and specific enough that later stages can derive behavior from it.

Hand-off: move to Spec when the problem, scope, and success shape are clear enough to derive observable behavior.

### Spec

Purpose: translate Requirements into user-visible behavior and constraints without choosing the implementation.

User decision points:

- Confirm the behavior is observable.
- Decide how edge cases should behave.
- Separate hard constraints from preferences.

Artifact responsibility: `spec.md` owns behavior and constraints. It should say what must be true from the user's or system's point of view, not how the code will achieve it.

Hand-off: move to Design when the behavior and constraints are concrete enough to support implementation tradeoffs.

### Design

Purpose: choose the implementation approach that satisfies the Spec in the current codebase.

User decision points:

- Choose among meaningful implementation alternatives.
- Confirm tradeoffs, boundaries, and non-goals.
- Push back if the design changes observable behavior rather than implementing the agreed behavior.

Artifact responsibility: `design.md` owns the selected approach and the rationale needed for review. It should connect decisions to behavior and constraints without restating the full Spec.

Hand-off: move to Tasks when the implementation approach is clear enough to split into ordered work.

### Tasks

Purpose: turn the Design into a dependency-ordered set of implementation cards.

User decision points:

- Confirm the task split is reviewable.
- Check that each task has observable completion criteria.
- Challenge task cards that are too broad, too mechanical, or missing verification signals.

Artifact responsibility: `tasks.md` owns the implementation DAG, task goals, dependencies, completion criteria, and load-bearing citations back to the plan.

Hand-off: move to implementation when the first unblocked task is clear and its completion criteria are testable or otherwise observable.

### Implementation

Purpose: land one task against current code or documentation.

User decision points:

- Resolve ambiguity when current code contradicts the plan.
- Decide whether scope expansion should be split into a new feature.
- Review the durable rationale that remains after transient plan artifacts stop mattering.

Artifact responsibility: implementation consumes `tasks.md` and the cited plan anchors, but the delivered repository must carry the important WHYs in stronger places: code shape, tests, annotations, comments when justified, commit messages, or PR text.

Hand-off: continue to the next unblocked task, revise the plan if implementation discovers drift, or close the feature when every task is complete.

### Off-pipeline moves

LeanPlan includes two moves for moments when the planned path is no longer enough:

- **sharpen** is a reflect-and-re-derive move when understanding shifts but the committed artifacts do not need direct edits yet. Use it to clarify what changed before continuing.
- **revise** is the artifact update path when implementation or review discovers that a Requirements, Spec, Design, or Tasks artifact is wrong or stale. Use it to update the highest affected layer and then re-evaluate downstream artifacts.

Use these moves when the plan and reality disagree. Do not silently patch around upstream wrongness in the current task.

### Mechanisms LeanPlan uses

The mechanisms below are visible to users because they affect what the agent asks for, what it writes, and when it stops.

#### Brevity controls

What you see: LeanPlan pushes artifacts to stay short and focused.

Why it exists: LLMs perform better when the working set is compact and relevant. Long artifacts hide the current decision inside stale or duplicated context.

How to work with it: keep surface artifacts lean, move detailed rationale into archive material when needed, and cite instead of restating the same fact in multiple places.

When to challenge it: if a short artifact no longer carries enough intent for implementation or review, add the missing constraint in the artifact that owns it instead of relying on memory.

#### Stage ownership

What you see: each stage owns a different kind of fact.

Why it exists: one prose home per fact reduces drift. Requirements own intent, Spec owns behavior, Design owns approach, Tasks own execution order, and implementation owns durable delivered rationale.

How to work with it: place new information in the highest artifact it affects. If a behavior changes, update Spec before Design or Tasks.

When to challenge it: if the same fact appears in several artifacts, remove duplication or keep only a citation where the downstream artifact needs a pointer.

#### Surface and archive layering

What you see: the main artifacts stay compact, while longer rationale can live in supporting archive material.

Why it exists: reviewers and agents need the current decision path quickly, but deeper history should still be recoverable when it matters.

How to work with it: keep the main artifact decision-ready. Move detailed exploration, rejected alternatives, and long analysis out of the surface artifact unless the next stage must read it every time.

When to challenge it: if a downstream task cannot be done safely without opening an archive every time, promote the needed constraint into the surface artifact.

#### Traceability

What you see: later artifacts point back to earlier behavior, constraints, and decisions.

Why it exists: implementation should not become a disconnected task list. Traceability keeps a task tied to the reason it exists and helps reviewers see whether the delivered work still satisfies the original intent.

How to work with it: preserve meaningful links while planning, then carry the substance of important constraints into durable project surfaces during implementation.

When to challenge it: if a citation points to an anchor whose substance no longer matches the task, revise the plan rather than treating the citation as decorative.

#### Validation

What you see: `validate.py` checks feature artifacts and reports contract problems.

Why it exists: LeanPlan uses lightweight automation to catch missing sections, broken coverage, and shape drift before implementation relies on a bad plan.

How to work with it: run validation before implementation and after plan edits. Treat failures as signals that the plan needs correction.

When to challenge it: validation checks artifact structure and coverage, not whether the product decision is wise. Human review still owns product judgment and implementation quality.

#### Stop-the-line moments

What you see: the agent pauses instead of continuing when it finds contradictions, missing verification paths, invalid dependencies, externally visible behavior changes, unprovable constraints, or scope expansion.

Why it exists: continuing through known drift creates plans that look valid but no longer describe the work being done.

How to work with it: resolve the highest affected layer first, usually through revise, then continue implementation.

When to challenge it: if the pause is caused by uncertainty rather than real drift, answer the decision directly and continue without expanding the plan.

## Adoption guidance

LeanPlan is most useful when a team wants better collaboration with an agent on bounded feature work, not when it wants a heavyweight permanent specification system.

### Good first projects

Choose a first project that has:

- A visible user or maintainer outcome.
- A deployable slice that can land in one reviewable change set.
- Enough ambiguity to benefit from structured thinking.
- Clear current code or documentation that implementation can inspect.

Avoid starting with broad platform rewrites, open-ended research, or work whose success cannot be observed. Split those into a first concrete slice before using LeanPlan.

### Gradual adoption path

You do not need to adopt every discipline at once.

1. Start by using LeanPlan for Requirements through Tasks, then implement normally.
2. Add validation once the team is comfortable with the artifact shapes.
3. Use implementation-stage discipline when task cards and citations are proving useful.
4. Add sharpen and revise when the team starts catching drift mid-feature.

The goal is better decisions and handoffs, not ceremony. If a step does not improve implementation or review, inspect whether the feature is too small, too broad, or being forced into the wrong artifact.

### Collaboration expectations

The human owns intent, tradeoffs, and acceptance of behavior. The agent owns careful derivation, consistency checks, code investigation, and scoped implementation. LeanPlan works when both sides treat artifacts as shared working memory, not as paperwork.

Expect the agent to ask when:

- Scope may exceed one deployment-sized feature.
- The current code contradicts the plan.
- A completion criterion has no observable verification path.
- A decision would change externally visible behavior.

### Misuse signals

LeanPlan is probably being used outside its intended shape when:

- The feature plan becomes a permanent canonical spec.
- The task list reads like a script rather than intent plus constraints.
- The agent implements downstream artifacts after discovering upstream drift.
- The same rationale is copied into multiple artifacts.
- Validation is treated as a substitute for product or code review.
- The feature cannot be explained as one deployable slice.

## Part 3: Reference

This part is for quick lookup. It is intentionally compact; use the earlier sections when you need explanation and `references/*.md` when you need canonical agent procedure.

### Commands

Codex form:

```text
$leanplan requirements "short feature title"
$leanplan specify <KEY>
$leanplan design <KEY>
$leanplan tasks <KEY>
$leanplan implement <KEY> <task-id>
```

Claude Code slash-command form:

```text
/requirements "short feature title"
/specify <KEY>
/design <KEY>
/tasks <KEY>
/implement <KEY> <task-id>
/sharpen <what-shifted>
/revise <KEY>
```

Utility scripts:

```bash
~/.local/share/leanplan/scripts/leanplan-new "short feature title"
python3 ~/.local/share/leanplan/scripts/validate.py docs/features/<KEY>
python3 ~/.local/share/leanplan/scripts/validate.py --stage tasks docs/features/<KEY>
python3 ~/.local/share/leanplan/scripts/validate.py --strict docs/features/<KEY>
```

### Artifact responsibilities

| Artifact | Owns | Does not own |
|---|---|---|
| `requirements.md` | Problem, scope, success shape | Behavior details or implementation approach |
| `spec.md` | Observable behavior and constraints | Code structure or task order |
| `design.md` | Chosen approach, tradeoffs, boundaries | Product intent or task execution |
| `tasks.md` | DAG, task cards, completion criteria, dependencies | Canonical product rationale |
| Archive material | Deeper rationale and exploration | Facts every downstream stage must always load |
| Code, tests, PR text | Durable delivered rationale | Round-local planning handles |

### Stage transition cues

| From | Move on when | Stop when |
|---|---|---|
| Requirements to Spec | Intent and scope are clear | The feature is not one deployable slice |
| Spec to Design | Behavior and constraints are observable | Behavior is still ambiguous |
| Design to Tasks | Approach and boundaries are chosen | Tradeoffs are unresolved |
| Tasks to implementation | First unblocked task is clear | Completion cannot be verified |
| One task to next task | Criteria are satisfied and rationale is durable | Implementation found upstream drift |

### Review expectations

- Requirements review asks whether the right problem and boundary are captured.
- Spec review asks whether behavior and constraints are observable and complete enough.
- Design review asks whether the chosen approach satisfies the Spec in the current codebase.
- Tasks review asks whether the DAG is coherent, scoped, and verifiable.
- Implementation review asks whether the delivered change satisfies the task and carries important rationale outside transient plan artifacts.

### Validation modes

| Mode | Use when |
|---|---|
| `validate.py docs/features/<KEY>` | Checking the full feature artifact set before implementation or review |
| `--stage requirements` | Iterating on Requirements only |
| `--stage spec` | Iterating on Spec and its coverage shape |
| `--stage design` | Iterating on Design after Spec is stable |
| `--stage tasks` | Checking task coverage and DAG shape |
| `--strict` | CI or pre-commit should treat warnings as failures |
| `--json` | Tooling needs machine-readable output |
| `--allow-large` | You intentionally accept size guardrail warnings for a special case |

### Common failure signals

| Signal | Likely response |
|---|---|
| The feature keeps growing | Split to the next deployment-sized slice |
| Behavior changes during implementation | Revise from the highest affected artifact |
| The agent needs many unrelated files loaded at once | Narrow the task or improve artifact ownership |
| Completion criteria are subjective | Rewrite them around observable evidence |
| A task only says "implement the design" | Add task-specific goal, constraints, and completion criteria |
| The guide and references seem to disagree | Treat `references/*.md` and adapters as canonical agent procedure, then fix the human-facing explanation |
