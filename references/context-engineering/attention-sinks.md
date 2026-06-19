---
source: ce-kb:attention-sinks
last_refreshed: 2026-06-20
---

# Attention Sinks

Transformers park a large, semantically-indifferent share of attention on the first few tokens — the "attention sink" — because SoftMax must sum to one, so unmatched query mass lands on the earliest always-visible positions. When managing your own context, never blindly drop the prefix: preserve the opening tokens (system prompt / framing) when compacting or evicting, since they anchor the attention distribution. Keeping just ~4 initial tokens plus a recent-token window restores stable generation over very long contexts.

**Counters:** Naive prefix truncation or sliding-window eviction that discards the oldest tokens — losing the sink destabilizes attention and makes long-context perplexity blow up.

**Sources:** StreamingLLM / Efficient Streaming Language Models with Attention Sinks — Xiao et al., 2023 — https://arxiv.org/abs/2309.17453

**Related:** [[compaction-vs-eviction]], [[lost-in-the-middle]], [[three-axes-of-context-degradation]]
