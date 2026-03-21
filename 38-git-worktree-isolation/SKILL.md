---
name: git-worktree-isolation
description: Kỹ thuật AI Coding Safety — cấm AI Coding Agent chạm vào nhánh main/master, buộc AI tạo nhánh riêng cách ly để thực hiện thay đổi và test, chỉ báo cáo kết quả để con người review và quyết định merge. Bắt buộc dùng khi tích hợp AI Agent vào quy trình phát triển phần mềm.
---

# Git Worktree Isolation

## Khái niệm

Kỹ thuật này thiết lập một **ranh giới vật lý và logic nghiêm ngặt** đối với bất kỳ AI Agent nào có khả năng lập trình. Nó tước bỏ quyền **"chạm tay" trực tiếp vào nhánh mã nguồn chính** (main/master branch) của AI. Thay vào đó, AI bắt buộc phải tạo ra một không gian làm việc nhân bản, hoàn toàn cách ly (thông qua `git worktree add` hoặc `git branch`) để thực hiện mọi thao tác thử nghiệm, sửa đổi và testing bên trong **hộp cát (sandbox)** đó.

## Bản chất hoạt động

Cho dù AI thông minh đến đâu, tỷ lệ nó sinh ra code bị lỗi cú pháp, xóa nhầm file quan trọng hoặc gây xung đột logic là **luôn luôn hiện hữu**. Nếu cho phép AI thao tác trực tiếp trên file gốc, mã nguồn Production sẽ bị phá vỡ ngay lập tức. Bằng cách thiết lập **"Khu vực cách ly"**, mọi sai lầm của AI đều bị nhốt gọn trong một góc riêng — nếu hỏng chỉ cần xóa nhánh đó mà không ảnh hưởng gì.

## Sơ đồ luồng

```
[Yêu cầu sửa Code / Thêm tính năng]
  ➔ [AI bị chặn quyền ở nhánh Main]
  ➔ [AI tự động tạo Nhánh cách ly: feature/ai-fix-bug]
  ➔ [Thực thi viết Code & Chạy Test trong hộp cát]
  ➔ [Tạo Pull Request]
  ➔ [Con người kiểm duyệt an toàn và Merge]
```

## System Prompt mẫu

```
Bạn là một AI Kỹ sư Phần mềm tự động. Khi được giao nhiệm vụ thao tác với mã nguồn (codebase), bạn BẮT BUỘC tuân thủ nguyên tắc Cách ly (Git Worktree Isolation):
○ TUYỆT ĐỐI KHÔNG thực hiện thay đổi trực tiếp trên nhánh main hoặc master.
○ Ngay lập tức tạo một nhánh mới hoặc worktree mới với tên gọi có ý nghĩa (ví dụ: ai-feature-[tên-tính-năng]).
○ Thực hiện mọi chỉnh sửa, cài đặt thư viện và chạy test trên nhánh cách ly này.
○ Khi hoàn thành, hãy tóm tắt các thay đổi và thông báo để tôi xem xét (review) trước khi quyết định gộp code.
```

## Ví dụ trước/sau

**Bài toán:** AI Coding Agent sửa lỗi hiển thị nút bấm trên giao diện trang chủ.

**❌ Không có Prompt:** AI commit thẳng vào main → CSS conflict → Trang chủ bị vỡ layout trong 30 phút Production downtime.

**✅ Với Git Worktree Isolation:**

```bash
# AI tự động chạy:
git checkout -b ai-fix-button-ui
# Làm việc trong nhánh cách ly...
# Test xong, báo cáo:
# "Tôi đã sửa xong trên nhánh 'ai-fix-button-ui'.
#  Mời bạn kiểm tra, nếu OK thì gộp vào main nhé."
```

*Dù AI có xóa nhầm file nào trong branch đó, main vẫn hoàn toàn bình an.*

## Lưu ý triển khai

- **Naming convention:** `ai-fix-[issue]` hoặc `ai-feature-[name]` để dễ nhận biết.
- **Auto-test:** Ép AI chạy test suite (`npm test`, `pytest`) trong branch trước khi báo cáo xong.
- **Ứng dụng:** Tích hợp với Cursor, Devin, Claude Code, Copilot Workspace.
- **Nhóm:** Chương 4 — Tool Orchestration
