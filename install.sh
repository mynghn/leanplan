#!/usr/bin/env bash
# install.sh — LeanPlan adapter installer.
#
# Usage:
#   bash install.sh                       # install symlinks pointing at this repo's adapters/
#   bash install.sh --uninstall           # remove the LeanPlan symlinks
#
# Run from inside a checked-out LeanPlan repo. Creates symlinks from the runtime
# skill registries (~/.claude/skills/<name>, ~/.agents/skills/<name>) into
# this repo's adapters/ and utils/ subtrees.

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_SKILLS_DIR="$HOME/.claude/skills"
CODEX_SKILLS_DIR="$HOME/.agents/skills"

CLAUDE_SKILLS=(leanplan-frame leanplan-specify leanplan-design leanplan-tasks leanplan-implement leanplan-rethink leanplan-revise leanplan-validate)
CODEX_SKILLS=(leanplan-frame leanplan-specify leanplan-design leanplan-tasks leanplan-implement leanplan-rethink leanplan-revise leanplan-validate)
UTILITY_SKILLS=(leanplan-installation-freshness)

action="${1:-install}"

ensure_parent_dirs() {
    mkdir -p "$CLAUDE_SKILLS_DIR" "$CODEX_SKILLS_DIR"
}

remove_legacy_codex_front_door() {
    link="$CODEX_SKILLS_DIR/leanplan"
    if [ -L "$link" ] && [ "$(readlink "$link")" = "$REPO_DIR/adapters/codex/leanplan" ]; then
        rm "$link"
        echo "removed legacy $link"
    fi
}

install_symlinks() {
    ensure_parent_dirs
    remove_legacy_codex_front_door
    for s in "${CLAUDE_SKILLS[@]}"; do
        ln -sfn "$REPO_DIR/adapters/claude/$s" "$CLAUDE_SKILLS_DIR/$s"
        echo "linked $CLAUDE_SKILLS_DIR/$s -> $REPO_DIR/adapters/claude/$s"
    done
    for s in "${CODEX_SKILLS[@]}"; do
        ln -sfn "$REPO_DIR/adapters/codex/$s" "$CODEX_SKILLS_DIR/$s"
        echo "linked $CODEX_SKILLS_DIR/$s -> $REPO_DIR/adapters/codex/$s"
    done
    for s in "${UTILITY_SKILLS[@]}"; do
        ln -sfn "$REPO_DIR/utils/$s" "$CLAUDE_SKILLS_DIR/$s"
        echo "linked $CLAUDE_SKILLS_DIR/$s -> $REPO_DIR/utils/$s"
        ln -sfn "$REPO_DIR/utils/$s" "$CODEX_SKILLS_DIR/$s"
        echo "linked $CODEX_SKILLS_DIR/$s -> $REPO_DIR/utils/$s"
    done
}

uninstall_symlinks() {
    remove_legacy_codex_front_door
    for s in "${CLAUDE_SKILLS[@]}"; do
        link="$CLAUDE_SKILLS_DIR/$s"
        if [ -L "$link" ]; then
            rm "$link"
            echo "removed $link"
        fi
    done
    for s in "${CODEX_SKILLS[@]}"; do
        link="$CODEX_SKILLS_DIR/$s"
        if [ -L "$link" ]; then
            rm "$link"
            echo "removed $link"
        fi
    done
    for s in "${UTILITY_SKILLS[@]}"; do
        for link in "$CLAUDE_SKILLS_DIR/$s" "$CODEX_SKILLS_DIR/$s"; do
            if [ -L "$link" ]; then
                rm "$link"
                echo "removed $link"
            fi
        done
    done
}

case "$action" in
    install) install_symlinks ;;
    --uninstall|uninstall) uninstall_symlinks ;;
    *) echo "usage: $0 [install|--uninstall]" >&2; exit 2 ;;
esac
