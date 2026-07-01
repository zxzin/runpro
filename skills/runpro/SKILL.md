---
name: runpro
description: Execute a project from a folder of raw materials. Use when the user drops messages, screenshots, documents, drafts, and references into a project directory and wants Codex to identify the real goal, build a plan, do the work, drive the project to a submission-ready state, verify completion, and return a clear final summary of what was required, what was completed, and how it was done.
---

# Project Folder Executor

## Overview

Use this skill when the project starts as a folder full of messy inputs, but the expected outcome is a finished, reviewable, or submittable result.

This is not a summary-only skill. This skill is for automatic intake, planning, routing, execution, delivery tracking, final checking, and completion reporting.

The default interaction model is:

1. reconstruct requirements
2. assess whether the current materials are sufficient to complete the project
3. lock the requirements with user confirmation
4. execute only against the locked scope
5. return result only by default

## Optimized Operating Model

The goal is not to mirror a human manual workflow. The goal is to minimize user input while still keeping project execution reliable.

Default principle:

- the user should only need to point at a project folder or invoke `$runpro`
- the skill should infer as much as safely possible
- explicit questions should be reserved for high-impact ambiguity only
- execution should continue until the project reaches a real handoff state

Quality overrides efficiency.

If there is any conflict between token savings and:

- requirement adherence
- assignment correctness
- factual truthfulness
- source sufficiency
- local institutional rule compliance
- format compliance
- final delivery quality

the skill must preserve quality and spend the extra work required.

## Exact Local Rules Rule

For school, university, course, workplace, client, funding-body, journal, conference, or platform submissions, local rules override generic knowledge.

Default rule:

- do not treat broad labels such as `Harvard`, `APA`, `essay`, `report`, `reflective writing`, `critical thinking`, `poster`, `PPT`, `portfolio`, `word count`, `template`, or `submission-ready` as self-explanatory when local materials define them more narrowly
- inspect the exact local rule source before execution whenever it is present in the folder or referenced by the user
- local rule sources include assessment briefs, rubrics, marking grids, course handbooks, module guides, tutor feedback, lecture slides, examples, templates, style guides, referencing guides, word-count policies, academic-integrity policies, submission portal instructions, filenames, screenshots, and comments from the user
- extract local requirements into the requirement ledger as separate checkable items, including rules that look minor or mechanical
- final readiness must be checked against those local sources, not against generic assumptions about the genre

When a local source and a generic convention conflict, the local source controls unless it is obviously outdated or contradicted by a later authoritative local source. If source priority is unclear, use the newest assignment-specific source first, then course/module guide, then institutional guide, then generic convention.

Common local-rule areas that must be checked when relevant:

- task wording, learning outcomes, rubric criteria, and marking bands
- required topic, case study, question choice, or scenario boundaries
- topic differentiation, default-topic risk, and collision risk with classmates, exemplars, teacher examples, assignment-suggested topics, previous submissions, and topics that a generic LLM would likely recommend from the same materials
- structure, section sequence, headings, reflective model, PEEL/critical-writing expectations, and conclusion rules
- word-count policy, including what is included or excluded
- formatting, template, title page, cover sheet, font, spacing, margins, page numbers, and file type
- citation and reference style, including institutional variants
- source type limits, recency expectations, source count, and evidence hierarchy
- use of first person, reflective voice, professional voice, or third person
- AI-use, authorship, plagiarism, declaration, and academic-integrity constraints
- tables, figures, appendices, captions, and whether they count toward the word limit
- submission filename, folder/package contents, export type, and visible metadata

Do not mark a project `Ready to submit` if any applicable local-rule area has only been inferred from generic practice while a local source is available to check.

## Topic Differentiation And Collision-Avoidance Rule

For graded coursework, school, university, or cohort-based submissions where students choose a topic, topic selection must consider not only feasibility but also collision risk.

Default rule:

- do not automatically recommend the broadest, safest, or most obvious topic simply because it has the easiest source base
- identify topics that are likely to be chosen by many classmates or generated by generic AI from the same assignment materials, especially when the brief lists examples or the course used a worked case
- treat user warnings about classmates, prior cohorts, AI-default topics, or previous assignment similarity as local rules and record them in the requirement ledger or approval gate
- compare candidate topics on both source sufficiency and differentiation: assignment fit, specificity, available English evidence, China or local-context policy support, ability to support required critical analysis, prior-work overlap, teacher-example overlap, and likely classmate collision
- prefer a topic that is specific, source-backed, locally relevant, and analytically rich over a generic default topic, as long as it still satisfies every locked requirement
- if a distinctive topic has weaker source support than a default topic, do not hide the trade-off; either gather more sources, narrow the topic, or present the choice for confirmation
- do not sacrifice truthfulness, required content coverage, or source sufficiency merely to be unusual

For assignment-plan or proposal work, record the selected topic and the rejected default topics with the reason, such as `rejected due to high collision/default-AI risk`, `forbidden by class example`, `overlaps prior work`, or `insufficient evidence`.

## High Achievement Target

When the user wants a high-scoring submission, treat the default goal as:

- maximize the probability that the final submission can score around `90+` under the real grading standard
- achieve full completion of all required assignment content first
- then push quality, depth, fit-to-rubric, and polish to the level most likely to reach that score band
- no unresolved fixable weakness in core requirement coverage
- no visible mismatch between deliverable type and expected quality tier

This is still not a guarantee of an external grade. Real grading depends on the instructor, rubric interpretation, and factors outside the workspace. But the workflow should optimize toward that outcome, not merely toward "good enough."

Default rule:

- do not stop at "acceptable"
- do not trade away required content to achieve a cleaner but narrower result
- push the work until all required content is complete and the audit indicates the submission is plausibly in the `90+` band, or a true blocker remains

For graded academic writing, "high-scoring" must include argument quality, not only completion and formatting. Apply the following gate only when the project is a paper, academic report, literature review, dissertation-style submission, proposal, or other source-backed written assignment where analysis and evidence quality affect the grade. Do not apply it as a hard blocker to unrelated project types such as code projects, operational documents, simple forms, administrative summaries, design-only decks, data-cleaning outputs, or business artifacts unless the user/rubric explicitly asks for academic argumentation.

When this gate applies, the submission is not high-achievement ready until the audit confirms:

- a rubric ledger was built from the assignment brief, rubric, marking criteria, teacher feedback, required questions, and required format rules before full drafting
- local-rule sources were identified, prioritized, and converted into checkable requirements before full drafting; this includes course-specific or institution-specific rules for structure, word count, formatting, citation, academic integrity, templates, file type, and submission mechanics when present
- every rubric criterion, required question, required sub-part, and actionable teacher-feedback point has a final `pass`, `partial`, `fail`, or `not assessable` judgement with draft-location evidence
- no high-weight or central rubric item remains `fail`, `partial`, or `not assessable` when the project is marked `Ready to submit`
- academic standards were checked as a strict gate, including citation style, in-text/reference matching, reference-list correctness, formatting, captions, figures/tables, paragraph reasoning, and academic register
- citation style was resolved from the exact assignment or institutional guide, not from a generic style name; if the folder contains a referencing guide, library guide, style PDF, assessment appendix, or exemplar reference list, that file is the authority and its examples must be checked before drafting and again before handoff
- final reference-list formatting was line-by-line audited against the exact local guide when assessable, including title quotation rules, punctuation between title/journal/volume, DOI/URL wording, access-date wrapper, capitalization, issue spacing, italics or lack of italics, and ordering
- source-claim integrity was checked for major factual, empirical, evaluative, and comparative claims, and each major claim is either supported by a suitable source or explicitly repaired/removed
- the thesis, research question, or central judgement directly answers the assignment prompt instead of orbiting around the topic
- every rubric criterion, required question, and required sub-part has a visible answer in the body, not only an implied answer in the overall theme
- each major section has a clear analytical job and contributes to the final judgement; no section exists only as background filler
- paragraphs use evidence to explain implications, causes, trade-offs, limits, or consequences rather than simply placing citations after descriptive statements
- the source base is appropriate to the claim type, with peer-reviewed, guideline, official, primary-data, or otherwise authoritative evidence used for high-stakes factual claims
- contrary evidence, limitations, uncertainty, or trade-offs are acknowledged where the topic or rubric expects evaluation rather than advocacy
- key terms, scope boundaries, comparison criteria, and methodology choices are defined before they are used to make evaluative claims
- tables, figures, diagrams, and other visuals are actively used in the prose to draw conclusions rather than merely displayed
- literature coverage is comparative and evaluative, not just a list of source summaries or formulation examples
- literature synthesis identifies patterns, disagreements, evidence strength, and gaps rather than only saying what each source found
- repeated central ideas are stated once and then developed through evidence, comparison, or application-specific analysis instead of being restated across sections
- claims tied to citations identify the relevant measured outcome when possible, such as overrun, drainage, viscosity, modulus, hardness, sensory score, oral friction, storage stability, yield, accuracy, cost, or other field-specific metric
- numerical or empirical claims preserve direction, magnitude, units, groups, and conditions when those details affect interpretation
- the work applies theory, frameworks, course concepts, methods, or case context explicitly when the assignment provides or implies them
- transitions and topic sentences make the argument traceable so the reader can follow why one section leads to the next
- the conclusion is shorter than the body analysis, states the final judgement directly, and does not re-summarize every earlier section
- the conclusion answers the original prompt, states implications and limits, and does not introduce unsupported new claims
- commercial pages, product labels, marketing claims, and screenshots are not treated as evidence for scientific, nutritional, sensory, performance, or sustainability superiority unless the source actually measures that outcome
- all citations correspond to real sources actually used, and no citation is decorative, mismatched, or attached to a claim the source does not support

When the project is a formal academic paper, academic report, literature review, dissertation-style submission, proposal, or similar graded source-backed written submission, use the `checkpro` skill before final handoff when available. If that skill is unavailable, apply the same checks manually and record the result in the final audit. If the project is not this genre, do not force `checkpro`; use the route-specific quality checks instead.

## Conservative Score Rule

For high-achievement projects, the controlling estimate is the most conservative credible estimate, not the most optimistic scenario.

- do not mark the work as `90+ plausible` if your lowest credible current estimate still falls below `90`
- if two plausible readings conflict, such as `90+ plausible` versus `83-88` or `86-91`, the lower reading controls and the project must re-enter remediation
- if a later self-check, user question, or score reassessment produces a lower-than-target estimate, treat that as invalidating the current ready state unless a true blocker explains why improvement cannot continue
- do not treat "already meets requirements" as equivalent to "already meets the high-achievement target"

Use [execution-gates.md](./references/execution-gates.md) as the default phase-gate model.

## Strict Mode

Use `strict mode` for high-risk projects where requirement drift, format drift, or optimistic self-checks would materially hurt the result.

Default triggers for `strict mode`:

- essay, paper, proposal, literature review, formal report, analyst-style course report, or other graded written submission
- source-backed or literature-backed work
- explicit formatting requirements, template, rubric, or official form
- target outcome depends on reaching a high score band such as `90+`
- native-file validation matters, such as real `.docx` or `.pptx` checking

Default rule:

- high-risk tasks enter `strict mode` automatically
- low-risk tasks may use a lighter path only when there is no meaningful risk of missing requirements or handing off a falsely qualified result

In `strict mode`, use this fixed chain:

1. bootstrap
2. reconstruct requirements
3. build `requirement-ledger.md`
3a. for graded academic or source-backed written submissions, build `rubric-ledger.md` from the brief, rubric, marking criteria, teacher feedback, required questions, and required format rules before drafting
3b. for graded academic or source-backed written submissions, identify the exact citation/referencing authority before drafting; inspect any local referencing guide, library style PDF, assessment appendix, or exemplar reference list and record the exact style variant and key examples in `requirement-ledger.md` or `rubric-ledger.md`
3c. for any school, university, course, workplace, client, journal, conference, or platform submission, identify exact local-rule sources before drafting or building; record source priority and extract rule-specific checks for word count, structure, format, template, academic integrity, submission mechanics, and any local terminology
4. assess feasibility
5. draft `approval-gate.md`
6. run `scripts/validate_requirement_lock.py`
7. get user confirmation
8. run `scripts/validate_requirement_lock.py --require-approved`
9. execute and keep `requirement-ledger.md`, `rubric-ledger.md`, `source-log.md`, `source-visual-inventory.md`, and `source-claim-audit.md` updated whenever they apply
10. run `scripts/validate_requirement_ledger.py --final`
11. run `scripts/validate_final_audit.py`
11a. for assignment-style document work, rerun `scripts/validate_final_audit.py --require-citation-micro-audit`
11b. for source-backed presentation work, verify `source-log.md` and `source-visual-inventory.md` before editing final references/source slides, run `scripts/validate_source_visual_inventory.py`, then rerun `scripts/validate_final_audit.py --require-presentation-source-audit`
12. for academic or source-backed graded written submissions, run `checkpro` or an equivalent academic-quality audit after the blocking validators pass; this audit must include rubric compliance, academic standards, source-claim integrity, prompt/rubric alignment, analytical section purpose, evidence quality, comparative synthesis, limitations or counterarguments, visual/table integration, citation-to-outcome specificity, empirical precision, theory/framework application, repetition control, conclusion sharpness, and citation support integrity when those dimensions are relevant to the assignment
12a. record rubric compliance in the `Rubric Compliance Audit` section of `final-audit.md`, then rerun `scripts/validate_final_audit.py --require-rubric-compliance-audit`
12b. record academic convention and formatting checks in the `Academic Standards Audit` section of `final-audit.md`, then rerun `scripts/validate_final_audit.py --require-academic-standards-audit`
12c. record source-claim checks in the `Source-Claim Integrity Audit` section of `final-audit.md`, then rerun `scripts/validate_final_audit.py --require-source-claim-audit`
12d. record the broader academic-quality result in the `Academic Quality Audit` section of `final-audit.md`, then rerun `scripts/validate_final_audit.py --require-academic-quality-audit`
12e. for assignment-style document work, run a manual citation-and-format micro-defect sweep after the academic-quality audit when academic citation quality is relevant; this sweep must use the exact local citation authority from step 3b rather than a generic Harvard/APA/MLA/etc. memory; otherwise run the route-specific final polish sweep
12e-2. run a local-rule compliance sweep against the exact local-rule sources from step 3c; this must check the final artifact, not only the draft notes, for word-count policy, visible structure, file format, template behavior, title/heading rules, academic-integrity/declaration requirements, required/forbidden content, submission package contents, and any local naming or export rules
12e-3. run a student-facing residue audit on the actual final artifact before handoff; this must inspect visible text, including headers, footers, captions, tables, comments, notes pages, and presentation scripts when present. If a scan script can read the file type, run `scripts/scan_student_facing_residue.py` on every final submission artifact. Record the result in the `Student-Facing Residue Audit` section of `final-audit.md`, then rerun `scripts/validate_final_audit.py --require-student-facing-residue-audit`
12f. for source-backed or visually polished presentation work, run a manual PPTPRO-quality sweep after the blocking validators pass: source-visual candidate inventory, selected/rejected visual rationale, image/source-structure provenance, references-vs-sources separation, visual enrichment/image plan, generated-image handling, rounded-corner consistency, human-facing source text, preview/render inspection, and script/slide correspondence when a script exists
13. hand off only if the validators, the academic-quality audit, the micro-defect sweep, and the completion gates pass

Do not skip or reorder these steps in `strict mode` unless the user explicitly overrides the process.

### Strict Mode Enforcement

In `strict mode`, mandatory steps are blocking gates, not preferences.

Default enforcement rules:

- if a required gate is skipped, unknown, stale, or only asserted narratively, the project is not ready
- if a validator, audit, source check, native-file check, or route-specific check fails, the next action is remediation, not handoff
- if a required check cannot run, record the reason as a limitation or blocker in `final-audit.md`; do not describe the project as clean
- if the missing check is material to submission correctness, the status must be `Blocked` or at most `Ready for review`, not `Ready to submit`
- every final readiness claim must be backed by evidence in `requirement-ledger.md`, `final-audit.md`, or the actual output file
- for academic or source-backed graded written work, `Academic Quality Audit` must explicitly cover the high-achievement dimensions instead of recording only a one-line pass
- for graded written work, `Rubric Compliance Audit`, `Academic Standards Audit`, and `Source-Claim Integrity Audit` must be explicit and evidence-bearing; a one-line "passed" statement is not enough
- for graded written work, a broad statement such as "Harvard style checked" is not enough when an institutional guide or style PDF is available; the final audit must name the exact guide used and state at least the key formatting rules checked, such as title quotation, journal punctuation, URL wording, access-date format, and reference ordering
- for school, university, course, workplace, client, journal, conference, or platform submissions, a broad statement such as "requirements checked" is not enough; the final audit must name the exact local sources used and state the concrete local-rule categories checked
- every explicit requirement must have a final status and evidence; broad statements such as "covered overall" do not satisfy the ledger
- if the agent notices after handoff drafting that a mandatory step was missed, it must withdraw the ready state internally, run the missing step, and repair any issue before responding
- process overrides must be explicit, narrow, and recorded in `approval-gate.md`; user convenience does not override truthfulness, source sufficiency, required templates, required formats, or native-file validation
- no final response may imply completion while the control files still contain pending, failed, incomplete, unresolved, or placeholder readiness fields

## Efficiency Gate

Load [efficiency-policy.md](./references/efficiency-policy.md) to keep token and tool usage proportional to the project.

Default rule:

- do not read everything
- do not reload unchanged material
- do not spend polish tokens before correctness and completeness

Efficiency is subordinate to correctness, truthfulness, and submission quality.

Use route-specific references and generated state files as the default working surface.

## Truthfulness Gate

Load [truthfulness-policy.md](./references/truthfulness-policy.md) for any task involving facts, citations, literature, references, real-world claims, validation, or completion reporting.

This rule is mandatory:

- do not invent facts
- do not invent sources
- do not invent validation results
- do not claim completion unless the project actually reached that state

If something cannot be verified, mark it as inference, unresolved, or blocked.

## Personal Identity Field Rule

For assignment cover pages, title pages, forms, headers, footers, or submission shells, personal identity fields are non-blocking by default.

Default rule:

- do not ask the user only to fill personal fields such as student name, student ID, candidate number, class, section, email, phone number, or similar submitter identifiers
- do not invent, infer, or fabricate these values
- if the field is blank in the provided template, keep it blank or preserve the empty placeholder
- if the field already contains user-provided content in the source materials, preserve it unless the user asks to remove it
- missing personal identity fields do not make the project `Cannot Complete Yet`
- record them as intentionally left blank or not applicable when they appear in an audit, checklist, or requirement ledger

This rule does not apply to assignment content facts, case names, source author names, participant data, project ownership references, institutional names, dates, or other information that materially affects the academic content or acceptance requirements.

For literature or research writing:

1. gather real sources first
1a. if the task is a scientific manuscript, paper-derived report, lab-style results write-up, journal-style section draft, or other evidence-led academic writing, identify the manuscript/source type, define the one-sentence central claim, list the evidence that supports it, and define the boundary where the claim stops before full drafting
2. prefer a source base centered on recent literature from roughly the last five years
3. prefer higher-impact, core-journal, guideline, review, or otherwise authoritative sources when available
4. record them in `runpro_workspace/10_analysis/source-log.md`
5. verify that the source base is sufficient
6. for source-backed written submissions, create or update `runpro_workspace/10_analysis/source-claim-audit.md` with the major factual, empirical, evaluative, and comparative claims
7. only then write the literature-backed content

For scientific-manuscript or paper-derived writing:

- choose the section logic from the task rather than defaulting to a generic essay shell; common section jobs are context/problem, gap, approach/design, evidence, interpretation, implication, and limitation
- calibrate claim verbs to evidence strength; do not let `show`, `demonstrate`, `suggest`, `indicate`, `may`, and `could` collapse into the same certainty level
- remove unsupported novelty, priority, universality, or causation claims instead of polishing them

For source-claim auditing:

- map each major claim to the source or sources that support it
- verify that the source supports the specific claim attached to it, not only the general topic
- preserve direction, magnitude, units, sample, method, population, date range, and conditions where those details affect interpretation
- tie broad claims such as `better`, `effective`, `significant`, `sustainable`, `high quality`, or `improved` to a measured or clearly defined outcome
- flag uncited, overbroad, decorative, mismatched, invented-looking, or not-assessable citations
- repair, narrow, cite, or remove claims that cannot be supported truthfully

Older sources are exceptions. Use them mainly when they are seminal, foundational, method-defining, guideline-level, or explicitly required.

For source-backed presentations:

1. build and verify `source-log.md` first
2. create `runpro_workspace/10_analysis/source-visual-inventory.md` before slide drafting; record real source visuals, source structures, traceable contextual images, possible generated visuals, and diagram/source-structure substitutes as candidate visuals
3. actively inspect the major sources for relevant real source visuals and source structures before deciding the deck can be image-free: book/report covers, official metadata, tables of contents, chapter/case structures, field sites, methods, original data figures, article screenshots, media-event facts, or other evidence objects
4. for each visual candidate, record source/search path, visual type, URL/file path or provenance notes, evidence/slide role, selected or rejected status, and inclusion/exclusion reason
5. run `scripts/validate_source_visual_inventory.py runpro_workspace/10_analysis/source-visual-inventory.md` before building the final deck; if no visual is selected, only rerun with `--allow-zero-selected-with-rationale` when the inventory includes a strong `Zero-Image Rationale` explaining what was searched, why candidates were rejected, and what diagram/matrix/source-structure visual system replaces them
6. after source-native visuals are covered, make a visual enrichment plan for text-heavy decks: use relevant supporting photos, maps, contextual images, generated illustrations, diagrams, object shots, or compact visual systems to improve clarity and display power; use only traceable, context-relevant, high-quality external images and record provenance
6a. if the user explicitly asks to `找图`, `加图`, `图片`, `真实图片`, `direct images`, or otherwise criticizes missing images, self-created source cards, editable diagrams, tables, charts, icon clusters, and source-structure substitutes do not satisfy that direct-image requirement by themselves. The agent must actively search for and insert at least one traceable real photo, official/product image, source screenshot, report/page image, map, or other externally sourced visual when the topic has any usable image source. If no such real/traceable image exists, the inventory must state exactly where it was searched and why each real-image candidate was rejected before falling back to generated or diagrammatic visuals.
7. when no real or traceable image fits and a custom content visual would make a slide clearer, use Codex/ChatGPT's built-in image generation with the current latest built-in image model/tool exposed by the environment; record generated-image provenance and never use generated images as source evidence, real-event proof, or substitutes for data/source figures
8. only then write or revise the final deck's references or sources slides
9. do not repair the final deck first and backfill the source log or source-visual inventory later
10. if the deck contains both scholarly references and data, media, website, image, generated-image, or source-entry-point provenance, keep them clearly separated instead of merging them into one pseudo-reference list unless the assignment explicitly requires a combined format
11. avoid source-backed decks that are only repeated text-card summaries; the final deck must include at least one source-native visual, traceable contextual image, generated content visual, original figure/table, source-structure page, or purpose-built diagram/matrix unless the zero-image rationale has been validated
12. a zero-picture PPTX is not automatically acceptable; it can be ready only if `source-visual-inventory.md` proves visual candidates were searched and rejected and the deck uses a documented non-picture visual substitute such as a matrix, source-structure diagram, map-like schematic, or evidence-flow visual
13. keep source logs, final audits, provenance records, and other workflow bookkeeping out of the visible PPT and delivery script; use concise human-facing source labels or a normal `Sources used` slide instead of sentences like `Full source provenance and image credits are recorded in the project source log`
14. for scientific paper, preprint, thesis-seminar, journal-club, or other figure-led academic decks, classify the source type before slide drafting and choose the matching narrative arc: question-to-evidence, problem-to-solution, workflow-to-validation, design-to-inference, property-to-mechanism, or evidence-map
15. map each selected figure or table to a slide claim before layout; decide whether the original visual should stay whole, be cropped, or be split across slides
16. use conclusion-style slide titles on most scientific content slides and keep result slides figure-first; avoid generic labels such as `Results`, `Method`, or `Figure 3`
17. if a slide uses multiple figure panels, each panel must have a distinct analytical role such as overview, comparison/deviation, validation, or relationship/mechanism; do not keep redundant panels that answer the same question unless the repetition is clearly useful

Load [academic-format-policy.md](./references/academic-format-policy.md) for essays, papers, literature reviews, citation-backed reports, and source-backed presentations.

## Final Delivery Hygiene

Final artifacts must read like finished submissions, not working files.

This rule is mandatory for any deliverable that will be submitted, presented, exported, or handed off:

- do not leave workflow status text in the final artifact
- do not leave engineering or build remarks in the final artifact
- do not leave workspace, file-management, or editing-process notes in the final artifact
- do not leave comments about matching, syncing, rebuilding, or where files are saved in the final artifact
- do not leave AI/tool/prompt/process language in the final artifact, including text that describes how the writing avoids AI similarity, default ChatGPT output, classmates' work, previous assignments, or internal wording strategy
- do not leave internal audit vocabulary in the final artifact unless it is explicitly part of the user's requested deliverable; examples include `source log`, `final audit`, `requirement ledger`, `rubric ledger`, `runpro_workspace`, `replacewords`, `RunPro`, `Codex`, `ChatGPT`, `prompt`, and `AI-generated`
- do not leave student-visible sentences written from the assistant's process perspective, such as `I will avoid using the same sort of words/phrasing...`, `this is not a generic essay`, `not a general essay`, `the bite is around...`, or references to palliative care/end-of-life work when that is only a prior-task avoidance rule
- for written deliverables, reserve bold styling for the title or heading hierarchy unless the assignment or template explicitly requires another use
- do not use bold inside body paragraphs, bullet text, table body text, captions, or other running text merely to add emphasis

Examples of text that must not appear in final deliverables:

- `current script matched`
- `latest PPT`
- `submission folder`
- `workspace`
- `build script`
- `for editing and rehearsal`
- `speaker notes were removed`
- `current PPT build`
- `I will avoid using the same sort of words/phrasing`
- `previous assignment`
- `ChatGPT`
- `AI-generated`
- `source log`
- `final audit`
- `requirement ledger`
- `runpro_workspace`

Before handoff:

1. scan the visible content of the final artifact for process-facing language
2. remove or rewrite any internal note so it becomes real user-facing content, or delete it entirely
3. for written deliverables, remove any non-required bold emphasis from body text and keep bold only where the heading or title structure requires it
4. if the artifact is produced by script, add a denylist or validation check so banned wording cannot silently pass through
5. verify the exported final file itself, not only the source text
6. after any late text replacement, manual polishing, `$replacewords` pass, export, or template reassembly, rerun the student-facing residue audit on the final artifact itself
7. if the audit finds internal residue, do not hand off; repair the visible artifact, re-export if needed, rerun the scan, and record the clean result in `final-audit.md`

## Student-Facing Residue Gate

This is a blocking gate for every final artifact that a student, client, marker, audience, or external reviewer will see.

The final artifact must not contain:

- internal workflow notes, planning notes, status notes, or implementation commentary
- assistant/tool traces such as `ChatGPT`, `Codex`, `RunPro`, `replacewords`, `prompt`, `AI-generated`, `LLM`, or model/process references
- anti-AI, anti-similarity, or wording-strategy explanations, including comments about avoiding the same article, avoiding classmates' phrasing, reducing AI detection, or matching a previous style
- prior-project or prior-assignment residue that is not part of the current assignment content
- file paths, workspace paths, helper filenames, export/build notes, or audit file names
- hidden template prompts, editor notes, comments, notes-page text, captions, table text, headers, or footers that expose the production process

Required workflow:

1. Extract visible text from the final artifact itself, not only from draft markdown or source notes.
2. Inspect all available text surfaces for the artifact type: DOCX body/header/footer/footnote/comment text, PPTX slide/notes/comment text, PDF extracted text, captions, tables, and scripts.
3. Use `scripts/scan_student_facing_residue.py` where the file type is supported, then do a manual sanity read for high-risk academic or client-facing artifacts.
4. Treat every hit as a handoff blocker unless it is clearly legitimate content requested by the assignment or user.
5. Rewrite process-language into normal subject-matter prose or remove it entirely. Do not disguise the process note by making it slightly less direct.
6. Rerun the scan after repairs and after any later replacement/export step.
7. Record the file(s) checked, surfaces checked, findings, repair actions, and final pass/fail result in `Student-Facing Residue Audit` inside `final-audit.md`.

The audit wording must be evidence-bearing. A one-line statement such as `checked and clean` is not enough for strict mode.

## Self-Optimization Loop

Load [remediation-loop.md](./references/remediation-loop.md) whenever validation fails, the output is incomplete, or a better path becomes available during execution.

Default rule:

- do not stop at problem reporting
- diagnose the issue
- propose the repair options
- choose the most reliable low-cost fix
- apply the fix
- re-run the relevant validation
- continue until the project passes or a true external blocker remains

If missing material can be reasonably supplemented, supplement it.

If a failed check is fixable inside the workspace, fix it instead of handing the failure back to the user.

## Collaboration Framework

Load [collaboration-framework.md](./references/collaboration-framework.md) when you need the higher-level reasoning pattern behind this skill.

Default collaboration stance:

1. define the end state first
2. inventory the current materials
3. verify facts and boundaries before committing to a path
4. perform a gap analysis
5. decide whether the current folder is sufficient to complete the work
6. lock the exact requirements with the user before execution
7. choose a primary path, a backup path, and a contingency path that still satisfies all locked requirements
8. build a runnable first version
9. validate continuously
10. iterate from usable to shippable
11. close the delivery properly
12. preserve the method as a reusable template

This is a reference input, not a constraint. Optimize for fewer turns, higher automation, and faster convergence.

## When To Use

Use this skill for requests like:

- "我把资料放进项目文件夹，你帮我自动做完"
- "读取这个项目目录里的图片和文档，判断要交付什么"
- "根据项目原始资料先出计划，再一步一步完成"
- "把这个项目推进到可提交状态"
- "最后检查是否都完成了，并给我总结反馈"

Do not use this skill for one-off note cleanup, pure translation, or simple content summarization when no project execution is expected.

## Core Operating Model

Treat the project folder as the source of truth.

The default loop is:

1. bootstrap the project workspace
2. infer the project goal and deliverable
3. determine whether the current materials are sufficient to complete the project
4. lock the exact confirmed requirements and a feasible execution path
5. build a runnable first version
6. iterate until requirement coverage is acceptable
7. validate and package the final delivery
8. produce a final delivery summary

If the folder contains both raw inputs and earlier outputs, prefer the latest explicit requirements and keep older drafts only as references.

## Expected Project Root

Load [project-folder-layout.md](./references/project-folder-layout.md) when setting up or normalizing the project directory.

Strong default behavior:

- accept a flat project folder if that is what the user provides
- scan the entire folder first
- if state folders are missing, create a minimal working structure
- keep the user's original input files untouched

If the user did not provide a clean kickoff note, create one from the source materials using [project-start-template.md](./references/project-start-template.md).

## Zero-Friction Invocation

The preferred invocation is minimal:

- user points to a project folder
- user says to run `$runpro`

Optional kickoff details help, but are not required.

The skill should default to:

1. run `scripts/bootstrap_project.py`
2. inspect the generated inventory and state files
3. read the most relevant source material
4. prepare a feasibility verdict
5. prepare a strict requirement lock
6. wait for user confirmation before execution

## Standard Project State Files

Load [project-state-files.md](./references/project-state-files.md) and maintain these files unless the project already has a better equivalent:

All generated files should live under `runpro_workspace/` by default.

Keep the clean handoff folder at `runpro_workspace/submission/` so the user can open the runpro workspace and see the submission folder immediately without drilling into deeper delivery layers.

`runpro_workspace/submission/` is only for the actual submission package.

Do not place drafts, markdown working files, template reference files, style exemplars, audits, notes, helper exports, or duplicate variants there unless the assignment explicitly requires them in the final submission package.

For written deliverables, if the assignment does not explicitly require another final format, default the final submission artifact to `Word/.docx`.

- `runpro_workspace/10_analysis/project-inventory.md`
- `runpro_workspace/10_analysis/project-intake.md`
- `runpro_workspace/10_analysis/project-brief.md`
- `runpro_workspace/10_analysis/requirement-ledger.md`
- `runpro_workspace/10_analysis/rubric-ledger.md`
- `runpro_workspace/10_analysis/feasibility-check.md`
- `runpro_workspace/10_analysis/project-routing.md`
- `runpro_workspace/10_analysis/route-playbook.md`
- `runpro_workspace/10_analysis/source-log.md`
- `runpro_workspace/10_analysis/source-visual-inventory.md`
- `runpro_workspace/10_analysis/source-claim-audit.md`
- `runpro_workspace/10_analysis/approval-gate.md`
- `runpro_workspace/10_analysis/execution-plan.md`
- `runpro_workspace/10_analysis/delivery-checklist.md`
- `runpro_workspace/10_analysis/final-audit.md`
- `runpro_workspace/10_analysis/remediation-log.md`
- `runpro_workspace/10_analysis/final-summary.md`

These files are the control surface for the project:

- `project-inventory.md`: normalized file inventory and priority candidates
- `project-intake.md`: normalized project startup information
- `project-brief.md`: what the project actually is
- `requirement-ledger.md`: item-by-item traceability for explicit requirements, prohibitions, and format rules from source files
- `rubric-ledger.md`: criterion-by-criterion grading alignment for graded academic or source-backed written submissions
- `feasibility-check.md`: whether the current folder is sufficient to complete the work and what is missing if not
- `project-routing.md`: inferred project type, confidence, branch choice, and routing evidence
- `route-playbook.md`: route-specific next actions, validations, and exit criteria
- `source-log.md`: real sources used for fact-backed or literature-backed work
- `source-visual-inventory.md`: candidate source visuals, supporting images, generated visuals, and diagram/source-structure substitutes for source-backed presentations
- `source-claim-audit.md`: major claim to source-support mapping for source-backed writing
- `approval-gate.md`: strict pre-execution requirement lock, approval status, and drift controls
- `execution-plan.md`: what will be done and in what order
- `delivery-checklist.md`: what must be true before the project is considered complete
- `final-audit.md`: detailed end-of-project self-check, unresolved items, and completion decision
- `remediation-log.md`: what failed, what was tried, what fixed it, and what remains blocked
- `final-summary.md`: internal completion note kept outside the clean submission folder

## Intake Workflow

### 1. Bootstrap The Workspace

Run `scripts/bootstrap_project.py` against the project root first.

Bootstrap responsibilities:

- create missing working folders
- generate `project-inventory.md`
- generate `project-routing.md`
- generate `route-playbook.md`
- generate missing state files
- normalize the project into an executable workspace

### 2. Define The End State

Before detailed execution, identify:

- project goal
- final deliverable
- deadline
- evaluation standard

If the user already provided these clearly, normalize them into `project-intake.md`.

If not, infer the most likely answers from the folder and mark uncertainties explicitly.

### 3. Inventory The Folder

Use the generated `project-inventory.md` first. Re-run `scripts/project_inventory.py` only if the project changes materially during execution.

Use the inventory to identify:

- candidate requirement documents
- conversation records
- screenshots and visual references
- previous drafts
- likely final output files
- code or asset folders

Then read the most relevant files directly. Do not read every file blindly.

### 4. Reconstruct The Project

Use [intake-schema.md](./references/intake-schema.md) to normalize the project.

At minimum, determine:

- project goal
- deliverable type
- expected genre and writing register
- expected depth and quality tier implied by the course, template, or sample
- target audience or reviewer
- hard requirements
- required structure, sequence, or section pattern
- required template, form, or submission shell
- explicit must-do items
- explicit must-not-do items
- topic-selection constraints, including differentiation goals, default-topic collision risk, classmate overlap risk, teacher-example overlap, and previous-submission overlap
- soft preferences
- missing information
- completion standard
- whether the project should run in `strict mode`

When missing information consists only of personal identity fields such as student name, student ID, candidate number, class, section, email, or phone number, do not stop to ask for it. Leave those fields blank by default and continue.

If the project type is still unclear after scanning, state the ambiguity in `project-brief.md` and choose the most conservative workable interpretation.

Before moving on, create `runpro_workspace/10_analysis/requirement-ledger.md`.

Requirement-ledger rules:

- create one ledger item per explicit requirement-bearing instruction, not one summary per file
- include the source file, screenshot, message, or template reference for each item
- include content, structure, format, prohibition, and emphasis requirements
- do not collapse detailed assignment instructions into a generic paraphrase if the underlying files are more specific

If the project meets the default `strict mode` triggers, mark that explicitly in `project-brief.md` and continue under the fixed chain.

For graded academic, source-backed written, formal report, literature review, proposal, or dissertation-style work, create `runpro_workspace/10_analysis/rubric-ledger.md` before drafting. Build it from the assignment brief, rubric, marking criteria, teacher feedback, required questions, required format rules, and template obligations.

Rubric-ledger rules:

- create one item per rubric criterion, required question, required sub-part, actionable teacher-feedback point, or format criterion
- include source, weight or importance, expected evidence, draft location, status, evidence, and repair action
- use final statuses `pass`, `partial`, `fail`, or `not assessable`
- do not treat a broad section as satisfying a criterion unless the answer is visible and direct
- do not mark high-score readiness while a central or high-weight rubric item is `partial`, `fail`, or `not assessable`
- if no rubric exists, build a `rubric-inferred` ledger from the brief and genre, and record that limitation

### 5. Assess Feasibility

Before execution, determine whether the current folder contents are sufficient to complete the project truthfully and to the required standard.

Record the result in `runpro_workspace/10_analysis/feasibility-check.md`.

The feasibility check should answer:

- can the project be completed with the current materials
- whether the current materials are sufficient to realistically target the `90+` score band
- which required inputs are already present
- which required inputs are missing
- which gaps are recoverable inside the workspace
- which gaps require user or external supplementation
- what would be needed to continue if the answer is no
- whether the current requirement ledger appears complete enough to trust for execution
- whether `strict mode` is required for this project and why

Use one of these verdicts:

- `Can Complete`
- `Can Complete With Recoverable Gaps`
- `Cannot Complete Yet`

Rules:

- do not claim `Can Complete` if required source material, official templates, essential data, or mandatory assignment instructions are still missing
- do not claim the `90+` target is realistically reachable if the rubric, template, source base, or core evidence is too weak
- do not treat a reduced-scope version as valid if the assignment expects all parts to be completed
- missing personal identity fields such as student name, student ID, candidate number, class, section, email, or phone number are not blockers and should not be requested as a standalone confirmation step
- if the current materials are not enough, say so explicitly
- if the missing items can be safely created or supplemented inside the workspace, list them as recoverable gaps
- if the missing items must come from the user, an institution, or an external system, stop and request exactly those items before execution

### 6. Route The Project

Load [routing-matrix.md](./references/routing-matrix.md) and use `scripts/classify_project.py` to infer the most likely project branch.

Primary branches:

- adaptive
- document
- presentation
- code
- data
- mixed

The route decision should be recorded in `project-routing.md` with:

- primary route
- secondary route if relevant
- confidence
- evidence
- default first working version
- route-specific validations

Then generate `route-playbook.md` so the next execution step is explicit instead of implicit.

Treat routing as a working hypothesis, not a rigid classification. If execution reveals a better route, switch early.

### 7. Verify Facts And Boundaries

Before execution, check:

- which requirements are confirmed versus inferred
- which template, sample, or shell implies the expected genre, depth, and quality bar
- which structure, section order, and methodology emphasis are mandatory
- which template, form, or file format is mandatory
- which older drafts are references only and must not be reused directly
- which files or systems can be changed
- which tools or platforms are available
- which constraints are hard blockers
- whether the factual basis is sufficient for a truthful result

Do not quietly treat guesses as facts.

Do not quietly replace an exact requirement with a near-equivalent interpretation.

### 8. Lock An Execution Path

Turn the reconstructed project into an actionable plan and choose the safest path that can still satisfy all locked requirements.

The plan should be phase-based and include:

- what will be produced
- in what order
- what files will be touched
- what validations are required
- what blockers would stop completion

The plan should explicitly include:

- primary path
- backup path
- contingency path that still satisfies all locked requirements
- high-achievement path to maximize the chance of a `90+` outcome when feasible

If a fast, reliable path exists, prefer it over the user's likely manual process only when it still respects the exact confirmed requirements, expected genre, and template-derived quality bar.

The contingency path is not allowed to downgrade:

- a formal report into a memo-like note
- a template-driven submission into a generic freeform document
- a course-context quality bar into a merely readable but underdeveloped draft
- a complete assignment into a partial one with missing required sections or tasks

Do not begin execution yet. Move to the feasibility check and requirement lock first.

### 9. Requirement Lock

Before execution, prepare a strict requirement lock from:

- `project-intake.md`
- `project-brief.md`
- `requirement-ledger.md`
- `feasibility-check.md`
- `project-routing.md`
- `route-playbook.md`

Record it in `runpro_workspace/10_analysis/approval-gate.md`.

The requirement lock should include:

- confirmed project goal
- confirmed final deliverable
- expected genre and writing register
- expected depth and quality tier
- target quality threshold
- confirmation that all required assignment content must be completed
- required structure or sections
- required format, template, or form
- explicit assignment formatting requirements when they are provided
- default formatting fallback when the materials do not specify font or layout rules
- non-negotiable requirements
- explicitly forbidden moves or substitutions
- accepted inferences
- personal identity fields that will be left blank by default
- open questions needing confirmation
- locked execution direction
- approval status

Pause here and ask the user to confirm or correct the scope.

The user-facing confirmation message at this pause must be written in Chinese by default, even if the internal state files are in English.

This Chinese confirmation message should concisely include:

- 我理解的项目目标
- 最终交付物
- 已锁定的核心要求
- 计划执行路径
- 需要用户确认或补充的问题
- 明确的确认请求，例如 `请确认以上范围和计划是否可以开始执行；如果有偏差，请直接指出需要修改的地方。`

Do not include missing student name, student ID, candidate number, class, section, email, or phone number as a confirmation question. If these fields appear in the template and are not already filled, state briefly that they will be left blank by default only if necessary.

Do not present this pre-execution review request only in English unless the user explicitly asks for English.

Before asking for confirmation, run `scripts/validate_requirement_lock.py` against the drafted requirement lock to ensure the critical fields are actually populated.

Only after explicit user confirmation should execution begin.

After the user confirms, treat the requirement lock as binding.

After confirmation, re-run `scripts/validate_requirement_lock.py --require-approved` before deep execution.

If the project is in `strict mode`, do not begin deep execution until both validations pass.

Do not:

- change the required section structure on your own
- collapse a formal report into a short memo-like artifact
- translate "not too academic" into casual, underdeveloped, or note-like prose when the task still expects a formal report
- soften a required methodology emphasis into a generic discussion
- swap in a different template, form, or shell because it seems close enough
- reuse an old draft that the user or materials ruled out
- omit a hard requirement because another version seems more natural

If execution reveals that the confirmed requirement lock cannot be followed exactly:

- stop
- explain the blocker precisely
- ask for re-approval or correction

Do not improvise a substitute for a missing required form or template unless the user explicitly approves that substitution.

If a required template or sample exists, extract its structural and style signals before drafting the body. Do not draft the content first and retrofit the template later unless the user explicitly accepts that fallback.

For template-bound partial edits, lock the full artifact strategy before editing:

- identify the complete source artifact, its page/slide/section count, and the exact user-owned edit range
- identify the preserved range that must stay unchanged, such as teammate sections, appendix pages, official template pages, or locked instructor content
- default to delivering the full artifact with preserved sections intact unless the user explicitly asks for an excerpt-only deliverable
- if only one range is revised, build or audit that range separately when useful, but assemble the final handoff so unedited ranges are not silently deleted
- when a template exists, use its palette, typography, spacing logic, and visual tone as the starting point; redesign within the template direction instead of replacing it with a generic new design
- record the edit range, preserved range, and final assembly strategy in the requirement ledger or approval gate

If the assignment provides explicit formatting rules, lock them before drafting, write under those rules from the start, and run a final whole-document formatting pass after the content is complete.

For written deliverables, unless the assignment or template explicitly says otherwise, lock this styling rule as part of the format requirements:

- bold is allowed for the document title and heading hierarchy
- bold is not allowed for mid-paragraph emphasis, list-item emphasis, caption emphasis, or other body-text emphasis
- report tables default to black-and-white three-line table styling
- inserted project flowcharts or process diagrams default to black-and-white styling, with black lines and text on a white background rather than colored nodes or arrows

## Execution Workflow

### 10. Route To The Right Domain

Once the project type is clear, continue with the most relevant execution path:

- documents, reports, proposals, PRDs
- slide decks or presentations
- code or app work
- design assets
- spreadsheets or structured data work

Use the best available specialized skill, tool, or plugin for that domain after intake. This skill is the orchestrator, not the endpoint.

Load the branch-specific reference that matches the chosen route:

- [adaptive-branch.md](./references/adaptive-branch.md)
- [document-branch.md](./references/document-branch.md)
- [presentation-branch.md](./references/presentation-branch.md)
- [code-branch.md](./references/code-branch.md)
- [data-branch.md](./references/data-branch.md)
- [mixed-branch.md](./references/mixed-branch.md)

Route-specific expectations:

- `adaptive`: optimize around the real end state and define custom acceptance checks when needed
- `document`: prioritize structure, requirement coverage, and outward-facing clarity
- `presentation`: prioritize slide scaffolding, layout viability, visual validation, and use of specialized presentation skills. When editable PPT or PPTX output is required, default to the `PowerPoint` skill unless the task explicitly calls for a different presentation workflow.
- For visually polished PPT/PPTX work, especially when the user asks for beauty, design quality, repeated checking, or a non-generic deck, use `$pptpro` as the strict presentation design workflow and source of truth before final handoff. Do not apply a weaker local Runpro PPT standard. Load its design system and slide recipes, assign every revised slide a recipe, avoid serif fonts and beige/cream AI-looking backgrounds unless explicitly required or already dictated by the provided template, use softer rounded rectangles for new cards/callouts/panels unless the template requires square geometry, use concept/flow/case/layout recipes instead of generic bullets, avoid repeated same-structure content slides, create and validate `source-visual-inventory.md` for source-backed decks, add real source visuals/structures for book/report/source-led decks when available, create a visual enrichment plan for text-heavy decks, use relevant supporting images or generated illustrations when they would make the deck more concrete or visually powerful, use Codex/ChatGPT built-in image generation with the current latest image tool/model for custom content visuals when no real or traceable image fits, keep source-log/audit/provenance bookkeeping out of visible slides and scripts, make media slides look like case/event analysis rather than ordinary text cards, and for scientific paper or journal-club decks also classify the source type, choose a figure-led argument arc, use conclusion-style titles, and avoid redundant multi-panel evidence. Add script-to-slide markers, render previews, manually inspect them, repair overflow or confusing design marks, and run `pptpro_audit.py --render --strict` before handoff.
- For template-bound or partial-scope presentations, apply `$pptpro` to the revised range while preserving the rest of the deck. The final PPTX should normally remain the complete deck. If preserved slides are image-only or otherwise not compatible with strict audit checks, create an audit-only copy for the revised range, run PPTPRO strict audit on that copy, then render and inspect the final full deck to verify assembly, slide order, and preserved pages.
- `code`: prioritize a runnable or buildable path, core functionality, and technical validation
- `data`: prioritize reproducible transformations, sheet or pipeline correctness, and summary outputs
- `mixed`: choose a primary route based on the final deliverable, then support it with secondary assets

### 11. Build A Runnable First Version

Do not aim for the final polished output first.

Default progression:

1. skeleton version
2. usable version
3. optimized version
4. delivery version

The first version should prove that the project can run, render, compile, read, or otherwise function in its core form.

### 12. Execute Iteratively

Drive the project in short loops:

1. update the plan
2. do the next concrete step
3. record progress in the checklist
4. update the requirement ledger for any item whose status changed
5. validate the produced output
6. if validation fails, enter the remediation loop immediately
7. continue until the deliverable is submission-ready or genuinely blocked

Default to action. Do not keep re-planning after the path is clear.

### 13. Handle Problems Without Stalling

When a blocker appears, switch immediately into this form:

- what the problem is
- why it happened
- which options are available
- which option is recommended

Do not freeze the project unless no reasonable path remains.

If the problem is internally fixable:

- try the best repair
- validate again
- record the outcome in `remediation-log.md`

Only escalate to the user after the repair loop fails or an external dependency blocks progress.

### 14. Track Assumptions And Gaps

If information is missing:

- make a reasonable assumption when the risk is low
- record it explicitly
- continue execution

If the missing detail would materially change the project outcome, change the locked requirements, force fabricated factual content, or require substituting a required structure, template, or form, stop and ask a focused question or mark the task blocked.

### 15. Run A Detailed Completion Audit

Before handoff, run a detailed completion audit against:

- the approved requirement lock
- the requirement ledger
- the delivery checklist
- route-specific validation requirements
- actual output files

Record the audit in `runpro_workspace/10_analysis/final-audit.md`.

The completion audit must answer, item by item:

- what requirement was checked
- whether it passed
- what evidence supports that verdict
- what remains incomplete
- what repair action is required next

The completion audit should also produce:

- a rubric-compliance audit with pass/partial/fail/not-assessable results for every central rubric, brief, required-question, teacher-feedback, and format criterion
- an academic-standards audit covering citation style, in-text/reference matching, reference metadata, formatting, figures/tables, paragraph logic, headings, word count, appendices, and academic register where applicable
- a source-claim integrity audit for major factual, empirical, evaluative, and comparative claims in source-backed writing
- a student-facing residue audit covering visible final-artifact text, internal workflow/tool/process language, previous-assignment residue, AI/prompt references, file paths, and repair/recheck evidence
- a requirement-weighted internal quality score out of `100`
- an estimated score-band judgment such as `below 80`, `80-89`, or `90+ plausible`
- the reasons the submission is below the `90+` target if it is below that band
- the next repairs most likely to improve the estimated score band

For high-achievement projects, the estimated score band must be the most conservative credible current band. If the evidence supports both a lower and a higher band, record the lower band as controlling, list the upside case separately in the reasoning if needed, and continue remediation until the controlling band reaches the target or a true blocker remains.

Every explicit requirement from `requirement-ledger.md` must appear in the final audit with an explicit verdict. Do not replace this with a broad summary like "most requirements satisfied."

For assignment-style document work, the completion audit must include one explicit post-validation micro-defect sweep after the deliverable already appears handoff-ready. This sweep is for non-blocking but still grade-relevant defects that broad validators often miss, such as:

- in-text and reference-list mismatches
- reference-list ordering or alphabetization defects
- author-name fidelity issues, including missing diacritics or incorrect initials
- weak handling of no-author, unpublished, or local course materials
- filename-like surrogate citations that should be title-based or otherwise style-correct

If this sweep finds a fixable issue, do not hand off yet. Repair it, recheck it, and only then continue to handoff.

If any required item is incomplete, failed, inconsistent, or weak enough to threaten acceptance:

- do not hand off
- return to the remediation loop
- continue until the item passes or a true blocker remains

Do not treat "mostly done" as complete.

Do not hand off as high-quality completion if required assignment content is still incomplete.

Do not hand off as `90+`-target quality if the audit still judges the submission below that band while fixable improvements remain.

## Completion Workflow

Load [final-checklist.md](./references/final-checklist.md) before declaring the project done.

The project is only complete when:

- the required deliverable exists
- `runpro_workspace/submission/` contains only the project-required submission contents
- for written deliverables with no explicitly required final format, the primary submission artifact is `.docx`
- markdown, template-reference, style-reference, draft, and duplicate helper files are kept out of `runpro_workspace/submission/` unless explicitly required
- hard requirements are covered
- all required assignment parts are completed unless a true blocker is documented
- the initial feasibility verdict has been satisfied, or any unresolved item is documented as a true blocker
- the final output conforms to the approved requirement lock
- every explicit item in `requirement-ledger.md` is marked `satisfied`, `blocked`, or `not applicable`
- personal identity fields such as student name or student ID may be left blank by default and do not block handoff unless the user explicitly asked to fill them
- any explicit assignment formatting rules were followed during drafting and rechecked on the final document after content completion
- for written deliverables, any non-required bold emphasis has been removed from body text and bold remains only in the title or heading hierarchy unless the assignment explicitly requires otherwise
- for final deliverables, the student-facing residue audit has inspected the actual final artifact and found no internal workflow, tool, prompt, AI-similarity, prior-assignment, file-path, helper-filename, or audit-language residue
- for written deliverables, report tables use black-and-white three-line styling unless the assignment or template explicitly requires another table style
- for written deliverables, embedded figures or charts do not contain duplicate internal chart titles when the document already provides a figure caption/title; axis labels, legends, units, and necessary data annotations remain inside the figure
- for written deliverables, figures, charts, and diagrams look academically polished and visually balanced: controlled whitespace, readable labels, restrained colors, consistent typography, no chart junk, no clipped labels, and no off-center visual weight
- for written deliverables, inserted project flowcharts or process diagrams use black-and-white styling unless the assignment or template explicitly requires another visual rule
- for template-bound or partial-scope presentation work, the final deck preserves unedited sections unless an excerpt-only deliverable was explicitly locked
- for template-bound or partial-scope presentation work, the final audit distinguishes the revised range audit from the full-deck render/assembly check
- the final audit judges the submission plausibly in the target score band or a true blocker explains why it cannot
- open blockers are either resolved or explicitly documented
- key outputs have been checked
- the detailed completion audit has been recorded
- the final summary is written
- the project has passed all applicable execution gates
- all fixable validation failures have been remediated
- any assignment-style document micro-defects found after blocking validation have been remediated and rechecked
- no factual claim that required verification is left unsupported

Before declaring completion, run:

- `scripts/validate_requirement_ledger.py --final`
- `scripts/validate_final_audit.py`
- for graded academic written submissions, `scripts/validate_final_audit.py --require-rubric-compliance-audit`
- for assignment-style document work, `scripts/validate_final_audit.py --require-academic-standards-audit`
- for source-backed written submissions, `scripts/validate_final_audit.py --require-source-claim-audit`
- for academic or source-backed graded written submissions, `scripts/validate_final_audit.py --require-academic-quality-audit`
- for assignment-style document work, `scripts/validate_final_audit.py --require-citation-micro-audit`
- for any external-facing final artifact supported by the scanner, `scripts/scan_student_facing_residue.py <final artifact path>` for each final artifact
- for any final artifact that will be submitted, presented, exported, or handed off, `scripts/validate_final_audit.py --require-student-facing-residue-audit`
- when the target threshold is `90+` or equivalent high-achievement wording, `scripts/validate_final_audit.py --require-90-plus`

If the project is in `strict mode`, these validations are mandatory and handoff must stop when they fail.

Do not mark the project complete just because a draft exists.

If the completion audit finds an unfinished or non-compliant item, continue working until it is finished or a true blocker is documented.

## Final Response Contract

At the end, default to result-only output.

Provide:

1. the finished deliverable or the path to the finished deliverable
2. only the minimum completion note needed to use the result

Do not repeat the planning narrative unless:

- the user asks for it
- something remains blocked
- a limitation materially affects the result

Lead with completion status:

- `Ready to submit`
- `Ready for review`
- `Blocked`

Status language must be precise:

- do not say `no issues`, `没有问题`, or equivalent unless both blocking checks and the final micro-defect sweep found no remaining fixable problems
- if only the blocking checks are clean, say `no blocking issues found` rather than implying the work is defect-free
- if minor issues were found and fixed during the final sweep, say that explicitly
- if minor but non-blocking issues remain, do not imply clean completion; report them and use the appropriate status instead

For high-achievement projects:

- do not ask the user whether to continue optimization merely because a later reassessment says the work is still below the target band; that reassessment is itself a remediation trigger
- if a later answer or self-check lowers the estimate below the locked target and no true blocker exists, withdraw the ready state internally, update the audit/remediation state, and continue working automatically unless the user explicitly asks to stop or switch to review mode

## Invocation

Direct invocation should use the skill name explicitly:

- `用 $runpro 处理 /absolute/path/to/project`
- `Use $runpro on /absolute/path/to/project and drive it to a handoff-ready state`

If the project path is already obvious from context, the shortest usable form is:

- `$runpro 处理这个项目目录`

## Autonomy Rules

- Prefer executing to completion over handing back a plan.
- Preserve user source files.
- Keep intermediate state in the project folder so work is inspectable.
- Make uncertainty visible instead of hiding it.
- If the user gives a separate summary of working style or communication preferences, merge that into the operating approach but keep the project folder as the factual source of truth.
- Reuse the same kickoff, validation, and handoff pattern across projects unless the user overrides it.
- Prefer automation and inference over requiring the user to fill structured templates manually.
- If a result is not yet qualified, keep improving it until it is qualified or a real blocker prevents completion.
- Always pause for user confirmation after scope reconstruction and before execution starts.
- Never silently replace an exact template, form, required structure, or prohibited reuse rule with a near-equivalent alternative. Re-lock the scope with the user first.
