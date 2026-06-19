---
source: ce-kb:compaction-vs-eviction
last_refreshed: 2026-06-20
---

# Compaction Vs Eviction

Two ways to reclaim a full context window, losing different things. Eviction drops tokens (truncate old turns, discard messages) — cheap, survivors stay verbatim, but dropped content is gone with no trace; safe only for what is provably stale or reconstructible from disk/tools. Compaction summarizes-and-reinitializes via an LLM pass, preserving semantic continuity across more history than fits raw — use when continuity matters but raw history won't fit, paired with external notes so dropped detail can be recovered, not just summarized. Timing is not a %-of-window call: prefer a **task boundary** (the working set honestly shrinks), else **observed degradation**, with a **~70-80%-used backstop** as last resort. A bigger window (1M) moves only the backstop, not the quality-optimal point — keep the working set lean regardless.

**Counters:** Lossy budget reclamation that silently loses load-bearing context — eviction's unsignaled drops, or aggressive compaction that summarizes away detail whose importance surfaces later — plus compacting too late (rot is absolute-token-driven, below advertised size) or too often (each pass invalidates the prefix/KV cache).

**Sources:** LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models — 2023 — https://arxiv.org/abs/2310.05736; Effective Context Engineering for AI Agents — Anthropic — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; Context Rot — Chroma, 2025 — https://www.trychroma.com/research/context-rot; RULER — 2024 — https://arxiv.org/abs/2404.06654; Prompt Caching — Anthropic — https://claude.com/blog/prompt-caching

**Related:** [[structured-note-taking]], [[context-as-working-set]], [[explore-then-compact-handoff]], [[jit-loading]], [[context-rot]], [[effective-vs-advertised-context]], [[prefix-cache-economics]]
