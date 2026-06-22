# 260620-sparse-arrival-drawout — Spec

## Behavior
### B-1: drawout-engages-on-sparse-arrival
When the requirement stage begins with a sparse arrival — input that carries no formed problem understanding — an elicitation exchange engages before any distillation, rather than the sparse input being distilled as-is.

### B-2: candidate-framings-offered-for-choice
When the elicited problem admits more than one plausible framing, the draw-out presents the alternatives for the planner to choose among, rather than silently adopting the first framing.

### B-3: unclear-details-surfaced-before-distill
When the sparse input has gaps or ambiguities bearing on the problem, the draw-out raises them and resolves them with the planner before distillation.

### B-4: distill-consumes-formed-understanding
When the draw-out concludes, distillation operates on the elicited understanding, so the committed requirement reflects that understanding rather than the original sparse phrase.

## Constraint
### C-1: opt-in-never-forced
The draw-out is never mandatory. It never blocks the stage, never becomes required pre-work, and never auto-fires as a stage precondition; the planner can always decline it or cut it short and proceed to distillation. An arrival that already carries a formed understanding is never subjected to it.

### C-2: drawout-forms-understanding-not-requirement
The draw-out only forms the planner's understanding; it never writes or commits the requirement artifact. Distillation remains the sole producer of the committed requirement.

## Non-goals

- **Re-deriving an already-formed understanding that a disturbance shifted** — that is the sibling sharpening contract (issue #8). This Spec governs the cold start, where no understanding exists yet to reflect against; its trigger is the *absence* of a formed understanding, not a disturbance to one.
