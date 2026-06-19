# 260619-context-engineering-knowledges-grounding — RESEARCH

Evidence only. Interpretations live in DESIGN RATIONALE. Gathered 2026-06-19 via a cold audit (LeanPlan internals + the then-14 KB entries; two breadth-heavy scans run in isolated sub-agents, conclusions distilled here). Re-measured 2026-06-20 at vendoring — the KB had grown to 15 (see CE knowledge base below).

## CE knowledge base — structure and edge graph

Source: `~/.local/share/context-engineering-knowledge-base/` (skill copy at `~/.claude/skills/context-engineering-knowledge-base`). NOT `~/.local/share/context-engineering-kb/` (that path does not exist).

- 15 entries + `INDEX.md` (14 at the 2026-06-19 audit; `explore-execute-boundary` was added to the KB after the audit — see closure note below). Slugs: `attention-sinks`, `compaction-vs-eviction`, `context-as-working-set`, `context-isolation`, `context-rot`, `distractor-sensitivity`, `effective-vs-advertised-context`, `explore-execute-boundary`, `explore-then-compact-handoff`, `jit-loading`, `literal-vs-latent-matching`, `lost-in-the-middle`, `prefix-cache-economics`, `structured-note-taking`, `three-axes-of-context-degradation`.
- Entry frontmatter fields: `name`, `description`, `last_refreshed` (ISO date; all 15 dated 2026-06-19), `sources` (list of `title — author/venue — URL`). Body carries `Related: [[slug]]` edges. `INDEX.md` has no frontmatter (heading + `- [slug](knowledge/slug.md) — desc` bullets).
- `three-axes-of-context-degradation` is an index over three axes: **position** (`lost-in-the-middle`, `attention-sinks`), **length** (`context-rot`, `effective-vs-advertised-context`), **noise** (`distractor-sensitivity`, `literal-vs-latent-matching`).
- Edge-graph closure: the transitive closure over `Related` edges from the concepts this feature cites reaches **all 15** entries. `three-axes-of-context-degradation` links all six axis members; `compaction-vs-eviction` links `effective-vs-advertised-context` + `prefix-cache-economics`; `explore-then-compact-handoff` links `explore-execute-boundary` (its temporal sibling). No proper subset of the 15 is link-closed. (Re-measured 2026-06-20 at vendoring: the 2026-06-19 audit counted 14; `explore-execute-boundary` was added to the KB afterward and `explore-then-compact-handoff` gained an edge to it, extending the closure by one. `explore-execute-boundary`'s own edges all resolve in-set, so 15 is closed. Per `DESIGN#Decision-1` invalidation trigger — "the KB's concept set changes shape" — the full closure is vendored.)

## Principle → concept mapping (verified)

Verified against `references/*.md`, `leanplan.md`, the adapter SKILLs, and the 15 entries.

- JIT loading (philosophy P1; `leanplan.md` §1.2 / §4) → `jit-loading`.
- No flat task scripting (philosophy P2; `leanplan.md` §1.3) → `jit-loading`, `distractor-sensitivity`, `context-rot`. A frozen step-by-step script rots against current code into a stale distractor; re-deriving at task entry JIT-loads current reality.
- Small surface / attention discipline (philosophy P3; §6 prose rule) → `lost-in-the-middle`, `distractor-sensitivity`.
- Archive verbose reasoning (philosophy P4; §4 surface/archive) → `jit-loading`, `context-as-working-set`.
- Persist-by-migration-to-code (philosophy P7; §10) → `structured-note-taking`.
- Isolation (not yet present) → `context-isolation`, `explore-then-compact-handoff`.
- Stable→volatile load order (not yet present) → `prefix-cache-economics` (entry states "order stable-to-volatile").
- Edge-placement in long artifacts (not yet present) → `lost-in-the-middle`. The "~100-line" trigger is a LeanPlan-local heuristic (reuses the §6 ToC>100 threshold); the concept itself states no line cutoff.
- Session-boundary discipline (not yet present) → `explore-execute-boundary` (the temporal explore→execute / plan→impl boundary — primary), `compaction-vs-eviction`, `explore-then-compact-handoff`, `context-isolation`; "warm session" also traces to `prefix-cache-economics`.

## Self-conformance gaps (measured)

- JIT self-violation: every stage adapter SKILL eager-loads `philosophy.md` (23 lines) + `artifact-contract.md` (126) + `<stage>.md` before acting. `impl` = 23 + 126 + 98 = **247 lines** loaded up front, while `impl.md` itself prescribes JIT-loading of artifact anchors. Sharpest case: `artifact-contract.md` (126 lines) loads at every stage even when structure is not being edited.
- Isolation: `Agent` is in the `design` and `impl` adapter `allowed-tools`, absent from `specify` (the REQ→SPEC research edge); `requirement`/`plan` lack it too. No stage reference prescribes isolating breadth-heavy investigation into a sub-agent that returns only the distilled artifact.
- Prefix-cache ordering: no stable→volatile load-order rule in `leanplan.md` §6 or in adapter authoring guidance.
- Edge-placement: §6 has a ToC>100-line rule only; no rule re-anchors critical invariants near a long artifact's tail or orders high-stakes DAG cards at the edges.
- Session-boundary: absent as a principle. §14 notes cross-session continuity is handled by harness + git, with no artifact planned.

## Portability + tooling baseline (current)

- LeanPlan references the CE knowledge base **zero** times today; skills load only `~/.local/share/leanplan/references/*`. The shipped framework already runs standalone.
- `install.sh` only symlinks `adapters/{claude/*, codex/leanplan}` into the runtime skill registries; it does not enumerate `references/`. Files added under `references/` ship via the git tree (chezmoi external clone / `git clone`), so no `install.sh` change is needed to ship new references.
- `validate.py` validates one feature dir under `docs/features/<KEY>` (`SURFACE_FILES` = requirement/spec/design/plan; optional rationale/research). It never reads `references/`. Its "frontmatter discouraged" check is scoped to those feature files. Records under `references/` are invisible to it and may carry provenance frontmatter without tripping it.
- Skills resolve via symlink to the installed copy `~/.local/share/leanplan/`; repo edits to the framework take effect for running skills only after reinstall / `chezmoi update`.

## Principle 7 scope

- P6/P7 (plan docs transient; no living canonical specs) and the no-frontmatter rule both scope to per-feature plan docs under `docs/features/`. `references/` holds permanent framework docs, not per-feature plan artifacts — corroborated by the validator scoping above.
