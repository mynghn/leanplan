# 260620-sparse-arrival-drawout — Design Rationale

## D-1: drawout-as-requirement-front-step

**Forces.** A sparse arrival yields a thin, guessed requirement (`requirements.md` Problem). The fix has to engage at exactly one moment — the front of the requirement stage, before distillation — and it has to stay lean (opt-in, never forced). Two enabling facts already hold in the codebase: `AskUserQuestion` is granted to the requirement adapter (`adapters/claude/requirements/SKILL.md`), and `references/sharpen.md` (Inputs) already delegates the blank-slate draw-out to "the requirement stage's concern." The obligation, not the tooling or the seam, is what is missing — the current `references/requirements.md` step 3 ("Draft interactively") is a soft, distill-side line that assumes the arrival already carries a problem.

**Alternatives considered.**
- *A separate `/drawout` move, parallel to `/sharpen`.* Rejected. B earned its own move because it is invocable mid-*any*-stage (requirement through implementation) against a disturbance — it has no fixed home. E is bound to a single moment: the front of the requirement stage. A free-floating move would re-create the requirement stage's entry context, fragment the form→distill flow into two invocations, and add a surface (a skill + a reference doc) for behavior that belongs inside a stage the framework already runs. The sharp-vs-broad decision (2026-06-20) already judged "one move over both" inferior; a separate-but-parallel move is the same over-construction from the other side.
- *Leave step 3 as the soft "Draft interactively" line.* Rejected — that is the status quo the requirement names as the problem: it is skippable, distill-side, and silent on sparseness, so it does not reliably draw a sparse arrival out (`Spec#B-1`).

**Chosen path.** A load-bearing draw-out step at the front of `references/requirements.md`, gated on a sparse-arrival judgment, offered through the already-granted interactive tooling, declinable at any point. Because both runtimes load that one shared reference, the behavior reaches Claude and Codex without an adapter change. The step is the *obligation* that was absent.

**Invalidation triggers.** If the same draw-out is later wanted at another stage's entry (e.g. `references/specify.md`, which has no elicitation today), revisit whether it generalizes into a shared move rather than living inside one stage — but E deliberately scopes to the requirement cold start. If the sparse-arrival judgment proves unreliable enough that planners are regularly mis-routed *and* the decline path does not absorb the cost, the trigger may need a sharper signal.

## D-2: ephemeral-understanding-no-artifact

**Forces.** Between the draw-out and distillation a formed understanding exists transiently. B built `understanding.md` right next door — an append-only delta archive — so the tempting move is to persist E's understanding the same way.

**Alternative considered.** *Persist the formed understanding to `understanding.md` (or a new artifact) for traceability.* Rejected. B's `understanding.md` is an append-only log of *deltas* — mid-round shifts to an already-formed understanding, written to be consumed by *later* stages and any subsequent artifact revision (`artifact-contract.md` → Understanding). E's lifecycle is the opposite: the understanding is formed from a cold start and consumed *immediately* by the next step in the same session, and its durable distilled form is `requirements.md` itself. Persisting it separately would duplicate the requirement and inflate the review surface — against the lean bet — for a record that has no second consumer.

**Chosen path.** Keep the formed understanding ephemeral and in-conversation; distillation consumes it and writes `requirements.md`. This also keeps E clear of B's artifact model, which the split was meant to separate.

**Invalidation trigger.** If a real need emerges to audit the pre-distill understanding apart from `requirements.md` — e.g. to retain the candidate framings that were weighed and rejected (`Spec#B-2`) — revisit a lightweight archive then. Until a second consumer exists, `requirements.md` is the only durable home.
