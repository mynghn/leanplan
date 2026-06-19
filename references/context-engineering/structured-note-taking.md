---
source: ce-kb:structured-note-taking
last_refreshed: 2026-06-20
---

# Structured Note-Taking

The *write* operation of context engineering: persist plans, decisions, and progress to a durable file outside the window (a `NOTES.md`, to-do list, or scratchpad), then read them back on demand. It is the write-side complement of JIT loading — JIT reads references in when needed; note-taking writes state out so it survives. Externalize anything you must not forget and treat the window as scratch.

**Counters:** Loss of long-horizon coherence when the window is summarized, compacted, or reset — without externalized state the agent forgets plans and progress and cannot resume multi-hour or cross-session work.

**Sources:** Effective Context Engineering for AI Agents — Anthropic — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; How We Built Our Multi-Agent Research System — Anthropic — https://www.anthropic.com/engineering/multi-agent-research-system; Context Engineering for Agents — LangChain — https://www.langchain.com/blog/context-engineering-for-agents

**Related:** [[jit-loading]], [[context-as-working-set]], [[compaction-vs-eviction]], [[explore-then-compact-handoff]]
