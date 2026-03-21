---
name: sequential-dependency
description: Kỹ thuật Pipeline Orchestration — thiết lập "chuỗi cung ứng dữ liệu" nghiêm ngặt giữa các tools, ép AI thiết lập trạng thái CHỜ và chỉ kích hoạt Tool B khi Tool A đã trả về kết quả thực tế. Cấm hallucinate tham số. Dùng khi xây dựng content pipeline, image generation workflow, hay bất kỳ chuỗi bước phụ thuộc nhau.
---

# Sequential Dependency

## Khái niệm

Kỹ thuật này thiết lập một **"chuỗi cung ứng dữ liệu"** nghiêm ngặt giữa các công cụ (Tools). Nó dạy AI hiểu rằng: **Tool B bắt buộc phải dùng Output của Tool A làm Input**. Do đó, AI tuyệt đối không được kích hoạt Tool B nếu Tool A chưa chạy xong và trả về kết quả cuối cùng.

## Bản chất hoạt động

Các hệ thống Agent rất dễ bị **"Ảo giác tham số"** (Parameter Hallucination) khi cố gắng chạy quá nhanh. Nếu Tool B bị gọi mà chưa nhận được dữ liệu thực tế từ Tool A, AI sẽ tự động **"đoán bừa"** (hallucinate) một dữ liệu giả để điền vào — dẫn đến toàn bộ quy trình phía sau bị hỏng hóc nặng nề. Kỹ thuật này ép AI xây dựng một biểu đồ luồng (DAG) trong não trước khi hành động.

## Sơ đồ luồng

```
[Nhiệm vụ Đa bước]
  ➔ [AI Lập bản đồ Phụ thuộc: Tool B cần Input từ Tool A]
  ➔ [Kích hoạt Lệnh Chờ (Wait State)]
  ➔ [Thực thi Tool A]
  ➔ [Nhận Output A thực tế]
  ➔ [Trích xuất dữ liệu từ Output A → truyền vào Tool B]
  ➔ [Thực thi Tool B]
```

## System Prompt mẫu

```
Bạn là một AI Orchestrator (Nhạc trưởng Điều phối). Khi thực thi chuỗi tác vụ dưới đây, bạn BẮT BUỘC tuân thủ nguyên tắc Phụ thuộc Tuần tự (Sequential Dependency):
○ Xác định rõ công cụ nào cần kết quả của công cụ trước đó để hoạt động.
○ TUYỆT ĐỐI KHÔNG tự bịa ra (hallucinate) các tham số đầu vào cho một công cụ.
○ Bạn phải thiết lập trạng thái 'CHỜ' (Wait). Chỉ khi Công cụ [A] trả về kết quả thành công, bạn mới được phép trích xuất kết quả đó và đưa vào làm tham số chạy Công cụ [B]. Nếu [A] thất bại, dừng ngay lập tức.
```

## Ví dụ trước/sau

**Bài toán:** Content Pipeline: Generate_Copy → (dùng image_prompt từ copy) → Generate_Image → Post.

**❌ Không có Prompt:** AI gọi `Generate_Image(prompt="[ASSUMED_PROMPT]")` ngay lập tức → Hình ảnh không liên quan đến nội dung bài viết.

**✅ Với Sequential Dependency:**

1. AI gọi `Generate_Copy()` → **Trạng thái: CHỜ**
2. Tool trả về: `{copy: "Bài viết...", image_prompt: "Gàn màu đỏ cam cầm khiên Cloud Server"}`
3. AI trích xuất `image_prompt` → Truyền vào `Generate_Image(prompt="Gàn màu đỏ cam...")`
4. Nếu Generate_Copy thất bại → **Dừng ngay, không tiếp tục**

**Kết quả:** Hình ảnh khớp chính xác với nội dung bài viết.

## Lưu ý triển khai

- **Stop on Failure:** Nếu bước trước thất bại → phải dừng ngay, không tiếp tục với dữ liệu giả.
- **Kết hợp với Parallel:** Sequential cho các tác vụ phụ thuộc, Parallel cho các tác vụ độc lập trong cùng một pipeline.
- **Nhóm:** Chương 4 — Tool Orchestration
