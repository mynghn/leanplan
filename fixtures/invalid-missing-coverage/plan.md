# LP-EXAMPLE — TASK

## Guidelines

- Strictly additive to chezmoi source — no edits to the framework doc itself; the script is expected to overwrite the runtime copy at apply time.

## Dependency DAG

```mermaid
flowchart LR
    subgraph S [Script]
        S1[S1: sync script] --> S2[S2: smoke test]
    end
```

Single track (`S` = script). Tiny feature.

## Task: S1

**Goal**: Author `dot_local/share/leanplan/scripts/executable_sync-leanplan.sh` in chezmoi source per `DESIGN#Decision-1-sync-as-shell-script-in-canonical-scripts`. Script hard-codes the in-repo path per `DESIGN#Decision-2-in-repo-path-hard-coded`, re-inserts the runtime header note between title and body per `DESIGN#Decision-3-header-note-reinsertion-between-title-and-body`, invokes `chezmoi apply ~/.local/share/leanplan/framework-design.md` at the end per `DESIGN#Decision-4-chezmoi-apply-called-at-script-end`, and prints `already up-to-date <hash>` or `updated <prior> -> <new>` via `shasum -a 256` per `DESIGN#Decision-5-hash-check-via-shasum`. Error-exit before writing anything when the in-repo source is absent, satisfying `SPEC#O-3-missing-source-errors`.

**Repo**: `mynghn/dotfiles` (chezmoi source).

**Completion criteria**:

- Runtime `~/.local/share/leanplan/scripts/sync-leanplan.sh` exists and is executable after `chezmoi apply`.
- After making a whitespace edit in the in-repo source, running the script causes `shasum -a 256 ~/.local/share/leanplan/framework-design.md` to change to match the new in-repo body — verifies `SPEC#O-1-single-invocation-sync` and `SPEC#INV-1-directional`.
- Running the script with the in-repo path temporarily renamed produces exit status non-zero, a stderr error message, and leaves the runtime file unchanged — verifies `SPEC#O-3-missing-source-errors`.
- Runtime file body (lines from the framework intro paragraph onward) is byte-equal to the in-repo body after sync; the drift-marker header `> Runtime canonical at ...` remains on line 3 — verifies `SPEC#INV-2-header-note-preservation`.

**Dependencies**: none.

## Task: S2

**Goal**: Smoke-test the round trip. Evolve the in-repo source with a whitespace-only edit; run the sync; verify the runtime copy reflects it and the header note survives, per `SPEC#O-1-single-invocation-sync` and `SPEC#INV-2-header-note-preservation`. Then rename the source temporarily; run the sync; verify non-zero exit + unchanged runtime per `SPEC#O-3-missing-source-errors`.

**Repo**: local (no commit).

**Completion criteria**:

- One successful happy-path run + one error-path run observed and noted.

**Dependencies**: S1 (enabler — script must exist).

## Forward coverage

| SPEC item | Realized by |
|---|---|
| O-1 single-invocation-sync | S1 + S2 Completion |
| O-3 missing-source-errors | S1 + S2 Completion |
| INV-1 directional | S1 Completion ("matches new in-repo body"; no reverse-write path tested because architecture forbids it) |
| INV-2 header-note-preservation | S1 + S2 Completion |
| INV-3 atomicity-under-failure | **GAP** — no task explicitly tests mid-run failure. Decision-6 accepts a small non-atomic window (source-write vs chezmoi-apply) with self-heal on next run. Acceptable for personal-phase; revisit if atomicity becomes load-bearing. |
