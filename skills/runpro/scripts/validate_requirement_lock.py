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

    print("Requirement lock OK")


if __name__ == "__main__":
    main()
