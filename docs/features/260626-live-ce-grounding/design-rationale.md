# 260626-live-ce-grounding — Design Rationale

## D-1: delete-the-vendored-cards

Forces: the cards drift silently from their source (`requirements.md` Problem), and the stance that justified them — "portability is inviolable" — is hollowed by the source vault being private, so the self-contained-grounding benefit only ever fully resolved in the maintainer's own environment.

This **reverses** that feature's two-layer-vendored-archive decision (its `D-1`) and narrows its portable-self-contained constraint (its `C-1`) — both in `docs/features/260619-context-engineering-knowledges-grounding/`. That design's own rejected alternative — *"name-only, KB as an optional external companion"* — is essentially what is now chosen, because its rejection rested on a premise (`C-1`: the full definition must resolve locally on a bare install) that this feature consciously relaxes: operation and named grounding stay local, only the deep definition goes live.

Alternative — **keep the cards and build a sync/drift-checker** (issue #27's original lever, the prior feature's `D-8` optional regenerator promoted to required): rejected. It spends machinery to keep a copy honest when the copy buys little real portability (private source) and forks the knowledge from where it should be exercised. Deleting the copy removes the drift class entirely instead of policing it.

Invalidation: if the source vault becomes public **and** an outside-adopter use-case emerges that needs the full definition resolvable with nothing external, reconsider a drift-free vendoring path (e.g. a submodule or generated bundle) — not a hand-distilled copy.

## D-2: map-resolves-live-with-gloss-floor

Forces: a challenged hook must reach the current definition when the source is present (`B-1`), degrade without error when it is absent (`B-2`), and always resolve locally to at least a named concept + gloss (`C-2`) — all without re-introducing a copy.

Chosen: the map stays the single resolution point. Its `[[<slug>]]` becomes a concept reference whose deep layer is the live CE knowledge base, reached via the `context-engineering-knowledge-base` **skill** — Metacognition's public interface — and its existing per-rule gloss is the local floor. Three properties decide for the skill over a location reference: (a) its name is **identical across the Claude / Codex / agents registries** (verified), so it is a Metacognition identifier rather than a harness one and is safe to name in this provider-neutral map; (b) it **abstracts the vault location** (the path lives inside the skill), so LeanPlan is insulated from any storage relayout; (c) it **dogfoods the exact retrieve interface** Metacognition is built around — the whole point of the reversal — rather than reaching around it to raw files.

Access alternatives considered (the user's "skill vs. location (remote/local)" fork):
- **Reference the local vault path** (`~/.local/share/metacognition-vault/...`) — rejected: same freshness as the skill (both read the same local checkout) but strictly more brittle — it hardcodes one install layout, bypasses the skill's INDEX + `⚠`-degraded signalling, and exercises none of Metacognition's interface.
- **Fetch the private remote** (`github.com/mynghn/metacognition-vault`) — rejected: the repo is **private**, so this adds auth + network to every challenge and fails for anyone without credentials; and it is unnecessary — keeping the local vault current vs. the remote is already Metacognition's own `metacognition-freshness` job. LeanPlan reading the live **local** source while Metacognition keeps that source synced is the clean separation: LeanPlan dogfoods both the retrieve path and (transitively) the freshness path. "Fresh by construction" comes from reading the single live source, not from hitting the remote.
- **Name-only, no gloss floor** — rejected: a bare install's challenge would bottom out at the slug with no meaning attached, and it fails `C-2`. The user's chosen posture is gloss-fallback, not bare-name.
- **Add a one-line gloss of each *concept's definition*** (beyond the per-rule application gloss) — rejected: that edges back toward a distilled copy and reopens the drift surface this feature exists to close. The per-rule gloss is genuinely LeanPlan's own (it states *why this rule rests on the concept*), not a paraphrase of the source definition, so it is safe to keep; a concept-definition gloss would not be.

Invalidation: the `context-engineering-knowledge-base` skill changes name or interface shape (re-point the resolution note), or the per-rule glosses prove too thin as a floor in practice (promote a fuller gloss — while holding the copy line above).

## D-3: frame-as-harness-supplied-grounding

Forces: relaxing an "inviolable" constraint deserves an explicit framework-level home, or a future challenger re-litigates it from scratch; and the framework's own discipline is *document the path, never strip a grounding hook* (the recurring lesson from prior CE-grounding work).

Chosen: frame CE deep-grounding as another instance of the existing `framework-design.md` §13 split — "the framework names the behavior portably; the harness supplies the mechanism when present; a bare install does it by hand" — exactly parallel to session-management (`D-7`). §13 already names "no external KB" as the bare-install baseline, so CE grounding slots in cleanly: the gloss is the by-hand floor, the live KB is the supplied mechanism. This makes the narrowed portability a principled, recorded position rather than a silent wording change.

Alternative — **edit the resolution wording silently** (just fix line 13 / philosophy line 28): rejected. The change reverses a stated system policy; burying it in two reworded sentences would leave the reversal undocumented and invite re-debate. The §13 instance is the durable record.

Invalidation: the framework abandons the §13 "harness provides vs. we build" split (then CE grounding's framing moves with it).
