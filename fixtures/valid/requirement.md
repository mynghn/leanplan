# LP-EXAMPLE — Automate LeanPlan framework-doc sync

## Problem

The canonical doc lives in two places: a canonical in-repo source at `upstream/docs/canonical-doc.md` (where it is authored and evolved) and a runtime copy at `~/.local/share/leanplan/framework-design.md` (consumed by both Claude Code and Codex skill adapters). Today the two are kept in sync by a manual copy + apply step — easy to forget, silently leaves the runtime stale while skills assume alignment with the latest framework doc. As the canonical doc evolves, the drift risk compounds.

## Outcome

Framework-doc evolutions made in the in-repo source propagate to the runtime copy reliably with a single command. The framework operator never has to remember a multi-step manual sync. Success signal: after editing the in-repo source, invoking the sync produces a runtime copy whose body content (excluding any preserved drift-marker header) hashes equal to the source byte-for-byte.

## Non-goals

- Cross-machine or cross-user sync. Personal-phase is single-user, single-machine.
- Generic file-sync utility. This is specifically for the framework doc.
- Bidirectional sync. The in-repo source is authoritative; the runtime copy is downstream-only.
