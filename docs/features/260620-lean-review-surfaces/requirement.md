# 260620-lean-review-surfaces — Skim-readable, de-duplicated review surfaces

## Problem

LeanPlan's four surface artifacts — REQUIREMENT, SPEC, DESIGN, PLAN — exist to be **reviewed**, by agents and humans alike. Two forces make them fail at that job, and both are LeanPlan violating its own small-surface / leanness bet:

- **The heaviest surfaces read worst.** DESIGN lands as dense prose blobs and PLAN's task goals as run-on sentences, so a reviewer can't answer *"what does this decide, and what must I check?"* at skim depth. The surfaces that most need scrutiny get rubber-stamped — and their over-specific detail leaks downstream unchecked. (REQUIREMENT and SPEC already read well; DESIGN is worst, PLAN mediocre.)
- **The same fact is authored several times.** One property gets reworded across REQUIREMENT, SPEC, DESIGN, and PLAN, because some artifact and section boundaries are blurred and the no-restatement discipline guards only some seams. Restatement inflates every surface, and the copies drift apart with no canonical home.

Who feels it: **human reviewers** give up and rubber-stamp; **downstream agents** have their attention diluted and inherit the leaked over-specification.

## Outcome

The four surfaces become **graspable at skim depth** and **carry each fact once** — without losing their identity as interim SDD artifacts.

User stories:

- **Skim-readable surfaces** — a reviewer answers *"what does this decide, and what must I check?"* from headings and lead lines alone, on every surface. DESIGN and PLAN reach the bar REQUIREMENT and SPEC already meet.
- **Each fact stated once** — any given property appears one authored time; every other appearance is a reference, not a reworded copy. One canonical home; nothing silently drifts.

System policies:

- **Functional identity preserved** — only legibility and de-duplication change; each artifact must stay a valid, trustworthy interim SDD doc rather than lose its identity.
- **Leanness is the test** — every change must reduce a reviewer's and an agent's reading load. Verbosity is the arch-enemy, and the fix is applied to LeanPlan's own docs too.

Confirmed when: a human reviews any surface at skim depth and gets its bottom line, and a search for any cross-cutting property finds a single prose statement plus bare references elsewhere — zero re-paraphrases.

## Non-goals

- Changing **what** an artifact contains or its stage role — only legibility and de-duplication change.
- The artifact **later-update / evolution** process, and the upfront **problem-understanding** experience — each a separate feature.
- Reworking the seams that are already clean (RATIONALE vs RESEARCH vs DESIGN; DESIGN vs TASK tech-realization). The blur is localized — don't over-correct.
- Re-building the surface size/verbosity enforcement that just landed on `main` — this feature builds on it. Raw size caps are distinct from its concerns (BLUF *structure* and *de-duplication*), which a size cap doesn't address.

## Upstream

- LeanPlan self-feedback distill, 2026-06-20. Sibling features (problem-understanding; later-update) and the full four-thread grounding are parked in `docs/leanplan-feedback-backlog.md`.
