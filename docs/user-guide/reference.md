# LeanPlan Reference

This page is for quick lookup. It is intentionally compact; use the guide pages when you need explanation and `references/*.md` when you need canonical agent procedure.

## Commands

Codex form:

```text
$leanplan requirements "short feature title"
$leanplan specify <KEY>
$leanplan design <KEY>
$leanplan tasks <KEY>
$leanplan implement <KEY> <task-id>
$leanplan sharpen <what-shifted>
$leanplan revise <KEY> [Delta-N | what drifted]
$leanplan validate docs/features/<KEY>
```

Claude Code slash-command form:

```text
/requirements "short feature title"
/specify <KEY>
/design <KEY>
/tasks <KEY>
/implement <KEY> <task-id>
/sharpen <what-shifted>
/revise <KEY> [Delta-N | what drifted]
```

Utility scripts:

```bash
~/.local/share/leanplan/scripts/leanplan-new "short feature title"
python3 ~/.local/share/leanplan/scripts/validate.py docs/features/<KEY>
python3 ~/.local/share/leanplan/scripts/validate.py --stage tasks docs/features/<KEY>
python3 ~/.local/share/leanplan/scripts/validate.py --strict docs/features/<KEY>
```

## Artifact responsibilities

| Artifact | Owns | Does not own |
|---|---|---|
| `requirements.md` | Problem, scope, success shape | Behavior details or implementation approach |
| `spec.md` | Observable behavior and constraints | Code structure or task order |
| `design.md` | Chosen approach, tradeoffs, boundaries | Product intent or task execution |
| `tasks.md` | DAG, task cards, completion criteria, dependencies | Canonical product rationale |
| Archive material | Deeper rationale and exploration | Facts every downstream stage must always load |
| Code, tests, PR text | Durable delivered rationale | Round-local planning handles |

## Stage transition cues

| From | Move on when | Stop when |
|---|---|---|
| Requirements to Spec | Intent and scope are clear | The feature is not one deployable slice |
| Spec to Design | Behavior and constraints are observable | Behavior is still ambiguous |
| Design to Tasks | Approach and boundaries are chosen | Tradeoffs are unresolved |
| Tasks to implementation | First unblocked task is clear | Completion cannot be verified |
| One task to next task | Criteria are satisfied and rationale is durable | Implementation found upstream drift |

## Review expectations

- Requirements review asks whether the right problem and boundary are captured.
- Spec review asks whether behavior and constraints are observable and complete enough.
- Design review asks whether the chosen approach satisfies the Spec in the current codebase.
- Tasks review asks whether the DAG is coherent, scoped, and verifiable.
- Implementation review asks whether the delivered change satisfies the task and carries important rationale outside transient plan artifacts.

## Validation modes

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

## Common failure signals

| Signal | Likely response |
|---|---|
| The feature keeps growing | Split to the next deployment-sized slice |
| Behavior changes during implementation | Revise from the highest affected artifact |
| The agent needs many unrelated files loaded at once | Narrow the task or improve artifact ownership |
| Completion criteria are subjective | Rewrite them around observable evidence |
| A task only says "implement the design" | Add task-specific goal, constraints, and completion criteria |
| The guide and references seem to disagree | Treat `references/*.md` and adapters as canonical agent procedure, then fix the human-facing explanation |

## See also

- [`using-leanplan.md`](./using-leanplan.md) — the full stage workflow.
- [`mechanisms.md`](./mechanisms.md) — why LeanPlan behaves the way it does.
- Back to [`USER_GUIDE.md`](../../USER_GUIDE.md) for the entry path and Quickstart.
