#!/usr/bin/env python3
"""Validate LeanPlan feature artifacts.

Usage:
  python3 validate.py docs/features/0007-anomaly-publisher [--stage full] [--json] [--allow-large]
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


SURFACE_FILES = {
    "requirements": "requirements.md",
    "spec": "spec.md",
    "design": "design.md",
    "tasks": "tasks.md",
}

OPTIONAL_FILES = {
    "rationale": "design-rationale.md",
    "research": "research.md",
    "understanding": "understanding-shifts.md",
    "deferrals": "deferrals.md",
}

ARTIFACT_ORDER = ("requirements", "spec", "design", "tasks")

# Surface-budget soft caps, in PROSE lines (fenced code/diagrams and blank lines
# excluded — see _prose_line_count). The grounding is distractor/review-fidelity
# density, which is a prose property; a big Mermaid diagram or inline schema is
# legit reference detail, not bloat, so it must not trip the cap. Advisory
# backstop for pathological bloat, NOT a budget to fill — a well-formed
# one-deployment artifact sits far under these. Mirrors the DAG-size guardrail:
# warn by default, --strict escalates to error, --allow-large suppresses.
# Direction, not a hard cap; tune per repo. Source of truth:
# references/artifact-contract.md → "Surface Budget" — this dict mirrors that
# list; keep the two in sync.
SURFACE_SOFT_CAP = {"requirements": 90, "spec": 110, "design": 160, "tasks": 220}

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
# A trailing ` (retired)` marker is tolerated on any anchor/Task heading: a
# superseded item is retired by marking its heading (artifact-contract.md ->
# Anchors), and its ID must keep resolving in that retired state so inbound
# citations don't break (the marker is captured into its own group, never folded
# into the id/target). Without this the marker would silently de-resolve the
# anchor — the exact loss retire-by-note exists to prevent. Coverage is the one
# place the retired state DOES matter: a retired Task grants no forward-coverage
# credit (see _check_traceability), so a superseded card can't satisfy a live B.
RETIRED_SUFFIX = r"(\s+\(retired\))?"
# Deferral anchors additionally tolerate a `(resolved -> <citation>)` resolve-in-place
# marker (artifact-contract.md -> Deferrals): a drained deferral is retired in place by
# appending the marker to its heading, citing where the decision landed. Like `(retired)`,
# the marker is captured into its own group and never folded into the id/slug, so the
# Defer-<N> ID keeps resolving in its resolved state; the target cited inside the marker is
# itself resolution-checked by CITATION_RE (a slug-deep marker still flags broken). ANCHOR_RE
# tolerates either marker (harmless on B/C/D/Delta, load-bearing on Defer); TASK_RE stays
# retired-only — a Task is not a deferral. `Defer` precedes `D` in the kind alternation (as
# `Delta` does), so a `Defer-N` heading never first-matches the `D` (Design decision) branch.
ANCHOR_TRAILING_MARKER = r"(\s+\((?:retired|resolved\s*->[^)]*)\))?"
ANCHOR_RE = re.compile(r"^(#{2,4})\s+((B|C|Delta|Defer|D)-(\d+):\s+([a-z0-9][a-z0-9-]*))" + ANCHOR_TRAILING_MARKER + r"\s*$", re.MULTILINE)
TASK_RE = re.compile(r"^(#{2,4})\s+T:\s+([A-Za-z][A-Za-z0-9-]*)" + RETIRED_SUFFIX + r"\s*$", re.MULTILINE)
CITATION_RE = re.compile(
    r"\b(?P<file>Spec|Design|Rationale|Research|Tasks|Understanding|Deferrals)#(?P<target>"
    r"(?:B|C|D)-\d+-[a-z0-9][a-z0-9-]*|Delta-\d+-[a-z0-9][a-z0-9-]*|Defer-\d+-[a-z0-9][a-z0-9-]*|T:[A-Za-z][A-Za-z0-9-]*)"
)
# The owning-stage field of a Defer-N block (artifact-contract.md -> Deferrals):
# `**Owning stage**: <Requirements|Spec|Design|Tasks>`. The no-loss check reads it
# to decide which stage a deferral is addressed to, then keys the advisory on
# whether that stage's artifact already exists.
DEFER_OWNER_RE = re.compile(r"\*\*Owning stage\*\*:\s*([A-Za-z]+)", re.IGNORECASE)
# A Spec B/C item appearing on a line containing **GAP** is treated as
# deliberately uncovered — see references/artifact-contract.md "**GAP**
# acknowledgment". Validator skips it in forward-coverage checks.
GAP_RE = re.compile(r"\*\*GAP\*\*")
FRONTMATTER_RE = re.compile(r"^---\s*\n.*?\n---\s*\n", re.DOTALL)
CODE_FENCE_RE = re.compile(r"```(?P<lang>[A-Za-z0-9_-]*)\n(?P<body>.*?)```", re.DOTALL)
SCRIPTY_TASK_RE = re.compile(
    r"\b(edit|modify|change|replace)\s+(?:file\s+)?[`'\"]?[^`\n'\"]+[`'\"]?\s+"
    r"(?:at|on)\s+(?:line|L)\s*\d+",
    re.IGNORECASE,
)


@dataclass
class Issue:
    level: str
    path: str
    message: str
    line: int | None = None


class Validator:
    def __init__(self, feature_dir: Path, stage: str, allow_large: bool, strict: bool = False) -> None:
        self.feature_dir = feature_dir
        self.stage = stage
        self.allow_large = allow_large
        self.strict = strict
        self.issues: list[Issue] = []
        self.texts: dict[str, str] = {}

    def run(self) -> list[Issue]:
        self._load_files()
        self._check_required_files()
        self._check_common()
        self._check_surface_size()
        self._check_deferrals_no_loss()

        if self._includes("requirements"):
            self._check_requirement()
        if self._includes("spec"):
            self._check_spec()
        if self._includes("design"):
            self._check_design()
        if self._includes("tasks"):
            self._check_plan()
            self._check_traceability()
        return self.issues

    def _includes(self, stage: str) -> bool:
        if self.stage == "full":
            return True
        return ARTIFACT_ORDER.index(stage) <= ARTIFACT_ORDER.index(self.stage)

    def _load_files(self) -> None:
        for key, filename in {**SURFACE_FILES, **OPTIONAL_FILES}.items():
            path = self.feature_dir / filename
            if path.exists():
                self.texts[key] = path.read_text(encoding="utf-8")

    def _check_required_files(self) -> None:
        if not self.feature_dir.exists():
            self._error(".", f"feature directory does not exist: {self.feature_dir}")
            return
        for stage in ARTIFACT_ORDER:
            if self._includes(stage) and stage not in self.texts:
                self._error(SURFACE_FILES[stage], "required surface artifact is missing")

    def _check_common(self) -> None:
        for key, text in self.texts.items():
            filename = self._filename_for_key(key)
            if FRONTMATTER_RE.match(text):
                self._warn(filename, "frontmatter is discouraged; artifact type is implied by filename", 1)
            self._check_duplicate_anchors(filename, text)
            self._check_citations(filename, text)
            self._check_must_usage(filename, text)

    def _prose_line_count(self, text: str) -> int:
        # Review-surface prose only: exclude fenced code/diagram blocks (Mermaid,
        # schemas, code samples are legit reference detail, not attention-diluting
        # prose) and blank lines (whitespace aids review; don't penalize it).
        # Toggle in/out of a fence on any ``` or ~~~ line so unclosed, tilde,
        # indented, or info-stringed fences are all handled (a paired-regex
        # substitution would miss those and miscount their bodies as prose).
        count = 0
        in_fence = False
        for line in text.splitlines():
            if re.match(r"^\s*(```|~~~)", line):
                in_fence = not in_fence
                continue
            if not in_fence and line.strip():
                count += 1
        return count

    def _check_surface_size(self) -> None:
        # Surface-budget guardrail (advisory). --allow-large suppresses entirely;
        # --strict escalates a breach to error. Direction, not a hard cap.
        if self.allow_large:
            return
        for stage in ARTIFACT_ORDER:
            if not self._includes(stage) or stage not in self.texts:
                continue
            cap = SURFACE_SOFT_CAP[stage]
            lines = self._prose_line_count(self.texts[stage])
            if lines <= cap:
                continue
            msg = (
                f"{SURFACE_FILES[stage]} has {lines} prose lines (> {cap} soft cap; "
                "diagrams/code excluded); small-surface guardrail — tighten the prose, "
                "move depth to Rationale/Research, or split the feature"
            )
            if self.strict:
                self._error(SURFACE_FILES[stage], msg)
            else:
                self._warn(SURFACE_FILES[stage], msg)

    def _check_deferrals_no_loss(self) -> None:
        # Advisory no-loss check for the Deferrals lane. A Defer-N addressed to a
        # stage whose <stage>.md already exists, but carrying no resolve-in-place
        # marker on its heading, is an undrained deferral at or past its owning
        # stage — surface it. Warn by default; --strict escalates, mirroring the
        # surface-budget guardrail. NOT a hard gate: an unresolved deferral for a
        # stage not yet authored is legitimate (that file does not exist -> skipped).
        # STRUCTURAL half only — whether a marked-resolved deferral genuinely landed
        # where it cites is the Close-Out Reconciliation tier the validator cannot
        # see (it reads artifacts, not the decisions behind them).
        text = self.texts.get("deferrals", "")
        if not text:
            return
        heads = sorted(m.start() for m in HEADING_RE.finditer(text))
        for match in ANCHOR_RE.finditer(text):
            if match.group(3) != "Defer":
                continue
            if match.group(6):  # trailing marker (resolved -> … or retired) = accounted for
                continue
            defer_target = f"Defer-{match.group(4)}-{match.group(5)}"
            # Owning stage is read from the block body (this heading -> next heading).
            body_end = next((h for h in heads if h > match.start()), len(text))
            owner_match = DEFER_OWNER_RE.search(text[match.end():body_end])
            if not owner_match:
                continue  # no parseable owning stage — substance (review) tier catches it
            owner = owner_match.group(1).lower()
            if owner not in SURFACE_FILES or owner not in self.texts:
                continue  # unrecognized, or owning stage not yet authored — not a structural call
            msg = (
                f"undrained deferral {defer_target} addressed to {owner}, whose "
                f"{SURFACE_FILES[owner]} already exists — drain it at the {owner} stage and "
                "mark it resolved, or it is a silently-dropped omission"
            )
            line = self._line_for_offset(text, match.start())
            if self.strict:
                self._error("deferrals.md", msg, line)
            else:
                self._warn("deferrals.md", msg, line)

    def _check_requirement(self) -> None:
        text = self.texts.get("requirements", "")
        if not text:
            return
        self._require_sections("requirements.md", text, ("Problem", "Outcome"))
        self._warn_empty_conditional("requirements.md", text, ("Guarantee", "Non-goals", "Upstream"))
        banned = ("Kafka", "Redis", "Spring", "Kotlin", "Postgres", "MySQL", "gRPC", "Flink")
        for term in banned:
            if re.search(rf"\b{re.escape(term)}\b", text):
                self._warn("requirements.md", f"possible implementation choice in Requirements: {term}")

    def _check_spec(self) -> None:
        text = self.texts.get("spec", "")
        if not text:
            return
        self._require_sections("spec.md", text, ("Behavior",))
        behaviors = self._anchors("spec", kind="B")
        if not behaviors:
            self._error("spec.md", "Spec Behavior must contain at least one B anchor")
        if self._has_section(text, "Constraint") and not self._anchors("spec", kind="C"):
            self._error("spec.md", "Constraint section exists but has no C anchors")
        self._warn_empty_conditional("spec.md", text, ("Constraint", "Non-goals"))
        if re.search(r"^\s*-\s+\[[ xX]\]", text, re.MULTILINE):
            self._warn("spec.md", "checkbox acceptance criteria are not LeanPlan anchors")

    def _check_design(self) -> None:
        text = self.texts.get("design", "")
        if not text:
            return
        self._require_sections("design.md", text, ("Architecture",))
        if "```mermaid" not in text:
            self._error("design.md", "Architecture must include a Mermaid diagram")
        if not self._anchors("design", kind="D"):
            self._error("design.md", "Design must contain at least one D anchor")
        self._check_design_rationale_consistency()

    def _check_plan(self) -> None:
        text = self.texts.get("tasks", "")
        if not text:
            return
        # tasks.md may use either "Dependency DAG" or just "DAG" as the section header.
        if self._has_section(text, "Dependency DAG"):
            dag_section = "Dependency DAG"
        elif self._has_section(text, "DAG"):
            dag_section = "DAG"
        else:
            self._error("tasks.md", "missing required section: Dependency DAG (or DAG)")
            dag_section = None
        if dag_section and "```mermaid" not in self._section_body(text, dag_section):
            self._error("tasks.md", f"{dag_section} must be Mermaid")
        self._warn_ascii_diagram("tasks.md", text)
        tasks = self._tasks()
        if not tasks:
            self._error("tasks.md", "Tasks artifact must contain at least one task card")
        # One-deployment guardrail: advisory by default; --strict escalates to error;
        # --allow-large overrides entirely.
        if not self.allow_large:
            if len(tasks) > 16:
                msg = f"task count {len(tasks)} exceeds one-deployment guardrail (>16)"
                if self.strict:
                    self._error("tasks.md", msg)
                else:
                    self._warn("tasks.md", msg)
            elif len(tasks) > 12:
                self._warn("tasks.md", f"task count {len(tasks)} is near the one-deployment limit (>12)")
        if re.search(r"^\s*-\s+\[[ xX]\]", text, re.MULTILINE):
            self._warn("tasks.md", "checkbox task lists are discouraged; use task cards")
        for task_id, body, line in tasks:
            if SCRIPTY_TASK_RE.search(body):
                self._warn("tasks.md", f"Task {task_id} looks like line-level scripting", line)
            if not self._task_has_reason(body):
                self._error("tasks.md", f"Task {task_id} has no Spec/Design/guideline reason citation", line)

    def _check_traceability(self) -> None:
        if "spec" not in self.texts or "tasks" not in self.texts:
            return
        plan_text = self.texts.get("tasks", "")
        # Collect Spec item IDs annotated as **GAP** in tasks.md (deliberately uncovered).
        gap_acked = self._gap_acknowledged_targets(plan_text)
        # Coverage credit comes only from LIVE tasks: a retired (superseded) task's
        # citations must not satisfy a live Spec item, else retiring the sole task
        # of a live behavior would silently pass a real coverage hole.
        coverage_text = self._plan_text_excluding_retired_tasks(plan_text)
        for anchor in self._anchors("spec", kind="B") + self._anchors("spec", kind="C"):
            target = anchor["target"]
            if f"Spec#{target}" in coverage_text:
                continue
            if target in gap_acked:
                continue
            self._error("tasks.md", f"Spec anchor is not covered by any task: Spec#{target}")

    def _gap_acknowledged_targets(self, plan_text: str) -> set[str]:
        """Return Spec item targets (e.g. 'B-1-foo' or 'C-3-bar') annotated on a
        line containing **GAP**. Lines may reference the item by full target
        (B-1-foo / C-3-bar) or by ID alone (B-1 / C-3); both forms are
        accepted as ack."""
        acked: set[str] = set()
        # Map ID-only to full targets we know about so a bare 'C-3' on a GAP
        # line ack's C-3-<whatever-slug>.
        spec_targets = {a["target"] for a in self._anchors("spec", kind="B")} | {
            a["target"] for a in self._anchors("spec", kind="C")
        }
        id_to_targets: dict[str, list[str]] = {}
        for t in spec_targets:
            # target form: 'B-1-foo-bar' or 'C-3-baz'; extract 'B-1' / 'C-3'.
            m = re.match(r"((?:B|C)-\d+)-", t)
            if m:
                id_to_targets.setdefault(m.group(1), []).append(t)
        for line in plan_text.splitlines():
            if not GAP_RE.search(line):
                continue
            # Full-target form on the GAP line.
            for m in re.finditer(r"\b((?:B|C)-\d+-[a-z0-9][a-z0-9-]*)\b", line):
                acked.add(m.group(1))
            # ID-only form on the GAP line — ack all matching targets.
            for m in re.finditer(r"\b((?:B|C)-\d+)\b", line):
                for t in id_to_targets.get(m.group(1), []):
                    acked.add(t)
        return acked

    def _check_duplicate_anchors(self, filename: str, text: str) -> None:
        seen: dict[str, int] = {}
        for item in self._parse_anchors(text):
            target = item["target"]
            if target in seen:
                self._error(filename, f"duplicate anchor: {target}", item["line"])
            seen[target] = item["line"]
        seen_tasks: dict[str, int] = {}
        for task in self._parse_tasks(text):
            target = f"T:{task['id']}"
            if target in seen_tasks:
                self._error(filename, f"duplicate task anchor: {target}", task["line"])
            seen_tasks[target] = task["line"]

    def _check_citations(self, filename: str, text: str) -> None:
        anchors_by_file = {
            "Spec": {a["target"] for a in self._anchors("spec")},
            "Design": {a["target"] for a in self._anchors("design")},
            "Rationale": {a["target"] for a in self._anchors("rationale")},
            "Tasks": {f"T:{t['id']}" for t in self._parse_tasks(self.texts.get("tasks", ""))},
            # Inbound Understanding#Delta-N citations resolve against understanding-shifts.md's
            # delta anchors — a revised artifact cites the Delta that justified it. Research
            # stays skipped below: it carries descriptive headings, not a resolvable anchor set.
            "Understanding": {a["target"] for a in self._anchors("understanding")},
            # Inbound `Deferrals#` citations resolve against deferrals.md's `Defer` anchors —
            # e.g. a Design decision noting it resolved a parked deferral.
            "Deferrals": {a["target"] for a in self._anchors("deferrals")},
        }
        for match in CITATION_RE.finditer(text):
            file_key = match.group("file")
            target = match.group("target")
            if file_key == "Research":
                continue
            if target not in anchors_by_file.get(file_key, set()):
                self._error(filename, f"broken citation: {file_key}#{target}", self._line_for_offset(text, match.start()))

    def _check_must_usage(self, filename: str, text: str) -> None:
        if filename == "spec.md":
            return
        for match in re.finditer(r"\bMUST(?:\s+NOT)?\b", text):
            self._warn(filename, "MUST/MUST NOT should be reserved for true invariants", self._line_for_offset(text, match.start()))

    def _check_design_rationale_consistency(self) -> None:
        design_anchors = {a["target"] for a in self._anchors("design", kind="D")}
        rationale_anchors = {a["target"] for a in self._anchors("rationale", kind="D")}
        # Orphan-rationale-block check needs the file to exist; but the
        # design->rationale LINK check below must run even when design-rationale.md
        # is ENTIRELY absent — a Design that links design-rationale.md#D-N
        # with no such file is a dangling pointer, the strictly-worse case of the
        # missing-block error. Gating the whole method on file presence (an early
        # return) silently passed it; gate only the orphan loop instead.
        if "rationale" in self.texts:
            for target in rationale_anchors - design_anchors:
                self._error("design-rationale.md", f"rationale decision has no matching Design decision: {target}")
        for target in design_anchors:
            if f"design-rationale.md#{target}" in self.texts.get("design", "") and target not in rationale_anchors:
                self._error("design-rationale.md", f"Design links to missing rationale block: {target}")

    def _task_has_reason(self, body: str) -> bool:
        # B / C / D are the live anchor vocabulary (§9 dropped "AC").
        # Must match CITATION_RE's kinds so a Behavior-only task — permitted by
        # the contract, common for trivial-realization features — is accepted.
        if re.search(r"\b(Spec#(?:B|C)-\d+-[a-z0-9-]+|Design#D-\d+-[a-z0-9-]+)", body):
            return True
        return bool(re.search(r"\*\*Guidelines\*\*:\s*\S|^## Guidelines\b", body, re.MULTILINE))

    def _warn_ascii_diagram(self, filename: str, text: str) -> None:
        for fence in CODE_FENCE_RE.finditer(text):
            lang = fence.group("lang").strip().lower()
            body = fence.group("body")
            if lang == "" and ("┌" in body or "-->" in body or "->" in body):
                self._warn(filename, "ASCII diagram/code-fence detected; use Mermaid", self._line_for_offset(text, fence.start()))
        if re.search(r"^\s*#{2,4}\s+ASCII DAG\b", text, re.MULTILINE):
            self._warn(filename, "ASCII DAG section detected; use Mermaid only")

    def _require_sections(self, filename: str, text: str, sections: tuple[str, ...]) -> None:
        for section in sections:
            if not self._has_section(text, section):
                self._error(filename, f"missing required section: {section}")

    def _warn_empty_conditional(self, filename: str, text: str, sections: tuple[str, ...]) -> None:
        for section in sections:
            if self._has_section(text, section) and not self._section_body(text, section).strip():
                self._warn(filename, f"conditional section is empty: {section}")

    def _has_section(self, text: str, section: str) -> bool:
        return bool(re.search(rf"^##\s+{re.escape(section)}\s*$", text, re.MULTILINE))

    def _section_body(self, text: str, section: str) -> str:
        match = re.search(rf"^##\s+{re.escape(section)}\s*$", text, re.MULTILINE)
        if not match:
            return ""
        next_match = re.search(r"^##\s+", text[match.end() :], re.MULTILINE)
        end = match.end() + next_match.start() if next_match else len(text)
        return text[match.end() : end]

    def _anchors(self, key: str, kind: str | None = None) -> list[dict[str, object]]:
        return [
            a
            for a in self._parse_anchors(self.texts.get(key, ""))
            if kind is None or a["kind"] == kind
        ]

    def _tasks(self) -> list[tuple[str, str, int]]:
        text = self.texts.get("tasks", "")
        parsed = self._parse_tasks(text)
        result = []
        for index, task in enumerate(parsed):
            start = int(task["end"])
            end = int(parsed[index + 1]["start"]) if index + 1 < len(parsed) else len(text)
            result.append((str(task["id"]), text[start:end], int(task["line"])))
        return result

    def _parse_anchors(self, text: str) -> list[dict[str, object]]:
        anchors = []
        for match in ANCHOR_RE.finditer(text):
            kind = match.group(3)
            number = match.group(4)
            slug = match.group(5)
            anchors.append({
                "kind": kind,
                "target": f"{kind}-{number}-{slug}",
                "line": self._line_for_offset(text, match.start()),
            })
        return anchors

    def _parse_tasks(self, text: str) -> list[dict[str, object]]:
        tasks = []
        for match in TASK_RE.finditer(text):
            tasks.append({
                "id": match.group(2),
                "retired": bool(match.group(3)),
                "start": match.start(),
                "end": match.end(),
                "line": self._line_for_offset(text, match.start()),
            })
        return tasks

    def _plan_text_excluding_retired_tasks(self, plan_text: str) -> str:
        """plan_text with every retired Task card's span removed, so a superseded
        task grants no forward-coverage credit. A retired card is kept for history
        via retire-by-note, but it is dead work — it must not satisfy a live Spec
        item. Span = the retired heading through just before the next task heading
        (or end of text for the last card)."""
        parsed = self._parse_tasks(plan_text)
        cuts = []
        for index, task in enumerate(parsed):
            if not task.get("retired"):
                continue
            start = int(task["start"])
            end = int(parsed[index + 1]["start"]) if index + 1 < len(parsed) else len(plan_text)
            cuts.append((start, end))
        if not cuts:
            return plan_text
        kept, prev = [], 0
        for start, end in cuts:
            kept.append(plan_text[prev:start])
            prev = end
        kept.append(plan_text[prev:])
        return "".join(kept)

    def _filename_for_key(self, key: str) -> str:
        if key in SURFACE_FILES:
            return SURFACE_FILES[key]
        return OPTIONAL_FILES[key]

    def _line_for_offset(self, text: str, offset: int) -> int:
        return text.count("\n", 0, offset) + 1

    def _error(self, path: str, message: str, line: int | None = None) -> None:
        self.issues.append(Issue("error", path, message, line))

    def _warn(self, path: str, message: str, line: int | None = None) -> None:
        self.issues.append(Issue("warning", path, message, line))


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate LeanPlan feature artifacts")
    parser.add_argument("feature_dir", type=Path)
    parser.add_argument(
        "--stage",
        choices=("requirements", "spec", "design", "tasks", "full"),
        default="full",
        help="Validate through the selected stage",
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    parser.add_argument(
        "--allow-large",
        action="store_true",
        help="Suppress size guardrails: allow >16 tasks and over-cap surface artifacts",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help=(
            "Strict mode: escalate the one-deployment guardrail breach (>16 tasks) to an error, "
            "and exit non-zero if any warnings are present. Honors $LEANPLAN_STRICT=1 as well."
        ),
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    strict = args.strict or os.environ.get("LEANPLAN_STRICT") == "1"
    issues = Validator(args.feature_dir, args.stage, args.allow_large, strict).run()
    if args.json:
        print(json.dumps([asdict(issue) for issue in issues], ensure_ascii=False, indent=2))
    else:
        if not issues:
            print("LeanPlan validation passed.")
        else:
            for issue in issues:
                loc = issue.path if issue.line is None else f"{issue.path}:{issue.line}"
                print(f"{issue.level.upper()}: {loc}: {issue.message}")
    has_error = any(issue.level == "error" for issue in issues)
    has_warning = any(issue.level == "warning" for issue in issues)
    if has_error:
        return 1
    if strict and has_warning:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
