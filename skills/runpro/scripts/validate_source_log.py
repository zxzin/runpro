#!/usr/bin/env python3
"""
Validate that source-log.md contains enough real source entries for source-backed work.
"""

from __future__ import annotations

import argparse
from datetime import datetime
import re
from pathlib import Path

FIELD_HEADERS = {
    "## Source": "source",
    "## Year": "year",
    "## URL Or File Path": "url",
}


YEAR_RE = re.compile(r"\b(19|20)\d{2}\b")


def parse_entries(text: str) -> list[dict[str, str]]:
    lines = text.splitlines()
    entries: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    current_field: str | None = None

    for raw in lines:
        line = raw.rstrip()
        stripped = line.strip()

        if stripped == "## Source":
            if current:
                entries.append(current)
            current = {"source": "", "year": "", "url": ""}
            current_field = "source"
            continue

        if stripped == "## Year":
            if current is None:
                current = {"source": "", "year": "", "url": ""}
            current_field = "year"
            continue

        if stripped == "## URL Or File Path":
            if current is None:
                current = {"source": "", "year": "", "url": ""}
            current_field = "url"
            continue

        if stripped.startswith("## "):
            current_field = None
            continue

        if current is not None and current_field and stripped:
            if current[current_field]:
                current[current_field] += " " + stripped
            else:
                current[current_field] = stripped

    if current:
        entries.append(current)

    return entries


def usable_source_count(entries: list[dict[str, str]]) -> int:
    return sum(1 for entry in entries if entry["source"] and entry["url"])


def extract_year(value: str) -> int | None:
    match = YEAR_RE.search(value)
    if not match:
        return None
    year = int(match.group(0))
    if 1900 <= year <= 2100:
        return year
    return None


def recent_source_summary(
    entries: list[dict[str, str]],
    current_year: int,
    preferred_recent_years: int,
) -> tuple[int, int]:
    dated_years = [extract_year(entry.get("year", "")) for entry in entries]
    usable_years = [year for year in dated_years if year is not None]
    if not usable_years:
        return 0, 0

    recent_cutoff = current_year - preferred_recent_years
    recent_count = sum(1 for year in usable_years if year >= recent_cutoff)
    return len(usable_years), recent_count


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_log", help="Path to source-log.md")
    parser.add_argument("--min-sources", type=int, default=3, help="Minimum required source entries")
    parser.add_argument(
        "--preferred-recent-years",
        type=int,
        default=0,
        help="Treat sources within this many years of the current year as recent; set to 0 to disable recency checks",
    )
    parser.add_argument(
        "--min-recent-ratio",
        type=float,
        default=0.0,
        help="Minimum fraction of dated sources that should count as recent when recency checks are enabled",
    )
    parser.add_argument(
        "--current-year",
        type=int,
        default=datetime.now().year,
        help="Current year used for recency checks",
    )
    args = parser.parse_args()

    path = Path(args.source_log).expanduser().resolve()
    if not path.exists():
        raise SystemExit(f"Source log not found: {path}")

    text = path.read_text(encoding="utf-8")
    entries = parse_entries(text)
    usable_sources = usable_source_count(entries)

    if usable_sources < args.min_sources:
        raise SystemExit(
            f"Insufficient verified sources: found {usable_sources}, need at least {args.min_sources}"
        )

    message = f"Verified sources OK: {usable_sources}"

    if args.preferred_recent_years > 0 and args.min_recent_ratio > 0:
        dated_count, recent_count = recent_source_summary(
            entries,
            current_year=args.current_year,
            preferred_recent_years=args.preferred_recent_years,
        )
        if dated_count == 0:
            raise SystemExit(
                "Recency check failed: no parseable source years found in source-log.md"
            )

        recent_ratio = recent_count / dated_count
        if recent_ratio < args.min_recent_ratio:
            raise SystemExit(
                "Insufficient recent sources: "
                f"{recent_count}/{dated_count} dated sources are within the last "
                f"{args.preferred_recent_years} years; need at least "
                f"{args.min_recent_ratio:.0%}"
            )

        message += (
            f" | recent sources OK: {recent_count}/{dated_count} within last "
            f"{args.preferred_recent_years} years"
        )

    print(message)


if __name__ == "__main__":
    main()
