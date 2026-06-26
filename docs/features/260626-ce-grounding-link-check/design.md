# 260626-ce-grounding-link-check — Design

## Architecture

```mermaid
flowchart TD
    RUN["maintainer runs leanplan-ce-grounding-link-check (on demand, after a Metacognition update)"]
    RUN --> SKILL["SKILL.md — read-first, report-only; runs check.sh, shows verdict"]
    SKILL --> CHECK["check.sh — read-only"]
    CHECK --> ENUM["enumerate LeanPlan grounded slugs — context-engineering hooks + map links"]
    CHECK --> REACH{"live source INDEX reachable? (override env, else conventional vault path)"}
    REACH -->|no| ABSENT["report: source absent — expected gloss fallback — B-2, exit 0"]
    REACH -->|yes| DIFF["diff grounded slugs vs the INDEX slug-registry — names only, never bodies"]
    DIFF --> REPORT["report dangling = grounded slug not in source, with referencing files; clean if none — B-1; advisory exit 0, --strict nonzero"]
    REPORT --> FIX["dangling? maintainer repairs via /leanplan-revise — C-1 report-only, human-gated"]
```

The inspection is a read-only utility skill: `check.sh` enumerates the slugs LeanPlan grounds in, compares them against the live source's INDEX slug-registry when reachable, and reports dangling references; the source's absence is a distinct, non-error outcome. It mutates nothing — repairs flow through `/leanplan-revise` (`Spec#C-1-report-only-no-mutation`).

## D-1: realize-as-utility-skill-with-check-script
Build it as a utility skill `leanplan-ce-grounding-link-check` under `utils/` — a `SKILL.md` (read-first, report-only) over a deterministic `check.sh` — mirroring `leanplan-installation-freshness`, and install it via `install.sh`'s `UTILITY_SKILLS` (both Claude and Codex registries). Realizes the on-demand, report-only shape of `Spec#C-1-report-only-no-mutation`. See rationale at [design-rationale.md#D-1-realize-as-utility-skill-with-check-script].
- `SKILL.md` resolves `<LEANPLAN_ROOT>` from the installed symlink (walk up two from `utils/<name>/`), runs `check.sh`, shows the verdict, and — only when dangling is found — points the maintainer at `/leanplan-revise` to repair. It is not a planning-stage skill; it owns only grounding-link validity.

## D-2: check-algorithm-and-advisory-posture
`check.sh` is read-only and deterministic: (1) enumerate LeanPlan's grounded slug set — the union of `(context-engineering: <slug>)` hook slugs across `references/`, `framework-design.md`, `adapters/`, and the map's `[[<slug>]]` links; (2) resolve the live source INDEX (D-3); (3) when reachable, report every grounded slug absent from the source as **dangling**, each with the files that reference it, and report clean when none; when unreachable, report the distinct source-absent outcome. Realizes `Spec#B-1-dangling-grounding-is-reported`, `Spec#B-2-source-absent-is-reported-distinctly`. See rationale at [design-rationale.md#D-2-check-algorithm-and-advisory-posture].
- **Advisory by default** — clean, source-absent, and dangling-found all exit 0 (report only); a `--strict` flag exits nonzero on dangling for CI gating. Mirrors `leanplan-validate` / `scan-leaks` (warn by default, strict to block).
- The grounded-slug enumeration is the same logic proven runnable by hand against the live INDEX (15/15 clean today); `check.sh` only encodes it.

## D-3: source-access-via-index-registry-located-by-convention
The check reaches the live source through its **INDEX slug-registry** — the same source-of-truth the `context-engineering-knowledge-base` skill itself reads — never the concept bodies, located by `$LEANPLAN_CE_SOURCE_INDEX` override, else the conventional Metacognition vault INDEX path (`~/.local/share/metacognition-vault/context-engineering/INDEX.md`), else treated as absent. Realizes `Spec#C-2-reference-only-not-semantic` and the reachability half of `Spec#C-3-self-contained-run`. See rationale at [design-rationale.md#D-3-source-access-via-index-registry-located-by-convention].
- **Reference-only, concretely** — it extracts only each INDEX line's `<slug>` (the name registry); it never opens `knowledge/<slug>.md`, and it ignores the `⚠`-degraded marker entirely — a flagged-but-present slug still resolves, so it yields no finding (`Spec#C-2`).
- **Self-contained** — enumerating LeanPlan's grounded slugs needs nothing external; only the diff needs the source, and its absence is the B-2 outcome, never a run failure (`Spec#C-3`).
- Guards the post-`260626-live-ce-grounding` grounding model; the slug enumeration works against the map either way, so the skill is buildable independently of that feature's merge (it only becomes *load-bearing* once the deep layer is live).
