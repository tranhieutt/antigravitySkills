---
name: cmd-claw
description: "Start NanoClaw v2 â€” ECC"
source: everything-claude-code
date_added: '2026-03-23'
tags:
- command
- ecc
- slash-command
---

# /claw

> **ECC Command** — Gọi bằng \@cmd-claw\ trong Antigravity, hoặc \/claw\ trong Claude Code.

---
description: Start NanoClaw v2 â€” ECC's persistent, zero-dependency REPL with model routing, skill hot-load, branching, compaction, export, and metrics.
---

# Claw Command

Start an interactive AI agent session with persistent markdown history and operational controls.

## Usage

```bash
node scripts/claw.js
```

Or via npm:

```bash
npm run claw
```

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `CLAW_SESSION` | `default` | Session name (alphanumeric + hyphens) |
| `CLAW_SKILLS` | *(empty)* | Comma-separated skills loaded at startup |
| `CLAW_MODEL` | `sonnet` | Default model for the session |

## REPL Commands

```text
/help                          Show help
/clear                         Clear current session history
/history                       Print full conversation history
/sessions                      List saved sessions
/model [name]                  Show/set model
/load <skill-name>             Hot-load a skill into context
/branch <session-name>         Branch current session
/search <query>                Search query across sessions
/compact                       Compact old turns, keep recent context
/export <md|json|txt> [path]   Export session
/metrics                       Show session metrics
exit                           Quit
```

## Notes

- NanoClaw remains zero-dependency.
- Sessions are stored at `~/.claude/claw/<session>.md`.
- Compaction keeps the most recent turns and writes a compaction header.
- Export supports markdown, JSON turns, and plain text.

