# 260621-derivable-orthogonality — Spec

## Behavior
### B-1: req-spec-placement-derivable-from-model
The REQ↔Spec seam (intent vs. observable contract) is decided by the model, not by a separately memorized discriminator. When a fact is authored on the wrong side, a reader reasoning from the model's stated axes alone flags the misplacement and names the correct home; and the model text presents this seam as a consequence of an axis, not as a standalone rule. The one-canonical-home enforcement shipped in `260620-lean-review-surfaces` is inherited, not re-specified — this contracts only that the *placement decision itself* is model-derivable. One-shot test: plant an observable, testable predicate in Requirements (or a bare intent in Spec); a reader applying only the model places it correctly and cites the axis, invoking no side-rule.

### B-2: design-task-placement-derivable-from-model
The Design↔Tasks seam (the finished system vs. the work that builds it) is decided by the model, not by a memorized discriminator. When a fact is authored on the wrong side, a reader reasoning from the model's stated axes alone flags the misplacement and names the correct home; and the model presents this seam as a consequence of an axis, not as the bolted-on time note that splits the two today. One-shot test: plant a finished-system shape in a Tasks card (or a work-ordering step in Design); a reader applying only the model flags it and names the correct home, citing the axis.

### B-3: model-vocabulary-coherent-and-derivable
The model's own element names follow from the model: the name a reader would predict from the axes for an element — an axis label, an artifact, an edge/skill, a model-reframed section — is the name in use, and one element resolves to one coherent naming scheme rather than several names bridged by latent inference (as today's `plan` edge → `TASK` artifact → `plan.md` file must be). Scope is the naming *decisions* the redesign justifies (the settled scheme), not the codebase-wide propagation sweep (Non-goals). One-shot test: for each element in the settled scheme, its name is predictable from the axes (a stated naming rule derives it) and denotes exactly one element — no element wears several names, no name spans several elements.

### B-4: recall-and-dedup-compose
Edge-placement-for-recall and state-each-fact-once read as one non-contradictory instruction: an author following both at once takes a single action instead of choosing between them. (Minor rider; not a new axis.) One-shot test: read the two rules together — they yield one instruction with no residual contradiction for the author to resolve (re-anchoring at the edge places an anchor pointer, never restated prose).

## Constraint
### C-1: identity-and-traceability-preserved
Across the model rework and any settled renames, every artifact keeps its stage role and content, and the framework stays structurally valid: all anchors resolve, every citation and the Spec-B/C↔Tasks traceability hold, and no information is lost — only the model's self-description, the crispness of its high-traffic distinctions, and its element labels change. Verified by the structural validator over the framework's own artifacts and fixtures, plus diff inspection for content preservation.

### C-2: model-surface-not-inflated
The rework adds no review surface a reviewer experiences as bloat. The reworked model (the coordinate-model section of `framework-design.md` and the touched guards in `artifact-contract.md`) stays within its prose budget, and the net change is clarification — crisper distinctions and coherent names — not expansion. A new axis in the model is admissible only insofar as it makes a load-bearing boundary self-evident; it must not read as added surface. The absolute-budget half is backstopped by the surface-budget guard; the no-inflation *delta* (the guard sees size, not change) is verified by diff inspection.

## Non-goals
- The specific axis set and labels, and the specific renames, that realize these outcomes are Design's concern. This contract holds for any model rework that makes the two named seams derivable and the names coherent — not for one chosen axis scheme.
- Mechanically propagating the settled scheme across every citation, validator regex, template, fixture, and shipped feature is a **separate dedicated effort**, not within this feature's plan (the full rename is ~1,000 sites — larger than this feature itself). Its end state is covered by B-3 and C-1, not contracted here as a separate observable.
- The runtime guarantee that cited content is actually loaded before an agent acts on it — sibling feature `jit-load-guarantee`.
- Re-doing `260620-lean-review-surfaces`' legibility (BLUF) and de-duplication enforcement — this contract sits one layer below those guards (the model that makes them derivable), not on top.
- Re-deriving what any artifact contains or its stage role; only the model's self-description, high-traffic distinction-crispness, and element labels are in scope.
