# 260626-ce-grounding-link-check — Understanding Shifts

## Delta-1: package-as-doctor-umbrella-absorbing-freshness

The grounding-link inspection is now realized as one of two diagnostics inside a new `leanplan-doctor` health-check skill that **absorbs** the existing `leanplan-installation-freshness` skill — not a standalone sibling skill. Doctor is the single "is my LeanPlan healthy?" command: one `SKILL.md` running two labeled sections — installation freshness (git-freshness + symlink parity) and CE grounding links (the grounded-slug resolution check) — each keeping its own fix route.

Kills D-1's original choice: a standalone `leanplan-ce-grounding-link-check` skill mirroring the freshness sibling, justified by "one responsibility per skill" (which explicitly rejected folding into freshness).

Why: the maintainer reversed it. Both checks are the same kind of on-demand, read-first, report-only maintenance inspection; a single health command is better UX than two near-identical sibling skills, and "installation freshness" was too narrow a home. The grounding diagnostic's reference-only / report-only contract is unaffected — it survives as doctor's grounding section, which simply has no auto-fix and points to `/leanplan-revise`.

Scope-of-impact: Design#D-1-realize-as-utility-skill-with-check-script, Tasks#T:U1, Tasks#T:U2, Tasks#T:U3.
