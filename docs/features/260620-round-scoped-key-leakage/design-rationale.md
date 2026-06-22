# 260620-round-scoped-key-leakage — Design Rationale

## D-1: guidance-carries-substance

Guidance is the only universal arm, so the rule's substance must live there regardless of what we mechanize. The implementation agent authors on surfaces no git hook or CI can see — runtime logs, runbooks, external wikis, the body of a Slack post — and guidance travels with the agent to all of them. So even in a world with a perfect mechanical gate, the guidance edit is load-bearing.

Why extend P7 rather than add a 9th principle: the leak is a *failure mode* of P7 ("persist by migration to code"), not a new axis of behavior. P7 already says "distill non-obvious WHYs into durable forms"; it simply never said "carry the substance, not the round-local key." Adding a standalone "round-scoped vs durable identifiers" principle was the alternative — rejected to keep philosophy.md lean (8 tight principles; a new one for a single failure mode dilutes the set). The distinction it would name is real but is better attached to P7, whose hierarchy is exactly where the migration happens, and cross-linked to P6 (transience) which is *why* the key dangles.

Why this closes the observed gap: the existing implementation close-out already had "distill WHYs" and "confirm plan artifacts non-load-bearing," yet leaks happened — because an agent can satisfy "I migrated the WHY" by writing "satisfies C-1", which *feels* migrated but smuggles the round-local key. The explicit guard ("substance, not the key") plus a concrete close-out self-check names the failure the prior wording allowed.

Invalidation triggers: if leaks persist on non-code surfaces despite the guidance, the distinction is under-weighted as a P7 clause and should be elevated to a standalone principle. If the self-check proves to be dead weight an agent rubber-stamps, lean harder on the mechanical arm instead of adding more prose.

## D-2: narrow-leak-detector

Match enforcement *strength* to detection *precision*. Two token classes leak, with very different precision:

- **Anchor tokens and citations** (`C-1`, `Spec#C-1-…`) are near-zero false-positive in durable code or prose — `-` is not an identifier character in mainstream languages, and an `<ARTIFACT>#<anchor>` citation essentially never occurs by accident. High precision → safe to mechanize.
- **Feature ids** (`0004`, `260620-…`, bare tracker keys) are low precision and sit in the grey zone the Spec explicitly excluded: a readable scope slug (`docs(lean-review-surfaces)`) and a PR↔issue numeric link are legitimate. A hard grep here generates false positives that erode trust until the gate is disabled wholesale.

So the detector covers only the high-precision class. A useful property falls out for free: because the narrow pattern matches neither readable slugs nor bare numbers, the grey-zone *needs no special-case exclusion logic* — the allowed cases simply don't match. The alternative (a broad grep with a curated allow-list to carve the grey zone back out) was rejected as both noisier and more code.

Why a separate `scan-leaks` rather than a `validate.py` mode: `validate.py` is contractually "comprehensive validator for a *feature dir*" — feature-scoped, structural. The leak lives *outside* the feature dir, across an arbitrary set of staged files and PR text. Overloading validate.py with a repo-wide, file-list-driven, text-driven scan would blur its clean input model. A focused sibling that shares the token vocabulary keeps both tools legible.

The dogfooding check: LeanPlan's own distillation hierarchy ranks durable forms types > tests > **custom lint (Tier 3)** > commit > PR > inline comment, and assigns cross-cutting rules to Tier 3. "No round-scoped key in durable artifacts" is a cross-cutting lexical rule. So the framework applied to its own rule prescribes a lint, not prose alone — guidance-only would persist a cross-cutting rule as the Tier-6 "last resort." Guidance + lint is the substance-and-enforcement pairing the feature itself advocates.

Invalidation triggers: if the false-positive rate is non-trivial even on the narrow class, tighten toward citations-only or lean on the suppression directive. If feature-id leaks prove costly in practice, revisit the broad scope deliberately — with the grey-zone allow-list that entails — rather than by reflex.

## D-3: per-surface-backstop

Guidance is universal but unobservable; a mechanical check is observable but necessarily per-surface. Each integration point exists because it sees a surface the others can't:

- **pre-commit** sees staged code before it lands — earliest feedback, works with no CI.
- **commit-msg** sees the message, which `pre-commit` cannot (the message does not exist yet at pre-commit time). Ships with the hook bundle so commit-message coverage does not depend on a repo having CI.
- **GitHub Action** sees PR descriptions and review comments, which *no* local git hook can observe — they are created server-side via the API/UI after push. This is the only place those surfaces are mechanically reachable, which is why the user's "also cover PR comments/descriptions" forces a GitHub-side component rather than another local hook.

An honest asymmetry: PR *descriptions* are gateable (block the PR check until the body is clean), but PR *comments* are post-hoc — already posted by the time anything sees them — so the most a check can do is detect-and-flag promptly, not prevent. True prevention on comments still rests on the guidance arm at authoring time.

The accepted boundary: logs, runbooks, wikis, and other surfaces get guidance but no mechanical gate. Building a detector for every conceivable durable surface is unbounded; the mechanical arm covers the high-frequency, reachable surfaces (code, message, PR) and guidance covers the long tail. We state this rather than implying total mechanical coverage.

Warn-by-default matches the existing `pre-commit-leanplan` stance and suits an imperfect-precision check: a warning surfaces the leak at write time, when the author still has context, without a hard block that invites disabling. `LEANPLAN_STRICT` / CI escalates to a block for teams that want the gate.

This repo currently has no CI, so the GitHub Action ships as an installable workflow *template* (alongside `pre-commit-leanplan`), not as live infra assumed present. Whether a given repo — including LeanPlan's own — enables it is an install choice, not a design dependency.

Invalidation trigger: if a new high-frequency leak surface appears (say, generated API docs), add an integration point for it; the detector core is already surface-agnostic, so the cost is one thin adapter, not a redesign.
