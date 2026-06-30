# 260630-item-orthogonality — Deferrals

### Defer-1: existing-artifact-reconciliation-scope

**Owning stage:** Tasks.

Open question: how far does the rollout reconcile *existing* framework artifacts to the new item-orthogonality rule — only dogfood the docs this feature edits, or also bounded-audit the highest-overlap-risk existing items (e.g. the Spec B/C worked example, shipped feature specs)?

Why it surfaced now: the Outcome calls item-orthogonality a "first-class property of LeanPlan artifacts," which invites a reflexive sweep — but a full retroactive audit of all shipped artifacts would balloon a one-deployment feature, so the boundary is unsettled.

Forces glimpsed: reflexivity is a framework value (its own surface should obey its rules) ↔ one-deployment scope guardrail ↔ a bounded "touch what you edit + the canonical example" pass may capture most value cheaply.

Option seen (not chosen): scope reconciliation to artifacts this feature already edits, treating a broader audit as a separate follow-up.
Left open for Tasks to re-derive against the actual edit set.
