# LeanPlan Requirement Stage

LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work in monorepos. This doc carries the procedure for the REQUIREMENT stage — capturing biz WHAT before any tech choice. Edge: standalone input → REQUIREMENT.

Companion: `philosophy.md` (principles), `artifact-contract.md` (shape rules).

## Inputs

- Feature intent: a short business problem or solution title (free-form phrase), or an existing `NNNN-slug` feature id to revise.
- Optional upstream context: Jira issue, PRD, Slack thread. When present it supplies the biz *problem* — but it is **not** the feature identity; record refs under `## Upstream`.

## Output

`<cwd>/docs/features/<KEY>/requirement.md`

## Procedure

1. **Allocate the feature.** Parse `$ARGUMENTS`. If it already matches an existing `NNNN-slug` id (a dir under `docs/features/`), you are revising — operate on `docs/features/<that-id>/` directly. Otherwise treat `$ARGUMENTS` as a biz-intent / title phrase, confirm a short kebab slug with the user (slugs are permanent in the dir name), then run `~/.local/share/leanplan/scripts/leanplan-new "<slug-or-title>"`. It allocates the next repo-local number, creates the directory, and prints the resolved `docs/features/<NNNN-slug>` path on stdout — **capture that path** and use it for every subsequent write. If `leanplan-new` exits non-zero, stop (don't write). If `$ARGUMENTS` looks like a Jira-style key (`[A-Z]+-\d+`), do **not** use it as the directory name — fetch the issue for upstream context (step 2) and record the key under `## Upstream`.
2. **Load upstream** (when a Jira key, PRD link, or Slack thread is supplied): harvest the biz *problem*, not the requested implementation — upstream often arrives mixed with solution suggestions; strip them. Capture the tracker key / links under `## Upstream` as metadata — optional context, never the directory identity.
3. **Draft interactively**. Misframed Problem is the single largest source of downstream rework. Confirm framing with the user before writing:
   - **Problem** — what biz pain or opportunity drives this? Who feels it? What is currently broken, missing, or constrained?
   - **Outcome** — biz future state + observable success signal, folded into one paragraph (don't split signal into a separate "Success metric" section).
   - **Non-goals** — only if scope edges are genuinely ambiguous.
   - **Upstream** — only if refs exist; short list.
4. **Write** the artifact at the path `leanplan-new` printed in step 1 (e.g. `docs/features/0007-anomaly-publisher/requirement.md`). Do **not** `mkdir` — `leanplan-new` is the single directory allocator; the requirement skill never creates the dir itself.
5. **Self-check** before exiting:
   - Grep body for tech-stack nouns (Kafka, Redis, Kotlin, Spring, gRPC, Postgres, Flink, Kubernetes, Docker, etc.) — zero hits expected.
   - Outcome names a biz-observable signal.
   - Conditional sections are omitted when empty (don't ship empty Non-goals or Upstream sections).

## Guardrails

- **No implementation choices.** No specific stack (Kafka, Redis, Postgres, gRPC), no internal architecture, no chosen pattern. Biz-vocabulary channels — "admin tool", "partner API", "batch integration" — are fine; they name channels, not choices.
- **Outcome folds the success signal.** One paragraph, biz future state + observable signal. Don't split.
- **Conditional sections must earn their place.** Non-goals only when scope is ambiguous; Upstream only when refs exist. Otherwise omit — empty sections dilute the review surface.
- **Biz-native vocabulary.** Reviewers are PMs / stakeholders. Avoid internal system names unless they *are* the biz context (e.g. a product line).

## Template

```markdown
# <KEY> — <short biz-framed title>

## Problem
<business pain/opportunity, who feels it, what is broken or constrained>

## Outcome
<business future state + observable success signal, folded>

## Non-goals
- <only when scope edges are ambiguous>

## Upstream
- <Jira / PRD / Slack refs when they exist — tracker key recorded here as metadata, never the dir name>
```

## Hand-off

Tell the user: next edge is `/specify <KEY>` (Claude) or `specify <KEY>` (Codex), where `<KEY>` is the repo-local id `leanplan-new` allocated (e.g. `0007-anomaly-publisher`). Iterating on REQUIREMENT first is fine — `specify` re-derives from REQUIREMENT each invocation.
