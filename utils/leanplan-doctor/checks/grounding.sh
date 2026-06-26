#!/usr/bin/env bash
# leanplan-doctor / grounding — read-only inspection that reports whether
# LeanPlan's context-engineering grounding references still resolve against the
# live Metacognition source. Reference-only and report-only: it reads slug NAMES
# (LeanPlan's grounding hooks + map links, and the source INDEX's slug registry),
# never concept bodies, and mutates nothing. Semantic correctness is
# Metacognition's; this only verifies the names still resolve.
set -uo pipefail

# --- args ---------------------------------------------------------------------
STRICT=0
for arg in "$@"; do
  case "$arg" in
    --strict) STRICT=1 ;;
    -h|--help)
      echo "usage: grounding.sh [--strict]"
      echo "  reports CE grounding slugs that no longer resolve in the live source."
      echo "  advisory exit 0 by default; --strict exits nonzero when dangling."
      exit 0 ;;
    *) echo "unknown arg: $arg" >&2; exit 2 ;;
  esac
done

# --- LeanPlan root ------------------------------------------------------------
# This script lives at utils/leanplan-doctor/checks/grounding.sh — walk up three.
# `pwd -P` is load-bearing: the script is installed as a symlink, so a logical
# pwd would walk up the symlink's location (e.g. ~/.claude/skills) instead of the
# real checkout. Resolve the physical path first, then walk up.
if [ -n "${LEANPLAN_ROOT:-}" ]; then
  ROOT="$LEANPLAN_ROOT"
else
  CHECK_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
  ROOT="$(cd "$CHECK_DIR/../../.." && pwd -P)"
fi

MAP="$ROOT/references/context-engineering.md"

# --- enumeration --------------------------------------------------------------
# Scope: `(context-engineering: <slug>)` hook slugs across references/,
# framework-design.md, and adapters/; plus the map's `[[<slug>]]` links, harvested
# from the map file only. The slug-shape filter (^[a-z0-9-]+$) is load-bearing —
# it drops the documentation placeholders `<slug>` and `…` that appear in the
# hook/link FORMAT examples, so only real concept names count as grounded.

list_scope_files() {
  [ -f "$ROOT/framework-design.md" ] && printf '%s\n' "$ROOT/framework-design.md"
  for d in "$ROOT/references" "$ROOT/adapters"; do
    [ -d "$d" ] && find "$d" -type f -name '*.md'
  done
}

# Grounded slugs referenced by a single file. Hooks count everywhere in scope;
# [[slug]] links count only in the map. Reuse this for both the global set and
# the per-slug "referenced by" report so the two cannot drift.
slugs_in_file() {
  local f="$1"
  {
    grep -hoE '\(context-engineering: [a-z0-9, -]+\)' "$f" 2>/dev/null \
      | sed -E 's/^\(context-engineering: //; s/\)$//' | tr ',' '\n'
    if [ "$f" = "$MAP" ]; then
      grep -hoE '\[\[[a-z0-9-]+\]\]' "$f" 2>/dev/null | sed -E 's/^\[\[//; s/\]\]$//'
    fi
  } | sed -E 's/^[[:space:]]+//; s/[[:space:]]+$//' | grep -E '^[a-z0-9-]+$'
}

grounded_slugs() {
  list_scope_files | while IFS= read -r f; do slugs_in_file "$f"; done | sort -u
}

referencing_files() {
  # files (ROOT-relative) whose grounded-slug set includes $1
  local slug="$1" f
  list_scope_files | while IFS= read -r f; do
    if slugs_in_file "$f" | grep -qxF "$slug"; then
      printf '%s\n' "${f#"$ROOT"/}"
    fi
  done
}

# --- source INDEX resolution --------------------------------------------------
# Override, else conventional Metacognition vault path, else treated as absent.
# Absent is the expected gloss-fallback outcome, never an error: enumerating
# LeanPlan's own grounded slugs needs nothing external; only the diff needs the
# source, so its absence is a distinct outcome, never a failure to run.
if [ -n "${LEANPLAN_CE_SOURCE_INDEX:-}" ]; then
  INDEX="$LEANPLAN_CE_SOURCE_INDEX"
else
  INDEX="$HOME/.local/share/metacognition-vault/context-engineering/INDEX.md"
fi

# Slug NAMES only, from each INDEX line's `[<slug>](knowledge/<slug>.md)` link.
# Tolerant of a leading `⚠ ` degraded marker and never opens knowledge/<slug>.md:
# the verdict turns only on whether a name resolves, never on a concept's content
# or health — a flagged-but-present slug still resolves, so it yields no finding.
index_slugs() {
  grep -oE '\[[a-z0-9-]+\]\(knowledge/' "$INDEX" 2>/dev/null \
    | sed -E 's/^\[//; s/\]\(knowledge\/$//' | sort -u
}

# --- report -------------------------------------------------------------------
echo "== leanplan-doctor / CE grounding links ================================"

grounded="$(grounded_slugs)"
n_grounded="$(printf '%s\n' "$grounded" | grep -c . || true)"

# A real LeanPlan checkout always carries grounding hooks. Enumerating zero means
# the root is wrong or the checkout is broken — a misconfiguration, never a clean
# result. Fail loudly (exit 2) rather than silently report "all 0 slugs resolve".
if [ "$n_grounded" -eq 0 ]; then
  printf '[grounded] **  no grounding hooks found under %s\n' "$ROOT"
  echo "               0 grounded slugs enumerated — wrong LeanPlan root or a broken"
  echo "               checkout, not a clean result. Set \$LEANPLAN_ROOT, or run via the"
  echo "               resolved skill path."
  echo "========================================================================"
  exit 2
fi

if [ ! -f "$INDEX" ]; then
  printf '[source ]  n/a  source absent — expected gloss fallback (looked for %s)\n' "$INDEX"
  printf '[grounded] %s grounded slug(s) enumerated; diff skipped — source needed only to find dangling\n' "$n_grounded"
  echo "========================================================================"
  echo "Map gloss is the local floor while the source is absent. Nothing to fix."
  exit 0
fi

source_slugs="$(index_slugs)"
n_source="$(printf '%s\n' "$source_slugs" | grep -c . || true)"
dangling="$(comm -23 <(printf '%s\n' "$grounded") <(printf '%s\n' "$source_slugs"))"

printf '[source ]  ok  %s (%s slug(s))\n' "$INDEX" "$n_source"

if [ -z "$dangling" ]; then
  printf '[links  ]  ok  all %s grounded slug(s) resolve in the live source\n' "$n_grounded"
  echo "========================================================================"
  exit 0
fi

n_dangling="$(printf '%s\n' "$dangling" | grep -c . || true)"
printf '[links  ]  **  %s grounded slug(s) no longer resolve in the live source (dangling):\n' "$n_dangling"
printf '%s\n' "$dangling" | while IFS= read -r slug; do
  [ -n "$slug" ] || continue
  refs="$(referencing_files "$slug" | awk 'NR>1{printf ", "} {printf "%s", $0} END{if (NR) print ""}')"
  printf '            - %s\n                referenced by: %s\n' "$slug" "$refs"
done
echo "========================================================================"
echo "Repair via /leanplan-revise — re-ground or retire each dangling reference."
echo "This inspection is report-only; it edits no grounding."

[ "$STRICT" = 1 ] && exit 1
exit 0
