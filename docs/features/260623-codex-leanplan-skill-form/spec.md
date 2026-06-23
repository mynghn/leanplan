# 260623-codex-leanplan-skill-form — Spec

## Behavior

### B-1: codex-move-catalog-complete
When a maintainer inspects the Codex LeanPlan surface, every supported LeanPlan move has an explicit entry contract: `requirements`, `specify`, `design`, `tasks`, `implement`, `sharpen`, `revise`, and `validate`. Each entry contract names the user intent it accepts, the required input shape, the canonical reference it loads, and the next handoff or terminal result. One-shot test: inspect the Codex LeanPlan surface and assert the catalog covers the full move set with no implicit-only move.

### B-2: requested-move-selects-matching-stage
When a user invokes a specific LeanPlan move in Codex, the active behavior is the matching stage or off-pipeline move, not a generic framework run. The response follows that move's input requirements, writes or validates only that move's artifact boundary, and gives the matching handoff. One-shot test: invoke each cataloged move against a controlled feature fixture and assert the selected canonical reference and output boundary match the requested move.

### B-3: adapter-parity-is-reviewable
When a reviewer compares the Codex and Claude LeanPlan adapters, every Codex entry contract maps to the same canonical LeanPlan move as its Claude counterpart, or carries a visible Codex-specific runtime reason for diverging in surface shape. One-shot test: build the adapter mapping table; each row resolves to one shared reference and either a same-shape counterpart or an explicit divergence reason.

## Constraint

### C-1: canonical-reference-single-home
Stage procedure, artifact shape, guardrails, and validation semantics stay authored in the shared LeanPlan references. The Codex surface may route to those references and add Codex-specific invocation glue, but it does not fork or restate the stage procedures as an independent source of truth. Verified by inspection: each Codex entry contract points to the shared reference that owns the move.

### C-2: one-stage-jit-loading-preserved
Normal Codex execution loads the requested move's canonical reference and only the on-demand companion material that move requires. It does not load unrelated stage references merely because those stages share the LeanPlan framework. Verified by tracing a representative invocation for each move and checking the loaded reference set.

### C-3: activation-quality-drives-surface-shape
The chosen Codex surface shape is justified by activation quality: users and agents can reliably select the intended LeanPlan move without carrying unrelated stage procedure in the active context. If the Codex shape differs from the Claude shape, the reason is a Codex runtime constraint or activation-quality tradeoff, not convenience or historical accident. Verified by the visible divergence rationale required by B-3.

### C-4: cross-vendor-semantic-parity
For every supported LeanPlan move, Codex and Claude resolve to the same canonical reference and preserve the same artifact boundary, validation expectation, and handoff meaning. Vendor-specific surface differences are allowed only as invocation glue and must be documented in the adapter mapping so an adapter diff cannot silently fork LeanPlan behavior. Verified by comparing the Codex and Claude move mappings against the shared references.

## Non-goals

- **Choosing file count as the contract.** The observable contract is complete, correct, reviewable LeanPlan move selection; whether that is implemented by one surface or several is Design's decision.
- **Changing LeanPlan stage semantics.** The move set, canonical references, artifact contracts, and validators remain the existing shared framework behavior.
- **Changing Claude behavior for parity alone.** Claude may remain stage-specific unless a shared-framework issue is discovered later.
