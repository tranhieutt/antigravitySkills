---
name: advanced-variable-extraction
description: Kỹ thuật PS+ Prompting — buộc AI trích xuất và gán dữ liệu vào biến số cụ thể TRƯỚC khi tính toán. Dùng khi xử lý văn bản lộn xộn chứa nhiều con số, bóc tách thông tin từ hợp đồng/chat dài, hay giải bài toán logic nhiều cạm bẫy.
---

# Advanced Variable Extraction

## Khái niệm

Dựa trên nền tảng "PS+ Prompting" (Plan-and-Solve Plus), kỹ thuật này buộc AI phải tìm kiếm, trích xuất và gán dữ liệu vào các biến số cụ thể **trước khi** thực hiện bất kỳ bước tính toán trung gian nào. Tách biệt hoàn toàn pha đọc hiểu dữ liệu và pha xử lý logic.

## Bản chất hoạt động

Khi đối mặt với văn bản chứa nhiều số liệu "rác" gây nhiễu, AI dễ bị hallucinate hoặc gán nhầm giá trị nếu vừa đọc vừa tính ngay. Bằng cách ép AI "lập bảng tóm tắt dữ kiện" trước, bộ nhớ làm việc (working memory) của AI chỉ cần tập trung vào các biến đã được làm sạch.

## Sơ đồ luồng

```
[Đầu vào: Văn bản thô lộn xộn]
  ➔ [AI Quét & Trích xuất: Biến 1, Biến 2, Biến n]
  ➔ [AI Xử lý/Tính toán CHỈ dựa trên các Biến đã trích xuất]
  ➔ [Kết quả đầu ra]
```

## System Prompt mẫu

```
Bạn là một hệ thống phân tích dữ liệu vô cùng chuẩn xác. Trước khi trả lời câu hỏi hoặc thực hiện bất kỳ lập luận/tính toán nào, bạn bắt buộc phải tuân thủ bước sau:
● XÁC ĐỊNH & TRÍCH XUẤT BIẾN SỐ: Đọc kỹ toàn bộ ngữ cảnh đầu vào, tìm kiếm các thông số quan trọng và gán chúng thành các biến số rõ ràng.
● Tuyệt đối không bắt đầu suy luận nếu chưa liệt kê rành mạch danh sách các biến số này.
```

## Ví dụ Before/After

**Dữ liệu đầu vào:** "Tháng trước cửa hàng nhập 150 thùng sữa, giá mỗi thùng 300k. Tuần đầu bán 40 thùng giá 350k. Tuần hai giảm giá bán 50 thùng giá 320k. Tiền thuê mặt bằng 5000k. Lợi nhuận ròng?"

**✅ Bước 1 — Trích xuất biến:**

```
So_thung_nhap = 150
Gia_nhap_1_thung = 300k
Ban_dot_1_SL = 40,  Ban_dot_1_Gia = 350k
Ban_dot_2_SL = 50,  Ban_dot_2_Gia = 320k
Chi_phi_codinh = 5000k
```

**✅ Bước 2 — Tính toán:**

- Doanh thu = (40×350k) + (50×320k) = 30,000k
- Chi phí vốn đã bán = 90×300k = 27,000k
- Lợi nhuận gộp = 3,000k
- Lợi nhuận ròng = 3,000k − 5,000k = **−2,000k (Lỗ)**

## Biến thể nâng cao

**JSON Enforcement:** Ép AI xuất biến ra JSON tĩnh để hệ thống tự động đẩy sang tool khác:

```json
{"Gia_nhap": 300, "SL_ban": 40, "Gia_ban": 350}
```

## Lưu ý triển khai

- **Ứng dụng tốt nhất:** Tóm tắt hợp đồng pháp lý, bóc tách thông tin CRM từ chat dài, giải bài toán logic đố chữ nhiều cạm bẫy.
- **Nhóm:** Chương 1 — Cognitive Frameworks & Reasoning
