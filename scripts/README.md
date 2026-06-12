# LeanPlan canonical scripts

All LeanPlan tooling lives at `~/.local/share/leanplan/scripts/`, applied via chezmoi from `dot_local/share/leanplan/scripts/`. Both Claude Code (`~/.claude/skills/{requirement,specify,design,plan,impl}`) and Codex (`~/.agents/skills/leanplan/`) adapters dereference this canonical path.

## Tools

| Tool | Purpose | Exit codes |
|---|---|---|
| `validate.py` | Comprehensive validator for `<feature-dir>`. Anchor integrity, bidirectional coverage, drift regex, duplicate-anchor + broken-citation + frontmatter + MUST/MUST NOT misuse + ASCII-diagram + checkbox + design ↔ rationale consistency, advisory one-deployment guardrail. `**GAP**` ack accepted. | 0 clean / 1 errors (or warnings under `--strict`) |
| `leanplan-new <slug-or-title>` | Allocates the next repo-local feature number (scan `docs/features/*` max + 1, zero-pad 4; `$LEANPLAN_ID_WIDTH` overrides), creates `<cwd>/docs/features/<NNNN-slug>/{requirement,spec,design,design-rationale,plan}.md`, and prints the resolved path on stdout (human messages on stderr). Non-numeric legacy dirs coexist. Stubs pass `validate.py --stage requirement` clean on a fresh dir (later stages validate as each is filled in). | 0 / 1 (bad input) / 2 (dir exists) |
| `leanplan-selftest` | Defect-injection battery against the bundled `fixtures/valid/` (override via `LEANPLAN_FIXTURE`). Verifies validator catches the expected drift in each scenario. | pass count on stdout / fail count as exit |
| `pre-commit-leanplan` | Installable per-repo git pre-commit hook. Warn-only by default; `LEANPLAN_STRICT=1` blocks on errors. Install via `ln -s ~/.local/share/leanplan/scripts/pre-commit-leanplan <repo>/.git/hooks/pre-commit`. | 0 / non-zero in strict mode on validator errors |

## Validator quick reference

```bash
python3 ~/.local/share/leanplan/scripts/validate.py docs/features/0007-anomaly-publisher   # <KEY> = NNNN-slug
python3 ~/.local/share/leanplan/scripts/validate.py docs/features/<KEY> --stage spec
python3 ~/.local/share/leanplan/scripts/validate.py docs/features/<KEY> --json
python3 ~/.local/share/leanplan/scripts/validate.py docs/features/<KEY> --strict   # CI / pre-commit
python3 ~/.local/share/leanplan/scripts/validate.py docs/features/<KEY> --allow-large
```

## Conventions enforced

The contract validators uphold lives in `~/.local/share/leanplan/references/artifact-contract.md`. If a rule needs to change, update the contract first; validators must mirror it. The framework doc at `~/.local/share/leanplan/leanplan.md` is the source for evolving the framework itself.
