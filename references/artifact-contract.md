# LeanPlan Artifact Contract

LeanPlan is a lean, LLM-aware spec-driven-development framework for one-deployment-sized feature work. This doc carries the structural rules — feature layout, anchor patterns (`B-<N>`, `C-<N>`, `D-<N>`, `T: <id>`), traceability, drift guards.

Companion: `philosophy.md` (principles), `<stage>.md` (per-stage procedure).

## Feature Layout

Feature artifacts live under `docs/features/<KEY>/`, where `<KEY>` is the feature id allocated by `leanplan-new` in one of three forms: `NNNN-slug` (repo-local sequence number + kebab slug, e.g. `0007-anomaly-publisher`, the default); a bare tracker key (e.g. Jira `NEWCS-3595`) when the feature is anchored to a tracker item; or `YYMMDD-slug` (date, e.g. `260616-anomaly-publisher`). Tracker / PRD / Slack refs that are *not* the id are recorded as Requirements `## Upstream` metadata.

Surface artifacts:

- `requirements.md`
- `spec.md`
- `design.md`
- `tasks.md`

Archive artifacts, created when useful:

- `design-rationale.md`
- `research.md`
- `understanding-shifts.md`
- `deferrals.md`

## Surface / Archive layering

What loads when — each tier loads only via an explicit trigger from the layer above (JIT by construction); the archive is lossless, so moving depth off the surface keeps it loadable:

- **Surface** (`requirements.md`, `spec.md`, `design.md`, `tasks.md`) — loaded by default at review + implement time.
- **`design-rationale.md`** — loaded on challenge to a Design decision (anchor link from Design).
- **`research.md`** — loaded behind rationale, when raw evidence is needed.
- **`understanding-shifts.md`** — off-pipeline delta log, not a challenge-loading tier; written by `sharpen`, consumed by `revise`.
- **`deferrals.md`** — off-pipeline deferral lane, not a challenge-loading tier; written by any stage's capture hook, drained (JIT-loaded) at its owning stage's entry.

The full tier model (L0/L1/L2 labels, design reasoning) lives in `framework-design.md` §4.

## Stage Ownership

| Artifact | Owns |
|---|---|
| Requirements | Desired outcome — incl. system policies as *why a cross-cutting property matters* |
| Spec | Externally-observable contract — canonical prose home for `B` / `C` facts |
| Design | Internal realization — the finished-system shape |
| Design Rationale | Decision WHY |
| Research | Evidence |
| Understanding Shifts | Understanding deltas — mid-round re-derivation log |
| Deferrals | Deferred cross-stage decisions — open items addressed forward to their owning stage |
| Tasks | Time-ordered work navigation |

## Anchors

Anchor headings live at any of H2 / H3 / H4 to fit document structure — the markdown fragment derives from the heading text, not its level, so an anchor can move between levels without breaking a citation. The text after the heading marker must match exactly:

- `B-<N>: <slug>` — Behavior item (episode-verifiable)
- `C-<N>: <slug>` — Constraint (continuous property)
- `D-<N>: <slug>` — Design decision
- `T: <id>` — Tasks card
- `Delta-<N>: <slug>` — understanding delta (Understanding archive)
- `Defer-<N>: <slug>` — deferred cross-stage decision (Deferrals archive); a trailing `(resolved -> <…>)` resolve-in-place marker is tolerated alongside the retired marker ` (retired)`, and keeps the anchor resolving

Use kebab-case slugs. IDs are stable: never renumber an existing anchor after edits, and never delete a superseded `B` / `C` / `D` / `T:` — retire it in place by appending ` (retired)` to its anchor heading and recording the supersession reason in the body. The marker is not part of the slug, so the ID still resolves and prior review and traceability stay reconstructable — e.g. `### B-2: stale-behavior (retired)` keeps resolving as `B-2-stale-behavior`. (`leanplan-validate` tolerates the heading marker; do not instead decorate the slug itself.)

Citation forms:

- `Spec#B-1-detected-anomaly-published`
- `Spec#C-1-mission-fail-safe`
- `Design#D-2-direct-kafka-publisher`
- `Tasks#T:A1`
- `UnderstandingShifts#Delta-1-premise-falsified`
- `Deferrals#Defer-1-cache-strategy`

## Required Shapes

### Requirements

- `## Problem`
- `## Outcome`
- `## Guarantee` only when continuous domain properties (system-policy intent) exist
- `## Non-goals` only when the Requirements scope is ambiguous
- `## Upstream` only when Jira, PRD, Slack, or similar sources exist — the external tracker key (e.g. Jira `PROJ-123`) is recorded here as metadata, never as the directory identity

### Spec

- `## Behavior` containing one or more `B-<N>: <slug>` items (episode-verifiable behaviors)
- `## Constraint` containing one or more `C-<N>: <slug>` items, only when continuous properties exist
- `## Non-goals` only when the Spec's scope is ambiguous

Episode-triggered behavior belongs in B. Continuous properties belong in C.

### Design

- `## Architecture` with at least one visual block: Mermaid diagram or fenced ASCII art
- One `D-<N>: <slug>` block per material choice
- Non-trivial decisions link to a matching block in `design-rationale.md`

### Design Rationale

Use matching `D-<N>: <slug>` anchors. Body is **free-form prose** — typically forces, alternatives considered, chosen path, invalidation triggers. **No prescribed inner-section schema**: capture reasoning, don't fill a form.

### Research

Use descriptive topic headings. Store evidence only. Interpretation belongs in rationale.

### Understanding Shifts

Append-only archive of understanding deltas — one `Delta-<N>: <slug>` block per mid-round shift, conclusion-first. Each block leads with what the understanding now is, then the prior assumption it kills, why (the disturbance + any verification verdict), and scope-of-impact as bare `Spec#…` / `Design#…` / `Tasks#…` citations to the committed work it bears on — no restatement. IDs are stable; append, never renumber — duplicate `Delta-<N>` anchors are validator-caught. A delta's *outbound* `Spec#` / `Design#` / `Tasks#` citations are resolution-checked, and *inbound* `UnderstandingShifts#Delta-N-slug` citations now resolve against these `Delta-<N>` anchors too — a revised artifact cites the Delta that justified it. Research# citations stay recorded-for-retrieval only: Research carries descriptive headings, not a resolvable anchor set.

### Deferrals

Off-review-surface archive of deliberately-deferred cross-stage decisions, created when useful. One `Defer-<N>: <slug>` block per deferral, each addressed forward to the later stage that owns the decision. A sibling to the understanding-shift archive — never a blend: an understanding delta is a *committed* change to propagate; a deferral is an *open* question to re-decide. Not loaded at default review/implement time; JIT-loaded only by its owning stage's drain.

Each block is shaped so it cannot read as a settled decision (conclusion-first):

- **Owning stage** — one of Requirements / Spec / Design / Tasks; the stage the deferral is addressed to.
- the open **question** + why it surfaced now
- **forces** glimpsed
- at most an **option seen** — explicitly marked *not chosen*. There is no "decision" field.

Resolution is retire-in-place: when the owning stage drains it, append `(resolved -> <Spec#… | Design#… | Tasks#…>)` to the block heading, citing where the decision landed — the same convention as ` (retired)`, so the `Defer-<N>` ID keeps resolving. Append-only; IDs stable; duplicate `Defer-<N>` anchors are validator-caught. An unresolved deferral whose owning stage's artifact already exists is surfaced by `leanplan-validate` (advisory) — never silently dropped; once drained, the resolve-in-place marker cites where the decision landed and that anchor's normal coverage tracks it. The capture and drain procedures live in `references/deferral.md`.

### Tasks (`tasks.md`)

- Optional `## Guidelines` for feature-wide work-stance rules
- `## Dependency DAG` (or `## DAG`) with Mermaid; track subgraphs and prefixed task IDs (e.g. `P1`, `A1`, `D1`, `I1`) when coordination matters
- One `T: <id>` block per land-able work item

Each task card must include:

- **Goal** — *process-framed* statement of WHAT outcome this task achieves + HOW (when the work approach is non-obvious), with inline `Spec#…` and `Design#…` anchors colocated with the supported sentence. **Anchor — don't restate.** Tech-realization specifics (field mappings, response shapes, signatures, call sequences) belong in the cited Design Decision; the Goal points to them.
- **Repo** — where the work lives
- **Completion** — observable verification + method (test / monitor / SLO / one-shot observation). Enumerated scenarios/cases are healthy here — this is process-specific.
- **Dependencies** — prior task IDs as enablers (not gates)
- **Guidelines** — only when task-local stance matters

## Traceability

- Every Spec B and C maps to at least one task completion criterion or task body citation.
- Every task cites at least one Spec B, Spec C, Design decision, or explicit guideline reason.
- Tasks dependencies are enablers, not rigid gates. Implementation agents re-evaluate them at task entry.
- At implement close-out **and on the review path**, run **Close-Out Reconciliation** (`implement-closeout.md`) on a task's load-bearing citations — a reviewer runs it independently, not only the implementing agent, which keeps a self-skipped consultation catchable.

### `**GAP**` acknowledgment

A Spec B or C item may be deliberately uncovered (no task verifies it directly) when the team has accepted the gap. Annotate it on a line containing `**GAP**` inside `tasks.md` (typically in a forward-coverage table). The validator treats such items as acknowledged — not coverage errors. Use sparingly and document the acceptance rationale next to the marker.

## One Prose Home Per Fact

A fact is authored as prose **once**, in its owning artifact; every other occurrence is an anchor reference, never a re-paraphrase. A search for any cross-cutting fact then returns one prose statement plus bare `…#…` anchors — zero restatements.

The rule binds **every seam**, not only Design→Spec:

- **Altitude split (REQ ↔ Spec — the World↔Machine cut, `framework-design.md` §2).** A cross-cutting property has two altitudes, two homes: Requirements owns the *intent* (the rule + why it matters, no observable, testable predicate); Spec `B` / `C` owns the *observable form* (the canonical home — the same rule carrying an observable, testable predicate: a threshold, condition, or test). Neither restates the other's altitude — this resolves the blurred seam where a continuous property could read as either. *Discriminator:* a line with an observable, testable predicate is Spec's; a line stating only the rule and its rationale is Requirements's. E.g. REQ — *"prices stay in parity across channels; split pricing erodes trust"* / Spec#C — *"web price == app price for identical input."*
- **Symmetric citation downstream.** Every realization reference cites its target's anchor and stops — Design→Spec, Tasks→Spec, Tasks→Design alike.
- **Within Design.** The Architecture caption owns boundaries and flow; `Decision` blocks own realization claims — the caption doesn't restate a Decision.
- **Within Tasks.** Inline `Completion` citations are the canonical forward-coverage home; a forward-coverage table, if kept, is a derived view of them, not a re-authored mapping — and only the deliberately-uncovered subset carries the reserved `**GAP**` marker.

Each stage doc carries its seam's operational instance; the per-artifact Drift Guards below are instances of this rule, not separate ones. Each avoided restatement removes a near-miss distractor; the surviving bare anchor is a literal lexical handle, not a latent lookup. (context-engineering: distractor-sensitivity, literal-vs-latent-matching)

## Prose Style

Applies to every artifact, in any authoring language. Write-time guidance, not validator-enforced.

- **Conclusion first.** Open each section, decision, and task card with its conclusion — the claim, choice, or outcome — then the support, so it is graspable from headings and lead lines alone. The blob-prone free-prose fields — the Design `Decision` body and the Tasks `Goal` — carry a worked good/bad example in `design.md` / `tasks.md`; Requirements and Spec are list-shaped by construction and already conform.
- **Lists over dense paragraphs.** When content enumerates parallel points, conditions, or steps, use bullet or ordered lists. Reserve flowing prose for a single causal chain.
- **Short, declarative sentences.** Break run-ons; promote a buried qualifier to its own clause or bullet rather than nesting it in parentheses.
- **Concise, not compressed.** Cut redundancy, not meaning: drop what's repeated or already implied, never a distinct piece of information the reader needs (`bypass-check save` ❌ drops *which* check; "save without the duplicate check" ✅ keeps it). The same loss hides in a separator-joined pile, or even in plain words ("the save" for the one that skips the duplicate check). Ask what answer went missing, not how long the line is — a term or `·` that drops nothing is fine. Spend the words. (context-engineering: literal-vs-latent-matching)

Why: this serves the small-surface and LLM-aware principles — buried ledes and dense blocks get rubber-stamped and dilute agent attention. Stage-specific shapes (e.g. Requirements user-story bullets) are instances of this rule, not exceptions.

## Surface Budget

The surface artifacts (Requirements, Spec, Design, Tasks) are designed for **review fidelity, not completeness** — a lean surface is reviewed carefully; a verbose one gets rubber-stamped, and its over-specific detail leaks into implementation. Keep each surface tight; push depth into the archives (Rationale, Research) or split an oversized feature.

- **Direction, not a hard cap.** Tightness is the target; the caps below are an advisory backstop for *pathological* bloat, not a budget to fill. A well-formed one-deployment artifact normally sits far under them.
- **Soft per-stage caps, in *prose* lines** (advisory — `leanplan-validate` warns above them, `--strict` escalates to error, `--allow-large` suppresses, mirroring the DAG-size guardrail): Requirements ~90, Spec ~110, Design ~160, Tasks ~220. **Visual blocks (Mermaid diagrams or ASCII art), fenced code/schemas, and blank lines are excluded** — they are legit reference detail, not attention-diluting prose, and a big architecture diagram must not read as bloat. This list is the source of truth; `leanplan-validate`'s `SURFACE_SOFT_CAP` mirrors it — keep the two in sync. A breach is a prompt to ask *"what prose belongs in an archive, or should this feature split?"* — not an automatic failure.
- **Archive is lossless.** Moving reasoning to Rationale or evidence to Research removes it from the *review surface*, not from existence — it stays JIT-loadable on challenge. **Lean ≠ information loss.** This is the contract that lets the surface stay small without the team fearing lost context.
- **The framework's own references apply this reflexively.** This budget caps user surface artifacts; the stage references themselves (`requirements.md` … `implement.md`) follow the same surface/tier discipline — stance, procedure, guardrails, and author-time calibration (worked examples, templates) stay always-loaded, while step-scoped lookup detail defers to an on-demand companion loaded at its consuming step. Advisory, not a validator-enforced gate.

Grounded in the small-surface and LLM-aware principles (`philosophy.md` P3). The "lean surface is reviewed better" claim rests on the well-established code-review finding that defect detection drops sharply past a few hundred lines; that lean LeanPlan surfaces specifically review better is a deliberate, not-yet-measured bet. (context-engineering: context-rot, effective-vs-advertised-context, distractor-sensitivity)

## Drift Guards

- Requirements has no implementation choices.
- Spec has no chosen stack or internal realization. Generic categories (message queue, event stream, HTTP API) only.
- Design has no work ordering, no infrastructure / database request procedure, no PR stacking — those belong in Tasks. Design **does** carry tech-realization specifics (field mappings, response shapes, signatures, call sequences, schemas) so plan tasks can anchor in.
- Tasks has no line-by-line edit script. Implementation agents re-derive against current code at task entry.
- **Tasks fields carry process specifics, not tech-realization specifics (the Product↔Process cut, `framework-design.md` §2).** Plan cards describe the *work* (Goal: what outcome / Completion: how to verify / Guidelines: work-stance). Tech-realization details — proto/response field mappings, controller orchestration sequences, method signatures, code paths, schemas — belong in a Design `D-<N>` block. The task card anchors via `Design#D-<N>-<slug>`; it does not restate the Decision's content. Symmetric guard with the Design row above. Detection cue: a Goal bullet that answers "after the work lands, the system looks like X" is drift — push X to Design; keep "this task achieves Y, verified by Z" in the card.
- MUST and MUST NOT are reserved for true invariants.
- Design visuals may be Mermaid diagrams or fenced ASCII art. Prefer a visual companion when prose would otherwise blur relationships, boundaries, sequences, state, or mappings; use as many visuals as clarify distinct structures. Tasks DAGs stay Mermaid unless the Tasks contract changes.
- Frontmatter is discouraged on plan artifacts; the artifact type is implied by filename.
