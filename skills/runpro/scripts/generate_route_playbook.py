#!/usr/bin/env python3
"""
Generate a route-specific execution playbook for runpro.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from classify_project import classify_project


PLAYBOOKS = {
    "adaptive": {
        "objective": "Drive an unusual or weak-signal project to a real handoff without forcing it into the wrong template.",
        "immediate_actions": [
            "Lock the real end-state requirement before overcommitting to a standard route.",
            "Choose the smallest viable output that proves the project is moving in the right direction.",
            "Define custom validation checks if no standard branch validation fully fits.",
        ],
        "execution_priorities": [
            "End-state fit",
            "Practical handoff shape",
            "Custom validation clarity",
            "Early correction if the provisional route is wrong",
        ],
        "recommended_skills": [
            "$runpro",
            "Use branch-specific skills only if the project later resolves into a clear standard route",
        ],
        "exit_criteria": [
            "The project meets the actual requested handoff need",
            "Custom validations are explicit and passed as far as feasible",
            "The final package is understandable and usable",
        ],
        "reference_file": "references/adaptive-branch.md",
    },
    "document": {
        "objective": "Produce a submission-ready written artifact with clear structure and full requirement coverage.",
        "immediate_actions": [
            "Read the highest-priority requirement and communication files first.",
            "Reconstruct the final document structure before polishing prose.",
            "Draft all major sections with real content, then close any missing support sections.",
        ],
        "execution_priorities": [
            "Audience and format fit",
            "Requirement coverage",
            "Fact correctness",
            "Handoff-ready clarity",
        ],
        "recommended_skills": [
            "$runpro",
            "Use Google Docs tools if the target output is a native Google Doc",
        ],
        "exit_criteria": [
            "All required sections exist",
            "Hard requirements are covered",
            "The document can be sent or submitted with minimal editing",
        ],
        "reference_file": "references/document-branch.md",
    },
    "presentation": {
        "objective": "Produce an editable deck with the right slide sequence, strong visual design, usable layout, and requirement coverage.",
        "immediate_actions": [
            "Determine whether the target output is PPTX, Google Slides, or Canva.",
            "If the deck must be beautiful, class-ready, or non-generic, load $pptpro and choose slide recipes before building.",
            "Build the slide sequence and scaffold the key slides first.",
            "Render previews, repair visual defects, and rerun checks before handoff.",
        ],
        "execution_priorities": [
            "Narrative flow",
            "Slide requirement coverage",
            "Editable output format",
            "PPTPRO recipe-driven visual quality when applicable",
            "Preview-checked layout readability",
        ],
        "recommended_skills": [
            "$runpro",
            "Use $pptpro for beautiful, designed, class-ready, or non-generic PPTX work",
            "Use $slides or PowerPoint tooling for editable PPTX generation",
            "Use Google Slides or Canva tools only when the target handoff requires them",
        ],
        "exit_criteria": [
            "The deck sequence is coherent",
            "Key slide content is complete",
            "Visual breakages and overflow are addressed through rendered preview checks",
            "PPTPRO strict audit passes when $pptpro was used",
        ],
        "reference_file": "references/presentation-branch.md",
    },
    "code": {
        "objective": "Produce a working code change whose core behavior is validated, not merely drafted.",
        "immediate_actions": [
            "Inspect the repository structure and identify the smallest end-to-end path.",
            "Implement a first runnable or buildable version of the core change.",
            "Run tests, builds, or smoke checks as soon as the critical path exists.",
        ],
        "execution_priorities": [
            "Working behavior",
            "Technical validation",
            "Regression control",
            "Clear handoff summary",
        ],
        "recommended_skills": [
            "$runpro",
            "Use the most specific stack skill when one clearly matches the codebase",
        ],
        "exit_criteria": [
            "The core behavior works",
            "Relevant validation passes where feasible",
            "Remaining risk is documented and not silently deferred",
        ],
        "reference_file": "references/code-branch.md",
    },
    "data": {
        "objective": "Produce a reproducible data output with validated transformations and a usable summary artifact.",
        "immediate_actions": [
            "Identify source data, output target, and expected decision artifact.",
            "Build the core transformation or calculation path first.",
            "Check totals, formulas, joins, or row counts before polishing summaries.",
        ],
        "execution_priorities": [
            "Traceability",
            "Transformation correctness",
            "Summary usability",
            "Repeatability",
        ],
        "recommended_skills": [
            "$runpro",
            "Use Google Sheets tools when the live target is a sheet",
        ],
        "exit_criteria": [
            "Core transformations are reproducible",
            "Major numbers are sane",
            "The summary output matches the project decision need",
        ],
        "reference_file": "references/data-branch.md",
    },
    "mixed": {
        "objective": "Complete the primary deliverable first, then add only the supporting secondary artifacts needed for a full handoff.",
        "immediate_actions": [
            "Use the final handoff artifact to choose the primary route.",
            "Build the first working version of the primary route before broadening scope.",
            "Add secondary outputs only when they materially support completion.",
        ],
        "execution_priorities": [
            "Primary handoff quality",
            "Secondary artifact usefulness",
            "Scope control",
            "Package coherence",
        ],
        "recommended_skills": [
            "$runpro",
            "Use the branch-specific skill or tool that matches the primary route first",
        ],
        "exit_criteria": [
            "Primary deliverable stands on its own",
            "Secondary outputs are complete enough to support the handoff",
            "The full package is coherent and not overbuilt",
        ],
        "reference_file": "references/mixed-branch.md",
    },
}


def route_playbook_to_markdown(report: dict) -> str:
    route = report["primary_route"]
    profile = PLAYBOOKS[route]
    lines = [
        "# Route Playbook",
        "",
        f"- Primary route: `{route}`",
        f"- Secondary route: `{report['secondary_route'] or 'none'}`",
        f"- Confidence: `{report['confidence']}`",
        "",
        "## Route Objective",
        profile["objective"],
        "",
        "## Immediate Next Actions",
    ]
    for step in profile["immediate_actions"]:
        lines.append(f"- {step}")

    lines.extend(["", "## First Working Version Target", report["first_working_version"], "", "## Execution Priorities"])
    for item in profile["execution_priorities"]:
        lines.append(f"- {item}")

    lines.extend(["", "## Recommended Skills Or Tools"])
    for item in profile["recommended_skills"]:
        lines.append(f"- {item}")

    lines.extend(["", "## Route-Specific Validations"])
    for item in report["validations"]:
        lines.append(f"- {item}")

    lines.extend(["", "## Exit Criteria"])
    for item in profile["exit_criteria"]:
        lines.append(f"- {item}")

    lines.extend(
        [
            "",
            "## Supporting Reference",
            f"- `{profile['reference_file']}`",
            "",
            "## Routing Evidence Snapshot",
        ]
    )
    if report["selected_evidence"]:
        for item in report["selected_evidence"]:
            lines.append(f"- {item}")
    else:
        lines.append("- No strong evidence detected")

    return "\n".join(lines) + "\n"


def generate_playbook(root: Path) -> str:
    _, report = classify_project(root)
    return route_playbook_to_markdown(report)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("project_root", help="Path to the project root")
    parser.add_argument("--output", help="Optional output path")
    args = parser.parse_args()

    root = Path(args.project_root).expanduser().resolve()
    if not root.exists() or not root.is_dir():
        raise SystemExit(f"Project root not found or not a directory: {root}")

    output = generate_playbook(root)
    if args.output:
        Path(args.output).expanduser().resolve().write_text(output, encoding="utf-8")
    else:
        print(output)


if __name__ == "__main__":
    main()
