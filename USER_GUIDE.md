# LeanPlan User Guide

LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work. This guide is for humans using LeanPlan with an agent. It explains how to start, what to expect from each stage, and where to look next.

Canonical agent procedure still lives in `references/*.md` and the runtime adapters. This guide explains that procedure for human readers; it does not replace the agent-facing instructions.

## How to use this guide

Read only as deep as you need:

1. **Quickstart** gives the shortest complete first-use path on this page.
2. **Using LeanPlan** explains the full workflow, user decision points, artifact responsibilities, off-pipeline moves, and handoffs in [`docs/user-guide/using-leanplan.md`](./docs/user-guide/using-leanplan.md).
3. **Mechanisms** explains LeanPlan-specific behavior such as brevity controls, stage ownership, traceability, validation, and stop-the-line moments in [`docs/user-guide/mechanisms.md`](./docs/user-guide/mechanisms.md).
4. **Adoption** helps teams decide fit, choose a first project, and avoid misuse in [`docs/user-guide/adoption.md`](./docs/user-guide/adoption.md).
5. **Reference** gives compact lookup tables for commands, artifacts, transitions, validation modes, and failure signals in [`docs/user-guide/reference.md`](./docs/user-guide/reference.md).

If this is your first LeanPlan run, start with Quickstart and continue until the first task has landed. If you only want to evaluate planning, you can stop after validation.

## Quickstart

### What you need before starting

- LeanPlan cloned to a checkout of your choice — call it `$LEANPLAN_ROOT` — with `install.sh` run so the skills are registered (see [`README.md`](./README.md) for install; a dotfile manager like chezmoi is optional, not required).
- A repository where feature plans live under `docs/features/`.
- A supported agent runtime (Claude Code or Codex) with the LeanPlan skills installed.
- A feature small enough to fit one deployment-sized change.

LeanPlan works best when the feature has real implementation value, visible review value, and clear boundaries. If the work is really a product area, split out the first deployment-sized slice.

### First-use path

#### 1. Create the feature directory

From the repository where you will plan the feature:

```bash
"$LEANPLAN_ROOT/scripts/leanplan-new" "short feature title"
```

The script prints the new feature path, usually under `docs/features/<KEY>`. Keep that path visible; later commands use the `<KEY>`.

What you do: name the feature in human terms.

What LeanPlan produces: a feature directory with the standard artifact files.

How you know this step is complete: the feature directory exists and you know its `<KEY>`.

#### 2. Capture Requirements

Ask your agent to run the LeanPlan Requirements stage for the allocated feature:

```text
$leanplan-requirements <KEY>
```

In Claude Code, use the installed LeanPlan slash command for the same stage:

```text
/leanplan-requirements <KEY>
```

Use the `<KEY>` printed by `leanplan-new`. Passing the title again asks the Requirements stage to allocate a new feature, which is useful only when you skipped Step 1 and want the agent to create the directory for you.

What you do: give the agent the existing feature key, then explain the user problem, boundaries, desired outcome, and any constraints it should preserve.

What the agent does: turns that input into a compact Requirements artifact plus any archive notes needed to keep rationale without bloating the surface artifact.

What LeanPlan produces: `requirements.md`, and possibly supporting archive material in the feature directory.

How you know this step is complete: the Requirements artifact states the problem, scope, and success shape clearly enough that the next stage can derive behavior from it.

#### 3. Derive the Spec

Ask the agent to run the Spec stage for the same `<KEY>`:

```text
$leanplan-specify <KEY>
```

In Claude Code: `/leanplan-specify <KEY>`. The later stages follow the same `$leanplan-<stage>` (Codex) / `/leanplan-<stage>` (Claude) pattern.

What you do: answer product-behavior questions and correct anything that does not match the intended user-visible behavior.

What the agent does: derives behavioral requirements and constraints from Requirements without turning them into implementation design.

What LeanPlan produces: `spec.md`.

How you know this step is complete: the Spec names the observable behavior and constraints reviewers will care about.

#### 4. Derive the Design

Ask the agent to run the Design stage:

```text
$leanplan-design <KEY>
```

What you do: choose between important implementation approaches when the agent surfaces tradeoffs.

What the agent does: maps the Spec to implementation decisions while preserving traceability back to the behavior and constraints.

What LeanPlan produces: `design.md`.

How you know this step is complete: the Design explains the chosen approach, rejected alternatives where relevant, and the boundaries implementation must preserve.

#### 5. Derive Tasks

Ask the agent to run the Tasks stage:

```text
$leanplan-tasks <KEY>
```

What you do: review the dependency order and confirm the task split still represents one deployment-sized feature.

What the agent does: turns the Design into task cards with goals, completion criteria, dependencies, and load-bearing citations.

What LeanPlan produces: `tasks.md`.

How you know this step is complete: the task DAG is reviewable, every task has observable completion criteria, and the next unblocked task is clear.

#### 6. Validate the plan

Run the validator on the feature directory:

```bash
"$LEANPLAN_ROOT/scripts/leanplan-validate" docs/features/<KEY>
```

What you do: treat validation failures as plan defects, not formatting annoyances.

What the validator does: checks the LeanPlan artifact contract, including required sections, traceability, and coverage.

What LeanPlan produces: validator output.

How you know this step is complete: validation exits successfully, or you have a specific issue to fix before implementation.

#### 7. Implement the first task

Ask the agent to implement the first unblocked task from `tasks.md`:

```text
$leanplan-implement <KEY> <task-id>
```

What you do: stay available for decision points, especially ambiguous behavior, scope expansion, or changes that would affect users.

What the agent does: reads the task card, load-bearing citations, and current code, then implements the smallest meaningful change for that task.

What LeanPlan produces: code or documentation changes in the repository, with the important rationale moved out of the temporary plan and into durable project surfaces when needed.

How you know the first LeanPlan flow is complete: the first task's completion criteria are satisfied, and any important WHY from the plan has a durable home outside the transient feature artifacts.

### Where to go next

After the first-use path, continue based on what you need:

- For the full stage-by-stage workflow, read [`docs/user-guide/using-leanplan.md`](./docs/user-guide/using-leanplan.md).
- For LeanPlan-specific mechanisms, read [`docs/user-guide/mechanisms.md`](./docs/user-guide/mechanisms.md).
- For team adoption guidance, read [`docs/user-guide/adoption.md`](./docs/user-guide/adoption.md).
- For command and artifact lookup, read [`docs/user-guide/reference.md`](./docs/user-guide/reference.md).
- For a real worked example, read the plan under [`docs/features/260620-artifact-later-update/`](./docs/features/260620-artifact-later-update) — a complete Requirements → Spec → Design → Tasks spine (with design-rationale and research archives) for an actual LeanPlan feature. Browse [`docs/features/`](./docs/features) for more.
- For framework internals, read [`framework-design.md`](./framework-design.md).
- For agent procedure, read the canonical files under [`references/`](./references/).
