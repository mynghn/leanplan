# 260626-contract-co-discovery — Understanding Shifts

## Delta-1: probe-discovers-by-investigation-not-elicitation

The Specify boundary-probe discovers candidate contract facts through three channels — **inspect the as-is** (code, architecture, live environment), **research the outer world** (SOTA, prior art, convention for the boundary class), and **ask the planner** for the human-held slice — with structured questions reduced to the one channel that fits a human oracle (tacit expectations/SLAs + accept/decline).

This kills the prior assumption that the probe's mechanism is "structured questions (`AskUserQuestion` / runtime-native prompt)" mirroring the Requirements draw-out. That copied the Requirements (World, Contract) mechanism — where the human is the *sole* oracle of an optative problem — onto the Specify (Machine, Contract) altitude, where the probe's targets (failure modes, concurrency/ordering, observable error behavior, environmental couplings) are mostly indicative "given properties" of code, neighbors, and environment: facts you investigate, not intentions you elicit. Two distinctions the first draft missed: (a) **altitude** — at Specify the human is one source, not the oracle; (b) **convergent vs generative** — inspecting only the as-is re-derives the status quo, so the generative reach is the *outer-world* research channel (the feature's own co-evolution / Twin Peaks grounding applied beyond the repo: the as-is is your own prior solution, the outer world is the industry's). Reuses Specify's existing research machinery (`research.md` as a source, the *Isolate breadth-heavy research* sub-agent guardrail) and mirrors `design.md`'s load-bearing inspect-current-code — no new surface.

Surfaced at implementation (the planner challenged whether `AskUserQuestion` is the only discovery path, then whether outer-world research lives inside "inspect"); grounded by a framework investigation + an RE/SOTA review archived at `research.md` → Discovery mechanism.

Scope of impact: Design#D-1-specify-discovery-probe.
