# 260622-human-user-manual — Understanding

## Delta-1: multi-file-guide-suite

The manual ships as a multi-file `docs/user-guide/` suite behind a single `USER_GUIDE.md` front door — entry orientation, the Quickstart first-use path, and a depth-routed table of contents — rather than as one single-file guide.

This supersedes the single-file decision in `Design#D-1-top-level-user-guide` (one `USER_GUIDE.md` holding three in-file parts) and its rejection of a `docs/` page tree, the in-`Using-LeanPlan` adoption placement in `Design#D-5-adoption-section`, and the in-file reference appendix in `Design#D-6-reference-appendix`.

Why: the suite grew to ~600 lines (`mechanisms.md` alone ~200) — past the point where one file serves the progressive-disclosure Guarantee a first-time reader depends on. The single front door neutralizes D-1's "too many choices" concern (the reader sees one entry, not a flat set of pages), and per-page just-in-time loading is reflexively consistent with LeanPlan's own JIT-loading and one-prose-home principles. D-1's own deferral condition — "split later if the reference section becomes too large to scan" — is now met. Cause: a deliberate structural change as the content grew, ratified after the fact; no Requirements or Spec change is implied.

Scope-of-impact: `Design#D-1-top-level-user-guide`, `Design#D-5-adoption-section`, `Design#D-6-reference-appendix`, `Tasks#T:D1`, `Tasks#T:D3`.
