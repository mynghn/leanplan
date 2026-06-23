# LeanPlan Adapter Map

LeanPlan adapters are runtime shells over shared framework behavior. This map is the review surface for cross-vendor parity: each move should resolve to the same canonical reference or script, with any vendor-specific surface difference recorded explicitly.

| Move | Canonical reference / script | Claude adapter | Codex skill | Artifact boundary | Handoff / terminal result | Divergence |
|---|---|---|---|---|---|---|
| `requirements` | `references/requirements.md` | `adapters/claude/requirements/SKILL.md` | `adapters/codex/leanplan-requirements/SKILL.md` | Writes `docs/features/<KEY>/requirements.md` after allocator-created feature dir | Claude `/specify <KEY>`; Codex `leanplan-specify <KEY>` | Codex skill name is prefixed; semantics match. |
| `specify` | `references/specify.md` | `adapters/claude/specify/SKILL.md` | `adapters/codex/leanplan-specify/SKILL.md` | Writes `docs/features/<KEY>/spec.md` | Claude `/design <KEY>`; Codex `leanplan-design <KEY>` | Codex skill name is prefixed; semantics match. |
| `design` | `references/design.md` | `adapters/claude/design/SKILL.md` | `adapters/codex/leanplan-design/SKILL.md` | Writes `docs/features/<KEY>/design.md` and rationale/research archives when needed | Claude `/tasks <KEY>`; Codex `leanplan-tasks <KEY>` | Codex skill name is prefixed; semantics match. |
| `tasks` | `references/tasks.md` | `adapters/claude/tasks/SKILL.md` | `adapters/codex/leanplan-tasks/SKILL.md` | Writes `docs/features/<KEY>/tasks.md` | Claude `/implement <KEY> <task-id>`; Codex `leanplan-implement <KEY> <task-id>` | Codex skill name is prefixed; semantics match. |
| `implement` | `references/implement.md` plus `references/implement-closeout.md` at close-out | `adapters/claude/implement/SKILL.md` | `adapters/codex/leanplan-implement/SKILL.md` | Changes code for one `T: <id>` card and verifies completion | Next unblocked task or final close-out | Codex skill name is prefixed; semantics match. |
| `sharpen` | `references/sharpen.md` | `adapters/claude/sharpen/SKILL.md` | `adapters/codex/leanplan-sharpen/SKILL.md` | Appends `docs/features/<KEY>/understanding-shifts.md`; reads but never edits surface artifacts | Return to interrupted move | Codex skill name is prefixed; semantics match. |
| `revise` | `references/revise.md` | `adapters/claude/revise/SKILL.md` | `adapters/codex/leanplan-revise/SKILL.md` | Edits justified artifact drift and implicated downstream artifacts only | Re-validate and resume interrupted move | Codex skill name is prefixed; semantics match. |
| `validate` | `scripts/leanplan-validate` | Embedded in Claude stage adapters | `adapters/codex/leanplan-validate/SKILL.md` | Reads a feature path and reports structural validation | Terminal validation result | Codex keeps a dedicated utility move; Claude validation remains stage-local glue. |

Vendor-specific invocation glue must not restate stage procedure. Edit `references/*.md` or `scripts/leanplan-validate` when LeanPlan behavior changes.
