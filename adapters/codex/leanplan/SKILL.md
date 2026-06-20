---
name: leanplan
description: Use LeanPlan, a portable LLM-aware spec-driven-development framework, to author or validate feature artifacts through the requirement, specify, design, plan, and impl stages, plus the off-pipeline sharpen move.
---

# LeanPlan

LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work in monorepos. This skill is the Codex-side dispatcher across all five stages plus the off-pipeline `sharpen` move; the Claude Code runtime exposes the same content via slash commands.

Use this skill when the user asks to create, refine, validate, or implement a LeanPlan feature plan. Canonical assets (shared between Claude Code and Codex runtimes) live at `~/.local/share/leanplan/`.

## Dispatch

Parse the user's intent and load only the matching reference from the canonical tree:

| Intent | Load |
|---|---|
| `requirement <slug-or-title>` | `~/.local/share/leanplan/references/requirement.md` |
| `specify <KEY>` | `~/.local/share/leanplan/references/specify.md` |
| `design <KEY>` | `~/.local/share/leanplan/references/design.md` |
| `plan <KEY>` | `~/.local/share/leanplan/references/plan.md` |
| `impl <KEY> <task-id>` | `~/.local/share/leanplan/references/impl.md` |
| `sharpen <what-shifted>` | `~/.local/share/leanplan/references/sharpen.md` |
| `validate <feature-path>` | Run `python3 ~/.local/share/leanplan/scripts/validate.py` |

Throughout, `<KEY>` is the feature id. Its three forms (sequence / tracker-key / date), the `leanplan-new` allocation, and the `## Upstream` rule are defined in `artifact-contract.md` / `leanplan.md` §5 and produced by the `requirement` edge — load them there rather than restating here.

For any artifact-writing stage, default-load only the matching stage reference. Load `~/.local/share/leanplan/references/artifact-contract.md` (structural rules) on demand — before writing or editing an artifact's structure or anchors — and `~/.local/share/leanplan/references/philosophy.md` (framework principles) when a principle's intent or grounding is in question, not up front (CE: jit-loading).

The framework doc at `~/.local/share/leanplan/leanplan.md` carries the full coordinate model, validator design, and stop-the-line catalog. Load it only when challenged on framework shape — `philosophy.md` covers the principles needed at runtime.

If the current repo has its own `docs/leanplan.md` (a project-local snapshot), read it as repo-local context only. The canonical references remain authoritative.

## Validation

```bash
python3 ~/.local/share/leanplan/scripts/validate.py docs/features/<KEY>
```

Flags:

- `--stage requirement|spec|design|plan|full` — partial check while iterating.
- `--json` — machine-readable output.
- `--strict` (or `LEANPLAN_STRICT=1`) — escalates the one-deployment guardrail to error and makes any warning exit non-zero. Suitable for CI / pre-commit.
- `--allow-large` — suppress the size guardrails (oversized DAGs and over-cap surface artifacts).

A SPEC O / INV item annotated on a line containing `**GAP**` (typically in plan.md's forward-coverage table) is treated as deliberately uncovered — see the artifact contract.

## Operating Rules

- Do not turn TASK into a script. Give intent, constraints, anchors, and completion criteria.
- Do not bulk-load every reference. Load only the stage reference needed now.
- Do not create living canonical specs. Plan artifacts are in-feature, transient, and migrated into code/tests/types/PR body at implementation close-out.
- When implementation contradicts a prior artifact, walk up to the highest affected layer and update there instead of patching downstream drift.
