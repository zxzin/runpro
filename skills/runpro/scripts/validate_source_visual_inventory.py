#!/usr/bin/env python3
"""
Validate source-visual-inventory.md for source-backed presentation work.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ENTRY_RE = re.compile(r"^##\s+(?:Visual Candidate|Candidate Visual|Source Visual)\b", re.I)
FIELD_RE = re.compile(r"^###\s+(.+?)\s*$")

FIELD_NAMES = {
    "source or search path": "source",
    "source/search path": "source",
    "source": "source",
    "visual type": "visual_type",
    "url or file path": "url",
    "url/file path": "url",
    "evidence role": "role",
    "slide role": "role",
    "status": "status",
    "inclusion or exclusion reason": "reason",
    "inclusion/exclusion reason": "reason",
    "selection rationale": "reason",
    "rejection rationale": "reason",
    "provenance notes": "provenance",
    "provenance": "provenance",
}

PLACEHOLDER_WORDS = {
    "",
    "pending",
    "todo",
    "tbd",
    "unknown",
    "n/a",
    "na",
}

SELECTED_STATUSES = {
    "selected",
    "used",
    "included",
    "kept",
    "use",
    "include",
    "selected for deck",
    "used in deck",
    "used as diagram",
    "used as source structure",
}

REJECTED_STATUSES = {
    "rejected",
    "excluded",
    "not used",
    "not selected",
    "omitted",
}


def normalize(value: str) -> str:
    return " ".join(value.lower().replace("_", " ").replace("-", " ").split()).strip(" .;:,")


def meaningful(value: str) -> bool:
    return normalize(value) not in PLACEHOLDER_WORDS


def parse_entries(text: str) -> tuple[list[dict[str, str]], str]:
    entries: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    current_field: str | None = None
    zero_rationale: list[str] = []
    in_zero_rationale = False

    for raw in text.splitlines():
        stripped = raw.strip()

        if stripped.lower().startswith("## zero-image rationale") or stripped.lower().startswith("## zero image rationale"):
            if current:
                entries.append(current)
                current = None
            current_field = None
            in_zero_rationale = True
            continue

        if ENTRY_RE.match(stripped):
            if current:
                entries.append(current)
            current = {
                "source": "",
                "visual_type": "",
                "url": "",
                "role": "",
                "status": "",
                "reason": "",
                "provenance": "",
            }
            current_field = None
            in_zero_rationale = False
            continue

        field_match = FIELD_RE.match(stripped)
        if field_match:
            key = normalize(field_match.group(1))
            current_field = FIELD_NAMES.get(key)
            in_zero_rationale = False
            continue

        if stripped.startswith("## "):
            if current:
                entries.append(current)
                current = None
            current_field = None
            in_zero_rationale = False
            continue

        if current is not None and current_field and stripped:
            current[current_field] = (current[current_field] + " " + stripped).strip()
        elif in_zero_rationale and stripped:
            zero_rationale.append(stripped)

    if current:
        entries.append(current)

    return entries, " ".join(zero_rationale)


def usable_entries(entries: list[dict[str, str]]) -> list[dict[str, str]]:
    usable: list[dict[str, str]] = []
    for entry in entries:
        if meaningful(entry["source"]) and meaningful(entry["visual_type"]) and meaningful(entry["role"]):
            usable.append(entry)
    return usable


def status_bucket(status: str) -> str:
    normalized = normalize(status)
    if normalized in SELECTED_STATUSES:
        return "selected"
    if normalized in REJECTED_STATUSES:
        return "rejected"
    return ""


def entry_has_traceability(entry: dict[str, str]) -> bool:
    url = entry.get("url", "")
    provenance = entry.get("provenance", "")
    return meaningful(url) or meaningful(provenance)


def zero_rationale_is_sufficient(value: str) -> bool:
    normalized = normalize(value)
    if len(normalized.split()) < 25:
        return False
    return all(
        marker in normalized
        for marker in ("searched", "candidate", "rejected")
    ) and any(marker in normalized for marker in ("substitute", "diagram", "matrix", "source structure"))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_visual_inventory", help="Path to source-visual-inventory.md")
    parser.add_argument("--min-candidates", type=int, default=2)
    parser.add_argument(
        "--allow-zero-selected-with-rationale",
        action="store_true",
        help="Allow no selected visuals only when a strong zero-image rationale is present.",
    )
    args = parser.parse_args()

    path = Path(args.source_visual_inventory).expanduser().resolve()
    if not path.exists():
        raise SystemExit(f"Source visual inventory not found: {path}")

    entries, zero_rationale = parse_entries(path.read_text(encoding="utf-8"))
    usable = usable_entries(entries)

    if len(usable) < args.min_candidates:
        raise SystemExit(
            f"Insufficient visual candidates: found {len(usable)}, need at least {args.min_candidates}. "
            "Record real source-native, contextual, generated, diagram, or source-structure candidates before drafting slides."
        )

    selected = [entry for entry in usable if status_bucket(entry["status"]) == "selected"]
    rejected = [entry for entry in usable if status_bucket(entry["status"]) == "rejected"]
    undecided = [entry for entry in usable if not status_bucket(entry["status"])]

    if undecided:
        raise SystemExit(
            "Visual candidates have unclear Status. Use selected/used/included or rejected/excluded/not used."
        )

    missing_reason = [entry for entry in usable if not meaningful(entry["reason"])]
    if missing_reason:
        raise SystemExit(
            "Every visual candidate needs an inclusion or exclusion reason."
        )

    missing_traceability = [entry for entry in usable if not entry_has_traceability(entry)]
    if missing_traceability:
        raise SystemExit(
            "Every visual candidate needs a URL/file path or provenance notes."
        )

    if not selected:
        if not args.allow_zero_selected_with_rationale:
            raise SystemExit(
                "No selected visual candidate found. Select at least one source-native, traceable, generated, "
                "diagrammatic, or source-structure visual, or rerun with a documented zero-image rationale."
            )
        if not zero_rationale_is_sufficient(zero_rationale):
            raise SystemExit(
                "No selected visual candidate found and zero-image rationale is too weak. "
                "It must state that candidates were searched, identify rejected candidate types, "
                "and name the substitute visual system such as a diagram, matrix, or source structure."
            )

    print(
        "Source visual inventory OK: "
        f"{len(usable)} candidates | selected={len(selected)} rejected={len(rejected)}"
    )


if __name__ == "__main__":
    main()
