# Document Branch

Use this branch when the main deliverable is a written artifact.

Load `truthfulness-policy.md` and `academic-format-policy.md` whenever the document depends on real-world facts, citations, literature, or assignment formatting rules.

## Target Outputs

Typical outputs:

- proposal
- report
- PRD
- requirements document
- brief
- submission draft

## First Working Version

The first working version should already contain:

- the full section structure
- real content in every major section
- explicit placeholders only where a true unknown remains

Do not start with a one-paragraph summary if the final deliverable is a full document.

## Execution Priorities

1. lock the intended audience and format
2. lock the expected genre, register, and depth
3. extract structure and formatting signals from any required template or sample
4. lock any assignment-specific formatting rules before full drafting
5. build a rubric ledger when the work is graded, academic, source-backed, or teacher-feedback driven
6. reconstruct the required sections and required emphasis
7. build or update the source log and source-claim audit before source-backed drafting
8. fill the core sections with usable content while already following the locked format rules, rubric ledger, and source-claim boundaries
9. supplement supporting sections
10. tighten clarity, consistency, academic standards, and handoff readiness

## Preferred Working Formats

- Markdown when the project is local and text-centric
- Google Docs when collaboration or comments matter
- DOCX when the recipient explicitly requires it, or by default when the final written submission format is otherwise unspecified

If the final written deliverable format is not explicitly specified, treat `.docx` as the default clean submission format.

If the final requirement is a Word-style deliverable, or the format defaults to Word, the final check should happen against the actual `.docx` delivery file whenever feasible.

Only place the clean final `.docx` submission artifact in `runpro_workspace/submission/`. Keep markdown sources, drafts, template references, and helper variants in working or draft folders unless the assignment explicitly asks for them as deliverables.

## Requirement-Locked Writing

Once the requirement lock is approved, treat these as binding when they are specified:

- expected genre or report type
- writing register
- depth or quality tier implied by the course context
- section order
- required subheadings
- methodology versus topic emphasis
- citation style
- required template or form
- disallowed reuse of old drafts

Before full drafting, capture the explicit file-based requirements into `runpro_workspace/10_analysis/requirement-ledger.md`.

For graded academic, source-backed written, formal report, literature review, proposal, or dissertation-style work, build `runpro_workspace/10_analysis/rubric-ledger.md` before full drafting.

Rubric-ledger requirements:

- one item per rubric criterion, required question, required sub-part, actionable teacher-feedback point, or format criterion
- source, weight or importance, expected evidence, draft location, status, evidence, and repair action for each item
- use statuses `pass`, `partial`, `fail`, or `not assessable`
- if no rubric exists, create a `rubric-inferred` ledger from the brief and genre and record the limitation
- do not begin polishing until central rubric items have a planned draft location

Do not rely on a high-level summary when the assignment files contain line-by-line or screenshot-level requirement detail.

If font or layout rules are not specified, record and follow the default academic formatting fallback instead of improvising document styling.

Do not silently replace a required academic or assignment structure with a more generic essay structure.

Do not silently downgrade a formal report, analyst-style course report, or template-led submission into a short answer memo, analyst note, or lightweight discussion piece.

If the exact required template or form is missing, unreadable, or unavailable, stop and surface that blocker instead of inventing a substitute shell.

If the template is available, extract its heading hierarchy, body style, title style, spacing pattern, and section rhythm before drafting the main text. Do not leave template fitting until the end unless that fallback is explicitly accepted.

If the assignment gives explicit formatting requirements, apply them during drafting instead of postponing them until after the text is written.

For written deliverables, unless the assignment or template explicitly requires another pattern, keep bold styling limited to the title and heading hierarchy. Do not use bold for inline emphasis inside body paragraphs, lists, captions, or other running text.

For written deliverables, unless the assignment or template explicitly requires another visual treatment:

- report tables should use black-and-white three-line table styling
- charts or figures embedded in the document should not contain duplicate internal chart titles when the surrounding prose or external figure caption already gives the figure title
- chart internals should still preserve axis labels, legends, units, tick labels, and necessary data annotations
- charts, figures, and diagrams should look visually balanced and academic: centered or optically balanced data region, controlled whitespace, restrained colors, readable labels, consistent typography, and no decorative chart effects
- legends, data labels, and annotations should clarify the figure without making it side-heavy, crowded, clipped, or visually louder than the data
- exported figures should be checked at the actual final document size, not only in the source plotting tool
- inserted project flowcharts or process diagrams should use black-and-white styling rather than colored nodes, arrows, or accent fills

## Source-Backed Writing

If the document depends on real-world facts, citations, or literature:

- collect real sources first
- prefer sources from roughly the last five years unless the assignment or topic needs older seminal work
- prefer high-impact, core-journal, review, guideline, or otherwise field-recognized sources when possible
- record them in `runpro_workspace/10_analysis/source-log.md`
- create or update `runpro_workspace/10_analysis/source-claim-audit.md` for major factual, empirical, evaluative, and comparative claims
- write only from the verified source base
- for scientific manuscripts, paper-derived reports, or figure-led academic writing, define the source/manuscript type, the one-sentence central claim, the main supporting evidence, and the boundary where the claim stops before full drafting
- for scientific manuscript-style work, map each major section to one job such as context/problem, gap, approach/design, evidence, interpretation, implication, or limitation instead of defaulting to a generic essay shell or lab-diary order

For literature reviews or citation-backed writing, do not start prose synthesis before the source log is adequate.

If the source base is weak or missing, do not fabricate. Report the gap explicitly.

Use `scripts/validate_source_log.py` before claiming literature-backed work is complete.

Source-claim rules:

- major claims must map to specific source support, not just a general topic source
- broad claims such as `better`, `effective`, `significant`, `sustainable`, `high quality`, or `improved` must identify the measured or defined outcome when possible
- preserve direction, magnitude, units, sample, method, population, date range, and conditions when they affect interpretation
- commercial pages, screenshots, product labels, and marketing sources cannot carry scientific, technical, performance, nutritional, sensory, or sustainability proof unless they contain measured evidence
- if a claim cannot be supported, narrow it, cite it correctly, move it to a limitation, or remove it

Default floor:

- essay or short paper: `--min-sources 5`
- literature review: `--min-sources 8`

Typical recent-source check:

- `--preferred-recent-years 5 --min-recent-ratio 0.6`

## Format-Strict Work

When the assignment specifies a citation or formatting style, record it in the plan and check it explicitly.

Treat formatting as a two-pass obligation:

- apply the required formatting rules while writing the document
- after the full document is complete, run a final whole-document format check against the assignment rules in the actual delivery file whenever feasible

Do not interrupt execution only to ask for personal identity fields. If a cover page, title page, header, footer, or form asks for student name, student ID, candidate number, class, section, email, phone number, or similar submitter identifiers, leave missing values blank by default and continue. Preserve any identity text already present in source materials, but do not invent or infer it.

Typical checks:

- APA, Harvard, MLA, Chicago, Vancouver, or numbered citation style
- assignment-specific font, spacing, alignment, margin, heading, caption, or page-layout rules
- correct in-text citation form
- correct reference-list form
- correct reference-list ordering and alphabetization for the required style
- author-name fidelity, including initials and diacritics, against the real source metadata
- style-correct handling of no-author, unpublished, or local course materials rather than filename-like shortcut citations
- the document genre and register match the approved quality bar
- superscripts or numbered references when required
- black body text unless the assignment says otherwise
- if no explicit font or layout requirement exists, standard academic fallback formatting is applied consistently
- if a required template exists, the final document reflects its heading and body style conventions rather than only copying text into it at the end
- bold styling is limited to the title and heading hierarchy unless the assignment or template explicitly requires bold in body text
- charts or figures render correctly in the actual document file
- embedded charts or figures avoid duplicate internal titles when an external `Figure X. ...` caption/title is used
- charts or figures are visually balanced, academically restrained, readable at final size, and free of clipped labels, excessive blank canvas, chart junk, or crowded legends
- when the workflow allows, charts or figures preserve editable or vector outputs such as SVG or PDF until final embedding; rasterize only when the final delivery format requires it
- for multi-panel figures, each panel has a distinct analytical role such as overview, comparison/deviation, validation, or relationship/mechanism rather than answering the same question repeatedly without a clear reason
- report tables use black-and-white three-line styling unless the assignment or template explicitly requires another table format
- inserted project flowcharts or process diagrams use black-and-white styling unless the assignment or template explicitly requires another visual rule
- report tables have visible captions/titles when expected by the genre, and header rows are visually distinct from body rows
- tables or visuals that are meant to carry analysis do not look like raw markdown grids or unfinished export defaults

Academic standards are part of drafting, not only final cleanup. Paragraphs should follow claim, evidence, analysis, and implication; core terms and comparison criteria should be defined before evaluative claims; figures and tables should be cited in the text and interpreted in prose; and academic register should remain precise without generic filler.

## Validation Focus

- every explicit requirement from `requirement-ledger.md` is represented in the document or explicitly blocked
- every central rubric item in `rubric-ledger.md` is represented in the document or explicitly blocked
- every hard requirement appears in the document or in a clearly marked pending block
- content names, dates, counts, and ownership references are correct; missing submitter identity fields such as student name or student ID may remain blank by default
- the structure matches the submission context
- the genre, register, and depth match the approved requirement lock
- the structure, emphasis, and template usage match the approved requirement lock
- a final whole-document format pass was run after content completion
- rubric-compliance, academic-standards, and source-claim audits were completed when relevant
- a final citation micro-audit was run after the document already appeared handoff-ready
- any late exporter or formatting fix was followed by another page-structure check for title page, executive summary, table placement, and page-count-sensitive sections
- the document reads as a final artifact, not as working notes
- any factual or literature-backed claims are traceable to real sources
- major claims in source-backed work are represented in `source-claim-audit.md`

## Common Repairs

- missing ledger item -> add the missing requirement to `requirement-ledger.md`, then fix the document and audit against it
- missing section -> add the section and fill it with the best supported content
- genre too light -> expand and rewrite toward the approved report style instead of trimming for brevity
- duplicated content -> consolidate repeated instructions into one clean statement
- weak structure -> rewrite headings before polishing sentences
- scientific manuscript/report has a weak argument spine -> rebuild the section order around claim, evidence, boundary, and explicit section jobs before polishing sentences
- template applied too late -> extract template styles first, then restyle and reflow the document before signoff
- format drift -> fix the actual delivery file against the assignment rules and rerun the final format check before signoff
- non-required bold emphasis in body text -> remove the bold styling, keep emphasis through wording alone, and rerun the final format check before signoff
- table uses colored fills or boxed export defaults without an explicit requirement -> restyle it into a black-and-white three-line table and rerun the real-file format check before signoff
- table exists but looks unfinished -> add a visible table caption, make the header row visually distinct, and rerun the real-file format check before signoff
- embedded chart contains a duplicate top title while the document already has a figure caption -> remove the internal chart title, preserve labels/legend/units, and rerun the real-file format check before signoff
- chart looks unbalanced, overly decorative, crowded, or mechanically exported -> rebalance the canvas, simplify styling, adjust legend/label placement, use restrained academic colors, and inspect the chart again in the actual document
- chart labels, legend, ticks, units, or annotations are clipped or too small at final size -> resize, simplify, or relabel the figure and rerun the real-file format check before signoff
- multi-panel figure is redundant, repetitive, or panel jobs are unclear -> remove or regroup panels so each panel answers a distinct analytical question, then rerun the real-file format check before signoff
- flowchart uses decorative colors without an explicit requirement -> restyle it into a black-and-white diagram, then rerun the real-file format check before signoff
- late formatting fix changed pagination -> restore the required page structure in the delivery file, then rerun the page-level check instead of assuming earlier pagination still holds
- incomplete handoff -> add appendix, assumptions, or next-step note as needed
- weak evidence base -> pause writing, gather real sources, and rebuild the affected section from verified material
- rubric criterion is partial/fail/not assessable -> revise the relevant section until the criterion is visibly answered, or document a true blocker before handoff
- source-claim mismatch -> narrow the claim, replace the source, add the measured outcome, or remove the claim before handoff
- citation-format mismatch -> fix the style in both the body and reference list before declaring completion
- weak no-author or local-material citation -> replace filename-like shorthand with the style-correct title-based or equivalent fallback, then recheck the reference list
- author-name simplification -> restore the source-accurate spelling, initials, and diacritics, then rerun the citation micro-audit
