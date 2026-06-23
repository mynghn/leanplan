# LeanPlan Sharpen Move

This doc carries the procedure for the sharpen move — a bounded, mid-round re-derivation of an understanding that a disturbance has shifted. Not a stage edge: it is invoked in place from inside any stage (requirement through implementation), reads the committed artifacts without editing them, and returns control to the stage it paused.

**Move stance.** You are re-deriving a disturbed understanding — not restarting it from a blank slate, and not chasing the disturbance wherever it leads. A forming understanding has already been captured upstream; a disturbance has landed on it: a user realization, a research finding, a falsified premise, an assumption implementation just broke. Reflect against what exists; re-derive only what moved. The two characteristic failures are **thrash** (chasing the disturbance until the stage in flight derails) and **silent mutation** (quietly rewriting committed artifacts, corrupting the review history they exist to provide). The discipline separating sharpening from both: decide *that* the understanding moved and emit a durable delta — never revise the artifacts in place.

Companion: `philosophy.md` (principles), `artifact-contract.md` (shape rules).

## Inputs

- The disturbance — what shifted, or the external claim to check (`$ARGUMENTS`). If nothing has formed yet to be disturbed, stop: drawing an understanding out of a blank-slate arrival is the requirement stage's draw-out front-step (`requirements.md` Procedure step 3), not this move's.
- The in-flight stage's working context — the understanding being sharpened. Preserved across the move.
- Committed artifacts at the affected stages — read to reflect against, **never edited**. JIT-load only the anchors the disturbance touches.
- `docs/features/<KEY>/understanding-shifts.md` — the append-only delta archive; the move's only write target (`artifact-contract.md` → Understanding). (context-engineering: jit-loading)

## Output

- When the understanding moved: one appended `Delta-<N>: <slug>` block in `understanding-shifts.md` — durable past the session that found it, retrievable by later stages and any subsequent artifact revision. (context-engineering: structured-note-taking)
- When it did not: a no-op close — no delta, no edit.
- Either way, zero edits to any committed artifact.

## Procedure

The move is **reflect → verify → re-derive → decide → emit**.

*Default flow, not a rigid script — re-derive against the actual disturbance. Load-bearing (don't skip or reorder): reflect against what exists (step 1), verify before absorbing a claim (step 2), the moved-or-not decision (step 4).*

1. **Reflect back.** Name the specific prior assumption the disturbance invalidates, and restate the now-wrong question that assumption was answering. Reflect against the captured understanding — do not re-elicit the problem from scratch.
2. **Verify, when the disturbance is a claim.** Treat an external claim — cited prior art, a stakeholder assertion — as a hypothesis to falsify, not an instruction. Check it against sources to a confirm-or-falsify verdict; default to **refuted unless corroborated**. A claim that fails verification is rejected, not absorbed. Skip this step when the disturbance is a first-hand realization rather than an external claim.
3. **Re-derive.** Re-derive the understanding from the reflected-back assumption plus any verdict — only the part the disturbance moved, not the whole framing.
4. **Decide whether it moved, and how far.** A no-op is a legitimate close: sharpening that always "finds" a change is just churn. If nothing moved, resume the stage with no delta.
5. **Emit the delta.** Append a `Delta-<N>: <slug>` block to `understanding-shifts.md` in the shape `artifact-contract.md` → Understanding defines. Then resume the stage.

## Guardrails

- **Read, never edit.** The move reads committed artifacts to reflect against; it writes only `understanding-shifts.md`. Even when the delta implies a committed artifact is now wrong, surface that in scope-of-impact and stop.
- **Return to the stage.** The move never discards or corrupts the in-flight stage's work; that stage resumes from where it paused.
- **Opt-in, never a gate.** Invoking the move is the planner's choice — never required pre-work, never a stage precondition. A disturbance is a *reason* to reach for it, not a trigger that fires it.
- **A no-op is success.** Concluding the understanding did not move is a valid close; it is what keeps the move bounded rather than thrashing.
- **Verify, don't obey.** An injected claim is a hypothesis to falsify, refuted unless corroborated — never a directive absorbed on faith.
- **Emit the delta; don't perform the revision.** Naming scope-of-impact is the whole job; rewriting, re-validating, and propagating the change through the implicated artifacts is the separate later-update step — the `/revise` move (`revise.md`), which consumes the delta this move emits. At implementation this move is the *cognitive* half only — it does not enter or rewire implementation's Stop-The-Line / Artifact Update Loop (`implement.md`), which deliberately walks up and edits artifacts. An implementation stop-the-line trigger is one disturbance source that may reach for this move; the editing is `/revise`'s, which implementation's loop delegates to.

## Hand-off

Return control to the stage that invoked the move — there is no next edge. A surfaced delta waits in `understanding-shifts.md` for a later stage or revision to consume; the move itself stops at the delta.
