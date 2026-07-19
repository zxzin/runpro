#!/usr/bin/env python3
"""Regression tests for RunPro's compact rules and fail-closed final gate."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent


def run(command: list[str], expect_success: bool = True) -> subprocess.CompletedProcess[str]:
    completed = subprocess.run(command, text=True, capture_output=True, check=False)
    if (completed.returncode == 0) != expect_success:
        output = "\n".join(part for part in (completed.stdout, completed.stderr) if part)
        expectation = "pass" if expect_success else "fail"
        raise AssertionError(f"Expected {expectation}: {' '.join(command)}\n{output}")
    return completed


def assert_compact_contract() -> None:
    skill_path = SKILL_DIR / "SKILL.md"
    text = skill_path.read_text(encoding="utf-8")
    if len(text.splitlines()) > 500:
        raise AssertionError("SKILL.md must remain under 500 lines")
    required_markers = (
        "`90+ plausible`",
        "conservative lower bound",
        "Exact Local Rules",
        "Topic selection",
        "requirement-ledger.md",
        "rubric-ledger.md",
        "source-claim-audit.md",
        "checkpro",
        "pptpro",
        "student-facing residue",
        "quality-receipt.json",
        "--check-receipt",
        "one-line",
        "renewed confirmation",
        "all required part",
    )
    lowered = text.lower()
    missing = [marker for marker in required_markers if marker.lower() not in lowered]
    if missing:
        raise AssertionError("Compact contract lost required guarantees: " + ", ".join(missing))


def write_fixture(project_root: Path) -> None:
    run([sys.executable, str(SCRIPT_DIR / "bootstrap_project.py"), str(project_root)])
    analysis = project_root / "runpro_workspace" / "10_analysis"
    submission = project_root / "runpro_workspace" / "submission"

    (analysis / "approval-gate.md").write_text(
        """# Requirement Lock

## Project Goal
Produce a high-scoring academic paper from verified evidence.

## Final Deliverable
A graded source-backed academic paper in a final text artifact.

## Execution Mode
Strict Mode

## Expected Genre And Register
Formal academic paper.

## Expected Depth Or Quality Tier
High achievement with analytical synthesis.

## Target Quality Threshold
90+ plausible with a conservative lower bound of at least 90.

## All Required Parts Must Be Completed
Every brief and rubric part must be present.

## Required Structure Or Sections
Introduction, analysis, conclusion, and references.

## Required Format Or Template
UTF-8 text fixture for validator regression.

## Explicit Formatting Requirements
Clear headings and a reference list.

## Default Formatting Fallback
Formal academic document conventions.

## Validation Profile
- strict_mode: yes
- target_90_plus: yes
- rubric_compliance_audit: yes
- academic_standards_audit: yes
- source_claim_audit: yes
- academic_quality_audit: yes
- citation_micro_audit: yes
- local_rule_audit: yes
- presentation_source_audit: no
- student_facing_residue_audit: yes
- source_log_validation: yes
- source_visual_inventory_validation: no
- checkpro_required: yes
- pptpro_required: no
- source_minimum: 3
- preferred_recent_years: 0
- min_recent_ratio: 0
- visual_minimum_candidates: 2
- allow_zero_selected_with_rationale: no
- pptpro_deck: none
- pptpro_script: none
- pptpro_min_pictures: 0

## Non-Negotiable Requirements
Use the assessment brief, rubric, exact citation guide, and real sources.

## Explicitly Forbidden Moves
No omitted assignment parts and no unsupported claims.

## Accepted Inferences
Only low-risk formatting inferences.

## Personal Identity Fields
Leave absent identity fields blank.

## Open Questions Needing Confirmation
None.

## Locked Execution Direction
Complete all parts, audit against the rubric, repair defects, and validate the final artifact.

## Approval Status
Approved.

## User Confirmation Record
The user confirmed this scope, strict mode, format, and 90+ target.
""",
        encoding="utf-8",
    )
    (analysis / "requirement-ledger.md").write_text(
        """# Requirement Ledger

## Requirement R1
### Source
Assessment brief and user confirmation.
### Type
Content and quality.
### Requirement
Complete every required part and target 90+.
### Status
satisfied
### Satisfaction Evidence
Final artifact and final audit cover the full locked requirement.
### Notes
Validated after the final change.
""",
        encoding="utf-8",
    )
    (analysis / "source-log.md").write_text(
        """# Source Log

## Source
Official source one
## Year
2026
## URL Or File Path
https://example.com/one

## Source
Peer-reviewed source two
## Year
2025
## URL Or File Path
https://example.com/two

## Source
Official source three
## Year
2024
## URL Or File Path
https://example.com/three
""",
        encoding="utf-8",
    )
    (analysis / "final-audit.md").write_text(
        """# Final Audit

## Audit Scope
The actual final text artifact and all locked requirements were checked.

## Target Threshold
90+ plausible.

## Internal Score
94/100.

## Estimated Score Band
92-94, using the lower credible estimate.

## Strict-Mode Validation Chain
All blocking validators passed after the final change.

## Final Format Check
The actual file, headings, reference list, structure, and visible layout passed.

## Student-Facing Residue Audit
The final artifact visible text, header, footer, caption, table, comments, and notes surfaces were checked. Workflow and process status notes, ChatGPT or Codex tool traces, prompt language, previous assignment wording, file path and workspace audit vocabulary were searched. Findings were clean after repair and recheck.

## Local Rule Compliance Audit
The assessment brief, rubric, template, and exact local citation style guide were the named local sources. Task wording, learning outcomes, structure, sections and headings were checked. Word count inclusions and exclusions were checked. Format, font, spacing, margins, and file type matched the template. Academic integrity, declaration, required content and forbidden content were checked. Filename, submission package and export mechanics were checked in the actual final artifact and visible file.

## Rubric Compliance Audit
Every rubric criterion and required question has a pass status, section and paragraph location, central or high-weight importance, visible evidence, and completed revision evidence. No repair action remains.

## Academic Standards Audit
Exact citation style and in-text/reference list parity passed. Author, year, title, DOI and URL metadata passed. Format, font, spacing, margins, headings, word count and pages passed. Figures, tables, captions and chart labels have visual balance, readable legends and clean whitespace. Paragraph claim, evidence, analysis and implication logic passed. Academic register, formal grammar and precise language passed.

## Source-Claim Integrity Audit
Every major factual, empirical, evaluative and comparative claim has source support. Specific measured outcomes and endpoints retain direction, magnitude, units, sample, method, population, condition and baseline. Evidence boundaries distinguish commercial examples from measured evidence. Narrowed or removed wording was rechecked.

## Academic Quality Audit
The prompt and rubric alignment are direct. Every major section has an analytical purpose. Evidence quality is authoritative and peer-reviewed where relevant. Comparative synthesis identifies literature patterns and disagreement. Limitations, counterarguments, trade-offs and uncertainty are evaluated. Visual and table evidence is integrated. Citations identify measured outcomes and empirical numeric magnitude, unit and baseline. Theory and framework application are explicit. The conclusion gives a concise final judgement. Citation support and claim support were rechecked.

## CheckPro Execution Evidence
CheckPro reviewed the actual final artifact and native file against the prompt, rubric, required questions and criteria. Argument, synthesis, evidence quality, limitations and conclusion discipline were checked. The conservative lower credible score risk controlled the estimated score band. Repairs were revised and rechecked before signoff.

## Citation Micro-Audit
The exact local guide was used for line-by-line citation punctuation, title treatment, ordering, DOI, URL and access-date cleanup; the clean result passed after recheck.

## Presentation Source Audit
Not applicable to this non-presentation deliverable.

## Requirement-By-Requirement Verdicts
- [pass] R1 — complete scope and quality target visible in the final artifact.

## Validation Evidence
Native artifact, ledgers, sources, audits and deterministic validators.

## Incomplete Or Failed Items
None.

## Required Remediation Actions
None.

## Blocking Issues
None.

## Completion Decision
Ready to submit
""",
        encoding="utf-8",
    )
    (submission / "final.txt").write_text(
        "Final academic submission\n\nThe evidence supports the stated conclusion.\n",
        encoding="utf-8",
    )


def remove_section(text: str, heading: str) -> str:
    start = text.index(heading)
    next_heading = text.find("\n## ", start + len(heading))
    if next_heading == -1:
        return text[:start].rstrip() + "\n"
    return text[:start].rstrip() + "\n\n" + text[next_heading + 1 :]


def assert_schema_migration() -> None:
    with tempfile.TemporaryDirectory(prefix="runpro-migration-") as raw:
        root = Path(raw)
        bootstrap = [sys.executable, str(SCRIPT_DIR / "bootstrap_project.py"), str(root)]
        run(bootstrap)
        analysis = root / "runpro_workspace" / "10_analysis"
        approval = analysis / "approval-gate.md"
        final_audit = analysis / "final-audit.md"
        approval.write_text(
            remove_section(approval.read_text(encoding="utf-8"), "## Validation Profile"),
            encoding="utf-8",
        )
        audit_text = remove_section(
            final_audit.read_text(encoding="utf-8"), "## Local Rule Compliance Audit"
        )
        audit_text = remove_section(audit_text, "## CheckPro Execution Evidence")
        final_audit.write_text(audit_text, encoding="utf-8")
        run(bootstrap)
        if "## Validation Profile" not in approval.read_text(encoding="utf-8"):
            raise AssertionError("Bootstrap did not migrate an existing approval gate")
        migrated_audit = final_audit.read_text(encoding="utf-8")
        for heading in ("## Local Rule Compliance Audit", "## CheckPro Execution Evidence"):
            if heading not in migrated_audit:
                raise AssertionError(f"Bootstrap did not restore {heading}")


def assert_final_gate() -> None:
    with tempfile.TemporaryDirectory(prefix="runpro-contract-") as raw:
        root = Path(raw)
        write_fixture(root)
        validator = [sys.executable, str(SCRIPT_DIR / "runpro_validate.py"), str(root)]
        run(validator)
        run([*validator, "--check-receipt"])

        artifact = root / "runpro_workspace" / "submission" / "final.txt"
        artifact.write_text(artifact.read_text(encoding="utf-8") + "Late safe edit.\n", encoding="utf-8")
        run([*validator, "--check-receipt"], expect_success=False)
        run(validator)

        approval = root / "runpro_workspace" / "10_analysis" / "approval-gate.md"
        approved_text = approval.read_text(encoding="utf-8")
        protected_gates = (
            "strict_mode",
            "target_90_plus",
            "rubric_compliance_audit",
            "academic_standards_audit",
            "source_claim_audit",
            "academic_quality_audit",
            "citation_micro_audit",
            "local_rule_audit",
            "student_facing_residue_audit",
            "source_log_validation",
            "checkpro_required",
        )
        for key in protected_gates:
            approval.write_text(
                approved_text.replace(f"- {key}: yes", f"- {key}: no"),
                encoding="utf-8",
            )
            failed = run(validator, expect_success=False)
            failure_output = (failed.stdout + failed.stderr).lower()
            if key not in failure_output:
                raise AssertionError(f"Under-scoped profile failure did not name {key}")

        presentation_text = approved_text.replace(
            "A graded source-backed academic paper in a final text artifact.",
            "A graded source-backed 90+ polished PowerPoint presentation and slide deck.",
        ).replace("Formal academic paper.", "Professional high visual quality presentation.")
        approval.write_text(presentation_text, encoding="utf-8")
        presentation_failure = run(validator, expect_success=False)
        presentation_output = (presentation_failure.stdout + presentation_failure.stderr).lower()
        for key in (
            "source_visual_inventory_validation",
            "presentation_source_audit",
            "pptpro_required",
        ):
            if key not in presentation_output:
                raise AssertionError(f"Presentation profile failure did not name {key}")

        approval.write_text(approved_text, encoding="utf-8")
        final_audit = root / "runpro_workspace" / "10_analysis" / "final-audit.md"
        audit_text = final_audit.read_text(encoding="utf-8")
        start = audit_text.index("## Rubric Compliance Audit")
        end = audit_text.index("## Academic Standards Audit")
        final_audit.write_text(
            audit_text[:start] + "## Rubric Compliance Audit\nPass.\n\n" + audit_text[end:],
            encoding="utf-8",
        )
        run(validator, expect_success=False)


def main() -> None:
    assert_compact_contract()
    assert_schema_migration()
    assert_final_gate()
    print("RunPro contract regression PASS")


if __name__ == "__main__":
    main()
