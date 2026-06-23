# LeanPlan Design Stage

This doc carries the procedure for the Design stage — choosing the realization (components, stack, decisions) that satisfies a Spec. Edge: Spec → Design.

**Stage stance.** Capture the finished-system shape in full — every realization detail a downstream task will need (field mappings, schemas, signatures, call sequences) lives here, so tasks anchor instead of paraphrase. Stop the moment it turns into *work* (ordering, rollout, cross-team request filing → Tasks). The two attractors to resist are under-capture and over-reach.

Companion: `philosophy.md` (principles), `artifact-contract.md` (shape rules).

Mid-stage, if a disturbance shifts the understanding, `leanplan-sharpen` is the sanctioned, opt-in response — an off-pipeline reflect-and-re-derive move that reads your artifacts but never edits them — instead of ignoring it or hand-rolling a fix.

## Inputs

- `<cwd>/docs/features/<KEY>/spec.md` (required). If absent, stop and point user at `specify`.
- Current code and repo conventions (inspect before choosing architecture).
- `<cwd>/docs/features/<KEY>/research.md` (optional, for context reuse).

## Outputs

- `<cwd>/docs/features/<KEY>/design.md` — required. Architecture + per-decision blocks.
- `<cwd>/docs/features/<KEY>/design-rationale.md` — write entries for **non-trivial** decisions only. Create if needed.
- `<cwd>/docs/features/<KEY>/research.md` — append `## <topic>` blocks when Spec→Design exploration turned up durable evidence. Create if needed.

## Procedure

*Default flow, not a rigid script — re-derive it against the actual Spec and current code. Load-bearing (don't skip or reorder): inspect current code before choosing (step 2), the coverage check (step 7), the self-check (step 9).*

1. **Load Spec** + artifact contract + any existing `research.md`. Then **drain deferrals** (load-bearing): if `deferrals.md` exists, surface each unresolved `Defer-<N>` addressed to this stage, `Design`, and re-examine it against the current option space — non-binding, re-derive not replay; resolve in place (refer to `references/deferral.md` for detailed procedure guide).
2. **Inspect current code** before choosing architecture. Reality is authoritative — don't pick components without seeing what already exists.
3. **Draft Architecture**: one or more visual blocks (Mermaid or fenced ASCII art) + brief caption showing chosen components, boundaries, and data / control flow. External systems appear as labeled nodes / edges. Prefer adding a visual companion anywhere a relationship, sequence, state, or mapping would otherwise be described in words; diagrams act as structured prompt material, so clear labels and boundaries matter more than the notation.
4. **Enumerate Decisions**: for each realization choice that emerged, open a `D-<N>: <slug>` block.
   - One-line WHAT — the choice made.
   - WHY: one line if trivial; anchor to Rationale if non-trivial. Schemas, interfaces, signatures fold inline within the relevant Decision.
5. **Write Rationale entries** for non-trivial decisions in `design-rationale.md`. Same `D-<N>: <slug>` heading. **Free-form prose** — typically forces, alternatives considered, chosen path, invalidation triggers. **No prescribed inner-section schema**.
6. **Archive durable research** as `## <topic>` blocks in `research.md`. Evidence only.
7. **Coverage check** — walk each Spec `B-<N>` and `C-<N>`. Each must be realized by ≥ 1 of:
   - a Decision block,
   - an Architecture element,
   - **or** (for trivial realization not worth a Decision block) a directly-cited Tasks Completion criterion that the downstream `plan` skill will add.
   Surface any uncovered items that *no* path realizes. Do not force-create a Decision for a trivial realization that the Tasks layer handles directly.
8. **Stop** if a design choice changes the Spec contract — Spec is wrong, not just this Design. Record the drift as a `Delta` in `understanding-shifts.md`, then run `leanplan-revise <KEY>` — it injects the fix at Spec and propagates downstream-only (`revise.md`). Don't hand-edit Spec inline.
9. **Self-check** before exit:
   - No work ordering, cross-team request filing, or rollout text (those belong in Tasks).
   - No top-level `## Schemas` or `## Interfaces` section — schemas live inside their Decisions.
   - Tech-realization specifics a downstream plan task will need (field mappings, response shapes, signatures, call sequences) are *captured here* — so the plan card can anchor in without restating. Skim each Decision: does it answer "what does the system look like in this slice?" completely?
   - Non-trivial decisions have resolvable rationale anchors in `design-rationale.md`.
   - Upstream Spec `B` / `C` are referenced, not re-stated; the Architecture caption doesn't restate a `Decision`.
   - Each Decision leads with its one-line WHAT (the choice), not preamble; past ~100 lines, order the highest-stakes Decisions at the edges, not buried mid-file (conclusion-first + edge-placement; `artifact-contract.md` → Prose Style).

## Guardrails

- **Chosen realization only.** Design is the finished-system shape, not the work that builds it. No work ordering, PR stacking, cross-team request procedure, or migration sequence — those belong in Tasks.
- **Park a genuine deferral; don't discard it.** A real cross-stage decision that surfaces here goes into `deferrals.md` as a `Defer-<N>` addressed to its owning stage, rather than being discarded — opt-in planner judgment; procedure in `references/deferral.md`.
- **Tech-realization specifics live here, in full.** Field-by-field mappings, response/proto shapes, method signatures, controller/service call sequences, schemas — capture them inside the relevant `D-<N>` block at design time. Downstream plan tasks should be able to anchor in via `Design#D-<N>-<slug>` *without restating* the content. If a plan task ends up paraphrasing a Decision because it lacked detail here, the missing detail is a gap in **this** doc — fill it. Symmetric guard with the corresponding rule in `tasks.md`.
- **Architecture visual material is mandatory.** Even a trivial one-component feature gets at least one diagram or ASCII visual — it forces clarity about boundaries. Use Mermaid when graph semantics carry the shape cleanly; use fenced ASCII art when layout, alignment, or mixed annotations express the idea better. More than one visual is fine when each earns its place.
- **Trivial vs. non-trivial.** Trivial decisions get a one-line inline why; non-trivial decisions (a real alternative was weighed, a tradeoff accepted, an invalidation trigger worth recording) anchor to Rationale.
  - ✅ trivial — "store the new flag on the existing `accounts` row — the repo's standard for per-account state" (no live alternative → one line, no Rationale).
  - ✅ non-trivial — "read-through cache over direct-DB read for the hot lookup → `D-3` + Rationale" (alternative weighed: staleness window vs. DB load; invalidation trigger worth recording).
  - ❌ a Rationale entry for the trivial one — forces a form where one line suffices.
  - ❌ burying the non-trivial tradeoff as a one-liner — the road-not-taken is the highest-loss-risk WHY under eviction; it needs Rationale → PR body, not a clause.
- **No fake decisions.** A choice with no real alternative isn't a decision — fold its content into the diagram or reference the Spec Constraint it satisfies.
- **Conclusion-first Decision body.** Line 1 is the choice itself; parallel facets (schema, rejected alternatives, invalidation cue) follow as a list below it — the body is graspable from its lead line alone (`artifact-contract.md` → Prose Style).
  - ✅ choice first: *"Store the session token as a salted hash, not plaintext — satisfies `Spec#C-2-tokens-never-stored-in-clear`; schema and the rejected encrypt-at-rest alternative follow as list items."*
  - ❌ choice buried: *"Because we already hash passwords and a second reversible secret widens the blast radius while `Spec#C-2-tokens-never-stored-in-clear` must still hold, we store the token as a salted hash…"* — the choice lands only after three clauses of preamble.
- **One prose home — cite, don't restate.** Design references an upstream Spec `B` / `C` by anchor (e.g. `satisfies Spec#C-3-non-blocking-handover`) instead of re-stating it. Within Design, the Architecture caption owns boundaries and flow only; it doesn't restate a `Decision`, and the `Decision` blocks own realization claims (`artifact-contract.md` → One Prose Home Per Fact).
- **Rationale is free-form.** No prescribed inner sections. Capture reasoning, don't fill a form.
- **Research is evidence-only.** Interpretations belong in Rationale.
- **Isolate breadth-heavy investigation.** When code investigation (a wide cross-module / SOTA scan) would swamp the working window, run it in a sub-agent that returns only the distilled findings — a Research entry or the conclusions — keeping the raw trail out. Guidance, not mandate — when breadth exceeds the window. (context-engineering: context-isolation, explore-then-compact-handoff)

## Hand-off

Next edge: `leanplan-tasks <KEY>`.
