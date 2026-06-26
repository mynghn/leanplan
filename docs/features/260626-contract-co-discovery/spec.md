# 260626-contract-co-discovery — Spec

## Behavior

### B-1: specify-probes-for-unnamed-contract-facts
Running Specify, the planner is offered a boundary-probe — surface candidate observable behaviors and constraints that the Requirements did not name but that become visible at the machine/world boundary, for the planner to accept into the contract or decline.

### B-2: design-found-fact-folds-back-as-completion
When Design surfaces a contract fact that is *additive* to the Spec — a new observable behavior or constraint, not a contradiction of an existing one — it is added to the Spec as the expected completion of a provisional contract, not treated as a "Spec is wrong" error.

### B-3: solution-discovered-fact-stated-agnostically
When a contract fact is discovered by exploring a realization, the Spec records it by its observable property, not by the realization that revealed it — so the recorded line still passes the implementation-swap test.

## Constraint

### C-1: discovery-moves-are-opt-in
The forward probe (`B-1`) and the back-fold (`B-2`) are opt-in offers, never gates: the planner may decline or cut either short and the pipeline proceeds. Consistent with the existing draw-out's opt-in stance.

### C-2: spec-stays-invariant-under-realization-swap
Every Spec line — including one discovered through solution exploration — stays unchanged when the realization is swapped. The discovery path may enrich the contract's content but never couples a Spec line to the solution that revealed it.

### C-3: discovery-feeds-dialogue-not-surface-bloat
The discovery moves feed the planner's working dialogue and the research archive; only surviving items reach the surface artifacts, whose reviewed size stays bounded. Adding the moves must not inflate the routinely-reviewed surface.

### C-4: contradictory-change-not-silently-folded
A Design choice that *invalidates* an existing Spec item surfaces as a genuine contract change, not silently absorbed as an additive completion. The additive and contradictory paths stay distinct.

### C-5: model-claims-grounded-and-honestly-attributed
The development-model claims the core docs make are anchored to cited primary sources; any claim that is the framework's own synthesis is marked as such, not asserted as an established result.
