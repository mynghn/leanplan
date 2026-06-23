# 260623-remove-chezmoi-dependency — Understanding Shifts

## Delta-1: codex-front-door-removed

Current base installs Codex as stage-specific `leanplan-*` skills only; the prior design assumed a legacy `leanplan` front-door skill still existed.

The shift surfaced while merging `origin/main` during `T: V1`: base deleted `adapters/codex/leanplan/SKILL.md`, changed `install.sh` to remove the legacy front-door symlink, and updated adapter docs to describe Codex stage skills only.

Scope of impact: Design#D-1-readme-primary-path-is-direct-checkout.
