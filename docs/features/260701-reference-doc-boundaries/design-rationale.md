# 260701-reference-doc-boundaries — Design Rationale

## D-1: stage-docs-unchanged

Forces: a "from scratch" mandate invites re-cutting every doc, but re-cutting an already-correct boundary is churn that risks regressions for no load-fidelity gain.

The concern→occasion map showed the five stage docs and the off-pipeline docs are occasion-pure.
At each stage-run everything co-loading (stance, procedure, guardrails, template) belongs to that run, and the only foreign references are one-line pointers that already defer the body to a JIT companion.
`implement.md` is the exemplar — it holds `implement-closeout.md` and `revise.md` out until their moment.

Chosen: confirm these boundaries and leave them, so the feature touches only the doc that is genuinely mis-bounded.
"From scratch" is honored by re-deriving the boundaries and finding most of them already right — a derivation that validates is still a derivation.

Rejected: re-boundarying the stage docs, for example splitting stance / procedure / guardrails into separate units.
Their contents share one occasion (the stage-run), so splitting would create the over-fragmentation the Requirements names a non-goal, and add cross-unit hops with no fidelity gain.

Invalidation: if a stage doc later grows a section with a genuinely disjoint occasion profile, split that section then — the same test, applied locally.

## D-2: slim-contract-to-cross-stage-core

Forces: the contract loads whole at every stage-run, but only a fraction of it fires at that trigger; the rest is other occasions' content taxing every author.
The retained core must be exactly the concerns whose occasion profile really is "every stage-run".

The map isolated that set: Anchors (needed whenever any artifact's structure or anchors are written — all stages, plus Delta / Defer at the moves), the four cross-cutting authoring principles (exercised at every stage self-check and at validation), and the Isolate-breadth guardrail (a cross-stage authoring practice).
These share the profile, so they are one unit.

Principle-home reaffirmation: One Prose Home Per Fact, One Concern Per Item, Prose Style, and Surface Budget stay in the contract, not `philosophy.md`.
They are structural rules about artifact shape, not P1–P9 meta-stances — the same reasoning `260630` used to home One Concern Per Item here and to reject `philosophy.md` and the coordinate model as its home.
Moving them to `philosophy.md` would re-open that settled decision and miscategorize a structural rule.

Alternatives weighed:

- Leave the contract whole — rejected: it is the single largest over-fetch in the framework.
- Split anchors and principles into two files — rejected: they share the every-stage-run occasion, so one unit with two sections matches the profile without adding a second load, and splitting would be topic-driven, the very error being corrected.

Invalidation: if the principle set grows a member whose occasion is only on-challenge, not every self-check, that member belongs in `philosophy.md`, not here.

## D-3: artifact-shape-one-home-at-its-stage

Forces: the artifact shapes are authored twice today — once as the contract's `Required Shapes`, once as each stage's fill-in Template — and both load at the same stage-run.
C-1 demands one home; the choice is which.

Chosen: the authoring stage's Template is the canonical home, and the contract drops `Required Shapes`.
The shape's occasion is the stage-run, and the stage doc is already loaded there, so co-locating the shape with the procedure that uses it means one load carries everything stage-specific (procedure + shape + drift guards + self-check).
`design.md` gains a Template it lacked, removing the asymmetry where three stages had a local shape and one reached into the contract for it.

Rejected: contract-owns-shapes, stage-Templates-removed.
This keeps a second unit (the contract) in every stage-run's shape lookup and splits the shape from the procedure that applies it — the under-fetch direction.
It also leaves the contract carrying eight artifacts' shapes, seven irrelevant at any given run.

Off-stage shapes: Rationale and Research fold into `design.md` (authored at design-run), Understanding-Shifts into `rethink.md`, Deferrals into `deferral.md` — each the doc whose move authors that artifact, several already carrying a partial copy.

Invalidation: if two artifacts ever share one authoring occasion and one shape, a shared home for that pair would beat two copies.

## D-5: traceability-to-tasks-and-closeout

Forces: Traceability rides the always-loaded contract, but its occasion is narrow — coverage is decided at `tasks-run` and re-checked at close-out / review, nowhere else.

Chosen: move Traceability + `**GAP**` to `tasks.md` (which already carries the bidirectional forward / reverse verification the same concept underlies) and keep the reconciliation pointer in `implement-closeout.md`.
This stops Traceability over-fetching at frame / specify / design runs, where coverage is never reasoned about.

Rejected: keep it in the slim core as "shared infrastructure".
It is not every-stage — treating narrow content as shared is exactly the topic-over-occasion error this feature corrects, and it would re-inflate the core D-2 just slimmed.

Invalidation: if a non-Tasks stage ever gains a coverage obligation, re-evaluate the home against the new occasion set.

## D-6: references-one-hop-and-boilerplate

Forces: consolidating every repeated line to a single home fights self-containment, while inlining everything fights non-duplication.
The resolution is to split by what the repeated content *is*.

Distinction drawn: a *payload* is multi-line content an agent reasons from, for example the Isolate-breadth guardrail repeated in four docs.
That is duplication that drifts, so it gets one canonical home in the slim core with a one-line pointer from each stage doc.
A *navigation trigger* is a one-line pointer such as the rethink note, the Companion line, or the deferral capture / drain pointers.
It is not a concern an agent reasons from — it is the JIT hook itself, and inlining a hook at the occasion it fires is correct progressive disclosure, not duplication.
The R3 self-check bullets `260630` inlined into every stage doc are the precedent: a cited trigger belongs at its point of use, and replacing it with a pointer would only add a hop.

One-hop rule: every cross-unit reference resolves in a single hop, and no relocation may create a doc → advanced → details chain, because partial reads then miss content.

Rejected: consolidate all repeated lines, including the one-line triggers, into shared homes.
This would strip the in-context hooks that make the JIT mechanism fire and push the docs toward over-fragmentation for a token saving measured in single lines.

Invalidation: if a "trigger" ever grows into a multi-line payload, it crosses the line and should move to a canonical home.

## D-7: framework-design-citation-repair

Forces: the Requirements and the original Spec C-4 scoped `framework-design.md` out ("untouched"), but inspection showed it cites the exact sections the fix relocates — `→ Required Shapes` / `→ Drift Guards` / `→ Traceability`, about seven times.
Relocating the sections while leaving `framework-design.md` literally untouched dangles those pointers, breaking C-2.
The goal effectively requires relocation, so "untouched" and "the fix" cannot both hold.

The planner adjudicated this surfaced conflict and chose citation-repair.
The alternatives were to keep it 100% untouched (abandon the relocation, leaving the over-fetch and duplication largely unfixed) or to expand scope and re-boundary `framework-design.md` itself (a larger feature).
Repair is the minimal touch that keeps both the fix and reference integrity.

Why this is not a scope breach: `framework-design.md` is the challenge-time archive whose whole job is to map each contract rule to its canonical `references/` home.
A pointer that follows its target to a new home preserves the archive's meaning exactly; it does not restructure or re-boundary the archive.
The Requirements' non-goal already draws this line — "updating a pointer to match a new boundary is ordinary follow-through, not mechanism change" — so the Requirements intent (do not re-boundary the out-of-set docs) is preserved.
Only the Spec's over-strong "untouched" wording needed the warm fold.

Chosen: repair the ~7 citations to their new homes, change nothing else in `framework-design.md`, and leave `README.md` fully untouched (it carries no such pointer).
Because the conflict was resolved by decision, no deferral is parked.

Invalidation: if a later feature does re-boundary `framework-design.md` itself, this repair folds into that larger effort; and if the archive is ever retired in favor of inline rationale, the pointer set disappears with it.
