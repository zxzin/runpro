# Intake Schema

Use this schema when the project starts from messy source material and you need to reconstruct what the project is, what must be delivered, and how completion will be judged.

## Core Extraction Fields

- `goal`: What needs to be achieved
- `deliverable`: What needs to be produced
- `project_type`: Document, presentation, code task, design task, data task, mixed
- `audience`: Who will read, review, approve, or receive it
- `source_materials`: What inputs are available
- `hard_constraints`: Deadlines, format rules, counts, required sections, must-have content
- `soft_preferences`: Tone, style, emphasis, examples, preferred framing
- `scope_in`: What is clearly included
- `scope_out`: What is clearly excluded
- `change_requests`: What changed during the conversation
- `acceptance_criteria`: How the output will be judged
- `deliverable_location`: Where the final result should live
- `validation_needed`: What checks must run before completion
- `blockers`: What would prevent end-to-end completion
- `unknowns`: Missing inputs that could still matter
- `nonblocking_identity_fields`: Submitter identity fields that should be left blank by default, such as student name, student ID, candidate number, class, section, email, or phone number

## Compression Rules

- Preserve exact numbers, names, dates, URLs, and ownership references.
- Merge repeated instructions into one normalized statement.
- Keep change history only if it affects the final result.
- Convert vague wishes into executable wording when safe.
- Distinguish source facts from working assumptions.
- Do not treat missing submitter identity fields as blockers or standalone questions. Keep them separate from content-critical unknowns.

## Conflict Rules

- Latest explicit instruction wins over earlier ambiguous phrasing.
- Concrete constraints win over generic preferences.
- If both sides remain plausible, keep the final draft conservative and note the unresolved point.

## Minimum Reconstruction Questions

If the request is unclear, silently try to answer these before asking the user:

1. What is the actual thing that must be delivered?
2. Who is it for?
3. What must be true for the recipient to accept it?
4. Which details are fixed versus inferred?
5. What is still missing but not blocking?
6. What evidence will show that the project is complete?

## Internal Working Format

Use this internal shape when reconstructing the project:

```text
Goal:
Deliverable:
Project type:
Audience:
Confirmed facts:
Constraints:
Validation needed:
Blockers:
Open questions:
Nonblocking identity fields:
Assumptions:
Next drafting mode:
```
