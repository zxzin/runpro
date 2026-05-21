# Project Folder Layout

This skill accepts either a flat project folder or a structured one.

## If The User Gives A Flat Folder

Treat every file under the project root as candidate input.

After intake, create a dedicated generated workspace folder and place all runpro-managed folders inside it.

Default generated workspace:

```text
runpro_workspace/
├── 10_analysis/
├── 20_working/
├── 20_drafts/
├── 30_tools/
└── submission/
```

`submission/` is the clean submission folder. It should contain only the actual files the project requires the user to submit.

If the deliverable is a written document and the assignment does not explicitly require another final format, the submission artifact should default to `Word/.docx`.

Keep `submission/` as a top-level child of `runpro_workspace/` so the user can see the handoff folder immediately after opening the generated workspace.

Do not move the user's original files unless there is a clear reason and the user asked for reorganization.

## Preferred Layout

If you are free to normalize the workspace, use:

```text
project-root/
├── 00_inbox/                        # optional raw docs, screenshots, chats, notes, references
├── README.md or notes.md            # optional human notes
└── runpro_workspace/
    ├── 10_analysis/                 # brief, plan, checklist, audits
    ├── 20_working/                  # in-progress outputs
    ├── 20_drafts/                   # draft exports when needed
    ├── 30_tools/                    # helper scripts or generated utilities when needed
    └── submission/                  # clean final deliverables only
```

## File Handling Rules

- Original materials stay untouched.
- Runpro-generated working files go under `runpro_workspace/`.
- Working files go under `runpro_workspace/10_analysis/`, `runpro_workspace/20_working/`, or `runpro_workspace/20_drafts/`.
- Helper utilities created by the workflow go under `runpro_workspace/30_tools/` when needed.
- Final outputs go under `runpro_workspace/submission/`.
- `runpro_workspace/submission/` must contain only project-required submission contents, not summaries, audits, helper notes, or process files.
- Do not place `.md` working files, reference templates, style exemplars, draft exports, or duplicate format variants in `runpro_workspace/submission/` unless the assignment explicitly requires them.
- If the project is submitting a written artifact and no explicit final file format is stated, keep the final submission artifact in `.docx` form.
- If the project already has a strong existing structure, adapt to it instead of forcing this exact one.

## Input Priorities

During intake, prioritize files with names that look like:

- requirements
- brief
- scope
- notes
- meeting
- chat
- feedback
- revision
- final
- submit
- deliverable

Also inspect screenshots, PDFs, slide decks, and image references when they appear likely to contain requirements or target output examples.
