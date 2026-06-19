# 260619-context-engineering-knowledges-grounding — DESIGN RATIONALE

## Decision-1: two-layer-vendored-archive

Forces: grounding must travel with the install (`INV-1`), stay off the hot path (`INV-3`), and not rot silently (`INV-2`) — while the framework stays lean.

Alternatives considered:

- **Name-only, no vendored content** (Report 1's school) — ground purely by concept name, treat the KB as an optional external companion. Rejected: fails `INV-1`/`O-2` — a reader on a fresh install can name the principle but cannot reach its definition+source. Names alone are not grounding; they are pointers to nothing shipped.
- **Inline the concept into the surface doc** — rejected: violates `INV-3` (bloats the hot path) and the small-surface principle; it is the exact bloat the brief warns against.
- **Single flat `context-engineering.md`** holding map + all concepts — rejected: one large file defeats JIT (you load all 14 to read one) and muddles the mapping/definition layers. The two-layer split (map → nodes) mirrors LeanPlan's own surface→archive and lets a challenge load just the one node it needs.
- **Vendor only the cited subset (~10), trim edges** — rejected after audit: the `Related`-edge closure from the cited set reaches all 14 (the `three-axes-of-context-degradation` lens links all six axis members; `compaction-vs-eviction` pulls in two more), so no proper subset is link-closed. A subset forces edge-pruning that diverges the copies from the KB and guts the lens. All 14 costs ≈ 0 (small distilled nodes) and keeps fidelity. **This overturns the brief's "subset, not all 14" locked decision** — the premise (that a smaller closed set exists) was false.

Chosen: vendor all 14 as a two-layer archive. This is in-bounds under principle 7: P6/P7 govern transient per-feature plan docs under `docs/features/`, not the framework's permanent `references/` (corroborated — the validator and the no-frontmatter rule are both feature-scoped; `research.md` → Principle 7 scope).

Invalidation triggers: the KB's own concept set changes shape (new axis, merged concepts); a concept's `Related` edges change enough that the vendored copy misleads; the leanness budget is genuinely threatened by node count (not at 14).

## Decision-2: surface-grounds-by-name-hook

The crux resolution. A concept *name* (`jit-loading`, `lost-in-the-middle`) is recognized context-engineering terminology, not a dependency — naming it is free and portable, and it is what every KB entry uses as its own `name:`. So the surface pays only a parenthetical; the definition lives one resolve-step away in the archive.

Alternative — inline a sentence of the concept at each rule — rejected: multiplied across rules it reconstitutes the verbose surface the framework exists to avoid, and it duplicates content that then drifts from the node. The name is identity; the node is content (the same discipline as LeanPlan's own anchor "ID + slug, not restatement", `leanplan.md` §9).

Accepted tradeoff: a reader must take one hop (name → mapping → node) to get the definition. That hop is the point — it keeps the hot path lean and is loaded only on challenge.

Invalidation: if a rule's grounding is challenged so often that the hop is friction, promote a one-line gloss to the rule — but never the full concept.

## Decision-3: adapters-lazy-load-references

This fixes a measured self-contradiction: every stage SKILL eager-loads `philosophy.md` (23) + `artifact-contract.md` (126) + `<stage>.md` before acting — 247 lines at `impl` — while the framework (and `impl.md` itself) preaches JIT loading. Grounding the framework in `jit-loading` while it violates `jit-loading` would be the loudest "do as I say, not as I do."

Chosen split: the `<stage>.md` procedure is the always-load (it is the actual instruction set + template for the edge). `artifact-contract.md` (the 126-line bulk, the worst offender) becomes load-on-demand. `philosophy.md` also becomes on-demand.

Correctness gate (the real risk): structural correctness depends on the contract, so the trigger must be reliable. The rule is explicit — **load `artifact-contract.md` before writing or editing an artifact's structure or anchors** — phrased as a stop condition in the SKILL, not left implicit. Lazy ≠ never; it is load-at-first-structural-need.

Alternative — keep `philosophy.md` always-loaded (it is small and carries the name-hooks) — defensible, but it reintroduces an eager reference and the name-hooks resolve via the mapping anyway; on-demand is the consistent choice. Revisit if agents in practice skip needed principle context.

Invalidation: a stage is observed authoring malformed structure because the contract was not pulled — then tighten the trigger or restore an always-load for that stage.

## Decision-4: isolation-as-method-primitive

`specify` (REQ→SPEC research), `design` (code investigation), and `impl` (broad code investigation) are the breadth-heavy edges — the ones whose raw investigation trail would swamp the planning window. Isolating that work into a sub-agent that returns only the distilled artifact grounds `context-isolation` + `explore-then-compact-handoff`. This feature's own cold audit is the worked example: two breadth scans ran isolated; only their conclusions reached `research.md`.

Tooling gap closed: the `specify` adapter lacked `Agent` in `allowed-tools` (`design`/`impl` already had it), so the primitive was unauthorizable on the very edge that most needs it.

Guidance, not mandate — "when breadth exceeds the window." Mandating sub-agents for trivial lookups would burn latency and tokens; the call is the agent's at investigation time.

Invalidation: harness sub-agent semantics change materially, or isolation is observed to lose signal the planner needed (then tune what the sub-agent returns, not whether to isolate).

## Decision-7: session-boundary-principle

Neither prior report carried this; the brief promotes it to first-class. The principle: the planning spine (requirement→spec→design→plan) is tightly coupled and belongs in one warm session; impl is the natural hard cut to a fresh frame. Grounds `compaction-vs-eviction` (summarize-and-reinitialize at a task boundary) + `explore-then-compact-handoff` + `context-isolation`; the "warm session" half also leans on `prefix-cache-economics` (cache warmth across the continuous spine).

Cross-session resolution (the fork the reports split on): **no new per-feature state artifact.** Report 1 proposed a transient `progress.md`; rejected here on principle 7 — impl survival across sessions is carried by harness task-state + git commits (which already carry distilled WHYs per principle 8), not a living doc. This holds P7 intact rather than reframing it.

Placement: design→plan is the loosest intra-planning seam (plan can be re-derived from design cheaply), so if any in-spine cut is ever needed it goes there; req→spec→design stay continuous.

Harness realization: on Claude Code the boundary and pivots are realized by grounded session-management commands — `/handoff <goal>` (a goal-scoped fresh-session brief at the plan→impl cut) and `/compact-focus` (in-session lean at a pivot). Both are themselves grounded in the same CE concepts (`explore-then-compact-handoff`, `compaction-vs-eviction`, `lost-in-the-middle`, `prefix-cache-economics`), so LeanPlan's principle and the harness commands agree by *shared grounding*, not coincidence — and this dogfood run uses `/handoff` at its own plan→impl cut. Portability gate: these are optional accelerators, named only in §13 / the Claude adapter, never in the portable principle; a bare install (no such commands, no KB) performs the boundary by hand. This is the §13 "what frontier harnesses provide vs. what we build" line applied to session management — the framework names the behavior, the harness supplies the mechanism when present.

Invalidation: the harness gains durable per-feature session state that makes an explicit boundary marker redundant, or loses task-state such that git alone is insufficient (then reconsider a transient externalization — still not a canonical doc).

## Decision-8: dated-provenance-and-optional-refresh

Vendoring buys portability at the cost of drift from the source KB. Mitigation mirrors the KB's own discipline against SOTA: stamp each node with `source` + `last_refreshed` so staleness is visible by inspection (`INV-2`), and provide an optional regenerator.

`source: ce-kb:<slug>` is a human-readable provenance label, not a resolvable path; the actual source tree is `~/.local/share/context-engineering-knowledge-base/knowledge/<slug>.md` (the refresh script resolves there — note the real dir name, not the brief's `context-engineering-kb`).

`scripts/sync-ce` is deferred: it is refresh-time-only convenience, not load-bearing for any SPEC item, and the first vendoring is done by hand anyway. Building it now would be speculative. Ship the dated nodes; add the script when refresh frequency justifies it.

Invalidation: manual refresh proves error-prone or frequent enough that hand-sync drifts — then build `sync-ce`.
