# LeanPlan Philosophy

LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work in monorepos. This doc carries the principles that shape what counts as a *good* artifact and a *good* implementation move at every stage.

## Stage map

REQUIREMENT (biz WHAT) → SPEC (tech contract, generic categories only) → DESIGN (chosen realization) → TASK (`plan.md` work cards) → code. Archive companions: DESIGN RATIONALE (WHY behind decisions), RESEARCH (evidence behind WHY).

## Behavior-shaping principles

1. **JIT loading.** Load only the slice needed now. Don't bulk-load every reference, every cited anchor, every archive doc. Cited `O-N` / `INV-N` / `Decision-N` blocks are loaded individually when the next step actually depends on them. (CE: jit-loading)
2. **No flat task scripting.** Plan cards carry intent + constraints + anchors + completion criteria. They are not step-by-step edit recipes. Implementation agents re-derive against current code at task entry.
3. **Small surface for review.** Verbose artifacts get rubber-stamped, leak over-specific instructions to implementation, and degrade agent reasoning. Keep surface artifacts terse; archive elsewhere. Terseness is necessary but not sufficient — *order* matters too: lead with the conclusion and prefer bullet / ordered lists over dense paragraphs, so the artifact is graspable from headings and lead lines (`artifact-contract.md` → Prose Style). (CE: lost-in-the-middle, distractor-sensitivity)
4. **Archive verbose reasoning.** Rationale lives in `design-rationale.md` (loaded on challenge); evidence lives in `research.md` (loaded behind rationale). Surface artifacts cite into archives, never inline them. (CE: jit-loading, context-as-working-set)
5. **One-deployment scope.** A feature should fit one deployable increment. Oversized work is split at SPEC entry, not absorbed into a sprawling plan.
6. **Plan docs are transient.** REQUIREMENT / SPEC / DESIGN / TASK exist for the plan-implement cycle. Once the work lands, code is the source of truth going forward — plan docs become discardable.
7. **Persist by migration to code.** At implementation close-out, the impl agent distills non-obvious WHYs from plan artifacts into durable code forms. Hierarchy: types > tests > annotations > commit message > PR body > inline comment. Distill against final code reality, not predicted at plan-write time. (CE: structured-note-taking)
8. **Session-boundary discipline.** The planning spine (requirement→spec→design→plan) is tightly coupled — keep it continuous in one warm session, where cross-stage reasoning back-propagates cheaply. Make the hard hand-off to a fresh session at the plan→impl boundary, where the artifact stabilizes and the work-nature flips to execution. Isolate noisy breadth-heavy sub-tasks into sub-agents; light-compact at major pivots. Cross-session impl survival rests on harness task-state + git commits (which already carry distilled WHYs, P7), not a new per-feature state artifact. (CE: explore-execute-boundary, compaction-vs-eviction, explore-then-compact-handoff, context-isolation)

## Companions

- `artifact-contract.md` — structural rules (feature layout, anchors, traceability, drift guards).
- `<stage>.md` — per-stage procedure (requirement, specify, design, plan, impl).
- `leanplan.md` — full framework design (coordinate model, edge semantics, validator design, stop-the-line catalog). Load only when challenged on framework shape.
