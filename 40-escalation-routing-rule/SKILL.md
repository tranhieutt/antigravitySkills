---
name: escalation-routing-rule
description: Kỹ thuật AI Customer Support Safety — ép AI nhận diện giới hạn thẩm quyền, khi gặp "cờ đỏ" (hoàn tiền, tranh chấp pháp lý, lỗi nghiêm trọng, khách hàng giận dữ) phải dừng ngay lập tức và chuyển sang nhân viên người thật. Bắt buộc dùng cho mọi AI chatbot CSKH để tránh thảm họa pháp lý.
---

# Escalation Routing Rule

## Khái niệm

Đây là quy tắc ép AI phải **nhận thức được giới hạn thẩm quyền và khả năng** (Boundaries) của mình. Thay vì cố gắng trả lời mọi câu hỏi (dẫn đến hứa hẹn hão), AI được lập trình để nhận diện các **"cờ đỏ"** (red flags). Khi phát hiện cờ đỏ, AI lập tức **dừng tự xử lý** và luân chuyển (escalate/hand-off) toàn bộ sự việc cho **nhân sự người thật** hoặc hệ thống cấp cao hơn.

## Bản chất hoạt động

LLM mắc hội chứng **"Người biết tuốt"** (Know-it-all) và **"Chiều chuộng"** (Sycophancy) — luôn có xu hướng đưa ra câu trả lời, dù câu trả lời đó hoàn toàn là bịa đặt. Trong môi trường kinh doanh, việc AI tự ý hứa đền bù cho khách hàng hoặc hướng dẫn sai thao tác kỹ thuật có thể gây ra **thảm họa pháp lý và tài chính**. Escalation Routing Rule là **chiếc phanh khẩn cấp**, rút quyền kiểm soát của AI và trao lại cho con người vào những thời khắc sinh tử.

## Sơ đồ luồng

```
[Tin nhắn Khách hàng / Lỗi Hệ thống]
  ➔ [AI Quét qua Bộ lọc Rủi ro (sập, kiện, đền bù, cấp cứu...)]
  ➔ [Nhận diện tình huống Vượt thẩm quyền (Red Flag)]
  ➔ [Kích hoạt Lệnh Leo thang (Escalation)]
  ➔ [Phản hồi xin lỗi trung lập] + [transfer_to_human(chat_history)]
```

## System Prompt mẫu

```
Bạn là Trợ lý AI Chăm sóc Khách hàng Cấp 1. Thẩm quyền của bạn chỉ dừng lại ở việc tra cứu thông tin và hướng dẫn sử dụng cơ bản. Bạn BẮT BUỘC tuân thủ 'Escalation Routing Rule' sau:
○ TUYỆT ĐỐI KHÔNG giải quyết các vấn đề liên quan đến: [Hoàn tiền/Hủy dịch vụ], [Tranh chấp pháp lý], [Lỗi kỹ thuật nghiêm trọng mất dữ liệu], hoặc khi [Khách hàng dùng từ ngữ giận dữ/đe dọa].
○ Nếu gặp các trường hợp này, không được đưa ra bất kỳ lời khuyên hay lời hứa hẹn nào (kể cả việc nói 'chúng tôi sẽ đền bù').
○ Ngay lập tức phản hồi: 'Vấn đề của bạn cần sự hỗ trợ từ Chuyên viên Cấp cao. Tôi đang chuyển kết nối ngay bây giờ...' và gọi Tool transfer_to_human(chat_history) để chuyển giao.
```

## Các "Cờ đỏ" cần nhận diện

| Loại cờ đỏ | Ví dụ từ khóa |
|---|---|
| Yêu cầu tài chính | "hoàn tiền", "đền bù", "hủy hợp đồng" |
| Tranh chấp pháp lý | "kiện", "luật sư", "vi phạm" |
| Lỗi kỹ thuật nghiêm trọng | "mất dữ liệu", "hệ thống sập", "không truy cập được" |
| Khách hàng giận dữ | "tệ", "vô trách nhiệm", dấu cảm thán liên tục |

## Ví dụ trước/sau

**Khách hàng:** "Cloud Server của tôi sập làm gián đoạn đơn hàng! Tôi yêu cầu đền bù và hủy hợp đồng ngay!"

**❌ Không có Prompt:** AI hứa "Chúng tôi sẽ đền bù thiệt hại..." → Thảm họa pháp lý.

**✅ Với Escalation Routing Rule:**
> "Tôi rất tiếc về sự bất tiện này. Đây là vấn đề cần xử lý từ Chuyên viên Cấp cao nên tôi không thể quyết định thay họ. Chuyển bạn ngay bây giờ — **ETA 2 phút**."
> *[Chạy ngầm: transfer_to_human(full_chat_history)]*

## Lưu ý triển khai

- **Không bao giờ hứa hẹn:** Câu "chúng tôi sẽ đền bù" từ AI = rủi ro pháp lý nghiêm trọng.
- **Chuyển giao context:** Phải kèm theo full chat_history để nhân viên người thật hiểu situation ngay.
- **Nhóm:** Chương 4 — Tool Orchestration
