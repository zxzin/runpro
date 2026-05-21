# PPTPRO Slide Recipes

Use these recipes as low-freedom starting points. Adapt content, but keep the structural logic.

## Shared Slide Skeleton

Use 16:9 widescreen.

Default structure:

- top accent strip: 0.15-0.25 in high
- content margin: about 0.7 in left/right
- title zone: top-left, large sans-serif
- source footer: quiet gray at bottom
- page number: bottom-right
- background: white or very light gray

If a supplied template uses a different strong visual language, adapt the skeleton to that template first. Keep its background, accent strip, title rhythm, footer/source treatment, and image style unless the user asks for a new direction. Do not force the default white/light-gray house style onto a template-bound deck.

Default typography:

- title: 30-36 pt, bold sans-serif
- section label: 9-11 pt, uppercase, accent color
- card title: 18-22 pt, bold for major cards; 16-18 pt only for compact cards
- card body: 14-18 pt for major cards; 12-14 pt only for compact labels or dense diagrams
- footer: 7.5-8.5 pt

Use Arial/Aptos/Helvetica-like sans-serif. Do not use serif fonts.

Default deck shell:

- Slide 1 is a simple cover: title, presentation date, presenter.
- The cover must not contain agenda blocks, thesis previews, abstract text, or content cards.
- The cover date is the actual talk/report date, not presentation duration or time limit.
- The final slide contains only `Thank You` and `Questions & Discussion` by default; `Questions` is acceptable when shorter is better.
- If the assignment forbids cover or closing pages, document that exception and do not add them.
- If editing only part of an existing deck, preserve the existing deck shell and locked slides. Do not add or remove cover/closing/teammate pages unless that is part of the approved scope.

Density defaults:

- Do not create a 3-5 inch tall card for a heading and one short sentence.
- If a card body is only one sentence, keep the card shallow or add real structured material inside it.
- Major visible cards should either be compact content cards or filled analysis panels, not empty frames.
- Keep the main visual mass in the middle and lower-middle of the slide.
- Avoid placing all cards high on the slide and then jumping to a bottom bar with an empty middle gap.
- When a bottom takeaway is used, tune the vertical rhythm so the content row, optional bridge strip, and takeaway feel connected.
- Every short pill or tag label must stay on one line.

Title rhythm defaults:

- Multi-line titles need comfortable leading; do not compress title lines.
- Keep the subtitle visibly separated from the title.
- If a title is too long, rewrite it or reduce size slightly; do not squeeze line spacing.

Text-fit defaults:

- Place text boxes inside card padding, not on top of card edges.
- Use at least 0.16 in horizontal and vertical inset for normal cards.
- The final rendered line must stay clear of the card bottom edge.
- If copy exceeds the safe area, shorten the copy or change the card layout before lowering font size.
- Do not use a text box that extends past the visible card frame even when the visible text looks short.

Corner defaults:

- Use rounded rectangles for visible cards, panels, callouts, synthesis bars, and evidence chips unless the supplied template requires square corners.
- Default PPTPRO cards should be visibly softer than sharp rectangles, roughly 0.12-0.18 in radius or 14-20% of the shorter side for normal cards.
- Use pill rounding only for compact labels and tags, not for large content panels.

## Recipe 1: Minimal Cover

Use for the first slide by default.

Layout:

- title as the main element
- presentation date
- presenter name
- optional course/module/institution only if provided or required
- restrained accent strip or small visual accent only; no content cards

Rules:

- Keep it simple and metadata-only.
- Use the actual presentation date, not speech duration.
- Do not include thesis statements, agenda bullets, source notes, or discussion questions.
- The cover should feel polished through typography, spacing, and alignment, not extra content.

## Recipe 2: Concept Map

Best for the first content slide in a course deck or reading application.

Layout:

- top accent strip
- label: `READING CONCEPTS`
- large title stating the reading's core idea
- one short context sentence
- three horizontal concept cards
- two bottom takeaways tied to readings/authors

Card structure:

- left colored vertical strip
- small label such as `STEP 1`
- 2-4 word card title
- one sentence body

Sizing:

- Keep each concept card compact, usually 1.2-1.8 in high.
- Use bottom takeaways or a synthesis band to fill the lower slide area instead of stretching the cards vertically.
- Keep each card's title/body text within an inset safe area; do not let body lines run past the right edge.

Example roles:

- `Gender rule`
- `Health action`
- `Social meaning`

Do not use unexplained dashes or decorative connectors. If cards are sequential, use a simple connector line between cards.

## Recipe 2A: Source / Book Object Page

Use for book, article, report, or source-led presentations where the audience should see the actual source before the argument becomes abstract.

Layout:

- top accent strip
- label such as `BOOK AS SOURCE`, `REPORT SOURCE`, or `SOURCE OBJECT`
- large title stating what the source contributes
- left or right source visual: book cover, report cover, article/source page, or official source screenshot
- opposite side: compact metadata chips or boxes
- lower-middle: one visual logic chain, field-site line, chapter/case structure, or evidence-type map
- bottom synthesis bar
- quiet source footer

Use real source material when available:

- book cover or official publisher image
- publication year, page count, edition, number of figures/tables, or relevant source facts
- table of contents, chapter titles, field sites, case studies, methods, key actors, or evidence types
- article/media source block with publisher and date

Rules:

- Do not place source visuals on the cover slide unless the user asks; keep the cover metadata-only.
- Use source visuals as evidence/object context, not decoration.
- Preserve aspect ratio for cover or source-page images.
- Do not let a source image collide with bottom takeaways or footers.
- Use at least one real source visual or source-structure element in a book/source-based deck when available and relevant.
- If no source image is available, build a source-structure graphic from verified facts: chapters, cases, field sites, methods, or evidence types.

## Recipe 2B: Supporting Image + Analysis

Use when the source itself is too text-heavy, or when a related real-world image would make a concept, case, place, event, process, or object easier to understand.

Layout:

- top accent strip
- concise analytical title
- one strong supporting image occupying roughly 35-55% of the slide width, or a horizontal image band when the image is contextual
- opposite side: 2-3 short analysis rows, evidence chips, or a compact mechanism/case explanation
- optional bottom synthesis bar
- quiet human-facing source footer or image credit when needed

Good supporting images:

- official/publication/publisher images
- relevant photos of the place, organization, object, policy document, event, lab, product, or setting being discussed
- reputable news/event images or screenshots when the slide is about a current media case
- maps, archival images, museum/government/university images, or other traceable contextual visuals
- AI-generated custom concept, context, process, object-composition, or atmosphere images made with the current latest built-in Codex/ChatGPT image tool when no real or traceable image fits and the image has a clear slide role

Rules:

- Source-native figures and book/report visuals come first. Use supporting images only after the required source visuals or data figures are preserved.
- A supporting image must clarify the slide's argument; do not use vague stock photos or decorative background imagery.
- Prefer traceable, high-resolution, non-watermarked images from reputable or official sources.
- Use generated images only as content-supporting visuals. Do not use them as proof of real events, as official source substitutes, or as replacements for data figures, screenshots, logos, maps, portraits, or source documents.
- Record generated-image provenance separately from cited sources: tool/model, prompt summary, date, and intended slide role.
- Preserve aspect ratio and crop only to remove irrelevant margins.
- Do not place long text over busy images. If text overlays are necessary, use a readable solid panel or strong contrast check.
- Record full image provenance in the source log, notes, or final audit according to the assignment needs. In the visible deck, use only concise human-facing credits such as `Image: NASA` or `Source: WHO, 2024`.
- Do not put internal file-tracking sentences such as `Full source provenance and image credits are recorded in the project source log` on slides, in speaker notes intended for delivery, or in scripts.
- If an image makes the slide prettier but not clearer, reject it.

Visual richness rule:

- A text-heavy deck should not rely on this recipe only once. Use image+analysis, source object, diagram, map, generated illustration, or figure-led layouts repeatedly across the deck so the audience sees the topic, not only text.
- Unless the user/template forbids images, each major section should include at least one visual-led slide or strong visual anchor.

## Recipe 3: Mechanism / Process Flow

Best for explaining cause, sequence, or social mechanism.

Layout:

- light gray background
- top accent strip
- title and subtitle
- optional dark callout in top-right
- four horizontal step cards
- synthesis bar near bottom
- source footer

Step cards:

- number: `01`, `02`, `03`, `04`
- label: one phrase
- body: one short sentence or phrase

Use this for relationships like:

- gender rule -> feeling -> behavior -> result
- belief -> action -> institution -> outcome
- claim -> evidence -> implication -> question

Avoid diagonal connectors unless they are necessary. Keep connectors subtle and clearly directional.

Balance rule:

- If the process has only three ideas, do not stretch three empty cards across the slide. Use a compact flow plus a bottom implication strip, or use a two-column cause/result structure.
- If labels appear as pills or tags, make each label wide enough for one-line text; never allow a one-word label to split.
- If a step card's body wraps to more lines than expected, widen that card or split the phrase. Do not let text collide with connectors or borders.
- Avoid placing the step row too high. If a synthesis bar sits near the bottom, lower the step row or add a bridge element so the slide does not have a large blank middle.

## Recipe 4: Media / Case Analysis

Best for recent media examples.

Layout:

- white background
- top accent strip
- small label: `2025 MEDIA CASE` or equivalent
- large case/article title
- source/publisher name top-right
- three case cards in one row
- synthesis bar
- discussion question bar
- source footer

Three cards:

1. `ARTICLE POINT`: what the media example says
2. `READING CONNECTION 1`: how it fits the main reading
3. `READING CONNECTION 2`: how it fits another concept/source

Card body must not exceed the visual room. If any card body wraps into the bottom edge, shorten it first, then resize.
The text box for each card must stay inside the card safe area; never let the text box extend outside the visible card rectangle.

Card density rule:

- Three-card rows should normally use 1.6-2.4 in card height unless each card contains a visible sub-structure.
- If the cards are taller than 2.4 in, add evidence chips, quote fragments, contrast rows, mini scales, or a lower synthesis region inside the cards.
- If each card has only a heading and one sentence, make the row shallower and use the saved space for synthesis or discussion.
- If one card needs more text height than the others, redesign the row instead of allowing that card's text to spill outside the frame.
- Do not separate the card row and synthesis/discussion bars with a large empty vertical gap.

## Recipe 4A: Field Site / Case Comparison

Use when a source has two or more real cases, field sites, chapters, products, groups, or time periods that should be compared.

Layout:

- title and subtitle
- two large comparison panels, or a 2 x 2 matrix if there are four cases
- each panel has a clear case label, small tag, and 2-3 short rows
- each row pairs a compact heading with one short evidence/action phrase
- bottom synthesis bar states the shared lesson or contrast
- quiet source footer

Good examples:

- `New York City` vs `Buenos Aires`
- `diagnosis route` vs `self-determination route`
- `media case` vs `reading concept`
- `chapter 1` vs `chapter 2` if the chapters have distinct analytical jobs

Rules:

- Use actual source structure, not invented categories.
- Keep each panel filled but not dense; avoid tall panels with text stranded near the top.
- Align row baselines across panels so the comparison is easy to scan.
- Keep row copy short; if a row wraps into the next row, shorten it or widen the text area.
- Do not force all cases into equal cards if one case needs a different visual treatment; redesign the comparison.

## Recipe 5: Report / Paper Data Figure

Use when converting a report, essay, final paper, thesis, or manuscript that contains real data figures/images.

Layout:

- concise result-oriented, conclusion-style title
- original data figure/image as the dominant evidence object, usually taking about 55-75% of the useful slide area when it carries the claim
- one short interpretation callout, narrow interpretation rail, or compact takeaway band
- quiet source/caption line attached close to the figure edge

Rules:

- Use the original figure/image asset from the source document whenever possible.
- Preserve aspect ratio and all labels, axes, legends, scales, and data marks needed for interpretation.
- Do not redraw, restyle, simplify, AI-generate, or approximate the figure unless the user explicitly asks and the underlying data are available.
- Avoid rigid 50/50 symmetry for figure-led evidence slides unless the text and visual truly carry equal weight.
- If the figure is dense, place it large enough to read and move interpretation into the speaker script.
- If the figure is still unreadable at presentation scale, crop it, split it, or give it its own slide instead of shrinking it further.
- If multiple source figures are relevant, prefer one figure per slide or use a clearly labeled comparison layout.
- If a multi-panel figure is used, keep only the panels with distinct analytical roles such as overview, comparison/deviation, validation, or relationship/mechanism. Do not keep two panels that answer the same question unless the redundancy is explicitly useful.
- Do not use a generic icon or decorative illustration in place of a real data figure.

## Recipe 5A: Regional / Lens Pattern Sequence

Use when several regions, cases, markets, or topic lenses must be compared across consecutive slides.

Goal:

- make each page feel like part of one family
- avoid repeating the exact same layout for every region/case
- keep comparison criteria consistent while varying visual structure

Recommended sequence:

- setup slide: mechanism/process flow or concept map explaining the comparison lenses
- region/case 1: supporting image + analysis rows
- region/case 2: image-led case page plus a compact matrix or "engine" panel
- region/case 3: platform/actor mix, hub-and-spoke, or numbered choice model
- conclusion: synthesis matrix, causal chain, or three-region comparison cards with a final implication

Rules:

- Keep the same comparison logic across cases, but vary the visible recipe.
- Each region/case slide needs one dominant visual anchor: real image, map, source object, mechanism diagram, matrix, or platform mix.
- Do not give every region/case the same three cards and bottom takeaway with only labels changed.
- Use supporting images only when they are specific, traceable, and analytically useful.
- A conclusion page should synthesize across cases, not introduce a fourth generic card layout.
- If the deck has a teammate or later section, end the user's section with a bridge that prepares the next section without rewriting that teammate's content.

## Recipe 6: Tag Stack + Explanation

Use only when labels are part of the argument, not as decoration.

Layout:

- left tag stack or legend, wide enough for every tag
- right explanation list or mini diagram
- bottom synthesis statement or implication strip

Rules:

- Each tag must fit on one line. If it wraps, widen the stack, shorten the label, or switch to a list.
- The right side must have a clear visual anchor such as numbered bullets, a bracket, or a diagram, not only floating text.
- The lower slide area should contain a takeaway, summary bar, or continuation of the diagram so the page does not feel empty.
- Tag text must be centered within each pill and stay clear of the pill edge.

## Recipe 7: Thank You + Questions Closing

Use for the final slide by default.

Layout:

- `Thank You` as the dominant text
- `Questions & Discussion` as the only supporting text by default
- `Questions` as the only supporting text when a shorter ending is more appropriate
- simple visual echo of the deck palette

Rules:

- Keep it minimal.
- Do not add presenter names, contact information, course lines, sources, Q&A prompts, closing phrases, evidence, or paragraphs.
- If the user explicitly requests extra closing information, treat that as an exception and keep it minimal.

## Recipe 8: Speaker-Script Matching

When a script is required, structure it like this:

```text
[Slide 1: slide title]
Speaker text for slide 1.

[Slide 2: slide title]
Speaker text for slide 2.
```

The script should carry nuance that is not on the slide. The slide should carry structure.

## Anti-Patterns

Reject and redesign if you see:

- title + generic bullet list on every slide
- beige/cream/tan background unless explicitly requested
- serif headline fonts unless explicitly requested
- giant cards with too much text
- giant cards with too little text
- text boxes that extend outside visible card frames
- card text touching or nearly touching a border
- text clipped at the bottom of a text box
- cover slide that uses presentation duration/time limit instead of presentation date
- missing cover slide or missing final `Thank You` + `Questions` / `Questions & Discussion` slide when not explicitly forbidden
- final slide with anything beyond `Thank You` and `Questions` or `Questions & Discussion`
- report/essay/paper-derived decks that omit relevant original data figures without a reason
- replacing real data figures with generic icons, AI-generated imagery, redrawn approximations, or text-only summaries
- cropping original figures so labels, axes, legends, or data marks become unreadable
- cover slide overloaded with agenda, abstract, thesis preview, or content cards
- cramped title line spacing or title/subtitle collision
- large empty vertical gap between the main content and bottom takeaway
- a large card or panel whose content sits only at the upper-left corner
- top-heavy slides where the title and first content row occupy the slide and the lower half is blank
- uneven card rows where all cards have the same large size but very different content density
- short pill/tag labels that wrap onto multiple lines
- cramped card text near borders
- unexplained short dashes or decorative line fragments
- consecutive content slides that use the same card-row structure with only the text changed
- book/source-based decks with no cover, source metadata, table/chapter/case structure, source screenshot, original figure, or other real source object when such material is available
- media/current-event slides that look like generic text-card summaries rather than case pages with a visible source/event block and reading connection
- source-backed decks that remain text-only even though relevant source visuals or supporting images are available
- text-heavy decks with no clear image, illustration, source-object, diagram, map, or figure-led pacing plan
- generic stock photos, low-resolution/watermarked images, AI-looking filler, or images that are only loosely related to the argument
- AI-generated images used as source evidence, factual screenshots, official-source substitutes, real-event proof, or generic decoration
- images cropped so tightly that the object, place, event, or data context becomes unclear
- sharp default rectangles for new cards, panels, callouts, or synthesis bars when the deck is not following a square-corner template
- visible internal workflow language such as `source log`, `final audit`, `working audit`, `requirement ledger`, `provenance recorded`, or `image credits are recorded`
- source text that looks like a major slide element
- a references slide when the assignment only needs source traceability
- template-bound decks whose revised slides ignore the supplied palette/title/footer/image style
- partial-scope decks that omit preserved teammate, appendix, or locked slides from the final handoff
