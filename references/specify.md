# LeanPlan Specify Stage

This doc carries the procedure for the SPEC stage — turning a REQUIREMENT into a generic-category tech contract. Edge: REQUIREMENT → SPEC.

**Stage stance.** State what the system externally exposes — observable behavior only; an implementation swap must not change a single line you write. The attractor to resist is realization leakage (naming *how* it's built); the "what a SPEC is NOT" test below is your instrument.

Companion: `philosophy.md` (principles), `artifact-contract.md` (shape rules).

Mid-stage, if a disturbance shifts the understanding, `/sharpen` (Claude) or `sharpen` (Codex) is the sanctioned, opt-in response — an off-pipeline reflect-and-re-derive move that reads your artifacts but never edits them — instead of ignoring it or hand-rolling a fix.

## Inputs

- `<cwd>/docs/features/<KEY>/requirement.md` (required). If absent, stop and tell the user to run `/requirement <feature-title>` (or `requirement <feature-title>` for Codex) first — it allocates the `<KEY>` (`NNNN-slug`) dir and prints its path.
- `<cwd>/docs/features/<KEY>/research.md` (optional, for context reuse).

## Outputs

- `<cwd>/docs/features/<KEY>/spec.md` — required.
- `<cwd>/docs/features/<KEY>/research.md` — append `## <topic>` blocks only when a finding is durable evidence worth archiving for future reference (codebase pattern discovery, SOTA article takeaway, industry convention, org history).

## Procedure

*Default flow, not a rigid script — re-derive it against the actual REQUIREMENT. Load-bearing (don't skip or reorder): the SPEC test (step 4) and the self-check (step 8).*

1. **Load REQUIREMENT** + the artifact contract (`artifact-contract.md`).
2. **Derive Outcome items**: for each biz outcome in REQUIREMENT, ask what externally-observable behavior signals it. Write as `O-<N>: <slug>` under `## Outcome`. One item per behavior; don't fold two into one.
3. **Lift Invariants**: collect continuous constraints — SLAs, non-blocking guarantees, idempotency, integrity rules, environmental bindings (existing backbone compatibility, compliance boundary, deployment envelope). Write as `INV-<N>: <slug>` under `## Invariants`. If a constraint has no realization alternative, it's an Invariant — not a DESIGN choice.
4. **Apply the SPEC test** on every line: can the implementation change without changing this externally-observable behavior? If yes, cut the line or push to DESIGN.
5. **Use generic-category tech only**: "message queue", "event stream", "HTTP API", "distributed cache". Specific names (Kafka, Redis, gRPC, Postgres, Spring) belong in DESIGN.
6. **Archive research findings** worth preserving as `## <topic>` blocks in `research.md`. Evidence only — interpretations belong in RATIONALE (written later by `design`).
7. **Write** `spec.md`.
8. **Self-check**:
   - Grep body for tech-stack nouns — zero hits expected.
   - Every O is episode-verifiable (you could write a one-shot test).
   - Every INV is continuous (no episode-triggered conditions hiding as Invariants).
   - Conditional sections (Invariants, Non-goals) omitted when empty.
   - Each item leads with its observable behavior, not preamble — the SPEC is graspable from headings + lead lines (conclusion-first; `artifact-contract.md` → Prose Style).

## Guardrails

- **O/INV split — episodic vs. continuous.**
  - Episode-triggered ("when X, Y happens") → `O-<N>: <slug>` under **Outcome**. Verifiable by a one-shot test.
  - Continuous property ("p99 < 5s", "non-blocking", "idempotent", "within compliance boundary X") → `INV-<N>: <slug>` under **Invariants**. Verified downstream by SLO / monitor / CI gate.
  - *Worked split* — one requirement ("anomalies are surfaced fast and we never lose one") fans into one O + two INVs:
    - ✅ `O-1: anomaly-published-on-detection` — *when* detected, an event is published (episodic; one-shot test).
    - ✅ `INV-1: publish-latency-p99-under-5s` — continuous; SLO-verified.
    - ✅ `INV-2: every-detected-anomaly-eventually-published` — continuous integrity; monitor-verified.
    - ❌ folding latency/no-loss *into* the O ("published within 5s and never dropped") — buries two continuous properties in an episodic item; they lose their SLO/monitor home.
- **What a SPEC is NOT** test: implementation can change without observable change → cut or push to DESIGN.
- **Generic-category tech only.** Specific stack names → DESIGN.
- **No false optionality.** If a property has no real alternative realization, it's an Invariant, not a DESIGN choice. Don't fake optionality.
- **SPEC `O` / `INV` is the observable canonical home.** An INV realizing a REQUIREMENT system-policy states the observable form and leaves the biz *intent* to REQUIREMENT (`artifact-contract.md` → One Prose Home Per Fact).
- **Stable IDs.** `N` is stable across slug edits. Append new items with higher numbers; retire by inline `(retired)` note rather than deleting.
- **Research archive is evidence-only.** Interpretations belong in RATIONALE.
- **Isolate breadth-heavy research.** When SPEC research (a wide SOTA / prior-art scan) would swamp the working window, run it in a sub-agent that returns only the distilled RESEARCH entries, not the raw search trail. Guidance, not mandate — when breadth exceeds the window. (CE: context-isolation, explore-then-compact-handoff)

## Template

```markdown
# <KEY> — SPEC

## Outcome

### O-1: <slug>
<when X, externally observable Y happens>

## Invariants

### INV-1: <slug>
<continuous property that must always hold>

## Non-goals
- <only when tech scope is ambiguous>
```

Heading levels are flexible (H2 / H3 / H4) per the artifact contract — items can be at H2 (flat) or H3 (nested under section header) as long as the heading text matches `O-<N>: <slug>` / `INV-<N>: <slug>` exactly.

## Hand-off

Next edge: `/design <KEY>` (Claude) or `design <KEY>` (Codex).
