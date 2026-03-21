---
name: first-principles-deconstruction
description: Kỹ thuật First-Principles Thinking (theo Elon Musk) — cấm AI suy luận bằng loại suy theo số đông, buộc AI bóc tách vấn đề đến sự thật nền tảng không thể bác bỏ, rồi xây dựng giải pháp hoàn toàn mới từ đó. Dùng khi cần giải pháp đột phá, thoát khỏi lối mòn ngành.
---

# First-Principles Deconstruction

## Khái niệm

Bắt nguồn từ triết học và vật lý học (được Elon Musk áp dụng thành công), kỹ thuật này **cấm AI suy luận dựa trên sự loại suy** (Analogy — tức sao chép cách người khác đang làm). Thay vào đó, ép AI phải bóc tách vấn đề từng lớp cho đến khi chạm tới những **"sự thật nền tảng"** (fundamental truths) không thể chối cãi, rồi từ đó xây dựng giải pháp hoàn toàn mới từ con số không.

## Bản chất hoạt động

LLM bản chất là cỗ máy học theo mẫu (pattern-matching). Nếu bạn hỏi nó cách làm một việc, nó sẽ lục lọi kho dữ liệu xem số đông đang làm thế nào rồi xào nấu lại → câu trả lời sáo rỗng, rập khuôn. **First-Principles vô hiệu hóa "chế độ bắt chước"**, buộc AI dùng tư duy logic thuần túy.

## Sơ đồ luồng

```
[Bài toán / Lối mòn hiện tại]
  ➔ [Deconstruct: Đập bỏ các giả định & thói quen]
  ➔ [Identify: Rút trích các Sự thật cơ bản (Vật lý, Toán học, Logic cốt lõi)]
  ➔ [Reconstruct: Lắp ráp giải pháp mới từ các sự thật đó]
  ➔ [Kết quả đột phá]
```

## System Prompt mẫu

```
Bạn là một nhà tư duy sắc bén theo Nguyên lý thứ nhất (First-Principles Thinking). Khi giải quyết bài toán này, tuyệt đối không được dựa trên các phép loại suy, thói quen, hay các giải pháp đang có sẵn trên thị trường. Bạn phải trình bày theo 3 bước:
○ Liệt kê và đập bỏ những giả định/lối mòn mà mọi người thường mặc định là đúng.
○ Xác định những 'sự thật cơ bản nhất' (fundamental truths) của vấn đề mà không thể bị bẻ gãy.
○ Xây dựng một giải pháp hoàn toàn mới dựa duy nhất trên những sự thật cơ bản vừa tìm được.
```

## Ví dụ trước/sau

**Bài toán:** Thiết kế hệ thống Stamina và Tài nguyên cho game khoa học viễn tưởng.

**❌ Không có Prompt:** Copy lại cơ chế thanh Stamina truyền thống của các game khác.

**✅ Với First-Principles:**

- **Bước 1 — Đập giả định:** Xóa "Stamina phải hồi theo thời gian thực" và "Mọi tài nguyên đều giống nhau".
- **Bước 2 — Sự thật cơ bản:** Di chuyển tàu cần nhiên liệu đốt. Khai thác hành tinh cần sức bền sinh học. Minerals (rắn) ≠ Energy (điện/nhiên liệu) — chúng khác biệt về vật lý, không thể tự biến đổi lẫn nhau.
- **Bước 3 — Giải pháp đột phá:** Hai hệ thống hoàn toàn tách biệt: Bio-Stamina (hồi phục bằng thực phẩm/nghỉ ngơi) và Ship-Energy (từ nhiên liệu/solar). Conversion phải qua công trình đặc biệt với chi phí cao.

## Lưu ý triển khai

- **Ứng dụng tốt nhất:** Thiết kế sản phẩm mới, chiến lược startup thoát khỏi competitive landscape, game design, brainstorming đột phá.
- **Hạn chế:** Không phù hợp khi cần câu trả lời nhanh hoặc bài toán đã có best practice rõ ràng.
- **Nhóm:** Chương 1 — Cognitive Frameworks & Reasoning
