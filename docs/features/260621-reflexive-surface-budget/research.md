# 260621-reflexive-surface-budget — Research

## Stage-reference inventory (worktree source, 2026-06-21)

Always-loaded stage references, prose line counts: requirements.md 96, specify.md 80, design.md 70, tasks.md 95, implement.md 106. On-demand companions: artifact-contract.md 157, philosophy.md 26, context-engineering.md 28. Off-pipeline: sharpen.md 45, revise.md 57. (Runtime `~/.local/share/leanplan/references/` was stale vs source for design.md and implement.md — a pull/reinstall updates it.)

implement.md's close-out detail is three tables: Distillation Hierarchy (L67–76), Commit-message-vs-inline-comment (L80–85), Squash-durability-promotion (L89–97); span ~L63–97, ~35 lines. Referenced only by procedure steps 7–8 and 10 (close-out / commit). The Stop-The-Line Triggers (L40–49) and Artifact Update Loop (L51–61) are consumed at step 4 (re-reason, early/mid-implementation) — not close-out — so they stay inline.

## Existing on-demand (JIT) idiom

The framework already defers the shared companions with a prose pointer carrying a trigger condition — e.g. implement.md L17: "artifact-contract.md — JIT only, before writing or editing an artifact's structure… philosophy.md only when a principle's intent is in question. (CE: jit-loading)". The SKILL.md adapters list the same companions with absolute runtime paths (`~/.local/share/leanplan/references/<name>.md`). There is no existing *within-reference* second tier: each stage reference inlines stance + procedure + guardrails + worked examples + template (+ implement.md's close-out tables). The fix reuses this idiom rather than introducing a new mechanism.

## Deployment model

`install.sh` (56 L) symlinks adapters only: `adapters/claude/<stage>` → `~/.claude/skills/<stage>` (stages: requirement specify design plan implementation sharpen revise) and `adapters/codex/leanplan` → `~/.agents/skills/leanplan`. It does not touch `references/`. The runtime `~/.local/share/leanplan/` is a whole-repo git clone (chezmoi `.chezmoiexternal.toml` entry `[".local/share/leanplan"]`, or `git clone …` per README "Without chezmoi"); `chezmoi update` / `git pull` refreshes it. Consequence: a new `references/*.md` deploys with the repo — no install.sh or chezmoi-config change needed.
