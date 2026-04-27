# LP-EXAMPLE — SPEC

## Outcome

### O-1: single-invocation-sync

Running the sync command once copies the in-repo framework-doc body to the runtime location. After the command exits successfully, the runtime copy's body (excluding a preserved drift-marker header) hashes equal to the in-repo source byte-for-byte.

### O-2: staleness-reporting

The sync command reports, on exit, whether the runtime copy was stale before sync — either `already up-to-date` or `updated <prior-hash> -> <new-hash>` — so the operator observes whether a real change happened.

### O-3: missing-source-errors

When the in-repo source does not exist at its expected path, the sync command exits non-zero and prints a clear error; it does not silently succeed, create an empty runtime copy, or leave a partially-written runtime copy.

## Invariants

### INV-1: directional

Sync is in-repo source → runtime copy. The runtime copy is never written back to the in-repo source.

### INV-2: header-note-preservation

The runtime copy retains its drift-marker header across syncs. The header is not present in the in-repo source — it is a runtime-local annotation.

### INV-3: atomicity-under-failure

If the sync command fails mid-run (read error, write error), the runtime copy is either unchanged or fully updated — never half-written.
