# 260623-deferral-lane — Design

## Architecture

A new per-feature archive, `deferrals.md`, holds deliberately-deferred decisions as `Defer-N` blocks, each addressed to a later stage. Capture and drain are woven into the *existing* stage procedures (not a new skill): a stage captures off-altitude decisions as it works, and at entry drains the ones addressed to it, re-examining each non-bindingly. The block shape and the capture/drain procedure live in an on-demand companion, `references/deferral.md`; each stage doc carries only a terse hook, so the always-loaded surface stays lean. No deferral is lost: close-out reconciliation plus an advisory `validate.py` check surface an unresolved one. Separately, the adjacent understanding-shift archive `understanding.md` is renamed `deltas.md`, so the open record and the committed record are unmistakable.

```mermaid
flowchart TB
    subgraph SP [Stage procedures: Requirements / Spec / Design / Tasks]
        CAP[capture: an off-altitude decision surfaces]
        DR[drain at entry: re-examine, non-binding]
    end
    DEF["references/deferral.md companion: shape + procedure"]
    LANE[("deferrals.md: Defer-N blocks, addressed to a stage")]
    REC["close-out reconciliation + validate.py advisory check"]

    DEF -. JIT-loaded at capture and drain .-> CAP
    DEF -. .-> DR
    CAP -- append Defer-N to its owning stage --> LANE
    LANE -- JIT-loaded at the owning stage --> DR
    DR -- resolve in place, cite where it landed --> LANE
    LANE -. unresolved past its owning stage .-> REC
```

## D-1: deferrals-archive-lane

A new per-feature archive `docs/features/<KEY>/deferrals.md`, a sibling to the understanding-shift archive — **not** an extension of it. Satisfies `Spec#C-4-deferral-and-understanding-records-single-role`, `Spec#C-2-capture-off-the-review-surface`, `Spec#C-5-capture-durable-across-resets`.

- **Anchor** `Defer-<N>: <slug>`; citation `Deferrals#Defer-<N>-<slug>`. The marker is deliberately distinct from `D-<N>` (Design decision) — a near-collision would re-read a deferral as a *decision*. `validate.py` `ANCHOR_RE` / `CITATION_RE` gain a `Defer` alternative, ordered before `D` (as `Delta` already is).
- **Tier** archive, off the review surface like the understanding archive — not loaded at default review/implement time; JIT-loaded only by its owning stage's drain. This is what keeps capture off the surface (`Spec#C-2`).
- **Durable** a file survives a context reset or compaction (`Spec#C-5`) — structured note-taking's write side (`research.md`).
- Registered in `validate.py` `OPTIONAL_FILES` and the `artifact-contract.md` layering + anchors tables.
- Sibling, not blend: rationale at [design-rationale.md#D-1-deferrals-archive-lane].

## D-2: non-binding-prior-block-shape

A `Defer-N` block is shaped so it cannot read as a settled decision. Satisfies `Spec#C-3-surfaced-deferral-is-non-binding`, `Spec#B-1-deferral-captured-on-set-aside`.

- **Fields** (conclusion-first): the open *question* + why it surfaced; the *owning stage* it is addressed to; *forces* glimpsed; at most an *option seen, marked not chosen*. There is no "decision" field.
- **Resolution** a drained deferral is retired in place by appending `(resolved -> <Spec#… | Design#… | Tasks#…>)` to its heading — reusing the `(retired)` retire-in-place convention (`artifact-contract.md` → Anchors). Append-only; IDs stable.
- Low-freedom shape (validator-anchored, consistent); what goes *in* it is planner judgment (D-3).
- Why this shape defeats pinning: rationale at [design-rationale.md#D-2-non-binding-prior-block-shape].

## D-3: capture-as-affirmative-stage-hook

Capture is a terse hook added at each stage's existing disposal points — not a new skill. Satisfies `Spec#B-1-deferral-captured-on-set-aside`, `Spec#C-6-capture-is-opt-in-judgment`, `Spec#C-2-capture-off-the-review-surface`.

- **Where** the points where a stage already discards off-altitude content — Requirements "strip them", Spec "push to Design", Design "belongs in Tasks", Tasks "push to Design". Each gains an affirmative redirect: *when a genuine cross-stage decision surfaces, append a `Defer-N` addressed to its owning stage instead of discarding it* — the positive-instruction complement of the existing prohibition.
- **Not a skill** capture has no independent applicability/termination/interface; it is woven into the host stage (contrast the standalone `sharpen` / `revise` moves). Rationale at [design-rationale.md#D-3-capture-as-affirmative-stage-hook].
- **Opt-in, high freedom** *whether* to defer is planner judgment — never auto-detected, never gated (`Spec#C-6`).
- **Surface-lean** the stage doc carries only the one-line hook; the block shape + procedure live in the on-demand companion `references/deferral.md` (progressive disclosure → `Spec#C-2`).

## D-4: drain-by-re-derivation-at-stage-entry

Each stage's entry step ("Load …") is extended to drain the deferrals addressed to it. Satisfies `Spec#B-2-deferrals-surfaced-at-owning-stage`, `Spec#C-3-surfaced-deferral-is-non-binding`.

- **What** load `deferrals.md`; surface the unresolved `Defer-N` addressed to this stage; re-examine each against the stage's *full current option space*; resolve in place (D-2).
- **High freedom — the anti-pin guarantee.** The drain is open-field prose ("re-examine against current options"), never a low-freedom "apply the deferred option" script — a rigid drain *would be* the pinning. Rationale at [design-rationale.md#D-4-drain-by-re-derivation-at-stage-entry].
- **Load-bearing** the consultation is observable and reconciled (D-5), per Feature M's load-bearing-consultation pattern — a skipped drain is catchable even though the decision it prompts is free.

## D-5: no-loss-via-reconciliation-plus-advisory-check

No deferral is silently lost, surfaced along what is mechanically checkable. Satisfies `Spec#B-3-undrained-deferral-flagged-at-close-out`, `Spec#C-1-no-deferral-silently-lost`.

- **Structural (`validate.py`, advisory).** A `Defer-N` addressed to a stage whose artifact (`<stage>.md`) exists, but carrying no `(resolved -> …)` marker, raises a warning (escalates under `--strict`, mirroring the surface-budget guardrail; not a hard gate — an unresolved deferral for a not-yet-run stage is legitimate).
- **Substance (review-tier).** Close-Out Reconciliation (`implement-closeout.md`) gains the deferrals as an obligation set — the reviewer judges whether a "resolved" deferral genuinely landed where it cites. Substance is the Feature M boundary the validator cannot see.
- Why split structural / substance: rationale at [design-rationale.md#D-5-no-loss-via-reconciliation-plus-advisory-check].

## D-6: rename-understanding-archive

Rename the adjacent archive `understanding.md` → `understanding-shifts.md`, qualifying the over-broad bare "understanding" with the contract's own "shift" language ("one `Delta-N` per mid-round shift"). Satisfies `Spec#C-4-deferral-and-understanding-records-single-role` — the (B) half, the standalone over-broad-label defect.

- **Anchor + citation prefix unchanged** — the `Delta-N` unit and the `Understanding#` citation prefix both stay; only the filename and its file references move. (Bare `deltas.md` / `shifts.md` were rejected — still broad, and `deltas.md` would stutter as `Deltas#Delta`.)
- **Scope: live framework only** — `references/{sharpen,revise,design,implement,artifact-contract}.md`, `framework-design.md`, `adapters/claude/{sharpen,revise}/SKILL.md`, `scripts/validate.py` (`OPTIONAL_FILES` value), `scripts/leanplan-selftest`, `fixtures/`.
- **Exempt (quote-as-data)** the historical `docs/features/260620-*` dirs (they describe *building* `understanding.md` — a sweep would falsify history) and *this* feature's own dir (it describes the rename). The reflexive-dir sweep exemption.
- **Supersedes** `framework-design.md`'s "keep Understanding (Delta-)" from #34 — that held when no sibling made the name ambiguous; this feature introduces exactly that sibling.
- Harm assessment + why the sibling forces the rename: rationale at [design-rationale.md#D-6-rename-understanding-archive].
