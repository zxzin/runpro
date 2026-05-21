# Efficiency Policy

Use this policy to prevent wasteful context growth and unnecessary tool usage.

## Core Principle

The skill should spend context only on information that is needed for the next concrete step.

Do not read, restate, or reload everything by default.

This policy never overrides:

- correctness
- truthfulness
- source sufficiency
- formatting compliance
- required validation

If efficiency conflicts with quality, choose quality.

## Default Efficiency Rules

- inventory first, then read selectively
- prefer route-specific references over generic broad reads
- summarize long source materials into working notes instead of repeatedly rereading raw inputs
- do not reopen the same files unless the project changed materially
- use scripts for inventory, routing, and validation rather than narrating those steps in full
- stop polishing low-value artifacts before the project has passed the core execution gates

## Context Budgeting

Prefer this order:

1. `project-inventory.md`
2. the highest-priority source files only
3. `project-routing.md`
4. `route-playbook.md`
5. route-specific reference

Do not load every reference file for every task.

## Source Budgeting

For source-backed work:

- gather enough real sources to support the assignment
- do not copy long source text into working memory unless needed
- record sources in `source-log.md`
- synthesize from the log and concise notes, not from repeated full-text rereads

## Output Budgeting

- first solve correctness
- then solve completeness
- only then spend tokens on polish

Avoid long meta-explanations when the next useful action is obvious.
