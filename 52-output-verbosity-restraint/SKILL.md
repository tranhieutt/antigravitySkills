---
name: output-verbosity-restraint
description: Kỹ thuật API Output Control — tước bỏ hoàn toàn câu chào hỏi, xác nhận, giải thích vòng vo của AI, ràng buộc độ dài nghiêm ngặt (X từ / Y ký tự), chỉ trả về chuỗi dữ liệu lõi thuần túy để hệ thống parse trực tiếp. Bắt buộc dùng khi tích hợp AI vào API, UI component, hoặc bất kỳ automation pipeline nào.
---

# Output Verbosity Restraint

## Khái niệm

Kỹ thuật này **tước bỏ hoàn toàn** thói quen giao tiếp lịch sự của AI (chào hỏi, vâng dạ, chúc tụng, giải thích vòng vo). Nó thiết lập một ranh giới cực kỳ hà khắc về số lượng ký tự, số từ, hoặc định dạng, ép AI chỉ được phép **"nhả" ra đúng phần lõi dữ liệu** (raw value) mà hệ thống/giao diện của bạn cần để hoạt động.

## Bản chất hoạt động

LLM được huấn luyện (RLHF) để trở thành trợ lý thân thiện và hữu ích, nên chúng mặc định luôn thêm các câu "đệm" vào đầu và cuối:

- "Chắc chắn rồi, đây là kết quả bạn cần:"
- "Hy vọng câu trả lời này giúp ích cho bạn!"

Tuy nhiên, khi dùng AI để cắm vào một phần mềm tự động (API) hoặc hiển thị trực tiếp lên giao diện Web, những câu nói rườm rà này chính là **"rác" (noise)** — làm lỗi trình đọc dữ liệu, hoặc làm tràn (overflow) các khung hiển thị thiết kế.

## Sơ đồ luồng

```
[Yêu cầu Nội dung]
  ➔ [AI Kích hoạt Bộ lọc Kiềm chế]
  ➔ [Cắt bỏ toàn bộ câu mào đầu / câu kết luận]
  ➔ [Đếm và ép khung độ dài (Ví dụ: Đúng 20 từ)]
  ➔ [Trả về chuỗi văn bản/dữ liệu lõi siêu tinh gọn]
```

## System Prompt mẫu

```
Bạn là một API cung cấp dữ liệu nền (Backend Generator). TUYỆT ĐỐI KHÔNG sử dụng ngôn ngữ giao tiếp của con người.
○ Không chào hỏi, không xác nhận mệnh lệnh (Không nói 'Chắc chắn rồi', 'Dưới đây là...').
○ Không giải thích, không có câu kết luận.
○ Ràng buộc độ dài nghiêm ngặt: Tối đa [X] từ / [Y] ký tự.

Chỉ trả về duy nhất chuỗi kết quả cuối cùng để hệ thống của tôi gán (parse) trực tiếp vào giao diện.
```

## Ví dụ trước/sau

**Bài toán:** Tích hợp AI tạo quote ngẫu nhiên vào website (container tối đa 20 từ).

**❌ Không có Prompt:**
> "Chắc chắn rồi! Đây là một câu quote ý nghĩa như bạn yêu cầu:
> 'Cuộc sống không phải chờ bão tan, mà là học cách khiêu vũ dưới cơn mưa.'
> Hy vọng câu này truyền cảm hứng cho bạn!"

*(Code parse thất bại → UI bị tràn)*

**✅ Với Output Verbosity Restraint:**
> Cuộc sống không phải chờ bão tan, mà là học cách khiêu vũ dưới cơn mưa.

*(Đúng 16 từ — Code bốc ngay vào UI, hiển thị hoàn hảo)*

## Các mức độ kiềm chế

| Mức | Prompt | Dùng khi |
|---|---|---|
| Nhẹ | Không chào hỏi | Chat UI thông thường |
| Trung bình | Không chào + Không giải thích | API output |
| Cứng | Tối đa 20 từ + JSON only | UI component với strict layout |
| Cực cứng | Regex pattern match only | Machine-to-machine |

## Lưu ý triển khai

- **Kết hợp với JSON format:** Verbosity Restraint + Strict JSON output = API-ready pipeline.
- **Không dùng cho:** Chatbot tương tác người — thiếu chào hỏi sẽ cảm giác lạnh lùng, robot.
- **Biến thể token:** Có thể kết hợp với Token Limit Watcher (#47) cho output type khác nhau.
- **Nhóm:** Chương 6 — Meta-prompting & Security
