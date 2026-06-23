# 260623-remove-chezmoi-dependency — LeanPlan is usable without a personal dotfile manager

## Problem

LeanPlan still presents and describes a personal dotfile workflow as the recommended or assumed way to install, refresh, and reason about the running framework. That makes an unrelated personal setup feel like part of LeanPlan itself.

The pain is practical:

- **New users face an avoidable prerequisite** — someone evaluating LeanPlan must understand a separate personal configuration tool before they can tell how LeanPlan is meant to be installed.
- **Maintainers inherit unclear delivery language** — current docs mix LeanPlan-owned installation with a maintainer's personal refresh workflow, so it is harder to describe what is product behavior and what is only one user's setup.
- **Runtime guidance looks environment-specific** — runtime docs imply the running copy is managed through that personal workflow, which weakens confidence that LeanPlan works in a plain checkout.

## Outcome

LeanPlan's installation, update, and runtime guidance are self-contained. A user can adopt and maintain LeanPlan from LeanPlan-owned instructions alone, while people who already use a personal dotfile workflow can keep doing so as an optional local preference.

User stories:

- **New adopters start directly** — a new user can follow the primary install path without learning or configuring a personal dotfile manager first.
- **Maintainers explain one product path** — a maintainer can describe how LeanPlan is installed, refreshed, and wired into supported agent runtimes using LeanPlan's own docs and tools.
- **Contributors see the boundary** — a contributor can distinguish current product guidance from historical examples, fixtures, or optional personal workflows.
- **Existing personal workflows stay optional** — a user who already manages local tooling through a dotfile manager can keep that workflow without it being the recommended or required LeanPlan path.

Confirmed when: current install and runtime guidance lead with a non-dotfile-managed path, no current user-facing source says the personal dotfile workflow is required or recommended for normal LeanPlan use, and remaining references are either optional notes or historical test material.

## Guarantee

- **LeanPlan owns its adoption story** — users should be able to understand the supported install and refresh flow from LeanPlan itself because adoption should not depend on a maintainer's private machine habits.
- **Optional means optional** — personal workflow notes must not read as the product contract, because that would recreate the same hidden dependency under softer language.

## Non-goals

- Banning users from managing LeanPlan through their own dotfile workflow.
- Rewriting old feature artifacts or fixtures only because they mention the prior workflow.
- Changing LeanPlan's stage model or artifact contract.

## Upstream

- User prompt, 2026-06-23: "Let's remove chezmoi dependency from LeanPlan. Start with $leanplan-requirements".
- Current README install guidance, which leads with the personal dotfile workflow before the direct install path.
- Current runtime docs, which describe canonical tooling as applied through that personal workflow.
