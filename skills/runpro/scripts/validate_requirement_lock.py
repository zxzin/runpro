#!/usr/bin/env python3
"""
Validate that approval-gate.md is populated enough to support strict execution.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


SECTION_RE = re.compile(r"^##\s+(.+?)\s*$")

REQUIRED_SECTIONS = [
    "Project Goal",
    "Final Deliverable",
    "Execution Mode",
    "All Required Parts Must Be Completed",
    "Required Structure Or Sections",
    "Required Format Or Template",
    "Non-Negotiable Requirements",
    "Explicitly Forbidden Moves",
    "Locked Execution Direction",
]

PLACEHOLDER_VALUES = {
    "",
    "tbd",
    "todo",
    "unknown",
    "pending",
    "pending user confirmation",
    "to confirm",
}

VALIDATION_PROFILE_KEYS = {
    "strict_mode",
    "target_90_plus",
    "rubric_compliance_audit",
    "academic_standards_audit",
    "source_claim_audit",
    "academic_quality_audit",
    "citation_micro_audit",
    "local_rule_audit",
    "presentation_source_audit",
    "student_facing_residue_audit",
    "source_log_validation",
    "source_visual_inventory_validation",
    "checkpro_required",
    "pptpro_required",
    "source_minimum",
    "preferred_recent_years",
    "min_recent_ratio",
    "visual_minimum_candidates",
    "allow_zero_selected_with_rationale",
    "pptpro_deck",
    "pptpro_script",
    "pptpro_min_pictures",
}

BOOL_PROFILE_KEYS = {
    key
    for key in VALIDATION_PROFILE_KEYS
    if key
    not in {
        "source_minimum",
        "preferred_recent_years",
        "min_recent_ratio",
        "visual_minimum_candidates",
        "pptpro_deck",
        "pptpro_script",
        "pptpro_min_pictures",
    }
}


def parse_validation_profile(value: str) -> dict[str, str]:
    profile: dict[str, str] = {}
    for raw in value.splitlines():
        line = raw.strip().lstrip("-*").strip()
        if ":" not in line:
            continue
        key, raw_value = line.split(":", 1)
        normalized_key = key.strip().lower().replace("-", "_").replace(" ", "_")
        if normalized_key in VALIDATION_PROFILE_KEYS:
            profile[normalized_key] = raw_value.strip()
    return profile


def validate_profile(profile: dict[str, str]) -> None:
    missing = sorted(VALIDATION_PROFILE_KEYS - set(profile))
    if missing:
        raise SystemExit(
            "Requirement lock validation profile is incomplete. Missing keys: "
            + ", ".join(missing)
        )

    invalid_booleans = sorted(
        key
        for key in BOOL_PROFILE_KEYS
        if profile[key].strip().lower() not in {"yes", "no"}
    )
    if invalid_booleans:
        raise SystemExit(
            "Requirement lock validation profile has unresolved yes/no values: "
            + ", ".join(invalid_booleans)
        )

    for key in (
        "source_minimum",
        "preferred_recent_years",
        "visual_minimum_candidates",
        "pptpro_min_pictures",
    ):
        try:
            value = int(profile[key])
        except ValueError as exc:
            raise SystemExit(f"Validation profile value {key} must be an integer.") from exc
        if value < 0:
            raise SystemExit(f"Validation profile value {key} cannot be negative.")

    try:
        recent_ratio = float(profile["min_recent_ratio"])
    except ValueError as exc:
        raise SystemExit("Validation profile value min_recent_ratio must be numeric.") from exc
    if not 0 <= recent_ratio <= 1:
        raise SystemExit("Validation profile min_recent_ratio must be between 0 and 1.")

    for key in ("pptpro_deck", "pptpro_script"):
        if not profile[key].strip():
            raise SystemExit(f"Validation profile value {key} must be a path or 'none'.")


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


def is_meaningful(value: str) -> bool:
    normalized = " ".join(value.split()).strip().lower()
    return normalized not in PLACEHOLDER_VALUES


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("approval_gate", help="Path to approval-gate.md")
    parser.add_argument(
        "--require-approved",
        action="store_true",
        help="Require Approval Status and User Confirmation Record to show confirmed execution scope",
    )
    parser.add_argument(
        "--require-validation-profile",
        action="store_true",
        help="Require a complete explicit validation profile with no pending values",
    )
    args = parser.parse_args()

    path = Path(args.approval_gate).expanduser().resolve()
    if not path.exists():
        raise SystemExit(f"Requirement lock not found: {path}")

    sections = parse_sections(path.read_text(encoding="utf-8"))

    missing = [name for name in REQUIRED_SECTIONS if not is_meaningful(sections.get(name, ""))]
    if missing:
        raise SystemExit(
            "Requirement lock is incomplete. Missing or placeholder sections: "
            + ", ".join(missing)
        )

    execution_mode = " ".join(sections.get("Execution Mode", "").split()).strip().lower()
    if execution_mode not in {"strict mode", "standard mode", "strict", "standard"}:
        raise SystemExit(
            "Requirement lock is incomplete. Execution Mode must explicitly be strict mode or standard mode."
        )

    explicit_formatting = sections.get("Explicit Formatting Requirements", "")
    fallback_formatting = sections.get("Default Formatting Fallback", "")
    if not is_meaningful(explicit_formatting) and not is_meaningful(fallback_formatting):
        raise SystemExit(
            "Requirement lock is incomplete. Need either explicit formatting requirements "
            "or a documented default formatting fallback."
        )

    if args.require_approved:
        approval_status = sections.get("Approval Status", "")
        approval_record = sections.get("User Confirmation Record", "")
        status_lower = " ".join(approval_status.split()).strip().lower()
        if "approved" not in status_lower and "confirmed" not in status_lower:
            raise SystemExit(
                "Requirement lock is not approved. Approval Status must explicitly say approved or confirmed."
            )
        if not is_meaningful(approval_record):
            raise SystemExit(
                "Requirement lock is not approved cleanly. User Confirmation Record is missing."
            )

    if args.require_validation_profile:
        profile_text = sections.get("Validation Profile", "")
        if not is_meaningful(profile_text):
            raise SystemExit(
                "Requirement lock is incomplete. Validation Profile is missing or unresolved."
            )
        validate_profile(parse_validation_profile(profile_text))

    print("Requirement lock OK")


if __name__ == "__main__":
    main()
