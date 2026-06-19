---
source: ce-kb:prefix-cache-economics
last_refreshed: 2026-06-20
---

# Prefix Cache Economics

Treat prompt layout as a cost surface and order content stable-to-volatile: durable, reused material first (system prompt, tool definitions, curated index), volatile material last (live query, fresh retrievals, scratch notes). The KV/prefix cache matches on an exact token prefix, so a stable, append-mostly prefix keeps reused tokens cache-warm — cache reads run ~10% of base input price and slash time-to-first-token, while the first write costs ~25% more, so caching only pays when the prefix is reused.

**Counters:** Editing or reordering the early/stable prefix between turns invalidates the cache from the changed token forward, silently forfeiting the ~90% read discount and re-incurring full compute on everything downstream.

**Sources:** Prompt Caching — Anthropic — https://claude.com/blog/prompt-caching

**Related:** [[context-as-working-set]], [[jit-loading]]
