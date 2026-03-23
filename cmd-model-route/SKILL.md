---
name: cmd-model-route
description: "ECC slash command: /model-route"
source: everything-claude-code
date_added: '2026-03-23'
tags:
- command
- ecc
- slash-command
---

# /model-route

> **ECC Command** — Gọi bằng \@cmd-model-route\ trong Antigravity, hoặc \/model-route\ trong Claude Code.

# Model Route Command

Recommend the best model tier for the current task by complexity and budget.

## Usage

`/model-route [task-description] [--budget low|med|high]`

## Routing Heuristic

- `haiku`: deterministic, low-risk mechanical changes
- `sonnet`: default for implementation and refactors
- `opus`: architecture, deep review, ambiguous requirements

## Required Output

- recommended model
- confidence level
- why this model fits
- fallback model if first attempt fails

## Arguments

$ARGUMENTS:
- `[task-description]` optional free-text
- `--budget low|med|high` optional

