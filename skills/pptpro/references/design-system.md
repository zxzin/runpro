# PPTPRO Design System

## Visual Intent

PPTPRO decks should feel like a careful editorial/classroom presentation: clean, modern, restrained, and easy to speak from. The audience should understand the slide in a few seconds while the script carries the full explanation.

## Default Palette

- Background: `#FFFFFF` or `#F8F9FA`
- Main text: `#161B20`
- Secondary text: `#657079`
- Rule/border gray: `#C4CBD2`
- Charcoal: `#1F242A`
- Teal: `#007B74`
- Blue: `#375984`
- Coral: `#DA4E34`

Avoid beige/cream/sand/tan as the main background because it often reads as generic AI template styling.

Template override: if the user supplies a real deck/template, the template palette controls unless the user asks for a new visual direction. Extract and reuse the existing palette, title rhythm, footer style, image treatment, and section markers first. The goal is a better version of the supplied deck, not a PPTPRO house-style replacement.

## Typography

- Use sans-serif fonts only by default: Arial, Aptos, Helvetica, Inter, or similar.
- Avoid serif fonts for PPT text unless the user explicitly asks.
- Use large, direct titles.
- Use small uppercase labels for section signals.
- Keep body text compact; move detail to speaker script.
- Card titles should usually be 18-22 pt when the card is a major slide element.
- Card body should usually be 14-18 pt when placed inside a visible card or panel.
- Do not use body text below 11 pt except footers, source notes, page numbers, or tiny section labels.
- Multi-line titles need real leading. Do not compress title lines to save vertical space.
- Keep a clear visual gap between title and subtitle; they should not read as one crowded block.

## Deck Shell

PPTPRO decks include a cover and closing slide by default.

Cover slide:

- Keep it minimal: title, presentation date, presenter.
- The date is the talk/report date. Do not use presentation duration, speaking length, or time limit as the date field.
- Add course, module, institution, or group only when the user provides it or the assignment expects it.
- Do not add thesis statements, agenda blocks, abstract text, decorative summaries, or case cards to the cover.
- Use the same visual language as the deck, but with fewer elements and calmer spacing.

Closing slide:

- Use only `Thank You` and `Questions & Discussion` by default.
- `Thank You` and `Questions` is also acceptable when a shorter ending fits better.
- Do not add presenter, contact, course, source, closing phrase, Q&A copy, or extra explanation.
- Keep the slide polished through spacing, type scale, and palette echo rather than extra content.

For partial-scope edits inside an existing deck:

- do not add a new cover or closing slide if the supplied deck already has the required shell or if the user is editing only a middle section
- do not delete or redesign preserved teammate, instructor, appendix, or economic/secondary sections
- when the final handoff is a full deck, inspect the complete page count and slide order after assembling preserved pages
- if preserved slides can only be appended as full-slide images, note that limitation in the audit, but keep them visually faithful

## Card And Panel Corners

Use softer rounded corners for PPTPRO's default visible containers.

- Use rounded rectangles for cards, callouts, panels, synthesis bars, evidence chips, and soft image masks unless a supplied template clearly uses square corners.
- Default visible cards should feel more rounded than PowerPoint's sharp rectangle default: use a medium-soft radius, roughly 0.12-0.18 in or 14-20% of the shorter side for normal cards.
- Use pill-level rounding only for short tags, labels, and chips. Do not make large analysis cards look like oversized pills.
- Keep the corner radius consistent within a slide family. A deck should not mix sharp boxes, lightly rounded cards, and pill cards without a clear hierarchy.
- If the deck is template-bound, preserve the template's corner language first, then subtly soften new cards only when it still looks continuous with the source file.

## Card Text Fit

Cards must be designed around the real rendered size of the text, not the intended copy length.

- Keep at least 0.16-0.24 in internal padding for normal cards; use more for large cards.
- Text boxes should sit fully inside the card safe area. Do not let the text box edge cross the card border.
- The visible last line must have room below it. Do not place body text so close to the bottom edge that descenders or line spacing appear clipped.
- If the text does not fit, repair in this order: shorten copy, widen the text box, increase card height, split into two cards, then reduce font size within the allowed range.
- Do not solve overflow by using tiny text. If a major card needs body text below 14 pt, the layout or copy is wrong.
- Long unbroken words, URLs, chemical names, and course codes must be given wider boxes or rewritten; do not allow them to push past borders.

## Visual Density And Balance

PPTPRO should feel open but not empty. Open space must frame content; it must not look like unused slide area.

Use these density rules before final rendering:

- Title/subtitle zone should normally take no more than the top 25-30% of the slide.
- The main content should occupy the middle and lower-middle canvas with clear visual weight.
- The lower 20-25% should contain a synthesis bar, takeaway, visual continuation, or intentional footer space.
- Avoid leaving the lower half blank unless the slide is a deliberate title/section divider.
- Avoid a large empty gulf between the main content row and the bottom synthesis/takeaway bar.
- If a bottom takeaway is used, connect the visual rhythm to it by lowering the main content, adding an intermediate evidence strip, or moving the takeaway upward.
- A visible card should have roughly 20-35% internal whitespace. If the whitespace is much larger, shrink the card or add structured content.
- A tall card or panel must contain more than a heading and one short sentence. Add comparison rows, evidence chips, a mini diagram, or split it into smaller cards.
- Text inside a card should feel vertically centered as a content block, not pinned to the upper-left corner.
- A row of cards should have similar perceived density. Do not let one card contain a paragraph while another contains one tiny line in the same-sized frame.
- Pill labels and tags must fit without wrapping. Increase width, reduce font size slightly, or use a stacked legend/list when labels are long.

## Title Rhythm

- Multi-line titles should use comfortable line spacing, usually about 1.10-1.22x.
- Do not let two title lines visually touch or feel stacked too tightly.
- Keep at least 0.14-0.22 in between a multi-line title and subtitle.
- If the title is long, reduce title size moderately, increase title box height, or rewrite the title before squeezing line spacing.
- Do not place the subtitle inside the title box unless the style is deliberately designed and visually spacious.

## Slide Patterns

### Concept Map

Use for reading concepts or definitions.

- Large thesis title.
- One short context sentence.
- Three step cards or concept cards.
- One or two takeaway statements.

### Process Flow

Use when the slide explains cause, sequence, or social mechanism.

- Four or fewer steps.
- Each step has a number, label, and short phrase.
- Connectors should clearly show direction.
- Avoid decorative dashes with unclear meaning.

### Media / Case Analysis

Use for recent media examples.

- Title names the media article/case.
- Three cards: article point, reading connection 1, reading connection 2.
- One synthesis bar.
- One discussion-question bar.

## Text Economy

- Slide title: 5-9 words if possible.
- Card title: 2-5 words.
- Card body: usually one sentence, preferably under 16 words.
- Footers: quiet and small.
- Script carries nuance; slides carry structure.

## Source Handling

If the assignment explicitly requires references, include a formal references slide or document section.

If not explicitly required, use `Sources used` for traceability rather than implying a formal bibliography requirement.

For source-backed presentations, keep sources matched to slide claims and avoid unsupported facts.

## Visual Enrichment Defaults

PPTPRO decks should feel visually developed, not like paragraphs distributed across cards.

- For text-heavy decks, create a visual enrichment plan before building: each content slide should be assigned a source visual, real/contextual image, generated illustration, diagram, map, icon cluster, mini chart, or an intentional text-only reason.
- Use images and illustrations regularly enough that the deck feels rich. As a default, aim for at least one meaningful visual anchor every 2-3 content slides and at least one visual-led slide per major section unless a template, assignment, or source constraint prevents it.
- Prefer content-specific visuals over decoration: source objects, place/event/object photos, maps, process scenes, concept illustrations, data figures, screenshots, or custom generated compositions tied to the slide message.
- Generated images are appropriate for conceptual scenes, process metaphors, atmosphere/context visuals, and object compositions when no real source or traceable image fits.
- Do not use generic stock-like imagery, vague decorative illustrations, or repeated icon-only filler to satisfy the visual plan.
- Keep text and visuals integrated: pair images with analysis rows, mechanism labels, comparison chips, or a short takeaway instead of placing images as background decoration.

## Audience-Facing Source Text

The deck itself should never expose internal project bookkeeping.

- Do not put workflow sentences on visible slides, in speaker notes intended for delivery, or in speaker scripts. Forbidden patterns include `source log`, `project source log`, `final audit`, `working audit`, `requirement ledger`, `provenance recorded`, `image credits are recorded`, and similar file-tracking language.
- Keep full source/image/generated-image provenance in working files, source logs, notes, or final audits outside the audience-facing deck.
- Visible source treatment should sound natural for a human-made presentation: concise footers such as `Source: WHO, 2024`, `Image: NASA`, `Data: World Bank`, or a normal `Sources used` slide.
- Do not write meta-disclaimers like `Full source provenance and image credits are recorded in the project source log` inside the PPT.
- If a formal references slide is required, list the actual references. If only traceability is needed, use a quiet `Sources used` section and omit internal workflow explanations.

## Generated Image Support

Use generated images selectively when they make the slide more specific and no real source-native or traceable supporting image is appropriate.

- Prefer source-native visuals and traceable external images first for evidence, real people, real places, events, documents, screenshots, products, and factual claims.
- Use Codex/ChatGPT's built-in image generation capability for custom conceptual scenes, process metaphors, atmosphere images, object/context illustrations, or abstract topic visuals that would otherwise be generic text.
- Select the current latest built-in image model/tool exposed by the environment. Do not hardcode a specific image model name in reusable project instructions; the default should move forward as the platform updates.
- Generated images must not replace original data figures, charts, source screenshots, official documents, logos, real-event evidence, or cited factual proof.
- Record generated-image provenance in the working audit, notes, or source log: tool/model, prompt summary, date, and intended slide role. Treat this as generated-asset provenance, not as a scholarly source.
- Reject generated images that look like filler, distort the topic, introduce false specificity, reduce readability, or make the deck look less credible.

## Report/Paper Data Figures

When a PPT is made from a report, essay, final paper, thesis, or manuscript, treat real data figures as source evidence, not decoration.

- First inventory the document's original evidence visuals: charts, data plots, survey result figures, model outputs, analytical screenshots, tables exported as images, and other real data images.
- Reuse the original figure/image asset in the PPT when the slide discusses that result.
- Preserve the original figure's data content, labels, scales, legend, and aspect ratio.
- Crop only margins, surrounding page whitespace, or irrelevant UI chrome. Do not crop out axes, labels, uncertainty marks, legends, captions needed for interpretation, or data points.
- Do not redraw, restyle, AI-generate, trace, or approximate the figure unless the user explicitly asks and the source data are available for faithful reconstruction.
- If the original figure is low resolution, extract it again from the source document/PDF before substituting a remake.
- Add a quiet figure caption/source note when the figure came from the report/paper or from an external cited source.
- If a source figure is omitted, record why: not relevant to the selected slide story, duplicated evidence, unreadable, or outside scope.

## Preview QA

After generating a deck:

1. Render or preview every slide.
2. Inspect for text overflow, clipping, overlap, text touching card borders, confusing marks, bad spacing, sparse cards, wrapped tags, tight title spacing, large vertical gaps, and uneven visual balance.
3. Compare slide messages with script markers.
4. For template-bound decks, compare revised slides with the source template style so the deck still feels continuous.
5. For partial-scope decks, confirm preserved slides are still present and in the locked order.
6. Fix and rerender until clean.

Do not hand off a deck based only on package/XML checks when a visual preview can be generated.

## Manual Visual Defect Sweep

After preview rendering, inspect every slide and answer:

- Does the slide have one obvious main message?
- Does the visual structure explain itself without narration?
- Are all text boxes comfortably inside their cards or regions?
- Does every card have a visible safe padding area around its text?
- Does the last line of every text box fit with vertical breathing room?
- Are multi-line titles and subtitles spaced comfortably?
- Is there a large empty gap between the main content and the lower takeaway?
- Does any label, card, or title feel cramped?
- Does any card or panel feel too empty for its size?
- Is the meaningful content distributed beyond the title area?
- Do pill labels and short tags fit on one line?
- Are connectors meaningful rather than decorative?
- Does the background avoid beige/cream AI-template styling?
- Is the slide/script relationship clear?

If any answer is weak, repair the deck and rerender.
