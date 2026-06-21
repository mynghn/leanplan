# LeanPlan Implementation Stage

This doc carries the procedure for the implementation stage — taking one task card to landed code, with stop-the-line triggers and distillation rules. Edge: TASK → code.

**Stage stance.** You are the senior re-reasoner, not a script-follower. The card is intent + constraints that may be stale against current code; inspect reality first, and when it contradicts the plan, walk up to the highest affected layer before coding — never patch around silently. The characteristic failures are executing the card as written and leaving WHYs stranded in discarded plan docs.

Companion: `philosophy.md` (principles), `artifact-contract.md` (shape rules).

Mid-stage, if a disturbance shifts the understanding, `/sharpen` (Claude) or `sharpen` (Codex) is the sanctioned, opt-in response — an off-pipeline reflect-and-re-derive move that reads your artifacts but never edits them, distinct from the Stop-The-Line / Artifact Update Loop below, which deliberately walks up and edits the affected layer (via `/revise`).

## Inputs

- `<cwd>/docs/features/<KEY>/plan.md` — locate `Task: <task-id>` card. If absent, stop.
- Cited anchors from the card (SPEC O/INV, DESIGN Decisions, optional Guidelines) — JIT-loaded only as needed.
- Current code at the affected paths.
- DESIGN RATIONALE — JIT only, when a stop-the-line trigger is under review.
- `artifact-contract.md` — JIT only, before writing or editing an artifact's structure or anchors (e.g. in the Artifact Update Loop); `philosophy.md` only when a principle's intent is in question. (CE: jit-loading)

## Output

- Working software (git commits on a feature branch).
- Distilled WHYs in the strongest durable form available — types, tests, annotations, commit messages, PR body, inline comments.

## Procedure

*Default flow, not a rigid script — this skill of all skills re-reasons rather than executes. Load-bearing (don't skip or reorder): inspect current code (step 3), the re-reason / stop-the-line check (step 4), explicit Completion verification (step 6), distillation (steps 7–8), the key-leak self-check (step 9).*

1. **Load** the selected `Task: <task-id>` card (Goal, Repo, Completion, Dependencies, Guidelines).
2. **JIT-load anchors** — read only the specific `O-<N>` / `INV-<N>` / `Decision-<N>` blocks referenced. Do not eagerly load the whole SPEC / DESIGN.
3. **Inspect current code** at the affected paths. Reality is authoritative.
4. **Re-reason** against current code: does the plan still apply? Any of the six stop-the-line triggers hit? If yes, run the Artifact Update Loop and surface to the user before coding.
5. **Implement** the smallest meaningful change that realizes Goal + passes Completion criteria. No speculative scope; no drive-by refactors beyond what the task requires.
6. **Verify each Completion criterion explicitly** — not "tests pass", but each specific criterion the card named.
7. **Distill WHYs** at close-out — migrate each non-obvious WHY into the strongest durable form. Load `~/.local/share/leanplan/references/impl-closeout.md` for the tier hierarchy and the commit-message / PR-body promotion rules; JIT — fetch only now, at close-out, not before. (CE: jit-loading)
8. **Confirm plan artifacts are non-load-bearing**: the WHYs they carried have migrated; discarding the plan would not lose context for future readers.
9. **Key-leak self-check** before commit — run the detector, don't eyeball it: `python3 ~/.local/share/leanplan/scripts/scan-leaks --strict <staged files>` for code, and `--text "<message/PR body>"` (or piped stdin) for the prose you're about to commit. It flags round-scoped tokens — in-round anchors, `SPEC#…`-style citations, the feature id used as a standing concept — and skips `docs/features/**`, where anchors resolve. Replace any hit with the constraint in words, or add `leanplan-allow-key` on the line for a legitimate match.
10. **Commit** with subject matching the change. Body carries distilled change rationale (alternatives, tradeoffs). For squash-merge teams, populate the PR body with the same content.
11. **Hand off** to the next unblocked task in the DAG, or raise any stop-the-line item that surfaced mid-task.

## Stop-The-Line Triggers

If any of the following surfaces at task entry or mid-implementation, stop and run the Artifact Update Loop before coding:

1. **Current code contradicts DESIGN.** Walk up to DESIGN.
2. **No verification path exists for a Completion criterion.** Walk up to TASK (fix the criterion) or further if the underlying SPEC O / INV lacks an observable signal.
3. **A Dependency is missing or itself invalidated.** Re-evaluate the DAG, not just this task.
4. **Implementation would require changing externally-observable behavior.** Walk up to SPEC; possibly REQUIREMENT.
5. **An Invariant is unprovable by the current test/monitor strategy.** Add a probe mechanism (test harness, monitor, SLO) at TASK level, or push to a continuous-verification mechanism via DESIGN.
6. **Task scope expands beyond the feature boundary.** One-deployment guardrail — pause and surface the split question.

## Artifact Update Loop

A stop-the-line trigger is an impl-time *detection*; the edit it implies is not impl's to perform inline. Hand the edit-and-propagate to the off-pipeline `/revise` move (`revise.md`) — the single home for editing committed artifacts — so a mid-impl correction follows the same path as a drift caught between stages.

On any trigger:

1. **Record the drift as a justification.** Capture what impl found — the contradiction, the missing verification path, the scope spill — as a `Delta` in `understanding.md`, or hand up an existing one. This is `/revise`'s required input, and it is what makes the correction an auditable update rather than a silent patch.
2. **Invoke `/revise <KEY>`.** It identifies the highest artifact the drift corrects (REQUIREMENT / SPEC / DESIGN / TASK), edits it and only its downstream — in place by default, re-deriving only on an anchor-set change — preserving anchor IDs, then re-validates. The walk-up, the downstream re-evaluation, and the one-deployment scope gate (split rather than grow) all live there now.
3. **Resume implementation** only after `/revise` completes and the feature re-validates.

Never patch the current task around an upstream wrongness — that silent drift is exactly what `/revise`'s justified, downstream-only discipline exists to prevent.

## Guardrails

- **Re-reason, don't execute.** The task card is intent + constraints; it may be stale against current code. Inspect first.
- **Walk up on upstream wrongness — never patch around silently.** If DESIGN is wrong, fix DESIGN; if SPEC is wrong, fix SPEC; etc. Patching only the current task masks drift from future readers.
- **Default no comments.** A new inline comment is justified only when a WHY cannot be encoded in a higher form (type / test / annotation / commit / PR body).
- **Smallest meaningful change.** No speculative scope, no drive-by refactors.
- **Distillation is not optional.** Every WHY the task relied on must have a durable home before the task is considered complete; don't leave plan docs as the only holder of important WHYs.
- **Isolate breadth-heavy investigation.** When broad code investigation would swamp the working window, run it in a sub-agent that returns only the distilled conclusions, keeping the raw trail out. Guidance, not mandate — when breadth exceeds the window. (CE: context-isolation, explore-then-compact-handoff)
