---
source: ce-kb:explore-execute-boundary
last_refreshed: 2026-06-20
---

# Explore-Execute Boundary

At an explore→execute / plan→implement boundary, prefer a hard hand-off to a fresh context over in-place compaction. Keep one phase continuous in a warm session — cross-stage reasoning back-propagates cheaply while context is live and the prefix cache stays warm — then make the hard cut where the artifact stabilizes and the work-nature flips. The hand-off is goal-first: select what the destination needs, not what the session did; volume scales with goal-proximity (plan→impl of one feature carries the plan, a sharp departure carries almost nothing). Externalize the goal-scoped brief to a durable file, order it material-first / instruction-last, and JIT the bulk. Gate: hand off only when a fresh frame's clean slate beats the cost of re-acquiring what is already warm.

**Counters:** A planning session maxes all three degradation axes at once — length (everything read), noise (dead ends and superseded branches), and buried conclusions (live decisions scattered mid-trajectory) — exactly as the successor execution phase, which must not re-explore, turns most precision-sensitive. A faithful session summary would re-import that noise into the fresh frame, defeating the reason to go fresh.

**Sources:** Effective Context Engineering for AI Agents — Anthropic — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; How We Built Our Multi-Agent Research System — Anthropic — https://www.anthropic.com/engineering/multi-agent-research-system

**Related:** [[explore-then-compact-handoff]], [[compaction-vs-eviction]], [[structured-note-taking]], [[context-isolation]]
