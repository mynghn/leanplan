# 260619-context-engineering-knowledges-grounding — Ground LeanPlan in proven context-engineering practice (portably)

## Problem

LeanPlan's entire design rests on context-engineering claims — agents have limited useful context, weak long-range attention, and do better with just-in-time intent plus current code. Those claims are **asserted, not traceable**: nothing connects a given framework rule to the established principle it implements. The cost lands on three readers:

- An **adopter** evaluating LeanPlan can't tell principled rules from arbitrary ones — trust rests on faith.
- A **maintainer** evolving it can't tell rules that are load-bearing-for-a-reason from incidental ones — changes risk eroding the design silently.
- Anyone **challenging** a rule finds the "why" bottoms out in assertion, not evidence.

The framework also doesn't always **practice what it preaches**, which undercuts credibility exactly where consistency would earn it. And whatever closes these gaps must not cost LeanPlan its defining property: it ships **self-contained and portable**, usable anywhere with nothing beyond what it ships.

## Outcome

LeanPlan becomes **credibly and traceably** grounded in context-engineering practice and visibly **conforms to its own advice** — with no loss of portability or leanness. This grounds and reconciles the existing framework; it does not restructure it.

User stories:

- **Trace a rule to its principle** — for any load-bearing rule, a reader can reach the recognized principle it implements and judge whether it holds.
- **Evolve with confidence** — a maintainer can see what each grounded rule rests on, so rules change or extend without silently breaking the design's logic.
- **Grounding travels with the install** — whoever installs LeanPlan gets the grounding too; it works standalone, needing nothing beyond what it ships.
- **The framework follows its own advice** — the guidance agents act on while running a stage embodies the same practices the framework teaches, instead of contradicting them.

System policies:

- **Portability is inviolable** — shipped LeanPlan never requires anything external to run.
- **Freshness is honest** — when the grounding was last reconciled against its sources is visible, so staleness cannot hide.
- **Leanness is preserved** — grounding must not inflate the day-to-day review surface that keeps artifacts reviewable.

A newcomer can take any load-bearing rule, follow it to the principle it implements, confirm the principle is sound — loading nothing LeanPlan doesn't itself ship — and observe the framework's own behavior conforming to those principles.

## Non-goals

- **Not a stage-model redesign.** The five stages, their contracts, and the validator stay as they are.
- **Not an automation deliverable.** Tooling to keep grounding fresh is optional, not required to satisfy this feature.
- **Not exhaustive grounding.** Only load-bearing rules need grounding; incidental conventions don't.

## Upstream

- Synthesis brief: `leanplan-ce-grounding-brief.md` (originating direction).
- Prior design reports: `leanplan-ce-revision-plan.md`, `ce-grounding-redesign-plan.md`.
