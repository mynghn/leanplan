# 260701-reference-doc-boundaries — Research

## Doc-boundary principles (context-engineering + skill-design KBs)

Distilled from the context-engineering, skill-design, and prompt-engineering knowledge bases; grounds the Spec's observable contract and the Design's boundary heuristics.
Evidence and principles only — the boundary decisions themselves live in `design.md` / `design-rationale.md`.

**Good-boundary properties (→ Spec contract):**

- Each unit is independently loadable and self-contained — an agent resolving one unit can act on the current occasion without pulling a sibling (context-engineering: jit-loading).
- Every concern lives in exactly one unit (no split = no under-fetch), and no unit bundles concerns with divergent occasion-profiles (no over-fetch) (skill-design: one-capability-granularity).
- Units are tiered by occasion frequency — a minimal always-loaded tier, an on-trigger tier, an on-demand tier — with the always-loaded tier carrying only near-universal content (skill-design: progressive-disclosure-token-economics).
- Every cross-unit reference is one hop and resolves to a real target — no nested chains, no dangling pointer (skill-design: directory-packaging).
- A unit over ~100 lines leads with a map so a partial read still sees full scope, and the occasion-relevant block is never buried mid-doc (context-engineering: lost-in-the-middle).
- The always-loaded set is ordered stable-to-volatile to form a cache-warm prefix (context-engineering: prefix-cache-economics).

**Boundary-decision heuristics (→ Design):**

- Boundary test = load-occasion profile: same when-to-fire groups into one unit (split into sections if what-to-read differs), different when-to-fire splits into separate units (skill-design: one-capability-granularity).
- A unit MAY serve many occasions when they share one trigger set — precedent: Anthropic's BigQuery skill keeps four reference files under one skill sharing one applicability condition and the loader pulls only the relevant file; validity stops at disjoint triggers (skill-design: one-capability-granularity).
- Tier by frequency: needed-every-moment goes always-loaded, needed-on-stage-entry goes load-on-entry, rare or heavy goes on-demand reference (skill-design: progressive-disclosure-token-economics; context-engineering: jit-loading).
- Default to JIT — hold an occasion→unit index of pointers and resolve to full content at need; the hybrid eagerly loads the small always-needed core and references the rest (context-engineering: jit-loading).
- Aggressively minimize the always-loaded set — it taxes every turn, so interrogate each block for whether it is needed at THIS occasion or can be pulled when the occasion arrives (context-engineering: context-as-working-set).

**Anti-patterns:**

- Over-fetch / distractor bundling — divergent-profile concerns co-located force near-relevant noise into every occasion's context, measurably lowering accuracy (context-engineering: distractor-sensitivity).
- Under-fetch — one concern split across units so an occasion must assemble several (skill-design: one-capability-granularity).
- Dangling / nested references — a concern behind a multi-hop chain causes partial reads; keep every reference one hop off the entry point (skill-design: directory-packaging).
- Buried block — a heavy topic-bundled doc places the occasion-relevant block mid-doc, where recall is weakest (context-engineering: lost-in-the-middle).
- Over-fragmentation — many ceremonial tiny units blur activation and add boundary overhead without benefit (skill-design: one-capability-granularity).
- Duplication / drift — copying a shared concern into several units creates copies that diverge; prefer one canonical home plus a named pointer (context-engineering: jit-loading).

**Tensions / judgment calls:**

- Progressive-disclosure granularity vs. tiny-file chasing — split only on a genuinely disjoint occasion-profile, never on topic alone (skill-design: one-capability-granularity).
- Prefix-cache stability vs. freshness — put durable material early in the always-loaded prefix and volatile material later, so edits don't invalidate the reused span (context-engineering: prefix-cache-economics).
- JIT leanness vs. preload speed — the hybrid (preload the hot core, reference the cold remainder) trades a little breadth for reliability (context-engineering: jit-loading).
- Self-containment vs. non-duplication — reconcile with one canonical home plus a one-level named reference, not a copy (skill-design: directory-packaging).

Prompt-engineering contributed no structural boundary principle; its only bearing is boundary hygiene — keep units self-contained, name references consistently, do not over-fragment (prompt-engineering: delimiters-and-structure).
