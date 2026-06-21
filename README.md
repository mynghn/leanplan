# LeanPlan

A lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work.

## What it is

LeanPlan defines five stages — **REQUIREMENT → SPEC → DESIGN → TASK → code** — with surface/archive layering, JIT-loaded rationale, and a validator that enforces the contract. The framework is shaped around how LLM agents actually consume planning artifacts: limited useful context, weak long-range attention, stronger performance with JIT-loaded intent plus current code.

The full framework design is in [`leanplan.md`](./leanplan.md).

## Layout

```
leanplan/
├── leanplan.md                 framework design (the canonical doc)
├── references/                 per-stage operational guidance
├── scripts/                    validate.py + scaffold + selftest + pre-commit hook
├── fixtures/                   valid (incl. a GAP-ack) / invalid examples
└── adapters/                   per-runtime skill implementations
    ├── claude/                 Claude Code (7-skill set)
    └── codex/leanplan/         Codex (1 dispatcher)
```

## Install

### Via chezmoi (recommended for personal-phase use)

Add this to your chezmoi source's `.chezmoiexternal.toml`:

```toml
[".local/share/leanplan"]
    type = "git-repo"
    url = "https://github.com/mynghn/leanplan.git"
    refreshPeriod = "168h"

[".local/share/leanplan.clone"]
    args = ["--depth=1"]

[".local/share/leanplan.pull"]
    args = ["--ff-only"]
```

Then add `symlink_*.tmpl` source files for each adapter target so chezmoi creates the runtime-registry symlinks. For Claude Code skills:

```
dot_claude/skills/symlink_requirement.tmpl   →  {{ .chezmoi.homeDir }}/.local/share/leanplan/adapters/claude/requirement
dot_claude/skills/symlink_specify.tmpl       →  ... /adapters/claude/specify
dot_claude/skills/symlink_design.tmpl        →  ... /adapters/claude/design
dot_claude/skills/symlink_plan.tmpl          →  ... /adapters/claude/plan
dot_claude/skills/symlink_impl.tmpl          →  ... /adapters/claude/impl
dot_claude/skills/symlink_sharpen.tmpl       →  ... /adapters/claude/sharpen
dot_claude/skills/symlink_revise.tmpl        →  ... /adapters/claude/revise
```

For Codex:

```
dot_agents/skills/symlink_leanplan.tmpl      →  {{ .chezmoi.homeDir }}/.local/share/leanplan/adapters/codex/leanplan
```

`chezmoi apply` clones LeanPlan into `~/.local/share/leanplan/` and creates the symlinks. `chezmoi update` pulls latest LeanPlan.

### Without chezmoi

```bash
git clone https://github.com/mynghn/leanplan.git ~/.local/share/leanplan
~/.local/share/leanplan/install.sh
```

`install.sh` creates the same per-runtime symlinks (Claude Code at `~/.claude/skills/<name>`, Codex at `~/.agents/skills/leanplan`).

## Quick start

```bash
# scaffold a feature dir — allocates a feature id and prints the path.
# Three id forms are supported:
~/.local/share/leanplan/scripts/leanplan-new "anomaly publisher"   # -> docs/features/0001-anomaly-publisher  (repo-local sequence, default)
~/.local/share/leanplan/scripts/leanplan-new NEWCS-3595           # -> docs/features/NEWCS-3595              (bare tracker key, e.g. Jira)
~/.local/share/leanplan/scripts/leanplan-new --date "anomaly publisher"  # -> docs/features/260616-anomaly-publisher  (date, today's YYMMDD)

# fill in artifacts (use the skills, or edit by hand)
# ...

# validate (use the path leanplan-new printed)
python3 ~/.local/share/leanplan/scripts/validate.py docs/features/0001-anomaly-publisher

# run the validator's own self-test
~/.local/share/leanplan/scripts/leanplan-selftest
```

## Edits

Run-time content at `~/.local/share/leanplan/` is a working git clone. Edit there directly for fast iteration; commit + push from that working tree to publish. Or work in a separate clone and `chezmoi update` to pull.

Editing the runtime tree is supported (it is a real working copy), but understand that `chezmoi update` from a stale local working copy will fast-forward only — uncommitted local edits are preserved.

## Contributing

Open an issue or PR. The validator should pass on every commit:

```bash
python3 scripts/validate.py fixtures/valid                # exit 0 (includes a GAP-acked SPEC item)
python3 scripts/validate.py fixtures/invalid-missing-coverage  # exit 1, expected
LEANPLAN_FIXTURE=$PWD/fixtures/valid scripts/leanplan-selftest # all pass (exit 0; prints "N passed, 0 failed")
```

## License

[MIT](./LICENSE)
