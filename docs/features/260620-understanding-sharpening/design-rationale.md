# 260620-understanding-sharpening — Design Rationale

## D-1: sharpen-as-non-stage-skill

Forces: B must be invocable mid-process from inside any stage (`B-1`), opt-in (`C-3`), and lean. Two realizations were weighed.

- **Protocol woven into the existing stage skills**, no new command: each stage doc embeds the reflect→verify→re-derive guidance. Leaner in file count, but there is no crisp, sanctioned *entry* — invocation depends on every stage re-deriving the move, and a mid-stage planner can't deliberately "pick it up."
- **A dedicated skill** (chosen): a skill is independently invocable at any point in a round, by the planner (`/sharpen`) or by the agent on a disturbance. That *is* the mid-process pick-up mechanism.

The decisive point: a skill is **not** a stage — it sits off the requirement→impl pipeline, so "a callable move" and "not a separate stage" hold at once. It is lean by construction in LeanPlan: a thin adapter over `references/sharpen.md`, the same shape as every stage. (An earlier worry that a separate command is heavyweight or "makes you exit your work" was wrong — invoking a skill loads its protocol into the same session and the stage resumes, `C-2`.)

Invalidation trigger: if agents reliably pick the move up from the woven pointer alone (D-4) and never invoke the skill, the skill is dead weight — collapse to the protocol-only form.

## D-2: understanding-delta-archive

Forces: the delta must survive a context reset (`C-4`), must not live in the committed surface artifacts (`C-1`), is a cross-stage *interpretation* (it can fire mid-requirement through impl), and is meant to be consumed by downstream stages and the future C (#9). Homes considered:

- `research.md` — **evidence-only** by contract; the delta is a decision/interpretation, not raw evidence. Wrong altitude.
- `design-rationale.md` — scoped to Design `D-<N>` reasoning; the delta is cross-stage and can predate any design decision. Wrong scope.
- a committed **surface artifact** — forbidden by `C-1`.
- the **warm session** — fails `C-4` (lost on reset).

Chosen: a new feature-local **archive** `understanding.md`, append-only `Delta-<N>: <slug>` blocks. As an archive it does not spend the Surface Budget, and it exists only when a delta is emitted. The `Delta-<N>` anchor makes a delta citable — the form the future C consumes (`Understanding#Delta-<N>-<slug>`) — consistent with LeanPlan's anchored-fact + one-prose-home model.

Invalidation trigger: if C (#9) lands with a different consumption model (e.g. deltas inlined into a revision changelog), revisit whether a standalone archive is the right home. Validator support for the new artifact/anchor is an impl task; if it proves heavy, entries can degrade to research-style descriptive headings without changing the design intent.

## D-3: reflect-verify-rederive-protocol

Forces: the move must sharpen, not thrash (`requirement` "bounded, never derailing"), and must not obey an injected claim on faith. Two non-obvious stances:

- **Adversarial verification of an injected claim** (step 2): a disturbance arriving as an external claim (cited prior-art, stakeholder assertion) is treated as a *hypothesis to falsify*, not an instruction. Grounding: the 0004 round's injected "Boris Cherny → Obsidian" claim was verified and **falsified** (actual source: Karpathy's "LLM Wiki"); obeying it would have mis-shaped the architecture. Default to "refuted unless corroborated."
- **A legitimate no-op** (step 4): the move may conclude the understanding did *not* move and close with no delta. Sharpening that always "finds" a change is just churn; pairing re-derivation with an explicit no-op branch is what keeps the move bounded.

Boundary with impl: `impl.md`'s existing Stop-The-Line + Artifact Update Loop already conflate cognitive re-derivation with artifact editing, but only at impl. B factors out the *cognitive* half as a stage-agnostic move and deliberately does **not** touch impl's loop or perform editing — generalizing and reconciling that loop is C's (#9) job.

Invalidation trigger: if the C reconciliation absorbs the cognitive half too, this protocol may collapse into C's entry procedure.
