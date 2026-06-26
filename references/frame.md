# LeanPlan Requirement Stage

This doc carries the procedure for the Requirements stage — capturing the desired outcome before any implementation choice. Edge: standalone input → Requirements.

**Stage stance.** Capture the desired outcome in language a PM reads — the future state and the pain behind it, in domain vocabulary. Domain-native *channels* ("admin tool", "partner API") are fine; the attractor to resist is implementation leakage — a chosen stack, architecture, or pattern (that belongs in Spec / Design).

Companion: `philosophy.md` (principles), `artifact-contract.md` (shape rules).

Mid-stage, if a disturbance shifts the understanding, `leanplan-rethink` is the sanctioned, opt-in response — an off-pipeline reflect-and-re-derive move that reads your artifacts but never edits them — instead of ignoring it or hand-rolling a fix.

## Inputs

- Feature intent: a short problem statement or solution title (free-form phrase), a tracker key to anchor on (e.g. Jira `NEWCS-3595`), or an existing feature id to revise.
- Optional upstream context: Jira issue, PRD, Slack thread. When present it supplies the *problem*. It may also become the feature id (tracker-key form) — but when it is *not* the id, record refs under `## Upstream`.

## Output

`<cwd>/docs/features/<KEY>/requirements.md`

## Procedure

*Default flow, not a rigid script — re-derive it against the actual input. Load-bearing (don't skip or reorder): allocate-before-write (step 1), the sparse-arrival judgment (step 3), the Problem-framing confirmation (step 4), the self-check (step 6).*

1. **Allocate the feature.** Parse `$ARGUMENTS` and pick the id form, then let `leanplan-new` create the dir (it is the single allocator — never `mkdir` yourself). It prints the resolved `docs/features/<id>` path on stdout — **capture that path** and use it for every subsequent write; if it exits non-zero, stop (don't write).
   - **Revising** — if `$ARGUMENTS` already names an existing dir under `docs/features/` (any form), operate on `docs/features/<that-id>/` directly; skip allocation.
   - **Tracker key** — if `$ARGUMENTS` is a Jira-style key (`[A-Z]+-\d+`) and the user wants the feature anchored to it, run `leanplan-new "<KEY>"`; the dir is the bare key (no slug). Still fetch the issue for problem context (step 2). If instead the key is only context (not the identity), treat it as upstream and allocate by title below.
   - **Date** — if the user wants a date-keyed feature, confirm a short kebab slug, then run `leanplan-new --date "<slug-or-title>"` (today's `YYMMDD`; pass `--date=YYMMDD` to override).
   - **Sequence** (default) — otherwise treat `$ARGUMENTS` as an intent / title phrase, confirm a short kebab slug with the user (slugs are permanent in the dir name), then run `leanplan-new "<slug-or-title>"` for the next repo-local `NNNN-slug`.
2. **Load upstream** (when a Jira key, PRD link, or Slack thread is supplied): harvest the *problem*, not the requested implementation — upstream often arrives mixed with solution suggestions; strip them. Capture under `## Upstream` any tracker key / links that are metadata — when the feature id itself is a tracker key, that key is the identity, so record only supplementary refs here.
3. **Draw out a sparse arrival** before distilling, so distillation works from a formed understanding instead of a thin guess. Always judge the arrival: does `$ARGUMENTS` plus any upstream already carry a *formed* problem — an articulable pain, with who feels it and what is broken? The read is qualitative, not a word count. When unsure, lean sparse and offer — a needless offer is cheap (the planner declines it), but a sparse arrival mistaken for formed is skipped with nothing left to decline, slipping undrawn into distillation.
   - **Formed → skip.** Proceed straight to distillation (step 4); never draw out an understanding that already exists.
   - **Sparse → draw it out** through structured questions (`AskUserQuestion` on Claude; the runtime-native prompt on Codex):
     - **Elicit** the problem — the pain, who feels it, what is broken, missing, or constrained.
     - **Frame** — offer two or more candidate problem framings for the planner to choose among; don't silently adopt the first.
     - **Surface** — raise the gaps and ambiguities bearing on the problem and resolve them with the planner.
   - **Opt-in, never a gate.** The step offers; it never blocks. The planner can decline it or cut it short and move to distillation at any point.
   - **Forms understanding, writes nothing.** The draw-out forms the planner's understanding in the conversation — no file. Distillation (steps 4–5) is the sole writer of `requirements.md` and works from that understanding.
   - **Cold start only.** This draws an understanding out of a blank-slate arrival; a disturbance to an *already-formed* understanding is `leanplan-rethink`, not this step.
4. **Draft interactively**. Misframed Problem is the single largest source of downstream rework. Confirm framing with the user before writing:
   - **Problem** — what pain or opportunity drives this? Who feels it? What is currently broken, missing, or constrained?
   - **Outcome** — desired future state + observable success signal. Prefer **user-story bullets** for user-visible behaviors using the form `**short title** — one-line summary. follow-up detail when needed.` not every outcome is a user story. Fold the success signal into the same section (don't split into a separate "Success metric" section).
   - **Guarantee** (conditional) — cross-cutting domain rules that hold continuously (price parity, state-machine rules, regional constraints), kept out of user-story shape. State the *intent* (why the rule matters); its observable, testable form is Spec's to own, so don't pre-empt Spec vocabulary here (`artifact-contract.md` → One Prose Home Per Fact). Omit the section when no such policies exist.
   - **Non-goals** — only if scope edges are genuinely ambiguous.
   - **Upstream** — only if refs exist; short list.
5. **Write** the artifact at the path `leanplan-new` printed in step 1 (e.g. `docs/features/0007-anomaly-publisher/requirements.md`). Do **not** `mkdir` — `leanplan-new` is the single directory allocator; the requirement skill never creates the dir itself.
6. **Self-check** before exiting:
   - Grep body for tech-stack nouns (Kafka, Redis, Kotlin, Spring, gRPC, Postgres, Flink, Kubernetes, Docker, etc.) — zero hits expected.
   - Outcome names a measurable success signal.
   - Outcome bullets that *are* user-visible behaviors are written in user-story form; system policies live under `## Guarantee`, not disguised as Outcome user stories.
   - Conditional sections are omitted when empty (don't ship empty Non-goals or Upstream sections).
   - Problem leads with the pain itself (who feels it, what's broken), not background — a PM grasps it from the first line (conclusion-first; `artifact-contract.md` → Prose Style).
   - Problem reflects a formed understanding, not a sparse guess — a sparse arrival was drawn out (problem elicited, framings weighed, gaps resolved) before distillation, and the draw-out wrote no file of its own.

## Guardrails

- **No implementation choices.** No specific stack (Kafka, Redis, Postgres, gRPC), no internal architecture, no chosen pattern. Domain-vocabulary channels — "admin tool", "partner API", "batch integration" — are fine; they name channels, not choices.
- **Park a genuine deferral; don't discard it.** A real cross-stage decision that surfaces here goes into `deferrals.md` as a `Defer-<N>` addressed to its owning stage, rather than being discarded — opt-in planner judgment; procedure in `references/deferral.md`.
- **Outcome folds the success signal.** Desired future state + observable signal in the same section. Don't split into a separate "Success metric" subsection.
- **User-story bullets where it fits.** When an outcome describes a user-visible behavior, write it as `**short title** — one-line summary. detail.` so reviewers can scan the feature shape. Don't twist system policies into fake user stories — they belong under `## Guarantee`.
- **Conditional sections must earn their place.** Non-goals only when scope is ambiguous; Upstream only when refs exist. Otherwise omit — empty sections dilute the review surface.
- **Domain-native vocabulary.** Reviewers are PMs / stakeholders. Avoid internal system names unless they *are* the domain context (e.g. a product line).
- **Draw out a sparse arrival; never force it.** When the arrival carries no formed problem, elicit it — problem, candidate framings, gaps — before distilling. The draw-out is opt-in: a formed arrival skips it, and the planner can decline or cut it short at any point. It forms the planner's understanding only — distillation stays the sole writer of `requirements.md`.

## Template

```markdown
# <KEY> — <short problem-framed title>

## Problem
<the pain or opportunity, who feels it, what is broken or constrained>

## Outcome
<one-paragraph framing: future state + scope boundary>

User stories:

- **<short title>** — <one-line user-observable behavior>. <follow-up detail if it sharpens the story; otherwise drop>.
- ...

<observable success signal folded into a final sentence or two>

## Guarantee
<only when cross-cutting domain rules (system-policy intent) exist; otherwise drop this section>

- **<short title>** — <the domain rule + why it matters; Spec owns its observable form>. <detail>.
- ...

## Non-goals
- <only when scope edges are ambiguous>

## Upstream
- <Jira / PRD / Slack refs when they exist — metadata; record here when they are not the feature id itself>
```

The Outcome user-stories / Guarantee system-policies split is a default shape, not a contract. Drop the Guarantee section when empty; collapse Outcome to flat bullets when the feature is small enough that grouping adds noise.

## Hand-off

Tell the user: next edge is `leanplan-specify <KEY>`, where `<KEY>` is the id `leanplan-new` allocated (e.g. `0007-anomaly-publisher`, `NEWCS-3595`, or `260616-anomaly-publisher`). Iterating on Requirements first is fine — `specify` re-derives from Requirements each invocation.
