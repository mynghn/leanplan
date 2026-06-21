# LeanPlan Implementation — Close-Out Distillation

On-demand companion to `impl.md`, loaded at procedure step 7 (close-out). Carries the distillation tier hierarchy and the commit-message / PR-body promotion rules — the lookup detail consumed only once close-out is reached, kept out of the always-loaded implementation reference (CE: jit-loading).

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

**Substance, not the key.** Whichever tier you promote a WHY into, carry the constraint *in words* — never the round-local handle that points at it. An in-round anchor (`O-N` / `INV-N` / `Decision-N`), a `SPEC#…`-style cross-artifact citation, or the feature id is plan-scoped (philosophy.md P6) and dangles once the plan is discarded; a durable form reading only "satisfies the round's anchor" *feels* migrated but has carried the handle, not the reason. Write the reason itself (e.g. "tokens must never be stored in clear").

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
