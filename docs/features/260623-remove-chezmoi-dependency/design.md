# 260623-remove-chezmoi-dependency — Design

## Architecture

Current LeanPlan guidance presents one primary checkout-based adoption path, then routes optional personal dotfile usage into a clearly labeled side path. Current runtime docs point back to the same checkout model; historical artifacts and fixtures remain classified rather than rewritten.

```mermaid
flowchart LR
    U[User] --> README[README primary install]
    README --> CLONE[~/.local/share/leanplan git checkout]
    CLONE --> INSTALL[install.sh adapter installer]
    INSTALL --> AGENTS[Claude and Codex skill registries]
    U --> UPDATE[README refresh guidance]
    UPDATE --> CLONE
    RUNTIME[scripts/README and framework-design runtime notes] --> CLONE
    README -. optional .-> DOTFILES[personal dotfile workflow note]
    HIST[fixtures and historical feature artifacts] -. classified .-> DOTFILES
```

## D-1: readme-primary-path-is-direct-checkout

`README.md` makes `git clone https://github.com/mynghn/leanplan.git ~/.local/share/leanplan` plus `~/.local/share/leanplan/install.sh` the primary install path, and makes `git -C ~/.local/share/leanplan pull --ff-only` the primary refresh path for the running tree. See rationale at [design-rationale.md#D-1-readme-primary-path-is-direct-checkout].

- Satisfies `Spec#B-1-primary-install-path-is-self-contained`, `Spec#B-2-refresh-path-is-self-contained`, and `Spec#C-1-no-current-guidance-requires-personal-dotfiles`.
- The README keeps the existing adapter registry targets: Claude Code at `~/.claude/skills/<name>` and Codex at `~/.agents/skills/{leanplan,leanplan-*}`.
- The README describes re-running `install.sh` after adapter-list changes as a harmless refresh of registry symlinks.

## D-2: installer-is-the-product-adapter-installer

`install.sh` is documented as LeanPlan's adapter installer, not as the non-personal-workflow alternative to another primary installer.

- Satisfies `Spec#B-1-primary-install-path-is-self-contained` and `Spec#C-1-no-current-guidance-requires-personal-dotfiles`.
- The script behavior stays unchanged: it links the checked-out `adapters/claude/*` and `adapters/codex/*` directories into the runtime skill registries, and `--uninstall` removes only those links.

## D-3: runtime-docs-use-normal-checkout-language

`scripts/README.md` and the opening source-of-truth note in `framework-design.md` describe `~/.local/share/leanplan` as a normal LeanPlan checkout that runtime adapters dereference.

- Satisfies `Spec#B-2-refresh-path-is-self-contained`, `Spec#B-3-plain-checkout-runtime-is-supported`, and `Spec#C-1-no-current-guidance-requires-personal-dotfiles`.
- `scripts/README.md` states that tools live under `~/.local/share/leanplan/scripts/` because the installed checkout provides them, not because a separate source tree applies them there.
- `framework-design.md` keeps `README.md` as the install source of truth and removes the personal-workflow wording from its first-line runtime summary.

## D-4: personal-workflow-is-an-optional-readme-note

Current README mentions the personal dotfile workflow only after the primary path, under an optional section for users who already manage local tools that way. See rationale at [design-rationale.md#D-4-personal-workflow-is-an-optional-readme-note].

- Satisfies `Spec#B-4-optional-personal-workflow-is-separated`, `Spec#C-1-no-current-guidance-requires-personal-dotfiles`, and `Spec#C-2-remaining-references-are-classified`.
- The optional note points back to the same runtime checkout and adapter targets rather than defining a second LeanPlan-owned install contract.

## D-5: historical-references-stay-archival

Existing `docs/features/**` and `fixtures/**` references to the personal workflow remain unchanged unless they become current guidance.

- Satisfies `Spec#C-2-remaining-references-are-classified`.
- The implementation verification treats `README.md`, `install.sh`, `scripts/README.md`, `framework-design.md`, and `adapters/README.md` as current guidance; old feature artifacts and fixtures are archival or test material.
