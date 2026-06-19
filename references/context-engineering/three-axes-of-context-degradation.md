---
source: ce-kb:three-axes-of-context-degradation
last_refreshed: 2026-06-20
---

# Three Axes Of Context Degradation

A routing frame for long-context failure: classify any symptom by the axis it exploits, then apply that axis's fix. **Position** — recall depends on where a fact sits ([[lost-in-the-middle]], [[attention-sinks]]); keep critical facts at the edges. **Length** — accuracy decays as input grows ([[context-rot]], [[effective-vs-advertised-context]]); curate to the smallest high-signal set. **Noise** — irrelevant content drags accuracy down ([[distractor-sensitivity]], [[literal-vs-latent-matching]]); strip distractors.

**Counters:** Treating the window as uniform free space where more tokens means more signal. The three axes are empirically real — accuracy falls with length, a single distractor already hurts, early items are found more reliably, and recall collapses when retrieval needs semantic inference rather than lexical overlap.

**Sources:** Context Rot — Chroma 2025 — https://www.trychroma.com/research/context-rot; NoLiMa: Beyond Literal Matching — 2025 — https://arxiv.org/abs/2502.05167; Effective Context Engineering for AI Agents — Anthropic — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

**Related:** [[lost-in-the-middle]], [[attention-sinks]], [[context-rot]], [[distractor-sensitivity]], [[literal-vs-latent-matching]], [[effective-vs-advertised-context]]
