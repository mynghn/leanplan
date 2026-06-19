# LeanPlan Feedback — Feature Backlog (parked)

Source: 4-item feedback distill, 2026-06-20. Delivering **sequentially, A first**.
Full grounding: 4-thread workflow `wf_4101899c-5af` (thread findings cited inline below; regenerable).

The 4 feedbacks distilled into **three features**. A is being authored now; B and C are
parked here with their forged framing so we reload — not re-derive — when we pick them up.

> **Base note (in-flight drift, 2026-06-20).** During this session `main` advanced — PR #6
> (`feat/ce-pe-adversarial-hardening`) merged, and **Surface Budget hardened**: prose-line
> caps 90/110/160/220 (diagrams/code/blanks excluded), now enforced in `validate.py`.
> Re-checked A against the new base: Problem/Outcome intact; **de-dup thread untouched**;
> leanness now partly mechanized → A *builds on* the budget enforcement (size caps ≠ BLUF
> structure). New base for this work = `origin/main` @ `8be1e86`.
> *(Meta: this is feature C's in-flight drift, happening live — confirms C is a real need.)*

---

## A — Lean review surfaces  ·  `[ACTIVE — requirement written → next: /specify]`

Threads **2 + 3**. BLUF readability + cross-artifact de-dup on the four rendered surfaces.
Acts on the *rendered* artifacts; ready to `/specify` soonest.

- **Readability (2):** principle already exists (`artifact-contract.md:108-125` Prose Style + Surface Budget; `~/AGENTS.md` `<document_brevity>`) — DESIGN/PLAN just don't obey it because their core fields are free-prose (DESIGN Decision body, PLAN Task Goal) and collapse into blobs/run-ons. Fix = conform, not invent.
- **Orthogonality (3):** blur is localized to two seams — REQUIREMENT "System policies" ≡ SPEC "Invariants" (same facts reworded; real example: portability/freshness/leanness → INV-1/2/3), and TASK Completion citations ≡ Forward-coverage table. De-dup guard only covers DESIGN↔SPEC today.
- Allocated at `docs/features/260620-lean-review-surfaces/`; `requirement.md` written + validated (2026-06-20).

---

## B — Problem-understanding before commit  ·  `[PARKED — framing settled]`

Thread **4, reframed**. The real prerequisite for a good requirement is the **user understanding their own problem**. B provides the optional, interactive space to deepen that understanding before the requirement is committed; whole-round benefit follows from it (it is not the goal).

- **Problem:** a good requirement — and everything downstream — rests on the user actually understanding their problem, but the front of a round gives no reliable space for it. Arrive with a vague thought → risk a guessed, thin requirement (no draw-out). Want to explore unclear details upfront — weigh candidate tech solutions and their real competences, do problem-research, surface hard TODOs (DML/DDL, cross-team infra asks) — and there's no welcomed place. Problem-understanding is left to chance.
- **Outcome direction:** LeanPlan reliably offers an interactive problem-understanding space at the front of a round that:
  - **Draws the user out when they arrive sparse** — reliable engagement, not guessing (the *deterministic* part).
  - **Welcomes free-ranging exploration when the user wants depth** — unclear problem details, candidate tech + competences, upfront research, hard downstream TODOs — without forcing it.
  - Lets the deepened understanding (and any context surfaced) **carry forward** to SPEC/DESIGN/PLAN, so exploration done once pays off downstream.
  - **Primary signal:** the user understands the problem well enough that `/requirement` distill succeeds; downstream benefit is the welcome consequence.
- **Decided scope / constraints:**
  - **Opt-in, never mandatory** — offered and done well when invoked; no forced heavy pre-work (leanness).
  - **Centered on the requirement's success** (problem-understanding first); carry-forward is secondary, not a mandate to pre-build downstream artifacts.
  - **Exploration may range across round concerns** (tech candidates, research, hard TODOs) but must **not pollute the biz-only requirement** — early tech/plan concerns land in their proper stage/archive later, not in `requirement.md`.
  - **"Deterministic" = reliably *create the space and draw out*,** not force exhaustive pre-work. Resolves the optional-vs-deterministic tension.
- **Open:**
  - Does carried-forward context get *captured* durably (a context note / `research.md`) or live in the warm session + the sharper requirement? (mechanism = design; "carries forward" = the biz promise)
  - Extends existing `research.md` + P8 warm-session continuity, or genuinely new?
- **Grounding:** thread-4 — whole interactive contract is one soft line (`requirement.md:28`), no trigger, no sparse-input branch; "interactive" absent from `philosophy.md`; `specify.md` has zero elicitation. Tools exist (`AskUserQuestion` granted); the *obligation* is absent.

---

## C — Artifact later-update process  ·  `[PARKED — framing settled]`

Thread **1**. How committed artifacts evolve *after* first commit, *while the feature is in flight*.

- **Problem:** mid-build, reality shifts (late stakeholder requirement, changed external contract, a task that exposes a wrong assumption). The only revision machinery (`impl.md:38-61` Artifact Update Loop) fires solely from impl stop-the-line triggers; a change before/between tasks has no entry point. The validator is stateless (no staleness notion). Differential volatility is never acknowledged.
- **Outcome direction:** a defined post-commit, pre-ship revision process — clear **entry point**; **reflect drift into downstream** so nothing stale survives into implementation; **preserve prior work** (stable IDs / retire-notes / hand edits); **effort proportional to volatility**.
- **Decided scope:**
  - **IN:** in-flight drift reflection — else you build stale software.
  - **OUT:** post-deploy drift tracking — P6 stands (docs discardable, code is truth).
  - **Volatility:** acknowledged-and-proportionate (gradient TASK > DESIGN > SPEC > REQUIREMENT) as an outcome promise; the *mechanism* is a design decision.
- **Grounding:** thread-1 — in-place revision contract (stable IDs, retire-by-note) is SPEC-only (`specify.md:46`) and ungeneralized; re-derive (`requirement.md:83`) vs re-evaluate-in-place (`impl.md:59`) conflict is unresolved; P6/P8 cover the lifecycle *end*, not its churning *middle*.

---

### Cross-cutting guards (all three)

- **Functional identity preserved** — anchors, traceability, stage ownership stay intact; only legibility / authoring discipline / revision support change.
- **Leanness is non-negotiable** — every change must reduce reviewer + agent reading load. Dogfood the feedback: these framework docs obey the same rules.
