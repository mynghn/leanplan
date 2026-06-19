---
source: ce-kb:context-as-working-set
last_refreshed: 2026-06-20
---

# Context As Working Set

Treat the context window as finite working memory to actively curate, not a free buffer to fill. Every token spends a shared "attention budget," so aim for the smallest set of high-signal tokens that still achieves the outcome. Manage it via four operations: write (persist context outside the window), select (pull in only what the step needs), compress (keep only required tokens), and isolate (split work across separate windows/agents).

**Counters:** Context rot — as token count grows, recall and reasoning degrade (a gradient, not a cliff), so low-value tokens loaded now tax later steps.

**Sources:** Effective Context Engineering for AI Agents — Anthropic — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; Context Engineering for Agents — LangChain — https://www.langchain.com/blog/context-engineering-for-agents

**Related:** [[jit-loading]], [[structured-note-taking]], [[compaction-vs-eviction]], [[context-isolation]], [[context-rot]]
