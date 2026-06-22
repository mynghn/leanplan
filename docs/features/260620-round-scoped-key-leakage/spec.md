# 260620-round-scoped-key-leakage — Spec

## Behavior
### B-1: durable-why-carries-substance-not-key

A durable artifact that carries a round's reason states it as substance, never as the round-scoped key. When an `impl` round promotes a reason into a durable artifact (code comment, commit / PR body, log, runbook), the artifact names the constraint in plain words — e.g. "tokens must never be stored in clear" — not the handle that points at it — e.g. "satisfies `C-1`". The reason crosses; only its round-local key is dropped.

One-shot test: run a round whose planning artifacts anchor a reason as `C-1`, then read the durable artifact it produces — the constraint appears in words, the token `C-1` does not.

## Constraint
### C-1: durable-artifacts-free-of-round-scoped-keys

Durable artifacts hold no round-scoped navigation handle used as a reference. Continuously gate-verifiable across produced durable outputs.

- **Covered artifacts** — code and inline comments, commit messages, PR descriptions and review comments, log lines and identifier names, runbooks — and any other durable surface: everything that outlives the round and is read without its planning docs.
- **Prohibited tokens** — any in-round anchor used as a reference (`B-<N>`, `C-<N>`, `D-<N>`, `T:<id>`, `Delta-<N>` — whether bare like "satisfies C-1" or in `Spec#…` / `Tasks#…` citation form), and any round-local feature id (`NNNN-slug`, `YYMMDD-slug`, bare tracker key) cited as a standing concept ("feature 0004").
- **Out of scope** — the round's own planning artifacts (`requirements.md`, `spec.md`, `design.md`, `tasks.md`, archives) keep their anchors, where they resolve. The prohibition is on carrying keys *out*, not on the in-round mechanism.
- **Not a violation** — a human-readable label that reuses a slug as the change's identity (a commit scope `docs(<slug>)`), or an external tracker link (a PR referencing its source issue by number / URL as a link). The target is the *opaque* handle used as if globally meaningful, not every id-shaped token.

## Non-goals

- **Anchor scheme unchanged** — no new id format, no renaming of the `B-` / `C-` / `D-` / `T:` / `Delta-` anchors or of feature ids.
- **Enforcement mechanism is Design's** — whether the guarantee lands as framework guidance, an `impl` close-out self-check, a pre-commit / CI gate, or a combination is not an observable of this contract; it is chosen at Design.
