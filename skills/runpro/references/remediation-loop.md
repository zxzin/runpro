# Remediation Loop

Use this loop whenever the current output is incomplete, fails validation, or does not yet meet the project's acceptance standard.

## Repair Policy

The default behavior is not to stop at "found issues."

The default behavior is:

1. identify the failed check or weakness
2. explain the likely cause
3. list candidate fixes
4. choose the most reliable low-cost fix
5. apply the fix
6. re-run the relevant check
7. repeat until pass or a true blocker remains

This applies equally to final self-audit failures. A failed completion audit item is still a failed check and must re-enter the repair loop.

This also applies when the output is merely acceptable but still below the target `90+` score band. A low score estimate or incomplete assignment coverage is a remediation trigger while fixable improvements remain.

When multiple plausible score readings exist, the most conservative credible reading controls. If a later reassessment drops the work below the target band, that immediately reopens the repair loop even if an earlier audit had marked the project ready.

## What Counts As A True Blocker

Only treat these as real blockers:

- required source material does not exist
- external system or permission is unavailable
- two hard constraints are incompatible
- further changes would be speculative and unsafe

Everything else should enter the repair loop.

Do not stop the loop just to ask whether you should continue pushing toward the already-locked target. Continue automatically unless:

- the user explicitly changes the target
- the user explicitly asks to stop
- a true blocker has appeared

## Supplement Rule

If the project is missing non-critical but necessary supporting material, create or supplement it when you can do so safely.

Examples:

- add a missing explanation section to a document
- create a supporting note or handoff file
- add missing validation output or summary
- fill obvious structural gaps in a slide deck or draft
- repair PPTPRO-level deck defects such as repeated text-card slides, missing visual enrichment, weak/generated image handling, sharp default boxes, internal workflow text on slides, missing preview inspection, or source-log/deck drift

Do not wait for the user to request obvious completion work.

## Repair Ordering

Prioritize repairs in this order:

1. explicit requirement-ledger failures
2. hard requirement failures
3. incomplete required assignment parts
4. broken core functionality
5. final-audit failures that keep the work below the target score band
6. final-audit failures that would block acceptance
7. missing supporting material
8. visual or structural defects
9. polish improvements

## Logging Rule

Record meaningful failures and repairs in `runpro_workspace/10_analysis/remediation-log.md`.

Suggested fields:

- issue
- impact
- cause
- options considered
- chosen fix
- validation result
- remaining risk

When the trigger came from the completion audit, also record which audit item failed and what evidence changed after the repair.

## Exit Rule

Do not exit the repair loop while a fixable failure remains.

Exit only when:

- the output passes the required checks
- the completion audit no longer contains any fixable failed or incomplete item
- the audit judges the submission plausibly within the target `90+` band or a true blocker prevents reaching it
- the remaining issue is explicitly non-blocking
- or a true blocker prevents further progress
