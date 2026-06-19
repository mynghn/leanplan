---
source: ce-kb:context-isolation
last_refreshed: 2026-06-20
---

# Context Isolation

ISOLATE — the fourth write/select/compress/isolate primitive: when breadth exceeds one window, fan work out into sub-agents that each explore a slice in their own fresh context, then return only the few high-signal, condensed tokens to the parent. The parent never sees the raw exploration (search dumps, dead ends, verbose tool output) — only the distilled answer. Isolation buys parallelism and compression at once, and scales usable tokens past a single window's limit. Reserve it for work that genuinely overflows one window: multi-agent setups can burn ~15x the tokens of a plain chat.

**Counters:** Keeps the parent window lean — raw intermediate tokens never enter it to drive distractor errors or context rot, and breadth that would otherwise exceed one window's effective capacity is offloaded instead of crammed in.

**Sources:** How We Built Our Multi-Agent Research System — Anthropic — https://www.anthropic.com/engineering/multi-agent-research-system; Context Engineering for Agents (write/select/compress/isolate) — LangChain — https://www.langchain.com/blog/context-engineering-for-agents

**Related:** [[explore-then-compact-handoff]], [[context-as-working-set]], [[compaction-vs-eviction]], [[context-rot]]
