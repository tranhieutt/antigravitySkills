---
name: file-overwrite-prevention
description: Kỹ thuật ngăn chặn mất code — cấm AI dùng placeholder (..., // existing code) khi chỉnh sửa file, bắt buộc trả về toàn bộ nội dung file hoặc dùng định dạng Search/Replace block chính xác. Bắt buộc dùng trong Agentic Workflows nơi AI có quyền ghi đè file gốc.
---

# File Overwrite Prevention

## Khái niệm

Kỹ thuật này thiết lập một **rào cản hành vi nghiêm ngặt**, cấm AI được phép "lười biếng". Nó ngăn chặn LLM sử dụng các đoạn mã giữ chỗ (placeholders), ép AI phải:

- In ra **toàn bộ nội dung tệp tin nguyên vẹn**, hoặc
- Sử dụng định dạng **"Tìm kiếm & Thay thế" (Search/Replace blocks)** cực kỳ chuẩn xác

Để không làm hỏng các logic đang hoạt động.

## Bản chất hoạt động

LLM có giới hạn về output tokens và thường tối ưu hóa để tiết kiệm tài nguyên. Khi đối mặt với file 1000 dòng mà chỉ cần sửa 5 dòng, bản năng AI là dùng `...` để lấp liếm phần còn lại. Trong **Agentic Workflow** cho phép AI trực tiếp ghi đè file gốc → thói quen này sẽ **xóa sạch toàn bộ hệ thống**.

## Sơ đồ luồng

```
[Yêu cầu sửa tính năng trong File lớn]
  ➔ [AI Đọc nguyên trạng File]
  ➔ [Kích hoạt kỷ luật: Cấm dùng placeholder]
  ➔ [AI tạo Search/Replace block HOẶC in ra 100% nội dung File]
  ➔ [Ghi đè File an toàn, không mất dữ liệu]
```

## System Prompt mẫu

```
Bạn là một Trợ lý Lập trình/Quản trị hệ thống cực kỳ cẩn thận. Khi tôi yêu cầu bạn chỉnh sửa một tệp tin (file) hoặc một đoạn mã nguồn, bạn BẮT BUỘC tuân thủ luật sau:
○ TUYỆT ĐỐI KHÔNG SỬ DỤNG CÁC ĐOẠN GIỮ CHỖ như // ... rest of the code ..., // existing code here, hay ....
○ Bạn phải cung cấp lại toàn bộ nội dung file từ dòng đầu đến dòng cuối sau khi đã sửa xong.
○ Nếu file quá dài, hãy sử dụng định dạng Khối Tìm kiếm/Thay thế chính xác:
  <<<< SEARCH
  [Code cũ nguyên bản]
  ====
  REPLACE
  [Code mới]
```

## Ví dụ trước/sau

**Bài toán:** File `PlanetGridModule` dài 500 dòng, cần thêm logic xử lý event `EVENT_BOSS_PASSED`.

**❌ Không có Prompt — Thảm họa:**

```javascript
class PlanetGridModule {
  // ... existing code ...
  handleBossEvent() { /* new code */ }
}
```

*→ Nếu AI Agent Apply code này → 500 dòng bị xóa sạch → Game crash*

**✅ Với File Overwrite Prevention:**

```
<<<< SEARCH
  initPlanet(id, x, y) {
====
REPLACE
  subscribeToEvent(EVENT_BOSS_PASSED, (bossPos) => {
    this.markPlanetDamaged(bossPos);
  });
  initPlanet(id, x, y) {
```

*→ Code được chèn vào đúng vị trí, 500 dòng còn lại bình an*

## Lưu ý triển khai

- **Bắt buộc** trong mọi Agentic Coding workflow (Cursor, Cline, Claude Code...).
- **Search block:** Phải là code cũ nguyên bản — AI không được tự ý thay đổi phần SEARCH.
- **Nhóm:** Chương 3 — Kỹ thuật Lập trình & Phân tích Dữ liệu
