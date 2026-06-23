# 260623-codex-leanplan-skill-form — Codex exposes LeanPlan stages with the right skill shape

## Problem

LeanPlan has one canonical stage model but two adapter shapes: Claude Code exposes each stage as its own skill surface, while Codex currently exposes a single dispatcher skill that multiplexes requirements, specify, design, tasks, implement, sharpen, revise, and validate. No load-bearing rationale is captured for that difference, so maintainers and agents cannot tell whether the Codex consolidation is an intentional runtime adaptation or an accidental mismatch.

The pain is practical:

- **Stage intent is less explicit on Codex** — a single activation trigger has to describe several different stage entries, each with its own input, output, and stop condition.
- **Adapter parity is harder to review** — when Claude and Codex package the same framework differently, reviewers lack a crisp rule for deciding whether a difference preserves semantics or hides drift.
- **JIT discipline can be diluted** — LeanPlan depends on loading only the matching stage reference; a broad dispatcher must be just as reliable as a stage-specific surface at selecting exactly the current stage's procedure.

## Outcome

Codex's LeanPlan adapter has a documented, reviewable skill shape that follows the same stage boundaries as the framework itself unless a Codex runtime constraint makes consolidation the better fit. The chosen form makes each LeanPlan entry point easy for an agent to activate intentionally, preserves one-stage-at-a-time reference loading, and makes any difference from the Claude adapter explainable from runtime behavior rather than historical accident.

User stories:

- **Maintainers see the rule** — a maintainer can inspect the Codex adapter and understand why its skill surface is consolidated or split without reverse-engineering the intent from the files.
- **Agents hit the right stage** — when a user asks for requirements, specify, design, tasks, implement, sharpen, revise, or validate, Codex activates the LeanPlan behavior with stage-specific inputs, outputs, and handoff language.
- **Reviews compare semantics, not packaging guesses** — a reviewer can check Codex against Claude by asking whether the same LeanPlan stage contract is preserved, not whether the two adapters happen to have the same number of files.
- **The final shape stays lean** — common framework content remains canonical and loaded on demand; adapter wrappers carry only the trigger and runtime glue needed for their surface.

Confirmed when: the Codex adapter's shape is selected by an explicit rule, each LeanPlan entry point is discoverable with its own stage intent, the adapter still loads only the matching canonical reference during normal use, and the Claude/Codex difference either disappears or is justified by a documented Codex-specific constraint.

## Guarantee

- **Canonical content stays shared** — stage procedure, artifact shape, and validation rules remain owned by the shared LeanPlan references so adapter changes do not fork framework behavior.
- **Vendor-neutral LeanPlan semantics** — Codex and Claude expose the same LeanPlan moves with the same meaning; vendor adapters are thin runtime shells around shared framework behavior, not separate dialects.
- **Runtime shape follows activation quality** — the preferred skill form is the one that gives agents the clearest trigger and completion boundary for the user's requested LeanPlan move.
- **JIT loading remains non-negotiable** — a more discoverable surface must not become a larger always-loaded prompt or a reason to load unrelated stage references.

## Non-goals

- Reworking LeanPlan's stage model or artifact contract.
- Changing Claude Code's stage-specific command behavior unless the comparison reveals a genuine shared-framework issue.
- Duplicating the canonical stage references into adapter files.
- Designing the later implementation task list in Requirements; this stage only captures the desired adapter outcome.

## Upstream

- User prompt, 2026-06-23: question whether Codex has a specific reason to keep LeanPlan as one consolidated skill while Claude Code exposes each subcommand as a separate skill, and request the LeanPlan Requirements stage.
- Current Codex adapter: `adapters/codex/leanplan/SKILL.md`.
- Current Claude stage adapters: `adapters/claude/{requirements,specify,design,tasks,implement,sharpen,revise}/SKILL.md`.
- Framework shape authority: `framework-design.md` §12, which maps LeanPlan skills to stage edges and off-pipeline moves.
- Skill-design grounding: `one-capability-granularity`, `progressive-disclosure-token-economics`, and `directory-packaging` knowledge-base entries.
