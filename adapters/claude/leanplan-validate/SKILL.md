---
name: leanplan-validate
description: LeanPlan — validate a LeanPlan feature path against the structural contract. Use for `/leanplan-validate <feature-path>` or an explicit "check / validate my LeanPlan artifacts" request.
argument-hint: "<feature-path>"
allowed-tools: Read, Bash(*/scripts/leanplan-validate *), Bash(ls *)
---

# leanplan validate

LeanPlan validation is the utility move that runs the shared structural validator. It authors no artifact — it reads a feature path and reports. Validation is also embedded as stage-local glue in every stage skill; this move is the standalone, on-demand entry point for checking artifacts between or after stages.

Resolve `<LEANPLAN_ROOT>` as the LeanPlan checkout containing this adapter: follow the real path of this `SKILL.md` from the installed skill symlink when present, then walk up three directories from `adapters/claude/<skill>/`. Substitute that absolute path wherever commands below use `<LEANPLAN_ROOT>`.

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
- Do not edit artifacts while validating; route repair work to `/leanplan-revise`.
