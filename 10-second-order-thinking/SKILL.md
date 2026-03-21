---
name: second-order-thinking
description: Kỹ thuật Tư duy Bậc hai (Second-Order Thinking) từ Howard Marks — buộc AI dự phóng hệ quả bậc 2, bậc 3 ("và sau đó thì sao?") thay vì chỉ nhìn lợi ích bề nổi. Dùng để phân tích rủi ro chiến lược, đánh giá quyết định kinh doanh quan trọng, quản trị rủi ro dài hạn.
---

# Second-Order Thinking

## Khái niệm

Lấy cảm hứng từ triết lý đầu tư của tỷ phú **Howard Marks**, kỹ thuật này buộc AI không được dừng lại ở hệ quả trực tiếp hiển nhiên (Bậc 1). Thay vào đó, phải liên tục tự hỏi **"And then what?"** để dự phóng:

- **Hệ quả Bậc 2:** Tác dụng phụ của hệ quả Bậc 1
- **Hệ quả Bậc 3:** Tác động dài hạn đến toàn bộ hệ sinh thái

## Bản chất hoạt động

LLM mặc định thường bị "cận thị" (myopic). Khi đưa ra ý tưởng có vẻ hợp lý, bản năng AI là tâng bốc dựa trên lợi ích bề mặt. Ép AI suy nghĩ theo chuỗi nhân quả dài hạn kích hoạt khả năng "tưởng tượng hệ thống" — nhìn thấy hiệu ứng Domino mà một quyết định đơn lẻ gây ra cho bức tranh lớn.

## Sơ đồ luồng

```
[Quyết định / Ý tưởng]
  ➔ [Hệ quả Bậc 1: Hiển nhiên, tức thì]
  ➔ [Hệ quả Bậc 2: Hệ quả của hệ quả Bậc 1]
  ➔ [Hệ quả Bậc 3: Tác động dài hạn đến hệ sinh thái]
  ➔ [Đánh giá lại & Tinh chỉnh chiến lược ban đầu]
```

## System Prompt mẫu

```
Bạn là một nhà chiến lược quản trị rủi ro sử dụng Tư duy Bậc hai. Khi đánh giá bất kỳ quyết định hay chiến dịch nào, tuyệt đối không được chỉ nhìn vào lợi ích bề nổi. Bạn phải phân tích theo cấu trúc sau:
○ Quyết định: [Nêu lại quyết định]
○ Hệ quả Bậc 1: Kết quả trực tiếp, ngay lập tức là gì?
○ Hệ quả Bậc 2 (Sau 1-3 tháng): Hệ quả Bậc 1 sẽ gây ra những tác động dây chuyền nào đến vận hành, chi phí, hoặc hành vi người dùng?
○ Hệ quả Bậc 3 (Dài hạn): Tác động sâu rộng đến thương hiệu và hệ sinh thái?
Từ đó, hãy đưa ra lời khuyên để tối ưu hóa hoặc phòng ngừa rủi ro cho quyết định ban đầu.
```

## Ví dụ trước/sau

**Bài toán:** Chiến dịch tặng miễn phí tên miền .XYZ/.LOL khi mua .VN/.COM.

- **Bậc 1:** Doanh số .VN/.COM tăng vọt, khách hàng hứng thú.
- **Bậc 2:** Đội hỗ trợ quá tải xử lý yếu cầu quà tặng. Một số khách chỉ mua để lấy free domain, không có nhu cầu thực.
- **Bậc 3:** Nếu .XYZ/.LOL bị spam → reputation email của toàn hệ thống bị ảnh hưởng.
- **Lời khuyên:** Thêm điều kiện sử dụng (verify email thực), giới hạn số lượng, setup hệ thống tự động xử lý gift.

## Lưu ý triển khai

- **Ứng dụng tốt nhất:** Đánh giá chiến lược marketing, chính sách sản phẩm, quyết định đầu tư.
- **Số bậc:** Thường phân tích đến Bậc 3 là đủ; Bậc 4+ thường quá mơ hồ để có ích.
- **Nhóm:** Chương 1 — Cognitive Frameworks & Reasoning
