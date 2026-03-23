---
name: cmd-loop-status
description: "ECC slash command: /loop-status"
source: everything-claude-code
date_added: '2026-03-23'
tags:
- command
- ecc
- slash-command
---

# /loop-status

> **ECC Command** — Gọi bằng \@cmd-loop-status\ trong Antigravity, hoặc \/loop-status\ trong Claude Code.

# Loop Status Command

Inspect active loop state, progress, and failure signals.

## Usage

`/loop-status [--watch]`

## What to Report

- active loop pattern
- current phase and last successful checkpoint
- failing checks (if any)
- estimated time/cost drift
- recommended intervention (continue/pause/stop)

## Watch Mode

When `--watch` is present, refresh status periodically and surface state changes.

## Arguments

$ARGUMENTS:
- `--watch` optional

