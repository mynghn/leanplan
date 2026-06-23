# 260623-deferral-lane — Deferred decisions reach the stage that owns them — without loss, bloat, or pinning

## Problem

While a planner works one LeanPlan stage, decisions that belong to a *later* stage surface anyway — a realization "how" occurs mid-Requirements, an internal-shape question mid-Spec. LeanPlan's discipline tells the planner to push these away: Requirements strips solution suggestions, the sparse-arrival draw-out writes nothing, the self-check expects zero leakage. So the deferred decision — and the reason it surfaced — is *discarded*, not set aside. When the owning stage finally arrives, the planner re-derives from a blank slate, having thrown away the original spark.

The obvious fix — just keep the deferred thoughts — fails in two opposite ways, both worse than the loss:

- **Kept thoughts bloat the surface.** LeanPlan's core bet is that a lean artifact gets reviewed carefully and a verbose one gets rubber-stamped. A growing pile of parked items on the review surface breaks that bet.
- **Kept thoughts pin the later stage.** A spark deferred from Requirements that reaches Design reading like a settled choice *forecloses* the free exploration Design exists to do — against an option space that is now larger than when the spark first appeared.

So today the planner has only bad options: discard the spark (lose it), or keep it (bloat, or pin). Felt by anyone running a multi-stage planning round — sharply across rounds or sessions, where "it is still in the conversation" no longer holds.

## Outcome

A planner can deliberately set a decision aside when it surfaces at the wrong altitude, and trust it returns at the stage that owns it — carried with enough context (the spark, and why it surfaced) to act on, without growing the surface a reviewer reads, and without pre-committing the choice.

User stories:

- **Defer without losing** — a planner sets a decision aside mid-stage and later finds it waiting, with its original spark, at the stage that owns it — no re-derivation from scratch.
- **Re-open, don't inherit** — reaching a deferred decision, the owning stage re-examines it against its full current option space rather than treating it as already settled.
- **Catch the natural roam-off** — the planner preserves a decision that surfaced on its own during ordinary stage work, and is never pushed to go exploring low-altitude detail to fill the record.
- **Review stays lean** — a reviewer reads an early artifact that stays lean even though deferrals from it were captured.

Success signal: a decision deferred in an early stage is later picked up and visibly re-examined at its owning stage — evident in the planning record, not merely believed to have happened.

## Guarantee

- **Nothing deferred is silently lost.** A set-aside decision reliably reaches its owning stage; one never picked up surfaces as an omission rather than vanishing. *Why:* silent loss is the worst outcome — the planner stops trusting the move and reverts to discarding, or to deciding early.
- **The working surface stays lean.** Capturing deferrals must not inflate the artifacts a reviewer reads to review or implement. *Why:* a bloated surface gets rubber-stamped — the exact failure LeanPlan's small-surface discipline exists to prevent.
- **A deferral never pins its owning stage.** A captured decision reaches its owning stage as something to re-decide, never as a decision already made. *Why:* pinning forecloses the full-option-space exploration the later stage owes the problem.
- **Each adjacent planning record has one clear, well-named role.** The new deferral capture and LeanPlan's existing record of mid-round understanding shifts must each read as a single, unambiguous thing under a label that names it — neither an over-broad label whose scope a reader must guess, nor blurred into the other: a deferral is an *open* item to revisit; an understanding shift is a *committed* change to propagate. Scope is these two adjacent records, not a framework-wide relabeling. *Why:* two failures converge — an over-broad label invites mis-reading on its own, and at this feature's seam it specifically lets "hold this open" slip into "act on this now," defeating the no-pinning guarantee at consumption.

## Non-goals

- **Not a forced exploration step.** This adds no phase that makes the planner explore low-altitude detail at an early stage. It preserves only what surfaces on its own.
- **Not an automated gate.** What to defer, and whether a deferral was honored, stays write-time judgment for planner and reviewer; nothing auto-detects, auto-files, or blocks on deferrals.
- **Not a general scratchpad.** It captures genuine cross-stage decisions deliberately set aside — not every passing thought, note, or open question.
