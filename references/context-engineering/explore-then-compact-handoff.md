---
source: ce-kb:explore-then-compact-handoff
last_refreshed: 2026-06-20
---

# Explore-Then-Compact-Handoff

When a step needs wide, token-heavy reading (research, broad file/web scans) but only a narrow conclusion matters downstream, spawn a sub-agent to explore inside its own context window, then have it return only the compacted finding — the answer, not the raw trail. Each explorer burns its own budget in parallel; the parent pays only for the summary. Reserve for breadth-first work valuable enough to justify the spend (multi-agent runs cost roughly 15x a chat interaction), not tight sequential dependencies. This is the spatial handoff (sub-agent to parent, within one session); for the temporal one — a whole session to a fresh context at an explore-to-execute boundary — see [[explore-execute-boundary]].

**Counters:** Keeps the dozens of pages, search hits, and dead ends an explorer wades through out of the parent's window, so noisy intake never bloats or distracts the main context — the parent stays lean and on-task.

**Sources:** How We Built Our Multi-Agent Research System — Anthropic — https://www.anthropic.com/engineering/multi-agent-research-system

**Related:** [[context-isolation]], [[compaction-vs-eviction]], [[structured-note-taking]], [[explore-execute-boundary]]
