---
name: leanplan
description: LeanPlan front door for Codex. Use for `$leanplan-<move>`; routes requirements, specify, design, tasks, implement, sharpen, revise, and validate to the matching leanplan-* skill.
---

# LeanPlan Front Door

LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work. This Codex skill is a compatibility front door for `$leanplan <move>` invocations.

## Dispatch

Parse the first argument, then read and follow the matching move wrapper. The target wrapper owns the input contract, canonical reference, validation command, and handoff language.

| Move | Load wrapper |
|---|---|
| `requirements <slug-or-title>` | `~/.local/share/leanplan/adapters/codex/leanplan-requirements/SKILL.md` |
| `specify <KEY>` | `~/.local/share/leanplan/adapters/codex/leanplan-specify/SKILL.md` |
| `design <KEY>` | `~/.local/share/leanplan/adapters/codex/leanplan-design/SKILL.md` |
| `tasks <KEY>` | `~/.local/share/leanplan/adapters/codex/leanplan-tasks/SKILL.md` |
| `implement <KEY> <task-id>` | `~/.local/share/leanplan/adapters/codex/leanplan-implement/SKILL.md` |
| `sharpen <what-shifted>` | `~/.local/share/leanplan/adapters/codex/leanplan-sharpen/SKILL.md` |
| `revise <KEY> [Delta-N | what drifted]` | `~/.local/share/leanplan/adapters/codex/leanplan-revise/SKILL.md` |
| `validate <feature-path>` | `~/.local/share/leanplan/adapters/codex/leanplan-validate/SKILL.md` |

If the requested move is missing or ambiguous, ask for one of the move names above. Do not infer a stage and proceed silently.

## Validation Flags

The validation utility and stage wrappers use:

```bash
python3 ~/.local/share/leanplan/scripts/validate.py docs/features/<KEY>
```

- `--stage requirements|spec|design|tasks|full` — partial check while iterating.
- `--json` — machine-readable output.
- `--strict` or `LEANPLAN_STRICT=1` — warnings exit non-zero and one-deployment guardrails become errors.
- `--allow-large` — suppress size guardrails.

## Boundary

This front door is routing glue only. It does not restate stage procedure, artifact shape, or implementation close-out rules. Those live in the move wrappers and the shared references they load.
