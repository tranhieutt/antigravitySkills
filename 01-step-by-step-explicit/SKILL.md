---
name: step-by-step-explicit
description: Kỹ thuật Chain of Thought (CoT) — bắt buộc AI chia nhỏ vấn đề và "suy nghĩ thành tiếng" từng bước trước khi đưa ra đáp án. Dùng khi cần độ chính xác cao trong toán học, logic, phân tích dữ liệu, hoặc bất kỳ bài toán phức tạp nào cần suy luận nhiều bước.
---

# Step-by-Step Explicit

## Khái niệm

Dựa trên Chain of Thought (CoT), bắt buộc AI chia nhỏ vấn đề và "suy nghĩ thành tiếng" trước khi đưa ra đáp án. Giúp AI giảm tải nhận thức: thay vì tính toán một bước khổng lồ, AI tạo ra các chuỗi logic ngắn — token đầu ra của bước 1 trở thành ngữ cảnh đầu vào cho bước 2 — từ đó giảm thiểu lỗi suy luận.

## Sơ đồ luồng

```
[Input của người dùng]
  ➔ [AI phân tích: Bước 1 → Bước 2 → Bước 3]
  ➔ [Kết luận cuối cùng]
```

## System Prompt mẫu

```
Bạn là một chuyên gia phân tích. Đừng trả lời ngay. Hãy chia nhỏ bài toán thành các bước logic rõ ràng, trình bày chi tiết cách bạn giải quyết từng bước (think step-by-step), sau đó mới đưa ra kết luận cuối cùng.
```

## Ví dụ Before/After

**Câu hỏi:** Một chiến dịch chạy 15 ngày, mỗi ngày tốn 50k, tỷ lệ chuyển đổi là 2% trên tổng 1000 lượt click mỗi ngày. Hỏi có bao nhiêu chuyển đổi và chi phí một chuyển đổi là bao nhiêu?

**❌ Không có Prompt:** Dễ bỏ sót bước, trả lời vội gây sai sót.

**✅ Có Prompt (Step-by-Step Explicit):**
- Bước 1: Tính tổng chi phí. 15 ngày × 50k/ngày = **750k**
- Bước 2: Tính số click tổng. 15 ngày × 1000 click/ngày = **15,000 click**
- Bước 3: Tính số chuyển đổi. 2% của 15,000 = **300 chuyển đổi**
- Bước 4: Tính chi phí/chuyển đổi. 750k / 300 = **2.5k**
- Kết luận: Bạn có **300 chuyển đổi** với chi phí **2.5k/chuyển đổi**.

## Lưu ý triển khai

- **Ưu điểm:** Độ chính xác cao, dễ kiểm tra lỗi từng bước.
- **Hạn chế:** Tốn nhiều token đầu ra hơn, chi phí API cao hơn, thời gian chờ phản hồi lâu hơn.
- **Phù hợp:** Bài toán cần độ chính xác cao hơn là cần tốc độ nhanh.
- **Nhóm:** Chương 1 — Cognitive Frameworks & Reasoning
