---
name: event-driven-standby
description: Kỹ thuật Event-Driven Standby — ép AI vào trạng thái "ngủ đông" im lặng hoàn toàn cho đến khi một điều kiện/sự kiện cực kỳ cụ thể xuất hiện mới kích hoạt hành động. Dùng cho automation pipeline, webhook monitoring, giám sát log hệ thống real-time để tiết kiệm chi phí API.
---

# Event-Driven Standby

## Khái niệm

Bản chất của AI là luôn muốn "nói" và phản hồi ngay lập tức mỗi khi nhận được dữ liệu. Kỹ thuật này ép AI đi ngược lại bản năng đó: Nó bị đưa vào trạng thái **"ngủ đông"** (Standby) hoặc giám sát thụ động. AI sẽ liên tục tiếp nhận luồng thông tin nhưng bị cấm phản hồi, **cho đến khi** một điều kiện/sự kiện (Event) cực kỳ cụ thể xuất hiện để "đánh thức" nó.

## Bản chất hoạt động

Trong các hệ thống tự động hóa real-time (giám sát tin nhắn, theo dõi log hệ thống), 99% dữ liệu đổ về là "tiếng ồn" (noise). Nếu AI phản ứng với mọi dữ liệu, bạn sẽ nhanh chóng đốt sạch ngân sách API và tạo ra thao tác rác. **Bộ lọc kích hoạt** chỉ tiêu tốn compute vào đúng "khoảnh khắc có giá trị cao" nhất.

## Sơ đồ luồng

```
[Cài đặt AI vào Trạng thái Chờ]
  ➔ [Dòng dữ liệu / Tin nhắn đổ về liên tục]
  ➔ [AI Giám sát ngầm: Sự kiện X đã xảy ra chưa?]
  ➔ [Nếu Chưa: Bỏ qua, im lặng (trả về '.')]
  ➔ [Nếu Rồi: Thoát chế độ chờ, thực thi Hành động Y]
  ➔ [Quay lại Trạng thái Chờ]
```

## System Prompt mẫu

```
Bạn là một trạm giám sát tự động. Trạng thái mặc định của bạn là [STANDBY] - tuyệt đối im lặng và không đưa ra bất kỳ phản hồi nào.

Bạn sẽ nhận được các luồng dữ liệu liên tục. Bạn chỉ được phép thoát khỏi trạng thái [STANDBY] KHI VÀ CHỈ KHI dữ liệu đầu vào chứa [Điều kiện kích hoạt cụ thể].

Khi điều kiện này thỏa mãn, hãy thực hiện [Hành động X]. Nếu không, hãy chỉ trả lời bằng một dấu chấm '.' để xác nhận đã đọc.
```

## Ví dụ trước/sau

**Bối cảnh:** Giám sát webhook thanh toán, kích hoạt email tặng .XYZ/.LOL khi mua .VN/.COM.

| Dữ liệu đổ về | Điều kiện | AI phản hồi |
|---|---|---|
| `{action: "add_to_cart", domain: ".VN"}` | Chưa paid | `.` (ngủ tiếp) |
| `{action: "paid", domain: ".NET"}` | Domain sai | `.` (ngủ tiếp) |
| `{action: "paid", domain: ".COM"}` | **Đúng điều kiện!** | **KÍCH HOẠT** → soạn email tặng code .XYZ |

## Lưu ý triển khai

- **Điều kiện phải cực kỳ cụ thể:** Tránh kích hoạt nhầm (false positive).
- **Dấu `.`:** Cho phép hệ thống biết AI đã nhận và xử lý dữ liệu — không phải bị treo.
- **Ứng dụng:** Make/Zapier webhook, Slack bot giám sát từ khóa, alert system monitoring.
- **Nhóm:** Chương 1 — Cognitive Frameworks & Reasoning
