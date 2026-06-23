#!/usr/bin/env bash
# leanplan-installation-freshness — read-only freshness + validity of a LeanPlan
# checkout and its installed skill symlinks.
set -uo pipefail

if [ -n "${LEANPLAN_ROOT:-}" ]; then
  ROOT="$LEANPLAN_ROOT"
else
  UTIL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
  ROOT="$(cd "$UTIL_DIR/../.." && pwd)"
fi

sync_state() {
  local repo="$1" br up d
  [ -n "$(git -C "$repo" status --porcelain 2>/dev/null)" ] && d=dirty || d=clean
  br="$(git -C "$repo" symbolic-ref --short HEAD 2>/dev/null || echo HEAD)"
  git -C "$repo" fetch -q origin 2>/dev/null || true
  up="origin/$br"
  git -C "$repo" rev-parse --verify -q "$up" >/dev/null 2>&1 || up="origin/HEAD"
  printf '%s behind=%s ahead=%s' "$d" \
    "$(git -C "$repo" rev-list --count "HEAD..$up" 2>/dev/null || echo '?')" \
    "$(git -C "$repo" rev-list --count "$up..HEAD" 2>/dev/null || echo '?')"
}

flag() {
  case "$1" in
    *behind=0*) printf '  ok ' ;;
    *behind=\?*) printf ' n/a ' ;;
    *) printf ' ** ' ;;
  esac
}

check_link() {
  local link="$1" target="$2" label="$3" actual
  if [ -L "$link" ]; then
    actual="$(readlink "$link")"
    if [ "$actual" = "$target" ]; then
      return 0
    fi
    echo "[skills ] ** $label stale: $link -> $actual (expected $target)"
  else
    echo "[skills ] ** $label missing: $link -> $target"
  fi
  return 1
}

is_git_repo() {
  git -C "$1" rev-parse --is-inside-work-tree >/dev/null 2>&1
}

echo "== leanplan-installation-freshness ====================================="
if is_git_repo "$ROOT"; then
  state="$(sync_state "$ROOT")"
  printf '[repo   ]%s %s  (%s)\n' "$(flag "$state")" "$state" "$ROOT"
else
  printf '[repo   ]  n/a  not a git checkout at %s\n' "$ROOT"
fi

missing=0
for adapter in "$ROOT"/adapters/claude/*; do
  [ -d "$adapter" ] && [ -f "$adapter/SKILL.md" ] || continue
  name="${adapter##*/}"
  check_link "$HOME/.claude/skills/$name" "$adapter" "Claude adapter $name" || missing=1
done
for adapter in "$ROOT"/adapters/codex/*; do
  [ -d "$adapter" ] && [ -f "$adapter/SKILL.md" ] || continue
  name="${adapter##*/}"
  check_link "$HOME/.agents/skills/$name" "$adapter" "Codex adapter $name" || missing=1
done
for util in "$ROOT"/utils/*; do
  [ -d "$util" ] && [ -f "$util/SKILL.md" ] || continue
  name="${util##*/}"
  check_link "$HOME/.claude/skills/$name" "$util" "Claude utility $name" || missing=1
  check_link "$HOME/.agents/skills/$name" "$util" "Codex utility $name" || missing=1
done

[ "$missing" = 0 ] && echo "[skills ]  ok  installed Claude + Codex skill symlinks match authored sources"

echo "========================================================================"
echo "Fix (after review, only if flagged **):"
echo "  git -C $ROOT pull --ff-only \\"
echo "    && $ROOT/install.sh"
