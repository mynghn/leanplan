# 260623-concise-not-compressed — Design

## Architecture

```mermaid
flowchart TD
    subgraph home["artifact-contract.md § Prose Style (the one home)"]
      R1["Conclusion first"]
      R2["Lists over dense paragraphs"]
      R3["Short, declarative sentences"]
      NEW["Concise, not compressed — NEW bullet"]
    end
    RAT["§ Surface Budget + philosophy P3<br/>(small-surface review bet)"] -->|grounds| home
    STAGES["stage docs: requirements / specify / design / tasks .md"] -.->|"cite the section, never copy"| home
```

Caption: `§ Prose Style` is the single home; it gains one named bullet (bold node) beside the three existing form-rules. The `§ Surface Budget` + philosophy P3 rationale is unchanged and still grounds it. Stage docs keep *citing* the section rather than copying the lesson — the single-home boundary. Realizes `Spec#B-1-distinction-named-in-shared-home`, `Spec#B-2-discriminator-sorts-a-line`, `Spec#C-1-surface-not-grown`.

## D-1: named-bullet-not-woven

Add the lesson as a fourth titled bullet in `§ Prose Style`, not woven into an existing rule — because it governs a distinct axis (did shortening drop a distinct piece of information, or only redundancy?) from the form-rules beside it (sentence length, list-vs-paragraph), and `Spec#B-1-distinction-named-in-shared-home` / `Spec#B-2-discriminator-sorts-a-line` require a named, citable handle. Realization:

- **Bullet content** (final wording finalized in place at implement, against the surrounding prose — it must itself be concise-not-compressed):

  > **Concise, not compressed.** Cut redundancy, not meaning: drop what's repeated or already implied, never a distinct piece of information the reader needs (`bypass-check save` ❌ drops *which* check; "save without the duplicate check" ✅ keeps it). The same loss hides in a separator-joined pile, or even in plain words ("the save" for the one that skips the duplicate check). Ask what answer went missing, not how long the line is — a term or `·` that drops nothing is fine. Spend the words. (context-engineering: literal-vs-latent-matching)

- **Grounding hook** — the bullet ends with `(context-engineering: literal-vs-latent-matching)`. Decompressing a packed token is *latent* recovery — inferring the concept from a handle that does not state it — and latent recall degrades as the surface grows (NoLiMa), which is precisely the LLM-reviewer-over-a-long-surface case. The hook matches the section's grounding convention (One-Prose-Home, Surface Budget both end in one) and reinforces the reflexive-grounding moat.
- **Worked contrast, inline** — a minimal good→bad pair (`bypass-check save` ❌ vs. plain depiction ✅), not a full ✅/❌ block. The example shows a **dropped axis restored** (which check), not just a reworded term — the discriminator is *what information went missing*, so the ✅ restores the same axis the ❌ deleted. The lexical case is primary (the more insidious); the pile and plain-but-lossy phrasing are named as the same loss, no separate example. It must not imply the *vocabulary or separator* is the defect — a familiar term and a stage-map `·` drop nothing and stay fine, which is what `Spec#B-2-discriminator-sorts-a-line` clears. The contrast is the doc's own §134 register; a full block belongs in a stage doc and fights `C-1`. (re-centered on axis-preservation — `Understanding#Delta-2-brevity-removes-redundancy-not-an-axis`)
- **Placement** — last in the bullet list, as the capstone: even after you have shortened sentences and used lists, do not compress. (Trivial ordering call.)
- **Citable handle** — the bold lead `**Concise, not compressed.**` is the name a reviewer cites when rejecting a compressed line (`Spec#B-2-discriminator-sorts-a-line`); the inline good→bad contrast is the recognizer, the "what answer went missing" line is the discriminator.

See rationale at [design-rationale.md#D-1-named-bullet-not-woven].

## D-2: single-home-held-surface

Author the lesson once in `§ Prose Style` and hold the section's prose footprint flat-or-smaller, satisfying `Spec#C-1-surface-not-grown`. Realization:

- **One home, no copies** — the lesson goes only in `§ Prose Style`; the stage docs already cite the section, so none is edited (the single-home rule, `artifact-contract.md` → One Prose Home Per Fact).
- **Offset the added lines by tightening adjacent slack**, not by adding net length — the longest existing bullet (`Conclusion first`) and the section `Why:` line carry trim-able verbosity. Tightening keeps `Spec` Non-goal *sharpens-does-not-replace*: trim prose, never a rule's meaning.
- **Verify the delta, not just the size** — the stateless surface-budget guard sees absolute size; non-growth is confirmed by reading the diff, and single-home by grepping the stage docs for any copy.
- **Deployment** — editing an existing tracked reference; it rides the existing whole-repo clone refresh (`chezmoi update` / `git pull`). No new file, no `install.sh` or symlink change.

See rationale at [design-rationale.md#D-2-single-home-held-surface].
