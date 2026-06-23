# LeanPlan Implementation Stage

This doc carries the procedure for the implementation stage — taking one task card to landed code, with stop-the-line triggers and distillation rules. Edge: Tasks → code.

**Stage stance.** You are the senior re-reasoner, not a script-follower. The card is intent + constraints that may be stale against current code; inspect reality first, and when it contradicts the plan, walk up to the highest affected layer before coding — never patch around silently. The characteristic failures are executing the card as written and leaving WHYs stranded in discarded plan docs.

Companion: `philosophy.md` (principles), `artifact-contract.md` (shape rules).

Mid-stage, if a disturbance shifts the understanding, `/sharpen` (Claude) or `leanplan-sharpen` (Codex) is the sanctioned, opt-in response — an off-pipeline reflect-and-re-derive move that reads your artifacts but never edits them, distinct from the Stop-The-Line / Artifact Update Loop below, which deliberately walks up and edits the affected layer (via `/revise` on Claude or `leanplan-revise` on Codex).

## Inputs

- `<cwd>/docs/features/<KEY>/tasks.md` — locate `T: <task-id>` card. If absent, stop.
- Cited anchors from the card (Spec B/C, Design Decisions, optional Guidelines) — JIT-loaded only as needed.
- Current code at the affected paths.
- Design Rationale — JIT only, when a stop-the-line trigger is under review.
- `artifact-contract.md` — JIT only, before writing or editing an artifact's structure or anchors (e.g. in the Artifact Update Loop); `philosophy.md` only when a principle's intent is in question. (context-engineering: jit-loading)

## Output

- Working software (git commits on a feature branch).
- Distilled WHYs in the strongest durable form available — types, tests, annotations, commit messages, PR body, inline comments.

## Procedure

*Default flow, not a rigid script — this skill of all skills re-reasons rather than executes. Load-bearing (don't skip or reorder): consult the card's load-bearing citations (step 2), inspect current code (step 3), the re-reason / stop-the-line check (step 4), explicit Completion verification (step 6), distillation (steps 7–8), the key-leak self-check (step 9).*

1. **Load** the selected `T: <task-id>` card (Goal, Repo, Completion, Dependencies, Guidelines).
2. **JIT-load anchors** — read only the specific `B-<N>` / `C-<N>` / `D-<N>` blocks referenced; do not eagerly load the whole Spec / Design. **For the card's load-bearing citations, reading is not optional.** The Spec `B` / `C` it realizes and the Design `Decision` it builds on must be opened and read; you cannot realize or build what you have not read. Naming the slug — or paraphrasing it — is not consulting it. Archive citations (Rationale, Research) stay load-on-challenge, never forced. The read leaves its proof at close-out (step 7): the substance you distill must carry the anchor's actual constraint, which a slug copied without reading cannot fake.
3. **Inspect current code** at the affected paths. Reality is authoritative.
4. **Re-reason** against current code: does the plan still apply? Any of the six stop-the-line triggers hit? If yes, run the Artifact Update Loop and surface to the user before coding.
5. **Implement** the smallest meaningful change that realizes Goal + passes Completion criteria. No speculative scope; no drive-by refactors beyond what the task requires.
6. **Verify each Completion criterion explicitly** — not "tests pass", but each specific criterion the card named.
7. **Distill WHYs** at close-out — migrate each non-obvious WHY into the strongest durable form. **The constraint of each of the card's load-bearing citations migrates too** (the Spec `B` / `C` it realizes, the Design `Decision` it builds on) — mandatory for that class, not gated on "non-obvious", since that substance is the step-2 consultation proof. Load `~/.local/share/leanplan/references/implement-closeout.md` for the tier hierarchy, the commit-message / PR-body promotion rules, and the close-out reconciliation that verifies this; JIT — fetch only now, at close-out, not before. (context-engineering: jit-loading)
8. **Confirm plan artifacts are non-load-bearing**: the WHYs they carried have migrated; discarding the plan would not lose context for future readers.
9. **Key-leak self-check** before commit — run the detector, don't eyeball it: `python3 ~/.local/share/leanplan/scripts/scan-leaks --strict <staged files>` for code, and `--text "<message/PR body>"` (or piped stdin) for the prose you're about to commit. It flags round-scoped tokens — in-round anchors, `Spec#…`-style citations, the feature id used as a standing concept — and skips `docs/features/**`, where anchors resolve. Replace any hit with the constraint in words, or add `leanplan-allow-key` on the line for a legitimate match.
10. **Commit** with subject matching the change. Body carries distilled change rationale (alternatives, tradeoffs). For squash-merge teams, populate the PR body with the same content.
11. **Hand off** to the next unblocked task in the DAG, or raise any stop-the-line item that surfaced mid-task.

## Stop-The-Line Triggers

If any of the following surfaces at task entry or mid-implementation, stop and run the Artifact Update Loop before coding:

1. **Current code contradicts Design.** Walk up to Design.
2. **No verification path exists for a Completion criterion.** Walk up to Tasks (fix the criterion) or further if the underlying Spec B / C lacks an observable signal.
3. **A Dependency is missing or itself invalidated.** Re-evaluate the DAG, not just this task.
4. **Implementation would require changing externally-observable behavior.** Walk up to Spec; possibly Requirements.
5. **A Constraint is unprovable by the current test/monitor strategy.** Add a probe mechanism (test harness, monitor, SLO) at Tasks level, or push to a continuous-verification mechanism via Design.
6. **Task scope expands beyond the feature boundary.** One-deployment guardrail — pause and surface the split question.
7. **A deferral was stranded by planning.** A `Defer-N` in `deferrals.md` addressed to a planning stage is still unresolved (no `(resolved -> …)` marker) though planning is complete — a parked decision was never drained. Check once, at first task entry (`validate.py` flags it). Drain it at its owning stage — re-examine against the now-current options and resolve in place, routing through `/revise` (Claude) or `leanplan-revise` (Codex) when the resolution edits a committed artifact — before building on the plan.

## Artifact Update Loop

A stop-the-line trigger is an implementation-time *detection*; the edit it implies is not implementation's to perform inline. Hand the edit-and-propagate to the off-pipeline `/revise` (Claude) or `leanplan-revise` (Codex) move (`revise.md`) — the single home for editing committed artifacts — so a mid-implementation correction follows the same path as a drift caught between stages.

On any trigger:

1. **Record the drift as a justification.** Capture what implementation found — the contradiction, the missing verification path, the scope spill — as a `Delta` in `understanding-shifts.md`, or hand up an existing one. This is `/revise` / `leanplan-revise`'s required input, and it is what makes the correction an auditable update rather than a silent patch.
2. **Invoke `/revise <KEY>`** (Claude) / **`leanplan-revise <KEY>`** (Codex) — JIT-load `revise.md` and run the move in-session. It identifies the highest artifact the drift corrects (Requirements / Spec / Design / Tasks), edits it and only its downstream — in place by default, re-deriving only on an anchor-set change — preserving anchor IDs, then re-validates. The walk-up, the downstream re-evaluation, and the one-deployment scope gate (split rather than grow) all live there now.
3. **Resume implementation** only after `/revise` / `leanplan-revise` completes and the feature re-validates.

Never patch the current task around an upstream wrongness — that silent drift is exactly what `/revise` / `leanplan-revise`'s justified, downstream-only discipline exists to prevent.

## Guardrails

- **Re-reason, don't execute.** The task card is intent + constraints; it may be stale against current code. Inspect first.
- **Walk up on upstream wrongness — never patch around silently.** If Design is wrong, fix Design; if Spec is wrong, fix Spec; etc. Patching only the current task masks drift from future readers.
- **Default no comments.** A new inline comment is justified only when a WHY cannot be encoded in a higher form (type / test / annotation / commit / PR body).
- **Smallest meaningful change.** No speculative scope, no drive-by refactors.
- **Distillation is not optional.** Every WHY the task relied on must have a durable home before the task is considered complete; don't leave plan docs as the only holder of important WHYs.
- **Isolate breadth-heavy investigation.** When broad code investigation would swamp the working window, run it in a sub-agent that returns only the distilled conclusions, keeping the raw trail out. Guidance, not mandate — when breadth exceeds the window. (context-engineering: context-isolation, explore-then-compact-handoff)
