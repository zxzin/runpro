# Code Branch

Use this branch when the main deliverable is software behavior, a code change, or a runnable implementation.

## Target Outputs

Typical outputs:

- feature implementation
- bug fix
- automation script
- site or app change
- pipeline or service update

## First Working Version

The first working version should prove the critical path:

- the project builds, runs, or executes where feasible
- the changed behavior exists in working form
- the branch has moved beyond planning into implementation

## Execution Priorities

1. inspect the codebase and current behavior
2. identify the smallest end-to-end change proving the core path
3. implement the vertical slice
4. run tests, builds, or smoke checks
5. fix failures and harden edge cases
6. summarize the result and remaining risk

## Preferred Working Paths

- inspect repo structure before coding
- use the most specific existing skill when the stack clearly matches one
- keep edits narrow until the core behavior is proven
- only broaden refactors when necessary for correctness

## Validation Focus

- build, run, or test succeeds where feasible
- acceptance criteria are reflected in behavior, not only code presence
- regressions are not introduced in adjacent paths
- delivery summary includes what changed and how it was checked

## Common Repairs

- failing test -> diagnose root cause, patch, rerun
- unclear acceptance criteria -> infer from surrounding code and project materials, then verify conservatively
- broken build -> restore buildability before polishing
- missing documentation -> add concise usage or handoff notes if the change needs them
