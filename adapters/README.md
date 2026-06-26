# LeanPlan Adapter Map

LeanPlan adapters are runtime shells over shared framework behavior. This map is the review surface for cross-vendor parity: each move should resolve to the same canonical reference or script, with any vendor-specific surface difference recorded explicitly.

| Move | Canonical reference / script | Claude adapter | Codex skill | Artifact boundary | Handoff / terminal result | Divergence |
|---|---|---|---|---|---|---|
| `frame` | `references/frame.md` | `adapters/claude/leanplan-frame/SKILL.md` | `adapters/codex/leanplan-frame/SKILL.md` | Writes `docs/features/<KEY>/requirements.md` after allocator-created feature dir | Claude `/leanplan-specify <KEY>`; Codex `leanplan-specify <KEY>` | Skill name matches across vendors; semantics match. |
| `specify` | `references/specify.md` | `adapters/claude/leanplan-specify/SKILL.md` | `adapters/codex/leanplan-specify/SKILL.md` | Writes `docs/features/<KEY>/spec.md` | Claude `/leanplan-design <KEY>`; Codex `leanplan-design <KEY>` | Skill name matches across vendors; semantics match. |
| `design` | `references/design.md` | `adapters/claude/leanplan-design/SKILL.md` | `adapters/codex/leanplan-design/SKILL.md` | Writes `docs/features/<KEY>/design.md` and rationale/research archives when needed | Claude `/leanplan-tasks <KEY>`; Codex `leanplan-tasks <KEY>` | Skill name matches across vendors; semantics match. |
| `tasks` | `references/tasks.md` | `adapters/claude/leanplan-tasks/SKILL.md` | `adapters/codex/leanplan-tasks/SKILL.md` | Writes `docs/features/<KEY>/tasks.md` | Claude `/leanplan-implement <KEY> <task-id>`; Codex `leanplan-implement <KEY> <task-id>` | Skill name matches across vendors; semantics match. |
| `implement` | `references/implement.md` plus `references/implement-closeout.md` at close-out | `adapters/claude/leanplan-implement/SKILL.md` | `adapters/codex/leanplan-implement/SKILL.md` | Changes code for one `T: <id>` card and verifies completion | Next unblocked task or final close-out | Skill name matches across vendors; semantics match. |
| `rethink` | `references/rethink.md` | `adapters/claude/leanplan-rethink/SKILL.md` | `adapters/codex/leanplan-rethink/SKILL.md` | Appends `docs/features/<KEY>/understanding-shifts.md`; reads but never edits surface artifacts | Return to interrupted move | Skill name matches across vendors; semantics match. |
| `revise` | `references/revise.md` | `adapters/claude/leanplan-revise/SKILL.md` | `adapters/codex/leanplan-revise/SKILL.md` | Edits justified artifact drift and implicated downstream artifacts only | Re-validate and resume interrupted move | Skill name matches across vendors; semantics match. |
| `validate` | `scripts/leanplan-validate` | `adapters/claude/leanplan-validate/SKILL.md` | `adapters/codex/leanplan-validate/SKILL.md` | Reads a feature path and reports structural validation | Terminal validation result | Skill name matches across vendors; both also embed validation as stage-local glue in every stage adapter. |

Both vendors name the eight shared moves `leanplan-<move>` — Claude installs loose symlinked skills (`~/.claude/skills/leanplan-<move>`) and Codex loose move skills (`~/.agents/skills/leanplan-<move>`), so neither has a plugin namespace and both carry the `leanplan-` vendor prefix to avoid collision. There is no gateway/front-door skill; invoke the move skill directly (Claude prefixes the runtime `/` sigil, Codex omits it). The skill set is symmetric across vendors: validation is embedded as stage-local glue in every stage adapter on both sides, and each also exposes a standalone `leanplan-validate` move as the on-demand entry point.

Vendor-specific invocation glue must not restate stage procedure. Edit `references/*.md` or `scripts/leanplan-validate` when LeanPlan behavior changes.

Installation utilities are not LeanPlan moves and do not live in this adapter map. They are authored
under `utils/`; for example, `utils/leanplan-installation-freshness/` checks the checkout and runtime
symlinks that `install.sh` manages.
