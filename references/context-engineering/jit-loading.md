---
source: ce-kb:jit-loading
last_refreshed: 2026-06-20
---

# Just-In-Time Loading

Carry pointers, not payloads: hold lightweight identifiers (file paths, stored queries, links) and resolve a reference to full content only at the moment a step needs it. This is the runtime read-side of treating context as a curated working set — the same progressive-disclosure idea behind Agent Skills, where a one-line description matches first and the body loads only on activation. Default to it when the corpus is large, browsable, or only partly relevant to any one step; a hybrid that pre-loads a little for speed and leaves the rest behind references balances against slower runtime exploration.

**Counters:** Window bloat from preloaded data the agent may never use, and the recall decay it causes — a stuffed context degrades retrieval even when the right tokens are present.

**Sources:** Effective Context Engineering for AI Agents — Anthropic — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; Equipping Agents for the Real World with Agent Skills — Anthropic — https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills

**Related:** [[context-as-working-set]], [[structured-note-taking]]
