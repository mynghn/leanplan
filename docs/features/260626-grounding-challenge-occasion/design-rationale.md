# 260626-grounding-challenge-occasion — Design Rationale

## D-1: occasion-home-in-ce-paragraph

Forces: the occasion must have exactly one home (`Spec#B-1`) without growing the surface (`Spec#C-1`).

Chosen: the §13 CE deep-grounding paragraph. It is the design archive (challenge-time home), already owns the deep-grounding framing, and already says hooks load "only when a hook is challenged" — so the occasion sentence completes a thought already in place, the leanest possible add.

Alternatives:
- **The map header (`context-engineering.md`)** — rejected: the map owns the *resolution mechanism* (how a slug resolves to live KB or gloss), not the *occasion* (when/why one would challenge). Putting the occasion there would split a design-rationale concept into the operational doc and duplicate framing. A reader resolving a hook is already mid-challenge and does not need the occasion meta-model; the auditor reasoning about the framework reads §13.
- **`philosophy.md`** — rejected: philosophy states behavior-shaping principles, not the consultation occasion; the occasion is design-archive material, a level below the principles.

Invalidation: if the §13 paragraph is ever split or relocated, the occasion sentence moves with the deep-grounding framing, not the resolution mechanism.

## D-2: disambiguate-the-two-challenges

Forces: "challenge" names two distinct events (`Spec#B-2`) — both real, both kept — and the disambiguation must not restate itself in two homes (`artifact-contract.md` → One Prose Home Per Fact) nor add machinery (`Spec#C-1`).

Chosen: the full one-line distinction lives in §13 (beside the new occasion, where the grounding challenge is described); §9's "Challenge mechanism" bullet is scoped to the *implementation* challenge and carries only a bare pointer to §13. This gives bidirectional discoverability — a reader landing at either section learns the other "challenge" exists — while authoring the distinction once.

Alternatives:
- **Restate the distinction in both §9 and §13** — rejected: two prose homes for one fact; the near-miss restatement is exactly the distractor the framework's own de-dup rule removes.
- **Rename one sense** (e.g. call §9's the "drift trigger", reserve "challenge" for grounding) — rejected as over-reach for `Spec#C-1`: a framework-wide term rename churns many sites for a clarity win a one-line scoping pointer already buys; "challenge" is apt for both (each interrogates a claim), they differ in *what* is interrogated (current reality vs. evidence), which the pointer states.

Invalidation: a future feature that *does* want a term rename (if the overload proves to mislead in practice despite the pointers) would supersede this with a sweep — a separate, larger effort.
