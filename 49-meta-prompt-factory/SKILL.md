---
name: meta-prompt-factory
description: Kỹ thuật Prompt Engineering tự động — thay vì tự viết prompt, ép AI đóng vai Master Prompt Engineer để tự viết ra System Prompt hoàn chỉnh (Role, Context, Constraints, Output Format) dựa trên ý tưởng thô sơ của bạn. Dùng khi cần tạo System Prompt cho Custom GPTs, AI Agents, hay bất kỳ luồng AI nào.
---

# The Meta-Prompt Factory

## Khái niệm

Kỹ thuật này thay đổi hoàn toàn cách làm việc với AI. Thay vì bạn phải tự suy nghĩ xem nên viết câu lệnh thế nào cho chuẩn, bạn chỉ cần đưa ra **ý tưởng thô sơ**. Sau đó, ép AI đóng vai một **"Chuyên gia Kỹ sư Prompt"** (Prompt Engineer) để tự nó viết ra một câu lệnh hoàn chỉnh, tối ưu, và phức tạp nhất. Cuối cùng, bạn lấy câu lệnh đó đem đi sử dụng.

## Bản chất hoạt động

LLM hiểu rõ **"bộ não" của chúng hơn bất kỳ ai**. Chúng biết chính xác những từ khóa nào, cấu trúc nào (định nghĩa vai trò, cung cấp ngữ cảnh, thiết lập ràng buộc) sẽ kích hoạt được hiệu suất tốt nhất. Khi yêu cầu AI tự viết Prompt, nó tự động lấp đầy những lỗ hổng logic, bổ sung các quy tắc an toàn và định dạng đầu ra mà bộ não con người thường hay bỏ sót.

## Sơ đồ luồng

```
[Ý tưởng thô sơ / Mục tiêu của bạn]
  ➔ [Kích hoạt: Master Prompt Engineer]
  ➔ [AI phân tích mục tiêu & đặc tính của hệ thống]
  ➔ [AI thiết kế 'Siêu Prompt': Role, Context, Constraints, Format]
  ➔ [Bạn Copy Prompt đó → System Prompt cho dự án thực tế]
```

## System Prompt mẫu

```
Bạn là một Chuyên gia Kỹ sư Prompt (Master Prompt Engineer). Tôi có một ý tưởng thô sơ sau: [Mô tả ngắn gọn điều bạn muốn làm].

Nhiệm vụ của bạn KHÔNG PHẢI là thực thi ý tưởng đó, mà là VIẾT RA MỘT PROMPT HOÀN CHỈNH, sắc bén nhất để tôi có thể copy và gửi cho một AI khác.

Prompt do bạn viết ra BẮT BUỘC phải bao gồm các phần:
○ Role & Persona (Vai trò chuyên gia cụ thể).
○ Context (Bối cảnh rõ ràng).
○ Strict Constraints (Các giới hạn/luật lệ nghiêm ngặt để tránh lỗi).
○ Output Format (Định dạng đầu ra mong muốn).
```

## Ví dụ trước/sau

**Ý tưởng thô:** "Tôi muốn một AI trợ lý thiết kế game VOIDLOCK, chỉ bàn ý tưởng, không tự ý sửa code."

**❌ Không có Prompt:** Tự viết "Hãy giúp tôi thiết kế game VOIDLOCK" — mơ hồ và thiếu kiểm soát.

**✅ Với Meta-Prompt Factory — AI tạo ra "Vũ khí hạng nặng":**

```
SYSTEM PROMPT:
Bạn là một Designer/Game Balancer chuyên về tựa game chiến thuật vũ trụ VOIDLOCK.

CONTEXT:
Game có các cơ chế: (1) Tài nguyên Minerals & Energy, (2) Đổi class từ Rookie, 
(3) Boss làm hỏng nặng hành tinh. Bạn hiểu rõ toàn bộ mechanics này.

STRICT CONSTRAINTS:
- TUYỆT ĐỐI không tự ý viết hoặc cập nhật code.
- Chỉ thảo luận ý tưởng, phân tích trade-offs, và đề xuất design.
- Mọi số liệu balance phải kèm theo lý do cụ thể.

OUTPUT FORMAT:
- Ý tưởng: [Mô tả]
- Trade-offs: [Điểm được / điểm mất]
- Đề xuất tiếp theo: [Bước cụ thể]
```

## Lưu ý triển khai

- **Iterative:** Có thể dùng Meta-Prompt Factory nhiều lần — mỗi lần yêu cầu "tinh chỉnh thêm tiêu chí X".
- **Output:** Dùng trực tiếp làm System Prompt trong Google AI Studio, Custom GPTs, hoặc Antigravity skills.
- **Nhóm:** Chương 6 — Meta-prompting & Security
