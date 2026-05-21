# Data Branch

Use this branch when the main deliverable is a spreadsheet result, dataset transformation, analysis artifact, or structured reporting output.

## Target Outputs

Typical outputs:

- cleaned spreadsheet
- analysis workbook
- summary report with tables or charts
- reproducible data transformation
- metrics or dashboard support file

## First Working Version

The first working version should prove:

- the core data path runs end to end
- the main table, sheet, or transformation exists
- inputs can be traced to outputs

## Execution Priorities

1. identify the source data and expected output
2. inspect schema, tabs, or column structure
3. build the core transformation or calculation path
4. validate counts, formulas, or joins
5. produce the requested summary view
6. package the outputs and describe traceability

## Preferred Working Paths

- use Google Sheets tools when the target is a live sheet
- use local scripts when repeatability matters
- prefer reproducible transformations over manual one-off edits

## Validation Focus

- source-to-output traceability is clear
- formulas or transformations are sane
- major totals or row counts are checked
- the summary output answers the actual project question

## Common Repairs

- inconsistent schema -> normalize columns before analysis
- broken formula flow -> simplify and verify stepwise
- unclear output goal -> infer the likely decision artifact and make it explicit in the summary
- weak reproducibility -> script the transformation or document the exact steps
