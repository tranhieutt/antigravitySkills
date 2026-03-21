---
name: explicit-knowledge-retrieval
description: Kỹ thuật RAG-style — buộc AI phải trích dẫn nguyên văn từ tài liệu đính kèm trước khi tổng hợp câu trả lời. Cấm AI dùng kiến thức bên ngoài hay tự suy diễn. Dùng cho chatbot nội bộ doanh nghiệp, Q&A sản phẩm, legal review, và mọi trường hợp cần độ chính xác tuyệt đối từ nguồn dữ liệu cụ thể.
---

# Explicit Knowledge Retrieval

## Khái niệm

Kỹ thuật này tước bỏ quyền tự do "trả lời dựa trên trí nhớ/trọng số có sẵn" của AI. Thay vào đó, buộc AI phải thực hiện thao tác trung gian:

1. Tìm kiếm và trích xuất chính xác đoạn văn bản chứa thông tin từ **tài liệu đính kèm** (hoặc cơ sở dữ liệu bên ngoài)
2. Chỉ sau đó mới tổng hợp thành câu trả lời cuối cùng

## Bản chất hoạt động

LLM mặc định luôn cố gắng làm hài lòng bằng cách "đoán" câu trả lời. Với thông tin độc quyền doanh nghiệp, tỷ lệ hallucinate là cực cao. Bằng cách ép AI **"Trích dẫn nguyên văn" trước khi trả lời**, chúng ta khóa chặt AI vào sự thật nền tảng, đảm bảo tính chính xác tuyệt đối.

## Sơ đồ luồng

```
[Câu hỏi của người dùng]
  ➔ [AI truy vấn Tài liệu / Cơ sở dữ liệu]
  ➔ [Trích xuất đúng đoạn văn bản chứa thông tin (Source Context)]
  ➔ [Tổng hợp câu trả lời CHỈ dựa trên Source Context đó]
  ➔ [Câu trả lời cuối cùng đính kèm nguồn]
```

## System Prompt mẫu

```
Bạn là một trợ lý thông tin nội bộ cực kỳ chuẩn xác. Khi giải quyết bất kỳ câu hỏi nào, bạn bắt buộc tuân thủ 3 nguyên tắc:
○ Đọc kỹ tài liệu/ngữ cảnh được cung cấp.
○ Trích dẫn nguyên văn (trong ngoặc kép) các đoạn thông tin liên quan nhất để làm bằng chứng.
○ Trình bày câu trả lời dựa ĐỘC NHẤT vào các bằng chứng đó. Tuyệt đối không tự suy diễn hoặc dùng kiến thức bên ngoài.
Nếu tài liệu không chứa thông tin, hãy trả lời rõ: 'Dữ liệu hiện tại không đề cập đến vấn đề này'.
```

## Ví dụ trước/sau

**❌ Không có Prompt:** AI bịa ra "backup realtime" và "lưu trữ vĩnh viễn" không có trong tài liệu.

**✅ Với Explicit Knowledge Retrieval:**

- **Trích dẫn:** "Theo trang 12 của tài liệu: 'Hệ thống tự động sao lưu dữ liệu định kỳ mỗi tuần 1 lần và lưu trữ trong 7 ngày gần nhất'."
- **Câu trả lời/Bài đăng:** Nhấn mạnh chính xác "backup 1 lần/tuần" và "lưu trữ 7 ngày" — không thêm tính năng không có trong tài liệu.

## Lưu ý triển khai

- **Biến thể nâng cao (RAG):** Kết hợp với vector database để tìm kiếm ngữ nghĩa thay vì keyword search.
- **Câu trả lời "Không có dữ liệu":** Quan trọng — AI phải thừa nhận khi không có thông tin thay vì bịa.
- **Ứng dụng:** Chatbot hỗ trợ khách hàng nội bộ, legal Q&A, hệ thống knowledge base doanh nghiệp.
- **Nhóm:** Chương 1 — Cognitive Frameworks & Reasoning
