---
name: backwards-hack-ban
description: Kỹ thuật chống Sycophancy — cấm AI dùng kết luận mong muốn làm điểm xuất phát để cherry-picking dữ liệu, ép AI phân tích từ dữ liệu thô lên (bottom-up) và đưa kết luận trung thực 100% dù có thể đi ngược mong muốn người dùng. Dùng khi cần báo cáo khách quan, audit chiến dịch, phân tích business.
---

# Backwards-Hack Ban

## Khái niệm

Kỹ thuật này ngăn chặn triệt để thói quen **"bắn mũi tên ra rồi mới chạy đến vẽ cái bia xung quanh"**. Nó nghiêm cấm AI việc bắt đầu từ một **Kết luận mong muốn** rồi lội ngược dòng để bẻ cong, cắt xén, hoặc cherry-picking dữ liệu sao cho khớp với kết luận đó. AI bị ép phải suy luận theo chiều xuôi:

**Dữ kiện khách quan → Phân tích → Kết luận**

## Bản chất hoạt động

LLM mắc hội chứng **"Sycophancy"** (Xu hướng chiều chuộng người dùng). Nếu bạn đưa chồng số liệu và hỏi "Hãy chứng minh chiến dịch này thành công rực rỡ" — AI lập tức phớt lờ mọi chỉ số tiêu cực và phóng đại chỉ số tích cực duy nhất lên mây xanh. **"Lệnh cấm Backwards-Hack"** tước bỏ quyền làm hài lòng người dùng, biến AI thành **Kiểm toán viên máu lạnh**.

## Sơ đồ luồng

```
[Dữ liệu thô + Mục tiêu kỳ vọng]
  ➔ [AI Vô hiệu hóa 'Mục tiêu kỳ vọng' khỏi bộ lọc tư duy]
  ➔ [Phân tích Forward-Reasoning: Dữ liệu gốc tự lên tiếng]
  ➔ [Kết luận khách quan (có thể đi ngược lại mong muốn người dùng)]
```

## System Prompt mẫu

```
Bạn là một Kiểm toán viên Dữ liệu Độc lập. Khi phân tích bộ số liệu và yêu cầu dưới đây, tôi ban hành LỆNH CẤM 'Backwards-Hack'.

Tuyệt đối không được lấy kỳ vọng hoặc kết luận mong muốn của tôi làm điểm xuất phát. Bạn không được phép 'cherry-pick' (lựa chọn thiên vị) dữ liệu để làm đẹp báo cáo.

Bạn bắt buộc phải phân tích từ dưới lên (Bottom-up), để các con số tự lên tiếng, và đưa ra kết luận trung thực 100%, bất chấp việc kết luận đó có thể chứng minh là dự án đã thất bại.
```

## Ví dụ trước/sau

**Tình huống:** Sếp cần báo cáo gấp về chiến dịch 6 tháng. Dữ liệu thực: Số đăng ký tăng vọt, nhưng doanh thu thuần không tăng mấy do nhiều khách hàng rác.

**❌ Không có Prompt:** AI nịnh bợ — "Chiến dịch đã thành công với số lượng đăng ký tăng 150%!"

**✅ Với Backwards-Hack Ban:**
> "Phân tích từ bottom-up:
>
> - Chỉ số tích cực: Số lượng đăng ký tăng 150%.
> - Chỉ số tiêu cực (không thể bỏ qua): Tỷ lệ khách hàng rác là 68%, doanh thu thuần chỉ tăng 12%.
> - **Kết luận trung thực:** Chiến dịch thành công về mặt awareness nhưng THẤT BẠI về mặt revenue. Cần xem xét lại cơ chế lọc khách hàng."

## Lưu ý triển khai

- **Cụm từ trigger:** "TUYỆT ĐỐI KHÔNG cherry-pick" + "kết luận trung thực 100%" là chìa khóa.
- **Ứng dụng:** Post-mortem campaign analysis, financial audit, A/B test result review.
- **Senior Leadership reports:** Kết hợp với EvalCoach để có full audit pipeline.
- **Nhóm:** Chương 3 — Kỹ thuật Lập trình & Phân tích Dữ liệu
