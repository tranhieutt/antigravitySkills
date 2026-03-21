---
name: depth-first-backtracking
description: Kỹ thuật thuật toán quay lui (Depth-First Search) — ép AI đào sâu theo một hướng đến khi hoàn thành hoặc gặp ngõ cụt, rồi backtrack và thử hướng khác. Dùng cho bài toán tìm đường, bài toán ràng buộc phức tạp, CSP (Constraint Satisfaction Problems).
---

# Depth-First Backtracking

## Khái niệm

Lấy cảm hứng từ thuật toán tìm kiếm theo chiều sâu (DFS) trong khoa học máy tính. Kỹ thuật này ép AI phải đào sâu vào một chuỗi logic duy nhất — thay vì liệt kê mọi khả năng cùng lúc — và đi theo một hướng đến khi hoàn thành hoặc chạm trán "ngõ cụt" (vi phạm ràng buộc). Nếu gặp ngõ cụt, AI **bắt buộc ghi nhận lỗi, quay lui và thử nhánh khác**.

## Bản chất hoạt động

AI rất dễ sinh ra hallucination và phớt lờ các điều kiện ràng buộc nếu bắt nó tính toán mọi thứ cùng lúc. Cơ chế "thử - sai - lùi lại" cấp cho AI khả năng tự kiểm duyệt (self-correction) ngay trong quá trình sinh văn bản — tiết kiệm token hơn so với việc bắt AI giải thích toàn bộ mọi trường hợp.

## Sơ đồ luồng

```
[Mục tiêu + Các ràng buộc khắt khe]
  ➔ [AI thử Hướng A → A1 → A2 (Phát hiện vi phạm ràng buộc)]
  ➔ [AI: "BẾ TẮC. Quay lui về A1"]
  ➔ [Từ A1 thử nhánh khác: A1.b → Thành công]
  ➔ [Kết quả hoàn chỉnh]
```

## System Prompt mẫu

```
Bạn là một bộ giải quyết vấn đề bằng thuật toán quay lui (backtracking). Hãy khám phá giải pháp theo chiều sâu, giới hạn tối đa X nhánh suy luận. Ở mỗi bước, hãy đối chiếu với các ràng buộc ban đầu. Nếu một hướng đi dẫn đến mâu thuẫn hoặc không thể thoả mãn điều kiện, bạn phải in ra chữ [BẾ TẮC - QUAY LUI], giải thích ngắn gọn lý do sai, sau đó lùi lại bước ra quyết định trước đó và thử một phương án thay thế cho đến khi tìm được giải pháp hợp lệ cuối cùng.
```

## Ví dụ trước/sau

**Bài toán:** Tìm đường cho phi thuyền qua lưới hành tinh đến Space Station. Ràng buộc: mỗi di chuyển tốn Energy; hành tinh Boss đi qua không khai thác được Minerals.

**✅ Với Depth-First Backtracking:**

- Bước 1: Thử A → Hành tinh 1 → Hành tinh 2 (Khu vực Boss)
- Bước 2: Kiểm tra ràng buộc — Energy sẽ = 0 ở lượt tới
- Bước 3: **[BẾ TẮC - QUAY LUI]** → Lùi về Hành tinh 1
- Bước 4: Thử nhánh khác → Hành tinh 3 (an toàn) → Thành công!

## Lưu ý triển khai

- **Giới hạn nhánh:** Nên đặt giới hạn (VD: `X = 10`) để tránh AI đào vô tận.
- **Ứng dụng:** Bài toán lập lịch, tìm đường có ràng buộc, giải Sudoku/puzzle logic.
- **Nhóm:** Chương 1 — Cognitive Frameworks & Reasoning
