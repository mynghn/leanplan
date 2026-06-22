# 260620-sparse-arrival-drawout — Front-of-round draw-out of a sparse arrival

## Problem

A LeanPlan round is only as sound as the planner's grasp of the problem at the moment `/requirement` distills it — and a planner who arrives *sparse* (a vague itch, a half-formed thought, nothing articulated yet) has no grasp to distill. Nothing at the front of a round draws them out first, so `/requirement` distills the vague phrase as-is into a thin, guessed requirement: the real problem stays under-elicited, plausible alternative framings go unweighed, and unclear details are never surfaced. That guess then propagates downstream, where a misframed problem is the most expensive thing to discover late.

## Outcome

At the front of a round, LeanPlan reliably draws a sparse arrival out — eliciting the problem, weighing candidate framings, surfacing unclear details — until the planner holds an understanding solid enough for `/requirement` to distill a real requirement instead of a guess. This is the literal cold start — forming an understanding where none exists yet; re-deriving an already-formed one that a disturbance shifted is the sibling move (Non-goals).

User stories:

- **Drawn out from a sparse start** — a planner who arrives with nothing formed is engaged to elicit the problem, instead of having a vague phrase distilled into a thin guess.
- **Candidate framings weighed, not the first one grabbed** — the draw-out surfaces more than one plausible framing of the problem and helps the planner choose, rather than locking in whatever they said first.
- **Unclear details surfaced before distill** — gaps and ambiguities in the sparse input are raised and resolved while the understanding forms, so what reaches `/requirement` is complete enough to stand.

System policies:

- **Opt-in, never forced pre-work** — the draw-out is there when an arrival is sparse; it never becomes a mandatory gate and never taxes a planner who already arrives with a formed understanding. Keeping the quick-start lean matters as much as catching the sparse case — the same leanness bet as the sibling move.

Confirmed when: a planner who arrives sparse is reliably drawn into a formed understanding before `/requirement` distills, rather than receiving a thin guess; a planner who arrives already-formed passes through without forced ceremony; and the resulting requirement traces to an elicited understanding, not a one-line phrase.

## Non-goals

- **Re-deriving a disturbed understanding** — when an understanding already exists and a disturbance shifts it (a mid-stage realization, a falsified premise, a returned research finding), reflecting and re-deriving it is the sibling sharpening move (issue #8), not this. The draw-out forms an understanding from a cold start, where there is nothing yet to reflect against.
- **Producing the requirement itself** — the draw-out forms the planner's understanding; distilling that into the committed requirement artifact stays `/requirement`'s job. This move feeds the distill, it does not replace it.

## Upstream

- Canonical framing: issue #12 (split from #8 / B on 2026-06-20, when B was sharpened to the disturbance-driven re-derivation move). Sibling: #8 (B).
- Grounding: thread-4 (original B framing, pre-broadening) + the 2026-06-20 sharp-vs-broad decision (broad umbrella judged inferior on execution).
