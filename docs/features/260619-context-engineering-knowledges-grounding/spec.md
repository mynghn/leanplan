# 260619-context-engineering-knowledges-grounding — Spec

## Behavior
### B-1: load-bearing-rule-names-its-principle
Each load-bearing framework rule identifies, by recognized name, the context-engineering principle it implements. A reader inspecting a rule can name that principle from the rule's own statement, without consulting anything else.

### B-2: principle-resolves-to-grounded-definition
Following a named principle reaches a grounding record that both defines the principle in the framework's own words and cites the external source(s) it derives from. The chain rule → principle → definition + source is traversable end to end.

### B-3: framework-conforms-to-its-own-advice
The framework's own authoring and loading behavior conforms to the principles it teaches: no stage's guidance contradicts a principle the framework espouses, and each taught practice that bears on the framework's own operation is reflected in that stage's guidance. (Which specific conformance changes achieve this is Design's concern.)

## Constraint
### C-1: portable-self-contained
In any installed copy, with no external knowledge base present, every grounding reference — rule → principle → definition → related concept — resolves locally. Shipped LeanPlan requires nothing beyond what it ships, either to be used or to have its grounding read.

### C-2: provenance-is-dated-and-visible
Every grounding record carries a visible record of its source(s) and the date it was last reconciled against them, so staleness is detectable by inspection rather than hidden.

### C-3: grounding-stays-off-the-hot-path
The surface loaded by default to author or review a feature is not enlarged by grounding. Grounding depth is reachable on demand, not carried in the default working set.

## Non-goals
- New validator rules or other enforcement tooling are not required by this contract — conformance is verifiable by inspection; whether any check is automated is a Design choice.
- A use-time dependency on any external knowledge base is excluded outright (see `C-1`), including an optional one.
- Re-deriving or restating the existing per-stage artifact contracts is out of scope; this contract sits alongside them.
