# 260623-deferral-lane — Design Rationale

## D-1: deferrals-archive-lane

A deferred decision and an understanding-shift delta are both append-only, off-pipeline records, so the cheap move is to put deferrals into the existing understanding archive — the earlier "option (c)". Rejected. A delta is **binding**: it records a committed change of belief and drives `revise` to edit committed artifacts ("this is now true, propagate it"). A deferral is the opposite — **non-binding**, an open item to re-decide ("hold this open, do not propagate"). Blending binding and non-binding items in one record destroys a reader's (or agent's) ability to tell "act on this" from "hold this open" — exactly what `Spec#C-3` / `C-4` forbid. So: a distinct sibling archive, a distinct anchor (`Defer-N` vs `Delta-N`), a distinct name. Invalidation trigger: if the two records ever came to be consumed identically, the split would be cost without benefit — but their consumption is opposite (revise-and-propagate vs re-decide-freely), so that won't hold.

## D-2: non-binding-prior-block-shape

The shape *is* the anti-pinning mechanism, not decoration. A captured deferral that recorded a chosen answer ("use a write-through cache") would arrive at its owning stage as a fait accompli and pin it — the harm `Spec#C-3` forbids. So the block deliberately has no "decision" field: it records the *question*, the *forces*, and at most an *option seen, marked not chosen*. This preserves the spark — the owning stage doesn't re-derive the forces from zero — while withholding the conclusion, so the stage still decides. It is the same "carry the substance, never the premature form" principle as philosophy P7 / Feature M, applied forward: carry the question and forces, never a premature answer. The structure is low-freedom (validator-anchored, consistent) so the drain and reconciliation can rely on it.

## D-3: capture-as-affirmative-stage-hook

Two alternatives weighed.

*A standalone capture skill, like `sharpen`.* Rejected: capture has no independent applicability, termination, or callable interface — it does not fire on its own trigger, it happens *during* ordinary stage work. By the skill-vs-tool-vs-prompt frame that makes it a stage-procedure addition, not a skill; a skill would impose an invocation ceremony that fights the "lightweight aside" the Spec wants (`B-1`, `C-6`).

*Merely loosening the existing prohibitions* ("strip less aggressively"). Rejected: a negative loosening gives the planner nothing to *do*. Capture is instead the **affirmative** complement (positive-instruction): "park it as a `Defer-N` addressed to its owning stage." The disposal points already exist — the stage has already judged the content off-altitude — so capture only redirects the discard into the lane rather than to nowhere.

Surface-lean by progressive disclosure: a one-line hook in the always-loaded stage body, the shape + procedure in the on-demand companion — the framework applying its own reflexive surface budget (Feature I).

## D-4: drain-by-re-derivation-at-stage-entry

The drain's *degree of freedom* is the whole ballgame. A low-freedom drain — "for each deferral addressed to you, apply its option" — would replay the deferred choice and pin the stage, destroying `Spec#C-3`. So the drain is deliberately high-freedom: open-field prose telling the stage to re-examine the question against its *full current option space* (richer now than when the spark first appeared) and decide freshly. This is the framework's existing re-derivation-over-replay stance (philosophy P2; `sharpen` is itself a re-derive move) applied to the forward lane.

The tension to hold: high freedom risks the drain being skipped or done shallowly. So the *consultation* is made load-bearing and reconciled (D-5, the Feature M pattern), even though the *decision* it prompts stays free. Freedom in the reasoning; rigor in the fact that the reasoning happened.

## D-5: no-loss-via-reconciliation-plus-advisory-check

No-loss needs surfacing, but surfacing splits along what is mechanically checkable. The *resolution marker* — whether a `(resolved -> …)` note is present on a `Defer-N` whose owning stage's artifact already exists — is structural, so `validate.py` can and does check it, as an advisory warning (escalating under `--strict`, mirroring the surface-budget guardrail; not a hard gate, because an unresolved deferral for a not-yet-run stage is legitimate). The *substance* — did the "resolved" deferral genuinely land where it cites, or is the marker slug-deep? — is precisely what the validator cannot judge, since it reads artifacts, not the decisions behind them (the Feature M boundary). So substance rides Close-Out Reconciliation, reviewer-judged. Validator-only would rubber-stamp slug-deep resolutions; review-only would forfeit the cheap structural catch. Both, each at its tier.

## D-6: rename-understanding-archive

The (B) half of `Spec#C-4` is a standalone defect: bare "understanding" is an over-broad god-word for a file that holds one specific thing — mid-round understanding-shifts (`Delta-N` blocks: what the understanding now is, the prior assumption it kills).

Naming trail. `deltas.md` (match the file to its unit) was rejected twice over: "delta" is itself a generic word for "change," and `Deltas#Delta-1` stutters in citations — the original file≠unit gap is in fact what kept `Understanding#Delta-1` clean. Bare `shifts.md` is still polysemous (work / gear / schedule shift) and does not self-identify in a directory listing. The fix keeps the good root and qualifies it: **`understanding-shifts.md`** — self-identifying, not a bare god-word, matching the contract's own "mid-round shift" wording. The `Delta-N` unit and the `Understanding#` citation prefix stay, so the anchor, the regex, and every citation site are untouched; only the filename literal moves. The file ("shifts") and unit ("Delta") then use synonyms for the same change — mildly loose, accepted to avoid an anchor-rename blast and to honor #34's "keep Delta-".

Alternative (R2): leave the file, tighten its role in contract prose only. Rejected — it satisfies distinctness-from-the-new-lane (the (A) half) but leaves the broad name (B) standing, which the user named as the actual defect.

Harm assessment (the user gated this on "no harm"). The rename moves the filename literal across roughly two dozen live references / adapters / validator / selftest / fixture sites; the `Understanding#` citation prefix and the `Delta-N` anchor do **not** move, which shrinks it further. None is value-destroying or irreversible; the sweep is scriptable and the selftest is the green checkpoint. Two real hazards, both handled:

1. It reverses `framework-design.md`'s deliberate "keep Understanding (Delta-)" from #34 — but that decision held *because no sibling made the name ambiguous*. This feature introduces exactly that sibling, so the premise changed; the reversal is principled, recorded as a supersession.
2. A blind sweep would corrupt the historical `260620-*` feature dirs that describe *building* `understanding.md`, and this feature's own dir that describes the rename. Both are exempt — quote-prior-vocab-as-data, the reflexive-dir lesson.

Invalidation trigger: if the blast radius were unbounded or touched irreversible external state, R2 would win. It is bounded and internal, so the rename ships — but as a cleanly separable task track, so it can be split out if the harm-call later goes the other way.
