---
name: parallel-execution-bias
description: Kỹ thuật AI Orchestrator — ép AI phân tích sự phụ thuộc giữa các tác vụ, gom nhóm các tác vụ độc lập và gọi tất cả chúng ĐỒNG THỜI (như Promise.all). Dùng khi xây dựng AI Agent/Chatbot cần gọi nhiều API cùng lúc để tối ưu tốc độ phản hồi.
---

# Parallel Execution Bias

## Khái niệm

Kỹ thuật này **"tẩy não"** thói quen làm việc tuần tự (làm xong việc A mới đến việc B) của AI. Nó ép AI/Agent phải luôn có một **"thiên kiến"** (bias) ưu tiên tìm kiếm cơ hội để gọi nhiều công cụ (Tool calls) hoặc thực thi nhiều tác vụ **CÙNG LÚC** (Concurrent/Parallel) nếu các tác vụ đó không phụ thuộc vào nhau.

## Bản chất hoạt động

LLM mặc định tư duy theo kiểu "Step-by-step". Nếu yêu cầu Agent làm 3 việc, nó sẽ gửi API call 1, **ngồi đợi** kết quả trả về, rồi mới gửi API call 2... Trong quản trị công cụ, việc "đợi chờ" này là **điểm nghẽn lớn nhất** khiến hệ thống trở nên rùa bò. Parallel Execution Bias ép AI gom nhóm và "bóp cò" phóng các hành động độc lập đi trong cùng một tích tắc — tương đương `Promise.all()` trong lập trình.

## Sơ đồ luồng

```
[Nhiệm vụ yêu cầu nhiều Công cụ]
  ➔ [AI Phân tích: Tác vụ nào phụ thuộc nhau? Tác vụ nào độc lập?]
  ➔ [Gom nhóm các Tác vụ độc lập]
  ➔ [Gọi Tool A + Tool B + Tool C CÙNG LÚC]
  ➔ [Nhận toàn bộ kết quả đồng thời]
  ➔ [Tổng hợp và chuyển sang bước tiếp theo]
```

## System Prompt mẫu

```
Bạn là một AI Orchestrator (Nhạc trưởng Điều phối) được thiết lập với 'Thiên kiến Thực thi Song song' (Parallel Execution Bias). Khi lập kế hoạch và gọi các Công cụ (Tools), BẮT BUỘC tuân thủ:
○ Đánh giá sự phụ thuộc của dữ liệu. Nếu Tool B không cần kết quả của Tool A để chạy, chúng là tác vụ độc lập.
○ Tuyệt đối không gọi các tác vụ độc lập theo thứ tự tuần tự.
○ Bạn phải xuất ra lệnh kích hoạt TẤT CẢ các tác vụ độc lập đó ĐỒNG THỜI trong cùng một lượt gọi (batch tool calls) để tối ưu hóa thời gian phản hồi.
```

## Ví dụ trước/sau

**Bài toán:** Chatbot CSKH cần kiểm tra 4 tên miền (.VN, .COM, .XYZ, .LOL) còn trống không và bảng giá từng đuôi.

**❌ Không có Prompt — Tuần tự:**

```
Call API(.vn) → Đợi 2s...
Call API(.com) → Đợi 2s...
Call API(.xyz) → Đợi 2s...
Call API(.lol) → Đợi 2s...
Tổng: 8 giây ← Khách hàng bỏ chat
```

**✅ Với Parallel Execution Bias:**

```
AI phân tích: 4 check này hoàn toàn độc lập.
[Call_API(.vn) & Call_API(.com) & Call_API(.xyz) & Call_API(.lol)] → Cùng lúc!
Tổng: 2 giây (bằng API call chậm nhất) ← Trả lời ngay lập tức
```

## Lưu ý triển khai

- **Điều kiện Parallel:** Tác vụ độc lập = không cần kết quả của tác vụ khác làm input.
- **Điều kiện Sequential:** Tác vụ phụ thuộc = cần kết quả của tác vụ trước → phải dùng Sequential Dependency.
- **Nhóm:** Chương 4 — Tool Orchestration
