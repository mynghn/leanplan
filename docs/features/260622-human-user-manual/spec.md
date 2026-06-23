# 260622-human-user-manual — Spec

## Behavior

### B-1: first-run-path
A first-time reader can find and complete a short first-use path that explains where to start, what the user does, what the agent does, what artifacts are produced, and how the reader knows the first LeanPlan flow is complete.

### B-2: end-to-end-workflow-guide
A returning reader can follow LeanPlan from requirements through implementation, with each stage described by its purpose, user decision points, artifact responsibility, and hand-off to the next stage.

### B-3: mechanism-explanations
A serious reader can find plain-language explanations of LeanPlan-specific mechanisms, including brevity controls, stage ownership, traceability, off-pipeline moves, validation, and stop-the-line moments. Each explanation states the user-visible behavior, the reason it exists, and where the user can challenge or intervene.

### B-4: adoption-guidance
A team evaluating LeanPlan can find guidance for introducing it gradually, choosing an appropriate first project, setting expectations for user-agent collaboration, and recognizing when the framework is being used outside its intended shape.

### B-5: lookup-reference
A power user can quickly look up the workflow stages, commands, artifact shapes, review expectations, and stage transition cues without reading the full guide from the beginning.

### B-6: existing-concept-alignment
A reader who moves between the human-facing docs and existing LeanPlan references encounters the same concept names, stage names, and artifact vocabulary, so the guide clarifies the framework without creating a parallel model.

## Constraint

### C-1: progressive-disclosure
The documentation remains useful at multiple depths: first-time readers can stop after the entry path, returning users can continue into workflow guidance, and serious users can drill into mechanisms and reference material without the entry path carrying all of that depth.

### C-2: mechanism-transparency
LeanPlan behavior is not described as agent magic or unexplained preference. Framework-specific behavior that constrains the user or agent is paired with its purpose and user-facing effect.

### C-3: non-canonical-agent-instructions
The human-facing docs do not become the canonical operating instructions for agents. They may explain agent-facing references to users, but they do not replace those references as the source of agent procedure.

### C-4: no-framework-behavior-change
The documentation suite describes the current LeanPlan workflow without requiring changes to stage behavior, artifact semantics, or validation behavior as part of this feature.
