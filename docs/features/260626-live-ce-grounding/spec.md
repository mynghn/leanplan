# 260626-live-ce-grounding — Spec

## Behavior

### B-1: challenged-hook-resolves-live-when-source-present
Resolving a challenged `(context-engineering: <slug>)` hook returns that concept's current definition and source citation **from the live external context-engineering knowledge base** when it is present — never from a definition held inside LeanPlan. One-shot verifiable: with the knowledge base installed, resolve any grounded slug and confirm the definition and citation are the live source entry's.

### B-2: challenged-hook-degrades-to-gloss-when-source-absent
Resolving the same hook when the knowledge base is absent or unreachable returns LeanPlan's own one-line gloss for that rule and completes cleanly — no error, no dangling reference. One-shot verifiable: with the knowledge base removed, resolve any grounded slug and confirm the gloss is returned and the act does not fail.

## Constraint

### C-1: operation-needs-nothing-external
With no external knowledge base installed, every LeanPlan stage authors or reviews its artifact and the validator passes. The external knowledge base is consulted only to resolve deep grounding on challenge, never to run a stage.

### C-2: every-hook-resolves-locally-to-a-named-concept-and-gloss
With no external knowledge base present, every `(context-engineering: <slug>)` hook in the framework resolves through LeanPlan's shipped map to a named concept and a one-line gloss. The hook→concept→gloss chain is complete and local for every hook; only the full sourced definition resolves live.

### C-3: no-vendored-definition-copy-ships
The shipped framework contains no distilled copy of the external knowledge base's concept definitions. The deep-definition layer is the live source itself, so no LeanPlan-held content can drift from it.

### C-4: grounding-stays-off-the-default-surface
The surface loaded by default to author or review a feature is not enlarged by grounding. The map, gloss, and live definition are reachable on demand only, never carried in the default working set.

## Non-goals
- No sync, drift-check, or re-distillation mechanism is part of this contract — with no copy retained, there is nothing to keep in sync.
- The contract covers only context-engineering grounding; it does not extend to the other knowledge-base disciplines.
