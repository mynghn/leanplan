# 260626-contract-co-discovery — Research

Evidence archive for the contract-co-discovery finding. Sources verified against primary text where noted. Interpretation (how we word the core docs) belongs in `design-rationale.md`.

## Co-evolution of contract and solution

Claim grounded: the contract and the solution co-evolve; the contract cannot be fully frozen before solutions are explored.

- **Nuseibeh, B.** "Weaving Together Requirements and Architectures." *IEEE Computer* 34(3):115–119, March 2001. DOI 10.1109/2.910904. (Title plural — "Architectures"; DOI + pages 115–119 verified, DOI gate.) — The **Twin Peaks** model: requirements (problem) and architecture (solution) are developed concurrently and progressively, each guiding and constraining the other; argues explicitly against a single frozen starting point that "produces artificially frozen requirements documents." Canonical SE source for contract/solution co-evolution.
- **Dorst, K. & Cross, N.** "Creativity in the Design Process: Co-evolution of Problem–Solution." *Design Studies* 22(5):425–437, 2001. DOI 10.1016/S0142-694X(01)00009-6 *(DOI verified, DOI gate — note the (01) year-code; the originally-recorded (00) variant is a dead identifier that 404s).* — Empirical protocol study of 9 expert designers: creative design proceeds as **co-evolution of problem space and solution space**, not problem-first. Origin of the "co-evolution" term Twin Peaks echoes for software.

Grounding strength: **STRONG** (two direct primary sources — SE and design theory).

## Solution-agnostic specification ("what, not how")

Claim grounded: a Spec states observable interface behavior independent of implementation, so an implementation swap changes no Spec line (supports `Spec#C-2`).

- **Zave, P. & Jackson, M.** "Four Dark Corners of Requirements Engineering." *ACM TOSEM* 6(1):1–30, January 1997. DOI 10.1145/237432.237434. *(Full text read.)* — Defines **implementation bias**: "requirements are supposed to describe what is observable at the interface between the environment and the machine, and nothing else about the machine. To say anything else about the machine is regarded as implementation bias." Strongest primary ground for "what, not how."
- **Gunter, C.A., Gunter, E.L., Jackson, M., Zave, P.** "A Reference Model for Requirements and Specifications" (**WRSPM**). *IEEE Software* 17(3):37–43, May/June 2000. DOI 10.1109/52.896248 *(DOI verified, DOI gate.)* *(Full text read via preprint.)* — Five artifacts W/R/S/P/M. The specification **S is restricted to the shared interface vocabulary** ("the free variables of S must be among those in ev and sv… cannot include any of those in eh or sh"), i.e. implementation-independent. Adequacy obligation: `W ∧ S ⇒ R`.

Grounding strength: **STRONG**.

## Problem-given vs solution-induced contract facts (the two-kinds distinction)

Status: **not an established named distinction in the RE canon.** It does NOT map onto WRSPM's W-vs-S (a world/machine + given-vs-built cut) nor onto Zave–Jackson's indicative-vs-optative (an is-vs-want cut) — both are orthogonal axes. Neither model has a category for a fact that comes into existence only once a realization is posited.

Closest established homes (cite as lineage):

- **"Derived requirements"** (INCOSE / SEBoK / systems-engineering lineage) — requirements not explicitly stated, arising from "factors introduced by the selected architecture, and the design," "inextricably intertwined with the design solution." This is essentially our *solution-induced* category under a coarser name. Adjacent: **"architecturally significant requirements"** (the bidirectional ASR↔architecture relationship).
- **Jackson, M.** *Problem Frames: Analysing and Structuring Software Development Problems.* Addison-Wesley, 2001. ISBN 0-201-59627-X. — **"Designed domain"** (a domain the engineer introduces / constructs) vs **"given domain"** (given/fixed/pre-established in the problem, not subject to the developer's design); "designed domain" is the closest Jackson-family concept to *solution-induced*. *(Terms confirmed, DOI gate — given-vs-designed is Jackson's origin axis; "given" ≠ "uncontrollable" — controllability is his separate biddable/causal axis.)*

LeanPlan delta beyond the lineage (factual, for `design-rationale` to interpret): our framing (a) pairs problem-given with solution-induced as two kinds of *contract fact* rather than a single "extra requirements" bucket, and (b) adds the **discover-vs-state** separation — a solution-induced fact can still be *stated* solution-agnostically (which follows directly from the implementation-bias principle above). The derived-requirements literature does not articulate (b).

Grounding strength: **PARTIAL** — cite the lineage; attribute the taxonomy to LeanPlan.

## World ↔ Machine axis (already cited by the framework)

- **Jackson, M.** "The World and the Machine." *Proc. 17th Int'l Conf. on Software Engineering (ICSE '95)*, pp. 283–292, 1995. DOI 10.1145/225014.225041. — World (problem domain) vs machine (constructed solution); shared phenomena form the interface. Confirms and completes the citation already at `framework-design.md`.

## Discovery mechanism — investigate vs elicit at the contract boundary

Claim grounded: at the (Machine, Contract) altitude most boundary facts (failure modes, concurrency/ordering, observable error behavior, environmental couplings) are indicative *given properties* of code/neighbors/environment — discovered by investigation — not optative intentions elicited from a stakeholder. (Grounds the probe's multi-channel discovery and its outer-world generative reach; that mechanism interpretation lives in `design-rationale.md` → D-1.)

- **Jackson, M.** *Problem Frames* (2001) + "The World and the Machine" (ICSE '95, cited above). — A domain's *given properties* (indicative) are facts about reality, found by investigating the world; the *requirement* (optative) is intent, surfaced by dialogue. Concurrency, interface behavior, and environmental couplings sit in the given-properties bucket — the discriminator for investigate-vs-elicit.
- **Goguen, J.A. & Linde, C.** "Techniques for Requirements Elicitation." *Proc. IEEE Int'l Symp. on Requirements Engineering (RE 1993)*, pp. 152–164. — interviews/questionnaires capture only what stakeholders can articulate; tacit knowledge ("we know more than we can tell," Polanyi, *The Tacit Dimension*, 1966) needs observation/analysis, not asking. *(Venue confirmed; page range and quotes not verified.)*
- **Glinz, M.** "On Non-Functional Requirements." *15th IEEE Int'l Requirements Engineering Conf. (RE'07)*, pp. 21–26. — quality requirements are *operationalized* into measurable form, not simply stated; stakeholders characteristically do not hold them explicitly. *(Venue/pages corroborated; not quote-verified.)*
- Investigative toolkit (evidence the discovery methods for these classes are artifact-/environment-facing, not interrogative): FMEA (IEC 60812:2018), FTA (IEC 61025; NUREG-0492, 1981), HAZOP (IEC 61882:2016), obstacle analysis (van Lamsweerde & Letier, *IEEE TSE* 26(10):978–1005, 2000), exception/scenario analysis (Cockburn, *Writing Effective Use Cases*, 2000; Sutcliffe, *IEEE TSE* 24(12), 1998), misuse/abuse cases (Sindre & Opdahl, *Requirements Eng.* 10(1):34–44, 2005; McDermott & Fox, ACSAC 1999), quality-attribute scenarios / ATAM (Bass, Clements & Kazman, *Software Architecture in Practice*; Kazman et al., CMU/SEI-2000-TR-004), interface analysis (BABOK §10.24), domain/context analysis. *(Standard identifiers well-corroborated; technique definitions cross-checked across multiple secondary sources, several not quote-verified line-by-line.)*
- Generative reach: co-evolution / Twin Peaks (Nuseibeh 2001; Dorst & Cross 2001 — see "Co-evolution" above) is the rationale for letting outer-world solution exploration surface contract facts; bounding discovery to the as-is limits co-evolution to one's own prior solution.

Grounding strength: **STRONG** for the investigate-vs-elicit claim (Jackson's indicative/optative + the tacit-knowledge / NFR-operationalization consensus). The technique citations are evidence the toolkit is investigative; identifiers corroborated, several not quote-verified (flagged below).

## Unverified details to confirm before publishing

- **Resolved (DOI gate, this round):** Dorst & Cross DOI corrected to `10.1016/S0142-694X(01)00009-6` (the `(00)` variant 404s); WRSPM `10.1109/52.896248`, Four Dark Corners `10.1145/237432.237434`, and World-and-the-Machine `10.1145/225014.225041` confirmed via Crossref; Nuseibeh title plural "Architectures" + pages 115–119 confirmed; *Problem Frames* designed/given-domain terms confirmed (given = pre-established / not-designed, not "uncontrollable"). These are the citations that land in core docs.
- Discovery-mechanism sources — Goguen & Linde RE 1993 page range; Glinz RE'07 pp. 21–26; and the investigative-toolkit identifiers (IEC 61025 edition; Sindre & Opdahl journal vol/pages vs. the original TOOLS Pacific 2000 paper; *Software Architecture in Practice* edition) are corroborated at the technique level but several are not quote-verified. These are evidence-of-investigative-toolkit, not load-bearing model claims; verify only if any is promoted into a core-doc citation.
- Tooling note: the `mgrep` web index was unavailable (HTTP 429, quota) during the discovery-mechanism scan; the sanctioned WebSearch fallback was used. Re-check borderline citations against primary text before publishing.
