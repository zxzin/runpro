#!/usr/bin/env python3
"""
Infer the most likely project route for runpro.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from project_inventory import build_inventory


ROUTE_LABELS = {
    "adaptive": "Adaptive",
    "document": "Document",
    "presentation": "Presentation",
    "code": "Code",
    "data": "Data",
    "mixed": "Mixed",
}

ROUTE_FIRST_VERSION = {
    "adaptive": "Define the smallest viable handoff for the actual requirement and build a provisional working version.",
    "document": "Create a structured draft with the key required sections and real content.",
    "presentation": "Create a deck skeleton with the key slide sequence and core content scaffolded.",
    "code": "Create a runnable or buildable path proving the core change works.",
    "data": "Create a reproducible core table, sheet flow, or analysis pipeline.",
    "mixed": "Create the primary deliverable skeleton first, then add only the supporting secondary artifacts.",
}

ROUTE_VALIDATIONS = {
    "adaptive": [
        "The provisional route still matches the end-state requirement",
        "The handoff package is practical and reviewable",
        "Custom acceptance checks are explicit",
    ],
    "document": [
        "Requirement coverage",
        "Facts, dates, and names checked",
        "Audience-fit structure and tone",
    ],
    "presentation": [
        "Slide sequence covers requirements",
        "Layout viability checked",
        "Editable delivery format preserved",
    ],
    "code": [
        "Build or run succeeds where feasible",
        "Core behavior validated",
        "Acceptance criteria reflected in behavior",
    ],
    "data": [
        "Traceability from source to output",
        "Formula or transformation sanity checks",
        "Summary output matches requested decision",
    ],
    "mixed": [
        "Primary route validated",
        "Secondary outputs support the main handoff",
        "No unnecessary side artifacts included",
    ],
}

DOC_EXTS = {".doc", ".docx", ".pdf", ".md", ".txt", ".rtf"}
PRESENTATION_EXTS = {".ppt", ".pptx", ".key"}
DATA_EXTS = {".xls", ".xlsx", ".csv", ".tsv", ".parquet", ".ipynb"}
CODE_EXTS = {
    ".py",
    ".js",
    ".jsx",
    ".ts",
    ".tsx",
    ".java",
    ".kt",
    ".swift",
    ".go",
    ".rs",
    ".rb",
    ".php",
    ".cpp",
    ".cc",
    ".c",
    ".cs",
    ".sh",
}

CODE_CONFIGS = {
    "package.json",
    "pnpm-lock.yaml",
    "yarn.lock",
    "pyproject.toml",
    "requirements.txt",
    "Cargo.toml",
    "go.mod",
    "Podfile",
    "pom.xml",
    "build.gradle",
    "settings.gradle",
    "Gemfile",
    "CMakeLists.txt",
}

ROUTE_KEYWORDS = {
    "document": [
        "proposal",
        "report",
        "brief",
        "requirement",
        "prd",
        "spec",
        "方案",
        "报告",
        "需求",
        "文档",
        "计划",
    ],
    "presentation": [
        "slides",
        "deck",
        "pitch",
        "presentation",
        "ppt",
        "汇报",
        "演示",
        "答辩",
        "路演",
    ],
    "code": [
        "bug",
        "feature",
        "app",
        "site",
        "api",
        "script",
        "automation",
        "代码",
        "功能",
        "程序",
        "网站",
    ],
    "data": [
        "data",
        "analysis",
        "metric",
        "sheet",
        "table",
        "dashboard",
        "数据",
        "分析",
        "报表",
        "表格",
    ],
}


def _route_scores(inventory: dict) -> tuple[dict[str, int], dict[str, list[str]]]:
    scores = {route: 0 for route in ("document", "presentation", "code", "data")}
    evidence = {route: [] for route in ("document", "presentation", "code", "data")}

    for item in inventory["files"]:
        path = Path(item["path"])
        suffix = path.suffix.lower()
        name = path.name.lower()
        path_text = str(path).lower()

        if suffix in DOC_EXTS:
            scores["document"] += 2
            evidence["document"].append(f"{path} [document file]")
        if suffix in PRESENTATION_EXTS:
            scores["presentation"] += 5
            evidence["presentation"].append(f"{path} [presentation file]")
        if suffix in DATA_EXTS:
            scores["data"] += 4
            evidence["data"].append(f"{path} [data file]")
        if suffix in CODE_EXTS:
            scores["code"] += 1
            evidence["code"].append(f"{path} [code file]")

        if path.name in CODE_CONFIGS:
            scores["code"] += 6
            evidence["code"].append(f"{path} [code config]")

        if any(part in {"src", "app", "lib", "tests"} for part in path.parts):
            scores["code"] += 2
            evidence["code"].append(f"{path} [source tree]")

        for route, keywords in ROUTE_KEYWORDS.items():
            if any(keyword in name or keyword in path_text for keyword in keywords):
                scores[route] += 2
                evidence[route].append(f"{path} [keyword match]")

    for route in evidence:
        deduped = []
        seen = set()
        for item in evidence[route]:
            if item not in seen:
                deduped.append(item)
                seen.add(item)
        evidence[route] = deduped[:8]

    return scores, evidence


def classify_inventory(inventory: dict) -> dict:
    scores, evidence = _route_scores(inventory)
    ranked = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    top_route, top_score = ranked[0]
    second_route, second_score = ranked[1]

    if top_score == 0:
        primary_route = "adaptive"
        confidence = "low"
        secondary_route = None
    elif top_score < 4 and second_score == 0:
        primary_route = "adaptive"
        confidence = "low"
        secondary_route = top_route
    elif second_score > 0 and second_score >= max(4, int(top_score * 0.7)):
        primary_route = "mixed"
        confidence = "medium" if top_score - second_score <= 3 else "low"
        secondary_route = f"{top_route}+{second_route}"
    else:
        primary_route = top_route
        secondary_route = second_route if second_score > 0 else None
        if top_score >= 8 and top_score - second_score >= 5:
            confidence = "high"
        elif top_score >= 4:
            confidence = "medium"
        else:
            confidence = "low"

    if primary_route == "mixed":
        primary_evidence = evidence[top_route] + evidence[second_route]
    elif primary_route == "adaptive":
        primary_evidence = []
        if top_route:
            primary_evidence.extend(evidence.get(top_route, []))
        if second_score > 0 and second_route and second_route in evidence:
            primary_evidence.extend(evidence.get(second_route, []))
    else:
        primary_evidence = evidence.get(primary_route, [])

    return {
        "primary_route": primary_route,
        "secondary_route": secondary_route,
        "confidence": confidence,
        "scores": scores,
        "ranked_routes": ranked,
        "evidence": evidence,
        "selected_evidence": primary_evidence[:10],
        "first_working_version": ROUTE_FIRST_VERSION[primary_route],
        "validations": ROUTE_VALIDATIONS[primary_route],
    }


def route_to_markdown(report: dict) -> str:
    lines = [
        "# Project Routing",
        "",
        f"- Primary route: `{report['primary_route']}`",
        f"- Secondary route: `{report['secondary_route'] or 'none'}`",
        f"- Confidence: `{report['confidence']}`",
        "",
        "## Route Scores",
    ]

    for route, score in sorted(report["scores"].items(), key=lambda item: item[1], reverse=True):
        lines.append(f"- {ROUTE_LABELS[route]}: `{score}`")

    lines.extend(
        [
            "",
            "## Selected Evidence",
        ]
    )
    if report["selected_evidence"]:
        for item in report["selected_evidence"]:
            lines.append(f"- {item}")
    else:
        lines.append("- No strong evidence detected")

    lines.extend(
        [
            "",
            "## Default First Working Version",
            report["first_working_version"],
            "",
            "## Route-Specific Validations",
        ]
    )
    for check in report["validations"]:
        lines.append(f"- {check}")

    return "\n".join(lines) + "\n"


def classify_project(root: Path) -> tuple[dict, dict]:
    inventory = build_inventory(root)
    report = classify_inventory(inventory)
    return inventory, report


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("project_root", help="Path to the project root")
    parser.add_argument("--format", choices=["json", "markdown"], default="markdown")
    parser.add_argument("--output", help="Optional output path")
    args = parser.parse_args()

    root = Path(args.project_root).expanduser().resolve()
    if not root.exists() or not root.is_dir():
        raise SystemExit(f"Project root not found or not a directory: {root}")

    _, report = classify_project(root)
    output = json.dumps(report, ensure_ascii=False, indent=2)
    if args.format == "markdown":
        output = route_to_markdown(report)

    if args.output:
        Path(args.output).expanduser().resolve().write_text(output, encoding="utf-8")
    else:
        print(output)


if __name__ == "__main__":
    main()
