# LeanPlan Implementation — Close-Out Distillation

On-demand companion to `implement.md`, loaded at procedure step 7 (close-out). Carries the distillation tier hierarchy and the commit-message / PR-body promotion rules — the lookup detail consumed only once close-out is reached, kept out of the always-loaded implementation reference (context-engineering: jit-loading).

## Distillation Hierarchy

At close-out, migrate non-obvious WHYs from plan anchors into the strongest durable form available. Prefer higher tiers:

| Tier | Form | Use when |
|---|---|---|
| 1 | **Types / signatures / module structure** | The WHY is a constraint the compiler or IDE can enforce. |
| 2 | **Tests** (unit, property, integration) | The WHY is a behavioral guarantee; the test name + body carry the reason. |
| 3 | **Enforced annotations** (custom lint, archunit, API linter) | The WHY is a cross-cutting rule. |
| 4 | **Commit message** | Change-scoped WHY — why this commit exists, alternatives considered, tradeoffs accepted. |
| 5 | **PR body** | Change rationale that must survive squash-merge. |
| 6 | **Inline comment** | Last resort — subtle invariant, workaround, non-obvious constraint that requires adjacency to the code. |

**Substance, not the key.** Whichever tier you promote a WHY into, carry the constraint *in words* — never the round-local handle that points at it. An in-round anchor (`B-N` / `C-N` / `D-N`), a `Spec#…`-style cross-artifact citation, or the feature id is plan-scoped (philosophy.md P6) and dangles once the plan is discarded; a durable form reading only "satisfies the round's anchor" *feels* migrated but has carried the handle, not the reason. Write the reason itself (e.g. "tokens must never be stored in clear").

### Commit message vs. inline comment

| Commit message | Inline comment |
|---|---|
| "Why this *change* was made" | "Why this *code* is shaped this way" |
| Alternatives rejected, tradeoffs accepted | Constraints the reader needs *while reading*, subtle invariants, workarounds |
| Investigative access (`git blame`, `git log`) | Adjacent access (eyes on the code) |
| Survives refactors | Dies with the line |

### Squash-durability promotion rule

Local commit messages are erased by squash-merge workflows. Persist by rationale kind:

| Rationale kind | Durable target |
|---|---|
| Local ("why this code is shaped this way") | code / tests / types / inline comment |
| Change ("why this commit exists", alternatives considered) | **PR body** or squash-commit message |
| Cross-feature architecture | runbook / org ADR / structural code (types, module boundaries) |

PR body is particularly durable — visible in GitHub history post-squash, linkable from future investigations. Don't rely on local commit messages for change rationale in squash-merge teams.

## Close-Out Reconciliation

The distillation above leaves the consultation proof; this step checks it. Run it at close-out as an implementation self-check, and re-run it on the review path. It is **review-tier, not a `validate.py` gate** — the validator reads artifacts, not the code / commits / PR where substance lands, so it cannot judge whether a migrated reason is genuine.

Reconcile the task card's **load-bearing citations** against the delivered work:

- **Obligation set.** Exactly the citations the card makes from the load-bearing prefixes — the Spec `B` / `C` a task realizes and the Design `Decision` it builds on. The card already enumerates them; no separate ledger is kept.
- **Check.** Each one's constraint must appear as substance in the delivered work — a type, test, annotation, commit body, PR body, or comment from the hierarchy above, carried *in words*. Substance means the anchor's **actual content** — the condition or reason it states — not a paraphrase of the slug name, which only re-says what naming the anchor already said; reproducing the content is what reading yields, and a self-describing slug does not. A reviewer who has opened the anchor judges the match. A load-bearing citation with no such substance, or only slug-deep substance, is a **surfaced skip**: its anchor was named but never consulted. Flag it; do not accept it as conforming.
- **Key on the artifact prefix, never the bare anchor.** A `Decision` cited from Design is load-bearing and in scope; the same `Decision` slug cited from Rationale is archive — load-on-challenge, never forced, and never a finding when absent. Archive-prefix citations (`Rationale#…`, `Research#…`) never enter the reconciliation.
- **Deferrals — the substance half of no-loss.** When the feature carries a `deferrals.md`, reconcile its `Defer-<N>` blocks too, as a second obligation set. An unresolved deferral addressed to a stage already authored is a surfaced omission — flag it (this confirms, and reaches past, `validate.py`'s structural advisory, which the reviewer cannot assume ran). A *resolved* one (a `(resolved -> …)` marker on its heading) is judged like any migrated WHY: did the decision genuinely land where the marker cites, or is the marker slug-deep? A slug-deep resolution is a surfaced skip, not conformance. The validator can see only the marker's presence; whether it is real is the reviewer's call.

The handles are read in-round, from the still-live plan card; the product carries only the distilled substance. So the check needs nothing round-scoped stamped into permanent history — it reads the card against the work, not a marker planted in the code.
