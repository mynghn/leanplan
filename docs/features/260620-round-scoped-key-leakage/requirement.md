# 260620-round-scoped-key-leakage — keep round-scoped keys out of durable artifacts

## Problem

LeanPlan's round-scoped identifiers keep leaking into artifacts that outlive the round, where they can no longer be decoded. Anchors (`O-`, `INV-`, `Decision-`) and feature ids (`0004`, `260620-…`) are navigation handles: they resolve only against one feature's planning artifacts. Yet `impl` work repeatedly emits them as if they were durable, global terms — a code comment "satisfies `INV-1`", a commit or PR body citing "feature `0004`" as a standing concept, a variable or log name built around a round key.

Those durable artifacts get read later *without* the planning docs in context — and the planning docs may be gone, since the framework treats them as discardable and the code as the truth. The reader then meets "`INV-1`" or "feature `0004`" with no way to tell which feature or which invariant was meant: a dangling, unresolvable reference. The ephemeral has leaked into the permanent.

## Outcome

Round-scoped identifiers stay inside the round that owns them. The framework already distills the *substance* of a reason into durable artifacts; this feature adds the matching restraint at the boundary — the substance crosses, the key does not. Future state: durable artifacts (code, comments, commit and PR bodies, logs, runbooks) read as self-contained, decodable without the round's planning docs.

- **Substance crosses, the key doesn't** — when a durable artifact needs a round's WHY, it states the constraint in plain terms ("tokens must never be stored in clear"), never the opaque handle ("satisfies `INV-1`"). The reason is durable; the round-local key for it is not.
- **Round keys stay in-round** — anchors and feature ids remain inside the feature's own planning artifacts, where they resolve and load on demand. Carried outward, they only strand.

The signal: no dangling round-scoped reference survives into durable space — every reason kept there stands on its own.

## Non-goals

- **In-round citation is untouched** — anchors still cross-reference freely *within* a round; that is the whole point of the scheme. This feature only stops keys from crossing *out*.
- **No change to the anchor scheme** — no new id format, no renaming of `O-` / `INV-` / `Decision-` or of feature ids.
- **Readable references aren't the target** — a human-meaningful scope label, or an external tracker link (a PR referencing its source issue), resolves on its own. The target is *opaque, round-local* keys used as if globally meaningful — not every id-shaped token in durable space.

## Upstream

- GitHub issue #11 — "Backlog: D — round-scoped keys must not leak into durable artifacts": https://github.com/mynghn/leanplan/issues/11
