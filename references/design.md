# LeanPlan Design Stage

This doc carries the procedure for the DESIGN stage — choosing the realization (components, stack, decisions) that satisfies a SPEC. Edge: SPEC → DESIGN.

**Stage stance.** Capture the finished-system shape in full — every realization detail a downstream task will need (field mappings, schemas, signatures, call sequences) lives here, so tasks anchor instead of paraphrase. Stop the moment it turns into *work* (ordering, rollout, INFRAREQ → TASK). The two attractors to resist are under-capture and over-reach.

Companion: `philosophy.md` (principles), `artifact-contract.md` (shape rules).

## Inputs

- `<cwd>/docs/features/<KEY>/spec.md` (required). If absent, stop and point user at `specify`.
- Current code and repo conventions (inspect before choosing architecture).
- `<cwd>/docs/features/<KEY>/research.md` (optional, for context reuse).

## Outputs

- `<cwd>/docs/features/<KEY>/design.md` — required. Architecture + per-decision blocks.
- `<cwd>/docs/features/<KEY>/design-rationale.md` — write entries for **non-trivial** decisions only. Create if needed.
- `<cwd>/docs/features/<KEY>/research.md` — append `## <topic>` blocks when SPEC→DESIGN exploration turned up durable evidence. Create if needed.

## Procedure

*Default flow, not a rigid script — re-derive it against the actual SPEC and current code. Load-bearing (don't skip or reorder): inspect current code before choosing (step 2), the coverage check (step 7), the self-check (step 9).*

1. **Load SPEC** + artifact contract + any existing `research.md`.
2. **Inspect current code** before choosing architecture. Reality is authoritative — don't pick components without seeing what already exists.
3. **Draft Architecture**: Mermaid diagram + brief caption showing chosen components, boundaries, and data / control flow. External systems appear as labeled nodes / edges.
4. **Enumerate Decisions**: for each realization choice that emerged, open a `Decision-<N>: <slug>` block.
   - One-line WHAT — the choice made.
   - WHY: one line if trivial; anchor to RATIONALE if non-trivial. Schemas, interfaces, signatures fold inline within the relevant Decision.
5. **Write RATIONALE entries** for non-trivial decisions in `design-rationale.md`. Same `Decision-<N>: <slug>` heading. **Free-form prose** — typically forces, alternatives considered, chosen path, invalidation triggers. **No prescribed inner-section schema**.
6. **Archive durable research** as `## <topic>` blocks in `research.md`. Evidence only.
7. **Coverage check** — walk each SPEC `O-<N>` and `INV-<N>`. Each must be realized by ≥ 1 of:
   - a Decision block,
   - an Architecture element,
   - **or** (for trivial realization not worth a Decision block) a directly-cited TASK Completion criterion that the downstream `plan` skill will add.
   Surface any uncovered items that *no* path realizes. Do not force-create a Decision for a trivial realization that the TASK layer handles directly.
8. **Stop** if a design choice changes the SPEC contract — update SPEC first per the artifact update loop.
9. **Self-check** before exit:
   - No work ordering / INFRAREQ / rollout text (those belong in TASK).
   - No top-level `## Schemas` or `## Interfaces` section — schemas live inside their Decisions.
   - Tech-realization specifics a downstream plan task will need (field mappings, response shapes, signatures, call sequences) are *captured here* — so the plan card can anchor in without restating. Skim each Decision: does it answer "what does the system look like in this slice?" completely?
   - Non-trivial decisions have resolvable rationale anchors in `design-rationale.md`.
   - SPEC Invariants are referenced (not re-stated).
   - Each Decision leads with its one-line WHAT (the choice), not preamble; past ~100 lines, order the highest-stakes Decisions at the edges, not buried mid-file (conclusion-first + edge-placement; `artifact-contract.md` → Prose Style).

## Guardrails

- **Chosen realization only.** DESIGN is the time-independent finished-system shape. No work ordering, PR stacking, INFRAREQ procedure, or migration sequence — those belong in TASK.
- **Tech-realization specifics live here, in full.** Field-by-field mappings, response/proto shapes, method signatures, controller/service call sequences, schemas — capture them inside the relevant `Decision-<N>` block at design time. Downstream plan tasks should be able to anchor in via `DESIGN#Decision-<N>-<slug>` *without restating* the content. If a plan task ends up paraphrasing a Decision because it lacked detail here, the missing detail is a gap in **this** doc — fill it. Symmetric guard with the corresponding rule in `plan.md`.
- **Architecture is mandatory.** Even a trivial one-component feature gets a diagram — it forces clarity about boundaries.
- **Trivial vs. non-trivial.** Trivial decisions get a one-line inline why; non-trivial decisions (a real alternative was weighed, a tradeoff accepted, an invalidation trigger worth recording) anchor to RATIONALE.
  - ✅ trivial — "store the new flag on the existing `accounts` row — the repo's standard for per-account state" (no live alternative → one line, no RATIONALE).
  - ✅ non-trivial — "read-through cache over direct-DB read for the hot lookup → `Decision-3` + RATIONALE" (alternative weighed: staleness window vs. DB load; invalidation trigger worth recording).
  - ❌ a RATIONALE entry for the trivial one — forces a form where one line suffices.
  - ❌ burying the non-trivial tradeoff as a one-liner — the road-not-taken is the highest-loss-risk WHY under eviction; it needs RATIONALE → PR body, not a clause.
- **No fake decisions.** A choice with no real alternative isn't a decision — fold its content into the diagram or reference the SPEC Invariant it satisfies.
- **No duplicate Invariants.** If SPEC says "must be non-blocking", DESIGN doesn't re-state it. Reference the SPEC anchor (e.g. `satisfies SPEC#INV-3-non-blocking-handover`).
- **RATIONALE is free-form.** No prescribed inner sections. Capture reasoning, don't fill a form.
- **RESEARCH is evidence-only.** Interpretations belong in RATIONALE.
- **Isolate breadth-heavy investigation.** When code investigation (a wide cross-module / SOTA scan) would swamp the working window, run it in a sub-agent that returns only the distilled findings — a RESEARCH entry or the conclusions — keeping the raw trail out. Guidance, not mandate — when breadth exceeds the window. (CE: context-isolation, explore-then-compact-handoff)

## Hand-off

Next edge: `/plan <KEY>` (Claude) or `plan <KEY>` (Codex).
