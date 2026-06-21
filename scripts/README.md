# LeanPlan canonical scripts

All LeanPlan tooling lives at `~/.local/share/leanplan/scripts/`, applied via chezmoi from `dot_local/share/leanplan/scripts/`. Both Claude Code (`~/.claude/skills/{requirement,specify,design,plan,impl,sharpen}`) and Codex (`~/.agents/skills/leanplan/`) adapters dereference this canonical path.

## Tools

| Tool | Purpose | Exit codes |
|---|---|---|
| `validate.py` | Comprehensive validator for `<feature-dir>`. Anchor integrity, bidirectional coverage, drift regex, duplicate-anchor + broken-citation + frontmatter + MUST/MUST NOT misuse + ASCII-diagram + checkbox + design ↔ rationale consistency, advisory one-deployment guardrail. `**GAP**` ack accepted. | 0 clean / 1 errors (or warnings under `--strict`) |
| `scan-leaks` | Narrow leak detector (sibling of `validate.py`): flags round-scoped anchor tokens (`O-`/`INV-`/`Decision-`/`Delta-<N>`) and cross-artifact citations (`SPEC#…`) leaked into durable outputs *outside* `docs/features/**`. Scans file paths or raw text (`--text` / stdin). High-precision only — feature ids, `docs(<slug>)` labels, and bare numbers don't match, so the allowed grey zone needs no allow-list; inline `leanplan-allow-key` suppresses a line. Callers exclude `docs/features/**`. | 0 clean (or leaks warn) / 1 leaks under `--strict` or `$LEANPLAN_STRICT=1` / 2 input error |
| `leanplan-new <slug-or-title>` / `<PROJ-123>` / `--date[=YYMMDD] <title>` | Allocates a feature id in one of three forms — `NNNN-slug` repo-local sequence (default; scan `docs/features/*` max + 1 over exactly-WIDTH-digit ids, zero-pad 4, `$LEANPLAN_ID_WIDTH` overrides), a bare tracker key auto-detected from an `[A-Z]+-N` arg, or `YYMMDD-slug` from `--date` (today, or an explicit override) — then creates `<cwd>/docs/features/<id>/{requirement,spec,design,design-rationale,plan}.md` and prints the resolved path on stdout (human messages on stderr). Other / legacy dirs coexist. Stubs pass `validate.py --stage requirement` clean on a fresh dir (later stages validate as each is filled in). | 0 / 1 (bad input) / 2 (dir exists) |
| `leanplan-selftest` | Defect-injection battery against the bundled `fixtures/valid/` (override via `LEANPLAN_FIXTURE`). Verifies `validate.py` catches the expected drift in each scenario, and that `scan-leaks` catches a round-scoped key leaked into non-artifact text. | pass count on stdout / fail count as exit |
| `pre-commit-leanplan` | Installable per-repo git pre-commit hook. Runs `validate.py` over staged feature dirs **and** `scan-leaks` over staged files outside `docs/features/**` (plus any `git config leanplan.scanExclude` / `LEANPLAN_SCAN_EXCLUDE` egrep). Warn-only by default; `LEANPLAN_STRICT=1` blocks. Install: `ln -s ~/.local/share/leanplan/scripts/pre-commit-leanplan <repo>/.git/hooks/pre-commit`. | 0 / non-zero in strict mode on findings |
| `commit-msg-leanplan` | Installable per-repo git `commit-msg` hook: runs `scan-leaks` over the commit message (comment lines stripped, since git drops them). Warn-only by default; `LEANPLAN_STRICT=1` blocks. Install: `ln -s ~/.local/share/leanplan/scripts/commit-msg-leanplan <repo>/.git/hooks/commit-msg`. | 0 / non-zero in strict mode on a leak |

## Validator quick reference

```bash
python3 ~/.local/share/leanplan/scripts/validate.py docs/features/0007-anomaly-publisher   # <KEY> = the feature id (NNNN-slug / PROJ-123 / YYMMDD-slug)
python3 ~/.local/share/leanplan/scripts/validate.py docs/features/<KEY> --stage spec
python3 ~/.local/share/leanplan/scripts/validate.py docs/features/<KEY> --json
python3 ~/.local/share/leanplan/scripts/validate.py docs/features/<KEY> --strict   # CI / pre-commit
python3 ~/.local/share/leanplan/scripts/validate.py docs/features/<KEY> --allow-large
```

## Leak scan quick reference

```bash
~/.local/share/leanplan/scripts/scan-leaks path/to/file.py            # scan a file (warn)
git diff --cached --name-only -z | xargs -0 ~/.local/share/leanplan/scripts/scan-leaks   # staged files
printf '%s' "$PR_BODY" | ~/.local/share/leanplan/scripts/scan-leaks --strict   # text via stdin, block on leak
~/.local/share/leanplan/scripts/scan-leaks --text "commit subject" --json      # text via arg, JSON out
```

The pre-commit hook always skips `docs/features/**` (anchors resolve there); add
repo-internal excludes with an egrep, e.g. for LeanPlan's own token-saturated
tooling — its detector vocabulary and test data are a legitimate-match class:

```bash
git config leanplan.scanExclude '^(scripts|fixtures)/'   # or: export LEANPLAN_SCAN_EXCLUDE='^(scripts|fixtures)/'
```

## PR-surface leak scan (GitHub Action)

`templates/leanplan-leak-scan.yml` is an installable workflow template covering the
surfaces no local hook can see — the PR description and review comments (plus a
changed-code safety net). Copy it into a repo's `.github/workflows/` to enable
(LeanPlan's own repo ships but does not run it). Warn-by-default annotations; set
the repo variable `LEANPLAN_STRICT=1` to fail the check on a leaking PR description
or changed code — comments are post-hoc, so they are flag-only. Pin the fetched
`scan-leaks` via the `LEANPLAN_REF` repo variable.

```bash
cp ~/.local/share/leanplan/scripts/templates/leanplan-leak-scan.yml <repo>/.github/workflows/
```


## Conventions enforced

The contract validators uphold lives in `~/.local/share/leanplan/references/artifact-contract.md`. If a rule needs to change, update the contract first; validators must mirror it. The framework doc at `~/.local/share/leanplan/leanplan.md` is the source for evolving the framework itself.
