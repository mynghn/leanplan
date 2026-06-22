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

### Sharpen and revise

Canonical references: [`sharpen.md`](../../references/sharpen.md), [`revise.md`](../../references/revise.md), [`framework-design.md` → Skill responsibilities](../../framework-design.md#12-skill-responsibilities).

What you see: LeanPlan gives two off-pipeline moves for moments when understanding shifts.

Why it exists: not every shift should immediately rewrite artifacts, but real drift also should not stay in conversation memory. `sharpen` and `revise` split those cases so the agent can preserve changed understanding without corrupting the artifact history.

How to work with it:

- Use **sharpen** when understanding moved but the committed artifacts do not need edits yet. It records the delta and returns to the current stage.
- Use **revise** when an artifact is wrong or stale. It updates the highest affected layer, then re-evaluates downstream artifacts instead of fully restarting the plan by default.
- Prefer these moves over hand-editing downstream artifacts to make the current task easier.

When to challenge it: if the agent reaches for `revise` without a clear drift reason, ask what changed and which artifact owns that change. If the answer is only "this wording could be nicer," normal editing may be enough.

## Goal 2: Review surface brevity

LeanPlan keeps the visible plan small because small review surfaces get read. Brevity is not a taste preference here; it is a review and reasoning mechanism. The goal is to preserve enough intent for correct implementation while avoiding a document that looks complete but gets skimmed.

### Surface and archive layering

Canonical references: [`artifact-contract.md` → Surface / Archive layering](../../references/artifact-contract.md#surface--archive-layering), [`framework-design.md` → Surface/archive layering](../../framework-design.md#4-surfacearchive-layering), [`philosophy.md` → Archive verbose reasoning](../../references/philosophy.md#behavior-shaping-principles).

What you see: Requirements, Spec, Design, and Tasks stay compact, while deeper rationale can live in supporting archive material such as design rationale or research notes.

Why it exists: reviewers and agents need the current decision path quickly. They also need a way to recover deeper reasoning when a decision is challenged. Surface/archive layering keeps both: the surface stays reviewable, and the archive remains available on demand.

How to work with it:

- Keep the main artifact decision-ready.
- Move exploration, rejected alternatives, and evidence into archives when they matter but do not need to be loaded every time.
- Link from the surface to the archive only where a reviewer may reasonably challenge the decision.

When to challenge it: if the surface is so short that reviewers cannot tell what was decided, promote the missing decision into the surface. If the surface is carrying history, debate, or backup evidence, archive it and leave a pointed citation.

### Surface budget pushback

Canonical references: [`artifact-contract.md` → Surface Budget](../../references/artifact-contract.md#surface-budget), [`validate.py` → surface-budget guardrail](../../scripts/validate.py).

What you see: the agent or validator may push back when a surface artifact grows past its soft prose budget, or when the task DAG starts looking too large for one deployment-sized change.

Why it exists: the budget is a tripwire, not a target. LeanPlan uses it to catch artifacts that are becoming hard to review or that may be hiding more than one feature. The right response is not automatic deletion; it is a deliberate choice about where the extra material belongs.

How to work with it:

- Ask what prose belongs in an archive, what belongs on the surface, and what should be removed as duplication.
- Split the feature when the size is evidence that the work is no longer one deployable slice.
- Use strict validation when the team wants budget warnings to block CI or pre-commit.
- Use `--allow-large` only when the larger surface is intentional and still reviewable.

When to challenge it: if a warning is caused by legitimate reference material such as a Mermaid diagram or fenced schema, make sure it is being counted correctly before shrinking the artifact. If the artifact is over budget because every line carries load-bearing intent, the better fix may be feature splitting, not prose compression.

### One prose home plus traceability

Canonical references: [`artifact-contract.md` → One Prose Home Per Fact](../../references/artifact-contract.md#one-prose-home-per-fact), [`artifact-contract.md` → Traceability](../../references/artifact-contract.md#traceability), [`framework-design.md` → References carry ID + slug](../../framework-design.md#9-key-design-resolutions).

What you see: later artifacts cite earlier anchors instead of copying their content.

Why it exists: brevity fails if every artifact repeats the same fact. Restatement creates drift and makes review harder because the reader must compare versions. Traceability preserves the relationship without multiplying prose.

How to work with it:

- Use anchor references to show why a task or decision exists.
- Keep the cited artifact as the source of the fact.
- During implementation, carry the substance of important constraints into durable surfaces like code shape, tests, annotations, commit messages, or PR text.

When to challenge it: if a citation is decorative and the task would mean the same thing without it, improve the task. If a citation points to an anchor whose substance no longer matches the work, revise the plan rather than treating the anchor as a label.

### Conclusion-first prose

Canonical references: [`artifact-contract.md` → Prose Style](../../references/artifact-contract.md#prose-style), [`framework-design.md` → Cross-cutting structural rules](../../framework-design.md#6-cross-cutting-structural-rules).

What you see: good LeanPlan artifacts lead with the claim, decision, or task outcome, then give support.

Why it exists: a short paragraph can still bury the useful part. Reviewers skim dense prose, and agents lose the thread when the conclusion arrives after caveats. LeanPlan's brevity goal depends on order as much as length.

How to work with it:

- Make headings and first lines carry the point.
- Prefer bullets or small tables when the reader needs to compare items.
- Put caveats after the decision they qualify.

When to challenge it: if you have to reread a section to discover what it decided, rewrite the lead. If a section starts with background and only later reveals the conclusion, invert it.

### Validation as a guardrail

Canonical references: [`validate.py`](../../scripts/validate.py), [`artifact-contract.md` → Required Shapes](../../references/artifact-contract.md#required-shapes), [`artifact-contract.md` → Anchors](../../references/artifact-contract.md#anchors).

What you see: `validate.py` checks feature artifacts and reports missing sections, broken references, coverage gaps, and size guardrail warnings.

Why it exists: LeanPlan's review surface depends on structure. Lightweight validation catches shape drift before an agent or reviewer relies on a plan that no longer has the required anchors, coverage, or dependency shape.

How to work with it:

- Run validation before implementation and after plan edits.
- Treat validation failures as plan defects, not formatting annoyances.
- Use strict validation when CI or pre-commit should fail on warnings.

When to challenge it: validation cannot decide whether the product judgment is good or whether the implementation is elegant. It protects the contract; humans still own intent, tradeoffs, and review quality.

### Brevity is not information loss

Canonical references: [`artifact-contract.md` → Surface Budget](../../references/artifact-contract.md#surface-budget), [`philosophy.md` → Persist by migration to code](../../references/philosophy.md#behavior-shaping-principles), [`implement.md` → Distill WHYs](../../references/implement.md#procedure).

What you see: LeanPlan cuts surface prose aggressively, but it does not ask the team to forget why decisions were made.

Why it exists: review surface brevity only works if users trust that important reasoning can be recovered. The archive path, citations, validation, and implementation close-out all exist to make brevity safe rather than shallow.

How to work with it:

- Ask "does this fact need to be read every time?" before placing it on the surface.
- Ask "where will this rationale live after implementation?" before closing a task.
- Prefer durable forms after the work lands: tests, types, annotations, commit messages, PR text, and only rarely comments.

When to challenge it: if brevity removes a constraint that implementation must honor, restore it to the owning artifact. If depth is useful only for audit or challenge, keep it archived and cited.
