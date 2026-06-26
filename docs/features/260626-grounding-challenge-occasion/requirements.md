# 260626-grounding-challenge-occasion — Model when (and why) a grounded rule's challenge consults Metacognition

## Problem

LeanPlan grounds each load-bearing rule in a context-engineering concept via `(context-engineering: <slug>)` hooks whose deep definitions now resolve live from Metacognition. The framework says these resolve "when a hook is challenged" and that the design archive is the "challenge-time home" — but it never models what that *challenge occasion actually is*: who interrogates a rule's grounding, when, and why. The mechanism is well-specified; the occasion behind it is left implicit.

Worse, **"challenge" is overloaded**. The §9 "Challenge mechanism" and the implementation stop-the-line triggers name a *different* event — an implementation-time artifact-vs-reality drift that routes to `revise` — yet share the word with the grounding interrogation that routes to Metacognition. A reader cannot tell which "challenge" loads the live source, nor when reaching for it is the right move.

Who feels it: the **maintainer / auditor**, who finds no single statement of when Metacognition is the right thing to consult (it had to be reconstructed from scattered pieces just to be stated); and any **reader** parsing "challenge", who conflates the implementation-drift event with the grounding-interrogation event. The net effect: the live dependency's *timing and role* read as vague even though its *mechanism* is precise.

## Outcome

LeanPlan crisply models the occasion on which a grounded rule's challenge consults Metacognition — a reader can tell *when* and *why* the live source is the right thing to reach for, and tell that event apart from the implementation-time challenge. The already-specified mechanism gains its missing occasion and trigger semantics in one prose home, with no new machinery.

User stories:

- **One home for "when to consult Metacognition"** — a single place states the occasion: interrogating a load-bearing rule's grounding — auditing it, evolving it, disputing it, or authoring a new grounding — off the operational path.
- **The two "challenges" are distinguishable** — a reader can tell the implementation-time challenge (artifact-vs-reality → `revise`) from the grounding challenge (rule-vs-evidence → Metacognition) without conflating the two.

Confirmed when a reader, given any `(context-engineering: <slug>)` hook, can name the occasion that would lead them to consult Metacognition and distinguish it from the §9 implementation challenge — from a single prose home, loading nothing external.

## Guarantee

- **Minimal altitude** — Metacognition-consultation stays modeled at the "on challenge, off the hot path" level. The sharpening clarifies the occasion in prose; it never promotes consultation to a move, stage, or subsystem. The framework's lean surface is preserved — a paragraph, not a subsystem.

## Non-goals

- **Not a new abstraction** — no named "consultation move", no dedicated lifecycle section, no sub-occasion taxonomy as formal concepts.
- **Not a mechanism change** — live resolution, the gloss fallback, and the link-check freshness gate are untouched; only the occasion and trigger *semantics* become explicit.
- **Not a stage-model, validator, or artifact-contract change.**

## Upstream

- Parent: `docs/features/260626-live-ce-grounding` (PR #57) — established the live Metacognition dependency and the `framework-design.md` §13 framing this sharpens.
- Sibling: `docs/features/260626-ce-grounding-link-check` — the referential-freshness half of the same relationship; this feature is the consultation-occasion half.
