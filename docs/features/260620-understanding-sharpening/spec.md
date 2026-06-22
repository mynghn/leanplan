# 260620-understanding-sharpening — Spec

## Behavior
### B-1: sharpen-invocable-mid-any-stage
When a disturbance hits an understanding that has begun to form — at any point from mid-requirement through implementation — the planner invokes the sharpening move in place and it engages within that stage's context.

### B-2: reflect-back-not-re-ask
On invocation, the move names the specific prior assumption the disturbance invalidates and restates the now-wrong question that assumption was answering — rather than re-eliciting the problem from a blank slate.

### B-3: injected-claim-verified-not-obeyed
When the disturbance is an external claim, the move verifies it against sources and produces a confirm-or-falsify verdict before the claim is allowed to reshape the round; a claim that fails verification is rejected, not absorbed.

### B-4: understanding-delta-emitted
When the move concludes the understanding moved, it emits a delta recording what changed, why, the prior assumption it kills, and the scope it implicates (which committed work the change bears on). When it concludes nothing moved, it closes with no delta and no change.

## Constraint
### C-1: no-auto-mutation-of-committed-artifacts
The move performs no edits to any committed artifact. Even when its delta implies a committed artifact is now wrong, the move surfaces that implication (B-4) and stops without editing.

### C-2: in-flight-stage-preserved
Invoking the move never discards or corrupts the in-progress work of the stage it was called from; that stage resumes from where it paused once the move concludes.

### C-3: opt-in-never-gates
The move never blocks a stage, never becomes required pre-work, and never auto-fires as a stage precondition; invoking it is always the planner's choice.

### C-4: understanding-delta-durable
An emitted delta persists beyond the working session that produced it and stays retrievable by later stages and any subsequent artifact revision; it survives a context reset.
