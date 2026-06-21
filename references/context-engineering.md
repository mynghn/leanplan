# Context-Engineering Grounding — name → node map

LeanPlan's load-bearing rules each name the context-engineering concept they implement, as a `(context-engineering: <slug>)` hook. This file resolves every such name to its vendored node and records which rule rests on it; the node carries the definition, sources, and `Related` edges. Load it only when a hook is challenged — it sits off the default hot path. Links: `[[<slug>]]` resolves to `context-engineering/<slug>.md`.

Everything here defends one thing — a lean, high-signal working set against the three axes of context degradation ([[three-axes-of-context-degradation]]). The axes are the *why*; the rules below are the *how*.

## The three degradation axes

- **Position** — recall depends on *where* a fact sits, not just whether it is present: [[lost-in-the-middle]], [[attention-sinks]].
- **Length** — accuracy decays as the input grows, even on easy tasks: [[context-rot]], [[effective-vs-advertised-context]].
- **Noise** — irrelevant content drags accuracy down: [[distractor-sensitivity]], [[literal-vs-latent-matching]].

## Grounded rules → concept

Each load-bearing rule, by where it lives, and the concept(s) its `(context-engineering: …)` hook names:

- **JIT-load intent + current code; lazy-load references** — philosophy P1; `framework-design.md` §1.2 / §4; stage adapters → [[jit-loading]]. Carry pointers, resolve to content at the moment of need.
- **No flat task scripting; re-derive at task entry** — philosophy P2; `framework-design.md` §1.3 → [[jit-loading]], [[distractor-sensitivity]]. A frozen step-by-step script rots against current code into a stale distractor; re-deriving JIT-loads current reality. Applied **reflexively**: the stage procedures in the skill references are themselves a default flow + load-bearing gates, not a rigid script (each reference's Procedure says so).
- **Archive verbose reasoning; keep the surface lean** — philosophy P4; §4 surface/archive → [[jit-loading]], [[context-as-working-set]]. The window is finite working memory, not a free buffer.
- **Small surface / attention discipline** — philosophy P3; §6 prose rule → [[lost-in-the-middle]], [[distractor-sensitivity]]. A short, high-signal surface evades the position and noise penalties.
- **Surface budget (advisory caps + lossless archive)** — `framework-design.md` §6; `artifact-contract.md` → Surface Budget; `validate.py` → [[context-rot]], [[effective-vs-advertised-context]], [[distractor-sensitivity]]. The instrumented form of small-surface: accuracy decays as the review surface grows, so cap it (advisory backstop) and push depth to the archives — which is lossless because the archive stays JIT-loadable.
- **Edge-placement in long artifacts** — `framework-design.md` §6, past the >100-line ToC threshold → [[lost-in-the-middle]]. Re-anchor critical invariants near the tail; order high-stakes DAG cards at the edges.
- **Stable→volatile load order** — `framework-design.md` §6 cross-cutting rule + adapter-authoring note → [[prefix-cache-economics]]. Order the prompt so the durable prefix stays cache-warm.
- **Grep-friendly anchored headings (ID+slug)** — `framework-design.md` §6; §8 / §9 → [[jit-loading]], [[literal-vs-latent-matching]]. The anchor is the lightweight pointer JIT resolves to full content; the grep-able exact slug is a literal lexical handle, not a latent-inference lookup.
- **One prose home per fact (de-dup to anchors)** — `artifact-contract.md` → One Prose Home Per Fact; per-seam instances in the stage docs → [[distractor-sensitivity]], [[literal-vs-latent-matching]]. A fact is authored as prose once; every other mention is a bare anchor. Each restatement avoided is a near-miss distractor removed, and the surviving anchor is a literal handle, not a latent lookup.
- **Persist by migration to durable code forms** — philosophy P7; §10 → [[structured-note-taking]]. Migrate WHYs into types / tests / commits, not living plan docs.
- **Isolate breadth-heavy investigation** — `specify.md` / `design.md` / `impl.md` (wide research / code scans), and `plan.md` (the bidirectional-verification sweep on large features) → [[context-isolation]], [[explore-then-compact-handoff]]. Fan wide reading into a sub-agent that returns only the distilled artifact or gap list.
- **Session-boundary discipline** — philosophy + `framework-design.md` §1; §13 harness note → [[explore-execute-boundary]], [[compaction-vs-eviction]], [[explore-then-compact-handoff]], [[context-isolation]]. Keep the planning spine warm in one session; hard-cut to a fresh frame at plan→impl. The "warm session" half also rests on [[prefix-cache-economics]].
