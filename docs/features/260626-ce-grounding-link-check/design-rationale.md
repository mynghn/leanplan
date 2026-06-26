# 260626-ce-grounding-link-check — Design Rationale

## D-1: realize-as-utility-skill-with-check-script

Forces: an on-demand, read-first, report-only inspection that installs across both runtimes and is triggered by a *Metacognition* update. It shares that exact shape with the pre-existing `leanplan-installation-freshness` maintenance check.

Chosen: package it as one diagnostic inside a `leanplan-doctor` utility skill — a single `SKILL.md` over two check scripts (freshness + grounding) presented as labeled sections — which **absorbs** `leanplan-installation-freshness` (retired) into one "is my LeanPlan healthy?" command. Both are the same kind of on-demand, read-first, report-only check, so a single health command beats two near-identical sibling skills, and "installation freshness" was too narrow a home. Each section keeps its own fix route — freshness self-heals (`git pull` + reinstall after confirm), grounding routes to `/leanplan-revise` — so doctor's report-first posture preserves the grounding check's report-only contract (`Spec#C-1-report-only-no-mutation`): the grounding section simply has no auto-fix. Reverses the original separate-skill decision per `UnderstandingShifts#Delta-1-package-as-doctor-umbrella-absorbing-freshness`.

Alternatives:
- **A bare script under `scripts/`** (like `scan-leaks` / `leanplan-validate`) — rejected as the *home*: `scripts/` holds the planning-pipeline tooling the stage skills call; a maintenance inspection the user invokes directly belongs in `utils/`. (The check scripts still do the work — this is only about where they live and how they're surfaced.)
- **A separate `leanplan-ce-grounding-link-check` sibling skill** (the original choice, mirroring freshness on "one responsibility per skill", which had rejected folding) — **reversed**: two sibling skills with the same shape and overlapping "run a health check" intent fragment the surface; one doctor with labeled sections is leaner and the single obvious entry point. The distinct-concern argument that first favored separation survives *inside* doctor — two sections with distinct externals (git origin vs the live source), triggers, and fix routes — rather than as two skills.

Invalidation: the two diagnostics diverge enough in trigger or audience that a combined report adds noise rather than convenience (re-split into focused skills), or utility-skill packaging / the `UTILITY_SKILLS` install path changes.

## D-2: check-algorithm-and-advisory-posture

Forces: report dangling grounding (`B-1`), distinguish a missing source from a missing slug (`B-2`), and do it in the framework's established **advisory** posture — issue #27 asked for "warn by default, strict to block, mirroring `leanplan-validate` / `scan-leaks`."

Chosen: a deterministic enumerate → diff → report script. Default exit 0 for clean, source-absent, *and* dangling-found (it is a report, not a gate); `--strict` exits nonzero on dangling for opt-in CI gating.

Alternatives:
- **Agent-driven resolution via the KB skill, no script** — rejected: the sibling pattern and the CI-advisory value both favor a deterministic script, and the source slug list is just the INDEX, readable directly without driving a harness skill.
- **Block (nonzero) by default** — rejected: a dangling reference is a maintainer-judgment repair (via `/leanplan-revise`), not a hard stop; defaulting to advisory matches the rest of the framework's tooling and avoids wedging unrelated commits.

Invalidation: dangling grounding proves frequent enough to warrant blocking by default (flip the default, or wire `--strict` into the pre-commit advisory).

## D-3: source-access-via-index-registry-located-by-convention

Forces: stay reference-only (`C-2`), stay self-contained (`C-3`), and honor the parent feature's principle — don't hardcode a brittle path; dogfood the source's own source-of-truth.

The tension this resolves: `260626`'s `D-2` chose "resolve via the *skill*, not a path" for the agent-facing map. A **script** consumer can't invoke a harness skill, so it needs a concrete location. Resolution: read the **INDEX** — the very registry the `context-engineering-knowledge-base` skill itself reads — located by `$LEANPLAN_CE_SOURCE_INDEX` override → conventional vault path → absent. Different consumer (script vs. agent), same source-of-truth (the INDEX), no single brittle literal.

Reading only the INDEX *slug names* — never `knowledge/<slug>.md` bodies, and ignoring the `⚠`-degraded marker — is what makes the check reference-only in fact, not just in intent: a reworded or flagged-but-present concept still appears in the registry, so it resolves and yields no finding. Semantic correctness stays Metacognition's, exactly the scope boundary the feature exists to hold.

Alternatives:
- **Hardcode one vault path, no override** — rejected: brittle (the parent's own concern); the override keeps it relocatable and testable.
- **Read concept bodies to also flag semantic drift** — rejected: violates `C-2` and re-imports the responsibility this feature deliberately leaves upstream.

Invalidation: the source stops exposing a flat INDEX slug-registry (re-point the enumeration), or the conventional path moves with no override set — in which case the check honestly reports source-absent, surfacing the staleness rather than hiding it.
