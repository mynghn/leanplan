# 260622-vocab-v2-rename — SPEC

## Outcome

### O-1: prior-vocab-absent-from-live-surfaces
When the rollout is complete, a scan of every live surface for prior-vocab tokens returns zero hits — no artifact name (`REQUIREMENT`/`SPEC`/`DESIGN`/`TASK`), edge/skill (`requirement`/`plan`/`impl`), item/anchor (`O-`/`INV-`/`Decision-`, `Task:`), filename (`requirement.md`/`plan.md`), or citation namespace from the prior vocab survives where a maintainer or agent would actually load it. The deliberate historical record — §8's prior-vocab column and any framing explicitly marked as transition history — is the sole exemption and is enumerated, not open-ended. One-shot test: run the residual-token scan over the repo minus the enumerated exemptions; assert zero hits.

### O-2: authority-caveat-retired
§8's "a separate, dedicated framework-wide rename rolls it out… until that sweep lands, the framework runs in the prior vocab" and Decision-2's matching "separate effort / L's own artifacts stay in today's vocab" framing read as past-tense historical record, not as a description of a live two-vocab state. One-shot test: inspect §8 and Decision-2; no sentence asserts the framework currently runs a prior/target split as an unfinished present-state condition.

## Invariants

### INV-1: identity-and-traceability-preserved
Across the rollout every artifact keeps its stage role and content, and the framework stays structurally valid in the new vocab: all anchors resolve, every cross-doc citation resolves, the bidirectional SPEC↔task coverage holds, and `validate.py`, `leanplan-selftest`, and `scan-leaks` pass on all shipped feature cycles and on both fixture sets. Verified by the structural validators over the framework's own artifacts and fixtures.

### INV-2: content-preserved-labels-only
The rollout changes labels, never meaning. No item is renumbered (`O-1`→`B-1`, never `O-1`→`B-2`); no prose is added, dropped, or re-argued beyond substituting a vocabulary token for its v2 equivalent. The net diff is a name substitution plus the bounded reflexive edits O-2 requires — not a content rewrite. Verified by diff inspection (the structural validator sees shape, not semantic preservation).

## Non-goals
- **The execution strategy.** Whether the rollout lands atomically or staged per artifact-family, how the validator/fixture lockstep is sequenced, and the rollback mechanism are DESIGN's to choose — none is an externally-observable behavior. This contract holds for any strategy that reaches the end-state above.
- **Re-deriving names.** The target scheme is §8, applied verbatim. No name is chosen, re-opened, or invented here.
- **Renaming ordinary English.** Only vocabulary-as-LeanPlan-term uses are in scope; generic "plan/spec/design/outcome/task" prose and "plan" the activity are untouched.
