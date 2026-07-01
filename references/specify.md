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

*Default flow, not a rigid script — re-derive it against the actual Requirements. Load-bearing (don't skip or reorder): the Spec test (step 5) and the self-check (step 9).*

1. **Load Requirements** + the artifact contract (`artifact-contract.md`). Then **drain deferrals** (load-bearing): if `deferrals.md` exists, surface each unresolved `Defer-<N>` addressed to this stage, `Spec`, and re-examine it against the current option space — non-binding, re-derive not replay; resolve in place (refer to `references/deferral.md` for detailed procedure guide).
2. **Derive Behavior items**: for each desired outcome in Requirements, ask what externally-observable behavior signals it. Write as `B-<N>: <slug>` under `## Behavior`. One item per behavior; don't fold two into one.
3. **Lift Constraints**: collect continuous constraints — SLAs, non-blocking guarantees, idempotency, integrity rules, environmental bindings (existing backbone compatibility, compliance boundary, deployment envelope). Write as `C-<N>: <slug>` under `## Constraint`. If a constraint has no realization alternative, it's a Constraint — not a Design choice.
4. **Probe the contract boundary** (opt-in) — steps 2–3 are convergent, projecting the Requirements; this is Specify's one generative move. It surfaces observable behaviors and constraints the Requirements did not name (failure modes, concurrency / ordering, observable error behavior, environmental couplings) — Requirements captures the desired *outcome*; these facts first appear where the system meets its users, neighbors, and operating conditions. Stay at Specify's altitude — investigate for *what the boundary observably exposes* (a contract fact, true under any realization), not *how to build it*; a finding that is a choice among realizations is Design's, sent there by the Spec test and *No false optionality* below (so this probe does not overlap Design's investigation). Most facts aren't in anyone's head, so discover them across three channels — and reach past the as-is, or you only re-derive the status quo:
   - **Inspect the as-is** — what the boundary already is: live environmental couplings, the real neighbor / interface contracts, operating conditions. Reality is authoritative; read *observable* facts, never a realization choice.
   - **Research the outer world** — the generative reach: the failure, error, concurrency, and coupling patterns a boundary of this *class* is known to expose (SOTA, prior art, convention, protocol docs), which the current system may not embody yet. Isolate a breadth-heavy scan to a sub-agent per *Isolate breadth-heavy research*; durable findings land in `research.md`, which the probe also reads as a source.
   - **Ask the planner** (`AskUserQuestion` on Claude; the runtime-native prompt on Codex) — the facts only a human holds: which neighbor / consumer expectations and SLAs the org commits to.

   Opt-in, never a gate: a complete contract passes through untaxed; the planner accepts or declines each candidate (whichever channel surfaced it) and can cut the probe short at any point. Accepted facts become `B`/`C` (each faces the Spec test below); declined items and raw candidates stay in dialogue and, when durable, `research.md` — never the surface (`artifact-contract.md` → Surface Budget).
5. **Apply the Spec test** on every line: can the implementation change without changing this externally-observable behavior? If yes, cut the line or push to Design.
6. **Use generic-category tech only**: "message queue", "event stream", "HTTP API", "distributed cache". Specific names (Kafka, Redis, gRPC, Postgres, Spring) belong in Design.
7. **Archive research findings** worth preserving as `## <topic>` blocks in `research.md`. Evidence only — interpretations belong in Rationale (written later by `design`).
8. **Write** `spec.md`.
9. **Self-check**:
   - Grep body for tech-stack nouns — zero hits expected.
   - Every B is episode-verifiable (you could write a one-shot test).
   - Every C is continuous (no episode-triggered conditions hiding as Constraints).
   - Conditional sections (Constraint, Non-goals) omitted when empty.
   - Each item leads with its observable behavior, not preamble — the Spec is graspable from headings + lead lines (conclusion-first; `artifact-contract.md` → Prose Style).
   - If the boundary probe ran, every accepted fact became a `B`/`C` and declined candidates left no surface trace — the probe fed dialogue / research, not `spec.md`.
   - Orthogonality pass — each `B` / `C` item asserts one concern no sibling does; resolve any pair across the round that shares one (*One Concern Per Item*, `artifact-contract.md`).

## Guardrails

- **B/C split — episodic vs. continuous.**
  - Episode-triggered ("when X, Y happens") → `B-<N>: <slug>` under **Behavior**. Verifiable by a one-shot test.
  - Continuous property ("p99 < 5s", "non-blocking", "idempotent", "within compliance boundary X") → `C-<N>: <slug>` under **Constraint**. Verified downstream by SLO / monitor / CI gate.
  - *Worked split* — one requirement ("anomalies are surfaced fast and we never lose one") fans into one B + two Cs:
    - ✅ `B-1: anomaly-published-on-detection` — *when* detected, an event is published (episodic; one-shot test).
    - ✅ `C-1: publish-latency-p99-under-5s` — continuous; SLO-verified.
    - ✅ `C-2: every-detected-anomaly-eventually-published` — continuous integrity; monitor-verified.
    - ❌ folding latency/no-loss *into* the B ("published within 5s and never dropped") — buries two continuous properties in an episodic item; they lose their SLO/monitor home.
    - ❌ `C-3: anomaly-event-is-published` — a Constraint that only re-asserts B-1's occurrence as a standing claim: same subject *and* same predicate as B-1, no new property → **overlap**, not a third C → merge into B-1 or cut.
  - *Subject-vs-predicate discriminator* — a shared subject is not overlap; test the **predicate**. A Behavior asserts the *occurrence*, and a legitimate Constraint asserts a *standing property* over that subject (C-1's latency bound, C-2's eventual delivery) — a distinct concern each. A Constraint that only re-states the occurrence (C-3) adds no predicate and collapses into the Behavior; the B/C *type* split feels like it already separated the items, but type-disjoint ≠ concern-disjoint. This applies *One Concern Per Item* (`artifact-contract.md`) at the B↔C seam — the converse of the conflation ❌ above.
- **What a Spec is NOT** test: implementation can change without observable change → cut or push to Design.
- **Generic-category tech only.** Specific stack names → Design.
- **Probe the boundary — opt-in, generative.** The convergent steps project the Requirements; the probe reaches for contract facts the outcome-level Requirements could not name (failure modes, concurrency, observable error behavior, environmental couplings) — by inspecting the as-is, researching the outer world (the generative reach past the status quo), and asking the planner for the human-held slice. Never a gate; candidates feed dialogue / research, only accepted ones reach the surface.
- **Discovered facts stay solution-agnostic.** A fact surfaced by inspecting or researching a realization is stated by its observable property, not the realization or source that revealed it — it must still pass the *What a Spec is NOT* test above. E.g. "consumers must tolerate reordering" (observable), not "tolerate the message broker's partition reordering" (coupled to the realization that surfaced it).
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
