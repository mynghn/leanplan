# 260701-reference-doc-boundaries — Reference-doc boundaries follow topic, not load-occasion

## Problem

LeanPlan's own reference docs — the files an agent loads to run a stage — draw their boundaries by topic, not by when their content is actually needed, so a single load rarely matches what the moment requires.

The clearest case is `artifact-contract.md`: 212 lines bundling 11 separable concerns (feature layout, anchor grammar, required shapes, traceability, one-prose-home, one-concern-per-item, prose style, surface budget, drift guards, and more).
An agent that loads it to answer one question — the anchor citation format, say — pays attention across the other ten concerns it did not need.
The same content is also split the other way: each stage doc re-embeds a Template that restates `artifact-contract.md`'s Required Shapes, so "the shape of a Spec" lives in more than one place an agent may have to reconcile.

Who feels it:

- **The LLM agent running a stage** loads a heavy, multi-concern doc and reasons across near-miss content irrelevant to its current step.
  The framework's own leanness bet rests on the finding that near-relevant content measurably degrades retrieval and lifts error — a bundled reference doc is exactly that noise, on the doc the agent reasons from.
- **The agent needing one concern that spans docs** must load and reconcile more than one file to assemble a single rule, and risks acting on a stale copy.
- **The framework's reflexive credibility** erodes: it preaches progressive disclosure and, as of 260630, One Concern Per Item, yet its own references obey neither at the doc level.

Observed structurally: 12 workflow docs total 898 lines, one of them holding a quarter of that across 11 topics, while the Required-Shapes-versus-per-stage-Template duplication means one concern has more than one home.

## Outcome

Reference-doc boundaries follow load-occasion, not topic: what an agent needs together at a point in its work loads together, and what it does not need does not ride along.

The unit of analysis is a concern — a coherent block of content — and each concern has a load-occasion profile, the set of workflow moments an agent needs it.
Boundaries are re-derived from those profiles from scratch, independent of the current file split: concerns that share a profile group into one independently-loadable unit, and concerns whose profiles diverge become separately loadable.
A single document may legitimately serve many load-occasions; the target is not one file per occasion, only that at each occasion the loaded content is the content that occasion needs.

User stories:

- **Agent loads only what the step needs** — running a stage, the agent pulls the concern its step requires without absorbing unrelated concerns bundled into the same file today.
- **One concern has one reachable home** — a rule such as the required shape of an artifact is authored once and loadable as a unit, not duplicated across a contract doc and per-stage templates.
- **Boundaries are derived, not inherited** — the target grouping comes from mapping concern to occasion, so a reviewer can see why each unit's contents belong together instead of accepting the historical grouping.

Success signal: every concern in the scoped docs is mapped to its load-occasion profile, and each independently-loadable unit holds only concerns that share a profile.
No occasion over-fetches a concern it does not need, and no single concern is fragmented across units so that an occasion must gather it.
A concern needed at several occasions sitting in one unit is not a defect; the defect this removes is the mismatch — concerns with divergent profiles bundled together (over-fetch), or one concern split across units (under-fetch).

## Non-goals

- **Maximal fragmentation.** The goal is not one file per load-occasion; a unit may serve many occasions when they need the same content, and over-splitting only trades over-fetch for the cost of chasing many tiny files.
- **Rewriting the rules themselves.** This re-draws where content lives and how it loads, not what the stage procedures, guardrails, or contract rules say.
- **The challenge-time archive and the front door.** `framework-design.md` (loaded on challenge) and `README.md` (the human entry point) have different load-occasions than the workflow docs and are out of scope here.
- **Re-engineering the loading mechanism.** How skills and adapters trigger a load is not redesigned; boundaries are re-drawn within the existing reference/JIT mechanism, and updating an adapter's pointer to match a new boundary is ordinary follow-through, not mechanism change.
- **A validator gate for occasion-alignment.** Like item-orthogonality before it, this is authored discipline verified by review, not mechanical detection.
