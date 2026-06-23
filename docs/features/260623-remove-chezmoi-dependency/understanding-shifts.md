# 260623-remove-chezmoi-dependency — Understanding Shifts

## Delta-1: codex-front-door-removed

Current base installs Codex as stage-specific `leanplan-*` skills only; the prior design assumed a legacy `leanplan` front-door skill still existed.

The shift surfaced while merging `origin/main` during `T: V1`: base deleted `adapters/codex/leanplan/SKILL.md`, changed `install.sh` to remove the legacy front-door symlink, and updated adapter docs to describe Codex stage skills only.

Scope of impact: Design#D-1-readme-primary-path-is-direct-checkout.

## Delta-2: install-root-is-not-fixed

Removing the personal setup dependency also means removing the exact `~/.local/share/leanplan` checkout assumption from current guidance and runtime wrappers.

The prior plan treated that path as an acceptable convention, but the user's clarification made it part of the same dependency class: agents and hooks should resolve LeanPlan's references and scripts from the checkout they are installed from, not from a maintainer-specific home path.

Scope of impact: Requirements, Spec#B-5-install-root-is-user-selected, Spec#C-3-no-current-guidance-requires-fixed-checkout-path, Design#D-1-readme-primary-path-is-direct-checkout, Design#D-3-runtime-docs-use-normal-checkout-language, Design#D-6-adapters-and-hooks-resolve-from-their-installed-path, Tasks#T:D2, Tasks#T:V2.

## Delta-3: validator-allow-pattern-is-too-broad

Using `Bash(python3 */scripts/validate.py *)` removes the fixed checkout path but still grants Claude a broad validator-shaped command.

The validator should be a LeanPlan-specific executable so adapter allow-lists can target `*/scripts/leanplan-validate *` directly and avoid a generic `validate.py` filename.

Scope of impact: Design#D-6-adapters-and-hooks-resolve-from-their-installed-path, Tasks#T:D2.
