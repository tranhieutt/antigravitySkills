---
name: pre-action-thinking
description: Kỹ thuật Scratchpad — buộc AI viết toàn bộ quá trình phân tích, lập kế hoạch, tự kiểm tra lỗi vào bên trong thẻ <thinking></thinking> trước khi đưa ra câu trả lời chính thức. Dùng khi yêu cầu phức tạp, nhiều ràng buộc, hoặc cần output cực kỳ chính xác và nhất quán.
---

# Pre-Action \<Thinking\>

## Khái niệm

Kỹ thuật này sử dụng các thẻ định dạng XML (thường là `<thinking>` và `</thinking>`) để tạo ra một **"không gian nháp"** (scratchpad) cho AI. AI bị ép phải viết toàn bộ quá trình phân tích, lập kế hoạch, và tự kiểm tra lỗi vào bên trong cặp thẻ này **trước khi** được phép xuất ra câu trả lời chính thức ở bên ngoài.

## Bản chất hoạt động

LLM sinh ra văn bản theo cơ chế dự đoán từ tiếp theo. Nếu bắt đầu viết câu trả lời ngay, AI dễ tự đưa mình vào thế bí (lỡ viết một câu mâu thuẫn với yêu cầu nhưng không thể quay lại xóa). Vùng `<thinking>` cho AI cơ hội sinh ra **"token nháp"** — đóng vai trò làm ngữ cảnh nền tảng vững chắc, giúp đoạn kết quả cuối cùng trở nên sắc bén, logic và tuân thủ chặt chẽ các điều kiện khó.

## Sơ đồ luồng

```
[Yêu cầu phức tạp]
  ➔ [AI mở thẻ <thinking>]
  ➔ [AI phân tích yêu cầu, liệt kê ràng buộc, lên dàn ý nháp]
  ➔ [AI đóng thẻ </thinking>]
  ➔ [AI viết kết quả cuối cùng dựa trên bản nháp]
```

## System Prompt mẫu

```
Trước khi đưa ra câu trả lời cuối cùng, bạn bắt buộc phải dành không gian để suy nghĩ, lập dàn ý và kiểm tra các ràng buộc. Toàn bộ quá trình tư duy này phải được đặt bên trong cặp thẻ <thinking> và </thinking>. Tuyệt đối không đưa ra bất kỳ kết luận nào trước khi thẻ đóng </thinking> xuất hiện. Sau khi đóng thẻ, hãy cung cấp câu trả lời hoàn chỉnh và được trau chuốt nhất của bạn.
```

## Ví dụ trước/sau

**Yêu cầu:** Viết bài Tết 2026, hai nhân vật Gàn + Ngựa, phong cách storytelling, tông màu Đỏ/Cam.

**❌ Không có Prompt:** AI vội vàng viết ngay, bỏ sót điều kiện màu sắc hoặc phong cách.

**✅ Với Pre-Action Thinking:**

```xml
<thinking>
Mục tiêu: Viết bài Tết 2026 cho thương hiệu.
Nhân vật: Linh vật "Gàn" và Ngựa (năm Bính Ngọ).
Phong cách: Storytelling, bài học cuộc sống.
Màu sắc: Bắt buộc tone Đỏ và Cam.
Ý tưởng: Ngựa = tốc độ/đi xa. Gàn = bền bỉ/gốc rễ/công nghệ lõi.
Bài học: Đi nhanh đến đâu cũng cần nền tảng vững chắc.
Hình ảnh: Gàn trao la bàn Cam dạ quang cho Ngựa dũng mãnh dưới hoàng hôn Đỏ rực.
</thinking>

[Kết quả cuối cùng: Bài viết đáp ứng đúng 100% ràng buộc]
```

## Lưu ý triển khai

- **Thẻ có thể tùy chỉnh:** `<analysis>`, `<draft>`, `<reasoning>` tùy theo context.
- **Ẩn thinking:** Một số hệ thống có thể parse và ẩn phần `<thinking>` khỏi người dùng cuối.
- **Phù hợp nhất:** Yêu cầu có nhiều ràng buộc đồng thời cần phải thỏa mãn.
- **Nhóm:** Chương 1 — Cognitive Frameworks & Reasoning
