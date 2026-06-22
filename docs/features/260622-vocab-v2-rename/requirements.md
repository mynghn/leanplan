# 260622-vocab-v2-rename — roll vocabulary v2 across the whole framework

## Problem

LeanPlan runs in two vocabularies at once. Feature L (#30) settled the complete vocabulary-v2 scheme and wrote it into `framework-design.md` §8 as the **naming authority** — but deferred the propagation, because rolling the scheme across the codebase is ~1,000 edits, larger than L's model change itself. So today the authority describes an ideal vocabulary the framework does not actually use: every other surface — the shipped feature cycles, the validators and fixtures, the skill adapters, the scaffolding, the reference guides — still speaks the prior vocab (`REQUIREMENT`/`SPEC`/`DESIGN`/`TASK`, `O-`/`INV-`/`Decision-`, `requirement.md`/`plan.md`). Maintainers and the agents running the skills read one vocabulary in §8 and write another in practice; §8 itself carries a standing "until the sweep lands" caveat marking the debt. The split is the cost of L having correctly shipped the *decision* without the *rollout*; this feature pays it down.

## Outcome

The framework speaks one vocabulary — v2 — everywhere a live surface speaks at all. Applying §8 (never re-deriving it), every artifact, edge/skill, item/anchor, validator regex, fixture, adapter, scaffold, reference guide, and shipped feature cycle is rolled to the v2 scheme, so a maintainer or agent reading any surface meets the same names §8 declares.

- **One live vocabulary** — no surface a maintainer or agent actually loads still speaks the prior vocab; the authority and the practice finally agree.
- **Authority caveat retired** — §8's "until the sweep lands" framing (and D-2's matching "separate effort" note) become past-tense historical record, not a description of a live two-vocab state.
- **Nothing lost in translation** — every artifact keeps its stage role and content; all anchors resolve, every citation and the Spec↔task traceability still hold, and sequence numbers are preserved (`O-1`→`B-1`, never renumbered). The change is labels, not meaning.

Success signal: the structural validators (`validate.py`, `leanplan-selftest`, `scan-leaks`) pass on all shipped feature cycles and fixtures, and a scan for prior-vocab tokens across live surfaces returns zero hits outside the deliberate historical record (§8's migration note). The framework that documents vocabulary v2 now also runs on it.

## Non-goals
- **Re-deriving or re-opening any name.** §8 is the locked authority and D-2 settled the scheme; this feature *applies* it. Any naming question is already answered there.
- **Renaming ordinary English.** Only vocabulary-as-LeanPlan-term uses are rolled. "Plan" the activity (the whole Requirements→Spec→Design→Tasks spine *is* "the plan", per §8) and generic "spec/design/outcome/task" prose are untouched.
- **Erasing the migration record.** §8's prior-vocab column and any explicitly historical framing are preserved by intent — they document the transition, not a live vocab.
- **Carrying the rollout itself.** The end state is contracted here; the ~1,000-edit execution is the implementation, planned in Design/Tasks and run in a separate later cut.

## Upstream
- #34 (this rollout, deferred from #30) · #30 (Feature L — the §8 authority + the locked scheme)
