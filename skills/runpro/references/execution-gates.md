# Execution Gates

Use this as the default project state machine.

## Gate 1: Goal Locked

Required:

- the likely project goal is clear enough to act
- the expected deliverable is identified
- major ambiguity is recorded
- the project is provisionally classified as `strict mode` or `standard mode`

Output:

- `project-intake.md`
- `project-brief.md`

## Gate 2: Feasibility Checked

Required:

- the current folder has been assessed for completion feasibility
- missing required materials are listed explicitly
- the project is classified as completeable now, completeable with recoverable gaps, or not completeable yet
- if the project is high-risk, `strict mode` is explicitly required

Output:

- `feasibility-check.md`

## Gate 3: Requirement Lock

Required:

- every explicit requirement from the project files has been captured in `requirement-ledger.md`
- exact required structure, format, template, and prohibitions are summarized
- high-impact ambiguity is either resolved or surfaced for confirmation
- the requirement lock passes structural validation before confirmation
- user confirmation is captured before execution starts
- in `strict mode`, the fixed validation chain remains active and cannot be skipped casually

Output:

- `requirement-ledger.md`
- `approval-gate.md`

## Gate 4: Path Locked

Required:

- primary path chosen
- backup path chosen
- contingency path that still satisfies all locked requirements is defined
- key blockers identified

Output:

- `execution-plan.md`

## Gate 5: First Working Version

Required:

- a skeleton or runnable version exists
- the critical path has been proven

Examples:

- a draft document with real structure
- a presentation with key slide scaffolding
- a code path that builds or runs
- a dataset pipeline that executes end to end

## Gate 6: Requirement Coverage

Required:

- hard requirements are represented
- requirement-ledger items are explicitly traced to satisfied, blocked, or not-applicable states
- major revisions are applied
- the output is no longer just a prototype
- fixable defects from earlier gates have been remediated

## Gate 7: Delivery Ready

Required:

- validation completed as far as feasible
- detailed completion audit completed
- requirement-ledger validation passes
- final-audit validation passes
- for academic or source-backed graded written submissions, academic-quality audit validation passes
- for visually polished PPT/PPTX work, PPTPRO-level checks pass: recipe map, visual enrichment/image plan, generated-image handling, rounded-corner consistency, human-facing source text, rendered preview inspection, and strict audit or documented limitation
- in `strict mode`, the requirement-lock validation chain and final validators all passed in order
- no fixable audit item remains unresolved
- all required assignment parts are complete unless a true blocker explains why they cannot be
- the final audit judges the submission plausibly within the target `90+` band or a true blocker explains why it cannot
- the current controlling score estimate is the most conservative credible estimate, not an optimistic upside case
- outputs organized for handoff
- final summary written
- no known fixable blocker remains
- status is one of:
  - `Ready to submit`
  - `Ready for review`
  - `Blocked`

## Usage Rule

Do not begin execution before Gate 2 and Gate 3 are complete unless the user explicitly waives the confirmation step.

If Gate 2 concludes `Cannot Complete Yet`, stop and request the missing required items instead of pretending execution can proceed.

Do not try to perfect a project that has not yet passed Gate 5.

For `strict mode` projects, do not bypass validator-backed gates with narrative confidence alone.

For `strict mode` projects, a skipped, stale, failed, unverified, or narratively asserted gate invalidates readiness. Reopen the active gate, repair the issue, rerun the relevant validation, and only then continue toward handoff.

For `strict mode` projects, user process overrides must be explicit and recorded. They cannot override truthfulness, source sufficiency, required templates, required formats, or material native-file validation.

If a later reassessment lowers the controlling score estimate below the target band and no true blocker exists, Gate 7 is reopened and remediation resumes automatically.

Move the project forward gate by gate.
