---
status: "accepted"
date: "2024-08-01"
decision-makers: [bandarji]
consulted: []
informed: []
---

# Use Go as Primary Language

## Context and Problem Statement

Trebor Sux started as a collection of files to learn Pytest. After some time,
actual game development took place, using Python. Working on another project
using Go with ANSI for TUI controls, standardizing on Go as the primary
language for both projects makes sense.

## Considered Options

* Use Go as the primary language
* Continue development with Python
* Choose another language and framework

## Decision Outcome

Chosen option: "Use Go as the primary language", because we can reuse TUI
controls developed within another project, the language enforces strict
typing and can compile (more easily) for binary distribution.
