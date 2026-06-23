# 260623-concise-not-compressed — Spec

## Behavior

### B-1: distinction-named-in-shared-home

The shared, all-artifact prose guidance names *information-compression-as-false-brevity* as a failure mode, distinct from the adjacent prose rules (list use, sentence length) it sits beside. It states the discriminator: brevity is short *explanatory* sentences and lists, never a denser form — an unfamiliar coined word, or several distinct concepts packed into one separator-joined token — that the reader must unpack. The lesson is authored once, in that one home — not copied into the per-stage docs. One-shot test: read the prose guidance → the concise/compressed distinction and its discriminator are present in the single shared home, additive to the existing rules.

### B-2: discriminator-sorts-a-line

Using the guidance, a reader sorts a candidate line by one question — does reading it force the reviewer to unpack the meaning? Two compression forms are flagged: an unfamiliar or coined word chosen over a plain depiction (`bypass-check save`), and a separator-joined pile that hides distinct concepts (`detect · de-dup · publish → ack`). A familiar standard term, a genuinely atomic enumeration, and a legitimate inline `·` / `→` such as a stage map (`requirements→spec→design→tasks`) are not flagged. One-shot test: given the guidance plus one compressed line and one clean line, a reviewer flags the first and clears the second, citing the rule — the discriminator distinguishes by reader-effort, it does not blanket-flag jargon or separators. (broadened to the lexical form — `Understanding#Delta-1-compression-has-a-lexical-form`)

## Constraint

### C-1: surface-not-grown

The refinement holds or reduces the prose-guidance surface. It adds no new section, and it copies the lesson into no per-stage doc — the lesson applies to itself. The stateless surface-budget guard sees absolute size, not this change-delta, so non-growth and single-home are verified by inspecting the diff and grepping for duplication.

## Non-goals

- **No enforced conformance check.** The distinction is verified by reader judgment at write/review time; nothing auto-flags a noun pile. The target property — *must the reader decompress?* — is reader- and context-relative, so it is not deterministically checkable, and no validator or linter rule is added. Whether to ever add one is left open.
- **Single lesson, any authoring language.** The lesson holds whatever language an artifact is authored in, but the separate standard-term-preservation lesson (not over-translating in a non-English language) stays out of scope.
- **Sharpens, does not replace.** The existing Prose Style rules and the Surface Budget rationale stand; this names a failure mode adjacent to them — it does not re-derive them.
