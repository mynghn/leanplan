# 260620-artifact-later-update — Spec

## Behavior
### B-1: update-invocable-from-any-in-flight-stage
A planner invokes one sanctioned update at any in-flight stage — requirement, spec, design, plan, or impl — naming the drift to inject, and the process engages on that feature's committed artifacts and produces a revision. It is reachable at stage boundaries, between tasks, and mid-task during impl — not only from an impl stop-the-line. Verifiable: invoking at each stage, including mid-task, engages rather than reporting no entry point.

### B-2: change-propagated-downstream
When an update changes an artifact, every downstream artifact whose content depends on the change is revised, and every touched artifact is re-validated. No downstream artifact is left citing or restating the superseded content. Verifiable: inject a change, then confirm each dependent downstream item reflects it and a content search finds no surviving reference to the prior version.

### B-3: prior-work-preserved
A revision preserves prior work rather than overwriting it. Anchor IDs (`B-`, `C-`, `D-`, `T:`) that survive the change still resolve and are not renumbered; superseded content is retained in a retired state, not silently deleted; the prior review and traceability history stays reconstructable. Verifiable: after an update that supersedes an item, its ID still resolves in a retired state and prior citations to surviving anchors still resolve.

### B-4: structural-ops-leave-nothing-stranded
A feature split or rename completes as a supported operation rather than improvised surgery. Afterward every resulting feature directory is a valid `<KEY>` form, every artifact is present and readable at its new path, and no artifact or citation points to an old or missing path. Verifiable: split or rename a feature, then confirm zero stranded or unread artifacts and zero dangling path references.

## Constraint
### C-1: no-unjustified-mutation
The process modifies committed artifacts only when the invocation carries a recorded justification for the drift (an understanding delta or equivalent drift reference). With no justification supplied, no committed artifact is mutated. Verifiable: every artifact-changing update traces to a justification record; an invocation lacking one produces no artifact change.

### C-2: committed-set-stays-consistent
A completed update leaves the feature's committed artifact set free of any reference to content it superseded and passing LeanPlan validation. No stale item survives in the committed set to be consumed downstream. Verifiable: validation passes on the feature after every update, and no committed artifact references superseded content.

### C-3: change-stays-downstream-only
An update flows downstream from the artifact it corrects: artifacts upstream of that artifact are never modified by the update. Correcting the spec leaves the requirement untouched while revising design and plan; a drift detected late but rooted in an earlier artifact is injected at that earlier artifact, not silently rippled upward. Verifiable: after an update, every artifact upstream of the corrected one is unchanged.

## Non-goals

- **Detecting or adjudicating the drift.** This contract takes the drift and its justification as input (C-1); it neither discovers drift nor judges whether the understanding truly moved. Surfacing drift is independent detection (#15); deciding it moved is understanding-sharpening (#8).
