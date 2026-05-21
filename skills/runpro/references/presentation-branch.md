# Presentation Branch

Use this branch when the main deliverable is a slide deck or presentation artifact.

Load `truthfulness-policy.md` and `academic-format-policy.md` whenever the deck depends on real citations, literature, or factual claims.

## Target Outputs

Typical outputs:

- PPT or PPTX deck
- pitch deck
- review deck
- talk outline turned into slides
- stakeholder update deck

## First Working Version

The first working version should prove:

- the slide sequence is correct
- each required section has a slide home
- the deck can be edited in the required format

The first pass is about structure and viability, not polish.

Exception for high-polish template-bound decks:

- still build a working version first, but do not hand off or show it as final-quality until the template, visual recipe map, supporting images, rendered previews, and audit loop have all been completed
- if the source deck is a required template or a teammate-shared file, the first working version must also prove that unchanged slides/pages can be preserved or reassembled without being lost

## Execution Priorities

1. determine the required deck format
2. define slide sequence and narrative arc
3. scaffold key slides with real content
4. for visually important PPT/PPTX work, load `$pptpro` and choose explicit slide recipes before building
5. make layout visually intentional, not merely viable
6. fix overflow, spacing, and visual hierarchy through preview-based checks
7. package the editable deck for handoff

## Preferred Working Paths

- Use `$pptpro` when the user asks for a beautiful, designed, high-quality, class-ready, or non-generic PPT, or when prior PPT quality feedback complains that the deck looks lazy, AI-like, beige/template-like, visually weak, or not carefully designed.
- Use the `PowerPoint` skill first for editable `.pptx` generation, visual validation, and final PPT handoff when PPT output is required
- Use the `slides` skill when the task explicitly benefits from the PptxGenJS authoring workflow or requires delivering the authoring `.js` alongside the deck
- Use the `pptx` skill as a fallback or for format-specific PPTX inspection and OOXML editing workflows
- Use Google Slides tools when the target is a native Slides deck
- Use Canva when the user explicitly wants Canva or on-brand visual generation

Do not rely on raw direct generation alone for final PPT quality checks. Use the presentation-specific workflow and validate the actual deck output.

## PPTPRO Strict Integration

When `$pptpro` is used, do not treat it as a loose style hint. Treat it as a strict deck-production workflow.

Load the PPTPRO skill body and, for designed PPT/PPTX work, also load:

- `$CODEX_HOME/skills/pptpro/references/design-system.md`
- `$CODEX_HOME/skills/pptpro/references/slide-recipes.md`

PPTPRO is the source of truth for visually polished PPT/PPTX production quality. Runpro presentation routing, planning, final-audit records, and handoff checks must not apply a weaker local PPT standard than the loaded PPTPRO skill.

Carry these defaults into the requirement lock unless the assignment or user says otherwise:

- use clean white or light-gray backgrounds instead of beige/cream AI-looking templates
- use sans-serif fonts only unless a template requires another font
- include a simple cover slide by default, containing only title, presentation date, and presenter unless the user/template requires more; the date is the talk/report date, not presentation duration
- include a simple final slide containing only `Thank You` plus `Questions` or `Questions & Discussion` by default unless explicitly forbidden
- prefer concept maps, process flows, case cards, and media-analysis layouts over generic bullet slides
- avoid repeated same-structure content slides; do not let multiple middle slides look like title + three text cards + bottom takeaway with only the words changed
- for book, article, report, or source-led decks, include real source object/context when available: book cover, official metadata, table of contents, chapter/case structure, field sites, methods, evidence types, source screenshots, or original figures
- for book-based decks, make at least one content slide show the source as an object or structure before reducing it to abstract concepts
- after preserving source-native visuals, create a visual enrichment plan for text-heavy decks and find or create visuals that improve display power: official/context photos, maps, policy or media screenshots, event images, organization/place/object photos, lab/product/process photos, generated illustrations, diagrams, or other visual anchors
- supporting images must be relevant, high-quality, source-attributable, and analytical rather than decorative; reject vague stock photos, low-resolution/watermarked images, AI-looking filler, and images that only fill empty space
- when no real or traceable image fits and a custom content visual would make the slide clearer, use Codex/ChatGPT's built-in image generation with the current latest built-in image model/tool exposed by the environment; log generated-image provenance separately from cited sources
- never use AI-generated images as source evidence, real-event proof, official-source substitutes, original data figures, logos, real-person portraits, maps, or factual screenshots
- use softer rounded rectangles for new cards, panels, callouts, and synthesis bars unless a supplied template clearly requires square-corner geometry
- keep internal workflow, audit, source-log, provenance-record, and file-tracking language out of visible slides, delivery notes, and scripts; use concise human-facing credits such as `Source: WHO, 2024`, `Image: NASA`, or a normal `Sources used` slide
- convert abstract reading ideas into visual logic such as process flows, source-structure maps, two-site/case comparisons, or media-event-to-theory analysis
- for scientific paper, preprint, thesis-seminar, journal-club, or other figure-led academic decks, classify the source type before drafting and choose the matching arc: question-to-evidence, problem-to-solution, workflow-to-validation, design-to-inference, property-to-mechanism, or evidence-map
- for scientific content slides, prefer conclusion-style titles over labels such as `Results`, `Method`, or `Figure 3`
- for figure-led scientific slides, let the main figure or table dominate the page when it carries the claim; keep interpretation compact and subordinate
- if a slide uses multiple figure panels, each panel must have a distinct analytical role such as overview, comparison/deviation, validation, or relationship/mechanism
- avoid unexplained decorative marks, dashes, boxes, or connectors
- avoid oversized empty cards, sparse panels, wrapped pill labels, and top-heavy slide balance
- avoid large empty vertical gaps between main content and bottom takeaway bars
- avoid cramped multi-line title spacing or title/subtitle collision
- avoid card text crossing, touching, or being clipped by card borders
- keep speaker scripts explicitly mapped to slide numbers
- distinguish assignment-required formal references from practical `Sources used` traceability
- when converting from a report, essay, final paper, thesis, or manuscript, inventory and reuse relevant original data figures/images from the source document instead of replacing them with generic visuals or text-only summaries
- render or preview every slide when tooling permits, inspect visually, repair defects, and rerun checks

For template-bound or partial-scope PPT/PPTX work, also lock:

- source deck/template filename and total slide count
- exact revised slide range
- exact preserved slide range
- whether the final deliverable must be the full deck or only the revised excerpt; default to full deck when the task says "modify this template" or "do not change the later/classmate section"
- visual language to preserve from the template, including palette, typography, title style, footer/source style, and image treatment
- audit plan for the revised range and render/assembly plan for the full final deck

Use this PPTPRO production chain:

1. write a compact design brief
2. inventory useful real source objects and structures before drafting: covers, official metadata, source screenshots, tables of contents, chapters, field sites, cases, methods, evidence types, original figures/images, or media-event facts
3. for scientific paper, preprint, thesis-seminar, journal-club, or other figure-led academic decks, classify the source type, choose the argument arc, and map the central claim, main evidence, and boundary before laying out slides
4. if the deck risks feeling text-only after source-native visuals, create a visual enrichment plan and find or create a candidate set of relevant supporting images, generated illustrations, diagrams, maps, or source-object visuals; keep only those that make the argument clearer or more concrete
5. if no real or traceable image fits and the slide would benefit from a custom concept, scene, process, object, or atmosphere visual, generate a limited image set with the current latest built-in Codex/ChatGPT image tool and record generated-image provenance
6. if building from a report/essay/final paper/thesis/manuscript, extract or inventory original data figures/images and decide which must appear in the deck
7. if editing an existing template, inventory the template's visual rules and decide which slides/pages must remain untouched
8. create a slide recipe map before building: slide number, user/preserved ownership, recipe, main message, image/source role, generated/external image role, and script role
9. assign each revised slide a recipe from `slide-recipes.md`, varying adjacent content slides unless repetition is intentional and useful
10. for scientific figure-led slides, decide whether the original figure should stay whole, be cropped, or be split across slides; if a slide uses multiple panels, keep only panels with distinct analytical roles
11. build editable PPTX with native slide objects, softer rounded cards where applicable, and original figure/image/source/supporting/generated-image assets where visual support is needed
12. assemble the final full deck with preserved slides intact when the source task is template-bound or partial-scope
13. generate per-slide previews
14. manually inspect the previews for visual defects, image relevance, generated-image appropriateness, image quality, repeated layout patterns, rounded-corner consistency, scientific evidence hierarchy, and full-deck assembly/order
15. repair any issue and rerender
16. run PPTPRO strict audit on the actual final deck when possible; if preserved slides are intentionally image-only or not parseable, run strict audit on a revised-range audit copy and separately render/inspect the final full deck
17. record the result in `final-audit.md`, including recipe map summary, image provenance, generated-image provenance, revised range, preserved range, and full-deck render status

For local PPTX handoffs using `$pptpro`, run its audit script with strict mode when available:

```bash
python $CODEX_HOME/skills/pptpro/scripts/pptpro_audit.py path/to/deck.pptx --script path/to/script.docx --render --strict
```

If the deck has no script, omit `--script` but still use `--render --strict`.

If the deck is converted from a report/essay/final paper/thesis/manuscript and a figure inventory identifies required original data images, or if the deck intentionally uses supporting images for visual enrichment, add `--min-pictures N` with the expected minimum number of image assets.

Treat any PPTPRO strict failure as a remediation trigger:

```bash
python $CODEX_HOME/skills/pptpro/scripts/pptpro_audit.py path/to/deck.pptx --script path/to/script.docx --render --strict
```

Manual visual inspection remains required because the audit script cannot know whether a slide is attractive. Reject and rebuild if any preview shows:

- generic title-plus-bullets as the dominant pattern
- cramped card text
- text touching card edges
- confusing connectors or decorative dashes
- cover slide using presentation duration/time limit instead of presentation date
- missing simple cover slide or missing final `Thank You` + `Questions` / `Questions & Discussion` slide when not explicitly forbidden
- final slide with presenter/contact/course lines, closing phrases, Q&A copy, or any text beyond `Thank You` and `Questions` / `Questions & Discussion`
- overloaded cover slide with abstract, agenda, thesis preview, or content cards
- consecutive content slides that share the same card-row structure and differ only in text
- scientific paper decks that merely mirror the source paper section order without a visible presentation argument arc
- scientific result slides titled only `Results`, `Method`, `Figure X`, or other topic labels when a conclusion-style title is available
- book/source-based decks with no real source visual, official metadata, table/chapter/case structure, field-site map, source screenshot, original figure, or other source-specific material when such material is available and relevant
- book/source-based decks that summarize only abstract concepts while ignoring the source's actual cases, chapters, methods, actors, places, figures, or evidence types
- source-backed decks that remain text-only when relevant source-native visuals or supporting images are available and would improve clarity
- text-heavy decks with no regular image, illustration, source-object, diagram, map, or figure-led pacing
- supporting images that are generic stock, low-resolution, watermarked, AI-looking, weakly related, untraceable, or used only as decoration
- AI-generated images used as evidence, factual screenshots, official-source substitutes, real-event proof, or generic decoration
- image-heavy slides where the image overwhelms the argument, creates poor text contrast, or causes awkward empty space/cropping
- visible internal project language such as `source log`, `final audit`, `working audit`, `requirement ledger`, `provenance recorded`, or `image credits are recorded`
- media/current-case slides that look like generic text summaries instead of case/event pages with a visible event source and explicit reading connection
- report/essay/final-paper-derived slides that discuss real data but omit the original data figure/image used in the source document
- original data figures replaced by generic icons, AI-generated graphics, redrawn approximations, or text-only summaries
- source figures cropped so labels, axes, legends, or data marks are lost
- scientific figure-led slides forced into symmetrical 50/50 layouts even though one side should clearly dominate
- multi-panel scientific slides where two or more panels answer the same question without a clear comparison reason
- giant empty cards or panels
- card text stranded at the top-left of a tall frame
- text boxes extending outside visible card frames
- text touching or clipping against card borders
- new cards, panels, callouts, or synthesis bars with sharp default rectangle corners when the deck is not following a square-corner template
- short tag/pill labels wrapping across lines
- meaningful content concentrated only near the title while the lower slide area is blank
- a large empty gap between the main content row and bottom synthesis/takeaway bar
- multi-line titles with cramped leading or subtitles too close to titles
- beige/cream AI-looking background
- serif fonts when not required
- slide content that does not match the speaker script
- formal `References` where the assignment only needs `Sources used`
- a template-bound deck where revised slides ignore the supplied template's visual language without user approval
- a partial-scope deck where teammate/locked slides are missing from the final deliverable despite the task asking to modify the provided template
- a final full deck whose slide order, page count, or preserved pages no longer match the locked scope

For source-backed decks, use `scripts/validate_source_log.py --min-sources 3` as a default floor unless the assignment requires more.

For source-backed decks, do not edit the final deck's references or sources slide until `source-log.md` has been rebuilt and verified. The correct order is:

1. verify `source-log.md`
2. update the final deck from the verified source log
3. run the final source audit on the actual deck

Do not patch the deck first and promise to reconcile the source log later.

For decks made from a report, essay, final paper, thesis, or manuscript:

1. inspect the source document for real data figures/images before drafting slides
2. extract the original image assets from the source file when possible, rather than taking low-quality screenshots
3. map each relevant data figure to the slide claim it supports
4. preserve figure aspect ratio and readable labels/axes/legends
5. document omitted source figures with a short reason in the working audit or figure inventory
6. use `Report / Paper Data Figure` from PPTPRO slide recipes for figure-led evidence slides

When the deck relies on literature or current evidence:

- prefer sources from roughly the last five years unless older seminal work is necessary
- prefer higher-impact, core-journal, review, guideline, or otherwise field-recognized sources
- use a recent-source check such as `--preferred-recent-years 5 --min-recent-ratio 0.6` unless the topic requires broader historical coverage

## Requirement-Locked Decks

Once the requirement lock is approved, treat these as binding when they are specified:

- slide order
- required sections or slide types
- required template or official form
- required reference style
- disallowed reuse of old topic content
- edited slide range and preserved slide range
- whether the final deliverable is the full deck or an excerpt

If the deck needs both academic references and non-literature provenance items such as datasets, websites, images, or source entry points, lock whether these should appear as separate sections or separate slides. Do not silently merge them into one list that visually reads like a pure reference slide unless the assignment explicitly wants that format.

Do not silently replace an official deck structure or required form with a generic slide sequence.

If the exact required template or official form is missing, stop and surface that blocker instead of improvising a near-equivalent deck.

If a preserved range belongs to another teammate or is outside the user's section, do not redesign it. Preserve it as editable slides when possible; if only a PDF/image source is available, preserve it as visually faithful full-slide images and record that choice in the final audit.

## Validation Focus

- slide order matches the intended story
- no core requirement is missing from the deck
- required structure, template usage, and emphasis match the approved requirement lock
- layout is readable and not visibly broken
- aesthetic constraints from the user are explicitly checked, such as no serif font, no beige background, no AI-looking template, and no unexplained decorative marks
- visually polished decks are checked for fit, density, rhythm, and balance: simple cover exists with presentation date rather than duration, final slide contains only `Thank You` plus `Questions` or `Questions & Discussion`, no card-border overflow, no giant sparse cards, no tiny-looking text inside large boxes, no wrapped short labels, no cramped title spacing, no large vertical gaps, and no bottom-empty slide layouts
- visually polished source-backed decks are checked for source-object specificity: repeated card layouts are avoided, real source visuals/structures are used when available, book/report decks show the source as an object or structure, and media slides read as case analysis rather than ordinary text cards
- visually polished decks are checked for appropriate image enrichment: text-heavy decks have a visual enrichment plan, relevant supporting images and appropriate generated content visuals were considered, any image used has clear provenance and a real content role, and no image harms readability, balance, or source integrity
- visually polished decks are checked for rounded-corner consistency: new cards, panels, callouts, and synthesis bars use softer rounded rectangles unless the supplied template requires square corners
- visually polished decks are checked for human-facing delivery language: no visible slide text, footer, speaker note intended for delivery, or script line contains source-log, audit, provenance-record, or file-tracking explanations
- template-bound decks are checked for fit to the supplied template's palette, typography, spacing, and page rhythm rather than being redesigned into an unrelated house style
- partial-scope decks are checked for final slide count, slide order, revised range, and preserved range
- slide/script correspondence is checked when a speaker script is part of the deliverable
- PPTPRO strict audit was run for `$pptpro` decks, or a limitation was recorded
- preview images were visually inspected and any fixable defect was repaired
- for report/essay/final-paper-derived decks, original data figures/images were inventoried and relevant ones appear in the deck as original figure assets
- editable output format matches the handoff requirement
- source-backed claims and references are traceable when the deck requires them
- the final references or sources slide was rebuilt from the verified `source-log.md`, not edited ahead of it
- academic references are not silently mixed with data, media, or website provenance unless the assignment explicitly requires a combined list
- the actual presentation file has no obvious overlap, overflow, or rendering breakage

## Common Repairs

- too much text -> split or compress slides before styling
- weak flow -> reorder slides before adjusting visuals
- layout breaks -> fix structure first, then design
- missing presenter context -> add notes or a delivery summary if needed
- citation or reference mismatch -> fix slide-level references and end references before signoff
- source-log/deck drift -> rebuild the end references or sources slide from the verified `source-log.md`, then rerun the source audit
- mixed reference/source slide -> split into `References` and `Data/Media Sources` or equivalent labeled sections unless the assignment explicitly requires a combined list
- internal workflow sentence appears in deck -> remove it from the PPT, keep the detail only in working logs/audits, and replace visible text with a concise source credit or normal `Sources used` entry if needed
- repetitive text-card deck -> redesign at least one middle slide as a source/object page, process flow, field-site/case comparison, source-figure slide, media case page, timeline, or matrix
- book/source deck feels generic -> add cover/official metadata, table/chapter/case structure, field sites, methods, key actors, evidence types, or other verified source-specific material
- source-backed deck still feels too text-only -> add relevant supporting images, generated illustrations, diagrams, source-object pages, or image-led layouts only if they strengthen the content, then rebalance text around them
- no suitable real/supporting image exists but a visual would improve clarity -> generate a custom content visual with the current latest built-in Codex/ChatGPT image tool, log it as generated, and keep it clearly non-evidentiary
- weak image use -> remove generic/decorative images, replace with a source-native visual or a traceable contextual image, or return to a diagram if no good image exists
- sharp default boxes -> switch new PPTPRO cards/callouts/panels to medium-soft rounded rectangles and rerender
- media slide feels generic -> create a visible event/source block and a separate reading/theory connection block
- missing preserved section -> reassemble from the original deck/PDF/template, then rerender the final full deck and record the revised-range audit separately if strict audit cannot parse preserved image slides
- template mismatch -> restyle the revised slides within the template's palette, title rhythm, source/footer style, and image treatment before any further content polish
