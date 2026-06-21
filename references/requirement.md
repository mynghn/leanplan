# LeanPlan Requirement Stage

This doc carries the procedure for the REQUIREMENT stage — capturing the biz outcome before any implementation choice. Edge: standalone input → REQUIREMENT.

**Stage stance.** Capture the business WHAT in language a PM reads — the outcome and the pain behind it, in biz vocabulary. Biz-native *channels* ("admin tool", "partner API") are fine; the attractor to resist is implementation leakage — a chosen stack, architecture, or pattern (that belongs in SPEC / DESIGN).

Companion: `philosophy.md` (principles), `artifact-contract.md` (shape rules).

Mid-stage, if a disturbance shifts the understanding, `/sharpen` (Claude) or `sharpen` (Codex) is the sanctioned, opt-in response — an off-pipeline reflect-and-re-derive move that reads your artifacts but never edits them — instead of ignoring it or hand-rolling a fix.

## Inputs

- Feature intent: a short business problem or solution title (free-form phrase), a tracker key to anchor on (e.g. Jira `NEWCS-3595`), or an existing feature id to revise.
- Optional upstream context: Jira issue, PRD, Slack thread. When present it supplies the biz *problem*. It may also become the feature id (tracker-key form) — but when it is *not* the id, record refs under `## Upstream`.

## Output

`<cwd>/docs/features/<KEY>/requirement.md`

## Procedure

*Default flow, not a rigid script — re-derive it against the actual input. Load-bearing (don't skip or reorder): allocate-before-write (step 1), the sparse-arrival judgment (step 3), the Problem-framing confirmation (step 4), the self-check (step 6).*

1. **Allocate the feature.** Parse `$ARGUMENTS` and pick the id form, then let `leanplan-new` create the dir (it is the single allocator — never `mkdir` yourself). It prints the resolved `docs/features/<id>` path on stdout — **capture that path** and use it for every subsequent write; if it exits non-zero, stop (don't write).
   - **Revising** — if `$ARGUMENTS` already names an existing dir under `docs/features/` (any form), operate on `docs/features/<that-id>/` directly; skip allocation.
   - **Tracker key** — if `$ARGUMENTS` is a Jira-style key (`[A-Z]+-\d+`) and the user wants the feature anchored to it, run `leanplan-new "<KEY>"`; the dir is the bare key (no slug). Still fetch the issue for biz context (step 2). If instead the key is only context (not the identity), treat it as upstream and allocate by title below.
   - **Date** — if the user wants a date-keyed feature, confirm a short kebab slug, then run `leanplan-new --date "<slug-or-title>"` (today's `YYMMDD`; pass `--date=YYMMDD` to override).
   - **Sequence** (default) — otherwise treat `$ARGUMENTS` as a biz-intent / title phrase, confirm a short kebab slug with the user (slugs are permanent in the dir name), then run `leanplan-new "<slug-or-title>"` for the next repo-local `NNNN-slug`.
2. **Load upstream** (when a Jira key, PRD link, or Slack thread is supplied): harvest the biz *problem*, not the requested implementation — upstream often arrives mixed with solution suggestions; strip them. Capture under `## Upstream` any tracker key / links that are metadata — when the feature id itself is a tracker key, that key is the identity, so record only supplementary refs here.
3. **Draw out a sparse arrival** before distilling, so distillation works from a formed understanding instead of a thin guess. Always judge the arrival: does `$ARGUMENTS` plus any upstream already carry a *formed* problem — an articulable pain, with who feels it and what is broken? The read is qualitative, not a word count. When unsure, lean sparse and offer — a needless offer is cheap (the planner declines it), but a sparse arrival mistaken for formed is skipped with nothing left to decline, slipping undrawn into distillation.
   - **Formed → skip.** Proceed straight to distillation (step 4); never draw out an understanding that already exists.
   - **Sparse → draw it out** through structured questions (`AskUserQuestion` on Claude; the runtime-native prompt on Codex):
     - **Elicit** the problem — the pain, who feels it, what is broken, missing, or constrained.
     - **Frame** — offer two or more candidate problem framings for the planner to choose among; don't silently adopt the first.
     - **Surface** — raise the gaps and ambiguities bearing on the problem and resolve them with the planner.
   - **Opt-in, never a gate.** The step offers; it never blocks. The planner can decline it or cut it short and move to distillation at any point.
   - **Forms understanding, writes nothing.** The draw-out forms the planner's understanding in the conversation — no file. Distillation (steps 4–5) is the sole writer of `requirement.md` and works from that understanding.
   - **Cold start only.** This draws an understanding out of a blank-slate arrival; a disturbance to an *already-formed* understanding is `/sharpen` (Claude) / `sharpen` (Codex), not this step.
4. **Draft interactively**. Misframed Problem is the single largest source of downstream rework. Confirm framing with the user before writing:
   - **Problem** — what biz pain or opportunity drives this? Who feels it? What is currently broken, missing, or constrained?
   - **Outcome** — biz future state + observable success signal. Prefer **user-story bullets** for user-visible behaviors using the form `**short title** — one-line summary. follow-up detail when needed.` Group system policies — cross-cutting biz rules (price parity, state-machine rules, regional constraints) — under a separate sub-group rather than forcing them into user-story shape; not every outcome is a user story. State the biz *intent* (why the rule matters); its observable, testable form is SPEC's to own, so don't pre-empt SPEC vocabulary here (`artifact-contract.md` → One Prose Home Per Fact). Fold the success signal into the same section (don't split into a separate "Success metric" section).
   - **Non-goals** — only if scope edges are genuinely ambiguous.
   - **Upstream** — only if refs exist; short list.
5. **Write** the artifact at the path `leanplan-new` printed in step 1 (e.g. `docs/features/0007-anomaly-publisher/requirement.md`). Do **not** `mkdir` — `leanplan-new` is the single directory allocator; the requirement skill never creates the dir itself.
6. **Self-check** before exiting:
   - Grep body for tech-stack nouns (Kafka, Redis, Kotlin, Spring, gRPC, Postgres, Flink, Kubernetes, Docker, etc.) — zero hits expected.
   - Outcome names a biz-observable signal.
   - Outcome bullets that *are* user-visible behaviors are written in user-story form; system policies are grouped separately, not disguised as user stories.
   - Conditional sections are omitted when empty (don't ship empty Non-goals or Upstream sections).
   - Problem leads with the pain itself (who feels it, what's broken), not background — a PM grasps it from the first line (conclusion-first; `artifact-contract.md` → Prose Style).
   - Problem reflects a formed understanding, not a sparse guess — a sparse arrival was drawn out (problem elicited, framings weighed, gaps resolved) before distillation, and the draw-out wrote no file of its own.

## Guardrails

- **No implementation choices.** No specific stack (Kafka, Redis, Postgres, gRPC), no internal architecture, no chosen pattern. Biz-vocabulary channels — "admin tool", "partner API", "batch integration" — are fine; they name channels, not choices.
- **Outcome folds the success signal.** Biz future state + observable signal in the same section. Don't split into a separate "Success metric" subsection.
- **User-story bullets where it fits.** When an outcome describes a user-visible behavior, write it as `**short title** — one-line summary. detail.` so reviewers can scan the feature shape. Don't twist system policies into fake user stories — group them separately.
- **Conditional sections must earn their place.** Non-goals only when scope is ambiguous; Upstream only when refs exist. Otherwise omit — empty sections dilute the review surface.
- **Biz-native vocabulary.** Reviewers are PMs / stakeholders. Avoid internal system names unless they *are* the biz context (e.g. a product line).
- **Draw out a sparse arrival; never force it.** When the arrival carries no formed problem, elicit it — problem, candidate framings, gaps — before distilling. The draw-out is opt-in: a formed arrival skips it, and the planner can decline or cut it short at any point. It forms the planner's understanding only — distillation stays the sole writer of `requirement.md`.

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

System policies: <only when cross-cutting biz rules exist; otherwise drop this group>

- **<short title>** — <the biz rule + why it matters; SPEC owns its observable form>. <detail>.
- ...

<observable success signal folded into a final sentence or two>

## Non-goals
- <only when scope edges are ambiguous>

## Upstream
- <Jira / PRD / Slack refs when they exist — metadata; record here when they are not the feature id itself>
```

The user-stories / system-policies split is a default shape, not a contract. Drop a group when it's empty; collapse to flat bullets when the feature is small enough that grouping adds noise.

## Hand-off

Tell the user: next edge is `/specify <KEY>` (Claude) or `specify <KEY>` (Codex), where `<KEY>` is the id `leanplan-new` allocated (e.g. `0007-anomaly-publisher`, `NEWCS-3595`, or `260616-anomaly-publisher`). Iterating on REQUIREMENT first is fine — `specify` re-derives from REQUIREMENT each invocation.
