---
source: ce-kb:effective-vs-advertised-context
last_refreshed: 2026-06-20
---

# Effective vs Advertised Context

A model's *effective* context — the length where it still answers reliably — is far shorter than its *advertised* window (32K/128K/1M). Treat the advertised number as a hard ceiling, never a working budget: don't fill it just because it fits. Aggressively select and compact so the live working set stays inside the effective zone.

**Counters:** Trusting a marketing token count as a usability guarantee. Passing the shallow needle-in-haystack probe (retrieve one planted fact) masks collapse on substantive long-context work — multi-hop tracing and aggregation — where accuracy degrades with input length well before the limit; RULER found only half of models claiming a 32K+ window still perform satisfactorily at 32K.

**Sources:** RULER: What's the Real Context Size of Your Long-Context Language Models? — Hsieh et al., 2024 — https://arxiv.org/abs/2404.06654

**Related:** [[context-rot]], [[three-axes-of-context-degradation]], [[context-as-working-set]]
