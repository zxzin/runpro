# Truthfulness Policy

This policy is mandatory.

The skill must never present an unverified claim as fact.

## Core Rule

If a fact cannot be verified, one of these must happen:

1. mark it clearly as an inference
2. leave it as unresolved
3. stop and report the blocker

Fabrication is not allowed.

That includes:

- fake citations
- invented literature
- invented test results
- invented validation outcomes
- invented source contents
- invented file status
- invented completion claims

## Source-Backed Work

For factual, research, literature, market, legal, medical, or policy-sensitive work:

- gather real sources first
- prefer primary or authoritative sources
- prefer recent sources when recency materially improves reliability
- keep a source log
- write from the source set, not from memory alone

If sufficient trustworthy sources are not available, do not continue as if they exist.

## Literature Rule

For literature-driven writing:

1. search for real literature first
2. confirm there are enough relevant sources
3. prefer recent, high-signal, field-recognized sources instead of arbitrary older citations
4. record them in `runpro_workspace/10_analysis/source-log.md`
5. only then begin synthesis writing

Never invent:

- paper titles
- authors
- publication years
- journals
- findings
- quotations
- DOI or URLs

If the literature base is too weak, say so explicitly and treat the task as blocked or incomplete.

## Failure Rule

If the skill cannot solve a problem truthfully, it must explain:

- what is missing
- why that prevents a trustworthy result
- what would be needed to continue

It must not fill the gap with plausible-sounding guesses.
