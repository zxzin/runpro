#!/usr/bin/env python3
"""
Initialize a project workspace for runpro.

Creates working directories, generates a project inventory, and writes the
standard state files if they do not already exist.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from classify_project import classify_inventory, route_to_markdown
from generate_route_playbook import route_playbook_to_markdown
from project_inventory import build_inventory, inventory_to_markdown


DEFAULT_WORKSPACE_DIR = "runpro_workspace"
DELIVERY_DIR = "submission"
LEGACY_DELIVERY_DIRS = ("90_delivery", "submisSiOn")

DIRS = [
    "10_analysis",
    "20_working",
    "20_drafts",
    "30_tools",
    DELIVERY_DIR,
]

FILES = {
    "10_analysis/project-intake.md": """# Project Intake

## Project Name

## Project Goal

## Final Deliverable

## Deadline

## Evaluation Standard

## Existing Materials

## Constraints

## Current Biggest Problem

## First Requested Action

## Pending Confirmation
""",
    "10_analysis/project-brief.md": """# Project Brief

## Goal

## Deliverable

## Execution Mode

## Strict-Mode Trigger Basis

## Expected Genre And Register

## Expected Depth Or Quality Tier

## Target Quality Threshold

## All Required Parts Must Be Completed

## Audience

## Confirmed Requirements

## Required Structure Or Sections

## Required Format Or Template

## Explicit Formatting Requirements

## Constraints

## Assumptions

## Open Questions

## Completion Standard
""",
    "10_analysis/requirement-ledger.md": """# Requirement Ledger

## Requirement R1

### Source

### Type

### Requirement

### Status

pending

### Satisfaction Evidence

### Notes
""",
    "10_analysis/rubric-ledger.md": """# Rubric Ledger

Use this file for graded academic, source-backed written, formal report, literature review, proposal, dissertation-style, or teacher-feedback-driven work.

## Rubric Item C1

### Source

### Criterion

### Weight Or Importance

### Expected Evidence

### Draft Location

### Status

pending

### Evidence

### Repair Action

### Notes
""",
    "10_analysis/feasibility-check.md": """# Feasibility Check

## Completion Verdict

## Execution Mode Recommendation

## High-Achievement Reachability

## Basis For Verdict

## Required Inputs Already Present

## Recoverable Gaps

## Missing Required Inputs

## Needed From User Or External Source

## Effect On Execution
""",
    "10_analysis/execution-plan.md": """# Execution Plan

## Current Status

## Active Gate

## Execution Mode

## Locked Requirements Reference

## Template Extraction Status

## Primary Path

## Backup Path

## Contingency Path That Still Satisfies Locked Requirements

## High-Achievement Path

## Work Phases

## Files To Create Or Update

## Validation Steps

## Risks Or Blockers
""",
    "10_analysis/delivery-checklist.md": """# Delivery Checklist

- [ ] End state defined
- [ ] Feasibility checked
- [ ] Requirement lock approved
- [ ] Requirement ledger completed
- [ ] Rubric ledger completed when applicable
- [ ] Materials inventoried
- [ ] Boundaries verified
- [ ] Gaps identified
- [ ] Missing required inputs resolved or explicitly blocked
- [ ] Feasible path locked
- [ ] Skeleton version completed
- [ ] Usable version completed
- [ ] Requirement coverage confirmed
- [ ] Final deliverable created
- [ ] Important revisions applied
- [ ] Validation completed
- [ ] Final whole-document format check passed
- [ ] Rubric compliance audit passed when applicable
- [ ] Academic standards audit passed when applicable
- [ ] Source-claim integrity audit passed when applicable
- [ ] Default report-table and process-diagram style rules were applied or explicitly overridden
- [ ] All required assignment parts completed
- [ ] Target score band is plausibly reachable or true blocker documented
- [ ] Final audit passed
- [ ] Fixable failures remediated
- [ ] Final summary written
""",
    "10_analysis/final-audit.md": """# Final Audit

## Audit Scope

## Target Threshold

## Internal Score

## Estimated Score Band

## Strict-Mode Validation Chain

## Final Format Check

## Rubric Compliance Audit

## Academic Standards Audit

## Source-Claim Integrity Audit

## Academic Quality Audit

## Citation Micro-Audit

## Presentation Source Audit

## Requirement-By-Requirement Verdicts

- [pending] R1

## Validation Evidence

## Incomplete Or Failed Items

## Required Remediation Actions

## Blocking Issues

## Completion Decision
""",
    "10_analysis/remediation-log.md": """# Remediation Log

## Issue

## Impact

## Likely Cause

## Options Considered

## Chosen Fix

## Validation Result

## Remaining Risk
""",
    "10_analysis/source-log.md": """# Source Log

## Source

## Type

## Author Or Publisher

## Year

## URL Or File Path

## What It Supports

## Notes
""",
    "10_analysis/source-claim-audit.md": """# Source-Claim Integrity Audit

Use this file for source-backed written work.

## Claim C1

### Draft Location

### Claim

### Claim Type

### Source Support

### Support Verdict

pending

### Evidence Boundary

### Required Repair

### Notes
""",
    "10_analysis/approval-gate.md": """# Requirement Lock

## Project Goal

## Final Deliverable

## Execution Mode

## Expected Genre And Register

## Expected Depth Or Quality Tier

## Target Quality Threshold

## All Required Parts Must Be Completed

## Required Structure Or Sections

## Required Format Or Template

## Explicit Formatting Requirements

## Default Formatting Fallback

## Non-Negotiable Requirements

## Explicitly Forbidden Moves

## Accepted Inferences

## Personal Identity Fields

Default: leave missing submitter identity fields blank unless the user explicitly provides values to use.

## Open Questions Needing Confirmation

## Locked Execution Direction

## Approval Status

## User Confirmation Record

Pending user confirmation
""",
    "10_analysis/final-summary.md": """# Final Summary

## Completion Status

## Project Goal

## What Was Required

## Delivered Outputs

## How It Was Completed

## Validation Performed

## What Remains

## Next Recommended Action

## Remaining Risks Or Open Items
""",
}


def migrate_legacy_delivery_dir(workspace_root: Path) -> None:
    actual_entries = {entry.name: entry for entry in workspace_root.iterdir()}

    if DELIVERY_DIR in actual_entries:
        return

    for legacy_name in LEGACY_DELIVERY_DIRS:
        legacy_dir = actual_entries.get(legacy_name)
        if legacy_dir is None:
            continue

        delivery_dir = workspace_root / DELIVERY_DIR
        if legacy_name.lower() == DELIVERY_DIR.lower():
            temp_dir = workspace_root / "__runpro_submission_tmp__"
            legacy_dir.rename(temp_dir)
            temp_dir.rename(delivery_dir)
        else:
            legacy_dir.rename(delivery_dir)
        return


def ensure_dirs(root: Path, workspace_dir: str) -> Path:
    workspace_root = root / workspace_dir
    workspace_root.mkdir(parents=True, exist_ok=True)
    migrate_legacy_delivery_dir(workspace_root)
    for rel in DIRS:
        (workspace_root / rel).mkdir(parents=True, exist_ok=True)
    return workspace_root


def write_if_missing(path: Path, content: str) -> None:
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def bootstrap(
    root: Path,
    force_inventory: bool = False,
    workspace_dir: str = DEFAULT_WORKSPACE_DIR,
) -> None:
    workspace_root = ensure_dirs(root, workspace_dir)

    inventory = build_inventory(root, extra_ignore_dirs={workspace_dir})
    inventory_path = workspace_root / "10_analysis" / "project-inventory.md"
    if force_inventory or not inventory_path.exists():
        inventory_path.write_text(inventory_to_markdown(inventory), encoding="utf-8")

    routing_path = workspace_root / "10_analysis" / "project-routing.md"
    routing = classify_inventory(inventory)
    if force_inventory or not routing_path.exists():
        routing_path.write_text(route_to_markdown(routing), encoding="utf-8")

    playbook_path = workspace_root / "10_analysis" / "route-playbook.md"
    if force_inventory or not playbook_path.exists():
        playbook_path.write_text(route_playbook_to_markdown(routing), encoding="utf-8")

    for rel, content in FILES.items():
        write_if_missing(workspace_root / rel, content)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("project_root", help="Path to the project root")
    parser.add_argument(
        "--force-inventory",
        action="store_true",
        help="Regenerate runpro_workspace/10_analysis/project-inventory.md even if it already exists",
    )
    parser.add_argument(
        "--workspace-dir",
        default=DEFAULT_WORKSPACE_DIR,
        help="Subdirectory under the project root where runpro should place all generated working folders",
    )
    args = parser.parse_args()

    root = Path(args.project_root).expanduser().resolve()
    if not root.exists() or not root.is_dir():
        raise SystemExit(f"Project root not found or not a directory: {root}")

    bootstrap(
        root,
        force_inventory=args.force_inventory,
        workspace_dir=args.workspace_dir,
    )
    print(f"Bootstrapped project workspace at {root / args.workspace_dir}")


if __name__ == "__main__":
    main()
