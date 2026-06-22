# 260621-derivable-orthogonality — DESIGN RATIONALE

## Decision-1: three-axes-world-machine-contract-realization-product-process

**Forces.** The model must let the two high-traffic seams (REQ↔SPEC, DESIGN↔TASK) be *derived*, not memorized (`SPEC#O-1`, `SPEC#O-2`), while staying minimal — no axis that doesn't earn its slot (`SPEC#INV-2`).

**Why three, not two — and not the critique's literal three.** The design went through two wrong turns before landing here, both instructive:

- *First wrong turn — collapse to two axes (World↔Machine × Product/Process), demoting Abstraction as "derivable."* This broke on a user counterexample: "persuade a person" (goal) and "give them a candy" (means) are **both World**, one abstract one specific — so WHAT/HOW varies *independently of* the World↔Machine axis; it isn't derivable from it. A 2-axis model also *over-scopes* Requirements: it would wave the candy into Requirements as "World," when Requirements is scoped (World, **Contract**) and the candy is (World, **Realization**) — a different cell.
- *The fix the counterexample forced.* Requirements = (World, Contract); the candy = (World, Realization) = a **World Design** that LeanPlan deliberately has no home for (it's non-software). So the second axis is real and load-bearing — but it is **not** "Abstraction." The honest SPEC↔DESIGN distinction is **observability**: Spec is what's visible *outside* the machine (the contract), Design is what's *inside* it (the realization). "Abstraction/WHAT-HOW" fails because it's a relative ladder — *DESIGN's what is SPEC's how* — whereas outside/inside is absolute. Hence **Contract ↔ Realization**.
- *Why not the critique's literal "Abstraction × Locus[R/S/P] × Product/Process".* Keeping locus 3-valued (R/S/P) makes Abstraction redundant (it just re-cuts the locus). Making locus **2-valued (World/Machine)** and pairing it with Contract/Realization gives three *non-redundant* axes — each the **sole** discriminator of exactly one seam. That single-axis-per-seam property is the whole point: it's what makes each boundary derivable.

**The empty cell is a feature, not a bug.** The old model's "empty (LOW, BIZ) cell" was read as a defect; it's the deliberate **World Design** scope marker (the World·Realization corner). Jackson's R/S/P are exactly the three *populated* product cells; the "missing fourth" is that empty corner — which is precisely why a software framework stops where it does.

**The pipeline is a one-axis-flip walk.** REQ→SPEC flips World→Machine; SPEC→DESIGN flips Contract→Realization; DESIGN→TASK flips Product→Process. So "distance" between any two artifacts = the axes between them: adjacent pairs differ by one axis (the blurrable, high-traffic seams L targets); non-adjacent pairs differ by 2–3 (robustly distinct, never high-traffic). This also resolved the "stage vs artifact" confusion: a **stage is the flip** (edge/activity/verb), an **artifact is the coordinate** (node/noun).

**Invalidation triggers.** A new stage that is neither a World/Machine·Contract/Realization position nor pure Process. Or a fact whose home needs a *fourth* independent axis.

**Grounding.** Jackson, *The World and the Machine*, ICSE 1995 — the world/machine dichotomy and shared phenomena; the R/S/P designations trace to its reference-model lineage (Gunter, Gunter, Jackson & Zave, *A Reference Model for Requirements and Specifications*, 2000). Osterweil, *Software Processes Are Software Too* — process as a first-class describable object. And the LeanPlan from-scratch critique, 2026-06-21.

## Decision-2: complete-vocabulary-naming-authority

**Forces.** `SPEC#O-3` wants every element name to *follow from the model*; the anti-churn bar (§8/§9, which rejected the `<KEY>` sweep at ~70 sites) and `SPEC#INV-2` bound the cost. The user elected *ideal-shape names across the board*, accepting the churn — so the job became: get the scheme right, then isolate the execution.

**The naming rule.** A skill shares its artifact's root — a verb where English has one (`specify`→Spec, `design`→Design), the bare noun where it doesn't (`requirements`→Requirements, `tasks`→Tasks). This retires the old `plan`-edge / `TASK`-artifact / `plan.md`-file triple (three names for one element) and makes `requirements`/`tasks` principled noun-skills rather than exceptions.

**Section names derive from the 2×2.** Requirements and Spec are both the **Contract** row, so each splits into an episodic and a continuous half, named by altitude: **Outcome/Guarantee** (World) and **Behavior/Constraint** (Machine). This (a) kills the old same-name "Outcome section on both artifacts" confusion the user flagged, (b) uses "Behavior" — the framework's *own* definition of a SPEC item ("externally-observable behavior") — and (c) gives Requirements' continuous biz properties (today's loose "system policies") a real home in **Guarantee**.

**Anchors: shortest unambiguous initial.** `B-` (Behavior), `C-` (Constraint), `D-` (Decision), `T:` (Task — colon because Task IDs are track-keyed `A1`/`P1`, not sequence numbers). `Delta-` stays spelled: `D-` is taken by Decision, and `Delta-` is grep-distinct from `D-` anyway, and it's the rarely-cited archive item. The artifact namespace in every citation (`DESIGN#D-1`) already implies the type, so short prefixes cost no legibility.

**Why `plan` is rejected** despite being the most intuitive single word: it's the *activity*, not an artifact. Planning is *what LeanPlan does* — the entire Requirements→Spec→Design→Tasks spine *is* "the plan." Naming one node "Plan" puts the activity's name (an edge concept) on a node, the exact node/edge conflation Decision-1 cleans up; "LeanPlan" already spent "plan" at the top level. It also collides with agent **plan-mode** (an external, unfixable clash, since LeanPlan runs inside those agents). `Tasks` names stage 4 by its content, and its plural also fixes the current stage(`TASK`)/item(`Task:`) clash.

**Execution split (triage → separate effort).** Occurrence counts (repo minus L's dir): SPEC 448, DESIGN 253, TASK 111/34 files, INV/Invariant 265/42 files, plan 164, O-/INV- anchors ~360. *Every* core name is 86–448 — far past the `<KEY>` bar. The full ideal scheme is a **~1,000-edit framework-wide sweep** (artifacts, edges, items, anchors, `validate.py` regex, fixtures, adapters, every shipped feature). That dwarfs L's model change and trips L's own "split the sweep if oversized" provision — so L ships the **decisions** (this scheme, written into `framework-design.md` §8 as the authority) and the sweep is a **separate, dedicated effort** with its own atomic re-validation. L's own artifacts stay in today's vocab until then; nothing is half-renamed.

**Invalidation trigger.** If the separate sweep proves intractable to do atomically, reconsider staging it per-artifact-family (anchors, then files, then prose) rather than all at once.
