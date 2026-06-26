# 260626-live-ce-grounding — Understanding Shifts

## Delta-1: referential-coupling-survives-unvendoring

The understanding now: dropping the vendored cards eliminates only the **content**-drift surface. LeanPlan still couples to Metacognition's evolution through its **reference** layer — the slugs its hooks and map name must still resolve in the live source. So LeanPlan's one standing obligation toward upstream evolution is **referential-link integrity** (one-way Metacognition→LeanPlan, advisory): validate that each grounded slug still resolves and that the resolution mechanism is reachable. A concept's **semantic** correctness or health is Metacognition's repair responsibility, never LeanPlan's. The buildable reference-link self-inspect skill is a named **fast-follow**, not built in this feature.

Kills the prior assumption: that the live dependency makes grounding "fresh by construction" with nothing left to reconcile — i.e. that issue #27's sync need fully dissolves. It dissolves for *content*, not for *references*.

Why (disturbance + verification): the planner flagged residual Metacognition→LeanPlan coupling; an empirical check confirmed LeanPlan grounds in exactly the 15 current INDEX slugs — no dangling, none degraded — but **1:1 by recency, not process**, which is issue #27's own liability reborn one layer up (reference instead of content). The check itself (grounded-slugs ⊆ live INDEX) is the fast-follow gate's whole logic, run by hand.

Scope-of-impact: Requirements (Outcome user story + a new Guarantee + narrowed Non-goals — the principle's home, at intent altitude since the check is fast-follow) and a downstream forward note on `Design#D-3-frame-as-harness-supplied-grounding`. Spec is unaffected — no `B`/`C` item claimed total drift-freedom; the unvendoring contract stands.
