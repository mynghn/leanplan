# LP-EXAMPLE — DESIGN RATIONALE

## Decision-2: in-repo-path-hard-coded

Alternatives considered:

- **env var (`LEANPLAN_SOURCE_PATH`)** — flexible for other machines or for CI, but no CI use case is in scope for personal-phase, and the operator always runs on one machine. Premature flexibility.
- **mise task with path in `mise.toml`** — mise is already the workspace's task runner, semantically clean. But adds a dependency (mise must be on PATH); shell-only execution is simpler.
- **chezmoi template resolving a personal config value** — would let the path live in `~/.config/chezmoi/chezmoi.toml`. Adds a chezmoi-template layer to what is otherwise a plain script. Over-engineered for one path.

Hard-coded path wins on simplicity. Personal-phase is a single-machine, single-user rollout; the path is stable until team-publish.

Invalidation triggers (revisit when):

- Source location moves (e.g., `upstream` renamed, or framework moves to its own repo).
- Cross-machine use becomes needed (start working from another laptop, CI integration).
- Team-publish happens — at which point the source may live inside a project `.claude/skills/` or be distributed differently.

## Decision-6: atomicity-via-chezmoi-source-write-then-apply

SPEC#INV-3-atomicity-under-failure says the runtime copy is "either unchanged or fully updated — never half-written". The implementation gives two atomicity windows:

1. **Source write (`> $SOURCE`)** — bash redirects atomically for small files (< pipe buffer); race with other writers isn't a concern in personal-phase.
2. **`chezmoi apply`** — chezmoi writes the target via temp-file-then-rename, atomic on POSIX.

What is *not* atomic end-to-end: the window between source-write success and `chezmoi apply` invocation. If the process crashes there, the chezmoi source is ahead of the runtime. Next invocation re-runs both, self-heals. The runtime copy itself is never half-written thanks to chezmoi's write-then-rename.

Alternatives considered:

- Write to a temp runtime path and `mv` into place — bypasses chezmoi, which would then see the runtime as drifted from source on next `chezmoi status`. Different drift problem.
- Lock file — overkill; no concurrent writers in personal-phase.

Accept the small window; self-healing is the mitigation.

Invalidation triggers:

- Concurrent sync invocations become possible (daemon, git hook). Then need a lock.
