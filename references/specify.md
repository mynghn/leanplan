# LeanPlan Specify Stage

This doc carries the procedure for the Spec stage — turning a Requirements into the observable contract, stated in generic-category tech only. Edge: Requirements → Spec.

**Stage stance.** State what the system externally exposes — observable behavior only; an implementation swap must not change a single line you write. The attractor to resist is realization leakage (naming *how* it's built); the "what a Spec is NOT" test below is your instrument.

Companion: `philosophy.md` (principles), `artifact-contract.md` (shape rules).

Mid-stage, if a disturbance shifts the understanding, `leanplan-rethink` is the sanctioned, opt-in response — an off-pipeline reflect-and-re-derive move that reads your artifacts but never edits them — instead of ignoring it or hand-rolling a fix.

## Inputs

- `<cwd>/docs/features/<KEY>/requirements.md` (required). If absent, stop and tell the user to run `leanplan-frame <feature-title>` first — it allocates the `<KEY>` (`NNNN-slug`) dir and prints its path.
- `<cwd>/docs/features/<KEY>/research.md` (optional, for context reuse).

## Outputs

- `<cwd>/docs/features/<KEY>/spec.md` — required.
- `<cwd>/docs/features/<KEY>/research.md` — append `## <topic>` blocks only when a finding is durable evidence worth archiving for future reference (codebase pattern discovery, SOTA article takeaway, industry convention, org history).

## Procedure

*Default flow, not a rigid script — re-derive it against the actual Requirements. Load-bearing (don't skip or reorder): the Spec test (step 4) and the self-check (step 8).*

1. **Load Requirements** + the artifact contract (`artifact-contract.md`). Then **drain deferrals** (load-bearing): if `deferrals.md` exists, surface each unresolved `Defer-<N>` addressed to this stage, `Spec`, and re-examine it against the current option space — non-binding, re-derive not replay; resolve in place (refer to `references/deferral.md` for detailed procedure guide).
2. **Derive Behavior items**: for each desired outcome in Requirements, ask what externally-observable behavior signals it. Write as `B-<N>: <slug>` under `## Behavior`. One item per behavior; don't fold two into one.
3. **Lift Constraints**: collect continuous constraints — SLAs, non-blocking guarantees, idempotency, integrity rules, environmental bindings (existing backbone compatibility, compliance boundary, deployment envelope). Write as `C-<N>: <slug>` under `## Constraint`. If a constraint has no realization alternative, it's a Constraint — not a Design choice.
4. **Apply the Spec test** on every line: can the implementation change without changing this externally-observable behavior? If yes, cut the line or push to Design.
5. **Use generic-category tech only**: "message queue", "event stream", "HTTP API", "distributed cache". Specific names (Kafka, Redis, gRPC, Postgres, Spring) belong in Design.
6. **Archive research findings** worth preserving as `## <topic>` blocks in `research.md`. Evidence only — interpretations belong in Rationale (written later by `design`).
7. **Write** `spec.md`.
8. **Self-check**:
   - Grep body for tech-stack nouns — zero hits expected.
   - Every B is episode-verifiable (you could write a one-shot test).
   - Every C is continuous (no episode-triggered conditions hiding as Constraints).
   - Conditional sections (Constraint, Non-goals) omitted when empty.
   - Each item leads with its observable behavior, not preamble — the Spec is graspable from headings + lead lines (conclusion-first; `artifact-contract.md` → Prose Style).

## Guardrails

- **B/C split — episodic vs. continuous.**
  - Episode-triggered ("when X, Y happens") → `B-<N>: <slug>` under **Behavior**. Verifiable by a one-shot test.
  - Continuous property ("p99 < 5s", "non-blocking", "idempotent", "within compliance boundary X") → `C-<N>: <slug>` under **Constraint**. Verified downstream by SLO / monitor / CI gate.
  - *Worked split* — one requirement ("anomalies are surfaced fast and we never lose one") fans into one B + two Cs:
    - ✅ `B-1: anomaly-published-on-detection` — *when* detected, an event is published (episodic; one-shot test).
    - ✅ `C-1: publish-latency-p99-under-5s` — continuous; SLO-verified.
    - ✅ `C-2: every-detected-anomaly-eventually-published` — continuous integrity; monitor-verified.
    - ❌ folding latency/no-loss *into* the B ("published within 5s and never dropped") — buries two continuous properties in an episodic item; they lose their SLO/monitor home.
- **What a Spec is NOT** test: implementation can change without observable change → cut or push to Design.
- **Generic-category tech only.** Specific stack names → Design.
- **Park a genuine deferral; don't discard it.** A real cross-stage decision that surfaces here goes into `deferrals.md` as a `Defer-<N>` addressed to its owning stage, rather than being discarded — opt-in planner judgment; procedure in `references/deferral.md`.
- **No false optionality.** If a property has no real alternative realization, it's a Constraint, not a Design choice.
- **Spec `B` / `C` is the observable canonical home.** A C realizing a Requirements system-policy states the observable form and leaves the *intent* to Requirements (`artifact-contract.md` → One Prose Home Per Fact).
- **Stable IDs.** `N` is stable across slug edits. Append new items with higher numbers; supersede by retire-by-note, not deletion — the global rule, in `artifact-contract.md` → Anchors.
- **Research archive is evidence-only.** Interpretations belong in Rationale.
- **Isolate breadth-heavy research.** When Spec research (a wide SOTA / prior-art scan) would swamp the working window, run it in a sub-agent that returns only the distilled Research entries, not the raw search trail. Guidance, not mandate — when breadth exceeds the window. (context-engineering: context-isolation, explore-then-compact-handoff)

## Template

```markdown
# <KEY> — Spec

## Behavior

### B-1: <slug>
<when X, externally observable Y happens>

## Constraint

### C-1: <slug>
<continuous property that must always hold>

## Non-goals
- <only when the Spec's scope is ambiguous>
```

Heading levels are flexible (H2 / H3 / H4) per the artifact contract — items can be at H2 (flat) or H3 (nested under section header) as long as the heading text matches `B-<N>: <slug>` / `C-<N>: <slug>` exactly.

## Hand-off

Next edge: `leanplan-design <KEY>`.
