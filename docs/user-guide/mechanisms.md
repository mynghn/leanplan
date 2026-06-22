# LeanPlan Mechanisms

This page explains LeanPlan-specific behavior that affects what the agent asks for, what it writes, and when it stops. It is explanatory user documentation, not canonical agent procedure.

## Brevity controls

What you see: LeanPlan pushes artifacts to stay short and focused.

Why it exists: LLMs perform better when the working set is compact and relevant. Long artifacts hide the current decision inside stale or duplicated context.

How to work with it: keep surface artifacts lean, move detailed rationale into archive material when needed, and cite instead of restating the same fact in multiple places.

When to challenge it: if a short artifact no longer carries enough intent for implementation or review, add the missing constraint in the artifact that owns it instead of relying on memory.

## Stage ownership

What you see: each stage owns a different kind of fact.

Why it exists: one prose home per fact reduces drift. Requirements own intent, Spec owns behavior, Design owns approach, Tasks own execution order, and implementation owns durable delivered rationale.

How to work with it: place new information in the highest artifact it affects. If a behavior changes, update Spec before Design or Tasks.

When to challenge it: if the same fact appears in several artifacts, remove duplication or keep only a citation where the downstream artifact needs a pointer.

## Surface and archive layering

What you see: the main artifacts stay compact, while longer rationale can live in supporting archive material.

Why it exists: reviewers and agents need the current decision path quickly, but deeper history should still be recoverable when it matters.

How to work with it: keep the main artifact decision-ready. Move detailed exploration, rejected alternatives, and long analysis out of the surface artifact unless the next stage must read it every time.

When to challenge it: if a downstream task cannot be done safely without opening an archive every time, promote the needed constraint into the surface artifact.

## Traceability

What you see: later artifacts point back to earlier behavior, constraints, and decisions.

Why it exists: implementation should not become a disconnected task list. Traceability keeps a task tied to the reason it exists and helps reviewers see whether the delivered work still satisfies the original intent.

How to work with it: preserve meaningful links while planning, then carry the substance of important constraints into durable project surfaces during implementation.

When to challenge it: if a citation points to an anchor whose substance no longer matches the task, revise the plan rather than treating the citation as decorative.

## Validation

What you see: `validate.py` checks feature artifacts and reports contract problems.

Why it exists: LeanPlan uses lightweight automation to catch missing sections, broken coverage, and shape drift before implementation relies on a bad plan.

How to work with it: run validation before implementation and after plan edits. Treat failures as signals that the plan needs correction.

When to challenge it: validation checks artifact structure and coverage, not whether the product decision is wise. Human review still owns product judgment and implementation quality.

## Stop-the-line moments

What you see: the agent pauses instead of continuing when it finds contradictions, missing verification paths, invalid dependencies, externally visible behavior changes, unprovable constraints, or scope expansion.

Why it exists: continuing through known drift creates plans that look valid but no longer describe the work being done.

How to work with it: resolve the highest affected layer first, usually through revise, then continue implementation.

When to challenge it: if the pause is caused by uncertainty rather than real drift, answer the decision directly and continue without expanding the plan.
