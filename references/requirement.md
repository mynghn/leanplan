# LeanPlan Requirement Stage

LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work in monorepos. This doc carries the procedure for the REQUIREMENT stage — capturing biz WHAT before any tech choice. Edge: standalone input → REQUIREMENT.

Companion: `philosophy.md` (principles), `artifact-contract.md` (shape rules).

## Inputs

- Feature key (e.g. `NEWCS-1234`).
- Optional upstream context: Jira issue, PRD, Slack thread, or user-provided business intent.

## Output

`<cwd>/docs/features/<KEY>/requirement.md`

## Procedure

1. **Resolve `<KEY>`**: parse `$ARGUMENTS`. If it matches a Jira-style key (`[A-Z]+-\d+`), fetch the issue (description, summary, linked PRD/Slack) for upstream context. Otherwise ask the user for the key + a short biz-intent sentence.
2. **Load upstream** (when present): Jira description, linked PRD, linked Slack thread. Harvest the biz *problem*, not the requested implementation — upstream often arrives mixed with solution suggestions; strip them.
3. **Draft interactively**. Misframed Problem is the single largest source of downstream rework. Confirm framing with the user before writing:
   - **Problem** — what biz pain or opportunity drives this? Who feels it? What is currently broken, missing, or constrained?
   - **Outcome** — biz future state + observable success signal. Prefer **user-story bullets** for user-visible behaviors using the form `**short title** — one-line summary. follow-up detail when needed.` Group system-level policies / cross-cutting invariants (price parity, state-machine rules, regional constraints) under a separate sub-group rather than forcing them into user-story shape — not every outcome is a user story. Fold the success signal into the same section (don't split into a separate "Success metric" section).
   - **Non-goals** — only if scope edges are genuinely ambiguous.
   - **Upstream** — only if refs exist; short list.
4. **Write** the artifact at `<cwd>/docs/features/<KEY>/requirement.md` (`mkdir -p` the dir).
5. **Self-check** before exiting:
   - Grep body for tech-stack nouns (Kafka, Redis, Kotlin, Spring, gRPC, Postgres, Flink, Kubernetes, Docker, etc.) — zero hits expected.
   - Outcome names a biz-observable signal.
   - Outcome bullets that *are* user-visible behaviors are written in user-story form; bullets that are system invariants are grouped separately, not disguised as user stories.
   - Conditional sections are omitted when empty (don't ship empty Non-goals or Upstream sections).

## Guardrails

- **No implementation choices.** No specific stack (Kafka, Redis, Postgres, gRPC), no internal architecture, no chosen pattern. Biz-vocabulary channels — "admin tool", "partner API", "batch integration" — are fine; they name channels, not choices.
- **Outcome folds the success signal.** Biz future state + observable signal in the same section. Don't split into a separate "Success metric" subsection.
- **User-story bullets where it fits.** When an outcome describes a user-visible behavior, write it as `**short title** — one-line summary. detail.` so reviewers can scan the feature shape. Don't twist system invariants into fake user stories — group them separately.
- **Conditional sections must earn their place.** Non-goals only when scope is ambiguous; Upstream only when refs exist. Otherwise omit — empty sections dilute the review surface.
- **Biz-native vocabulary.** Reviewers are PMs / stakeholders. Avoid internal system names unless they *are* the biz context (e.g. a product line).

## Template

```markdown
# <KEY> — <short biz-framed title>

## Problem
<business pain/opportunity, who feels it, what is broken or constrained>

## Outcome
<one-paragraph framing: future state + scope boundary>

User stories:

- **<short title>** — <one-line user-observable behavior>. <follow-up detail if it sharpens the story; otherwise drop>.
- ...

System policies: <only when cross-cutting invariants exist; otherwise drop this group>

- **<short title>** — <invariant or policy>. <detail>.
- ...

<observable success signal folded into a final sentence or two>

## Non-goals
- <only when scope edges are ambiguous>

## Upstream
- <Jira / PRD / Slack refs when they exist>
```

The user-stories / system-policies split is a default shape, not a contract. Drop a group when it's empty; collapse to flat bullets when the feature is small enough that grouping adds noise.

## Hand-off

Tell the user: next edge is `/specify <KEY>` (Claude) or `specify <KEY>` (Codex). Iterating on REQUIREMENT first is fine — `specify` re-derives from REQUIREMENT each invocation.
