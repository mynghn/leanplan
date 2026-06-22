# 260621-reflexive-surface-budget — Design Rationale

## D-1: tier-by-procedural-trigger

The keep/defer call turns on one discriminator: does the step-scoped content have a reliable procedural load-trigger? That is what makes deferral safe (`Spec#C-1-deferral-preserves-guidance`) instead of a silent guidance loss.

- **Forces.** The framework preaches JIT-loading yet inlines everything in each reference. Two failure modes bound the choice: keep-all-inline (the reflexive gap stays open) vs. defer-all-step-scoped (deferring author-time calibration the agent may never fetch — the issue's explicit worry).
- **Why the trigger discriminator.** A procedure step is a reliable trigger: an agent walking the procedure *hits* it and loads the companion. impl.md's close-out tables have step 7. Worked examples and templates are consumed at the open-reference write-step, but no procedure step says "now load the example" — they calibrate passively, so deferral risks a silent skip. They stay inline, justified by the C-1 hazard, not by line-count timidity.
- **Chosen path.** Defer iff step-scoped AND gated by an explicit procedure step. Reuse the existing on-demand-pointer idiom — no new tier format, so nothing new to learn or to drift.
- **Invalidation.** If a future reference grows step-scoped content behind a real procedure step (e.g. a large author-time checklist gated by a "validate" step), it becomes a defer candidate under the same rubric.

## D-2: defer-impl-closeout-tables

impl.md's three close-out tables are the one clear win — high value, low risk.

- **Value.** ~35 lines / 33% of impl.md, consumed only at close-out (steps 7–8, 10). impl is the scarcest-window stage: it alone holds current code + JIT-loaded anchors + the card while re-reasoning, so always-resident close-out detail competes with the work that needs the window most. Trimming here beats trimming any author-time reference.
- **Risk.** Low. The tables are self-contained — they do not interleave with procedure prose — so the companion cannot drift from the steps. Step 7 is an unambiguous trigger. The instruction to distill stays inline; only the lookup tables move.
- **Alternative rejected.** Keep inline ("only 35 lines"). Rejected: the reflexive principle, not raw size, is the point — these are a textbook JIT candidate by the framework's *own* jit-loading rule, and impl is exactly where the window cost bites hardest.
- **Deployment (verified).** install.sh symlinks adapters only; references reach runtime via the whole-repo clone into `~/.local/share/leanplan/` (`chezmoi update` / `git pull`). A new `references/*.md` needs no install or config change.
- **Invalidation.** If close-out detail is ever needed mid-implementation (steps 1–6), the defer is wrong — re-inline.

## D-3: record-verdicts-type-level

Record verdicts at content-type level, not per block — a per-block table would itself become the new drift surface the audit exists to avoid.

- **Forces.** `Spec#B-1-hot-path-fully-adjudicated` needs every always-resident block to carry a recorded verdict, verifiable by reading the hot path. But a per-block keep/defer table goes stale on every reference edit, re-importing the surface-budget cost we are removing.
- **Chosen path.** Three stable type-verdicts (keep / keep-inline-justified / defer) here, plus the one-line-per-reference audit summary below. Deferred blocks self-evidence via their in-reference load-pointer; obvious keeps need no record. B-1 verification: walk each reference; every block maps to a type whose verdict is here; defers show a pointer.
- **Reflexive closure.** A brief durable principle is added to `artifact-contract.md`'s Surface Budget section — the section that caps user artifacts but was silent on the framework's own references. It now states the references follow the same tiering discipline. Advisory and on-demand (artifact-contract is a companion), not a new enforcement gate (`Spec` Non-goal: one-time resolution, not a standing gate). This is a mild scope-edge — it edits a companion, not the hot path — taken because it is the reflexively-correct home for the durable record; drop it if strict hot-path-only scope is preferred.

### Audit summary (per reference)

| Reference (prose lines) | Verdict |
|---|---|
| requirements.md (96) | keep all — stance/procedure/guardrails always-needed; template + worked examples are author-time calibration with no procedural trigger |
| specify.md (80) | keep all — as above (B/C-split worked example) |
| design.md (70) | keep all — Decision-body worked ✅/❌ are author-time calibration |
| tasks.md (95) | keep all — Goal/Completion worked ✅/❌ are author-time calibration |
| impl.md (106) | **defer** the 3 close-out tables → `impl-closeout.md` (step-7 trigger); keep stance / procedure / guardrails / stop-the-line / artifact-update-loop |
| adapters (SKILL.md) | keep — already thin (tier-0 loader + on-demand companion pointers) |
