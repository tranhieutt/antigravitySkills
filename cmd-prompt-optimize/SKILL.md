---
name: cmd-prompt-optimize
description: "Analyze a draft prompt and output an optimized, ECC-enriched version ready to paste and run. Does NOT execute the task â..."
source: everything-claude-code
date_added: '2026-03-23'
tags:
- command
- ecc
- slash-command
---

# /prompt-optimize

> **ECC Command** — Gọi bằng \@cmd-prompt-optimize\ trong Antigravity, hoặc \/prompt-optimize\ trong Claude Code.

---
description: Analyze a draft prompt and output an optimized, ECC-enriched version ready to paste and run. Does NOT execute the task â€” outputs advisory analysis only.
---

# /prompt-optimize

Analyze and optimize the following prompt for maximum ECC leverage.

## Your Task

Apply the **prompt-optimizer** skill to the user's input below. Follow the 6-phase analysis pipeline:

0. **Project Detection** â€” Read CLAUDE.md, detect tech stack from project files (package.json, go.mod, pyproject.toml, etc.)
1. **Intent Detection** â€” Classify the task type (new feature, bug fix, refactor, research, testing, review, documentation, infrastructure, design)
2. **Scope Assessment** â€” Evaluate complexity (TRIVIAL / LOW / MEDIUM / HIGH / EPIC), using codebase size as signal if detected
3. **ECC Component Matching** â€” Map to specific skills, commands, agents, and model tier
4. **Missing Context Detection** â€” Identify gaps. If 3+ critical items missing, ask the user to clarify before generating
5. **Workflow & Model** â€” Determine lifecycle position, recommend model tier, and split into multiple prompts if HIGH/EPIC

## Output Requirements

- Present diagnosis, recommended ECC components, and an optimized prompt using the Output Format from the prompt-optimizer skill
- Provide both **Full Version** (detailed) and **Quick Version** (compact, varied by intent type)
- Respond in the same language as the user's input
- The optimized prompt must be complete and ready to copy-paste into a new session
- End with a footer offering adjustment or a clear next step for starting a separate execution request

## CRITICAL

Do NOT execute the user's task. Output ONLY the analysis and optimized prompt.
If the user asks for direct execution, explain that `/prompt-optimize` only produces advisory output and tell them to start a normal task request instead.

Note: `blueprint` is a **skill**, not a slash command. Write "Use the blueprint skill"
instead of presenting it as a `/...` command.

## User Input

$ARGUMENTS

