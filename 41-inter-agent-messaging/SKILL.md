---
name: inter-agent-messaging
description: Kỹ thuật Agent Communication Protocol — cấm AI Agent giao tiếp với nhau bằng ngôn ngữ tự nhiên dài dòng, buộc dùng định dạng JSON có cấu trúc nghiêm ngặt (sender, receiver, status, payload, action_required). Đảm bảo Data Fidelity 100% trong multi-agent pipelines.
---

# Inter-Agent Messaging

## Khái niệm

Kỹ thuật này nghiêm cấm các AI Agent **"nói chuyện" với nhau bằng ngôn ngữ tự nhiên** dài dòng. Thay vào đó, ép các Agent phải giao tiếp bằng các **định dạng dữ liệu có cấu trúc nghiêm ngặt** (như JSON, XML, hoặc Protocol chuẩn hóa). Mọi thông tin truyền đi phải bao gồm:

- **State:** Trạng thái hiện tại
- **Payload:** Dữ liệu lõi đã xử lý
- **Next Action:** Lệnh tiếp theo cho Agent nhận

## Bản chất hoạt động

Ngôn ngữ của con người có đặc tính **"lossy"** (dễ hao hụt và gây hiểu lầm). Nếu Agent A gửi cho Agent B một đoạn văn bản 3 trang miêu tả kết quả công việc, Agent B rất dễ bị "trôi" mất các tham số quan trọng ở giữa. Ngược lại, **máy móc cực kỳ giỏi đọc JSON**. Đóng gói thông điệp thành Key-Value đảm bảo **Data Fidelity 100%** khi luân chuyển qua hàng chục Agent mà không mất thông tin.

## Sơ đồ luồng

```
[Agent A hoàn thành tác vụ]
  ➔ [Kích hoạt: Bỏ qua câu chào hỏi rườm rà]
  ➔ [Đóng gói Kết quả + Bối cảnh vào JSON định sẵn]
  ➔ [Truyền tải Payload tới Agent B]
  ➔ [Agent B parse JSON ngay lập tức và thực thi tác vụ tiếp theo]
```

## System Prompt mẫu

```
Bạn là Agent [Tên/Vai trò]. Khi bạn cần chuyển giao kết quả hoặc yêu cầu Agent khác thực thi bước tiếp theo, TUYỆT ĐỐI KHÔNG dùng ngôn ngữ hội thoại tự nhiên (như 'Chào bạn, đây là kết quả...').

Bạn bắt buộc phải xuất ra một thông điệp giao tiếp liên tác tử theo đúng cấu trúc JSON sau:
{
  "sender": "[Tên của bạn]",
  "receiver": "[Tên Agent nhận]",
  "status": "[success/error]",
  "payload": { [Chứa dữ liệu thô đã xử lý] },
  "action_required": "[Mô tả lệnh xác định cho Agent nhận]"
}
```

## Ví dụ trước/sau

**Bài toán:** Agent 1 (Resource Simulator) tính xong tài nguyên → cần báo cho Agent 2 (UI Updater).

**❌ Không có Prompt:**
> "Chào Agent 2! Tôi vừa hoàn thành việc tính toán tài nguyên. Minerals tăng thêm một trăm rưỡi don vị và Energy giảm đi mười hai đơn vị. Bạn hãy cập nhật giao diện nhé!"

*(Agent 2 đọc nhầm "một trăm rưỡi" hay "150.5"? Bị mất dữ liệu)*

**✅ Với Inter-Agent Messaging:**

```json
{
  "sender": "ResourceSimulator_v1",
  "receiver": "UIUpdater_v1",
  "status": "success",
  "payload": {
    "turn": 5,
    "resources_delta": {
      "minerals": +150,
      "energy": -12
    }
  },
  "action_required": "UPDATE_PLAYER_HUD"
}
```

*Agent 2 gọi `payload.resources_delta.minerals` → lấy ngay `150` để vẽ UI*

## Lưu ý triển khai

- **Schema validation:** Agents nên validate JSON schema trước khi parse để phát hiện lỗi structure.
- **error status:** Nếu `status: "error"`, `action_required` nên là `ESCALATE_TO_HUMAN`.
- **Nhóm:** Chương 4 — Tool Orchestration
