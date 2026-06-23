# 260622-human-user-manual — Human-facing LeanPlan documentation suite

## Problem
LeanPlan is approaching v1.0, but its public learning surface is still weighted toward agent-facing references, adapter instructions, and framework internals. New users lack a clear path from first successful use to serious adoption, and serious users lack a human-readable explanation of the framework behaviors they are expected to trust.

This makes LeanPlan feel more like a black box than a workflow a user can reason about. Users can see that agents produce brief artifacts and enforce boundaries, but they cannot easily learn which mechanisms create those outcomes, what tradeoffs they imply, or when the user should intervene.

## Outcome
LeanPlan has a progressive documentation suite that teaches the workflow from first run through serious use, with enough mechanism-level explanation that users understand both what to do and why the framework behaves the way it does.

User stories:

- **First successful use** — a new user can follow a short path from install-ready context to a complete first LeanPlan planning flow. The path makes the user's role and the agent's role explicit.
- **Workflow fluency** — a returning user can understand the end-to-end stages, what each artifact owns, and how work moves from requirements through implementation.
- **Mechanism transparency** — a serious user can learn the LeanPlan-specific behaviors behind the workflow, including brevity controls, artifact ownership, traceability, off-pipeline moves, and stop-the-line moments.
- **Adoption confidence** — a team evaluating LeanPlan can see how to introduce it gradually, what discipline it expects from users, and which behaviors are deliberate framework choices rather than incidental agent behavior.
- **Reference confidence** — a power user can quickly look up commands, artifact shapes, stage responsibilities, and review expectations without rereading the full guide.

Success is visible when a reader can move from first-time orientation to confident serious use without relying on agent-facing references as the primary manual, and when the documentation explains LeanPlan's mechanisms clearly enough that brevity and review discipline no longer feel like hidden magic.

## Guarantee
- **Progressive disclosure** — the suite serves first-time, returning, and serious users without forcing every reader through the same depth. This keeps the entry path approachable while preserving depth for adoption and review.
- **Mechanism clarity** — LeanPlan-specific behavior is explained as visible framework mechanics, not as opaque agent preference. Users should understand the intent behind brevity, stage boundaries, traceability, off-pipeline moves, and review surfaces.
- **User agency** — the docs make clear where the user decides, confirms, challenges, or stops the workflow. LeanPlan should feel collaborative and inspectable, not autonomous in a way the user cannot govern.
- **Framework consistency** — the human-facing docs teach the same concepts and vocabulary LeanPlan already uses. They clarify the framework rather than inventing a parallel model.

## Non-goals
- Replacing the existing agent-facing references as the canonical operating instructions for agents.
- Rewriting the framework itself or changing LeanPlan stage behavior as part of the documentation work.
- Exhaustively documenting every adapter-specific edge case in the main user path.

## Upstream
- GitHub issue #23: https://github.com/mynghn/leanplan/issues/23
