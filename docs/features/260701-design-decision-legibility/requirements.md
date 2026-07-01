# 260701-design-decision-legibility — Design decisions land as prose, not judgeable units

## Problem

A reviewer reading `design.md` to judge whether a feature's design is sound often can't evaluate the decisions one by one.
They fail in two opposite ways that meet in the same wall of prose:

- **Blur** — a verbose decision fuses several non-separable design points into one section, so no single point is cleanly evaluable; the reviewer can't say what, exactly, is being decided.
- **Under-resolution** — a genuinely complex decision is stated too tersely: its mechanism isn't made graspable where it's read, and the realization detail needed to judge it lands incomplete.
  The reviewer then has to reconstruct the decision externally or go back to the author.

The pain persists *despite* the Design stage already intending better — it mandates full realization detail inside each Decision, a mandatory Architecture diagram, one-concern-per-Decision orthogonality, and a rationale archive for non-trivial WHYs.
That intent doesn't reliably land at the level of the individual Decision block, which is exactly where a reviewer reads.
The result is that `design.md` scans as continuous prose rather than a sequence of sharp, self-contained decisions — so the reviewer's judgment gets slower, coarser, and more dependent on the author.

## Outcome

A reviewer can read `design.md` and evaluate each design decision on its own — the file scans as a sequence of sharp decisions, not one wall of prose.

- **Atomic decision** — each Decision block carries one non-separable design point; a reviewer can name what it decides in a sentence, and no block silently bundles points that belong apart.
- **Graspable mechanism** — a genuinely complex decision is made understandable where it's read (e.g. a worked example or a local visual where a mechanism, sequence, state, or mapping would otherwise be a paragraph of prose), so the reviewer grasps it without re-deriving it.
- **Complete enough to judge** — the realization detail a reviewer needs to evaluate the decision (and a downstream task needs to act on it) is actually present, not gestured at.

The signal that confirms it: a reviewer works through a real `design.md` and judges every decision without reconstructing its mechanism externally or returning to the author for what the block should have carried — and no block bundles separable points.

## Guarantee

- **Lean discipline holds** — the win is *resolution*, not volume.
  Trivial decisions keep their one-line form; added depth or illustration is spent only where a decision's complexity genuinely demands it.
  The target is concise-not-compressed: de-blurring atomic points should net-reduce surface even as the few genuinely complex ones gain the detail they were missing — not a general license to make decisions longer.

## Non-goals

- Scoped to the Design stage's per-Decision unit — not the Requirements/Spec/Tasks stages.
- Not re-introducing mechanisms that already exist (the mandatory Architecture diagram, the rationale archive, the one-concern-per-item rule); the gap is that decision-level resolution doesn't land, not that a rule is missing to bolt on.
