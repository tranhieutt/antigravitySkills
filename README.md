# 🌌 Antigravity System Skills Library (v7.0.1)

Đây là kho lưu trữ kỹ năng (skills) chính thức được cài đặt cho hệ thống Antigravity/Gemini trên máy tính này.

- **Tổng số thư mục kỹ năng**: 1,560 (Đã cập nhật bộ Anthropic, Sec, Game Dev, The Agency, Khoa học & Awesome Skills bổ sung)
- **Phiên bản hệ thống**: 7.0.1 (Base) + Custom Recovery + Update 2026-03-16
- **Ngày cập nhật cuối**: 2026-03-16
- **Nguồn gốc**:
  - [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) (Thêm vào 2026-03-15)
  - [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills)
  - [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) (Thêm vào 2026-03-10)

## 🤔 Kỹ năng (Skills) là gì?

Kỹ năng là các bộ hướng dẫn chuyên biệt dạy cho trợ lý AI cách xử lý các nhiệm vụ cụ thể. Hãy coi chúng là các module kiến thức chuyên gia mà AI có thể tải được khi cần.

### Mới cập nhật (03/2026) 🚀

Hệ thống vừa được nâng cấp với các bộ kỹ năng chuyên gia:

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

- `@antigravity-design-expert` - **(Mới)** Thiết kế giao diện không trọng lực, 3D CSS
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

### Planning & Workflow

- `@brainstorming` - Lên ý tưởng và thiết kế kiến trúc
- `@writing-plans` - Lập kế hoạch thực hiện dự án
- `@jobs-to-be-done` - Phân tích nhu cầu cốt lõi của người dùng
- `@planning-with-files` - Hệ thống lập kế hoạch dựa trên file

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

- **[2026-03-16] Auto-update Skills (Antigravity Workflow)**: Đồng bộ repo Awesome Skills và repo Khoa học, tự động cài đặt các thư mục kỹ năng còn thiếu. Tổng số thư mục kỹ năng đạt 1,560.
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
