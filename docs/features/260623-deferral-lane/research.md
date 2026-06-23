# 260623-deferral-lane — Research

Evidence only; interpretation belongs in Design Rationale.

## Context-engineering basis: capture = note-taking (write), drain = JIT (read)

`structured-note-taking` (CE KB) — agentic memory is the *write* operation: persist notes/plans/state to durable storage outside the context window and re-read on demand; "externalize anything you must not forget… treat the window as scratch"; durable against compaction and resets. Evidence cited there: Claude-plays-Pokémon keeps tallies/maps across context resets; the multi-agent LeadResearcher saves its plan because context past 200K is truncated. Source: Anthropic, *Effective Context Engineering for AI Agents*.

`jit-loading` (CE KB) — the *read* complement: "maintain lightweight identifiers… load data into context at runtime"; "carry pointers, not payloads; resolve a reference to full content only at the moment of need," keeping the working set lean and avoiding the recall decay of a stuffed window. Stated tradeoff: runtime exploration is slower than pre-loading, and an unguided agent can waste context chasing dead-ends. Source: Anthropic, *Effective Context Engineering for AI Agents*.

Both resolve through the framework's own grounding nodes `(context-engineering: structured-note-taking | jit-loading)` (`references/context-engineering.md`).

## Adjacent-record precedent: the understanding-shift record (260620-understanding-sharpening)

That feature's Spec defines the belief-revision record: `B-4: understanding-delta-emitted` (emit a delta recording what changed, why, the prior assumption it kills, and the scope it implicates) and `C-4: understanding-delta-durable` (persists beyond the producing session, retrievable by later stages, survives a context reset). It is written by `sharpen` and consumed by `revise` as an append-only delta log (`references/artifact-contract.md` → Understanding). This is the *committed / backward-looking* record that the deferral capture (an *open / forward-looking* item) must stay distinct from — the basis for Spec `C-4`.

## Skill-design basis (Design realization)

`degrees-of-freedom` (skill-design KB) — the prescriptiveness dial: high-freedom prose where multiple approaches are valid; low-freedom scripts where consistency is critical. SkillsBench (arXiv:2602.12670): curated skills raised pass rates +16.6pp, self-generated ones −1.3pp — mis-/over-specification is a real cost, calibration pays. Sources: Anthropic skill best-practices; SoK Agentic Skills (arXiv:2602.20867).

`skill-vs-tool-vs-prompt-vs-subagent` (skill-design KB) — a skill packages procedure + applicability + termination + a callable interface and self-activates; a prompt template is static injected text lacking those; a sub-agent adds an isolated window + delegation. Source: SoK (arXiv:2602.20867); Anthropic Agent Skills.

`progressive-disclosure-token-economics` (skill-design KB) — three load tiers: L1 metadata always-loaded (~100 tok), L2 body on-activation (<5k recommended), L3 bundled files on-demand (effectively unlimited). Put the trigger in L1, the common path in L2, heavy/rare detail in L3. Sources: Claude docs; agentskills.io.

## Prompt-engineering pointers (implementation-time wording)

`positive-instruction` (PE KB) — convert prohibitions into affirmatives; the capture reframes each stage's "strip / discard" prohibition into a "park it" affirmative. `reasoning-scaffolds` (PE KB) — the high-freedom drain ("re-examine against the current option space") is a reason-then-decide scaffold; author its exact wording at implementation, not in Design.

## Rename blast radius (read-only repo scan, 2026-06-23)

- Filename `understanding.md` — ~30 occurrences: `references/{artifact-contract,sharpen,revise,design,implement}.md`, `adapters/claude/{sharpen,revise}/SKILL.md`, `scripts/validate.py` (`OPTIONAL_FILES`, ~line 29), `scripts/leanplan-selftest` (fixture injections ~155/219), `fixtures/`, and historical `docs/features/260620-*` dirs.
- Tier/artifact name "Understanding" — ~7: stage-ownership + tier tables in `artifact-contract.md` and `framework-design.md` (including the "keep Understanding (Delta-)" line from #34).
- Citation `Understanding#Delta-N-slug` — ~6: `artifact-contract.md` example, `revise.md`, `adapters/.../revise`, selftest assertions, `260620-artifact-later-update`.
- Validator/selftest hardcoding — `validate.py`: `OPTIONAL_FILES["understanding"]`, `ANCHOR_RE`/`CITATION_RE` carry the `Delta` alternation, inbound `Understanding#` resolution set; `leanplan-selftest` has duplicate-Delta + citation-ok + citation-broken cases with hardcoded assertion strings.
- In scope to sweep (D-6 = rename to `understanding-shifts.md`): the **filename literal** across live-framework sites. **Unchanged**: the `Understanding#` citation prefix and the `Delta-N` anchor (so the ~6 citation sites and the validator regex do not move). Exempt (quote-as-data): historical `docs/features/260620-*` and this feature's own dir.
