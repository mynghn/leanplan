# 260626-live-ce-grounding — Live context-engineering grounding instead of a drifting vendored copy

## Problem

LeanPlan keeps its own frozen copy of the context-engineering knowledge its design rests on — 15 distilled cards vendored inside the framework, copied from the Metacognition knowledge vault. That copy drifts from its source silently: it is current only because it was distilled the day after the source's last refresh — by recency, not by any process. The drift has already happened in miniature (an upstream `context-isolation` refresh the copy missed), and the standing plan to contain it (issue #27) is to *add machinery* — a sync/drift-checker — to keep a copy honest.

The copy was justified by one stance: portability must be inviolable, so the grounding must resolve with nothing external installed. But the source vault is **private** — so the "anyone can resolve the grounding locally" benefit only ever fully holds in the maintainer's own environment, the one place the live source is already present. The copy therefore buys little real portability while imposing a permanent maintenance liability, and it forks the knowledge away from its source: every challenge consults LeanPlan's frozen fork instead of the live Metacognition entry, so the source is never exercised or improved by this use.

Who feels it: the **maintainer**, who carries the drift liability and the proposed checker; the framework's **integrity**, since a challenger can resolve a grounded rule to a definition that has quietly gone stale; and **Metacognition itself**, whose context-engineering knowledge is consumed through a copy rather than used and evolved.

## Outcome

LeanPlan's context-engineering grounding becomes fresh by construction: there is no retained copy to drift, because a challenged rule's deep definition is resolved from the live Metacognition source, the single point of truth. LeanPlan keeps what is genuinely its own — the grounding hooks on each load-bearing rule and the rule→concept map, each carrying a brief inline gloss — so a challenge always reaches at least that gloss, and the framework never needs the source merely to run. The change makes LeanPlan a live consumer of Metacognition, exercising the source instead of freezing a fork of it.

User stories:

- **Challenge reaches a current definition** — challenging a grounded rule resolves to a live, sourced context-engineering definition when Metacognition is present, never a copy that may have drifted.
- **Content cannot silently rot** — with no vendored copy, a concept's *definition* can never drift: the live read always returns the current text, so the content-drift the earlier sync/drift-check chased no longer exists. (A thinner *reference* coupling survives — see Guarantee.)
- **A bare install still resolves** — without Metacognition present, every grounded rule still resolves to LeanPlan's own one-line gloss, and all planning and authoring stages run unchanged with nothing external.

The change is confirmed when no distilled context-engineering card remains in LeanPlan, a challenged hook fetches the live definition where Metacognition is installed and falls back to the gloss where it is not, and the `context-isolation`-class drift that issue #27 names can no longer occur — because there is no copy left to fall behind.

## Guarantee

- **Operation needs nothing external** — running any LeanPlan stage to author or review a feature never requires Metacognition or any external knowledge base. The live dependency is confined to deep, challenge-time grounding, which is off the default working set. (This narrows the former "portability is inviolable" stance: operation and named grounding stay self-contained; only the deep definition layer becomes a live dependency.)
- **Never a hard failure when the source is absent** — when Metacognition is missing or unreachable, grounding degrades to LeanPlan's own gloss rather than erroring, the way existing hooks skip when a tool is absent.
- **No divergent copy** — LeanPlan retains no distilled fork of the source's content; the deep layer *is* the source, so it cannot be stale relative to it.
- **Grounding stays off the hot path** — resolving a hook to its definition stays a challenge-time act, never carried in the default review surface.
- **Referential integrity is LeanPlan's only standing obligation to upstream evolution** — the hooks and map name concepts by slug, so the one coupling that survives unvendoring is that those names must still resolve in the live source. Keeping them valid is a one-way (Metacognition→LeanPlan), advisory concern — LeanPlan never pushes changes upstream. A concept's *semantic* correctness or health is Metacognition's repair responsibility, never LeanPlan's: LeanPlan validates that the reference link operates, not what it points to.

## Non-goals

- **Not a content re-distillation tool, and not the reference-link checker itself.** Issue #27's original lever — re-distilling a copy to keep it honest — is superseded: there is no copy to re-distill. The surviving, redirected need — an advisory check that LeanPlan's grounded slugs still resolve upstream — is named here as a one-way reference-link **soft-gate**, but built as a **fast-follow feature**, not in this one. Semantic review of concepts stays out of scope (Metacognition's responsibility).
- **Not removing the hooks or the rule→concept map.** Those are LeanPlan-authored and stay; only the copied definition cards are dropped.
- **Not expanding grounding to the other sibling knowledge bases.** Only context-engineering is grounded; the other Metacognition disciplines stay un-grounded, per the prior drift verdict.
- **Not a stage-model, validator, or artifact-contract change.** The five stages, their contracts, and the validator are untouched.

## Upstream

- Issue #27 (Backlog K) — https://github.com/mynghn/leanplan/issues/27 — reframed here from "sync/drift-check for the vendored snapshot" to "drop the snapshot, depend live."
- Source of #27: the full-framework adversarial review and its CE-snapshot drift verdict.
- Prior feature being reversed: `docs/features/260619-context-engineering-knowledges-grounding` — its `C-1` portability constraint and `D-1` / `D-2` / `D-8` rationale (the original vendoring decision).
