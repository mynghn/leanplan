# 260626-contract-co-discovery — Spec contract under-discovered from both directions

## Problem

The Spec is the pipeline's load-bearing handoff to Design — Design roams the solution space *against* it. Today that contract arrives systematically thin, so Design explores against an impoverished set of forces. Two distinct gaps cause it, and neither is addressed:

- **Forward (problem-given facts).** Specify is purely convergent: it projects each Requirements outcome into an observable behavior and lifts the constraints already implied, with its one active force being "resist realization leakage." It has no move to *discover* contract facts that Requirements never named but that first become visible at the machine boundary. A thin Requirements re-homes into a thin Spec, and nothing in the stage widens it.
- **Backward (solution-induced facts).** Some contract facts only *exist* once a realization is on the table — they cannot precede solution exploration, so Design is where they surface. But the framework files that surfacing as a defect ("Spec is wrong, not just this Design"), records it as drift, and routes it through a repair channel. The normal, expected completing-of-the-contract-through-design is mis-framed as an error — which discourages it and treats a normal back-and-forth as an anomaly.

Who feels it: the planner authoring Spec and then Design (today, the maintainer dogfooding LeanPlan on itself). What's broken: the framework's own promise to "roam the solution space as a stage's altitude justifies" is undercut at exactly the Spec↔Design seam, because the contract Design roams against was never fully discovered.

## Outcome

The Spec contract gets fully discovered from both directions — while its defining property holds intact: an implementation swap still changes no Spec line.

User stories (the planner is the user):

- **Specify surfaces what Requirements didn't name** — running Specify prompts the planner to probe the machine/world boundary for observable behaviors and constraints absent from Requirements, and to surface candidates, so problem-given contract facts that used to slip through are caught before Design.
- **Design-found contract facts are expected, not errors** — when a realization reveals a new contract fact, the planner folds it back into Spec as the expected closing of a provisional contract, not as a recorded "Spec was wrong" drift event.
- **Discovery never couples the Spec to a solution** — a fact discovered by exploring a realization is stated in solution-agnostic form, so swapping the realization still changes no Spec line.

Success is visible when a Spec authored through the enhanced pipeline carries contract items not traceable to any single Requirements outcome (the forward discovery fired), and solution-induced contract facts reach Spec through the sanctioned closing loop rather than the drift/repair channel (the backward path is no longer mis-filed).

## Guarantee

- **Solution-agnostic Spec invariant** — the Spec must stay invariant under realization change even though some of its facts are now discovered by exploring a realization. Why it matters: the entire value of a separate Spec is durability and substitutability; discovery-via-solution must enrich the contract's *statement* without coupling it to the solution that revealed it. This is the rule that keeps the fix from collapsing Spec into Design.
- **Lean review surface** — the new discovery moves must feed the planner's dialogue and the research archive, distilling only surviving items to the surface artifact, never bloating it. Why it matters: verbose surfaces get rubber-stamped and degrade reasoning, so leanness is a standing framework property, not negotiable per feature.

## Non-goals

- **Not a framework-wide co-evolution principle.** This round addresses the Spec↔Design seam only; lifting stage co-evolution to a foundational principle across all seams is a separate, larger effort.
- **Not a solution-divergence step for Design.** Whether Design should generate and weigh multiple candidate architectures is a related but distinct gap, out of scope here.
- **No change to the artifact contract.** Anchors, IDs, traceability, and drift guards stay as-is; this round changes stage *procedure*, not artifact *shape*.
