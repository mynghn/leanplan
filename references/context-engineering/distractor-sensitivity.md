---
source: ce-kb:distractor-sensitivity
last_refreshed: 2026-06-20
---

# Distractor Sensitivity

Treat retrieved context as a liability, not a safety margin: curate aggressively toward a small, high-signal set rather than padding with "might-be-useful" passages. Distractors — content topically near the target but not actually answering the question — measurably lower accuracy even when the correct answer is fully in the window, and the penalty compounds with both their count and total input length.

**Counters:** The noise axis of context degradation — near-miss passages competing with the true target for attention, producing recall misses and confident hallucinations (worst when many distractors and long contexts coincide).

**Sources:** Context Rot — Chroma, 2025 — https://www.trychroma.com/research/context-rot

**Related:** [[literal-vs-latent-matching]], [[three-axes-of-context-degradation]], [[context-rot]]