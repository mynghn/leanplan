# 260626-contract-co-discovery — Design Rationale

## D-1: specify-discovery-probe

Forces: current Specify is purely convergent — it projects each Requirements outcome, lifts the implied constraints, and resists realization leakage, with no generative move. So a thin Requirements re-homes into a thin Spec. The machine-contract altitude is exactly where a class of contract facts first becomes visible (failure modes, concurrency, observable error behavior, environmental couplings) that the World-altitude Requirements cannot see.

Alternatives weighed:
- **Make discovery a gate** — rejected: contradicts the framework's opt-in stance and the formed-arrival skip in Requirements; a complete contract should pass through untaxed.
- **Put discovery only in Requirements** — rejected: machine-boundary facts don't exist at the World altitude, so Requirements' Frame step can't reach them.
- **A new dedicated discovery stage** — rejected: surface bloat (philosophy P3) and a redundant edge; the probe belongs inside the stage that owns the contract.

Chosen: an opt-in generative probe inside Specify at the contract altitude, feeding dialogue/research with only accepted items reaching the surface.

Discovery mechanism (refined at implementation — `UnderstandingShifts#Delta-1-probe-discovers-by-investigation-not-elicitation`): the probe discovers through three channels, not the single structured-question move first drafted. The first draft named `AskUserQuestion` and mirrored Requirements' Elicit/Frame/Surface — but that copies the (World, Contract) altitude, where the human is the *sole* oracle of an *optative* problem, onto the (Machine, Contract) altitude, where the targets are mostly *indicative* "given properties" (Jackson) of code, neighbors, and environment: investigated, not elicited. The three: **inspect the as-is** (convergent grounding — what the boundary already is), **research the outer world** (the *generative reach* — as-is inspection alone re-derives the status quo; this is the feature's own co-evolution/Twin Peaks grounding applied beyond the repo, where the as-is is your own prior solution and the outer world is the industry's), and **ask the planner** for the human-held intent + accept/decline. RE corroboration: quality/boundary requirements are discovered by analysis, not stated in interviews (tacit knowledge — Goguen & Linde 1993; NFRs operationalized, not stated — Glinz 2007); evidence in `research.md` → Discovery mechanism. Named techniques (FMEA, HAZOP, exception analysis, …) stay in the archive — `specify.md` prizes a small review surface. Reuses Specify's existing research machinery (`research.md` as a source, the *Isolate breadth-heavy research* sub-agent guardrail); no new surface.

Altitude boundary (so the probe's investigation does not overlap Design's): both stages investigate the same reality, but Specify extracts the *observable contract* (alternative-free, true under any realization) while Design chooses the *realization* (among alternatives) — same act, different output altitude, the Contract↔Realization seam. The line is Specify's *existing* filter: the Spec test + *No false optionality* (a found fact with no realization alternative is a contract fact; a choice among alternatives is Design's). The probe inherits that filter rather than adding a boundary; research is continuous across the `specify`/`design` edges with one shared `research.md`, each stage extracting its own layer — so no duplicated investigation either.

Invalidation trigger: if dogfooding shows the probe routinely fires empty because Requirements is already complete, downgrade it from a procedure step to a one-line guardrail prompt.

## D-2: backward-discovery-folds-in-session

Forces: a contract fact surfacing during Design must reach the Spec, but Design is a *planning* stage that runs in the warm spine session (P8) — the Spec is still in the planner's working set, malleable, uncommitted. The framework's bug was treating this as an after-commit event: `design.md` step 8 said "Spec is wrong, run `revise`," importing `revise`'s committed-artifact + `Delta` machinery into a warm edit. `revise` is by definition the committed-artifact move (`revise.md`: "committed artifacts"; "no Delta → zero mutation"); using it here re-introduces the exact ceremony this round removes.

Deciding principle: a *move* (`/revise`, `/rethink`) is for touching an artifact *outside* the current working set; inline editing is for what's in it. The warm Spec is in Design's working set, so updating it is continued authoring — not a cross-artifact move.

Alternatives weighed:
- **Invoke `/revise` from the design skill** — rejected: drags `revise`'s committed/`Delta` framing onto a warm edit (or forces a no-`Delta` "warm mode" that blurs `revise`'s identity), and adds a context-switch to a two-line in-session edit.
- **A completion-kind `Delta`** (an earlier draft of this decision) — rejected: an additive fact kills no prior assumption, so it is not an understanding shift at all; it is ordinary anchor authoring, and the new anchor + its body is the record. The `Delta` ledger is for corrections, where something is killed and the surviving artifacts alone don't show what moved.
- **A new first-class "append"/"extension" type** — rejected: additive discovery is already covered by the most first-class thing there is, the anchor item; no new concept earns its surface.

Chosen: during Design, fold the fact into the Spec **inline** per the editing-loop core (walk to the Spec → author the new `B`/`C` for an additive fact, or retire-by-note + correct for a contradictory one → re-derive downstream → re-validate), with **no `Delta`** while warm. `/revise` stays the entry for the committed path. `framework-design.md` §194 is reconciled: its editing-loop core is inline for warm working-set edits, and `/revise` once committed.

Why no `Delta`/`revise` while warm is coherence, not just less ceremony: the `understanding-shifts.md` ledger records shifts *relative to a baseline*. A warm edit has no baseline — nothing to have moved from — so recording it as a `Delta` would assert a shift that never happened and pollute the ledger. The gate's absence is correctness, not a speed hack. (Commit-state is the proxy; the real line is the plan→implement handoff that creates a relied-upon baseline — not any checkpoint git commit.)

Dogfooding: this decision was itself reached by an in-session warm correction — D-2/C-4/Spec were re-derived inline, no `/revise` — and it began as an additive realization fact surfaced while authoring the Design. Both mechanisms the feature legitimizes, demonstrated on the feature.

Scope boundary (surfaced, not silently included): the *committed*-additive case — an additive fact surfaced during implementation, which still routes through `/revise` and would currently take a `Delta` — is left to a later refinement (teach `/revise` to accept a no-`Delta` additive add). This round fixes the warm path, the common case; `revise.md` and `artifact-contract.md` are untouched.

Invalidation trigger: if inline warm edits erode the editing-loop discipline in practice (downstream left un-re-derived, IDs renumbered), promote the discipline from a `design.md` reminder to a shared rule that both the inline path and `/revise` cite.

## D-4: primary-source-grounding

Grounding verdict (full evidence in `research.md`): co-evolution and solution-agnostic-Spec ground STRONGLY in canonical primary sources (Nuseibeh's Twin Peaks + Dorst & Cross; Zave–Jackson's implementation bias + the WRSPM reference model). The two-kinds taxonomy grounds only PARTIALLY — it is LeanPlan's synthesis, not an established RE distinction; its closest homes are "derived requirements" (≈ solution-induced) and Jackson's "designed domain."

Chosen path: cite the strong claims to their canonical sources in `framework-design.md` (the rationale / research-inputs archive, matching its existing inline-citation style); present the taxonomy as LeanPlan's own refinement with explicit credit to its lineage, never asserting it as canon. Honesty is the load-bearing discipline here (`Spec#C-5`) — over-claiming a citation would corrode exactly the robustness this round seeks.

Why `framework-design.md`, not `philosophy.md`: philosophy.md carries behavior-shaping principles, and we are deliberately not adding a co-evolution principle (a Non-goal), so there is no principle there to ground. framework-design.md already hosts the coordinate-model citations and research inputs.

Invalidation trigger: confirm the unverified DOIs (Dorst & Cross; WRSPM) and the *Problem Frames* "designed domain" wording before publishing; if any fails to verify, drop or replace that specific citation rather than weakening the honesty standard.
