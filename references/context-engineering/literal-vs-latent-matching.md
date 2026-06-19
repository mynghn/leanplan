---
source: ce-kb:literal-vs-latent-matching
last_refreshed: 2026-06-20
---

# Literal vs Latent Matching

A fact in the window is only reliably retrievable when the query shares its exact wording; when retrieval instead requires semantic inference or paraphrase, recall collapses as context grows. So when a needed fact depends on implication rather than shared keywords, pull it to a literal position near the query — restate it in the prompt or store it as an explicit note — rather than trusting the model to bridge the gap.

**Counters:** Silent recall failures on inference-based (latent) lookups across long context — the model has the fact in-window but cannot infer the association without a lexical cue, even with no irrelevant clutter present.

**Sources:** NoLiMa: Long-Context Evaluation Beyond Literal Matching — 2025 — https://arxiv.org/abs/2502.05167

**Related:** [[distractor-sensitivity]], [[context-rot]], [[three-axes-of-context-degradation]]
