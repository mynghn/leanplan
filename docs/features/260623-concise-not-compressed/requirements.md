# 260623-concise-not-compressed — Concise is not compressed: name the prose failure mode

## Problem

LeanPlan's reviewer — its primary reader — silently rubber-stamps prose they never actually read, whenever "lean" gets written as "compressed." That breaks the small-surface bet at its core: a lean surface is meant to be *reviewed carefully* (philosophy P3, Surface Budget), not skimmed.

The failure mode is information compression wearing concision's clothes. Chasing brevity, an author reaches for an unfamiliar or coined word where a plain depiction would read easier, or chains distinct concepts into a separator-joined noun pile — e.g. `call order · bypass-check save · conflict-id union → reconciled state`, which does both. It reads as terse, but the reviewer cannot judge it without first unpacking each term back into the point it stands for. That hidden unpacking cost is what erodes review fidelity — and it is invisible, because a compressed line looks like a lean model artifact, so the reviewer skims past it.

The current Prose Style guidance names adjacent habits ("lists over dense paragraphs," "short, declarative sentences") but never names *this* one. So the author has no rule to catch themselves against, and the reviewer has no name to reject it by.

## Outcome

The shared, all-artifact prose guidance distinguishes *concise* from *compressed* — naming information-compression-as-false-brevity as a failure mode the author can self-catch and the reviewer can reject by name. Brevity is defined explicitly: short *explanatory* sentences and lists, never a denser form — an unfamiliar coined word, or several concepts packed into one separator-joined token — that the reader must unpack.

User stories:

- **Author self-catches the compression** — tempted to reach for a coined word or pack concepts into one token, the author meets a named rule that says spend the words instead.
- **Reviewer rejects un-reviewable prose** — hitting a dense noun pile, the reviewer can name the defect and send it back rather than skim past it.

Success signal: a reader can name the concise/compressed distinction and cite it when flagging a compressed line, and the prose surface does not grow to carry the lesson (it applies to itself). The distinction is applied by write-time judgment.

## Non-goals

- An enforced gate — this stays write-time advice; nothing automatically flags a noun pile.
- Prose lessons beyond the concise/compressed distinction (e.g. preserving standard terms when authoring in a non-English language) — a separate lesson, out of scope here.
