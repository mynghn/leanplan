---
source: ce-kb:lost-in-the-middle
last_refreshed: 2026-06-20
---

# Lost In The Middle

Models read a long context unevenly: recall follows a U-shaped curve — strong for what sits at the start (primacy) or end (recency), much weaker for what is buried in the middle. Treat position as a control you own: place the task statement, highest-stakes instructions, and must-not-lose facts at the edges of the window, rank the most relevant retrieved documents at the edges too, and if a large middle is unavoidable, compact it — summarize and re-anchor key facts at a boundary instead of trusting the model to dig them out.

**Counters:** Positional (not semantic) recall failure — a correct, relevant fact gets missed purely because it landed mid-stack, where accuracy can dip toward the model's closed-book baseline even in long-context models.

**Sources:** Lost in the Middle: How Language Models Use Long Contexts — Liu et al., TACL 2023 — https://arxiv.org/abs/2307.03172; Efficient Streaming Language Models with Attention Sinks (StreamingLLM) — Xiao et al., 2023 — https://arxiv.org/abs/2309.17453

**Related:** [[attention-sinks]], [[three-axes-of-context-degradation]]
