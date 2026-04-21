# 🌌 Antigravity System Skills Library (v7.3.0)

Đây là kho lưu trữ kỹ năng (skills) chính thức được cài đặt cho hệ thống Antigravity/Gemini trên máy tính này.

- **Tổng số thư mục kỹ năng**: 1,833 ⭐ **(+27 skills mới - 2026-04-21)**
- **Phiên bản hệ thống**: 7.3.0 — ECC Integration
- **Ngày cập nhật cuối**: 2026-04-21
- **Nguồn gốc**:
  - [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) ⭐ **(Mới nhất - v7.3.0)** (Thêm vào 2026-03-23) — 27 agents + 99 skills
  - [github/spec-kit](https://github.com/github/spec-kit) (Thêm vào 2026-03-22)
  - [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) (Thêm vào 2026-03-15)
  - [K-Dense-AI/claude-scientific-writer](https://github.com/K-Dense-AI/claude-scientific-writer) (Thêm vào 2026-03-16)
  - [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills)
  - [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) (Thêm vào 2026-03-10)

## 🤔 Kỹ năng (Skills) là gì?

Kỹ năng là các bộ hướng dẫn chuyên biệt dạy cho trợ lý AI cách xử lý các nhiệm vụ cụ thể. Hãy coi chúng là các module kiến thức chuyên gia mà AI có thể tải được khi cần.

### Mới cập nhật (04/2026) 🚀

Thêm 27 kỹ năng mới bao gồm phát triển mobile, design, AI tools, và nhiều hơn nữa:

- **Mobile Development**: `android-native-dev`, `flutter-dev`, `ios-application-dev`, `react-native-dev`, `react-native-skills`
- **Web Development**: `fullstack-dev`, `frontend-dev`, `refactor`, `shader-dev`
- **Design & UI**: `awesome-design-md`, `bencium-controlled-ux-designer`, `bencium-innovative-ux-designer`, `composition-patterns`, `contrast-checker`, `use-of-color`
- **AI & Multimedia**: `minimax-docx`, `minimax-multimodal-toolkit`, `minimax-music-gen`, `minimax-music-playlist`, `minimax-pdf`, `minimax-xlsx`, `vision-analysis`
- **Other Tools**: `buddy-sings`, `gif-sticker-maker`, `link-purpose`, `pptx-generator`, `travel-optimization-engine`

### Mới cập nhật (03/2026) 🚀

Hệ thống vừa được nâng cấp với các bộ kỹ năng chuyên gia:

- **Everything Claude Code Integration** ⭐ **(Mới nhất - v7.3.0)**: Tích hợp toàn bộ **185 components** từ repo [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) — bao gồm:
  - **27 specialized agents** (`@planner`, `@architect`, `@tdd-guide`, `@security-reviewer`, `@code-reviewer`...)
  - **99 workflow skills** (AI/Agent, Backend, Frontend, Language Patterns, Security, Content...)
  - **59 slash commands** dạng `@cmd-*` (`@cmd-plan`, `@cmd-tdd`, `@cmd-code-review`, `@cmd-orchestrate`, `@cmd-go-review`...)
  - **12 rule folders** (common, typescript, python, golang, java, kotlin, rust, swift, cpp, csharp, php, perl)
  - Tổng số skills tăng lên **1,806**.
- **Spec-Kit SDD Workflow** *(v7.2.0)*: 9 skill Spec-Driven Development từ `github/spec-kit`. CLI tool `specify` (v0.3.2) đã được cài qua `uv`.
- **52 System Prompt Techniques** *(v7.1.0)*: 52 kỹ thuật Prompt Engineering chuyên sâu từ `strangecrab091/52systemprompt`, chia thành 6 chương — Cognitive Frameworks, Expert Personas, Coding Techniques, Tool Orchestration, Reflexion & Evaluation, Meta & Security. Xem danh sách đầy đủ bên dưới.
- **The Agency**: Nhập 68 agent chuyên biệt mới từ bộ `agency-agents` (VD: `@agency-frontend-developer`, `@agency-ux-researcher`, `@agency-growth-hacker`, v.v.) hoạt động như một công ty thực thụ.
- **AI Thinkers**: `@yann-lecun`, `@geoffrey-hinton`, `@ilya-sutskever`, `@andrej-karpathy`.
- **Tech Icons**: `@elon-musk`, `@bill-gates`, `@steve-jobs`, `@sam-altman`.
- **Anthropic/Claude Tools**: `@claude-code-expert`, `@claude-monitor`.
- **Advanced Development**: `@tanstack-query-expert`, `@antigravity-design-expert`, `@vercel-ai-sdk-expert`.

---

## 📂 Cấu trúc thư mục

Mỗi kỹ năng nằm trong thư mục riêng với cấu trúc:

```text
skills/
├── tên-kỹ-năng/             # Thư mục kỹ năng riêng lẻ
│   ├── SKILL.md             # Định nghĩa chính (bắt buộc)
│   ├── scripts/             # Script hỗ trợ (tùy chọn)
│   ├── examples/            # Ví dụ sử dụng (tùy chọn)
```

---

## Cách sử dụng

Sử dụng ký hiệu `@` kèm theo tên kỹ năng trong cửa sổ chat:

```text
@brainstorming giúp tôi thiết kế ứng dụng quản lý chi tiêu
```

---

## Danh mục kỹ năng tiêu biểu

### Creative & Design

- `@frontend_dev_ui_skill` - **(Mới)** Kiến trúc sư UI/UX Frontend cao cấp, tạo giao diện "đắt tiền" và loại bỏ lối mòn thiết kế AI
- `@antigravity-design-expert` - Thiết kế giao diện không trọng lực, 3D CSS
- `@ui-ux-pro-max` - Thiết kế UI/UX chuyên sâu
- `@algorithmic-art` - Nghệ thuật thuật toán với p5.js
- `@canvas-design` - Thiết kế poster và tác phẩm nghệ thuật

### Development & Engineering

- `@claude-code-expert` - **(Mới)** Tối ưu hóa việc sử dụng Claude Code CLI
- `@tanstack-query-expert` - **(Mới)** Quản lý async state chuyên sâu
- `@test-driven-development` - Lập trình hướng kiểm thử (TDD)
- `@systematic-debugging` - Gỡ lỗi hệ thống bài bản

### Security & Auditing

- `@007` - **(Mới)** Audit bảo mật, hardening và threat modeling cấp cao
- `@audit-skills` - **(Mới)** Quét mã độc và lỗ hổng trong các bộ Skill
- `@api-security-best-practices` - Bảo mật API theo chuẩn OWASP
- `@vulnerability-scanner` - Quét lỗ hổng bảo mật

### Game Development (Mới)

Hệ thống hiện hỗ trợ đầy đủ các mảng phát triển game chuyên sâu:

- `@game-development/3d-games` - Phát triển game 3D
- `@game-development/multiplayer` - Xây dựng game nhiều người chơi
- `@game-development/game-design` - Thiết kế cơ chế và lối chơi

### 🌱 Spec-Driven Development (Mới - v7.2.0)

> **Yêu cầu**: Phải chạy `specify init --here --ai agy --ai-skills` trong thư mục dự án trước khi dùng.

- `@speckit-constitution` - Tạo nguyên tắc/hiến pháp dự án (bước đầu tiên)
- `@speckit-specify` - Viết spec từ mô tả ngôn ngữ tự nhiên (Generated/Given/When/Then)
- `@speckit-clarify` - Hỏi câu hỏi làm rõ trước khi plan (giảm rework)
- `@speckit-plan` - Tạo kế hoạch kỹ thuật chi tiết (tech stack, architecture)
- `@speckit-analyze` - Kiểm tra nhất quán giữa spec/plan/tasks
- `@speckit-tasks` - Breakdown thành task list có dependency và parallel markers
- `@speckit-checklist` - Tạo quality checklist kiểm tra completeness
- `@speckit-implement` - Thực thi tất cả tasks theo thứ tự
- `@speckit-taskstoissues` - Convert tasks thành GitHub Issues
- `@speckit-updater` - Cập nhật spec-kit lên phiên bản mới nhất

### Planning & Workflow

- `@brainstorming` - Lên ý tưởng và thiết kế kiến trúc
- `@writing-plans` - Lập kế hoạch thực hiện dự án
- `@jobs-to-be-done` - Phân tích nhu cầu cốt lõi của người dùng
- `@planning-with-files` - Hệ thống lập kế hoạch dựa trên file

### 🧠 System Prompt Techniques (Mới - v7.1.0)

52 kỹ thuật Prompt Engineering được tách riêng theo 6 chương, kích hoạt tự động khi phù hợp:

**Chương 1 — Cognitive Frameworks & Reasoning:**

- `@01-step-by-step-explicit` - Chain of Thought, suy luận từng bước
- `@02-master-plan-and-solve` - Lập kế hoạch tổng thể trước khi thực thi
- `@04-tri-agent-deliberation` - Tree of Thoughts, 3 chuyên gia tranh luận
- `@08-ooda-loop-analyzer` - Phân tích theo vòng lặp OODA
- `@09-first-principles-deconstruction` - Tư duy First Principles (Elon Musk)
- `@10-second-order-thinking` - Tư duy Bậc hai (Howard Marks)
- `@13-pre-action-thinking` - Scratchpad `<thinking>` trước khi trả lời

**Chương 2 — Expert Persona Generation:**

- `@14-phd-level-systems-engineer` - Kỹ sư Hệ thống PhD 20 năm kinh nghiệm
- `@15-fintech-ui-ux-architect` - Kiến trúc sư UI/UX Fintech
- `@16-threat-intel-red-blue-team` - Red Team + Blue Team song song
- `@17-compliance-navigator` - Chuyên gia Tuân thủ pháp lý
- `@18-eval-coach-llmops` - LLM-as-a-Judge cho LLMOps pipeline
- `@19-creative-ad-legend` - Copywriter huyền thoại (David Ogilvy style)

**Chương 3 — Coding & Data Analysis:**

- `@25-no-owasp-top10` - Cấm code có lỗ hổng OWASP Top 10
- `@26-file-overwrite-prevention` - Ngăn AI dùng placeholder khi sửa file
- `@31-data-analysis-execution` - Bắt buộc viết code Python/SQL thay vì tính nhẩm
- `@33-browser-element-chunking` - Web scraping theo chunks HTML
- `@34-headless-shell-automation` - CLI Agent, viết script tự động

**Chương 4 — Tool Orchestration:**

- `@35-parallel-execution-bias` - Gọi tools song song (Promise.all)
- `@36-sequential-dependency` - Đảm bảo tool B chờ output của tool A
- `@37-orchestrator-worker-mesh` - Multi-Agent Orchestrator + Workers
- `@38-git-worktree-isolation` - Cấm AI chạm vào nhánh main
- `@40-escalation-routing-rule` - Chuyển sang nhân viên người thật khi cần

**Chương 5 — Reflexion & Evaluation:**

- `@42-actor-evaluator-dualism` - Self-critique: Actor viết → Evaluator chê → viết lại
- `@43-excellence-rubric-form` - Chấm điểm theo Rubric 1-5
- `@46-pre-mortem-simulation` - Giả định dự án đã thất bại, tìm nguyên nhân
- `@47-token-limit-watcher` - Tự động dừng trước khi chạm trần token

**Chương 6 — Meta-prompting & Security:**

- `@49-meta-prompt-factory` - AI tự viết System Prompt tối ưu
- `@50-strict-xml-encapsulation` - Ngăn Prompt Injection bằng XML tags
- `@51-system-hierarchy-shield` - Bảo vệ System Prompt khỏi Jailbreak
- `@52-output-verbosity-restraint` - Output thuần túy cho API/UI

---

## Tìm kiếm kỹ năng

Bạn có thể tìm kiếm bằng cách xem danh sách trong thư mục này hoặc xem file [main README](../README.md).

---

## 💡 Popular Skills to Try

**For beginners:**

- `@brainstorming` - Design before coding
- `@systematic-debugging` - Fix bugs methodically
- `@git-pushing` - Commit with good messages

**For developers:**

- `@test-driven-development` - Write tests first
- `@react-best-practices` - Modern React patterns
- `@senior-fullstack` - Full-stack development

**For security:**

- `@ethical-hacking-methodology` - Security basics
- `@burp-suite-testing` - Web app security testing

---

## Creating Your Own Skill

Want to create a new skill? Check out:

1. [CONTRIBUTING.md](../CONTRIBUTING.md) - How to contribute
2. [docs/SKILL_ANATOMY.md](../docs/SKILL_ANATOMY.md) - Skill structure guide
3. `@skill-creator` - Use this skill to create new skills!

**Basic structure:**

```markdown
---
name: my-skill-name
description: "What this skill does"
---

# Skill Title

## Overview
[What this skill does]

## When to Use
- Use when [scenario]

## Instructions
[Step-by-step guide]

## Examples
[Code examples]
```

---

## Documentation

- **[Getting Started](../docs/users/getting-started.md)** - Quick start guide
- **[Examples](../docs/contributors/examples.md)** - Real-world usage examples
- **[FAQ](../docs/users/faq.md)** - Common questions
- **[Visual Guide](../docs/users/visual-guide.md)** - Diagrams and flowcharts

---

## 🌟 Contributing

Found a skill that needs improvement? Want to add a new skill?

1. Read [CONTRIBUTING.md](../CONTRIBUTING.md)
2. Study existing skills in this folder
3. Create your skill following the structure
4. Submit a Pull Request

---

## 📜 Lịch sử cập nhật (History)

- **[2026-03-23] v7.3.0 — Everything Claude Code Full Integration**: Tích hợp đầy đủ repo [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) qua 4 bước:
  - **Agents (27)**: Cài 27 ECC core agents — `architect`, `planner`, `tdd-guide`, `security-reviewer`, `code-reviewer`, `build-error-resolver`, `e2e-runner`, `refactor-cleaner`, `typescript-reviewer`, `python-reviewer`, `rust-reviewer`, `go-reviewer`, `java-reviewer`, `kotlin-reviewer`, `flutter-reviewer`, `cpp-reviewer`, `database-reviewer`, `doc-updater`, `docs-lookup`, `loop-operator`, `chief-of-staff`, `harness-optimizer`, `java/kotlin/rust/go/pytorch-build-resolver`.
  - **Skills (99)**: Cài 99 ECC workflow skills — `backend-patterns`, `api-design`, `frontend-patterns`, `golang-*`, `kotlin-*`, `springboot-*`, `django-*`, `laravel-*`, `swift-*`, `perl-*`, `continuous-learning`, `autonomous-loops`, `eval-harness`, `security-review`, v.v.
  - **Commands (59)**: Convert 59 ECC slash commands thành skills với prefix `cmd-*` — `@cmd-plan`, `@cmd-tdd`, `@cmd-code-review`, `@cmd-build-fix`, `@cmd-orchestrate`, `@cmd-go-review`, `@cmd-learn`, `@cmd-save-session`, `@cmd-loop-start`, `@cmd-devfleet`, v.v.
  - **Rules (12 folders)**: Copy 12 rule folders vào `Rule/` — `common`, `typescript`, `python`, `golang`, `java`, `kotlin`, `rust`, `swift`, `cpp`, `csharp`, `php`, `perl` — mỗi folder chứa 5 rules: `coding-style`, `hooks`, `patterns`, `security`, `testing`.
  - **Audit**: Quét 1,648 skills — 85.9% CLEAN, 0 malicious. Convert `007` skill từ Bồ Đào Nha → Tiếng Anh.
  - Tổng số thư mục kỹ năng đạt **1,806**.

- **[2026-03-22] v7.2.0 — Tích hợp GitHub Spec-Kit (Spec-Driven Development)**: Cài đặt thành công `specify-cli v0.3.2` (GitHub official tool) via `uv tool install`. Khởi tạo project với `--ai agy --ai-skills` tạo ra 9 skill files trong `.agent/skills/`. Copy toàn bộ 9 skills vào hệ thống Antigravity global: `speckit-constitution`, `speckit-specify`, `speckit-clarify`, `speckit-plan`, `speckit-analyze`, `speckit-tasks`, `speckit-checklist`, `speckit-implement`, `speckit-taskstoissues`. Workspace tại `D:\Github-Spec-Kit` đã có đầy đủ `.specify/` directory với templates, scripts (PowerShell), và constitution.md. Tổng số thư mục kỹ năng đạt **1,621**.
- **[2026-03-21] v7.1.0 — Thêm 52 System Prompt Skills**: Tích hợp thành công toàn bộ 52 kỹ thuật Prompt Engineering từ bài viết `strangecrab091.github.io/52systemprompt` vào hệ thống skills. Bao gồm 6 chương: Cognitive Frameworks, Expert Personas, Coding Techniques, Tool Orchestration, Reflexion & Evaluation, và Meta & Security. Mỗi skill có SKILL.md đầy đủ với System Prompt mẫu, Before/After examples, và sơ đồ luồng. Tổng số thư mục kỹ năng đạt **1,613**.
- **[2026-03-17] Thêm kỹ năng Frontend UI/UX Premium**: Tổng hợp và xây dựng thành công kỹ năng `@frontend_dev_ui_skill` (từ dự án taste-skill) giúp AI tự động thiết kế UI/UX cao cấp, chống lại phong cách mặc định nhàm chán. Tổng số thư mục kỹ năng đạt 1,561.
- **[2026-03-16] Auto-update Skills (Antigravity Workflow)**: Đồng bộ repo `antigravity-awesome-skills` và tích hợp nhóm thư mục kỹ năng báo cáo khoa học từ `K-Dense-AI/claude-scientific-writer`, tự động cài đặt các thư mục kỹ năng còn thiếu. Tổng số thư mục kỹ năng đạt 1,560.
- **[2026-03-15] Cập nhật kỹ năng Khoa học**: Nạp thành công hơn 150+ kỹ năng từ repository `K-Dense-AI/claude-scientific-skills`. Tổng số lượng kỹ năng tăng lên 1,551 thư mục kỹ năng.
- **[2026-03-12] Cập nhật kỹ năng mới**: Đồng bộ hóa và cập nhật thêm 16 kỹ năng mới từ repository `sickn33/antigravity-awesome-skills`. Tổng cộng 1,398 thư mục kỹ năng hiện tại trải dài trên nhiều lĩnh vực.
- **[2026-03-10] Cập nhật "The Agency"**: Trích xuất và cài đặt thành công 68 agents (bao gồm Design, Engineering, Marketing, v.v...) từ nguồn `msitarzewski/agency-agents` dưới dạng skill, cho phép hệ thống vận hành theo mô hình Multi-Agent khép kín.
- **[2026-03-10] Cập nhật Core Awesome Skills**: Download và nâng cấp kho skill diện rộng với danh sách hơn 1,200+ kỹ năng từ [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills). Đợt này bổ sung các nhóm skill đặc biệt: *AI Thinkers*, *Tech Icons*, *Advanced Development*, *Security 007*, và *Game Dev*.

---

## References

- [Anthropic Skills](https://github.com/anthropic/skills) - Official Anthropic skills
- [UI/UX Pro Max Skills](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) - Design skills
- [Superpowers](https://github.com/obra/superpowers) - Original superpowers collection
- [Planning with Files](https://github.com/OthmanAdi/planning-with-files) - Planning patterns
- [NotebookLM](https://github.com/PleasePrompto/notebooklm-skill) - NotebookLM integration

---

**Need help?** Check the [FAQ](../docs/FAQ.md) or open an issue on GitHub!
