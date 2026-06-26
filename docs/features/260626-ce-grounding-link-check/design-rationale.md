# 260626-ce-grounding-link-check — Design Rationale

## D-1: realize-as-utility-skill-with-check-script

Forces: an on-demand, read-first, report-only inspection that installs across both runtimes and is triggered by a *Metacognition* update (not a LeanPlan one).

Chosen: mirror `leanplan-installation-freshness` — a `utils/<name>/` skill bundling its own `check.sh`, installed via `install.sh`'s `UTILITY_SKILLS` (which symlinks into both `~/.claude` and `~/.agents`). That sibling is the same *kind* of thing (a maintenance/freshness inspection the user runs on demand), so reusing its shape keeps the surface predictable.

Alternatives:
- **A bare script under `scripts/`** (like `scan-leaks` / `leanplan-validate`) — rejected as the *home*: `scripts/` holds the planning-pipeline tooling the stage skills call; a standalone maintenance inspection the user invokes directly belongs in `utils/` beside its sibling. (`check.sh` still does the work — this is only about where it lives and how it's surfaced.)
- **Fold into `leanplan-installation-freshness`** — rejected: that skill owns the *install* surface (checkout git-freshness + symlink parity); grounding-link integrity is a different concern against a different external (the live source), with a different trigger. One responsibility per skill.

Invalidation: utility-skill packaging or the `UTILITY_SKILLS` install path changes (then follow the sibling's new shape).

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
