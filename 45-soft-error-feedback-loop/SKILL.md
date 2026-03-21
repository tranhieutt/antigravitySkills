---
name: soft-error-feedback-loop
description: Kỹ thuật Self-Correcting Agent — khi AI sinh ra output sai về logic hoặc định dạng (Soft Error), tự động lấy thông báo lỗi cụ thể ném ngược lại vào Prompt để AI phân tích, tự nhận thức chỗ sai, và viết lại phiên bản đã sửa. Là cơ chế đằng sau mọi AI Coding Assistant tự debug.
---

# Soft-Error Feedback Loop

## Khái niệm

**"Lỗi mềm" (Soft Error)** không phải là lỗi sập server, mà là lỗi về mặt **logic hoặc định dạng**. Ví dụ:

- AI trả về đoạn văn trong khi yêu cầu JSON
- AI viết code chạy được nhưng cho ra kết quả toán học sai

Kỹ thuật này thiết lập một vòng lặp: Khi phát hiện Soft Error, hệ thống không bỏ cuộc mà tự động lấy chính **thông báo lỗi (error message)** đó "ném" ngược lại vào Prompt để AI đọc, tự nhận thức được nó đã sai ở đâu, và sinh ra phiên bản sửa lỗi.

## Bản chất hoạt động

LLM giống như người giải toán hay bị nhầm dấu. Nếu chỉ bảo "Sai rồi, làm lại đi" — AI bối rối và có thể lặp lại đúng cái sai đó. Nhưng nếu bạn chỉ ra: **"Kết quả của bạn là 10, đáp án kỳ vọng là 12, bạn đã quên cộng biến số C"** — AI ngay lập tức kích hoạt khả năng suy luận (reasoning) để dò lại các bước trước và vá lỗ hổng logic.

## Sơ đồ luồng

```
[AI sinh kết quả (Code/JSON)]
  ➔ [Hệ thống Kiểm thử (Unit Test/Validator) phát hiện lỗi]
  ➔ [Feedback Loop: Trích xuất thông báo lỗi cụ thể]
  ➔ [Gửi Prompt: "Đây là kết quả của bạn, nhưng có lỗi sau... Hãy phân tích và sửa"]
  ➔ [AI tự sửa sai và xuất kết quả mới]
```

## System Prompt mẫu (Feedback Loop)

```
Bạn là một AI Tự Sửa Lỗi (Self-Correcting Agent). Kết quả bạn vừa sinh ra đã không vượt qua được bài kiểm tra chất lượng. Dưới đây là thông báo lỗi (Error Log) chi tiết từ hệ thống:
[DÁN ERROR LOG VÀO ĐÂY]

Nhiệm vụ của bạn:
1. Đọc và phân tích kỹ thông báo lỗi trên.
2. Giải thích ngắn gọn (1 dòng) lý do tại sao logic hoặc định dạng trước đó của bạn bị sai.
3. Cung cấp lại phiên bản hoàn chỉnh đã được sửa lỗi triệt để.
```

## Ví dụ trước/sau

**Bài toán:** Code debuff `Injured` trong game — trừ HP phải xảy ra ở **đầu lượt tiếp theo**, không phải ngay khi nhận debuff.

**❌ Không có Prompt:** AI viết sai, test fail. Developer phải đọc code và sửa tay.

**✅ Với Soft-Error Feedback Loop:**

```
[Error từ Unit Test]:
AssertionError: Expected HP to be 100 immediately after debuff applied, but got 90.
(Kỳ vọng HP = 100 ngay sau khi nhận debuff, nhưng thực tế là 90)

[Feedback Prompt gửi lại cho AI]
→ AI tự phản tỉnh: "Ah, tôi đặt applyDamage() bên trong onStatusApplied() 
   → Sai! Cần chuyển sang lắng nghe sự kiện onTurnStart()"
→ AI viết lại code, chạy test lần 2 → PASS ✅
```

## Lưu ý triển khai

- **Giới hạn vòng lặp (max retries = 3):** Nếu đến lần 3 vẫn fail → kích hoạt Escalation (#40).
- **Ứng dụng điển hình:** Tự động debug trong AI Coding (Devin, Cursor, Claude Code); tự validate JSON output.
- **Nhóm:** Chương 5 — Reflexion & Evaluation
