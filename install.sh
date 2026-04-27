#!/usr/bin/env bash
# install.sh — non-chezmoi installer for LeanPlan adapters.
#
# Usage:
#   bash install.sh                       # install symlinks pointing at this repo's adapters/
#   bash install.sh --uninstall           # remove the LeanPlan symlinks
#
# Run from inside a checked-out LeanPlan repo. Creates symlinks from the runtime
# skill registries (~/.claude/skills/<name>, ~/.agents/skills/leanplan) into
# this repo's adapters/ subtree. The chezmoi-managed equivalent is described in
# README.md.

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_SKILLS_DIR="$HOME/.claude/skills"
CODEX_SKILLS_DIR="$HOME/.agents/skills"

CLAUDE_SKILLS=(requirement specify design plan impl)

action="${1:-install}"

ensure_parent_dirs() {
    mkdir -p "$CLAUDE_SKILLS_DIR" "$CODEX_SKILLS_DIR"
}

install_symlinks() {
    ensure_parent_dirs
    for s in "${CLAUDE_SKILLS[@]}"; do
        ln -sfn "$REPO_DIR/adapters/claude/$s" "$CLAUDE_SKILLS_DIR/$s"
        echo "linked $CLAUDE_SKILLS_DIR/$s -> $REPO_DIR/adapters/claude/$s"
    done
    ln -sfn "$REPO_DIR/adapters/codex/leanplan" "$CODEX_SKILLS_DIR/leanplan"
    echo "linked $CODEX_SKILLS_DIR/leanplan -> $REPO_DIR/adapters/codex/leanplan"
}

uninstall_symlinks() {
    for s in "${CLAUDE_SKILLS[@]}"; do
        link="$CLAUDE_SKILLS_DIR/$s"
        if [ -L "$link" ]; then
            rm "$link"
            echo "removed $link"
        fi
    done
    link="$CODEX_SKILLS_DIR/leanplan"
    if [ -L "$link" ]; then
        rm "$link"
        echo "removed $link"
    fi
}

case "$action" in
    install) install_symlinks ;;
    --uninstall|uninstall) uninstall_symlinks ;;
    *) echo "usage: $0 [install|--uninstall]" >&2; exit 2 ;;
esac
