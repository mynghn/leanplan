# 260620-artifact-later-update — Sanctioned in-flight artifact later-update

## Problem

Mid-build, the committed plan drifts from the understanding it is meant to encode, and it has to catch up. The cause need not be external: the world changed (a late stakeholder requirement, a revised external contract), or the planner changed their mind, or an assumption was wrong from the start and only surfaced now — when a task hit it, or thin earlier review finally caught it. But LeanPlan sanctions revising a committed artifact in exactly one place: the impl-stage Artifact Update Loop, which fires only from impl stop-the-line triggers. Every other occasion — a shift caught at an earlier stage, at a stage boundary, or between tasks — has no sanctioned entry point, and even that one loop is siloed inside impl. Validation is stateless, with no notion of staleness, so nothing flags the artifacts as out of date.

So whoever runs the round improvises, and improvisation fails two ways: **silent hand-editing** — rewriting validated artifacts and re-running validation by hand, with no traceable guarantee the change reached every downstream artifact it touches, so a stale assumption slips through to implementation and you build the wrong thing; or **off-framework surgery** — structural changes like splitting one feature into two or renaming its directory, done with raw shell (`mv`, `sed`) outside any skill and bypassing the directory allocator, which strands artifacts (the grounding split left design stubs unread at the new path). Either way the plan and reality diverge with nothing to catch it.

## Outcome

LeanPlan offers a **sanctioned, planner-invocable update** that injects a known drift — whatever its cause — into the committed plan from inside any in-flight stage, requirement through impl. It re-opens the affected artifacts, revises them, re-validates, and propagates the change downstream so nothing stale reaches implementation — preserving prior work rather than blowing it away, and responding in proportion to how far the change ripples. It runs only on a justified drift, never as a license to silently rewrite.

User stories:

- **Inject a known drift from any stage** — when a change lands mid-flight (at an earlier stage, at a stage boundary, between tasks, or during a task mid-impl), the planner invokes a sanctioned update right there, instead of hand-editing validated artifacts or doing raw-shell surgery.
- **Propagate downstream, leave nothing stale** — the update reflects the change through every downstream artifact it touches and re-validates, so a revised understanding reaches implementation intact rather than as a stale assumption that slipped past.
- **Preserve prior work** — the revision is surgical, not a blow-away rewrite: the review and traceability history survives, and superseded content is retired legibly rather than silently deleted.
- **Structural ops are first-class** — splitting a feature or renaming it is a supported operation that routes directory allocation through the framework's allocator and leaves no artifact stranded at an old path.

System policies:

- **Effort proportional to volatility** — artifacts differ in how often and how easily they change, and an update responds proportionately instead of imposing the same ceremony on every edit. The exact gradient is a design decision; the requirement is only that the differential is acknowledged, not flattened.
- **Never fires unjustified** — an update runs only when the understanding genuinely moved (handed off from a sharpening delta, an impl stop-the-line, or asserted by the planner). Absent that justification the artifacts must not move; this is the guard against silent drift.

Confirmed when: a planner who hits a mid-flight drift has a sanctioned update to invoke instead of improvising; the update propagates through every downstream artifact and re-validates, so nothing stale reaches implementation; prior work survives the revision (history intact, superseded items retired not deleted); and a feature split or rename routes through the allocator and strands no artifact.

## Non-goals

- **Post-deploy drift tracking** — once the feature ships, code is truth and the artifacts are discardable (P6). Keeping the docs in sync with a deployed, living feature is out.
- **Code-led reconciliation after impl** — folding uncommunicated, as-built commits back into the artifacts once implementation is done. This update is forward-protective: it propagates a known *understanding* drift downstream to protect work not yet built. After the last task there is no downstream left to protect, and syncing artifacts to final code is the reverse-direction work P6 retires. (A finished feature whose artifacts are still upstream for a *separate* in-flight feature is handled by that feature's own update — it still has un-built downstream.)
- **Detecting the drift or deciding the understanding moved** — surfacing drift (independent/adversarial review, #15) and deciding the framing actually shifted (understanding-sharpening, #8) are separate features. This update *consumes* a justified delta and repairs the artifacts; it does not find the drift or adjudicate it. Detect (#15) → decide (#8) → repair (this).

## Upstream

- Canonical: issue #9 ("Backlog: C — Artifact later-update process", `label:backlog`).
- Family: sibling **#8** (understanding-sharpening) emits the understanding delta this update consumes; **#15** (independent drift detection) routes findings to it. The three are impl's fused stop-the-line + Artifact Update Loop pulled apart and generalized across every stage: detect (#15) → decide (#8) → repair (this).
- Grounding: the 0004-knowledge-base-rehome round — at the spec→design boundary the feature was split (0004 foundation + 0005 generator), forcing in-place rewrites of already-validated requirement/spec artifacts and a raw `mv`/`sed` directory rename outside any skill; the rename left design stubs unread at the new path. The exact gap this closes.
