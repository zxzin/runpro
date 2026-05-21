#!/usr/bin/env python3
"""
Validate that final-audit.md is strict enough for handoff.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


SECTION_RE = re.compile(r"^##\s+(.+?)\s*$")
STATUS_RE = re.compile(r"\[([^\]]+)\]")
RANGE_RE = re.compile(r"(?<!\d)(\d{2,3})\s*(?:-|–|—|to)\s*(\d{2,3})(?!\d)")
NUMBER_RE = re.compile(r"(?<!\d)(\d{2,3})(?!\d)")

REQUIRED_SECTIONS = [
    "Audit Scope",
    "Target Threshold",
    "Estimated Score Band",
    "Strict-Mode Validation Chain",
    "Final Format Check",
    "Requirement-By-Requirement Verdicts",
    "Completion Decision",
]

READY_DECISIONS = {"ready to submit", "ready for review"}
NONBLOCKING_STATUSES = {"pass", "passed", "not applicable", "not-applicable", "not_applicable"}
FAIL_WORDS = {
    "fail",
    "failed",
    "incomplete",
    "pending",
    "todo",
    "to be fixed",
    "unresolved",
    "blocked",
    "blocker",
}
NEGATED_FAILURE_PHRASES = (
    "no fail",
    "no failed",
    "no incomplete",
    "no pending",
    "no todo",
    "no unresolved",
    "no blocked",
    "no blocker",
    "not blocked",
    "not applicable",
)
BLANKISH_VALUES = {
    "",
    "none",
    "n/a",
    "na",
    "no blocking issues",
    "no incomplete items",
    "no remediation required",
    "no required remediation actions",
}

ACADEMIC_QUALITY_MARKER_GROUPS = {
    "prompt/rubric alignment": ("prompt", "rubric", "assignment question", "required sub-part"),
    "section analytical purpose": ("section", "analytical purpose", "section-level", "major section"),
    "evidence quality": ("evidence quality", "source quality", "authoritative", "peer-reviewed"),
    "comparative synthesis": ("synthesis", "comparative", "comparison", "literature pattern"),
    "limitations or counterarguments": ("limitation", "counterargument", "trade-off", "uncertainty"),
    "visual or table integration": ("visual", "table", "figure", "diagram"),
    "citation-to-outcome specificity": ("citation-to-outcome", "citation to outcome", "measured outcome", "specific outcome", "endpoint"),
    "empirical precision": ("empirical", "numeric", "magnitude", "unit", "baseline"),
    "theory or framework application": ("theory", "framework", "course concept", "method"),
    "conclusion discipline": ("conclusion", "final judgement", "final judgment", "judgement-led", "judgment-led"),
    "citation support integrity": ("citation support", "source support", "claim support", "mismatched citation"),
}

MIN_ACADEMIC_MARKER_GROUPS = 8

RUBRIC_AUDIT_MARKER_GROUPS = {
    "criteria": ("criterion", "criteria", "rubric item", "required question", "teacher feedback"),
    "status": ("pass", "partial", "fail", "not assessable", "not-assessable"),
    "location": ("draft location", "section", "paragraph", "page", "table", "figure"),
    "weight or importance": ("weight", "importance", "high-weight", "central"),
    "evidence": ("evidence", "visible answer", "direct answer", "mapped"),
    "repair": ("repair", "revision", "fix", "remediation"),
}

MIN_RUBRIC_AUDIT_MARKER_GROUPS = 5

ACADEMIC_STANDARDS_MARKER_GROUPS = {
    "citation style": ("citation style", "apa", "harvard", "mla", "chicago", "vancouver", "numbered"),
    "in-text/reference matching": ("in-text", "reference list", "references", "citation parity", "cited/reference"),
    "reference metadata": ("author", "year", "title", "doi", "url", "metadata"),
    "formatting/layout": ("format", "font", "spacing", "margin", "heading", "word count", "page"),
    "figures/tables": ("figure", "table", "caption", "chart", "appendix"),
    "visual balance": ("visual balance", "balanced", "whitespace", "legend", "readable labels", "label readability", "chart quality"),
    "paragraph logic": ("claim", "evidence", "analysis", "implication", "paragraph"),
    "academic register": ("academic register", "formal", "precise", "grammar", "language"),
}

MIN_ACADEMIC_STANDARDS_MARKER_GROUPS = 5
REQUIRED_ACADEMIC_STANDARDS_MARKER_GROUPS = ("visual balance",)

SOURCE_CLAIM_MARKER_GROUPS = {
    "major claims": ("claim", "major claim", "factual", "empirical", "evaluative", "comparative"),
    "source support": ("source support", "supports", "supported", "cited source"),
    "specific outcome": ("measured outcome", "specific outcome", "endpoint", "defined outcome"),
    "empirical detail": ("direction", "magnitude", "unit", "sample", "method", "population", "condition", "baseline"),
    "evidence boundary": ("evidence boundary", "commercial", "marketing", "screenshot", "label"),
    "unsupported or repaired": ("unsupported", "needs source", "needs narrowing", "repaired", "removed"),
}

MIN_SOURCE_CLAIM_MARKER_GROUPS = 4

PRESENTATION_AUDIT_MARKER_GROUPS = {
    "source log consistency": ("source-log", "source log", "verified source", "source audit"),
    "references/source separation": ("references", "sources used", "source slide", "reference slide"),
    "source visual specificity": ("source object", "source visual", "book cover", "report cover", "source screenshot", "original figure"),
    "visual enrichment": ("visual enrichment", "image", "illustration", "diagram", "map", "visual anchor"),
    "generated image handling": ("generated image", "generated illustration", "built-in image", "image tool", "generated-asset"),
    "human-facing deck language": ("human-facing", "audience-facing", "source log", "workflow language", "internal workflow"),
    "original data figures": ("original data", "data figure", "source figure", "chart", "axis", "legend"),
    "rounded corner consistency": ("rounded", "corner", "cards", "panels", "callouts"),
    "rendered preview inspection": ("render", "preview", "visual inspection", "pptpro_audit", "strict audit"),
}

MIN_PRESENTATION_AUDIT_MARKER_GROUPS = 6


def parse_sections(text: str) -> dict[str, str]:
    sections: dict[str, str] = {}
    current: str | None = None
    buffer: list[str] = []

    for raw in text.splitlines():
        match = SECTION_RE.match(raw.strip())
        if match:
            if current is not None:
                sections[current] = "\n".join(buffer).strip()
            current = match.group(1).strip()
            buffer = []
            continue
        if current is not None:
            buffer.append(raw.rstrip())

    if current is not None:
        sections[current] = "\n".join(buffer).strip()

    return sections


def is_blankish(value: str) -> bool:
    normalized = normalize(value)
    return normalized in BLANKISH_VALUES


def normalize(value: str) -> str:
    normalized = " ".join(value.lower().replace("_", " ").split())
    return normalized.strip(" .;:,")


def has_failure_signal(value: str) -> bool:
    normalized = normalize(value)
    scrubbed = normalized
    for phrase in NEGATED_FAILURE_PHRASES:
        scrubbed = scrubbed.replace(phrase, "")
    return any(re.search(rf"\b{re.escape(word)}\b", scrubbed) for word in FAIL_WORDS)


def has_not_assessable_signal(value: str) -> bool:
    normalized = normalize(value)
    scrubbed = normalized
    for phrase in (
        "no not assessable",
        "no not-assessable",
        "zero not assessable",
        "zero not-assessable",
        "0 not assessable",
        "0 not-assessable",
        "not applicable",
    ):
        scrubbed = scrubbed.replace(phrase, "")
    return "not assessable" in scrubbed or "not-assessable" in scrubbed


def has_partial_signal(value: str) -> bool:
    normalized = normalize(value)
    scrubbed = normalized
    for phrase in ("no partial", "zero partial", "0 partial"):
        scrubbed = scrubbed.replace(phrase, "")
    return re.search(r"\bpartial\b", scrubbed) is not None


def extract_statuses(verdict_text: str) -> list[str]:
    statuses = [normalize(match.group(1)) for match in STATUS_RE.finditer(verdict_text)]
    if statuses:
        return statuses

    fallback_statuses: list[str] = []
    for raw_line in verdict_text.splitlines():
        line = raw_line.strip().lower()
        if not line.startswith("-"):
            continue
        for token in ("pass", "failed", "fail", "incomplete", "blocked", "not applicable", "pending"):
            if token in line:
                fallback_statuses.append(normalize(token))
                break
    return fallback_statuses


def extract_score_ranges(text: str) -> list[tuple[int, int]]:
    return [(int(start), int(end)) for start, end in RANGE_RE.findall(text)]


def extract_score_numbers(text: str) -> list[int]:
    return [int(value) for value in NUMBER_RE.findall(text)]


def target_requires_90_plus(target_threshold: str) -> bool:
    normalized = normalize(target_threshold)
    if any(
        marker in normalized
        for marker in (
            "90+",
            "90 +",
            "90 plus",
            ">=90",
            "90 or above",
            "high achievement",
            "high-achievement",
        )
    ):
        return True
    return False


def estimated_band_supports_90_plus(score_band_text: str) -> bool:
    normalized = normalize(score_band_text)
    if not normalized:
        return False

    if any(
        marker in normalized
        for marker in ("below 90", "under 90", "less than 90", "sub-90", "not yet 90")
    ):
        return False

    ranges = extract_score_ranges(score_band_text)
    if ranges:
        if min(min(start, end) for start, end in ranges) < 90:
            return False

    numbers = extract_score_numbers(score_band_text)
    if numbers:
        if min(numbers) < 90:
            return False
        if max(numbers) >= 90:
            return True

    if any(
        marker in normalized
        for marker in ("90+ plausible", "90 + plausible", "90 plus plausible", "plausibly in the 90")
    ):
        return True

    return False


def missing_academic_quality_markers(text: str) -> list[str]:
    normalized = normalize(text)
    missing: list[str] = []
    for label, markers in ACADEMIC_QUALITY_MARKER_GROUPS.items():
        if not any(marker in normalized for marker in markers):
            missing.append(label)
    return missing


def missing_marker_groups(text: str, marker_groups: dict[str, tuple[str, ...]]) -> list[str]:
    normalized = normalize(text)
    missing: list[str] = []
    for label, markers in marker_groups.items():
        if not any(marker in normalized for marker in markers):
            missing.append(label)
    return missing


def enforce_marker_coverage(
    section_name: str,
    section_text: str,
    marker_groups: dict[str, tuple[str, ...]],
    minimum_groups: int,
) -> None:
    missing_markers = missing_marker_groups(section_text, marker_groups)
    marker_count = len(marker_groups) - len(missing_markers)
    if marker_count < minimum_groups:
        raise SystemExit(
            f"{section_name} is too thin for strict validation. "
            f"Covered {marker_count}/{len(marker_groups)} required marker groups; "
            "missing: " + ", ".join(missing_markers)
        )


def enforce_named_marker_groups(
    section_name: str,
    section_text: str,
    marker_groups: dict[str, tuple[str, ...]],
    required_groups: tuple[str, ...],
) -> None:
    missing_markers = missing_marker_groups(
        section_text,
        {label: marker_groups[label] for label in required_groups if label in marker_groups},
    )
    if missing_markers:
        raise SystemExit(
            f"{section_name} is missing mandatory strict-validation coverage: "
            + ", ".join(missing_markers)
        )


def missing_presentation_audit_markers(text: str) -> list[str]:
    normalized = normalize(text)
    missing: list[str] = []
    for label, markers in PRESENTATION_AUDIT_MARKER_GROUPS.items():
        if not any(marker in normalized for marker in markers):
            missing.append(label)
    return missing


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("final_audit", help="Path to final-audit.md")
    parser.add_argument(
        "--require-90-plus",
        action="store_true",
        help="Require the estimated score band to explicitly indicate a 90+ target is plausible",
    )
    parser.add_argument(
        "--require-citation-micro-audit",
        action="store_true",
        help=(
            "Require a non-blank 'Citation Micro-Audit' section and fail if it still indicates "
            "pending or failed citation-level cleanup."
        ),
    )
    parser.add_argument(
        "--require-academic-quality-audit",
        action="store_true",
        help=(
            "Require a non-blank 'Academic Quality Audit' section and fail if it still indicates "
            "pending, failed, incomplete, or unresolved academic-quality remediation."
        ),
    )
    parser.add_argument(
        "--require-rubric-compliance-audit",
        action="store_true",
        help=(
            "Require a non-blank 'Rubric Compliance Audit' section with criterion-level "
            "rubric evidence."
        ),
    )
    parser.add_argument(
        "--require-academic-standards-audit",
        action="store_true",
        help=(
            "Require a non-blank 'Academic Standards Audit' section covering academic "
            "format, citation, figure/table visual quality, visual balance, and register checks."
        ),
    )
    parser.add_argument(
        "--require-source-claim-audit",
        action="store_true",
        help=(
            "Require a non-blank 'Source-Claim Integrity Audit' section covering major "
            "claim-to-source support checks."
        ),
    )
    parser.add_argument(
        "--require-presentation-source-audit",
        action="store_true",
        help=(
            "Require a non-blank 'Presentation Source Audit' section and fail if it still "
            "indicates pending, failed, or unresolved presentation source/PPTPRO-quality cleanup."
        ),
    )
    args = parser.parse_args()

    path = Path(args.final_audit).expanduser().resolve()
    if not path.exists():
        raise SystemExit(f"Final audit not found: {path}")

    sections = parse_sections(path.read_text(encoding="utf-8"))
    missing = [name for name in REQUIRED_SECTIONS if is_blankish(sections.get(name, ""))]
    if missing:
        raise SystemExit(
            "Final audit is incomplete. Missing required sections: " + ", ".join(missing)
        )

    if args.require_citation_micro_audit and is_blankish(
        sections.get("Citation Micro-Audit", "")
    ):
        raise SystemExit(
            "Final audit is incomplete. Missing required section: Citation Micro-Audit"
        )
    if args.require_academic_quality_audit and is_blankish(
        sections.get("Academic Quality Audit", "")
    ):
        raise SystemExit(
            "Final audit is incomplete. Missing required section: Academic Quality Audit"
        )
    if args.require_rubric_compliance_audit and is_blankish(
        sections.get("Rubric Compliance Audit", "")
    ):
        raise SystemExit(
            "Final audit is incomplete. Missing required section: Rubric Compliance Audit"
        )
    if args.require_academic_standards_audit and is_blankish(
        sections.get("Academic Standards Audit", "")
    ):
        raise SystemExit(
            "Final audit is incomplete. Missing required section: Academic Standards Audit"
        )
    if args.require_source_claim_audit and is_blankish(
        sections.get("Source-Claim Integrity Audit", "")
    ):
        raise SystemExit(
            "Final audit is incomplete. Missing required section: Source-Claim Integrity Audit"
        )
    if args.require_presentation_source_audit and is_blankish(
        sections.get("Presentation Source Audit", "")
    ):
        raise SystemExit(
            "Final audit is incomplete. Missing required section: Presentation Source Audit"
        )

    decision = normalize(sections["Completion Decision"])
    if decision not in READY_DECISIONS and decision != "blocked":
        raise SystemExit(
            "Completion Decision must be Ready to submit, Ready for review, or Blocked."
        )

    statuses = extract_statuses(sections["Requirement-By-Requirement Verdicts"])
    if not statuses:
        raise SystemExit(
            "Final audit has no parseable requirement verdict statuses. "
            "Use lines such as '- [pass] R1 ...'."
        )

    if decision in READY_DECISIONS:
        bad_statuses = [status for status in statuses if status not in NONBLOCKING_STATUSES]
        if bad_statuses:
            raise SystemExit(
                "Final audit cannot be ready while requirement verdicts still contain: "
                + ", ".join(sorted(set(bad_statuses)))
            )

        incomplete_text = normalize(sections.get("Incomplete Or Failed Items", ""))
        if incomplete_text and incomplete_text not in BLANKISH_VALUES:
            if has_failure_signal(incomplete_text):
                raise SystemExit(
                    "Final audit cannot be ready while Incomplete Or Failed Items still lists failures."
                )

        remediation_actions = normalize(sections.get("Required Remediation Actions", ""))
        if remediation_actions and remediation_actions not in BLANKISH_VALUES:
            raise SystemExit(
                "Final audit cannot be ready while Required Remediation Actions still lists pending work."
            )

        format_check = normalize(sections["Final Format Check"])
        if has_failure_signal(format_check):
            raise SystemExit(
                "Final audit cannot be ready while Final Format Check still indicates failure or pending work."
            )

        strict_mode_chain = normalize(sections["Strict-Mode Validation Chain"])
        if has_failure_signal(strict_mode_chain):
            raise SystemExit(
                "Final audit cannot be ready while Strict-Mode Validation Chain still indicates failure or pending work."
            )

        if args.require_citation_micro_audit:
            citation_micro_audit = normalize(sections.get("Citation Micro-Audit", ""))
            if has_failure_signal(citation_micro_audit):
                raise SystemExit(
                    "Final audit cannot be ready while Citation Micro-Audit still indicates failure or pending work."
                )

        if args.require_academic_quality_audit:
            academic_quality_audit = normalize(sections.get("Academic Quality Audit", ""))
            if has_failure_signal(academic_quality_audit):
                raise SystemExit(
                    "Final audit cannot be ready while Academic Quality Audit still indicates failure or pending work."
                )
            missing_markers = missing_academic_quality_markers(academic_quality_audit)
            marker_count = len(ACADEMIC_QUALITY_MARKER_GROUPS) - len(missing_markers)
            if marker_count < MIN_ACADEMIC_MARKER_GROUPS:
                raise SystemExit(
                    "Academic Quality Audit is too thin for strict high-achievement validation. "
                    f"Covered {marker_count}/{len(ACADEMIC_QUALITY_MARKER_GROUPS)} required marker groups; "
                    "missing: " + ", ".join(missing_markers)
                )

        if args.require_rubric_compliance_audit:
            rubric_compliance_audit = normalize(sections.get("Rubric Compliance Audit", ""))
            if (
                has_failure_signal(rubric_compliance_audit)
                or has_not_assessable_signal(rubric_compliance_audit)
                or has_partial_signal(rubric_compliance_audit)
            ):
                raise SystemExit(
                    "Final audit cannot be ready while Rubric Compliance Audit still indicates failed, partial, or not-assessable rubric coverage."
                )
            enforce_marker_coverage(
                "Rubric Compliance Audit",
                rubric_compliance_audit,
                RUBRIC_AUDIT_MARKER_GROUPS,
                MIN_RUBRIC_AUDIT_MARKER_GROUPS,
            )

        if args.require_academic_standards_audit:
            academic_standards_audit = normalize(sections.get("Academic Standards Audit", ""))
            if has_failure_signal(academic_standards_audit) or has_not_assessable_signal(academic_standards_audit):
                raise SystemExit(
                    "Final audit cannot be ready while Academic Standards Audit still indicates failed or not-assessable academic-standard checks."
                )
            enforce_marker_coverage(
                "Academic Standards Audit",
                academic_standards_audit,
                ACADEMIC_STANDARDS_MARKER_GROUPS,
                MIN_ACADEMIC_STANDARDS_MARKER_GROUPS,
            )
            enforce_named_marker_groups(
                "Academic Standards Audit",
                academic_standards_audit,
                ACADEMIC_STANDARDS_MARKER_GROUPS,
                REQUIRED_ACADEMIC_STANDARDS_MARKER_GROUPS,
            )

        if args.require_source_claim_audit:
            source_claim_audit = normalize(sections.get("Source-Claim Integrity Audit", ""))
            if has_failure_signal(source_claim_audit) or has_not_assessable_signal(source_claim_audit):
                raise SystemExit(
                    "Final audit cannot be ready while Source-Claim Integrity Audit still indicates failed, unsupported, or not-assessable claim support."
                )
            enforce_marker_coverage(
                "Source-Claim Integrity Audit",
                source_claim_audit,
                SOURCE_CLAIM_MARKER_GROUPS,
                MIN_SOURCE_CLAIM_MARKER_GROUPS,
            )

        if args.require_presentation_source_audit:
            presentation_source_audit = normalize(
                sections.get("Presentation Source Audit", "")
            )
            if has_failure_signal(presentation_source_audit):
                raise SystemExit(
                    "Final audit cannot be ready while Presentation Source Audit still indicates failure or pending work."
                )
            missing_markers = missing_presentation_audit_markers(presentation_source_audit)
            marker_count = len(PRESENTATION_AUDIT_MARKER_GROUPS) - len(missing_markers)
            if marker_count < MIN_PRESENTATION_AUDIT_MARKER_GROUPS:
                raise SystemExit(
                    "Presentation Source Audit is too thin for PPTPRO-level validation. "
                    f"Covered {marker_count}/{len(PRESENTATION_AUDIT_MARKER_GROUPS)} marker groups; "
                    "missing: " + ", ".join(missing_markers)
                )

        blocking_issues = normalize(sections.get("Blocking Issues", ""))
        if blocking_issues and blocking_issues not in BLANKISH_VALUES:
            raise SystemExit(
                "Final audit cannot be ready while Blocking Issues still contains active blockers."
            )

        require_90_plus = args.require_90_plus or target_requires_90_plus(
            sections["Target Threshold"]
        )
        if require_90_plus and not estimated_band_supports_90_plus(
            sections["Estimated Score Band"]
        ):
            raise SystemExit(
                "Final audit does not support a conservative 90+ plausible score band."
            )

    if decision == "blocked" and is_blankish(sections.get("Blocking Issues", "")):
        raise SystemExit(
            "Blocked final audit must explain the blocking issues explicitly."
        )

    print(f"Final audit OK: {sections['Completion Decision'].strip()}")


if __name__ == "__main__":
    main()
