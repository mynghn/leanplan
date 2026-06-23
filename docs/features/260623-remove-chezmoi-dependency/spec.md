# 260623-remove-chezmoi-dependency — Spec

## Behavior

### B-1: primary-install-path-is-self-contained

When a new user follows the primary install guidance from a fresh local environment, the guidance presents a complete LeanPlan-owned path to installed agent adapters without requiring a personal dotfile manager.

### B-2: refresh-path-is-self-contained

When an installed user needs to update LeanPlan, current guidance presents a complete LeanPlan-owned refresh path for the running LeanPlan copy without requiring a personal dotfile manager.

### B-3: plain-checkout-runtime-is-supported

When a maintainer or contributor reads runtime guidance, the running LeanPlan tree is described as a normal local checkout that can be edited, updated, and validated without personal dotfile infrastructure.

### B-4: optional-personal-workflow-is-separated

When current user-facing docs mention a personal dotfile workflow, the mention is separated from the primary path and labeled as optional or existing-user-specific.

### B-5: install-root-is-user-selected

When a user installs LeanPlan from a checkout they choose, current guidance and installed runtime adapters resolve LeanPlan references and scripts from that checkout instead of an exact home-relative path.

## Constraint

### C-1: no-current-guidance-requires-personal-dotfiles

Across current install, update, adapter, and runtime guidance, no normal-use instruction requires, recommends, or assumes a personal dotfile manager as the LeanPlan product path.

### C-2: remaining-references-are-classified

Remaining personal-dotfile references stay confined to optional guidance, historical feature artifacts, fixtures, or upstream context, so readers can distinguish current support from old examples.

### C-3: no-current-guidance-requires-fixed-checkout-path

Across current install, update, adapter, hook, and runtime guidance, no normal-use instruction requires or assumes an exact LeanPlan checkout location.

## Non-goals

- Removing support for users who choose to manage LeanPlan through their own dotfile workflow.
- Rewriting old feature artifacts or fixtures solely because they describe the prior workflow.
- Changing LeanPlan's stage model, artifact contract, or supported agent runtimes.
- Providing package-manager installation.
