---
name: orchestrator-worker-mesh
description: Kỹ thuật Multi-Agent Architecture — chia hệ thống thành Orchestrator (Nhạc trưởng phân rã công việc) và Workers (các AI chuyên biệt thực thi từng mảng cụ thể), chạy parallel và tổng hợp kết quả. Dùng khi xây dựng pipeline sản xuất nội dung, content factory, hay bất kỳ dự án phức tạp cần nhiều chuyên môn khác nhau.
---

# Orchestrator-Worker Mesh

## Khái niệm

Thay vì nhồi nhét mọi yêu cầu vào một "Siêu AI" duy nhất, kỹ thuật này chia hệ thống thành **hai vai trò biệt lập**:

- **Orchestrator (Nhạc trưởng):** Quản lý dự án — không trực tiếp làm việc chuyên môn, chỉ phân tích yêu cầu, chia nhỏ công việc (Breakdown) và giao task.

- **Workers (Nhân viên):** Các AI quy mô nhỏ hơn, được "cài cắm" các nhân cách chuyên biệt (như Creative Ad Legend hay Threat Intel) để thực thi **duy nhất một mảng việc xuất sắc nhất**.

## Bản chất hoạt động

Bất kỳ LLM nào khi phải gánh quá nhiều ngữ cảnh (viết code, cộng số liệu, sáng tạo nội dung, kiểm duyệt rủi ro) cùng một lúc đều bị **"pha loãng" sự tập trung**, dẫn đến kết quả hời hợt. Mạng lưới Mesh giúp mỗi Worker Agent nhận được một Prompt **cực kỳ hẹp và sắc bén** — kết quả tổng hợp lại thành một kiệt tác hoàn hảo.

## Sơ đồ luồng

```
[Dự án Lớn / Phức tạp]
  ➔ [Orchestrator: Phân rã thành Sub-tasks]
  ➔ [Giao: Task A → Worker 1, Task B → Worker 2, Task C → Worker 3]
  ➔ [Workers thực thi độc lập song song]
  ➔ [Orchestrator: Thu thập, đối chiếu và tổng hợp output]
  ➔ [Kết quả toàn diện]
```

## System Prompt mẫu (Orchestrator)

```
Bạn là một Orchestrator (Nhạc trưởng Điều phối Dự án) cấp cao. Khi nhận một yêu cầu phức tạp, BẮT BUỘC tuân thủ quy trình:
- Tuyệt đối không tự tay thực thi công việc chuyên môn.
- Phân rã yêu cầu thành 3-4 đầu việc chuyên biệt.
- Đóng gói chỉ thị (Prompt) chi tiết cho từng 'Worker' tương ứng để thực thi.
- Sau khi Workers hoàn thành, tổng hợp các mảnh ghép lại thành một Deliverable thống nhất.
```

## Ví dụ trước/sau

**Bài toán:** Chiến dịch khuyến mãi cần Facebook post + ý tưởng hình ảnh + kiểm duyệt pháp lý.

**❌ Không có Prompt:** Nhồi vào 1 AI → Bài viết vừa sáng tạo vừa an toàn pháp lý → Thỏa hiệp tất cả, xuất sắc không cái nào.

**✅ Với Orchestrator-Worker Mesh:**

| Worker | Nhân cách | Nhiệm vụ | Output |
|---|---|---|---|
| Worker 1 | Creative Ad Legend | Viết Facebook post vần điệu | Bài copy |
| Worker 2 | Brand Designer | Thiết kế prompt tạo ảnh Đỏ/Cam | Image prompt |
| Worker 3 | Compliance Navigator | Rà soát lỗi pháp lý trong bài copy | Bài đã sửa |

**Orchestrator tổng hợp:** Bài viết kiểm duyệt của Worker 3 + Ý tưởng ảnh của Worker 2 = Bộ tài liệu chiến dịch hoàn hảo.

## Lưu ý triển khai

- **Workers là độc lập:** Mỗi Worker không biết Workers khác đang làm gì → tránh cross-contamination.
- **Ứng dụng:** Content factory, market research pipeline, software development team simulation.
- **Nhóm:** Chương 4 — Tool Orchestration
