# 260621-derivable-orthogonality — A coherent coordinate model: derivable high-traffic boundaries, named to match

## Problem

LeanPlan's unverbose, de-duplicated review surface — what lets a human or agent grasp a whole feature's pre-delivery activity from a lean set of artifacts — is held together by authors **correctly applying memorized boundary rules**, not by the framework's own model. The promise degrades silently exactly where it carries the most weight.

- **The highest-traffic seams are policed by prose, not derived from the model.** Which artifact owns a fact at REQ↔Spec (intent vs. observable contract) and at Design↔Tasks (the finished system vs. the work that builds it) is decided by per-seam discriminator rules an author must recall and apply — none validator-enforceable. The stated model can't adjudicate these boundaries itself: it labels the high-traffic distinctions in a way that doesn't actually separate them, so correctness rests on vigilance. When a discriminator is misapplied — LLM authors especially — the same fact lands in two homes, re-inflating the very surface the framework exists to keep lean.
- **The model's vocabulary doesn't track the model.** Names that the axes should justify drift from them: one element wears several names across the framework (e.g. the `plan` edge produces the `Tasks` artifact stored in `tasks.md`), so a reader — and an agent matching literally — must bridge the gap by latent inference. Restating the axes without settling the names would leave a coherent model described in incoherent words.
- **A by-product: two authoring rules read against each other.** "Put the highest-stakes facts at the edges for recall" appears to contradict "state each fact once," so authors resolve the overlap inconsistently — a small rule-consistency gap, not a new concern.

Who feels it: **authors** carry a discriminator rulebook the model should carry for them; **reviewers and agents** can't reliably locate the one home for a fact, must bridge name-to-concept latently, and inherit a surface that silently re-inflates; the framework's **orthogonality bet** — its single lever for both leanness and low-distraction agent reasoning — weakens with no one noticing.

## Outcome

The framework's **highest-traffic content boundaries derive from its stated model**, and **the model's own vocabulary matches the model** — so orthogonality holds by construction at the seams that carry the most weight, and the name you'd guess from the model is the name that exists. Scope is deliberately narrow: fix the boundaries and names that pay for themselves, not every distinction or label software development could name.

User stories:

- **Boundaries that derive from the model** — an author placing a fact, or a reviewer checking one, can tell which artifact owns it by reasoning from the framework's stated axes, without recalling a separate per-seam rule. The seams the framework most often blurs and most often re-inflates from — REQ↔Spec and Design↔Tasks — read as consequences of the model, not memorized exceptions.
- **Vocabulary that matches the model** — as the axes are restated, the model's own element names are clarified to match: the axis labels, and the artifact and edge/skill (and any model-reframed section) names the new axes justify. One element, one name; the name follows from the model. This is naming *coupled to* the redesign — the decisions, not the codebase-wide sweep (see Non-goals).
- **Recall and dedup stop fighting** — edge-placement-for-recall and state-each-fact-once compose into one instruction an author follows without choosing between them. (Minor rider; not a new axis.)

System policies:

- **Derivability is the test** — a high-traffic boundary that still needs a memorized discriminator to apply correctly hasn't met the bar; the model itself must adjudicate it.
- **Add only axes that pay for themselves.** The target is a model that makes the *load-bearing* boundaries self-evident — not one that names every axis of software development. Completeness is not the goal; a verbose model would defeat the surface it exists to keep lean. Distinctions the framework already handles adequately stay where they are — e.g. real-world assumptions distribute across Spec Invariants (must-hold bindings), Rationale (design-critical assumptions), and Research (evidence), and are caught dynamically by `sharpen`; no dedicated home is added for them.
- **Naming is clarification, not expansion.** Renaming the model's *existing* elements to match the axes reduces cognitive load and sharpens agents' literal-matching; it adds no content, so it does not conflict with the "add only axes that pay for themselves" rule. Every rename must still clear the framework's anti-churn bar (§8/§9 rejected the `<KEY>` sweep-rename) — part of this work is triaging which renames clear it.
- **Builds on the seam-guards, doesn't redo them** — the legibility + one-prose-home enforcement already shipped (`260620-lean-review-surfaces`) stays; this makes those guards derivable, shrinking what rests on vigilance.
- **Identity preserved, no information lost** — every artifact keeps its stage role and content; only the model's self-description, the crispness of its high-traffic distinctions, and the labels of its elements change.

Confirmed when: a fact authored on the wrong side of REQ↔Spec or Design↔Tasks is catchable by reasoning from the stated model — not only by an expert's memory; those two boundaries are explained by the model rather than by a standalone rule; the name of each model element follows from the model (no element with several names for one thing); and the model gains no section or axis a reviewer would experience as added surface.

## Non-goals

- **A dedicated home for every missing axis.** Only the high-traffic seams that re-inflate the surface when blurred are in scope. World-assumptions keep their existing homes (Spec Invariants / Rationale / Research) plus `sharpen`'s dynamic catch; the Spec-Invariant *target-vs-inviolable* nuance is **deferred** unless it proves painful in practice (a future backlog item, not this feature).
- **The broad mechanical rename *sweep*.** L makes the naming *decisions* the model justifies and writes them as the authority scheme (`framework-design.md` §8); propagating that scheme across every citation, `validate.py` regex, template, fixture, and shipped feature — especially high-volume **anchor/ID-scheme** churn — is **a separate dedicated effort** that this feature stands up but does not execute. At ~1,000 sites the full scheme is larger than the model rework itself, so this feature's own oversized-sweep provision splits it out — keeping L's lean review surface intact and letting the model redesign land without waiting on contentious churn.
- The runtime guarantee that cited content is actually **loaded** before an agent acts on it — that is the sibling feature `jit-load-guarantee`.
- Re-doing `260620-lean-review-surfaces`' legibility (BLUF) and de-duplication enforcement — this feature sits one layer below it (the model), not on top.
- Changing **what** any artifact contains or its stage role — only the model's self-description, high-traffic distinction-crispness, and element labels change.

## Upstream

- LeanPlan self-feedback critique, 2026-06-21 — from-scratch review of stage decomposition, orthogonality, and LLM-internals fit. Grounded in seminal decomposition models (Jackson *world-and-machine* R/S/P; Parnas four-variable; Osterweil process-vs-product) and an 8-framework SDD benchmark (spec-kit, Kiro, OpenSpec, BMAD, Tessl, Claude Code, Cursor, Aider). Scope narrowed on review: capture only the *valuable-but-missing* high-traffic seams, not every missing axis — a complete model would be a verbose one. Naming coherence folded in as coupled to the redesign (the axes justify the names); the codebase-wide mechanical sweep is staged within this feature, not split out.
- Backlog: **#30** (`Backlog: L`). Sibling feature: `jit-load-guarantee` (**#31**). Builds on **#32 (merged)**, which renamed `leanplan.md` → `framework-design.md`, realigned it to its design+rationale-archive role (§5/§7 now cite `artifact-contract.md`), and **deferred the §2 coordinate-model rework to this feature**. So L reworks `framework-design.md` §2/§3 (the model) plus the derived guards/stage-ownership in `artifact-contract.md` (their canonical home); branch rebased onto post-#32 `main`.
