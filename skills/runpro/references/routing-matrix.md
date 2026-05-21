# Routing Matrix

Use this matrix after inventory and reconstruction to choose the execution branch.

This matrix is heuristic, not exhaustive. It exists to speed up routing, not to limit it.

## 1. Document Branch

Use when the project's main output is a written artifact such as:

- proposal
- report
- PRD
- brief
- requirements document
- submission letter

Strong signals:

- `.doc`, `.docx`, `.pdf`, `.md`, `.txt`
- filenames containing `proposal`, `report`, `brief`, `requirement`, `prd`, `方案`, `报告`, `需求`, `文档`

Default first working version:

- a structured draft with all major required sections present

Primary validations:

- hard requirement coverage
- facts, dates, and names checked
- final structure matches the intended audience and submission format

## 2. Presentation Branch

Use when the main output is a deck or talk artifact such as:

- PPT
- slide deck
- pitch
- presentation summary
- review deck

Strong signals:

- `.ppt`, `.pptx`
- filenames containing `slides`, `deck`, `pitch`, `presentation`, `ppt`, `汇报`, `演示`, `答辩`
- image references that appear to be slide screenshots

Default first working version:

- a deck skeleton with the key slide sequence and core content scaffolded

Primary validations:

- slide structure covers requirements
- layout is usable
- visual overflow or crowding is addressed
- handoff file is editable in the required format

## 3. Code Branch

Use when the main output is software behavior or a code change such as:

- app feature
- website change
- bug fix
- automation script
- pipeline implementation

Strong signals:

- source trees and build configs such as `package.json`, `pyproject.toml`, `requirements.txt`, `Cargo.toml`, `go.mod`, `Podfile`, `pom.xml`, `build.gradle`
- directories like `src/`, `app/`, `lib/`, `tests/`
- many code files with runnable project structure

Default first working version:

- a buildable or runnable path proving the core change works

Primary validations:

- build or run succeeds where feasible
- tests or smoke checks cover the core path
- acceptance criteria are reflected in behavior, not just code presence

## 4. Data Branch

Use when the main output is a dataset, spreadsheet result, calculation, chart pack, or analysis artifact.

Strong signals:

- `.xlsx`, `.xls`, `.csv`, `.tsv`, `.parquet`, `.ipynb`
- filenames containing `data`, `analysis`, `reporting`, `metrics`, `sheet`, `table`, `数据`, `分析`, `报表`

Default first working version:

- a reproducible core table, calculation flow, or analysis pipeline

Primary validations:

- source-to-output traceability
- row, formula, or transformation sanity checks
- summary outputs align with the requested decision or deliverable

## 5. Mixed Branch

Use when there are strong signals for multiple branches and the project requires more than one artifact type.

Default rule:

- choose the branch that matches the final deliverable as the primary route
- support it with secondary routes only as needed

Examples:

- report plus spreadsheet appendix -> primary `document`, secondary `data`
- pitch deck plus working demo -> primary `presentation`, secondary `code`
- software change plus handoff document -> primary `code`, secondary `document`

## 6. Adaptive Branch

Use when the project is unusual, weak-signal, or does not map cleanly to any standard branch.

Examples:

- a custom operational handoff package
- a hybrid artifact with no clear dominant format
- a new task type where the input evidence is sparse or misleading

Default rule:

- define the end state first
- choose a provisional route only as a working hypothesis
- let the actual deliverable drive execution and validation

## Routing Rule

Do not choose a branch based only on input file count.

Prefer the branch that best matches the intended final handoff.

If no standard branch fits comfortably, use `adaptive` instead of forcing a weak match.
