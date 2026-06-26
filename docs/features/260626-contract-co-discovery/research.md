# 260626-contract-co-discovery — Research

Evidence archive for the contract-co-discovery finding. Sources verified against primary text where noted. Interpretation (how we word the core docs) belongs in `design-rationale.md`.

## Co-evolution of contract and solution

Claim grounded: the contract and the solution co-evolve; the contract cannot be fully frozen before solutions are explored.

- **Nuseibeh, B.** "Weaving Together Requirements and Architectures." *IEEE Computer* 34(3):115–117, March 2001. DOI 10.1109/2.910904. (Title is plural — "Architectures".) — The **Twin Peaks** model: requirements (problem) and architecture (solution) are developed concurrently and progressively, each guiding and constraining the other; argues explicitly against a single frozen starting point that "produces artificially frozen requirements documents." Canonical SE source for contract/solution co-evolution.
- **Dorst, K. & Cross, N.** "Creativity in the Design Process: Co-evolution of Problem–Solution." *Design Studies* 22(5):425–437, 2001. DOI 10.1016/S0142-694X(00)00009-6 *(DOI unverified against landing page; vol/issue/pages confirmed across multiple records).* — Empirical protocol study of 9 expert designers: creative design proceeds as **co-evolution of problem space and solution space**, not problem-first. Origin of the "co-evolution" term Twin Peaks echoes for software.

Grounding strength: **STRONG** (two direct primary sources — SE and design theory).

## Solution-agnostic specification ("what, not how")

Claim grounded: a Spec states observable interface behavior independent of implementation, so an implementation swap changes no Spec line (supports `Spec#C-2`).

- **Zave, P. & Jackson, M.** "Four Dark Corners of Requirements Engineering." *ACM TOSEM* 6(1):1–30, January 1997. DOI 10.1145/237432.237434. *(Full text read.)* — Defines **implementation bias**: "requirements are supposed to describe what is observable at the interface between the environment and the machine, and nothing else about the machine. To say anything else about the machine is regarded as implementation bias." Strongest primary ground for "what, not how."
- **Gunter, C.A., Gunter, E.L., Jackson, M., Zave, P.** "A Reference Model for Requirements and Specifications" (**WRSPM**). *IEEE Software* 17(3):37–43, May/June 2000. DOI 10.1109/52.896248 *(DOI unverified; venue/vol/issue/pages confirmed).* *(Full text read via preprint.)* — Five artifacts W/R/S/P/M. The specification **S is restricted to the shared interface vocabulary** ("the free variables of S must be among those in ev and sv… cannot include any of those in eh or sh"), i.e. implementation-independent. Adequacy obligation: `W ∧ S ⇒ R`.

Grounding strength: **STRONG**.

## Problem-given vs solution-induced contract facts (the two-kinds distinction)

Status: **not an established named distinction in the RE canon.** It does NOT map onto WRSPM's W-vs-S (a world/machine + given-vs-built cut) nor onto Zave–Jackson's indicative-vs-optative (an is-vs-want cut) — both are orthogonal axes. Neither model has a category for a fact that comes into existence only once a realization is posited.

Closest established homes (cite as lineage):

- **"Derived requirements"** (INCOSE / SEBoK / systems-engineering lineage) — requirements not explicitly stated, arising from "factors introduced by the selected architecture, and the design," "inextricably intertwined with the design solution." This is essentially our *solution-induced* category under a coarser name. Adjacent: **"architecturally significant requirements"** (the bidirectional ASR↔architecture relationship).
- **Jackson, M.** *Problem Frames: Analysing and Structuring Software Development Problems.* Addison-Wesley, 2001. ISBN 0-201-59627-X. — **"Designed domain"** (a domain the engineer introduces) vs **"given domain"** (the uncontrollable world); "designed domain" is the closest Jackson-family concept to *solution-induced*. *(Designed/given-domain wording confirmed via secondary summaries, not the book text — unverified.)*

LeanPlan delta beyond the lineage (factual, for `design-rationale` to interpret): our framing (a) pairs problem-given with solution-induced as two kinds of *contract fact* rather than a single "extra requirements" bucket, and (b) adds the **discover-vs-state** separation — a solution-induced fact can still be *stated* solution-agnostically (which follows directly from the implementation-bias principle above). The derived-requirements literature does not articulate (b).

Grounding strength: **PARTIAL** — cite the lineage; attribute the taxonomy to LeanPlan.

## World ↔ Machine axis (already cited by the framework)

- **Jackson, M.** "The World and the Machine." *Proc. 17th Int'l Conf. on Software Engineering (ICSE '95)*, pp. 283–292, 1995. DOI 10.1145/225014.225041. — World (problem domain) vs machine (constructed solution); shared phenomena form the interface. Confirms and completes the citation already at `framework-design.md`.

## Unverified details to confirm before publishing

- DOIs marked unverified: Dorst & Cross (10.1016/S0142-694X(00)00009-6) and WRSPM (10.1109/52.896248) — confirm against publisher landing pages.
- *Problem Frames* "designed domain"/"given domain" wording — confirm against the book, not encyclopedic summaries.
- Nuseibeh title is plural ("Architectures"), not singular.
