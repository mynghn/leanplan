# 260621-jit-load-guarantee — Spec

Observable surface: a delivered unit of LeanPlan work that cites anchors, read under the framework's review path. To *consult* a citation is to open the cited anchor's content; this contract makes that act observable for the load-bearing class only. The generic words *check* and *review* name the observation channel, not a specific tool.

## Behavior
### B-1: load-bearing-consultation-observable
When delivered work acts on a load-bearing citation — a Spec `B`/`C` it realizes or a Design `Decision` it builds — the work observably evidences that the cited content was consulted, not merely that its anchor was named. Inspection distinguishes the two cases: the consulted case carries a consultation signal; acting on the slug alone does not. *(One-shot test: deliver a task that genuinely opened its cited Decision → the consultation signal is present and reads as consulted; deliver one that only echoed the slug → no signal.)*

### B-2: skipped-needed-load-surfaceable
When work acted on a load-bearing citation without consulting its content, that skip is surfaceable after the fact. Reading only the delivered artifacts, a reviewer or a check can flag it rather than letting it pass as conforming. A right-looking anchor with no consultation signal is catchable, not silently accepted. *(One-shot test: deliver a task that cites a load-bearing anchor it never opened → the review path surfaces the skip instead of green-lighting it.)*

## Constraint
### C-1: archive-citation-never-force-loaded
The contract never fires on a load-on-challenge (archive-tier) citation. Acting on a Rationale or Research anchor without opening it is always conforming: no consultation signal is required for it, and its absence is never a finding. The observable requirement exists for the surface / load-bearing class and for no other — the surface/archive layer is the scope boundary, reused, not re-invented.

### C-2: surface-no-less-lean
The review surface (Requirements, Spec, Design, Tasks) stays at least as lean as before this contract. Any consultation signal the contract introduces adds no standing prose a reviewer must read to grasp the feature, restates no archived or anchored content back onto the surface, and pushes no surface artifact over its existing Surface Budget.

## Non-goals
- **The form of the consultation signal is unspecified here.** Whether consultation is evidenced by a receipt, a restatement at the point of use, a check token, or a recorded trace is a Design choice. This contract requires only that consultation be observable (B-1) and a skip surfaceable (B-2).
- **Not a correctness guarantee.** The contract is that the needed load *occurs* and a skip is *catchable* — not that consulting the anchor produces a correct implementation. A consulted-but-still-wrong result is outside this contract.
