# 260622-vocab-v2-rename — DESIGN RATIONALE

## Decision-1: staged-authoring-atomic-landing

**Forces.** #34 and L's `Decision-2` both say "apply atomically and fully re-validate," with a stated fallback: "if atomic proves intractable, stage per family (anchors → files → prose)." But "atomic" was doing two jobs — *atomic authoring* (one commit) and *atomic landing* (one re-validated unit). The ~1,000-edit size and the validator coupling (Decision-2 of this design) force them apart.

**Alternatives considered.**
- *Pure atomic — one 1,000-edit commit.* Honors "atomic" literally. Rejected: unreviewable and unbisectable; if the end gate fails, the cause is a needle in a 1,000-edit haystack; the blast radius is the whole repo in one diff.
- *Green gate after every family.* The intuitive reading of "stage per family." **Impossible**, not merely costly: the gate's own members (`validate.py`'s `kind` values, `SURFACE_FILES`, section-name checks; the selftest's exact-string assertions) cannot half-flip. The instant content moves to `B-`/`tasks.md`/`Behavior` while the validator still expects `O-`/`plan.md`/`Outcome` (or vice-versa), the gate is red. There is no per-family ordering that keeps it green, because the validator and the content it checks are different families.
- *Bilingual transition validator* (widen the validator to accept both vocabs, sweep green-throughout, then narrow). Keeps the gate green. Rejected: a validator that accepts both vocabularies **cannot detect a missed rename** — the exact error class the completeness gate exists to catch (`O-3` left un-migrated still "validates"). It also adds a throwaway artifact with its own test burden. The masking flaw is disqualifying.

**Chosen path.** Stage by family for authoring/review; accept a **red gate between families**; isolate the intermediate states in the `leanplan-v2` worktree; run the full three-gate **once at the end**; merge as **one atomic PR**. "Atomic" is satisfied at the landing boundary (all-or-nothing merge of a re-validated whole), which is what #34's re-validation requirement actually needs — not atomic authoring, which buys nothing and costs reviewability.

**Rollback.** Per-family commits make revert surgical; a failed, unsalvageable end gate is `git reset --hard` to the pre-sweep base (`b2b59a5`). The worktree is disposable, so a botched sweep never touches `main`.

**Invalidation trigger.** If, in execution, the family count or the gate-flip turns out small enough that a single commit is genuinely reviewable, collapse to pure-atomic — the staging is a tactic for tractability, not a principle.

## Decision-2: gate-unit-flips-in-lockstep

**The crux #34 named: "the validators rename themselves."** The verification tooling is *inside* the sweep, and it validates the content being swept — so it cannot be trusted mid-flight and cannot move independently.

**What is coupled (found by reading the code).** `validate.py`'s `ANCHOR_RE` captures a `kind` group (`O`/`INV`/`Decision`/`Delta`) that becomes the anchor's type and flows into every `_anchors(kind=...)` call, every `_check_*` method, and every error string. Renaming the items therefore changes a *regex capture* **and** the dozens of call-sites keyed on its values, in one edit. Add `SURFACE_FILES`/`STAGE_ORDER`/`SURFACE_SOFT_CAP` (filename + stage keys), the required-section names (`Outcome`→`Behavior`, `Invariants`→`Constraint`), `CITATION_RE`'s file-key alternation, `scan-leaks`'s `ANCHOR_TOKEN_RE`/`CITATION_RE` (whose comment already says "keep all three in sync"), the fixtures' filenames **and** internal anchors, and the selftest's exact-string assertions (`SPEC#O-1`, `Decision-2`, `plan.md`, `Delta-1`…). All of these are expected-value assertions that flip the moment the vocabulary moves.

**Consequence.** These members form **one lockstep commit**. You cannot rename the fixtures without the validator that reads them, nor the validator without the selftest that asserts its output, nor any of them without the grammar in `artifact-contract.md` that is their source of truth. This is the single largest, most error-prone commit of the rollout and the reason a red intermediate gate is unavoidable (Decision-1).

**Found en route.** The selftest's `task_file()` helper already anticipates the migration but checks `task.md` — §8's file is `tasks.md`. The lockstep commit must reconcile the helper to `tasks.md`, or the selftest silently stops finding the TASK artifact post-rename.

## Decision-3: three-gate-acceptance

**Why one gate is not enough.** Each instrument is blind to a failure mode the others catch:
- **G1 structural** (`validate.py` + `leanplan-selftest` + `scan-leaks`, over all nine shipped cycles and both fixtures) proves the framework is internally consistent in the new vocab — anchors resolve, citations resolve, SPEC↔task coverage holds. But it passes a framework that is *consistently still old* (nothing migrated) and a framework where a non-validated file (e.g. `README.md`) kept an old token.
- **G2 completeness** (scan for residual prior-vocab tokens; assert zero outside an *enumerated* exemption list) catches the missed rename — a token left behind that is still internally consistent, which G1 cannot see. This is the gate the bilingual validator (Decision-1) would have destroyed.
- **G3 preservation** (diff review: only labels changed, no `O-1`→`B-2` renumber, no prose re-argued) catches over-reach — a "rename" that quietly rewrote content — which neither G1 nor G2 can see.

**The hard part of G2 is the exemption list.** "plan" appears 164× but most are ordinary English; the prior-vocab column in §8 and any explicitly-historical framing must *survive*. So G2's scan is token-class-anchored (`\bO-\d+\b`, `SPEC#…`, `### Decision-\d+`) and its exemptions are enumerated, not open-ended — an allow-list the plan must build and justify, not a blanket "ignore framework-design.md."

**Mapping.** G1→`SPEC#INV-1-identity-and-traceability-preserved`, G2→`SPEC#O-1-prior-vocab-absent-from-live-surfaces`, G3→`SPEC#INV-2-content-preserved-labels-only`. O-2 (caveat retirement) is verified inside G3's inspection (the §8/Decision-2 framing edit is a content-preservation-adjacent judgment, not a token scan).

## Decision-4: resolve-section-8-derivation-gaps

**Forces.** The memory of L's own rework is explicit: *the gap a name-sweep won't touch is where defects hide* (the retired-axis gloss that a rename leaves stranded). §8 is the locked authority for the *names*, but three application questions sit in that gap — §8 does not spell them letter-for-letter, and a blind `sed` resolves each one wrong.

- **(a) Citation-namespace casing.** Current citations are all-caps (`SPEC#`, `DESIGN#`, `TASK#`) because the artifacts were literally named `SPEC`/`DESIGN`/`TASK`. §8 renames the nodes to title-case `Spec`/`Design`/`Tasks`. The faithful application is to carry the new spelling into the citation token (`Spec#B-1-…`), and likewise `Rationale#`/`Research#`/`Understanding#`. **This is the one resolution that is a genuine fork, not a forced move**: a maintainer could instead choose to keep citation namespaces all-caps as a visual convention independent of node casing. We recommend title-case (faithful to §8, and the node name *is* the namespace), and flag it for ratification — flipping it is a one-line change to the citation-family transform spec, localized, not a re-plan.
- **(b) Anchor-regex alternation order.** `Decision`→`D` makes `D` a strict prefix of `Delta`. Python alternation is order-sensitive; `(B|C|D|Delta)` only matches `Delta-1` by backtracking and is fragile. Resolution: order the longer alternative first — `(B|C|Delta|D)` — in both `validate.py` and `scan-leaks`. The selftest's existing `Delta-N` injection case is the regression guard that proves it.
- **(c) REQUIREMENT Outcome→Outcome·Guarantee split.** §8 gives Requirements a new `Guarantee` section for continuous domain properties (today's loose "system policies"). This is more than a token rename: `validate.py`'s `_check_requirement` must add `Guarantee` as a *conditional* (warn-empty) section — not required, since not every requirement has continuous policies — and the scaffold + the requirement guide must relocate the system-policies sub-group there. SPEC's *section headings* also rename (`Outcome`→`Behavior`, `Invariants`→`Constraint`), tracking the item rename. INV-2's "labels only" budget explicitly admits these §8-mandated structural splits; they are scheme application, not free content.

**Invalidation trigger.** If the maintainer rejects title-case namespaces (a), the citation family (and `validate.py`'s `CITATION_RE` file-keys, `scan-leaks`'s `CITATION_RE`) flips to all-caps-retained; nothing else in the plan changes.
