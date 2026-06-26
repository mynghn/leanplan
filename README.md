# LeanPlan

A lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work.

## What it is

LeanPlan defines five stages — **Requirements → Spec → Design → Tasks → code** — that keep each artifact lean by pushing verbose rationale into separately-loaded archives, with a validator that enforces the contract. The framework is shaped around how LLM agents actually consume planning artifacts: limited useful context, weak long-range attention, and stronger performance when intent is loaded just-in-time alongside current code.

The full framework design is in [`framework-design.md`](./framework-design.md).

New to LeanPlan? Start with the human-facing [`USER_GUIDE.md`](./USER_GUIDE.md) for the first-use path and workflow orientation.

## Layout

```
leanplan/
├── framework-design.md                 framework design (the canonical doc)
├── references/                 per-stage operational guidance
├── scripts/                    leanplan-validate + scaffold + selftest + pre-commit hook
├── utils/                      installation/maintenance utility skills
├── fixtures/                   valid (incl. a GAP-ack) / invalid examples
└── adapters/                   per-runtime skill implementations
    ├── claude/                 Claude Code skills
    ├── codex/                  Codex skills
    └── README.md               cross-vendor adapter map
```

## Install

Choose a LeanPlan checkout location, then run the adapter installer from that checkout:

```bash
LEANPLAN_ROOT="$HOME/src/leanplan"
git clone https://github.com/mynghn/leanplan.git "$LEANPLAN_ROOT"
"$LEANPLAN_ROOT/install.sh"
```

`install.sh` creates the per-runtime symlinks from that checkout: Claude Code at `~/.claude/skills/leanplan-*`, Codex at `~/.agents/skills/leanplan-*`, and shared utility skills from `utils/`.

To update an installed copy:

```bash
LEANPLAN_ROOT="$HOME/src/leanplan"
git -C "$LEANPLAN_ROOT" pull --ff-only
"$LEANPLAN_ROOT/install.sh"
```

Re-running `install.sh` is safe and refreshes adapter symlinks after the adapter list changes.
Use `leanplan-doctor` from your agent to check the installed checkout and adapter symlinks (and CE
grounding-link health) before updating.

### Optional dotfile-manager use

If you already manage local tooling through a dotfile manager such as chezmoi, you can manage the same chosen LeanPlan checkout and registry symlinks there. This is optional; normal LeanPlan use follows the primary path above.

## Quick start

```bash
LEANPLAN_ROOT="$HOME/src/leanplan"  # or your chosen checkout

# scaffold a feature dir — allocates a feature id and prints the path.
# Three id forms are supported:
"$LEANPLAN_ROOT/scripts/leanplan-new" "anomaly publisher"   # -> docs/features/0001-anomaly-publisher  (repo-local sequence, default)
"$LEANPLAN_ROOT/scripts/leanplan-new" NEWCS-3595           # -> docs/features/NEWCS-3595              (bare tracker key, e.g. Jira)
"$LEANPLAN_ROOT/scripts/leanplan-new" --date "anomaly publisher"  # -> docs/features/260616-anomaly-publisher  (date, today's YYMMDD)

# fill in artifacts (use the skills, or edit by hand)
# ...

# validate (use the path leanplan-new printed)
"$LEANPLAN_ROOT/scripts/leanplan-validate" docs/features/0001-anomaly-publisher

# run the validator's own self-test
"$LEANPLAN_ROOT/scripts/leanplan-selftest"
```

## Edits

Runtime content lives in the LeanPlan checkout you chose during install. Edit there directly for fast iteration; commit and push from that working tree to publish. Or work in a separate clone, merge there, then pull the runtime checkout with `git -C "$LEANPLAN_ROOT" pull --ff-only`.

Editing the runtime tree is supported because it is a real working copy. Uncommitted local edits are preserved across a failed fast-forward; commit, stash, or move them before pulling remote changes.

## Contributing

Open an issue or PR. The validator should pass on every commit:

```bash
scripts/leanplan-validate fixtures/valid                # exit 0 (includes a GAP-acked Spec item)
scripts/leanplan-validate fixtures/invalid-missing-coverage  # exit 1, expected
LEANPLAN_FIXTURE=$PWD/fixtures/valid scripts/leanplan-selftest # all pass (exit 0; prints "N passed, 0 failed")
```

## License

[MIT](./LICENSE)
