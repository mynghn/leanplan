# 260622-human-user-manual — Design Rationale

## D-1: top-level-user-guide
`USER_GUIDE.md` is the single top-level human entry point, but the manual is a multi-file suite: the front door carries entry orientation, the Quickstart, and a depth-routed TOC, while `docs/user-guide/` holds focused, independently-loadable pages (workflow, mechanisms, adoption, reference).

The initial decision (v1.0) was a single-file `USER_GUIDE.md` holding all three parts, chosen over a `docs/` page tree on the grounds that a tree "creates too many choices before LeanPlan has a stable public learning path," with an explicit deferral: split later once the reference section grows too large to scan.

That condition was met while the manual was being written, so the split was ratified. Three forces decided it: (1) **volume** — the suite reached ~600 lines (`mechanisms.md` alone ~200), past the point where one file serves the progressive-disclosure Guarantee a first-time reader depends on; one 600-line file buries the first-use path. (2) **the "too many choices" risk is neutralized** by keeping a single front door (`USER_GUIDE.md` with a "read only as deep as you need" TOC) rather than exposing a flat set of pages — the reader still sees one entry. (3) **reflexive fit** — per-page just-in-time loading mirrors LeanPlan's own JIT-loading and one-prose-home principles, so the manual embodies the framework it teaches. Invalidation trigger: if the suite later shrinks below a single-screen-scannable size, reconsider collapsing it back. See UnderstandingShifts#Delta-1-multi-file-guide-suite.

## D-3: source-boundary-map
The manual should explain canonical agent references without becoming another canonical agent reference. If it owned procedure, the framework would gain a second source of truth and every stage change would require synchronizing prose across the human guide and `references/*.md`.

The chosen boundary is explanation over instruction: `USER_GUIDE.md` teaches users how to reason about LeanPlan behavior, while `references/*.md`, adapters, validators, and framework internals keep owning exact agent procedure. This keeps human adoption approachable without weakening operational consistency.

## D-4: mechanism-explanation-pattern
Mechanism sections need a repeated structure because the documentation goal is trust through inspectability, not just more prose. A flat description of each concept would still leave users guessing when they can push back or what behavior they should expect from the agent.

The chosen pattern makes every mechanism answer the same user questions: what will I observe, why does LeanPlan do this, how do I work with it, and when should I challenge it. The brevity section is the calibration point: describe hard cuts as one possible enforcement mode, but present the broader mechanism set so users do not reduce LeanPlan to arbitrary length policing.
