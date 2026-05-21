# Final Checklist

Do not declare completion until this checklist has been reviewed.

## Deliverable

- The main deliverable exists in the expected location.
- The deliverable format matches the project requirement.
- For written deliverables with no explicitly required final format, the final submission artifact is `.docx`.
- The latest requested revisions are reflected.
- If the assignment gave explicit formatting rules, those rules were followed during drafting and not deferred entirely to end-stage cleanup.
- No required quality step was skipped purely to save time or tokens.
- The deliverable is complete enough to be judged against the full requirement set, not just as a draft shell.
- The work is strong enough to target the `90+` score band rather than only bare acceptability.
- All required assignment parts are present rather than strategically omitted.
- For graded academic writing or source-backed written submissions, the final deliverable has passed an argumentation-quality audit, not only a completion and formatting audit.

## Requirement Coverage

- `runpro_workspace/10_analysis/requirement-ledger.md` exists and captures explicit file-based requirements rather than only a high-level summary.
- The final output matches the approved requirement lock in `runpro_workspace/10_analysis/approval-gate.md`.
- All hard requirements are either satisfied or explicitly marked as unresolved.
- All required assignment parts are complete unless a true blocker is documented.
- Required structure, section order, methodology emphasis, template bindings, and output format were respected.
- Expected genre, writing register, and depth were respected.
- No confirmed requirement was silently relaxed or reinterpreted during execution.
- No required template, form, or shell was replaced by a substitute unless the user explicitly approved that change.
- Dates, content names, numbers, and ownership references were checked. Missing submitter identity fields such as student name or student ID may be left blank by default and should not block handoff unless the user explicitly asked to fill them.
- No major scope item from the source materials was silently dropped.
- Any missing but necessary supporting material was supplemented.
- No unsupported factual claim is presented as verified fact.

## Execution Evidence

- The execution plan reflects what was actually done.
- The active gate progressed to final delivery state.
- `runpro_workspace/10_analysis/feasibility-check.md` exists and records whether the current materials were sufficient.
- The delivery checklist was updated during the work.
- `runpro_workspace/10_analysis/final-audit.md` exists and records a detailed completion review.
- The final audit records an internal quality score, target threshold, and estimated score band.
- The final audit records an estimated external score band and why the work is or is not plausibly in the `90+` range.
- Created or modified outputs are listed clearly in the final summary.
- The summary explains what was required, what was completed, and what remains.

## Validation

- Relevant validations were run for the project type.
- `scripts/validate_requirement_lock.py --require-approved` passes or the limitation is stated explicitly.
- `scripts/validate_requirement_ledger.py --final` passes or the limitation is stated explicitly.
- `scripts/validate_final_audit.py` passes or the limitation is stated explicitly.
- For graded academic written submissions, `scripts/validate_final_audit.py --require-rubric-compliance-audit` passes or the limitation is stated explicitly.
- For assignment-style document work, `scripts/validate_final_audit.py --require-academic-standards-audit` passes or the limitation is stated explicitly.
- For source-backed written submissions, `scripts/validate_final_audit.py --require-source-claim-audit` passes or the limitation is stated explicitly.
- For academic or source-backed graded written submissions, `scripts/validate_final_audit.py --require-academic-quality-audit` passes or the limitation is stated explicitly.
- For source-backed presentation work, `scripts/validate_final_audit.py --require-presentation-source-audit` passes or the limitation is stated explicitly.
- For high-risk or graded submission work, `strict mode` was explicitly used and its fixed validation chain was completed.
- The route-specific validations from `runpro_workspace/10_analysis/project-routing.md` were checked.
- The initial feasibility verdict was respected: either the project was completeable with the available materials, or the missing required inputs were resolved before handoff.
- Each locked requirement was evaluated explicitly, not assumed covered by a high-level impression.
- Each explicit item in `requirement-ledger.md` was evaluated explicitly rather than inferred from a broad summary.
- If a template or exemplar existed, its quality bar and style signals were extracted before or during drafting, not ignored until the end.
- Failed validations triggered remediation instead of being merely reported.
- The output was rechecked after each meaningful repair.
- If full validation was not possible, the limitation is stated explicitly.
- If the approved requirement lock had to change, renewed user confirmation was captured before execution continued.
- The audit judges the submission plausibly within the `90+` range, or a true blocker is documented explaining why that target could not be reached.
- The result is at least in `Ready for review` state before handoff.
- The `Estimated Score Band` reflects the most conservative credible current estimate rather than an optimistic upside scenario.
- For literature or research-backed work, `runpro_workspace/10_analysis/source-log.md` exists and reflects real sources actually used.
- For literature or research-backed work, `scripts/validate_source_log.py` passes or the limitation is stated explicitly.
- For literature-driven work, the source base is primarily recent, roughly within the last five years, unless older sources are clearly justified as seminal, foundational, or explicitly required.
- For literature-driven work, source quality was considered, with preference for higher-impact, core-journal, review, guideline, or otherwise authoritative sources when available.
- For graded academic written submissions, `runpro_workspace/10_analysis/rubric-ledger.md` exists and maps rubric, brief, teacher feedback, required questions, and format criteria to visible draft locations.
- For graded academic written submissions, every central rubric item is `pass` or explicitly blocked; no high-weight item remains partial, failed, or not assessable at handoff.
- For assignment-style document work, academic standards were checked as a strict gate, including citation style, in-text/reference matching, reference metadata, formatting, figure/table conventions, paragraph reasoning, headings, word count, appendices, and academic register where relevant.
- For source-backed written submissions, `runpro_workspace/10_analysis/source-claim-audit.md` exists and maps major factual, empirical, evaluative, and comparative claims to specific source support.
- For source-backed written submissions, major claims preserve measured outcome, direction, magnitude, units, sample, method, population, date range, and conditions when they affect interpretation.
- For source-backed written submissions, unsupported, overbroad, mismatched, decorative, or not-assessable citations were repaired, narrowed, replaced, or removed before handoff.
- For assignment-style document work, citation style and in-text/reference-list consistency were checked.
- For assignment-style document work, a final post-validation micro-defect sweep was run after the deliverable already looked handoff-ready.
- For assignment-style document work, that micro-defect sweep explicitly checked reference-list ordering, cited/reference parity, author-name fidelity, and no-author or unpublished-material handling.
- For assignment-style document work, filename-like placeholder citations were replaced with style-correct title-based or equivalent citations when required.
- For assignment-style document work, any explicit assignment formatting rules were checked against the final document after the full content was complete.
- For assignment-style document work, if no explicit font or layout requirement existed, the default academic formatting fallback was applied consistently.
- For assignment-style document work, bold styling is limited to the title and heading hierarchy unless the assignment or template explicitly requires bold in body text.
- For assignment-style document work, if no explicit table style was required, report tables use black-and-white three-line styling rather than colored fills or boxed export defaults.
- For assignment-style document work, embedded figures or charts do not contain duplicate internal chart titles when the document already provides a figure caption/title; axis labels, legends, units, and necessary data annotations are preserved.
- For assignment-style document work, charts, figures, and diagrams are visually balanced and academically polished: controlled whitespace, readable labels, restrained colors, consistent typography, honest scales, no decorative chart effects, no clipped labels, and no off-center visual weight.
- For assignment-style document work, when the workflow allows, charts and figures preserve editable or vector outputs such as SVG or PDF until final embedding rather than rasterizing too early without reason.
- For assignment-style document work, multi-panel figures use distinct panel roles such as overview, comparison/deviation, validation, or relationship/mechanism rather than repeating the same analytical question across panels.
- For assignment-style document work, if no explicit diagram style was required, inserted project flowcharts or process diagrams use black-and-white styling and do not rely on color coding for meaning.
- For assignment-style document work, any format defects found in the final whole-document check were fixed and rechecked before handoff.
- For assignment-style document work, any non-blocking but fixable citation or reference defect found in the micro-defect sweep was fixed and rechecked before handoff.
- For assignment-style document work, the final artifact still reads like the approved report type rather than a shortened memo or note.
- For assignment-style document work, any table or visual used as part of the analysis has a visible caption/title when expected by the genre and does not look like a raw export artifact.
- For academic or source-backed graded written submissions, meaningful analytical tables and visuals are interpreted in the surrounding prose and used to support conclusions, not merely inserted as information displays.
- For academic or source-backed graded written submissions, figures are inspected in the actual final document size so visual balance, label readability, legend placement, and data-region placement remain professional after embedding/export.
- For academic or source-backed graded written submissions, the thesis, research question, or central judgement directly answers the prompt and every rubric criterion or required sub-question is visibly answered.
- For academic or source-backed graded written submissions, the central claim, the main supporting evidence, and the boundary where that claim stops are all explicit enough to audit.
- For academic or source-backed graded written submissions, each major section has a clear analytical purpose and no section remains as generic background filler.
- For academic or source-backed graded written submissions, paragraphs connect claims, evidence, and implications rather than placing citations after descriptive statements.
- For academic or source-backed graded written submissions, high-stakes factual claims rely on appropriate evidence quality, and weaker sources are not used as the main proof for scientific, technical, policy, or performance conclusions.
- For academic or source-backed graded written submissions, literature coverage is comparative and evaluative rather than only source-by-source or example-by-example when the assignment calls for literature analysis.
- For academic or source-backed graded written submissions, the synthesis identifies patterns, disagreements, evidence strength, and gaps in the literature where relevant.
- For academic or source-backed graded written submissions, contrary evidence, limitations, uncertainty, trade-offs, or boundary conditions are acknowledged when the task expects evaluation.
- For academic or source-backed graded written submissions, repeated central ideas are reduced after their first clear statement and later sections develop those ideas through evidence, comparison, or application-specific analysis.
- For academic or source-backed graded written submissions, key terms, scope boundaries, comparison criteria, and methodology choices are defined before they are used to make evaluative claims.
- For academic or source-backed graded written submissions, broad claims such as `improved stability`, `better performance`, or `stronger outcome` are tied to specific measured outcomes from the cited study whenever the source permits.
- For academic or source-backed graded written submissions, numerical or empirical claims preserve direction, magnitude, units, groups, conditions, and comparison baselines when these details affect interpretation.
- For academic or source-backed graded written submissions, required theories, frameworks, course concepts, methods, or case context are applied explicitly rather than only mentioned.
- For academic or source-backed graded written submissions, section transitions and topic sentences make the argument traceable from prompt to conclusion.
- For academic or source-backed graded written submissions, commercial pages, product labels, and marketing materials are limited to market/ingredient examples unless they provide measured evidence for the claimed outcome.
- For academic or source-backed graded written submissions, the conclusion is concise, judgement-led, and not a repeated summary of all earlier sections.
- For academic or source-backed graded written submissions, every citation supports the specific claim attached to it and no citation is decorative, mismatched, or used only to create an impression of authority.
- For academic or source-backed graded written submissions, obvious awkward phrasing, grammar defects, mistranslated idioms, and vague academic language that would weaken professional credibility are fixed before high-score signoff.
- For assignment-style document work, table header rows are visually distinct from body rows in the actual delivery file.
- For assignment-style document work, any late-stage exporter or formatting fix triggered a fresh page-structure recheck rather than relying on earlier pagination evidence.
- For presentation work, the actual deck file was checked for overlap, overflow, and rendering issues or the limitation is stated explicitly.
- For visually polished PPT/PPTX work using `$pptpro`, `pptpro_audit.py --render --strict` passed, or the limitation is stated explicitly.
- For visually polished PPT/PPTX work using `$pptpro`, the final audit records which PPTPRO slide recipes were used and confirms preview images were manually inspected after the final repair pass.
- For template-bound or partial-scope PPT/PPTX work using `$pptpro`, the final audit records the revised slide range, preserved slide range, final slide count, and whether strict audit was run on the final deck or on a revised-range audit copy.
- For template-bound or partial-scope PPT/PPTX work, the final full deck was rendered or previewed after assembly so preserved pages, slide order, and visual continuity were checked.
- For visually polished PPT/PPTX work using `$pptpro`, the deck includes a simple cover slide with title, presentation date, and presenter; the cover does not use presentation duration as the date field; and the final slide contains only `Thank You` plus `Questions` or `Questions & Discussion` unless explicitly forbidden.
- For visually polished PPT/PPTX work, no user-forbidden visual trait remains, such as serif fonts, beige/cream backgrounds, generic bullet-only layouts, confusing decorative dashes, unexplained connectors, or text touching/overflowing cards.
- For visually polished PPT/PPTX work, card text boxes stay inside visible card frames with safe padding and no clipped last lines.
- For visually polished PPT/PPTX work, no large sparse cards, top-left-stranded card text, wrapped short labels, cramped title spacing, large vertical content gaps, or visually top-heavy/bottom-empty layouts remain.
- For visually polished PPT/PPTX work, new cards, callouts, panels, and synthesis bars use softer rounded rectangles unless the supplied template clearly requires square-corner geometry.
- For scientific paper, preprint, thesis-seminar, or journal-club decks, the final deck follows a visible argument arc matched to the source type rather than mechanically mirroring the paper section order.
- For scientific figure-led slides, conclusion-style titles are used where available and the dominant figure or table clearly outranks the interpretation text in visual hierarchy.
- For scientific multi-panel slides, each visible panel has a distinct analytical role and redundant panels were removed or justified.
- For visually polished PPT/PPTX work, text-heavy decks include a visual enrichment plan and use meaningful images, generated illustrations, diagrams, maps, source-object visuals, or figure-led layouts regularly enough that the deck does not read as repeated text cards.
- For PPT/PPTX work made from a report, essay, final paper, thesis, or manuscript, original data figures/images in the source document were inventoried, relevant ones were reused in the deck, and omissions were documented with reasons.
- For PPT/PPTX work made from a report, essay, final paper, thesis, or manuscript, no relevant original data figure was replaced by a generic icon, AI-generated visual, redrawn approximation, or text-only summary.
- For PPT/PPTX work with a speaker script, the script includes slide-number markers and the final audit confirms slide/script correspondence.
- For source-backed presentation work, `source-log.md` was verified before the final references/source slides were updated.
- For source-backed presentation work, the final deck references/source slides are consistent with the latest verified `source-log.md`.
- For source-backed presentation work, academic references are not mixed with data, media, or website provenance in a misleading pseudo-reference list unless the assignment explicitly requires a combined source list.
- For source-backed or visual presentation work, every external supporting image used has full provenance recorded in the source log, notes, or final audit according to the assignment need; visible deck footers use only concise human-facing credits when needed.
- For source-backed or visual presentation work, every generated image used was created with the current latest built-in Codex/ChatGPT image tool, logged with tool/model, prompt summary, date, and slide role, and was not used as a factual source or evidence substitute.
- For presentation work, the visible deck and delivery script contain no internal workflow language such as `source log`, `final audit`, `working audit`, `requirement ledger`, `provenance recorded`, or `image credits are recorded`; source notes are human-facing credits or normal references only.
- Efficiency decisions did not reduce required verification depth.
- If any required item failed the audit, work continued until it passed or a true blocker remained.
- If the work was still judged below the `90+` band, work continued until targeted repairs were exhausted or a true blocker remained.
- If a later reassessment lowered the credible score estimate below the target band, the project re-entered remediation instead of staying in a ready state.

## Final Handoff

- `runpro_workspace/10_analysis/final-summary.md` exists.
- The final handoff names key files or output locations clearly.
- The project is not handed off with known fixable failures.
- The project is not handed off while any audit item is still marked incomplete, failed, or "to be fixed."
- `runpro_workspace/submission/` contains only the actual required submission contents and no extra process files.
- `runpro_workspace/submission/` does not contain draft `.md` files, reference templates, style exemplars, or duplicate helper exports unless they are explicitly required for submission.
- The handoff does not claim certainty where evidence is missing.
- The handoff language distinguishes `no blocking issues` from `no remaining issues` and does not overstate the cleanliness of the result.
- The final response clearly states one of:
  - `Ready to submit`
  - `Ready for review`
  - `Blocked`
