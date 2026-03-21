---
name: contextual-metacognition
description: Kỹ thuật Metacognition — buộc AI tự đánh giá mức độ hiểu biết, nhận diện điểm mù thông tin, và chấm điểm tự tin (0-100%) trước khi tạo nội dung. Nếu tự tin < 80%, AI phải đặt câu hỏi làm rõ thay vì hallucinate. Dùng khi yêu cầu mơ hồ hoặc cần độ chính xác cao.
---

# Contextual Metacognition

## Khái niệm

Trong tâm lý học, **Metacognition** nghĩa là "nhận thức về tư duy của chính mình". Khi áp dụng vào AI, kỹ thuật này buộc hệ thống LLM phải tự đánh giá lại mức độ hiểu biết, nhận diện các điểm mù thông tin, và kiểm tra tính hợp lý của các giả định **trước khi** tạo ra bất kỳ nội dung nào.

## Bản chất hoạt động

Điểm yếu cốt lõi của AI là "hiệu ứng Dunning-Kruger" — sự tự tin thái quá ngay cả khi thiếu kiến thức. Nhận được yêu cầu mơ hồ, bản năng AI là tự động điền vào chỗ trống bằng cách "đoán bừa" (hallucinate) để làm hài lòng người dùng. Bộ lọc "Tự nhận thức" buộc AI phân biệt giữa **sự thật đã biết** và **thứ đang tự suy diễn**.

## Sơ đồ luồng

```
[Yêu cầu đầu vào]
  ➔ [AI Tự Vấn: Đã hiểu gì? Thiếu dữ kiện gì? Đang dùng giả định nào?]
  ➔ [Chấm điểm Tự tin (Confidence Score)]
  ➔ [Nếu < 80%: Đặt câu hỏi làm rõ]
  ➔ [Nếu ≥ 80%: Thực thi đưa ra kết quả]
```

## System Prompt mẫu

```
Trước khi thực hiện yêu cầu, bạn bắt buộc phải thực hiện bước 'Tự nhận thức' (Metacognition) theo cấu trúc sau:
○ Sự thật đã biết: Liệt kê các thông tin chắc chắn bạn đã hiểu từ yêu cầu.
○ Điểm mù: Liệt kê những thông tin quan trọng còn thiếu.
○ Giả định: Liệt kê các giả định bạn đang tự đặt ra để giải quyết bài toán.
○ Điểm tự tin (0-100%). Nếu điểm tự tin dưới 80%, tuyệt đối không tạo ra kết quả cuối cùng. Thay vào đó, hãy phản hồi bằng cách đặt câu hỏi sắc bén để tôi cung cấp thêm dữ kiện.
```

## Ví dụ trước/sau

**Yêu cầu:** "Lên ý tưởng chuỗi bài đăng Tết 2026 với linh vật 'Gàn' tương tác với nhân vật Ngựa."

**✅ Với Contextual Metacognition:**

- **Sự thật đã biết:** Cần chuỗi bài content Tết 2026. Hai nhân vật: Gàn và Ngựa.
- **Điểm mù:** Tính cách nhân vật Ngựa? Mối quan hệ hai nhân vật? Phong cách storytelling hay thông báo khuyến mãi?
- **Giả định:** Màu sắc tông Tết truyền thống (Đỏ/Vàng), đối tượng đại chúng.
- **Điểm tự tin: 45%** → **Phải đặt câu hỏi làm rõ trước khi tạo nội dung!**

## Lưu ý triển khai

- **Điểm mạnh:** Loại bỏ hallucination do yêu cầu mơ hồ, buộc collaboration thay vì one-shot guess.
- **Ngưỡng tự tin:** Có thể điều chỉnh từ 80% lên 90% nếu domain đòi hỏi chính xác tuyệt đối.
- **Nhóm:** Chương 1 — Cognitive Frameworks & Reasoning
