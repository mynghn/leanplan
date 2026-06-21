# 260620-artifact-later-update — RESEARCH

Verified current-state of the LeanPlan mechanisms this feature builds on (repo source, 2026-06-20). Evidence only — interpretation lives in `design-rationale.md`.

## impl Artifact Update Loop — the only existing revision machinery
`references/impl.md` 39–63. Fires from six impl stop-the-line triggers (code contradicts DESIGN; no verification path for a Completion criterion; missing/invalidated dependency; impl would change observable behavior; an Invariant is unprovable; task scope exceeds the feature boundary). Loop: (1) identify highest affected layer REQ/SPEC/DESIGN/TASK; (2) surface to user; (3) edit that layer; (4) re-evaluate downstream referencing artifacts — `impl.md:61`: "Default is re-evaluate in place, not fully re-derive"; (5) resume impl; (6) scope-gate — if REQUIREMENT exceeds one-deployment, split, don't grow. No invocation path exists outside impl; `leanplan.md` §9 scopes it "within the plan-implement cycle only."

## Stable-ID / retire-by-note scope
Global stable-ID rule at `artifact-contract.md:46` — "IDs are stable; do not renumber existing anchors after edits" — binds all anchor types. The `(retired)` retire-by-note FORM appears only at `specify.md:53` ("retire by inline `(retired)` note rather than deleting"), i.e. SPEC O/INV only; it is absent from `design.md`, `plan.md`, and the global Anchors section.

## validate.py — structural and stateless
Per-commit, single-feature structural checks: required files per `--stage`; duplicate-anchor; citation resolution (single-hop, same-feature); REQ/SPEC/DESIGN/TASK shape; design↔rationale set-consistency; SPEC→plan forward-coverage (flat `SPEC#<target>` string search, `**GAP**`-aware); surface-size soft caps; DAG-size. No staleness, drift, or cross-artifact semantic-consistency notion. `_check_citations` skips inbound `UNDERSTANDING#` and `RESEARCH#` citations — `validate.py:307`: `if file_key in ("RESEARCH","UNDERSTANDING"): continue`. No citation-graph traversal exists anywhere.

## leanplan-new — allocate-only
Three ID forms (NNNN-slug / tracker-key / `--date` YYMMDD-slug). Creates the stub feature dir; exits 2 if the dir already exists. No rename or split capability.

## sharpen → Delta handoff (the justified-input source)
`references/sharpen.md`: sharpen appends one `Delta-<N>: <slug>` block to `understanding.md` (append-only; its only write target) and never edits committed artifacts. Delta block shape (`artifact-contract.md:89`): the new understanding, the prior assumption it kills, why (disturbance + verification verdict), and scope-of-impact as bare `SPEC#`/`DESIGN#`/`TASK#` citations. The contract names this feature ("consumer (C)") as the deferred consumer of inbound `UNDERSTANDING#` citations.

## Skill definition pattern
One skill = `adapters/claude/<name>/SKILL.md` (YAML frontmatter: name, description, argument-hint, allowed-tools; plus a runtime-glue body) + `references/<name>.md` (authoritative procedure) + a dispatch row in `adapters/codex/leanplan/SKILL.md` + a row in the `leanplan.md` §12 skill table. `sharpen` is the canonical sibling.
