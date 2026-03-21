---
name: pre-mortem-simulation
description: Kỹ thuật Rủi ro Tiền thất bại — ép AI đóng vai "Kẻ báo tử từ tương lai", giả định dự án đã THẤT BẠI THẢM HẠI, truy tìm 3 nguyên nhân tồi tệ nhất và đề xuất Giải pháp Phòng ngừa tương ứng. Phá vỡ Optimism Bias, tìm ra blind spots trước khi launch.
---

# Pre-Mortem Simulation

## Khái niệm

Kỹ thuật này ép AI phải đóng vai một **"Kẻ báo tử"** hoặc **"Nhà du hành thời gian"** đến từ một tương lai vô cùng tồi tệ. Bạn cung cấp cho AI một kế hoạch (trông có vẻ rất hoàn hảo), và yêu cầu nó bắt buộc phải giả định rằng dự án này đã **thất bại thảm hại**. Nhiệm vụ của AI là lội ngược dòng để tìm ra lý do tại sao nó "chết" — từ đó vạch trần lỗ hổng và blind spots mà con người thường bỏ qua do Optimism Bias.

## Bản chất hoạt động

Cả con người lẫn LLM đều mắc phải **"Thiên kiến Lạc quan"** khi bắt đầu dự án mới — chỉ nhìn thấy con đường Happy Path. LLM thì luôn có xu hướng đồng tình và khen ngợi kế hoạch của bạn. Bằng cách kích hoạt Pre-Mortem, bạn **phá vỡ hoàn toàn lớp màng nịnh bợ** — cấp phép cho AI được quyền tàn nhẫn và vạch lá tìm sâu.

## Sơ đồ luồng

```
[Kế hoạch Tưởng chừng Hoàn hảo]
  ➔ [Kích hoạt: Nhà Phân tích Rủi ro từ Tương lai]
  ➔ [Giả định Kế hoạch đã Thất bại 100%]
  ➔ [Truy tìm Nguyên nhân: Điểm mù, Nút thắt cổ chai]
  ➔ [Mitigation Plan để chắp vá kế hoạch gốc]
```

## System Prompt mẫu

```
Bạn là một Chuyên gia Quản trị Rủi ro (Risk Management Expert). Chúng ta sẽ thực hiện một cuộc 'Khám nghiệm Tiền thất bại' (Pre-Mortem Simulation) cho kế hoạch dưới đây.

Hãy tưởng tượng bây giờ là 6 tháng sau. Dự án này vừa được triển khai và nó đã THẤT BẠI THẢM HẠI (gây lỗ nặng, sập hệ thống hoặc khủng hoảng truyền thông).

Tuyệt đối không khen ngợi kế hoạch của tôi. Bạn bắt buộc phải:
○ Chỉ ra 3 nguyên nhân tồi tệ nhất, thực tế nhất dẫn đến thảm họa này.
○ Phân tích các lỗ hổng trong logic vận hành, UX/UI, hoặc rủi ro từ các yếu tố bên ngoài.
○ Với mỗi nguyên nhân, hãy đề xuất một 'Giải pháp Phòng ngừa' (Mitigation) để tôi bổ sung vào kế hoạch ngay từ bây giờ.
```

## Ví dụ trước/sau

**Bài toán:** Chiến dịch Tết 2026 với linh vật Gàn + Ngựa, tone màu Đỏ/Cam, thúc đẩy sale Cloud Server.

**❌ Không có Prompt:** AI: "Ý tưởng rất sáng tạo và bắt trend! Tính kết hợp giữa mascot và năm Ngọ rất thú vị..."

**✅ Với Pre-Mortem Simulation:**

**Nguyên nhân 1 — Visual Fatigue:**
Lạm dụng màu đỏ/cam rực rỡ xuyên suốt làm người dùng mệt mỏi thị giác. Link và mã giảm giá bị chìm trong background.
→ **Mitigation:** Bổ sung mảng trắng/trung tính để nổi bật CTA.

**Nguyên nhân 2 — Lệch pha Cảm xúc:**
Chuyển từ câu chuyện tếu táo sang lời kêu gọi mua dịch vụ kỹ thuật quá gượng ép.
→ **Mitigation:** Tách biệt phần giải trí (ảnh 1-3) và phần sale (ảnh 4).

**Nguyên nhân 3 — Server Overload:**
Ngày mùng 1 Tết, traffic tăng đột biến làm sập Landing Page trong 2 giờ vàng.
→ **Mitigation:** Scale up server trước đêm Giao thừa.

## Lưu ý triển khai

- **Số nguyên nhân:** 3 là chuẩn. Có thể tăng lên 5 cho dự án rủi ro cao.
- **Thời điểm dùng:** Trước khi launch bất kỳ chiến dịch, tính năng, hoặc sản phẩm nào.
- **Kết hợp với Threat Intel (#16):** Pre-Mortem cho business risk, Threat Intel cho security risk.
- **Nhóm:** Chương 5 — Reflexion & Evaluation
