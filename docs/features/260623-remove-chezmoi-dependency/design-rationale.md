# 260623-remove-chezmoi-dependency — Design Rationale

## D-1: readme-primary-path-is-direct-checkout

The direct checkout path is already present in README, and `install.sh` already does the adapter wiring. Promoting that path avoids inventing packaging while removing the hidden prerequisite from the top-level adoption story.

Rejected alternatives:

- Keep the personal workflow first and soften the wording. That still teaches new users that a private machine habit is the product-shaped path.
- Introduce a new package manager or bootstrap wrapper. That would solve the prerequisite by adding another one, while the existing clone-plus-installer path already covers the product need.
- Remove the `~/.local/share/leanplan` convention. The adapters and scripts already use that canonical location, and changing it would create avoidable churn unrelated to the dependency removal.

Invalidate this if LeanPlan later ships a real package distribution; at that point README's primary path should become that package, with the checkout path demoted.

## D-4: personal-workflow-is-an-optional-readme-note

Keeping a small optional note preserves a useful local workflow without letting it define LeanPlan's support boundary. The important distinction is reader position: a new adopter should never need it; an existing dotfile user can still map LeanPlan's checkout and adapter links into their own system.

Rejected alternatives:

- Delete every mention from current docs. That would make the product boundary clean, but it would also hide a known working integration pattern from users who already chose that tool.
- Keep the full template block. That repeats adapter target details in a second install contract and makes future adapter-list changes easy to miss in one path.

The optional note should be removed entirely if it starts drifting from the primary path or reintroduces required/recommended language.
