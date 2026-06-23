# 260623-deferral-lane — Tasks

## Guidelines

- **Base.** All work is in this framework repo, in the `leanplan-N` worktree on `feat/deferral-lane`.
- **Reflexive sweep exemption (load-bearing).** The Rename track must never touch *this* feature's own dir or the historical `docs/features/260620-*` dirs — they describe `understanding.md` as data; rewriting them falsifies the record (`Design#D-6-rename-understanding-archive`). Confirm `git status` shows only intended files before committing.
- **Green checkpoint.** `scripts/leanplan-selftest` is the verification gate for every validator / contract / rename change (F2, L1, R2) — run it after each, not only at the end.
- **Reflexive surface budget.** The stage-doc additions (B2, B3) and contract additions (F1) stay terse — a one-line hook on the always-loaded surface, detail in the on-demand companion. The framework applies its own small-surface discipline.

## Dependency DAG

```mermaid
flowchart LR
    subgraph F [Foundation: lane structure]
      F1[F1 contract: lane + anchor] --> F2[F2 validate.py: Defer]
    end
    subgraph B [Behavior: capture + drain]
      B1[B1 deferral.md companion] --> B2[B2 capture hooks]
      B1 --> B3[B3 drain at entry]
    end
    subgraph L [No-loss]
      L1[L1 validate.py advisory check]
    end
    subgraph R [Rename: understanding-shifts]
      R1[R1 filename sweep] --> R2[R2 validate.py + selftest]
    end
    F1 --> B1
    F2 --> L1
    F2 -. coordinate validate.py edits .-> R2
```

Tracks: **F** registers the lane's structure; **B** weaves capture/drain into the stage docs; **L** makes no-loss observable; **R** is the separable `understanding.md` rename.

## T: F1

- **Goal**: Register the deferrals lane in the artifact contract so a deferral has a structural home distinct from the understanding-shift archive — add the off-review-surface archive tier, the `Defer-<N>` anchor and `Deferrals#Defer-<N>-<slug>` citation, and the non-binding block's required shape, per `Design#D-1-deferrals-archive-lane` and `Design#D-2-non-binding-prior-block-shape` (satisfying `Spec#C-4-deferral-and-understanding-records-single-role`, `Spec#C-2-capture-off-the-review-surface`, `Spec#C-5-capture-durable-across-resets`). Anchor the Decisions; don't restate the block fields.
- **Repo**: leanplan — `references/artifact-contract.md`, `framework-design.md` (§4 tier model).
- **Completion**:
  - Layering, anchors, and required-shape sections name `deferrals.md` / `Defer-N` / `Deferrals#`, with the lane placed as archive (not surface).
  - A feature dir whose `deferrals.md` holds a `Defer-1` block validates clean (after F2).
- **Dependencies**: none.

## T: F2

- **Goal**: Teach `validate.py` the lane so `Defer-N` anchors and `Deferrals#` citations resolve — extend `ANCHOR_RE` / `CITATION_RE` with a `Defer` alternative ordered before `D` (as `Delta` already is, so a deferral never parses as a Design decision), and register the lane file in `OPTIONAL_FILES` (`Design#D-1-deferrals-archive-lane`, `Spec#C-4-deferral-and-understanding-records-single-role`).
- **Repo**: leanplan — `scripts/validate.py`, `scripts/leanplan-selftest`.
- **Completion**:
  - selftest cases: a `Defer-1` anchor resolves; a `Deferrals#Defer-1-<slug>` citation resolves; a duplicate `Defer-1` errors; a broken `Deferrals#Defer-9-…` citation errors.
  - Full selftest green.
- **Dependencies**: F1 (the contract defines what the validator enforces).

## T: B1

- **Goal**: Author the on-demand companion `references/deferral.md` carrying the capture and drain procedures and the non-binding block shape — including the high-freedom, re-derive-don't-replay drain (`Design#D-4-drain-by-re-derivation-at-stage-entry`, `Design#D-2-non-binding-prior-block-shape`, `Spec#C-3-surfaced-deferral-is-non-binding`). This is the Level-3 reference the stage hooks point to (`Design#D-3-capture-as-affirmative-stage-hook`).
- **Repo**: leanplan — `references/deferral.md` (new).
- **Completion**:
  - The companion documents (a) the `Defer-N` block fields + the `(resolved -> …)` resolve-in-place marker; (b) capture = append a block addressed to its owning stage; (c) drain = surface + re-examine against the *current* option space, non-binding.
  - A planner following it produces a `Defer-N` block that passes F2's validation.
- **Dependencies**: F1.

## T: B2

- **Goal**: Add the capture hook at each *forward* disposal point — where a stage discards content bound for a later stage (Requirements "strip them", Spec "push to Design", Design "belongs in Tasks"; Tasks is the last stage, no forward target) — an affirmative redirect to park a genuine cross-stage decision as a `Defer-N` addressed forward to the later stage that owns it instead of discarding it (`Spec#B-1-deferral-captured-on-set-aside`, `Spec#C-6-capture-is-opt-in-judgment`, `Design#D-3-capture-as-affirmative-stage-hook`). Keep it a one-line hook into `references/deferral.md` so the always-loaded surface stays lean (`Spec#C-2-capture-off-the-review-surface`).
- **Repo**: leanplan — `references/{requirements,specify,design}.md`.
- **Completion**:
  - Each of the 3 capture-source stage docs carries a one-line capture hook pointing to the companion; the hook reads as opt-in (no gate, no auto-detect).
  - Each stage doc's prose-line count stays within its reflexive surface budget.
- **Dependencies**: B1.

## T: B3

- **Goal**: Extend each *downstream* stage's entry ("Load …") step — Spec, Design, Tasks — to drain the deferrals addressed to it: load `deferrals.md`, surface the unresolved `Defer-N` for this stage, re-examine each against the full current option space, and resolve in place (`Spec#B-2-deferrals-surfaced-at-owning-stage`, `Spec#C-3-surfaced-deferral-is-non-binding`, `Design#D-4-drain-by-re-derivation-at-stage-entry`). Requirements is first — nothing is addressed back to it. The consultation is load-bearing; the decision it prompts is free.
- **Repo**: leanplan — `references/{specify,design,tasks}.md`.
- **Completion**:
  - Each downstream stage's load step instructs the drain + re-examination as a load-bearing step.
  - The drain wording is re-derive-not-apply — no "apply the deferred option" phrasing anywhere (a low-freedom drain would re-introduce pinning).
- **Dependencies**: B1 (companion defines the drain); shares files with B2.

## T: L1

- **Goal**: Add the advisory `validate.py` no-loss check — a `Defer-N` addressed to a stage whose `<stage>.md` exists but lacking a `(resolved -> …)` marker is surfaced as a warning (escalating under `--strict`, mirroring the surface-budget guardrail), realizing `Spec#B-3-undrained-deferral-flagged-at-close-out` / `Spec#C-1-no-deferral-silently-lost` (`Design#D-5-no-loss-via-advisory-check`).
- **Repo**: leanplan — `scripts/validate.py`, `scripts/leanplan-selftest`.
- **Completion**:
  - selftest cases: an unresolved `Defer-N` whose owning stage's file exists → warning; a `(resolved -> …)`-marked one → no warning; a deferral for a not-yet-authored stage → no warning; `--strict` escalates the warning to an error.
- **Dependencies**: F2 (validator already parses `Defer`).

## T: R1

- **Goal**: Rename the archive `understanding.md` → `understanding-shifts.md` by sweeping the filename literal across live-framework files, keeping the `Delta-N` anchor and `Understanding#` citation prefix unchanged (`Spec#C-4-deferral-and-understanding-records-single-role`, `Design#D-6-rename-understanding-archive`). The historical `docs/features/260620-*` dirs and this feature's own dir are exempt (quote-as-data — see Guidelines).
- **Repo**: leanplan — `references/{sharpen,revise,design,implement,artifact-contract}.md`, `framework-design.md`, `adapters/claude/{sharpen,revise}/SKILL.md`.
- **Completion**:
  - No live-framework reference to the literal `understanding.md` survives (grep clean outside the exempt dirs); historical dirs unchanged.
  - `Understanding#Delta-…` citations still resolve (prefix + anchor untouched).
- **Dependencies**: none (separable track); coordinate the `validate.py` edits with F2.

## T: R2

- **Goal**: Make the tooling track the renamed file — point `validate.py` `OPTIONAL_FILES["understanding"]` at `understanding-shifts.md` and update the `leanplan-selftest` fixtures that write/assert the file, keeping the `Delta-N` / `Understanding#` assertions intact (`Design#D-6-rename-understanding-archive`).
- **Repo**: leanplan — `scripts/validate.py`, `scripts/leanplan-selftest`, `fixtures/`.
- **Completion**:
  - selftest green against `understanding-shifts.md`: the duplicate-`Delta` + citation-ok + citation-broken cases still pass.
- **Dependencies**: R1 (renames the file); coordinate `validate.py` with F2.
