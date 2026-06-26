# 260626-ce-grounding-link-check — Spec

## Behavior

### B-1: dangling-grounding-is-reported
Run with the live source reachable, the inspection reports every grounded slug — drawn from LeanPlan's `(context-engineering: <slug>)` hooks and the map — that has no resolving entry in the live source, and reports clean when every grounded slug resolves. One-shot verifiable: introduce a grounded slug absent from the source and confirm it is listed; with all slugs present, confirm a clean report.

### B-2: source-absent-is-reported-distinctly
Run with the live source absent or unreachable, the inspection reports a distinct "source absent — expected gloss fallback" outcome — not a dangling-grounding finding and not an error. One-shot verifiable: remove the source and confirm the outcome is the distinct absent-state report and the run exits without error.

## Constraint

### C-1: report-only-no-mutation
The inspection's only effect is its advisory report. It never edits LeanPlan's grounding or any LeanPlan artifact, and never writes to the live source or anything upstream. Corrections are made separately, outside this inspection.

### C-2: reference-only-not-semantic
The inspection's verdict depends only on whether a grounded slug resolves and whether the resolution path is reachable — never on a concept's content, meaning, or health (including any upstream degraded marker). An upstream change that leaves a slug resolving — a reworded definition, a flagged-but-present entry — yields no finding; only a slug that fails to resolve does.

### C-3: self-contained-run
The inspection runs and produces a verdict with nothing beyond what LeanPlan ships; the live source's absence yields the absent-state report (`B-2`), never a failure to run. The source is needed to find dangling references — never to execute.

## Non-goals
- The contract covers the on-demand inspection only; an automated watcher that triggers it is out of scope.
- The contract does not cover applying corrections — repair flows through LeanPlan's existing revise move, not this inspection.
