# LeanPlan Artifact Contract

LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work. This doc carries the structural rules — feature layout, anchor patterns (`O-<N>`, `INV-<N>`, `Decision-<N>`, `Task: <id>`), traceability, drift guards.

Companion: `philosophy.md` (principles), `<stage>.md` (per-stage procedure).

## Feature Layout

Feature artifacts live under `docs/features/<KEY>/`, where `<KEY>` is the feature id allocated by `leanplan-new` in one of three forms: `NNNN-slug` (repo-local sequence number + kebab slug, e.g. `0007-anomaly-publisher`, the default); a bare tracker key (e.g. Jira `NEWCS-3595`) when the feature is anchored to a tracker item; or `YYMMDD-slug` (date, e.g. `260616-anomaly-publisher`). Tracker / PRD / Slack refs that are *not* the id are recorded as REQUIREMENT `## Upstream` metadata.

Surface artifacts:

- `requirement.md`
- `spec.md`
- `design.md`
- `plan.md`

Archive artifacts, created when useful:

- `design-rationale.md`
- `research.md`
- `understanding.md`

## Surface / Archive layering

What loads when — each tier loads only via an explicit trigger from the layer above (JIT by construction); the archive is lossless, so moving depth off the surface keeps it loadable:

- **Surface** (`requirement.md`, `spec.md`, `design.md`, `plan.md`) — loaded by default at review + implement time.
- **`design-rationale.md`** — loaded on challenge to a DESIGN decision (anchor link from DESIGN).
- **`research.md`** — loaded behind rationale, when raw evidence is needed.
- **`understanding.md`** — off-pipeline delta log, not a challenge-loading tier; written by `sharpen`, consumed by `revise`.

The full tier model (L0/L1/L2 labels, design reasoning) lives in `framework-design.md` §4.

## Stage Ownership

| Artifact | Owns |
|---|---|
| REQUIREMENT | Biz intent — incl. system policies as *why a cross-cutting property matters* |
| SPEC | Externally-observable contract — canonical prose home for `O` / `INV` facts |
| DESIGN | Internal realization — the finished-system shape |
| DESIGN RATIONALE | Tech WHY |
| RESEARCH | Evidence |
| UNDERSTANDING | Understanding deltas — mid-round re-derivation log |
| TASK (`plan.md`) | Time-ordered work navigation |

## Anchors

Anchor headings live at any of H2 / H3 / H4 to fit document structure — the markdown fragment derives from the heading text, not its level, so an anchor can move between levels without breaking a citation. The text after the heading marker must match exactly:

- `O-<N>: <slug>` — Outcome item (episode-verifiable)
- `INV-<N>: <slug>` — Invariant (continuous property)
- `Decision-<N>: <slug>` — DESIGN decision
- `Task: <id>` — TASK card
- `Delta-<N>: <slug>` — understanding delta (UNDERSTANDING archive)

Use kebab-case slugs. IDs are stable: never renumber an existing anchor after edits, and never delete a superseded `O` / `INV` / `Decision` / `Task:` — retire it in place by appending ` (retired)` to its anchor heading and recording the supersession reason in the body. The marker is not part of the slug, so the ID still resolves and prior review and traceability stay reconstructable — e.g. `### O-2: stale-outcome (retired)` keeps resolving as `O-2-stale-outcome`. (`validate.py` tolerates the heading marker; do not instead decorate the slug itself.)

Citation forms:

- `SPEC#O-1-detected-anomaly-published`
- `SPEC#INV-1-mission-fail-safe`
- `DESIGN#Decision-2-direct-kafka-publisher`
- `TASK#Task:A1`
- `UNDERSTANDING#Delta-1-premise-falsified`

## Required Shapes

### REQUIREMENT

- `## Problem`
- `## Outcome`
- `## Non-goals` only when biz scope is ambiguous
- `## Upstream` only when Jira, PRD, Slack, or similar sources exist — the external tracker key (e.g. Jira `PROJ-123`) is recorded here as metadata, never as the directory identity

### SPEC

- `## Outcome` containing one or more `O-<N>: <slug>` items (episode-verifiable behaviors)
- `## Invariants` containing one or more `INV-<N>: <slug>` items, only when continuous properties exist
- `## Non-goals` only when tech scope is ambiguous

Episode-triggered behavior belongs in O. Continuous properties belong in INV.

### DESIGN

- `## Architecture` with a Mermaid diagram
- One `Decision-<N>: <slug>` block per material choice
- Non-trivial decisions link to a matching block in `design-rationale.md`

### DESIGN RATIONALE

Use matching `Decision-<N>: <slug>` anchors. Body is **free-form prose** — typically forces, alternatives considered, chosen path, invalidation triggers. **No prescribed inner-section schema**: capture reasoning, don't fill a form.

### RESEARCH

Use descriptive topic headings. Store evidence only. Interpretation belongs in rationale.

### UNDERSTANDING

Append-only archive of understanding deltas — one `Delta-<N>: <slug>` block per mid-round shift, conclusion-first. Each block leads with what the understanding now is, then the prior assumption it kills, why (the disturbance + any verification verdict), and scope-of-impact as bare `SPEC#…` / `DESIGN#…` / `TASK#…` citations to the committed work it bears on — no restatement. IDs are stable; append, never renumber — duplicate `Delta-<N>` anchors are validator-caught. A delta's *outbound* `SPEC#` / `DESIGN#` / `TASK#` citations are resolution-checked, and *inbound* `UNDERSTANDING#Delta-N-slug` citations now resolve against these `Delta-<N>` anchors too — a revised artifact cites the Delta that justified it. RESEARCH# citations stay recorded-for-retrieval only: RESEARCH carries descriptive headings, not a resolvable anchor set.

### TASK (`plan.md`)

- Optional `## Guidelines` for feature-wide work-stance rules
- `## Dependency DAG` (or `## DAG`) with Mermaid; track subgraphs and prefixed task IDs (e.g. `P1`, `A1`, `D1`, `I1`) when coordination matters
- One `Task: <id>` block per land-able work item

Each task card must include:

- **Goal** — *process-framed* statement of WHAT outcome this task achieves + HOW (when the work approach is non-obvious), with inline `SPEC#…` and `DESIGN#…` anchors colocated with the supported sentence. **Anchor — don't restate.** Tech-realization specifics (field mappings, response shapes, signatures, call sequences) belong in the cited DESIGN Decision; the Goal points to them.
- **Repo** — where the work lives
- **Completion** — observable verification + method (test / monitor / SLO / one-shot observation). Enumerated scenarios/cases are healthy here — this is process-specific.
- **Dependencies** — prior task IDs as enablers (not gates)
- **Guidelines** — only when task-local stance matters

## Traceability

- Every SPEC O and INV maps to at least one task completion criterion or task body citation.
- Every task cites at least one SPEC O, SPEC INV, DESIGN decision, or explicit guideline reason.
- TASK dependencies are enablers, not rigid gates. Implementation agents re-evaluate them at task entry.

### `**GAP**` acknowledgment

A SPEC O or INV item may be deliberately uncovered (no task verifies it directly) when the team has accepted the gap. Annotate it on a line containing `**GAP**` inside `plan.md` (typically in a forward-coverage table). The validator treats such items as acknowledged — not coverage errors. Use sparingly and document the acceptance rationale next to the marker.

## One Prose Home Per Fact

A fact is authored as prose **once**, in its owning artifact; every other occurrence is an anchor reference, never a re-paraphrase. A search for any cross-cutting fact then returns one prose statement plus bare `…#…` anchors — zero restatements.

The rule binds **every seam**, not only DESIGN→SPEC:

- **Altitude split (REQ ↔ SPEC — the World↔Machine cut, `framework-design.md` §2).** A cross-cutting property has two altitudes, two homes: REQUIREMENT owns the biz *intent* (the rule + why it matters, no observable, testable predicate); SPEC `O` / `INV` owns the *observable form* (the canonical home — the same rule carrying an observable, testable predicate: a threshold, condition, or test). Neither restates the other's altitude — this resolves the blurred seam where a continuous property could read as either. *Discriminator:* a line with an observable, testable predicate is SPEC's; a line stating only the rule and its rationale is REQUIREMENT's. E.g. REQ — *"prices stay in parity across channels; split pricing erodes trust"* / SPEC#INV — *"web price == app price for identical input."*
- **Symmetric citation downstream.** Every realization reference cites its target's anchor and stops — DESIGN→SPEC, TASK→SPEC, TASK→DESIGN alike.
- **Within DESIGN.** The Architecture caption owns boundaries and flow; `Decision` blocks own realization claims — the caption doesn't restate a Decision.
- **Within TASK.** Inline `Completion` citations are the canonical forward-coverage home; a forward-coverage table, if kept, is a derived view of them, not a re-authored mapping — and only the deliberately-uncovered subset carries the reserved `**GAP**` marker.

Each stage doc carries its seam's operational instance; the per-artifact Drift Guards below are instances of this rule, not separate ones. Each avoided restatement removes a near-miss distractor; the surviving bare anchor is a literal lexical handle, not a latent lookup. (context-engineering: distractor-sensitivity, literal-vs-latent-matching)

## Prose Style

Applies to every artifact, in any authoring language. Write-time guidance, not validator-enforced.

- **Conclusion first.** Open each section, decision, and task card with its conclusion — the claim, choice, or outcome — then the support. The artifact should be graspable from headings and lead lines alone. The two prose-shaped fields most prone to collapsing into a blob — the DESIGN `Decision` body and the TASK `Goal` — get a worked good/bad example in `design.md` / `plan.md`. REQUIREMENT and SPEC are list-shaped by construction (user-story bullets; atomic `O` / `INV` items) and already conform — the rule binds the free-prose fields, where the blob risk lives, not the lists.
- **Lists over dense paragraphs.** When content enumerates parallel points, conditions, or steps, use bullet or ordered lists. Reserve flowing prose for a single causal chain.
- **Short, declarative sentences.** Break run-ons; promote a buried qualifier to its own clause or bullet rather than nesting it in parentheses.

Why: this serves the small-surface and LLM-aware principles — buried ledes and dense blocks get rubber-stamped by reviewers and dilute agent attention. Stage-specific shapes (e.g. REQUIREMENT user-story bullets, `requirement.md`) are instances of this rule, not exceptions.

## Surface Budget

The surface artifacts (REQUIREMENT, SPEC, DESIGN, TASK) are designed for **review fidelity, not completeness** — a lean surface is reviewed carefully; a verbose one gets rubber-stamped, and its over-specific detail leaks into implementation. Keep each surface tight; push depth into the archives (RATIONALE, RESEARCH) or split an oversized feature.

- **Direction, not a hard cap.** Tightness is the target; the caps below are an advisory backstop for *pathological* bloat, not a budget to fill. A well-formed one-deployment artifact normally sits far under them.
- **Soft per-stage caps, in *prose* lines** (advisory — `validate.py` warns above them, `--strict` escalates to error, `--allow-large` suppresses, mirroring the DAG-size guardrail): REQUIREMENT ~90, SPEC ~110, DESIGN ~160, TASK ~220. **Mermaid diagrams, fenced code/schemas, and blank lines are excluded** — they are legit reference detail, not attention-diluting prose, and a big architecture diagram must not read as bloat. This list is the source of truth; `validate.py`'s `SURFACE_SOFT_CAP` mirrors it — keep the two in sync. A breach is a prompt to ask *"what prose belongs in an archive, or should this feature split?"* — not an automatic failure.
- **Archive is lossless.** Moving reasoning to RATIONALE or evidence to RESEARCH removes it from the *review surface*, not from existence — it stays JIT-loadable on challenge. **Lean ≠ information loss.** This is the contract that lets the surface stay small without the team fearing lost context.
- **The framework's own references apply this reflexively.** This budget caps user surface artifacts; the stage references themselves (`requirement.md` … `impl.md`) follow the same surface/tier discipline — stance, procedure, guardrails, and author-time calibration (worked examples, templates) stay always-loaded, while step-scoped lookup detail defers to an on-demand companion loaded at its consuming step. Advisory, not a validator-enforced gate.

Grounded in the small-surface and LLM-aware principles (`philosophy.md` P3). The "lean surface is reviewed better" claim rests on the well-established code-review finding that defect detection drops sharply past a few hundred lines; that lean LeanPlan surfaces specifically review better is a deliberate, not-yet-measured bet. (context-engineering: context-rot, effective-vs-advertised-context, distractor-sensitivity)

## Drift Guards

- REQUIREMENT has no implementation choices.
- SPEC has no chosen stack or internal realization. Generic categories (message queue, event stream, HTTP API) only.
- DESIGN has no work ordering, no INFRAREQ / DBREQ procedure, no PR stacking — those belong in TASK. DESIGN **does** carry tech-realization specifics (field mappings, response shapes, signatures, call sequences, schemas) so plan tasks can anchor in.
- TASK has no line-by-line edit script. Implementation agents re-derive against current code at task entry.
- **TASK fields carry process specifics, not tech-realization specifics (the Product↔Process cut, `framework-design.md` §2).** Plan cards describe the *work* (Goal: what outcome / Completion: how to verify / Guidelines: work-stance). Tech-realization details — proto/response field mappings, controller orchestration sequences, method signatures, code paths, schemas — belong in a DESIGN `Decision-<N>` block. The task card anchors via `DESIGN#Decision-<N>-<slug>`; it does not restate the Decision's content. Symmetric guard with the DESIGN row above. Detection cue: a Goal bullet that answers "after the work lands, the system looks like X" is drift — push X to DESIGN; keep "this task achieves Y, verified by Z" in the card.
- MUST and MUST NOT are reserved for true invariants.
- Mermaid is used for diagrams; no ASCII fallback.
- Frontmatter is discouraged on plan artifacts; the artifact type is implied by filename.
