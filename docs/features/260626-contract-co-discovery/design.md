# 260626-contract-co-discovery — Design

## Architecture

The Spec↔Design seam gains two discovery flows. **Forward**: an opt-in probe inside Specify. **Backward**: a contract fact surfacing in Design folds into the Spec **in-session** while the spine is warm — *additive* (author a new item) vs *contradictory* (re-author), the two kept distinct — with `/revise` reserved for the committed path.

```ascii
  Requirements ──► Spec ──► Design ──► Tasks
                      ▲   │
       FORWARD ───────┘   │   D-1  opt-in boundary-probe inside Specify:
       (D-1)              │        behaviors/constraints Requirements never named
                          │        → accept (becomes B/C) or decline.
                          │
       BACKWARD (D-2): a contract fact surfaces while choosing realization,
       folded in the WARM working set (the spine is still being authored):
                          │
         additive      → author a new B/C into the Spec, in-session
         contradictory → retire-by-note the item + author the correction, in-session
              then re-derive the downstream already authored, re-validate.
              No Delta, no /revise while warm — the two paths stay distinct (C-4).
                          │
       Once the Spec is committed / handed-off (e.g. a fact surfaced during
       implementation): the same update routes through /revise, where its
       Delta gate belongs.
```

No new concept: additive discovery is ordinary anchor authoring, and `/revise` keeps its committed-only identity.

## D-1: specify-discovery-probe
Insert an opt-in discovery step into the Specify procedure — after Lift-Constraints, before the Spec test — that probes the machine/world boundary for observable behaviors and constraints the Requirements did not name, surfacing candidates to accept into B/C or decline. Satisfies `Spec#B-1-specify-probes-for-unnamed-contract-facts`, `Spec#C-1-discovery-moves-are-opt-in`, `Spec#C-3-discovery-feeds-dialogue-not-surface-bloat`.
- Target: `references/specify.md`, a new procedure step between step 3 (Lift Constraints) and step 4 (Spec test); plus a matching Guardrails bullet and a self-check bullet.
- Shape: mirror `references/requirements.md` step 3 (Elicit / Frame / Surface) at the contract altitude — probe for failure modes, concurrency, observable error behavior, environmental couplings. `AskUserQuestion` on Claude, runtime-native prompt on Codex.
- Opt-in, never a gate: a complete contract skips it; the planner may decline or cut short (C-1). Candidates live in dialogue/research; only accepted items reach the surface, bounded by `artifact-contract.md` → Surface Budget (C-3).
- WHY: non-trivial — see `design-rationale.md#D-1-specify-discovery-probe`.

## D-2: backward-discovery-folds-in-session
During Design, a contract fact that surfaces folds into the Spec **in-session** — the warm spine is the Design stage's working set, so this is continued authoring, not a cross-artifact move. Satisfies `Spec#B-2-design-found-fact-folds-back-as-completion`, `Spec#C-4-contradictory-change-not-silently-folded`.
- `references/design.md` step 8 — replace the blanket "Spec is wrong, run revise" with a working-set branch:
  - **additive** (a new observable behavior/constraint contradicting no existing item) → author it into the Spec as a new `B`/`C` (higher anchor); the anchor + its body is the record — no `Delta`;
  - **contradictory** (invalidates an existing item) → retire-by-note the item and author the correction in-session;
  - then re-derive the downstream already authored and re-validate — the editing-loop core (`framework-design.md` §194) applied **inline, without** the `Delta` gate while warm. Don't patch downstream to mask the change.
- `/revise` is **not** invoked while warm. It remains the entry for the **committed** path — a contract fact surfaced once the Spec is committed/handed-off (e.g. during implementation) still routes through `/revise`, where its `Delta` gate belongs.
- `references/framework-design.md` §194 — reconcile: the editing-loop core is carried **inline for warm working-set edits**, and by `/revise` once committed (today's text folds every in-flight stage into `/revise`).
- No new concept: additive discovery is ordinary anchor authoring — no completion-`Delta`, no `artifact-contract.md` change, no new type.
- WHY: non-trivial — see `design-rationale.md#D-2-backward-discovery-folds-in-session`.

## D-3: solution-agnostic-statement-guard
Add a guardrail (on the D-2 in-session fold in `design.md`, mirrored on the D-1 probe in `specify.md`): a fact discovered through a realization is stated by its observable property, not the realization that revealed it, and must pass the existing implementation-swap test. Satisfies `Spec#B-3-solution-discovered-fact-stated-agnostically`, `Spec#C-2-spec-stays-invariant-under-realization-swap`.
- WHY (trivial): a direct application of Specify's existing "what a Spec is NOT" test to discovered facts — no new mechanism. Guardrail example: "consumers must tolerate reordering" (agnostic), not "tolerate the broker's partition reordering" (coupled to the realization).

## D-4: primary-source-grounding
Ground the development-model claims in `framework-design.md` with verified primary citations, attributing the framework's own synthesis honestly. Satisfies `Spec#C-5-model-claims-grounded-and-honestly-attributed`.
- Home: `framework-design.md` — its role already includes "research inputs," and the axis table already cites Jackson inline. Co-evolution → Nuseibeh (Twin Peaks) + Dorst & Cross; solution-agnostic Spec → Zave–Jackson (implementation bias) + WRSPM; complete the existing Jackson "World and the Machine" cite. Evidence is archived in `research.md`.
- The **two-kinds taxonomy** (problem-given / solution-induced) is presented as LeanPlan's own refinement, credited to the "derived requirements" lineage + Jackson's "designed domain" — explicitly NOT asserted as established RE canon.
- `philosophy.md` stays citation-light: we are not adding a co-evolution *principle* (Non-goal), so there is no principle there to ground.
- Confirm the DOIs / wording marked unverified in `research.md` before publishing.
- WHY: non-trivial — see `design-rationale.md#D-4-primary-source-grounding`.

## Coverage

`Spec#B-1`→D-1 · `Spec#B-2`→D-2 · `Spec#B-3`→D-3 · `Spec#C-1`→D-1 · `Spec#C-2`→D-3 (+ the swap-test invariant the in-session fold preserves) · `Spec#C-3`→D-1 · `Spec#C-4`→D-2 · `Spec#C-5`→D-4. All eight anchors realized by a Decision.
