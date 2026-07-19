#!/usr/bin/env python3
"""
Scan final, student-facing artifacts for internal workflow/process residue.

Supported directly with the Python standard library:
- plain text / markdown-like files
- DOCX
- PPTX

PDF support uses pdftotext when available, then falls back to pypdf/PyPDF2 if
installed. Unsupported or unreadable files fail closed.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import zipfile
from dataclasses import dataclass
from pathlib import Path
from xml.etree import ElementTree as ET


TEXT_EXTENSIONS = {
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
}


@dataclass(frozen=True)
class Pattern:
    label: str
    regex: re.Pattern[str]


PATTERNS = [
    Pattern(
        "assistant/tool trace",
        re.compile(r"\b(ChatGPT|Codex|RunPro|replacewords|cutai|fixaipro)\b", re.I),
    ),
    Pattern(
        "AI or prompt process trace",
        re.compile(
            r"\b(AI[- ]?generated|large language model|LLM|prompt|AI detection|AI similarity|default ChatGPT)\b",
            re.I,
        ),
    ),
    Pattern(
        "internal audit vocabulary",
        re.compile(
            r"\b(source log|final audit|requirement ledger|rubric ledger|student-facing residue audit|process-text residue)\b",
            re.I,
        ),
    ),
    Pattern(
        "workspace or helper path",
        re.compile(
            r"(runpro_workspace|/Users/|\\Users\\|\b10_analysis\b|\b30_tools\b|source-log|final-audit|requirement-ledger)",
            re.I,
        ),
    ),
    Pattern(
        "previous assignment residue",
        re.compile(
            r"\b(previous assignment|previous task|palliative care|end-of-life work|same article|same essay|classmates?' work|words/phrasing|same sort of words)\b",
            re.I,
        ),
    ),
    Pattern(
        "workflow status residue",
        re.compile(
            r"\b(current script matched|latest PPT|submission folder|workspace|build script|speaker notes were removed|for editing and rehearsal)\b",
            re.I,
        ),
    ),
    Pattern(
        "process-framing sentence",
        re.compile(
            r"\b(this is not a generic essay|not a general essay|not write a generic list|the bite is around)\b",
            re.I,
        ),
    ),
]


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def xml_text(xml_bytes: bytes) -> str:
    try:
        root = ET.fromstring(xml_bytes)
    except ET.ParseError:
        return ""

    chunks: list[str] = []
    for node in root.iter():
        if local_name(node.tag) in {"t", "instrText"} and node.text:
            chunks.append(node.text)
    return " ".join(chunks)


def extract_zip_office(path: Path, prefixes: tuple[str, ...]) -> list[tuple[str, str]]:
    entries: list[tuple[str, str]] = []
    with zipfile.ZipFile(path) as zf:
        for name in sorted(zf.namelist()):
            if not name.endswith(".xml"):
                continue
            if not any(name.startswith(prefix) for prefix in prefixes):
                continue
            text = xml_text(zf.read(name))
            if text.strip():
                entries.append((name, text))
    return entries


def extract_docx(path: Path) -> list[tuple[str, str]]:
    return extract_zip_office(
        path,
        (
            "word/document.xml",
            "word/header",
            "word/footer",
            "word/footnotes",
            "word/endnotes",
            "word/comments",
            "word/textbox",
            "word/glossary",
        ),
    )


def extract_pptx(path: Path) -> list[tuple[str, str]]:
    return extract_zip_office(
        path,
        (
            "ppt/slides/",
            "ppt/notesSlides/",
            "ppt/comments",
            "ppt/slideMasters/",
            "ppt/handoutMasters/",
        ),
    )


def extract_pdf(path: Path) -> list[tuple[str, str]]:
    pdftotext = shutil.which("pdftotext")
    if pdftotext:
        result = subprocess.run(
            [pdftotext, "-layout", str(path), "-"],
            check=False,
            capture_output=True,
            text=True,
        )
        if result.returncode == 0 and result.stdout.strip():
            return [("pdf-extracted-text", result.stdout)]

    for module_name in ("pypdf", "PyPDF2"):
        try:
            module = __import__(module_name)
        except ImportError:
            continue

        reader_class = getattr(module, "PdfReader", None)
        if reader_class is None:
            continue
        reader = reader_class(str(path))
        pages = []
        for index, page in enumerate(reader.pages, start=1):
            try:
                text = page.extract_text() or ""
            except Exception:
                text = ""
            if text.strip():
                pages.append((f"page-{index}", text))
        if pages:
            return pages

    raise RuntimeError(
        "PDF text extraction is unavailable. Install pdftotext or pypdf/PyPDF2, or run a manual residue audit and record the limitation."
    )


def extract_text(path: Path) -> list[tuple[str, str]]:
    suffix = path.suffix.lower()
    if suffix in TEXT_EXTENSIONS:
        return [(path.name, path.read_text(encoding="utf-8", errors="replace"))]
    if suffix == ".docx":
        return extract_docx(path)
    if suffix == ".pptx":
        return extract_pptx(path)
    if suffix == ".pdf":
        return extract_pdf(path)
    raise RuntimeError(f"Unsupported file type for residue scan: {suffix or '(none)'}")


def clean_context(value: str, start: int, end: int, radius: int = 90) -> str:
    left = max(0, start - radius)
    right = min(len(value), end + radius)
    context = " ".join(value[left:right].split())
    return context


def find_hits(
    entries: list[tuple[str, str]],
    allow_patterns: list[re.Pattern[str]],
) -> list[tuple[str, str, str]]:
    hits: list[tuple[str, str, str]] = []
    for surface, text in entries:
        for pattern in PATTERNS:
            for match in pattern.regex.finditer(text):
                context = clean_context(text, match.start(), match.end())
                if any(allow.search(context) for allow in allow_patterns):
                    continue
                hits.append((surface, pattern.label, context))
    return hits


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("artifacts", nargs="+", help="Final artifact paths to scan")
    parser.add_argument(
        "--allow",
        action="append",
        default=[],
        help="Regex for an intentional visible use to ignore. Use sparingly and document it in final-audit.md.",
    )
    args = parser.parse_args()

    allow_patterns = [re.compile(value, re.I) for value in args.allow]
    all_hits: list[tuple[Path, str, str, str]] = []
    extraction_errors: list[tuple[Path, str]] = []

    for raw_path in args.artifacts:
        path = Path(raw_path).expanduser().resolve()
        if not path.exists():
            extraction_errors.append((path, "file not found"))
            continue
        try:
            entries = extract_text(path)
        except Exception as exc:
            extraction_errors.append((path, str(exc)))
            continue

        for surface, label, context in find_hits(entries, allow_patterns):
            all_hits.append((path, surface, label, context))

    if extraction_errors:
        print("Student-facing residue scan could not inspect all artifacts:", file=sys.stderr)
        for path, error in extraction_errors:
            print(f"- {path}: {error}", file=sys.stderr)
        return 2

    if all_hits:
        print("Student-facing residue scan found visible process/internal text:", file=sys.stderr)
        for path, surface, label, context in all_hits:
            print(f"- {path} :: {surface} :: {label}: {context}", file=sys.stderr)
        return 1

    for raw_path in args.artifacts:
        print(f"OK: no student-facing residue hits in {Path(raw_path).expanduser().resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
