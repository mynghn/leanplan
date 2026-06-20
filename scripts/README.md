# LeanPlan canonical scripts

All LeanPlan tooling lives at `~/.local/share/leanplan/scripts/`, applied via chezmoi from `dot_local/share/leanplan/scripts/`. Both Claude Code (`~/.claude/skills/{requirement,specify,design,plan,impl,sharpen,revise}`) and Codex (`~/.agents/skills/leanplan/`) adapters dereference this canonical path.

## Tools

| Tool | Purpose | Exit codes |
|---|---|---|
| `validate.py` | Comprehensive validator for `<feature-dir>`. Anchor integrity, bidirectional coverage, drift regex, duplicate-anchor + broken-citation + frontmatter + MUST/MUST NOT misuse + ASCII-diagram + checkbox + design ↔ rationale consistency, advisory one-deployment guardrail. `**GAP**` ack accepted. | 0 clean / 1 errors (or warnings under `--strict`) |
| `leanplan-new <slug-or-title>` / `<PROJ-123>` / `--date[=YYMMDD] <title>` / `--rename <old> <new>` | Allocates a feature id in one of three forms — `NNNN-slug` repo-local sequence (default; scan `docs/features/*` max + 1 over exactly-WIDTH-digit ids, zero-pad 4, `$LEANPLAN_ID_WIDTH` overrides), a bare tracker key auto-detected from an `[A-Z]+-N` arg, or `YYMMDD-slug` from `--date` (today, or an explicit override) — then creates `<cwd>/docs/features/<id>/{requirement,spec,design,design-rationale,plan}.md` and prints the resolved path on stdout (human messages on stderr). Other / legacy dirs coexist. Stubs pass `validate.py --stage requirement` clean on a fresh dir (later stages validate as each is filled in). `--rename <old> <new>` relocates an existing feature: moves the dir, rewrites every intra-repo `docs/features/<old>` reference (segment-boundary matched, so a sibling sharing the prefix is untouched), refreshes the moved artifacts' H1 identity, and re-validates the result. | 0 / 1 (bad input) / 2 (dir exists) |
| `leanplan-selftest` | Defect-injection battery against the bundled `fixtures/valid/` (override via `LEANPLAN_FIXTURE`). Verifies validator catches the expected drift in each scenario. | pass count on stdout / fail count as exit |
| `pre-commit-leanplan` | Installable per-repo git pre-commit hook. Warn-only by default; `LEANPLAN_STRICT=1` blocks on errors. Install via `ln -s ~/.local/share/leanplan/scripts/pre-commit-leanplan <repo>/.git/hooks/pre-commit`. | 0 / non-zero in strict mode on validator errors |

## Validator quick reference

```bash
python3 ~/.local/share/leanplan/scripts/validate.py docs/features/0007-anomaly-publisher   # <KEY> = the feature id (NNNN-slug / PROJ-123 / YYMMDD-slug)
python3 ~/.local/share/leanplan/scripts/validate.py docs/features/<KEY> --stage spec
python3 ~/.local/share/leanplan/scripts/validate.py docs/features/<KEY> --json
python3 ~/.local/share/leanplan/scripts/validate.py docs/features/<KEY> --strict   # CI / pre-commit
python3 ~/.local/share/leanplan/scripts/validate.py docs/features/<KEY> --allow-large
```

## Conventions enforced

The contract validators uphold lives in `~/.local/share/leanplan/references/artifact-contract.md`. If a rule needs to change, update the contract first; validators must mirror it. The framework doc at `~/.local/share/leanplan/leanplan.md` is the source for evolving the framework itself.
