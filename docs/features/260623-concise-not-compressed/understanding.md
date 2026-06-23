# 260623-concise-not-compressed — Understanding

## Delta-1: compression-has-a-lexical-form

Compression has two forms and the lesson must teach both. **Lexical** — choosing an unfamiliar or coined word over a plain, easy-to-read depiction of the point (the primary intended case). **Syntactic** — packing several distinct concepts into one separator-joined token-string. Both shift the same cost to the reviewer (unpacking the meaning), so the existing discriminator — reader's effort, not length — already spans both; only the framing and example were too narrow.

This kills the prior assumption that compression meant only the syntactic noun-pile form. The shipped framing ("packing distinct concepts into a separator-joined token") and the single example (`detect · de-dup · publish → ack`, built from *familiar* words) demonstrated only the syntactic form and excluded the lexical one.

Why: the planner clarified that the primary intended case was the lexical "compressy word vs. plain depiction" failure. The original arrival example (`call order · bypass-check save · conflict-id union → …`) carried coined terms (`bypass-check save`, `conflict-id union`) that the shipped example dropped, losing the lexical dimension. The familiar-standard-term boundary (a familiar term costs the reader little) keeps this distinct from the out-of-scope multilingual term-preservation lesson — both resolve to reader-effort.

Scope-of-impact: Requirements (Problem + Outcome failure-mode characterization), Spec#B-1-distinction-named-in-shared-home, Spec#B-2-discriminator-sorts-a-line, Design#D-1-named-bullet-not-woven.

## Delta-2: brevity-removes-redundancy-not-an-axis

The discriminator's root is information-preservation, not reader-effort. Brevity is legitimate only when it removes **redundancy** — information repeated, derivable, or already implied, whose removal changes nothing the reader didn't already have. It is illegitimate the moment it drops or fuses an **orthogonal axis** of information — a distinct dimension of meaning (*which* check, in what order, on what) the reader cannot recover. Reader-effort and unfamiliarity are downstream symptoms of an axis being dropped or fused, not the test itself.

This refines, not kills, `Delta-1`: the lexical and syntactic forms are two common *ways* an axis gets dropped — a coined word fuses the *which*, a pile fuses the *order/relation*. It also catches a case the reader-effort framing missed: axis-loss in perfectly familiar words ("the save" for "the save that skips the duplicate check") — easy to read, silently lossy.

Why: `bypass-check save` is bad primarily because it deletes the "which check" axis (the bypassed check is the duplicate/redundancy one), not merely because it is unfamiliar. The planner sharpened the rule to: cut redundancy, never an orthogonal axis; any information-axis loss bought with fewer tokens is never approved. Reflexive constraint — the bullet must *depict* this plainly ("cut what's repeated, never a distinct piece of meaning"), never state it in information-theory jargon, or the anti-compression rule violates itself.

Scope-of-impact: Requirements (Outcome brevity-definition), Spec#B-1-distinction-named-in-shared-home, Spec#B-2-discriminator-sorts-a-line, Design#D-1-named-bullet-not-woven.
