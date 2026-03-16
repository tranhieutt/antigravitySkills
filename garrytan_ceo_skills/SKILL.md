---
name: garrytan_ceo_skills
description: |
  Garry Tan's CEO & GStack skills suite. Combines 9 specialized workflow skills (plan-ceo-review, plan-eng-review, review, ship, qa, qa-only, browse, setup-browser-cookies, retro). Use this skill when the user asks to adopt founder/CEO mode, engineer manager mode, perform paranoid code reviews, QA testing with explicit scoring, automated shipping, or when explicitly requested to use Garry Tan's skills or gstack.
---

# Garry Tan's CEO Skills (GStack)

This is a unified skill bundling 9 opinionated and specialized workflows developed by Garry Tan for high-rigor planning, executing, and reviewing. 

## Supported Modes & Specialized Skills:

You have access to 9 sub-skills within this directory. **When using this skill or requested to perform one of these tasks, you MUST read the corresponding `SKILL.md` from its respective folder before proceeding.** 

1. **`/plan-ceo-review`** - *Founder / CEO Mode*: Rethink problems. Find the 10-star product. (Path: `C:\Users\x1 carbon\.gemini\antigravity\skills\garrytan_ceo_skills\plan-ceo-review\SKILL.md`)
2. **`/plan-eng-review`** - *Eng Manager / Tech Lead Mode*: Lock in architecture, edge cases, tests. (Path: `C:\Users\x1 carbon\.gemini\antigravity\skills\garrytan_ceo_skills\plan-eng-review\SKILL.md`)
3. **`/review`** - *Paranoid Staff Engineer Mode*: Catch bugs that pass CI but fail in production. (Path: `C:\Users\x1 carbon\.gemini\antigravity\skills\garrytan_ceo_skills\review\SKILL.md`)
4. **`/ship`** - *Release Engineer Mode*: Sync main, run tests, push branch, open PR. (Path: `C:\Users\x1 carbon\.gemini\antigravity\skills\garrytan_ceo_skills\ship\SKILL.md`)
5. **`/browse`** - *QA Engineer Mode*: Headless browser to test interactions. (Path: `C:\Users\x1 carbon\.gemini\antigravity\skills\garrytan_ceo_skills\browse\SKILL.md`)
6. **`/qa`** - *QA + Fix Engineer Mode*: Test app, find bugs, fix with atomic commits. (Path: `C:\Users\x1 carbon\.gemini\antigravity\skills\garrytan_ceo_skills\qa\SKILL.md`)
7. **`/qa-only`** - *QA Reporter Mode*: Same as `/qa` but without fixing. (Path: `C:\Users\x1 carbon\.gemini\antigravity\skills\garrytan_ceo_skills\qa-only\SKILL.md`)
8. **`/setup-browser-cookies`** - *Session Manager Mode*: Import real browser cookies to headless. (Path: `C:\Users\x1 carbon\.gemini\antigravity\skills\garrytan_ceo_skills\setup-browser-cookies\SKILL.md`)
9. **`/retro`** - *Engineering Manager Retro Mode*: Analyze team activity and performance. (Path: `C:\Users\x1 carbon\.gemini\antigravity\skills\garrytan_ceo_skills\retro\SKILL.md`)

## Implementation Instructions
- **To activate a mode**, use the `view_file` tool to read the specific `SKILL.md` provided in the path above and strictly follow its instructions.
- Tools like `browse` might require `bun` and compilation. If needed, the script is at `C:\Users\x1 carbon\.gemini\antigravity\skills\garrytan_ceo_skills\setup`.
