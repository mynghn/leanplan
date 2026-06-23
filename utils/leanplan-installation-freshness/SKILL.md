---
name: leanplan-installation-freshness
description: LeanPlan — check and, after confirmation, update freshness of the installed LeanPlan checkout and its Claude/Codex skill symlinks. Use after a LeanPlan main-branch update, when installed `leanplan-*` skills may be stale, or to confirm the local installation is current. LeanPlan is install-bootstrapped; update via git pull + re-run install.sh.
argument-hint: "[check | update]"
---

# leanplan-installation-freshness

Check the LeanPlan installation surface: the LeanPlan checkout containing this utility skill, its git
freshness vs `origin`, and whether installed Claude/Codex skill symlinks match the authored adapter
and utility-skill directories.

Resolve `<LEANPLAN_ROOT>` as the LeanPlan checkout containing this utility: follow the real path of
this `SKILL.md` from the installed skill symlink when present, then walk up two directories from
`utils/leanplan-installation-freshness/`. Substitute that absolute path wherever commands below use
`<LEANPLAN_ROOT>`.

This is not a planning-stage skill. It owns only installation/update validity.

**Read-first, confirmed-update.** Run the check, show the verdict, then update only if it flags `**`,
and only after the user confirms.

## 1. Check (read-only)

```sh
<LEANPLAN_ROOT>/utils/leanplan-installation-freshness/check.sh
```

The check reports clean/dirty + **behind/ahead vs origin** (fetch-only), and symlink parity: every
authored `adapters/claude/<skill>/SKILL.md`, `adapters/codex/<skill>/SKILL.md`, and
`utils/<utility-skill>/SKILL.md` should have a matching installed symlink under `~/.claude/skills/`
and/or `~/.agents/skills/`.

## 2. Update (only if flagged, only after confirmation)

```sh
git -C <LEANPLAN_ROOT> pull --ff-only
<LEANPLAN_ROOT>/install.sh
```

Re-run the check to confirm `behind=0` and symlinks `ok`.
