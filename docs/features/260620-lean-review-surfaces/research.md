# 260620-lean-review-surfaces — Research

Evidence from a cold audit of the LeanPlan references + the worked `260619-context-engineering-knowledges-grounding` feature (4-thread grounding workflow). Evidence only; interpretation lives in `design-rationale.md`.

## Duplication found across the artifact chain

- **Requirements System-policies ≡ Spec Invariants.** In the 260619 example, the three System-policies (portability / freshness / leanness) map 1:1 to `spec.md` C-1 / C-2 / C-3 — the same facts reworded at both homes.
- **De-dup guard is asymmetric.** `design.md` carries "No duplicate Invariants" (Design→Spec) only; `artifact-contract.md` Drift Guards have no equivalent for REQ→Spec or Tasks→Spec.
- **Root in the contract.** `requirements.md` defines the System-policies sub-group using Spec vocabulary ("cross-cutting invariants (price parity, state-machine rules, regional constraints)") — collapsing the role boundary at definition time.
- **Tasks Completion citations ≡ Forward-coverage table.** In 260619 `tasks.md`, per-task `Completion` already cites its Spec anchor; a tail forward-coverage table re-states the inverse Spec-item→task map — the same traceability fact twice.
- **Design Architecture caption ≡ D-1.** In 260619 `design.md`, the Architecture caption restates D-1's layering and its `C-1` satisfaction claim.

## Prose-shaped fields read worst (legibility ranking REQ ~ Spec > Tasks > Design)

- **Design `Decision` body** ("one-line WHAT then prose WHY") collapses into a single dense paragraph — 260619 `design.md` D-7 is a ~120-word unbroken block fusing principle, mechanism, caveat, and anchors.
- **Tasks `Goal`** (process-framed statement + inline anchors) collapses into a run-on — 260619 `tasks.md` A1 Goal fuses outcome, method, and two anchors in one clause.
- **Requirements / Spec read better** because their templates are list-shaped by construction: user-story bullets; atomic `### B-<N>` / `### C-<N>` items whose slug carries the BLUF.

## Existing legibility machinery (principle present; conformance is the gap)

- `artifact-contract.md` **Prose Style** (conclusion-first / lists over dense prose / short sentences) is declared to apply to every artifact.
- `~/AGENTS.md` `<document_brevity>` states the same BLUF + segregate-depth rule globally.
- **Surface Budget** is enforced in `validate.py` (`_prose_line_count` + `SURFACE_SOFT_CAP` 90/110/160/220, diagrams/code/blanks excluded) — caps prose *size*, not *structure*.
