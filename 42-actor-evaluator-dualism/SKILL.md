---
name: actor-evaluator-dualism
description: Kỹ thuật Self-Critique — ép một LLM phân liệt thành Actor (viết nháp) và Evaluator (mổ xẻ lỗi không thương tiếc), sau đó Actor viết lại dựa trên phản hồi của Evaluator. Chỉ hiển thị phần đánh giá và bản hoàn chỉnh. Dùng khi cần output chất lượng cao không qua nhiều vòng chat.
---

# Actor-Evaluator Dualism

## Khái niệm

Kỹ thuật này ép một LLM duy nhất phải **phân liệt thành hai nhân cách** làm việc nối tiếp nhau:

- **Actor:** Viết ra bản nháp
- **Evaluator:** Đóng vai vị giám khảo khó tính, tàn nhẫn mổ xẻ bản nháp để tìm lỗ hổng
- **Actor (lần 2):** Đọc lời chê bai và viết ra bản hoàn chỉnh (Final Output)

## Bản chất hoạt động

LLM có điểm yếu chết người: Chúng sinh văn bản theo **chiều tiến (forward-generation)**. Khi đang viết ở dòng số 5, không thể quay lại sửa dòng số 1 — dẫn đến các bản nháp đầu tiên thường mắc lỗi logic hoặc quên ràng buộc. Tuy nhiên, AI lại **xuất sắc trong việc đọc và nhận xét**. Vòng lặp **"Làm → Chê → Sửa"** ngay trong một prompt ép AI dùng tư duy bậc cao để tự gỡ lỗi chính luồng suy nghĩ của nó.

## Sơ đồ luồng

```
[Yêu cầu Nhiệm vụ]
  ➔ [ACTOR: Sinh bản nháp (Draft) - ẩn]
  ➔ [EVALUATOR: Soi chiếu với tiêu chí gốc, liệt kê điểm trừ/lỗi sai]
  ➔ [ACTOR: Hấp thụ phản hồi, viết lại bản Final]
  ➔ [Chỉ in ra kết quả Final cho người dùng]
```

## System Prompt mẫu

```
Trong phiên làm việc này, bạn sẽ thực hiện một quy trình Nhị nguyên (Actor-Evaluator).

Bước 1 (Actor): Viết một bản nháp nội bộ cho yêu cầu bên dưới.

Bước 2 (Evaluator): Đóng vai một chuyên gia kiểm duyệt khắt khe. Hãy tự đánh giá bản nháp trên dựa trên 3 tiêu chí [A, B, C]. Chỉ ra ít nhất 2 điểm cần cải thiện.

Bước 3 (Final Output): Đóng vai Actor một lần nữa. Dựa trên những góp ý khắt khe ở Bước 2, hãy viết lại một phiên bản hoàn hảo nhất.

Yêu cầu trình bày: Chỉ hiển thị [Phần Đánh Giá] và [Bản Hoàn Chỉnh]. Bỏ qua bản nháp.
```

## Ví dụ trước/sau

**Bài toán:** Viết kịch bản bài đăng Fanpage Tết 2026 với linh vật Gàn + Ngựa, thúc đẩy sale Cloud Server.

**❌ Không có Prompt:** AI viết một lần → Sáo ngữ, thiếu màu sắc thương hiệu Đỏ/Cam, CTA yếu.

**✅ Với Actor-Evaluator Dualism:**

**[EVALUATOR Đánh giá - Hiển thị]:**
>
> - Lỗi 1: Chưa nổi bật màu sắc Đỏ/Cam — thương hiệu không được nhận diện.
> - Lỗi 2: Tương tác Gàn-Ngựa quá lỏng lẻo, chưa thể hiện tính "gàn dở đáng yêu" của mascot.
> - CTA "Đăng ký ngay" quá chung chung, thiếu urgency.

**[Bản Hoàn Chỉnh - Hiển thị]:**
*(Bài viết đã sửa hoàn toàn đáp ứng cả 3 góp ý trên)*

## Lưu ý triển khai

- **Chỉ hiển thị 2 bước cuối:** Người dùng không cần thấy bản nháp thô.
- **Số tiêu chí:** 3 là tối ưu. Quá nhiều → Evaluator bị pha loãng.
- **Kết hợp với Excellence Rubric (#43):** Dùng Rubric làm bộ tiêu chí của Evaluator.
- **Nhóm:** Chương 5 — Reflexion & Evaluation
