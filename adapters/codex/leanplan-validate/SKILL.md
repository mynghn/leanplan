---
name: leanplan-validate
description: LeanPlan — validate a LeanPlan feature path in Codex. Use for `leanplan-validate <feature-path>` or direct validation requests.
---

# leanplan-validate

LeanPlan validation is the utility move that runs the shared structural validator. It does not author an artifact.

Resolve `<LEANPLAN_ROOT>` as the LeanPlan checkout containing this adapter: follow the real path of this `SKILL.md` from the installed skill symlink when present, then walk up three directories from `adapters/codex/<skill>/`. Substitute that absolute path wherever commands below use `<LEANPLAN_ROOT>`.

Run:

```bash
<LEANPLAN_ROOT>/scripts/leanplan-validate <feature-path>
```

Flags:

- `--stage requirements|spec|design|tasks|full` — partial check while iterating.
- `--json` — machine-readable output.
- `--strict` or `LEANPLAN_STRICT=1` — warnings exit non-zero and one-deployment guardrails become errors.
- `--allow-large` — suppress size guardrails.

Runtime glue:

- Accept either `docs/features/<KEY>` or an explicit feature path.
- Report validation failures with the failing file and message.
- Do not edit artifacts while validating; route repair work to the relevant LeanPlan move.
