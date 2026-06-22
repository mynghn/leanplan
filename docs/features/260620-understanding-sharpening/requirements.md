# 260620-understanding-sharpening — Sanctioned mid-round understanding-sharpening

## Problem

A LeanPlan round treats the problem understanding as settled once it's captured — yet understanding keeps shifting whenever a disturbance lands on it: the user realizes something mid-stage, research returns a finding, a premise proves false, or implementation exposes a wrong assumption. These land once an understanding has begun to form — anywhere from mid-requirement through implementation, not at a tidy front. LeanPlan sanctions understanding-work at exactly one moment — blank-slate, before the requirement stage. Once a round is underway there is no sanctioned move for *"stop — the framing just changed under me; re-derive it."*

So whoever runs the round — agent and user together — improvises, and improvisation fails two ways: **thrash**, chasing the disturbance unbounded until the stage in flight derails; or **silent mutation**, quietly rewriting committed artifacts and corrupting the traceability and review history they exist to provide. Either way a falsified premise can slip downstream, and the round keeps building on understanding it should have stopped to re-derive.

## Outcome

LeanPlan offers a **sanctioned, bounded sharpening move invocable from inside any stage** — requirement through implementation — triggered by a disturbance to the current understanding, not by ordinary stage iteration. It reflects and re-derives *without* touching committed artifacts, and its product is a durable record of how the understanding changed. It engages only where an understanding already exists to be disturbed; drawing a *sparse* arrival out from a blank slate — when nothing has formed yet — is a separate concern (Non-goals).

User stories:

- **Sharpen from inside any stage** — when a disturbance hits the current understanding mid-stage, the planner invokes a sanctioned sharpening move right there, instead of ignoring the disturbance or hand-rolling a response.
- **Reflect back the broken assumption** — the move names the assumption the disturbance just invalidated and reflects back the now-wrong question, rather than re-interrogating the problem from scratch.
- **An injected claim is checked, not obeyed** — when the disturbance is an external claim, the move surfaces it as a hypothesis to verify, so a wrong claim is caught before it reshapes the round.
- **A durable understanding delta** — the move's product is a recorded delta — what changed, why, which prior assumption it kills — that persists beyond the moment it's found and that downstream stages, and any later artifact revision, consume.

System policies:

- **Bounded, never derailing** — sharpening re-derives understanding *without* auto-mutating any committed artifact; the stage in flight is preserved. This discipline is what separates sharpening from thrashing.
- **Opt-in, never mandatory** — the move is available when understanding is disturbed; it never becomes forced pre-work and never gates a stage. The bet is keeping understanding *correct*, not adding ceremony.
- **Decide, then hand off — never revise in place** — the move decides *that* understanding moved and how far, and emits the delta; turning that into rewritten artifacts belongs to the separate later-update process. Sharpening may legitimately end with no artifact change at all.

Confirmed when: a planner who hits a mid-round disturbance has a sanctioned move to reach for instead of improvising; the move ends with a recorded understanding delta and zero silent edits to committed artifacts; and a falsified premise is named and stopped rather than carried silently downstream.

## Non-goals

- **Performing the artifact revision** — re-opening, rewriting, re-validating, and propagating a changed understanding through committed artifacts (including feature splits/renames) is the separate later-update feature. This move decides understanding moved and emits the delta; it does not edit the artifacts.
- **Drawing out a blank-slate arrival** — eliciting an understanding when the user arrives with nothing formed yet (the front-of-round *sparse-arrival* draw-out) is a separate requirement-stage interactivity concern, parked as issue #12. This move sharpens an understanding that already exists and just shifted; it does not form one from a vacuum — its reflect-back, verify-claim, and kill-an-assumption mechanics all presuppose a prior understanding.

## Upstream

- LeanPlan self-feedback distill, 2026-06-20 (thread 4, broadened then sharpened). Canonical framing: issue #8.
- Grounding: the 0004-knowledge-base-rehome round — three real mid-stream understanding shifts (a user realization reframing the problem; an injected prior-art claim verified and falsified; a synthesis forcing a feature split), none at front-of-round.
