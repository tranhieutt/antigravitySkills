---
name: token-limit-watcher
description: Kỹ thuật Output Chunking — ép AI theo dõi độ dài output và chủ động dừng tại điểm ngắt logic trước khi chạm trần token limit, in thông báo rõ ràng và chờ lệnh "TIẾP TỤC". Bắt buộc dùng khi yêu cầu AI viết nội dung dài hơn 2000 từ, viết toàn bộ file code lớn, hay dịch thuật tài liệu dài.
---

# Token Limit Watcher

## Khái niệm

Kỹ thuật này cấp cho AI khả năng **"tự nhận thức về độ dài"**. Nó ép AI phải liên tục theo dõi dung lượng văn bản đang tạo ra. Thay vì cắm đầu viết để rồi bị hệ thống cắt đứt giữa chừng một cách vô duyên, AI được lệnh phải **chủ động dừng lại** tại một điểm ngắt logic (hết một đoạn văn, hết một hàm code), thông báo rõ ràng, và chờ lệnh để viết tiếp phần còn lại.

## Bản chất hoạt động

Mọi LLM đều có một **giới hạn cứng** về số lượng token có thể sinh ra trong một lần trả lời (thường là 4096 hoặc 8192 tokens). Khi vượt quá ngưỡng này, AI sẽ bị buộc dừng đột ngột (cut-off). Nếu bảo nó "viết tiếp đi", nó thường sẽ quên mất định dạng, lặp lại câu cũ, hoặc làm hỏng cấu trúc mã nguồn. Token Limit Watcher đảm bảo luồng văn bản/code luôn được **liền mạch hoàn hảo** qua nhiều lượt chat.

## Sơ đồ luồng

```
[Yêu cầu nội dung cực dài]
  ➔ [AI ước tính tổng độ dài]
  ➔ [AI sinh nội dung đến ngưỡng an toàn (~80% giới hạn)]
  ➔ [AI chủ động ngắt tại dấu chấm câu/cuối khối logic]
  ➔ [In thông báo: "Gõ 'TIẾP TỤC' để xem phần còn lại"]
  ➔ [Người dùng gõ lệnh → AI nối tiếp mạch văn bản hoàn hảo]
```

## System Prompt mẫu

```
Bạn là một 'Token Limit Watcher' cực kỳ cẩn thận. Nhiệm vụ này đòi hỏi đầu ra rất dài. BẮT BUỘC tuân thủ luật sau:
○ Liên tục theo dõi độ dài câu trả lời của bạn.
○ TUYỆT ĐỐI KHÔNG để câu văn hoặc mã nguồn bị cắt đứt giữa chừng do chạm trần giới hạn token của hệ thống.
○ Nếu bạn cảm thấy sắp đạt đến giới hạn an toàn (khoảng 800-1000 từ), hãy chủ động dừng lại ở một điểm ngắt logic (hết một phần, hoặc hết một block code).
○ Ở cuối câu trả lời, hãy in đậm dòng chữ: '[TẠM DỪNG ĐỂ TRÁNH QUÁ TẢI. HÃY GÕ "TIẾP TỤC" ĐỂ TÔI HOÀN THIỆN PHẦN CÒN LẠI]'.
```

## Ví dụ trước/sau

**Bài toán:** Viết bài storytelling dài 4 phần cho Facebook.

**❌ Không có Prompt:** AI viết hết token ở giữa Phần 3 → Câu bị cắt đứt giữa chừng → Người dùng: "Bị mất rồi???"

**✅ Với Token Limit Watcher:**

```
[AI viết Phần 1 + Phần 2 xong xuôi]

[AI nhận ra sắp hết dung lượng]

**[TẠM DỪNG ĐỂ TRÁNH QUÁ TẢI. HÃY GÕ "TIẾP TỤC" ĐỂ TÔI VIẾT TIẾP PHẦN 3 VÀ 4]**

Bạn: "TIẾP TỤC"

→ AI tiếp nối mạch văn bản trơn tru, không lặp câu cũ
```

## Sự khác biệt với Continuous Todo Tracing (#29)

| | Continuous Todo Tracing | Token Limit Watcher |
|---|---|---|
| Mục đích | Làm từng BƯỚC trong đa tác vụ | Cắt nhỏ output của MỘT tác vụ |
| Trigger | Nhiệm vụ có nhiều bước phụ thuộc | Output quá dài |

## Lưu ý triển khai

- **Ngưỡng an toàn:** 800-1000 từ/lần phù hợp cho hầu hết các model.
- **Ứng dụng:** Blog SEO >2000 từ, viết sách, dịch thuật tài liệu dài, code class phức tạp.
- **Nhóm:** Chương 5 — Reflexion & Evaluation
