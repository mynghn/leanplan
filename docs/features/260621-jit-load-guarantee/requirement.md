# 260621-jit-load-guarantee — The load the lean surface depends on actually happens

## Problem

LeanPlan defers detail off the immediate card in two different ways, and only one of them is safe today.

- **Isolated for brevity, but still always needed.** A task's cited SPEC Outcome/Invariant (what it realizes) and DESIGN Decision (how) are pushed off the card to keep it lean, but the work genuinely depends on them. These must reach the point of use.
- **Deliberately hidden until really needed.** RATIONALE and RESEARCH sit in the archive tier, loaded only on challenge — genuinely optional, and fine to never load when the work doesn't need them.

The framework's surface/archive layering already draws this line — surface = needed-by-default, archive = load-on-challenge. The gap is that **nothing makes the first kind actually load.** Surface artifacts cite anchors instead of restating detail, trusting just-in-time loading — but an implementation agent can act on a citation's short name (slug) alone, and when it does, leanness silently becomes **under-specification**: it proceeds on a compressed label and misses the cited constraint.

- The leaner the surface, the larger the un-loaded risk for the always-needed class.
- "Self-sufficient at cut-off" (a card must read completely without its target) doubles as a **licence to not load** — the sentence feels like enough.
- The failure is silent and looks compliant: right anchor cited, plausible text, still divergent because the anchor was never opened. Nothing distinguishes "consulted" from "acted on the name."

Who feels it: **implementation agents** act on partial information believing they are compliant; **reviewers** see a correct-looking citation and can't tell the load was skipped; the framework's **efficiency bet** (lean surface + load-on-demand) has a safeguard on the *lean* half and none on the *load* half — for the class that can't afford to skip it.

## Outcome

For the **always-needed class** — content isolated off the card only for brevity that the current work depends on — consulting the cited anchor before acting is **required, and a skipped load is surfaceable**, with the surface no less lean. The **deliberately-deferred class** (the archive tier) stays exactly as optional as it is today.

User stories:

- **The needed load is part of the work, not a courtesy** — when an agent's action depends on a load-bearing citation (a SPEC O/INV it realizes, a DESIGN Decision it builds), consulting that content before acting is a required step of the work.
- **A skipped needed-load is catchable** — an implementation that acted on a load-bearing citation it never opened is detectable after the fact, rather than passing as silently compliant.
- **Optional stays optional** — archive citations (RATIONALE / RESEARCH) remain load-on-challenge; the work is never forced to open content it doesn't need.

System policies:

- **The surface/archive layer is the discriminator** — the always-needed class is the surface / load-bearing citations; the deliberately-deferred class is the archive tier. The guarantee scopes to the former by reusing the boundary the framework already has, not by inventing a new tag. (Shares the derivable-boundary spirit of the sibling feature `derivable-orthogonality`.)
- **Leanness must not buy silent under-specification** — for the always-needed class, every byte moved off the card stays reachable *and is actually reached*.
- **"Self-sufficient at cut-off" is for resilience, not for skipping a needed load** — a card surviving without its target must never become permission to act without it.
- **Keep the anchor model; close its gap** — the cite-don't-restate discipline stays; the fix makes the *needed* just-in-time load reliable, not optional. It neither restates archived detail back onto the surface nor eager-loads everything.

Confirmed when: an implementation that acts on a load-bearing cited constraint demonstrably consulted it, not just its slug; a skipped load on such a citation can be surfaced rather than passing silently; archive citations are never force-loaded; and the review surface is no less lean than it is today.

## Non-goals

- The static content-boundary / coordinate-model work — that is the sibling feature `derivable-orthogonality`.
- **Guaranteeing the deliberately-deferred class.** RATIONALE / RESEARCH (and any genuinely-optional, load-on-challenge content) stay skippable by design — forcing them to load would defeat the deferral that keeps the surface lean.
- Restating anchor content back onto the surface (the "embed full context in the card" approach) — that abandons the leanness bet; the goal is to make the *needed* load reliable, not to remove the need for it.
- Changing **what** any artifact contains or its stage role.

## Upstream

- LeanPlan self-feedback critique, 2026-06-21 — the "no actual guarantee on JIT loading's occurrence" finding: brevity-via-anchors assumes reliable resolution, but nothing ensures it. The field is split on this exact fork — BMAD embeds full context into each card (locality, accepts redundancy); LeanPlan anchors for leanness and depends on the load happening. Grounded in the context-engineering concepts *literal-vs-latent-matching* (an un-restated fact is a latent dependency whose recall collapses unless pulled to the point of use) and *distractor-sensitivity*. Scope sharpened on review: the guarantee covers only the *always-needed* (surface / load-bearing) deferral class; the *deliberately-deferred* archive class stays optional, per the existing surface/archive layering. **#32 (merged)** made `artifact-contract.md` the canonical home for that surface/archive loading-trigger model — the *scoping* this feature reuses; #32 supplies the load *trigger* (when to load), not the load *enforcement* (that it actually happens) this feature adds. Branch rebased onto post-#32 `main`.
- Backlog: **#31** (`Backlog: M`). Sibling feature: `derivable-orthogonality` (**#30**). Related: **#26** (J — outcome eval listing "anchors get JIT-resolved" among the unmeasured bets).
