---
source: ce-kb:context-rot
last_refreshed: 2026-06-20
---

# Context Rot

Model reliability decays as input length grows — even on trivial tasks — because tokens are not processed uniformly; the "uniform token processing" assumption is false. Treat added length as a reliability cost, not a safety margin: keep the working set lean and high-signal, and prune aggressively rather than stuffing the window "just in case."

**Counters:** The degradation gets worse when matching needs semantic inference (not lexical overlap) and when distractors are present — so padding the context erodes the whole task, not merely the buried needle.

**Sources:** Context Rot: How Increasing Input Tokens Impacts LLM Performance — Chroma, 2025 — https://www.trychroma.com/research/context-rot

**Related:** [[three-axes-of-context-degradation]], [[effective-vs-advertised-context]], [[distractor-sensitivity]], [[literal-vs-latent-matching]]
