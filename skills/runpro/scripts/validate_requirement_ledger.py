#!/usr/bin/env python3
"""
Validate that requirement-ledger.md tracks explicit requirements cleanly.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


BLOCK_RE = re.compile(r"^##\s+Requirement\s+(.+?)\s*$")
FIELD_RE = re.compile(r"^###\s+(.+?)\s*$")

FIELD_NAMES = {
    "Source": "source",
    "Type": "type",
    "Requirement": "requirement",
    "Status": "status",
    "Satisfaction Evidence": "evidence",
    "Notes": "notes",
}

FINAL_ALLOWED_STATUSES = {
    "satisfied",
    "blocked",
    "not applicable",
    "not-applicable",
    "not_applicable",
}

PLACEHOLDER_WORDS = {
    "pending",
    "todo",
    "tbd",
    "unknown",
    "unresolved",
}


def parse_blocks(text: str) -> list[dict[str, str]]:
    blocks: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    current_field: str | None = None

    for raw in text.splitlines():
        stripped = raw.strip()

        block_match = BLOCK_RE.match(stripped)
        if block_match:
            if current is not None:
                blocks.append(current)
            current = {
                "id": block_match.group(1).strip(),
                "source": "",
                "type": "",
                "requirement": "",
                "status": "",
                "evidence": "",
                "notes": "",
            }
            current_field = None
            continue

        field_match = FIELD_RE.match(stripped)
        if field_match and current is not None:
            current_field = FIELD_NAMES.get(field_match.group(1).strip())
            continue

        if stripped.startswith("## "):
            current_field = None
            continue

        if current is not None and current_field and stripped:
            if current[current_field]:
                current[current_field] += " " + stripped
            else:
                current[current_field] = stripped

    if current is not None:
        blocks.append(current)

    return blocks


def is_meaningful(value: str) -> bool:
    normalized = " ".join(value.split()).strip().lower()
    return bool(normalized) and normalized not in PLACEHOLDER_WORDS


def normalize_status(value: str) -> str:
    return " ".join(value.lower().replace("_", " ").split())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("requirement_ledger", help="Path to requirement-ledger.md")
    parser.add_argument(
        "--final",
        action="store_true",
        help="Require end-state statuses suitable for handoff",
    )
    args = parser.parse_args()

    path = Path(args.requirement_ledger).expanduser().resolve()
    if not path.exists():
        raise SystemExit(f"Requirement ledger not found: {path}")

    blocks = parse_blocks(path.read_text(encoding="utf-8"))
    if not blocks:
        raise SystemExit("Requirement ledger is empty. No requirement blocks were found.")

    problems: list[str] = []
    satisfied = 0
    blocked = 0
    not_applicable = 0

    for block in blocks:
        label = block["id"]
        for field in ("source", "type", "requirement", "status"):
            if not is_meaningful(block[field]):
                problems.append(f"{label}: missing or placeholder {field}")

        status = normalize_status(block["status"])
        if args.final:
            if status not in FINAL_ALLOWED_STATUSES:
                problems.append(
                    f"{label}: invalid final status '{block['status']}'. "
                    "Use satisfied, blocked, or not applicable."
                )
            elif status == "satisfied":
                if not is_meaningful(block["evidence"]):
                    problems.append(f"{label}: satisfied requirement is missing Satisfaction Evidence")
                satisfied += 1
            elif status == "blocked":
                if not is_meaningful(block["notes"]):
                    problems.append(f"{label}: blocked requirement is missing explanatory Notes")
                blocked += 1
            else:
                not_applicable += 1

    if problems:
        raise SystemExit("Requirement ledger validation failed:\n- " + "\n- ".join(problems))

    summary = f"Requirement ledger OK: {len(blocks)} items"
    if args.final:
        summary += (
            f" | satisfied={satisfied} blocked={blocked} not_applicable={not_applicable}"
        )
    print(summary)


if __name__ == "__main__":
    main()
