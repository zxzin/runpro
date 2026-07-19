#!/usr/bin/env python3
"""Run RunPro's final blocking checks once and bind them to a quality receipt."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from validate_requirement_lock import parse_sections, parse_validation_profile


SCRIPT_DIR = Path(__file__).resolve().parent
SKILLS_DIR = SCRIPT_DIR.parent.parent
PPTPRO_AUDIT = SKILLS_DIR / "pptpro" / "scripts" / "pptpro_audit.py"
SUPPORTED_RESIDUE_EXTENSIONS = {
    ".txt",
    ".md",
    ".markdown",
    ".rst",
    ".csv",
    ".tsv",
    ".json",
    ".yaml",
    ".yml",
    ".py",
    ".js",
    ".jsx",
    ".ts",
    ".tsx",
    ".html",
    ".css",
    ".scss",
    ".java",
    ".c",
    ".cc",
    ".cpp",
    ".h",
    ".hpp",
    ".swift",
    ".kt",
    ".kts",
    ".go",
    ".rs",
    ".sql",
    ".sh",
    ".bash",
    ".zsh",
    ".toml",
    ".ini",
    ".cfg",
    ".xml",
    ".docx",
    ".pptx",
    ".pdf",
}
YES_NO_KEYS = {
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
    "allow_zero_selected_with_rationale",
}


def normalized(value: str) -> str:
    return " ".join(value.lower().replace("_", " ").split())


def is_yes(profile: dict[str, str], key: str) -> bool:
    return profile[key].strip().lower() == "yes"


def parse_int(profile: dict[str, str], key: str) -> int:
    try:
        return int(profile[key])
    except ValueError as exc:
        raise SystemExit(f"Validation profile value {key} must be an integer.") from exc


def parse_float(profile: dict[str, str], key: str) -> float:
    try:
        return float(profile[key])
    except ValueError as exc:
        raise SystemExit(f"Validation profile value {key} must be numeric.") from exc


def run_check(label: str, command: list[str]) -> dict[str, str]:
    completed = subprocess.run(command, text=True, capture_output=True, check=False)
    output = "\n".join(part.strip() for part in (completed.stdout, completed.stderr) if part.strip())
    if completed.returncode != 0:
        raise SystemExit(f"{label} failed.\n{output}")
    final_line = output.splitlines()[-1] if output else "passed"
    return {"label": label, "result": final_line}


def contains_any(text: str, markers: tuple[str, ...]) -> bool:
    return any(marker in text for marker in markers)


def require_yes(profile: dict[str, str], key: str, reason: str, failures: list[str]) -> None:
    if not is_yes(profile, key):
        failures.append(f"{key} must be yes: {reason}")


def validate_profile_consistency(
    sections: dict[str, str],
    profile: dict[str, str],
    submission_files: list[Path],
) -> list[str]:
    failures: list[str] = []
    for key in YES_NO_KEYS:
        if profile.get(key, "").strip().lower() not in {"yes", "no"}:
            failures.append(f"{key} must be explicitly yes or no")

    scope_text = normalized(
        "\n".join(
            sections.get(name, "")
            for name in (
                "Project Goal",
                "Final Deliverable",
                "Execution Mode",
                "Expected Genre And Register",
                "Expected Depth Or Quality Tier",
                "Target Quality Threshold",
                "All Required Parts Must Be Completed",
                "Required Structure Or Sections",
                "Required Format Or Template",
                "Explicit Formatting Requirements",
                "Non-Negotiable Requirements",
                "Explicitly Forbidden Moves",
                "Locked Execution Direction",
            )
        )
    )
    execution_mode = normalized(sections.get("Execution Mode", ""))
    target_90 = contains_any(
        scope_text,
        ("90+", "90 +", "90 plus", "at least 90", "90 or above", "high achievement"),
    )
    written = contains_any(
        scope_text,
        (
            "essay",
            "paper",
            "written assignment",
            "academic report",
            "literature review",
            "dissertation",
            "proposal",
            "docx",
            "word document",
            "report",
            "reflection",
            "reflective",
            "portfolio",
        ),
    )
    graded = contains_any(
        scope_text,
        ("graded", "grade", "score", "rubric", "assessment", "assignment", "coursework", "marking"),
    )
    source_backed = contains_any(
        scope_text,
        ("source-backed", "source backed", "citation", "reference", "literature", "research", "evidence"),
    )
    presentation = contains_any(scope_text, ("pptx", "powerpoint", "presentation", "slide deck", "slides"))
    polished_presentation = presentation and (
        target_90
        or contains_any(scope_text, ("pptpro", "polished", "professional visual", "high visual quality"))
    )
    local_submission = contains_any(
        scope_text,
        (
            "school",
            "university",
            "course",
            "module",
            "assignment",
            "assessment",
            "workplace",
            "client",
            "journal",
            "conference",
            "platform submission",
            "rubric",
            "template",
        ),
    )
    graded_written = graded and written
    native_sensitive = contains_any(
        scope_text,
        (".docx", ".pptx", "native file", "spreadsheet", "software", "code change", "dataset", "exported file"),
    )
    high_risk = (
        target_90
        or graded_written
        or source_backed
        or presentation
        or local_submission
        or native_sensitive
    )

    if high_risk:
        require_yes(profile, "strict_mode", "high-risk work must use strict mode", failures)
        if execution_mode not in {"strict", "strict mode"}:
            failures.append("Execution Mode must be Strict Mode for this high-risk project")
    if target_90:
        require_yes(profile, "target_90_plus", "the locked target is 90+", failures)
    if graded_written:
        for key, reason in (
            ("rubric_compliance_audit", "graded written work needs criterion-level rubric coverage"),
            ("academic_standards_audit", "graded written work needs actual-file academic standards checks"),
            ("academic_quality_audit", "graded written work needs argumentation-quality checks"),
            ("checkpro_required", "formal graded written work requires CheckPro or its recorded equivalent"),
        ):
            require_yes(profile, key, reason, failures)
    if source_backed and written:
        for key, reason in (
            ("source_log_validation", "source-backed written work needs verified sources"),
            ("source_claim_audit", "source-backed written work needs claim-to-source checking"),
            ("citation_micro_audit", "source-backed written work needs citation-level cleanup"),
        ):
            require_yes(profile, key, reason, failures)
    if local_submission:
        require_yes(profile, "local_rule_audit", "local submission rules override generic conventions", failures)
    if source_backed and presentation:
        for key, reason in (
            ("source_log_validation", "source-backed presentation needs verified sources"),
            ("source_visual_inventory_validation", "source-backed presentation needs visual candidates and provenance"),
            ("presentation_source_audit", "source-backed presentation needs deck/source consistency"),
        ):
            require_yes(profile, key, reason, failures)
    if polished_presentation:
        require_yes(profile, "pptpro_required", "polished or 90+ presentation work requires PPTPro strict audit", failures)
    if any(path.suffix.lower() in SUPPORTED_RESIDUE_EXTENSIONS for path in submission_files):
        require_yes(
            profile,
            "student_facing_residue_audit",
            "final submission artifacts must be checked for workflow, tool, prompt, and prior-task residue",
            failures,
        )

    if is_yes(profile, "source_log_validation") and parse_int(profile, "source_minimum") < 3:
        failures.append("source_minimum must be at least 3 when source-log validation is enabled")
    if is_yes(profile, "source_visual_inventory_validation") and parse_int(
        profile, "visual_minimum_candidates"
    ) < 2:
        failures.append("visual_minimum_candidates must be at least 2 when visual inventory validation is enabled")
    if is_yes(profile, "pptpro_required") and profile["pptpro_deck"].strip().lower() == "none":
        failures.append("pptpro_deck must name the final deck when pptpro_required is yes")
    if not is_yes(profile, "pptpro_required") and profile["pptpro_deck"].strip().lower() != "none":
        failures.append("pptpro_deck must be none when pptpro_required is no")
    if not is_yes(profile, "source_visual_inventory_validation") and is_yes(
        profile, "allow_zero_selected_with_rationale"
    ):
        failures.append("allow_zero_selected_with_rationale cannot be yes when visual inventory validation is disabled")

    return failures


def resolve_project_path(project_root: Path, raw: str) -> Path:
    candidate = Path(raw).expanduser()
    path = candidate.resolve() if candidate.is_absolute() else (project_root / candidate).resolve()
    try:
        path.relative_to(project_root)
    except ValueError as exc:
        raise SystemExit(f"Validation path escapes the project root: {raw}") from exc
    if not path.exists() or not path.is_file():
        raise SystemExit(f"Validation artifact not found: {path}")
    return path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def manifest_files(project_root: Path, analysis_dir: Path, submission_dir: Path) -> list[Path]:
    paths = [
        path
        for path in analysis_dir.rglob("*")
        if path.is_file() and path.name != "quality-receipt.json"
    ]
    if submission_dir.exists():
        paths.extend(path for path in submission_dir.rglob("*") if path.is_file())
    return sorted(set(paths), key=lambda path: path.as_posix())


def relative_manifest(project_root: Path, paths: list[Path]) -> dict[str, str]:
    return {path.relative_to(project_root).as_posix(): sha256(path) for path in paths}


def check_receipt(project_root: Path, workspace_dir: str) -> None:
    analysis_dir = project_root / workspace_dir / "10_analysis"
    submission_dir = project_root / workspace_dir / "submission"
    receipt_path = analysis_dir / "quality-receipt.json"
    if not receipt_path.exists():
        raise SystemExit(f"Quality receipt not found: {receipt_path}")
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    expected = receipt.get("manifest", {})
    current = relative_manifest(
        project_root,
        manifest_files(project_root, analysis_dir, submission_dir),
    )
    if current != expected:
        changed = sorted(set(current) | set(expected))
        changed = [path for path in changed if current.get(path) != expected.get(path)]
        raise SystemExit(
            "Quality receipt is stale. Re-run final validation after changes to: "
            + ", ".join(changed)
        )
    validator_hashes = receipt.get("validator_hashes", {})
    current_validator_hashes = {
        path.name: sha256(path)
        for path in sorted(SCRIPT_DIR.glob("*.py"))
        if path.name != "__init__.py"
    }
    if receipt.get("pptpro_used"):
        current_validator_hashes["pptpro_audit.py"] = sha256(PPTPRO_AUDIT)
    if current_validator_hashes != validator_hashes:
        raise SystemExit("Quality receipt is stale because the validation contract changed.")
    print(f"Quality receipt current: {receipt_path}")


def validate(project_root: Path, workspace_dir: str) -> None:
    workspace_root = project_root / workspace_dir
    analysis_dir = workspace_root / "10_analysis"
    submission_dir = workspace_root / "submission"
    approval_gate = analysis_dir / "approval-gate.md"
    requirement_ledger = analysis_dir / "requirement-ledger.md"
    final_audit = analysis_dir / "final-audit.md"

    for path in (approval_gate, requirement_ledger, final_audit):
        if not path.exists():
            raise SystemExit(f"Required RunPro state file not found: {path}")

    sections = parse_sections(approval_gate.read_text(encoding="utf-8"))
    profile = parse_validation_profile(sections.get("Validation Profile", ""))
    submission_files = sorted(
        (path for path in submission_dir.rglob("*") if path.is_file()),
        key=lambda path: path.as_posix(),
    ) if submission_dir.exists() else []

    results: list[dict[str, str]] = []
    results.append(
        run_check(
            "requirement lock",
            [
                sys.executable,
                str(SCRIPT_DIR / "validate_requirement_lock.py"),
                str(approval_gate),
                "--require-approved",
                "--require-validation-profile",
            ],
        )
    )
    consistency_failures = validate_profile_consistency(sections, profile, submission_files)
    if consistency_failures:
        raise SystemExit(
            "Validation profile contradicts the locked project scope:\n- "
            + "\n- ".join(consistency_failures)
        )

    results.append(
        run_check(
            "requirement ledger",
            [
                sys.executable,
                str(SCRIPT_DIR / "validate_requirement_ledger.py"),
                str(requirement_ledger),
                "--final",
            ],
        )
    )

    final_command = [sys.executable, str(SCRIPT_DIR / "validate_final_audit.py"), str(final_audit)]
    final_flags = {
        "target_90_plus": "--require-90-plus",
        "citation_micro_audit": "--require-citation-micro-audit",
        "academic_quality_audit": "--require-academic-quality-audit",
        "rubric_compliance_audit": "--require-rubric-compliance-audit",
        "academic_standards_audit": "--require-academic-standards-audit",
        "source_claim_audit": "--require-source-claim-audit",
        "presentation_source_audit": "--require-presentation-source-audit",
        "student_facing_residue_audit": "--require-student-facing-residue-audit",
        "local_rule_audit": "--require-local-rule-audit",
        "checkpro_required": "--require-checkpro-evidence",
    }
    for key, flag in final_flags.items():
        if is_yes(profile, key):
            final_command.append(flag)
    results.append(run_check("final audit", final_command))

    if is_yes(profile, "source_log_validation"):
        source_command = [
            sys.executable,
            str(SCRIPT_DIR / "validate_source_log.py"),
            str(analysis_dir / "source-log.md"),
            "--min-sources",
            str(parse_int(profile, "source_minimum")),
        ]
        preferred_years = parse_int(profile, "preferred_recent_years")
        recent_ratio = parse_float(profile, "min_recent_ratio")
        if preferred_years > 0 or recent_ratio > 0:
            if preferred_years <= 0 or recent_ratio <= 0:
                raise SystemExit(
                    "preferred_recent_years and min_recent_ratio must both be positive when recency validation is enabled."
                )
            source_command.extend(
                [
                    "--preferred-recent-years",
                    str(preferred_years),
                    "--min-recent-ratio",
                    str(recent_ratio),
                ]
            )
        results.append(run_check("source log", source_command))

    if is_yes(profile, "source_visual_inventory_validation"):
        visual_command = [
            sys.executable,
            str(SCRIPT_DIR / "validate_source_visual_inventory.py"),
            str(analysis_dir / "source-visual-inventory.md"),
            "--min-candidates",
            str(parse_int(profile, "visual_minimum_candidates")),
        ]
        if is_yes(profile, "allow_zero_selected_with_rationale"):
            visual_command.append("--allow-zero-selected-with-rationale")
        results.append(run_check("source visual inventory", visual_command))

    scanned_artifacts: list[Path] = []
    if is_yes(profile, "student_facing_residue_audit"):
        scanned_artifacts = [
            path for path in submission_files if path.suffix.lower() in SUPPORTED_RESIDUE_EXTENSIONS
        ]
        if not scanned_artifacts:
            raise SystemExit(
                "Student-facing residue audit is required, but no supported final artifact exists in submission/."
            )
        results.append(
            run_check(
                "student-facing residue",
                [
                    sys.executable,
                    str(SCRIPT_DIR / "scan_student_facing_residue.py"),
                    *[str(path) for path in scanned_artifacts],
                ],
            )
        )

    pptpro_used = is_yes(profile, "pptpro_required")
    if pptpro_used:
        if not PPTPRO_AUDIT.exists():
            raise SystemExit(f"PPTPro audit script not found: {PPTPRO_AUDIT}")
        deck = resolve_project_path(project_root, profile["pptpro_deck"])
        pptpro_command = [
            sys.executable,
            str(PPTPRO_AUDIT),
            str(deck),
            "--render",
            "--strict",
            "--min-pictures",
            str(parse_int(profile, "pptpro_min_pictures")),
        ]
        script_value = profile["pptpro_script"].strip()
        if script_value.lower() != "none":
            script_path = resolve_project_path(project_root, script_value)
            pptpro_command.extend(["--script", str(script_path)])
        results.append(run_check("PPTPro strict audit", pptpro_command))

    manifest = relative_manifest(
        project_root,
        manifest_files(project_root, analysis_dir, submission_dir),
    )
    validator_hashes = {
        path.name: sha256(path)
        for path in sorted(SCRIPT_DIR.glob("*.py"))
        if path.name != "__init__.py"
    }
    if pptpro_used:
        validator_hashes["pptpro_audit.py"] = sha256(PPTPRO_AUDIT)
    receipt = {
        "schema_version": 1,
        "status": "PASS",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "project_root": str(project_root),
        "validation_profile": profile,
        "checks": results,
        "scanned_artifacts": [path.relative_to(project_root).as_posix() for path in scanned_artifacts],
        "pptpro_used": pptpro_used,
        "manifest": manifest,
        "validator_hashes": validator_hashes,
    }
    receipt_path = analysis_dir / "quality-receipt.json"
    receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"RunPro final validation PASS ({len(results)} blocking checks): {receipt_path}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run RunPro's final fail-closed validation chain and create/check a hash-bound receipt."
    )
    parser.add_argument("project_root", help="Project root containing runpro_workspace")
    parser.add_argument("--workspace-dir", default="runpro_workspace")
    parser.add_argument(
        "--check-receipt",
        action="store_true",
        help="Verify that no control file, final artifact, or validator changed after the last PASS.",
    )
    args = parser.parse_args()
    project_root = Path(args.project_root).expanduser().resolve()
    if not project_root.exists() or not project_root.is_dir():
        raise SystemExit(f"Project root not found: {project_root}")
    if args.check_receipt:
        check_receipt(project_root, args.workspace_dir)
    else:
        validate(project_root, args.workspace_dir)


if __name__ == "__main__":
    main()
