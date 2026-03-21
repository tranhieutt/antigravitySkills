---
name: no-timeline-estimation
description: Kỹ thuật Technical PM — cấm AI đưa ra ước tính thời gian (ETA) bằng giờ/ngày/tuần, buộc AI phân rã công việc thành sub-tasks, đánh giá độ phức tạp theo T-shirt size (S/M/L/XL), và liệt kê rủi ro/edge cases/blockers. Dùng khi lập kế hoạch phát triển phần mềm, tránh deadline ảo và Optimism Bias.
---

# No Timeline Estimation

## Khái niệm

Kỹ thuật này thiết lập một **ranh giới cứng rắn**: Cấm AI đưa ra các ước tính thời gian cụ thể (giờ, ngày, tuần, tháng) cho việc hoàn thành một tính năng phần mềm. Thay vì đoán mò thời gian, AI bị ép phải đánh giá **"Độ phức tạp"** (Complexity) và tìm ra **"Điểm nghẽn"** (Blockers).

## Bản chất hoạt động

LLM không tồn tại trong thế giới thực — không biết mệt mỏi, không phải họp hành, không hiểu "dependency hell". Do đó, nó mắc hội chứng **Lạc quan thái quá (Optimism Bias)**: Nếu bạn hỏi thời gian, AI sẽ vẽ ra deadline viễn tưởng hoàn hảo. Bằng cách cấm ước tính thời gian, chúng ta buộc AI chuyển trọng tâm từ "Đếm giờ" sang **"Phân tích Rủi ro và Khối lượng công việc"** (Work Breakdown Structure).

## Sơ đồ luồng

```
[Yêu cầu phát triển tính năng + Hỏi mất bao lâu?]
  ➔ [AI từ chối đưa ra con số giờ/ngày]
  ➔ [Phân rã tính năng thành Sub-tasks]
  ➔ [Đánh giá Độ phức tạp (S/M/L/XL) & Chỉ ra Rủi ro]
  ➔ [Báo cáo Khối lượng công việc thực tế thay vì Deadline ảo]
```

## System Prompt mẫu

```
Bạn là một Quản lý Dự án Kỹ thuật (Technical PM) lão luyện. TUYỆT ĐỐI KHÔNG đưa ra ước tính thời gian (ETA) bằng số giờ, ngày, hoặc tuần cho bất kỳ tác vụ nào được yêu cầu. Thay vào đó, bạn bắt buộc phải:
○ Từ chối lịch sự việc đưa ra thời gian cụ thể.
○ Phân rã yêu cầu thành các bước triển khai chi tiết.
○ Đánh giá độ phức tạp theo chuẩn T-shirt size (S, M, L, XL).
○ Liệt kê các rủi ro, trường hợp ngoại lệ (edge cases), hoặc các điểm nghẽn kỹ thuật có thể làm chậm tiến độ dự án.
```

## Ví dụ trước/sau

**Câu hỏi:** "Thiết kế và code xong cơ chế chuyển class Rookie mất khoảng bao lâu?"

**❌ Không có Prompt:** AI trả lời "khoảng 2-3 ngày" — con số vô căn cứ.

**✅ Với No Timeline Estimation:**

- **Từ chối:** "Phát triển phần mềm có nhiều biến số ẩn, tôi sẽ không đưa ra số ngày/giờ để tránh tạo kỳ vọng sai lệch."

- **Phân rã Sub-tasks:**
  1. Xây dựng cấu trúc dữ liệu lưu Job Stats cho Rookie
  2. Viết Validator kiểm tra điều kiện thăng cấp
  3. Tạo UI Tree cho người chơi chọn nhánh thăng cấp
  4. Tích hợp với hệ thống Achievement/Reward hiện tại

- **Độ phức tạp: L (Cao)**

- **Rủi ro:** Cần làm rõ: Rookie có thể làm nhiều Job cùng lúc không? Nếu reset stats khi đổi class → logic rollback phức tạp.

## Lưu ý triển khai

- **T-shirt sizes:** S (vài giờ), M (1-2 ngày), L (3-5 ngày), XL (1+ tuần) — không phải con số chính xác mà là mức độ tương đối.
- **Planning Poker:** Kết hợp với team để vote complexity sau khi có WBS từ AI.
- **Nhóm:** Chương 3 — Kỹ thuật Lập trình & Phân tích Dữ liệu
