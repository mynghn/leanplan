# LeanPlan Mechanisms

This page explains why LeanPlan behaves the way it does. It is user-facing explanation, not canonical agent procedure. The agent-facing rules still live in `references/*.md` and the runtime adapters; each mechanism below links back to its canonical sources.

LeanPlan's mechanisms are not separate tricks. They mostly serve two framework goals:

1. **LLM-aware design**: keep the agent working from the right slice of intent, current code, and constraints instead of flooding it with stale or unrelated prose.
2. **Review surface brevity**: make the plan small enough that humans and agents actually review it carefully, while preserving deeper rationale for moments that need it.

## Goal 1: LLM-aware design

LLMs are sensitive to what is loaded, where the important facts sit, and how much distracting context surrounds the current decision. LeanPlan is shaped to give the agent a compact working set, then reload detail only when a stage or task needs it.

### Just-in-time loading

Canonical references: [`philosophy.md` → JIT loading](../../references/philosophy.md#behavior-shaping-principles), [`implement.md` → Procedure](../../references/implement.md#procedure), [`framework-design.md` → Surface/archive layering](../../framework-design.md#4-surfacearchive-layering).

What you see: the agent reads the current stage artifact, specific cited anchors, and relevant code instead of loading every LeanPlan reference and every archive file up front.

Why it exists: a bigger context window is not the same as better reasoning. Old rationale, unrelated task details, and copied summaries compete with the facts the agent needs now. LeanPlan treats context as working memory: load the slice for this step, keep reloadable links to the rest.

How to work with it:

- Expect the agent to open only the cited `B-`, `C-`, `D-`, or `T:` blocks that bear on the current step.
- Keep links and anchor names meaningful, because they are the handles the agent uses to retrieve detail later.
- Put long analysis in archive material when it is useful but not needed on every pass.

When to challenge it: if the agent cannot make a safe decision without repeatedly opening an archive, promote the needed constraint into the surface artifact that owns it. A fact that is always needed should not hide behind a challenge path.

### Stage ownership

Canonical references: [`artifact-contract.md` → Stage Ownership](../../references/artifact-contract.md#stage-ownership), [`framework-design.md` → Role segregation](../../framework-design.md#3-role-segregation).

What you see: each artifact owns a different kind of fact.

Why it exists: LLMs are easy to mislead with near-duplicate statements. If the same behavior appears in Requirements, Spec, Design, and Tasks with slightly different wording, the agent has to guess which one is authoritative. LeanPlan reduces that ambiguity by giving every kind of fact one prose home.

How to work with it:

- Requirements owns problem, scope, and success shape.
- Spec owns observable behavior and constraints.
- Design owns the implementation approach and tradeoffs.
- Tasks owns work ordering, completion criteria, and load-bearing citations.
- Implementation owns the durable final rationale after the plan has served its purpose.

When to challenge it: if a downstream artifact starts restating upstream content, replace the restatement with a citation or move the fact back to the artifact that owns it. If behavior changes, revise Spec before patching Design or Tasks around the change.

### No flat task scripts

Canonical references: [`philosophy.md` → No flat task scripting](../../references/philosophy.md#behavior-shaping-principles), [`artifact-contract.md` → Tasks shape](../../references/artifact-contract.md#tasks-tasksmd), [`tasks.md` → Stage stance](../../references/tasks.md), [`implement.md` → Re-reason, don't execute](../../references/implement.md#guardrails).

What you see: task cards describe goals, constraints, dependencies, and completion evidence rather than step-by-step edit recipes.

Why it exists: implementation happens against current code, not the code that existed when the plan was written. A detailed script can become stale before the task starts, then distract the agent from re-reading the real implementation. LeanPlan wants the task to preserve intent while forcing the agent to re-reason at task entry.

How to work with it:

- Read a task card as a scoped outcome, not a command transcript.
- Let the agent inspect current code before deciding exact edits.
- Use completion criteria to judge whether the task landed, not whether the agent followed a predicted sequence.

When to challenge it: if a task is so vague that two implementers would do different work, add clearer intent or completion criteria. If it is so specific that it names every edit, push realization details back into Design or let implementation derive them from code.

### Stop-the-line moments

Canonical references: [`implement.md` → Stop-The-Line Triggers](../../references/implement.md#stop-the-line-triggers), [`implement.md` → Artifact Update Loop](../../references/implement.md#artifact-update-loop), [`framework-design.md` → Challenge mechanism](../../framework-design.md#9-key-design-resolutions).

What you see: the agent pauses when it finds contradictions, missing verification paths, invalid dependencies, externally visible behavior changes, unprovable constraints, or scope expansion.

Why it exists: LLMs can keep moving through a broken premise very convincingly. LeanPlan makes certain drift visible instead of letting the agent silently patch around it. The pause protects the plan from becoming a polished explanation of the wrong work.

How to work with it:

- Treat a stop as a signal about the plan, not as agent hesitation.
- Resolve the highest affected layer first: Requirements for scope, Spec for behavior, Design for approach, Tasks for execution shape.
- Continue only after the corrected artifact and downstream references still make sense.

When to challenge it: if the pause is caused by uncertainty rather than real drift, answer the decision directly and continue. Stop-the-line is meant to prevent known wrongness, not to turn every ambiguity into a planning ceremony.

### Rethink and revise

Canonical references: [`rethink.md`](../../references/rethink.md), [`revise.md`](../../references/revise.md), [`framework-design.md` → Skill responsibilities](../../framework-design.md#12-skill-responsibilities).

What you see: LeanPlan gives two off-pipeline moves for moments when understanding shifts.

Why it exists: not every shift should immediately rewrite artifacts, but real drift also should not stay in conversation memory. `rethink` and `revise` split those cases so the agent can preserve changed understanding without corrupting the artifact history.

How to work with it:

- Use **rethink** when understanding moved but the committed artifacts do not need edits yet. It records the delta and returns to the current stage.
- Use **revise** when an artifact is wrong or stale. It updates the highest affected layer, then re-evaluates downstream artifacts instead of fully restarting the plan by default.
- Prefer these moves over hand-editing downstream artifacts to make the current task easier.

When to challenge it: if the agent reaches for `revise` without a clear drift reason, ask what changed and which artifact owns that change. If the answer is only "this wording could be nicer," normal editing may be enough.

## Goal 2: Review surface brevity

LeanPlan keeps the visible plan small because small review surfaces actually get read. Brevity here is a review and reasoning mechanism, not a taste preference: preserve enough intent for correct implementation while avoiding a document that looks complete but gets skimmed.

### Surface and archive layering

Canonical references: [`artifact-contract.md` → Surface / Archive layering](../../references/artifact-contract.md#surface--archive-layering), [`artifact-contract.md` → Surface Budget](../../references/artifact-contract.md#surface-budget), [`framework-design.md` → Surface/archive layering](../../framework-design.md#4-surfacearchive-layering), [`philosophy.md` → Archive verbose reasoning](../../references/philosophy.md#behavior-shaping-principles).

What you see: Requirements, Spec, Design, and Tasks stay compact; deeper rationale lives in supporting archive material (design rationale, research, understanding-shifts, deferrals). The agent or validator pushes back when a surface artifact grows past its soft prose budget, or when the task DAG looks too large for one deployment-sized change.

Why it exists: reviewers and agents need the current decision path fast, but must still recover deeper reasoning on challenge — layering keeps both. The budget is a tripwire for "this is getting hard to review, or hiding more than one feature," not a target. And brevity is not information loss: the archive path, citations, and implementation close-out exist so cut prose is recoverable, not forgotten.

How to work with it:

- Keep the main artifact decision-ready; move exploration, rejected alternatives, and evidence into archives when they matter but need not load every time.
- When a budget warning fires, decide where the material belongs — archive it, cite it, or split the feature — rather than blindly deleting. Use `--allow-large` only when the larger surface is intentional and still reviewable; use strict validation when the team wants warnings to block CI.
- Before closing a task, ask where each important WHY will live afterward (tests, types, annotations, commit/PR text).

When to challenge it: if the surface is so short that reviewers cannot tell what was decided, promote the missing decision back onto it. If a warning is caused by legitimate reference material — a Mermaid diagram, a fenced schema — check it is counted correctly before shrinking. And brevity means *concise, not compressed*: if a line reads terse but you cannot tell what it means without unpacking a coined term or a `·`-joined pile, that is compression — ask for it in plainer words. Cut redundancy, never a distinction the reader needs.

### Traceability over restatement

Canonical references: [`artifact-contract.md` → One Prose Home Per Fact](../../references/artifact-contract.md#one-prose-home-per-fact), [`artifact-contract.md` → Traceability](../../references/artifact-contract.md#traceability), [`framework-design.md` → References carry ID + slug](../../framework-design.md#9-key-design-resolutions).

What you see: later artifacts cite earlier anchors (`B-`, `C-`, `D-`, `T:`) instead of copying their content.

Why it exists: brevity fails if every artifact repeats the same fact — restatement creates drift and forces the reader to compare versions to find the authoritative one. Citation preserves the relationship without multiplying prose. This is the same one-prose-home principle behind stage ownership, seen from the downstream side.

How to work with it:

- Use anchor references to show why a task or decision exists; keep the cited artifact as the source of the fact.
- During implementation, carry the substance of important constraints into durable surfaces — code shape, tests, annotations, commit messages, PR text — not just the anchor.

When to challenge it: if a citation is decorative and the task would mean the same thing without it, improve the task. If a citation points to an anchor whose substance no longer matches the work, revise the plan rather than treating the anchor as a label.

### Validation as a guardrail

Canonical references: [`leanplan-validate`](../../scripts/leanplan-validate), [`artifact-contract.md` → Required Shapes](../../references/artifact-contract.md#required-shapes), [`artifact-contract.md` → Anchors](../../references/artifact-contract.md#anchors).

What you see: `leanplan-validate` checks feature artifacts and reports missing sections, broken references, coverage gaps, and size guardrail warnings (see `reference.md` for the flags).

Why it exists: LeanPlan's review surface depends on structure. Lightweight validation catches shape drift before an agent or reviewer relies on a plan that no longer has the required anchors, coverage, or dependency shape.

How to work with it: run validation before implementation and after plan edits; treat failures as plan defects, not formatting annoyances.

When to challenge it: validation cannot decide whether the product judgment is good or the implementation elegant. It protects the contract; humans still own intent, tradeoffs, and review quality.

## Next

- Read [`adoption.md`](./adoption.md) for team adoption guidance.
- Read [`reference.md`](./reference.md) for quick command and artifact lookup.
- Back to [`USER_GUIDE.md`](../../USER_GUIDE.md) for the entry path and Quickstart.
