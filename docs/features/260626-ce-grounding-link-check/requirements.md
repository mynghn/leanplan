# 260626-ce-grounding-link-check — Keep LeanPlan's grounding reference-links valid against the live source

## Problem

LeanPlan grounds each load-bearing rule in a context-engineering concept named by slug — the `(context-engineering: <slug>)` hooks and the `context-engineering.md` map. Once the deep definitions resolve live from Metacognition (feature `260626-live-ce-grounding`), those slugs become a one-way reference coupling: if Metacognition renames, merges, or retires a concept, LeanPlan's hooks and map keep naming a slug that no longer resolves — and the failure is **silent**. The live lookup finds nothing, the local gloss fallback masks the gap, and a grounded rule's "why" quietly stops reaching a real upstream concept while still appearing grounded. Today LeanPlan's slugs match the live source exactly — but only by recency, not by any process, the same liability issue #27 named for stale content, now at the reference layer. Nothing surfaces a dangling grounding except chance.

Who feels it: the **maintainer**, whose framework loses traceability — the grounding credibility that is the whole reason the hooks exist — with no warning; and a **challenger**, who resolves a hook, silently gets only the gloss, and never learns the upstream concept is gone.

## Outcome

LeanPlan can verify on demand that its context-engineering grounding still references the live Metacognition source — making reference integrity a process, not luck. After a Metacognition change, the maintainer runs a self-inspection and gets an advisory worklist: which grounded slugs no longer resolve upstream, and whether the live resolution path is reachable at all. The inspection is one-way (Metacognition→LeanPlan) and advisory — it reports; the maintainer decides and applies any correction through LeanPlan's existing revise path. It validates that the reference link operates; it never judges what the link points to.

User stories:

- **Surface dangling grounding** — running the self-inspection lists every grounded slug that no longer resolves in the live source (renamed, merged, or retired upstream), turning a silent break into a named worklist item.
- **Tell "source absent" from "concept gone"** — the inspection reports whether the live resolution path is present and resolving, so an expected gloss-fallback (Metacognition not installed) is distinguished from a real dangling reference (source present, slug missing).
- **Report-only, human-gated** — the inspection only reports; corrections flow through LeanPlan's normal revise move. Nothing in LeanPlan is auto-edited, and nothing is ever written upstream.

Confirmed when, run after a Metacognition change that retires or renames a grounded concept, the inspection names exactly the affected LeanPlan grounding and nothing spurious; and run against an agreeing source, it reports clean — which is what it reports today, with LeanPlan's slugs matching the live source one-to-one.

## Guarantee

- **Reference-only, never semantic** — the inspection checks that a grounded slug resolves and that the resolution path is reachable; it never assesses a concept's meaning, correctness, or health (including any upstream degraded / `⚠` flag). Whether a concept's content is right or current is Metacognition's responsibility, not LeanPlan's.
- **One-way and advisory** — Metacognition→LeanPlan only; the inspection reports and never auto-edits LeanPlan, and LeanPlan never writes anything upstream.
- **Degrades, never blocks** — when Metacognition is absent, the inspection reports "source absent — expected gloss fallback," not an error; it mirrors the framework's own graceful-degradation posture and needs nothing external to run.

## Non-goals

- **Not a content-freshness or re-distillation check** — there is no vendored copy to refresh; definitions are live. This inspects references, not content.
- **Not an automated watcher** — detection is human-triggered (run on demand, e.g. after a Metacognition update). An always-on listener is a possible later iteration, not this feature.
- **Not a semantic or quality review of concepts** — concept correctness and health are Metacognition's domain.
- **Not auto-repair** — fixes go through the existing revise move, human-gated; the inspection never edits grounding itself.
- **Not a change to the stages, validator, or artifact contract.**

## Upstream

- Parent feature: `docs/features/260626-live-ce-grounding` — established the live Metacognition dependency and named this fast-follow (its Requirements `## Guarantee`, Design `D-3`, and `understanding-shifts.md` `Delta-1`). Its merge is a prerequisite for *implementing* this inspection (it operates on the post-`260626` live-grounding model), though this contract is planned independently.
- Issue #27 (Backlog K) — the originating "process, not luck" intent, redirected here from the content layer to the reference layer.
