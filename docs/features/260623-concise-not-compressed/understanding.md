# 260623-concise-not-compressed — Understanding

## Delta-1: compression-has-a-lexical-form

Compression has two forms and the lesson must teach both. **Lexical** — choosing an unfamiliar or coined word over a plain, easy-to-read depiction of the point (the primary intended case). **Syntactic** — packing several distinct concepts into one separator-joined token-string. Both shift the same cost to the reviewer (unpacking the meaning), so the existing discriminator — reader's effort, not length — already spans both; only the framing and example were too narrow.

This kills the prior assumption that compression meant only the syntactic noun-pile form. The shipped framing ("packing distinct concepts into a separator-joined token") and the single example (`detect · de-dup · publish → ack`, built from *familiar* words) demonstrated only the syntactic form and excluded the lexical one.

Why: the planner clarified that the primary intended case was the lexical "compressy word vs. plain depiction" failure. The original arrival example (`call order · bypass-check save · conflict-id union → …`) carried coined terms (`bypass-check save`, `conflict-id union`) that the shipped example dropped, losing the lexical dimension. The familiar-standard-term boundary (a familiar term costs the reader little) keeps this distinct from the out-of-scope multilingual term-preservation lesson — both resolve to reader-effort.

Scope-of-impact: Requirements (Problem + Outcome failure-mode characterization), Spec#B-1-distinction-named-in-shared-home, Spec#B-2-discriminator-sorts-a-line, Design#D-1-named-bullet-not-woven.
