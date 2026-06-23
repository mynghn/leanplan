# 260623-concise-not-compressed — Design Rationale

## D-1: named-bullet-not-woven

A distinct named bullet wins over weaving the lesson into an existing rule, because the lesson must be *citable* and it is a *different axis* than the rules around it.

- **Forces.** `Spec#B-1` wants the failure mode named in the shared home; `Spec#B-2` wants a reviewer able to reject a line *by citing the rule*. Both need a stable handle. Pulling against that, `Spec#C-1` wants no surface growth — which a woven clause would honor more cheaply.
- **Why a separate axis.** The neighbors govern *form* — sentence length, list-vs-paragraph. Compression is about *semantic density per token*: a line can be a short sentence or a clean list item and still force the reader to decompress. Folding it into "Short, declarative sentences" would mis-file it as a length rule and lose exactly the case that matters (short *and* compressed).
- **Alternatives weighed.**
  - *Weave into "Short, declarative sentences"* — rejected: buries the name (no citable handle for B-2) and conflates density with length.
  - *New top-level `§` section* — rejected: the handoff and `Spec` Non-goal say refinement, not new section; a section overstates a one-bullet lesson.
  - *A full good/bad example block* (the ✅/❌ form `design.md`/`tasks.md` carry) — rejected: those live in stage docs for field-specific blob risk, and a full block fights `C-1`.
  - *Bad-only (pile, no good form)* — also rejected: it shows the smell, not the fix, and under-teaches the `Spec#B-2` discriminator, which is about *sorting* a line — best taught by contrast.
- **Chosen path.** One titled bullet, last in the list, carrying name + a minimal inline good→bad contrast (pile ✗ vs. decompressed ✓, the doc's own §134 register) + reader-effort discriminator + the "spend the words" imperative.
- **Grounding (context-engineering).** The lesson is the authoring-side corollary of `literal-vs-latent-matching`: spelling a concept out gives the reviewer a *literal* handle, while packing distinct concepts into one joined token forces *latent* recovery of each. NoLiMa measures that collapse — 99.3% short-context recall falling to 69.7% at 32K — which is the long-surface LLM-review case the small-surface bet targets. So the bullet carries `(context-engineering: literal-vs-latent-matching)`, convention-matching not decorative. (`effective-vs-advertised-context` is a weaker length-axis fit; `distractor-sensitivity` already grounds the section's de-dup rule.)
- **Exemplar shape (prompt-engineering: `exemplar-selection`).** A contrastive demonstration teaches whatever *varies* between its halves, and the reader imitates the salient pattern — so the ✓ must decompress the *same* content as the ✗ (vary density alone, not topic), and the set must not tilt toward "separator = bad." A `·`-only-bad example would induce the over-trigger `Spec#B-2` forbids; the contrast must carry the decompression-effort discriminator, not a ban on separators. This is the lens for vetting the final example wording.
- **Invalidation.** If the lesson ever needs more than a few lines to land (e.g. multiple worked contrasts), revisit — it may have outgrown a bullet and belong in a stage doc's example slot, or signal the lesson was mis-scoped.

## D-2: single-home-held-surface

Hold `§ Prose Style` flat-or-smaller while adding the bullet, by tightening genuine slack in the existing prose rather than letting the section grow — because the anti-compression lesson must not bloat its own home, and the cheapest offset that respects scope is in-place tightening.

- **Forces.** `Spec#C-1-surface-not-grown` plus the reflexive point (the Requirements success signal: the lesson applies to itself). Against it: `Spec` Non-goal *sharpens-does-not-replace* bounds how much of the neighbors I may touch — I can trim verbosity, not alter a rule's meaning or delete a rule.
- **Alternatives weighed.**
  - *Accept minor net growth* — rejected as the default: it concedes the reflexive point on the very feature that names anti-bloat, when slack exists to reclaim.
  - *Move existing Prose Style detail to an archive / framework-design.md* — rejected: heavier than warranted, and it would scatter the one home.
  - *Tighten adjacent slack in place* — chosen: the `Conclusion first` bullet and the section `Why:` line carry trim-able words; reclaiming them offsets the new bullet without changing any rule.
- **Chosen path.** One home, no stage-doc copies; offset by in-place tightening; confirm by diff + grep, since the stateless guard checks size, not change.
- **Invalidation.** If holding the surface flat would force trimming that changes a rule's meaning (crossing into *replace*), stop — accept the minimal growth instead, and note `C-1` as the relaxed line. The non-goal outranks the surface target.
- **Realized at implement (this clause fired).** Flat was not reachable: the worked-example bullet is ~84 words, exceeding the section's honest trim-able slack — both named offsets were taken (`Conclusion first` −30 words; the `Why:` line −4), and removing the `Why:` rationale to reach flat would change meaning. So `C-1`'s literal *holds-or-shrinks* is **relaxed to minimal justified growth: +50 words / +1 line** in `§ Prose Style` (195→245 prose words; measured). The added words are the lesson's own worked good/bad example — content the lesson requires, not padding — and sharpens-not-replace held (no existing rule's meaning dropped). The task's `holds-or-shrinks` Completion criterion reads through this clause; it was a proxy for "don't bloat," which minimal-offset-then-accept satisfies.
