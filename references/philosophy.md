# LeanPlan Philosophy

LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work. This doc carries the principles that shape what counts as a *good* artifact and a *good* implementation move at every stage.

## Stage map

Requirements (desired outcome) → Spec (observable contract, generic categories only) → Design (chosen realization) → Tasks (`tasks.md` work cards) → code. Archive companions: Design Rationale (WHY behind decisions), Research (evidence behind WHY).

## Behavior-shaping principles

1. **JIT loading.** Load only the slice needed now. Don't bulk-load every reference, every cited anchor, every archive doc. Cited `B-N` / `C-N` / `D-N` blocks are loaded individually when the next step actually depends on them. (context-engineering: jit-loading)
2. **No flat task scripting.** Plan cards carry intent + constraints + anchors + completion criteria. They are not step-by-step edit recipes. Implementation agents re-derive against current code at task entry. (context-engineering: jit-loading, distractor-sensitivity)
3. **Small surface for review.** Verbose artifacts get rubber-stamped, leak over-specific instructions to implementation, and degrade agent reasoning. Keep surface artifacts terse; archive elsewhere. Terseness is necessary but not sufficient — *order* matters too: lead with the conclusion and prefer bullet / ordered lists over dense paragraphs, so the artifact is graspable from headings and lead lines (`artifact-contract.md` → Prose Style). (context-engineering: lost-in-the-middle, distractor-sensitivity)
4. **Archive verbose reasoning.** Rationale lives in `design-rationale.md` (loaded on challenge); evidence lives in `research.md` (loaded behind rationale). Surface artifacts cite into archives, never inline them. (context-engineering: jit-loading, context-as-working-set)
5. **One-deployment scope.** A feature should fit one deployable increment. Oversized work is split at Spec entry, not absorbed into a sprawling plan.
6. **Surface artifacts are transient.** Requirements / Spec / Design / Tasks exist for the plan-implement cycle. Once the work lands, code is the source of truth going forward — surface artifacts become discardable.
7. **Persist by migration to code.** At implementation close-out, the implementation agent distills non-obvious WHYs from plan artifacts into durable code forms. Hierarchy: types > tests > annotations > commit message > PR body > inline comment. Distill against final code reality, not predicted at plan-write time. Carry the *substance* of each WHY, never its round-local key: an in-round anchor (`B-N` / `C-N` / `D-N`) or `Spec#…`-style citation is plan-scoped (P6) and dangles once the plan is discarded, so a durable form that says only "satisfies the round's anchor" has migrated the handle, not the reason — write the reason itself. (context-engineering: structured-note-taking)
8. **Session-boundary discipline.** The planning spine (requirements→spec→design→tasks) is tightly coupled — keep it continuous in one warm session, where cross-stage reasoning back-propagates cheaply. Make the hard hand-off to a fresh session at the plan→implementation boundary, where the artifact stabilizes and the work-nature flips to execution. Isolate noisy breadth-heavy sub-tasks into sub-agents; light-compact at major pivots. Cross-session implementation survival rests on harness task-state + git commits (which already carry distilled WHYs, P7), not a new per-feature state artifact. (context-engineering: explore-execute-boundary, compaction-vs-eviction, explore-then-compact-handoff, context-isolation, prefix-cache-economics)
9. **Explore at altitude; defer forward, don't chase or discard.** Range freely over the solution space a stage's altitude warrants — but when a genuinely cross-stage decision surfaces, *defer it forward* to the stage that owns it rather than chase it now or discard it. Deferring is what keeps the exploration on-altitude: the spark is preserved for its owning stage without pulling the current stage off-task or padding its artifact, and the owning stage re-derives it against its full current options (never replays a parked answer). The capture/drain procedure is `references/deferral.md`. (context-engineering: structured-note-taking, jit-loading)

## Companions

- `artifact-contract.md` — structural rules (feature layout, anchors, traceability, drift guards).
- `<stage>.md` — per-stage procedure (frame, specify, design, tasks, implement).
- `rethink.md` — the off-pipeline rethink move: re-derives a disturbed understanding mid-round, reads committed artifacts but never edits them.
- `revise.md` — the off-pipeline later-update move; invoked at any in-flight occasion to inject a justified drift and propagate it downstream-only. rethink's repair-half complement: it edits committed artifacts, but only against a recorded justification.
- `framework-design.md` — full framework design (coordinate model, edge semantics, validator design, stop-the-line catalog). Load only when challenged on framework shape.
- `context-engineering.md` — the name→node map resolving the `(context-engineering: <slug>)` grounding hooks that trail the principles above to their context-engineering concept node (definition, sources, related edges). Load only when a hook is challenged.
