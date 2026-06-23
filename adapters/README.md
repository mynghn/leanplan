# LeanPlan Adapter Map

LeanPlan adapters are runtime shells over shared framework behavior. This map is the review surface for cross-vendor parity: each move should resolve to the same canonical reference or script, with any vendor-specific surface difference recorded explicitly.

| Move | Canonical reference / script | Claude adapter | Codex move skill | Codex front-door alias | Artifact boundary | Handoff / terminal result | Divergence |
|---|---|---|---|---|---|---|---|
| `requirements` | `references/requirements.md` | `adapters/claude/requirements/SKILL.md` | `adapters/codex/leanplan-requirements/SKILL.md` | `$leanplan requirements <intent>` | Writes `docs/features/<KEY>/requirements.md` after allocator-created feature dir | `specify <KEY>` | Codex skill name is prefixed; semantics match. |
| `specify` | `references/specify.md` | `adapters/claude/specify/SKILL.md` | `adapters/codex/leanplan-specify/SKILL.md` | `$leanplan specify <KEY>` | Writes `docs/features/<KEY>/spec.md` | `design <KEY>` | Codex skill name is prefixed; semantics match. |
| `design` | `references/design.md` | `adapters/claude/design/SKILL.md` | `adapters/codex/leanplan-design/SKILL.md` | `$leanplan design <KEY>` | Writes `docs/features/<KEY>/design.md` and rationale/research archives when needed | `tasks <KEY>` | Codex skill name is prefixed; semantics match. |
| `tasks` | `references/tasks.md` | `adapters/claude/tasks/SKILL.md` | `adapters/codex/leanplan-tasks/SKILL.md` | `$leanplan tasks <KEY>` | Writes `docs/features/<KEY>/tasks.md` | `implement <KEY> <task-id>` | Codex skill name is prefixed; semantics match. |
| `implement` | `references/implement.md` plus `references/implement-closeout.md` at close-out | `adapters/claude/implement/SKILL.md` | `adapters/codex/leanplan-implement/SKILL.md` | `$leanplan implement <KEY> <task-id>` | Changes code for one `T: <id>` card and verifies completion | Next unblocked task or final close-out | Codex skill name is prefixed; semantics match. |
| `sharpen` | `references/sharpen.md` | `adapters/claude/sharpen/SKILL.md` | `adapters/codex/leanplan-sharpen/SKILL.md` | `$leanplan sharpen <what-shifted>` | Appends `docs/features/<KEY>/understanding.md`; reads but never edits surface artifacts | Return to interrupted move | Codex skill name is prefixed; semantics match. |
| `revise` | `references/revise.md` | `adapters/claude/revise/SKILL.md` | `adapters/codex/leanplan-revise/SKILL.md` | `$leanplan revise <KEY> [Delta-N | what drifted]` | Edits justified artifact drift and implicated downstream artifacts only | Re-validate and resume interrupted move | Codex skill name is prefixed; semantics match. |
| `validate` | `scripts/validate.py` | Embedded in Claude stage adapters | `adapters/codex/leanplan-validate/SKILL.md` | `$leanplan validate <feature-path>` | Reads a feature path and reports structural validation | Terminal validation result | Codex keeps a dedicated utility move because the front door already exposes validation; Claude validation remains stage-local glue. |

Vendor-specific invocation glue must not restate stage procedure. Edit `references/*.md` or `scripts/validate.py` when LeanPlan behavior changes.
