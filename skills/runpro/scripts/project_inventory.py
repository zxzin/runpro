#!/usr/bin/env python3
"""
Create a lightweight inventory of a project folder so the skill can identify
likely requirement sources, working files, and final outputs before execution.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path


IGNORE_DIRS = {
    ".git",
    ".idea",
    ".vscode",
    ".venv",
    "venv",
    "__pycache__",
    "node_modules",
    "dist",
    "build",
    ".next",
    ".turbo",
}

DEFAULT_GENERATED_WORKSPACE = "runpro_workspace"

CATEGORY_EXTENSIONS = {
    "text": {
        ".md",
        ".txt",
        ".json",
        ".yaml",
        ".yml",
        ".csv",
        ".tsv",
        ".html",
        ".css",
        ".js",
        ".jsx",
        ".ts",
        ".tsx",
        ".py",
        ".java",
        ".swift",
        ".kt",
        ".xml",
        ".sh",
    },
    "document": {".pdf", ".doc", ".docx", ".ppt", ".pptx", ".xls", ".xlsx", ".rtf"},
    "image": {".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp", ".tif", ".tiff", ".svg"},
    "audio": {".mp3", ".wav", ".m4a", ".aac", ".flac"},
    "video": {".mp4", ".mov", ".avi", ".mkv", ".webm"},
    "archive": {".zip", ".rar", ".7z", ".tar", ".gz"},
}

KEYWORD_GROUPS = {
    "requirements": ["requirement", "brief", "scope", "需求", "要求", "说明"],
    "communication": ["chat", "conversation", "meeting", "notes", "feedback", "沟通", "会议", "记录"],
    "delivery": ["final", "deliverable", "submit", "report", "proposal", "总结", "交付", "提交"],
    "reference": ["reference", "sample", "example", "mockup", "截图", "参考", "样例"],
}


def categorize_file(path: Path) -> str:
    suffix = path.suffix.lower()
    for category, extensions in CATEGORY_EXTENSIONS.items():
        if suffix in extensions:
            return category
    return "other"


def keyword_hits(path: Path) -> list[str]:
    name = path.name.lower()
    hits: list[str] = []
    for label, keywords in KEYWORD_GROUPS.items():
        if any(keyword in name for keyword in keywords):
            hits.append(label)
    return hits


def iter_files(root: Path, extra_ignore_dirs: set[str] | None = None):
    effective_ignore_dirs = set(IGNORE_DIRS)
    effective_ignore_dirs.add(DEFAULT_GENERATED_WORKSPACE)
    if extra_ignore_dirs:
        effective_ignore_dirs.update(extra_ignore_dirs)

    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in effective_ignore_dirs for part in path.parts):
            continue
        yield path


def build_inventory(root: Path, extra_ignore_dirs: set[str] | None = None) -> dict:
    files = []
    category_counts = defaultdict(int)
    keyword_candidates = []

    for path in iter_files(root, extra_ignore_dirs=extra_ignore_dirs):
        rel = path.relative_to(root)
        category = categorize_file(path)
        category_counts[category] += 1
        hits = keyword_hits(path)
        record = {
            "path": str(rel),
            "category": category,
            "size_bytes": path.stat().st_size,
            "keyword_hits": hits,
        }
        files.append(record)
        if hits:
            keyword_candidates.append(record)

    keyword_candidates.sort(key=lambda item: (-len(item["keyword_hits"]), item["path"]))

    return {
        "root": str(root),
        "total_files": len(files),
        "category_counts": dict(sorted(category_counts.items())),
        "priority_candidates": keyword_candidates[:30],
        "files": sorted(files, key=lambda item: item["path"]),
    }


def inventory_to_markdown(inventory: dict) -> str:
    lines = []
    lines.append(f"# Project Inventory")
    lines.append("")
    lines.append(f"- Root: `{inventory['root']}`")
    lines.append(f"- Total files: `{inventory['total_files']}`")
    lines.append("")
    lines.append("## Category Counts")
    for category, count in inventory["category_counts"].items():
        lines.append(f"- {category}: `{count}`")
    lines.append("")
    lines.append("## Priority Candidates")
    if inventory["priority_candidates"]:
        for item in inventory["priority_candidates"]:
            hits = ", ".join(item["keyword_hits"])
            lines.append(f"- `{item['path']}` [{item['category']}] keywords: {hits}")
    else:
        lines.append("- None")
    lines.append("")
    lines.append("## File List")
    for item in inventory["files"]:
        lines.append(f"- `{item['path']}` [{item['category']}]")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("project_root", help="Path to the project root")
    parser.add_argument("--format", choices=["json", "markdown"], default="markdown")
    parser.add_argument("--output", help="Optional output file path")
    parser.add_argument(
        "--exclude-dir",
        action="append",
        default=[],
        help="Additional directory name to exclude from the inventory scan",
    )
    args = parser.parse_args()

    root = Path(args.project_root).expanduser().resolve()
    if not root.exists() or not root.is_dir():
        raise SystemExit(f"Project root not found or not a directory: {root}")

    inventory = build_inventory(root, extra_ignore_dirs=set(args.exclude_dir))
    output = json.dumps(inventory, ensure_ascii=False, indent=2)
    if args.format == "markdown":
        output = inventory_to_markdown(inventory)

    if args.output:
        Path(args.output).expanduser().resolve().write_text(output, encoding="utf-8")
    else:
        print(output)


if __name__ == "__main__":
    main()
