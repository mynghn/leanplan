---
name: leanplan-doctor
description: LeanPlan health check — run on demand to diagnose the installed LeanPlan in one command. Reports installation freshness (the LeanPlan checkout's git-freshness + Claude/Codex skill-symlink parity) and CE grounding-link validity (whether LeanPlan's `(context-engineering: <slug>)` grounding references still resolve against the live Metacognition source). Use after a LeanPlan main-branch update, after a Metacognition context-engineering update, when installed `leanplan-*` skills may be stale, or to check whether the local LeanPlan installation is healthy. Read-first and report-only.
argument-hint: "[--strict]"
---

# leanplan-doctor

Diagnose the installed LeanPlan in one read-only pass, reported as two labeled sections:

1. **Installation freshness** — the LeanPlan checkout's git clean/behind/ahead vs `origin` (fetch-only) and whether installed Claude/Codex skill symlinks match the authored adapter and utility-skill directories.
2. **CE grounding links** — whether LeanPlan's context-engineering grounding references (the `(context-engineering: <slug>)` hooks and the map's `[[<slug>]]` links) still resolve against the live Metacognition source's INDEX slug-registry. Reference-only: it checks that slug *names* resolve, never a concept's content or health.

This is not a planning-stage skill; it owns only installation + grounding health.

Resolve `<LEANPLAN_ROOT>` as the LeanPlan checkout containing this utility: follow the real path of
this `SKILL.md` from the installed skill symlink when present, then walk up two directories from
`utils/leanplan-doctor/`. Substitute that absolute path wherever commands below use `<LEANPLAN_ROOT>`.

**Read-first, report-only.** Run both checks, show the verdicts. Doctor mutates nothing. Each section
has its own repair route — apply it only after reviewing the report, and (for freshness) only after
the user confirms.

## 1. Installation freshness (read-only)

```sh
<LEANPLAN_ROOT>/utils/leanplan-doctor/checks/freshness.sh
```

Reports clean/dirty + **behind/ahead vs origin** and skill-symlink parity. On a `**` flag (behind, or
a stale/missing symlink), repair only after the user confirms:

```sh
git -C <LEANPLAN_ROOT> pull --ff-only
<LEANPLAN_ROOT>/install.sh
```

Re-run to confirm `behind=0` and symlinks `ok`.

## 2. CE grounding links (read-only)

```sh
<LEANPLAN_ROOT>/utils/leanplan-doctor/checks/grounding.sh
```

Reads the live source via `$LEANPLAN_CE_SOURCE_INDEX`, else the conventional vault INDEX
(`~/.local/share/metacognition-vault/context-engineering/INDEX.md`). Three verdicts:

- `[links  ]  ok` — every grounded slug resolves. Nothing to do.
- `[source ]  n/a  source absent` — the source is unreachable; LeanPlan falls back to the map's local
  gloss. Expected when the vault is not installed, **not** a defect.
- `[links  ]  **  … dangling` — one or more grounded slugs no longer resolve, each listed with its
  referencing files. Repair via `/leanplan-revise` — re-ground the hook to a current concept name, or
  retire the reference. The check never edits grounding itself.

Add `--strict` to the grounding check to exit nonzero on dangling (for CI gating); by default it is
advisory and exits 0.
