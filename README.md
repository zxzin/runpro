# Codex Academic Delivery Skills

Bilingual, source-grounded Codex skills for turning messy academic materials into submission-ready papers, revisions, and presentation decks.

This pack is built for English-first and bilingual workflows. Chinese trigger phrases are included where they are genuinely useful, but the core logic is not Chinese-only.

## What This Pack Does

Most prompt packs stop at drafting. This one is built around delivery closure:

1. reconstruct the real assignment or project scope from messy inputs
2. build from verified sources instead of backfilling citations later
3. audit writing against rubric, argument quality, and evidence quality
4. preserve native document formatting when reinserting revised text
5. produce visually strong, editable presentation decks from source-backed materials
6. strip workflow residue before final handoff

The result is a workflow stack for:

- papers
- reports
- literature reviews
- revisions after supervisor or teacher feedback
- paper-to-PPT and report-to-PPT work
- final submission cleanup

## Why This Is Different

- It is submission-grade, not prompt-snippet-grade.
- It treats source-claim integrity as a real quality gate.
- It treats tables, figures, and multi-panel visuals as part of the argument, not decoration.
- It includes format-preserving reinsertion instead of only rewriting.
- It includes a deck-production workflow, not just slide outlines.
- It is designed for English output, bilingual use, and academic handoff reality.

## Core Skills

### `runpro`
Project-folder orchestrator. Reconstructs requirements, locks scope, routes to the right specialist skill, enforces validation, and drives work to a real handoff state.

### `checkpro`
High-score academic audit. Checks rubric coverage, source-claim support, argument quality, synthesis, evidence hierarchy, figures/tables, and conservative readiness.

### `pptpro`
Strict editable PPT/PPTX production workflow. Builds non-generic decks, reuses real figures, enforces preview-and-repair loops, and keeps presentation outputs visually intentional.

### `replacewords`
Reinsert revised wording back into an original paper or document while preserving formatting, typography, paragraph settings, citation layout, and document conventions.

### `minimal-revision`
Minimal-change revision workflow for accepted drafts that need reviewer, supervisor, or teacher comments implemented without broad rewriting or unnecessary polishing.

### `final-delivery-clean`
Final-pass hygiene skill that removes workflow notes, engineering meta text, and process-facing language from deliverables before submission or handoff.

## Recommended Story

Do not market this repo as:

- a policy-evasion pack
- a generic writing prompt collection
- a China-only prompt set

Market it as:

> a bilingual academic delivery stack for Codex that goes from messy inputs to submission-ready outputs

The strongest story is the full chain:

`runpro -> checkpro -> replacewords / minimal-revision -> pptpro -> final-delivery-clean`

## Install

Copy the folders under `skills/` into your Codex skills directory:

```bash
mkdir -p "$CODEX_HOME/skills"
cp -R skills/* "$CODEX_HOME/skills/"
```

If your Codex setup uses `~/.codex/skills` directly:

```bash
mkdir -p ~/.codex/skills
cp -R skills/* ~/.codex/skills/
```

## Installation Safety

This repo uses the public skill names `runpro`, `checkpro`, `pptpro`, `replacewords`, `minimal-revision`, and `final-delivery-clean`.

If you already have customized skills with the same folder names in your local Codex setup, do not copy this pack over them unless you intentionally want to replace those local versions. Back up existing folders first, or install into a clean Codex profile.

The packaged repo itself is inert until copied into a Codex skills directory. Keeping it on the Desktop, publishing it to GitHub, or sharing the zip does not affect your active local skills.

## Suggested First Demos

See [DEMO_PROMPTS.md](./DEMO_PROMPTS.md).

If you only show one workflow publicly, show this one first:

1. a messy assignment folder
2. a rubric-aware audit
3. a final PPT with real figures
4. a DOCX reinsertion that preserves formatting

That demo sequence is more star-worthy than showing sentence rewriting alone.

## Repo Positioning

If you want the broadest appeal, use an English-facing public name and description even if many users are bilingual.

Strong public name candidates:

- `codex-academic-delivery-skills`
- `submission-ready-skills`
- `paper-to-ppt-delivery-stack`

Recommended short description:

> Bilingual Codex skills for source-grounded academic writing, audit, format-preserving revision, paper-to-PPT delivery, and final submission cleanup.

## Included Directory Layout

```text
skills/
  checkpro/
  final-delivery-clean/
  minimal-revision/
  pptpro/
  replacewords/
  runpro/
```
