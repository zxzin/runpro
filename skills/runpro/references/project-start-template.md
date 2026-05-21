# Project Start Template

Use this template when the user starts a new project or when the project folder does not already contain a clear kickoff note.

Create `runpro_workspace/10_analysis/project-intake.md` in this shape:

```text
# Project Intake

## Project Name
## Project Goal
## Final Deliverable
## Deadline
## Evaluation Standard
## Existing Materials
## Constraints
## Current Biggest Problem
## First Requested Action
```

## Rules

- If the user supplied these fields explicitly, preserve their wording.
- If the folder implies some of these fields but does not state them directly, fill them with cautious inferences and label them as inferred.
- If a field is missing and not blocking, leave it under a short `Pending Confirmation` note instead of stopping the project.
- Treat this intake file as the normalized startup contract for the project.
- After the intake is normalized, convert it into a strict requirement lock before execution begins.
- The requirement lock should explicitly capture required sections, required format or template, must-do items, and must-not-do items whenever the materials imply them.
- After the requirement lock is presented, execution must wait for user confirmation.
- Once confirmed, do not deviate from that lock unless the user re-approves the change.
