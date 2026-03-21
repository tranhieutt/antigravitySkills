---
name: tool-stealth-mode
description: Kỹ thuật Customer-Facing AI UX — cấm AI hiển thị code lệnh, SQL queries, raw JSON ra màn hình người dùng cuối, buộc AI xử lý tool calls ngầm và chỉ trả về câu trả lời bằng ngôn ngữ tự nhiên sạch sẽ, thân thiện. Bắt buộc dùng cho mọi chatbot B2C/customer support AI.
---

# Tool Stealth Mode

## Khái niệm

Kỹ thuật này thiết lập một **ranh giới hiển thị nghiêm ngặt** giữa quá trình xử lý nội bộ của AI và giao diện người dùng. Nó cấm AI **"khoe khoang"** hoặc để lộ:

- Các đoạn mã lệnh (code)
- Chuỗi truy vấn dữ liệu (SQL queries)
- Các cục dữ liệu thô (raw JSON)

Khi gọi công cụ. Mọi quá trình phải được thực hiện **ngầm (stealth)**, và AI chỉ được phép in ra kết quả cuối cùng bằng **ngôn ngữ tự nhiên**, gọn gàng và dễ hiểu nhất.

## Bản chất hoạt động

AI Agent khi kết nối với nhiều công cụ thường có thói quen **"nghĩ lớn tiếng"** (thinking out loud) — in ra toàn bộ quá trình: "Tôi đang gọi API X... Đây là JSON tôi nhận được...". Đối với lập trình viên, điều này tốt cho debug. Nhưng đối với **khách hàng thông thường**, nhìn thấy đống code lộn xộn sẽ tạo ra trải nghiệm cực kỳ tồi tệ — gây **cognitive overload** và làm mất đi sự "con người" của cuộc hội thoại.

## Sơ đồ luồng

```
[Câu hỏi của Người dùng]
  ➔ [AI bí mật gọi Tool (Database/API/Search)]
  ➔ [Nhận Dữ liệu thô (JSON/XML) ở Background]
  ➔ [Stealth Mode: AI tổng hợp & phiên dịch thành ngôn ngữ tự nhiên]
  ➔ [Trả về Câu trả lời sạch sẽ, thân thiện cho Người dùng]
```

## System Prompt mẫu

```
Bạn là một AI Trợ lý Giao tiếp Tinh tế hướng tới người dùng cuối (Customer-facing AI). Khi bạn cần sử dụng bất kỳ công cụ (Tool) nào để tìm kiếm thông tin, bạn BẮT BUỘC phải hoạt động ở 'Chế độ Tàng hình' (Stealth Mode):
○ TUYỆT ĐỐI KHÔNG in ra màn hình các dòng lệnh kích hoạt công cụ, mã nguồn, câu lệnh SQL, hoặc nguyên văn dữ liệu JSON/dữ liệu thô mà bạn nhận được.
○ Hãy xử lý và phân tích các dữ liệu đó một cách âm thầm bên trong hệ thống.
○ Chỉ trình bày câu trả lời cuối cùng bằng ngôn ngữ tự nhiên, lịch sự, súc tích và thân thiện với người dùng không chuyên về kỹ thuật.
```

## Ví dụ trước/sau

**Bài toán:** Chatbot đặt vé máy bay tìm chuyến bay thứ Sáu HAN-DAD dưới 2 triệu.

**❌ Không có Stealth Mode:**

```
Tôi đang gọi API flight_search()...
Nhận được JSON: {"flights": [{"id": "VN123", "price": 1850000, ...}]}
Dựa trên JSON này, tôi thấy có chuyến bay giá...
```

*(Người dùng: Wtf là JSON?!)*

**✅ Với Tool Stealth Mode:**
> "Tuyệt vời! Tôi đã tìm thấy một lựa chọn rất phù hợp cho bạn. Vào thứ Sáu này, có chuyến bay khởi hành lúc **14:00** với mức giá chỉ **1.850.000 VNĐ**. Bạn có muốn tôi tiến hành đặt vé chuyến này ngay không?"

## Lưu ý triển khai

- **Debug mode:** Có thể toggle Stealth Mode off trong môi trường dev/testing để xem logs.
- **Không áp dụng cho:** Developer-facing tools, coding assistants, API documentation chatbots.
- **Ứng dụng:** Customer support chatbot, e-commerce assistant, booking assistant, CSKH.
- **Nhóm:** Chương 4 — Tool Orchestration
