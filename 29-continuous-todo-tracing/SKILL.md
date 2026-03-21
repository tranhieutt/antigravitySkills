---
name: continuous-todo-tracing
description: Kỹ thuật Todo Tracking — ép AI hoạt động như cỗ máy quản lý dự án: lập Todo List đầu dự án, mỗi cuối phản hồi bắt buộc in lại danh sách cập nhật tiến độ ([x] done / [ ] pending). Chống "context amnesia" trong các dự án đa bước, đảm bảo không bỏ sót bước nào.
---

# Continuous Todo Tracing

## Khái niệm

Kỹ thuật này ép AI phải hoạt động như một **cỗ máy quản lý dự án siêu nhỏ**. Nó bắt buộc AI phải:

1. Lập một danh sách công việc (To-Do List) ở ngay đầu dự án
2. **Ở cuối mỗi câu trả lời**, bắt buộc in lại danh sách với tiến độ cập nhật (đánh dấu `[x]` vào việc đã xong)

**Trước khi chuyển sang bước tiếp theo.**

## Bản chất hoạt động

LLM có "bộ nhớ ngắn hạn" (Context Window) hạn chế. Khi cuộc hội thoại kéo dài, câu lệnh hay dàn ý từ lúc đầu sẽ bị trôi tuột đi (**context window amnesia**). Bằng cách ép AI liên tục in ra To-Do List ở câu trả lời gần nhất, chúng ta đang liên tục "nhắc bài" cho nó. Cái danh sách đó đóng vai trò như một **mỏ neo (anchor)**, giúp AI luôn nhận thức được mình đang ở đâu trong bức tranh lớn.

## Sơ đồ luồng

```
[Nhiệm vụ đa bước]
  ➔ [AI Lập Todo List: [ ] 1.A, [ ] 2.B, [ ] 3.C]
  ➔ [AI Thực thi Bước A]
  ➔ [AI in cập nhật: [x] A, [ ] B, [ ] C]
  ➔ [Lệnh tiếp tục từ người dùng]
  ➔ [AI nhìn vào list → Thực thi Bước B]
  ➔ [Đến khi [x] tất cả]
```

## System Prompt mẫu

```
Bạn là một Trợ lý Thực thi cực kỳ kỷ luật. Đối với bất kỳ nhiệm vụ nào có nhiều bước, bạn BẮT BUỘC tuân thủ quy trình sau:
○ Đầu tiên, hãy lập một danh sách 'TODO LIST' đánh số thứ tự rõ ràng.
○ Chỉ thực hiện MỘT BƯỚC duy nhất trong mỗi lần phản hồi để đảm bảo chất lượng.
○ Ở CUỐI mỗi câu trả lời, bạn bắt buộc phải in ra trạng thái hiện tại của TODO LIST. Sử dụng dấu [x] cho các bước đã hoàn thành và [ ] cho các bước còn tồn đọng. Tuyệt đối không được quên in TODO LIST này ra cho đến khi toàn bộ dự án kết thúc.
```

## Ví dụ trước/sau

**Bài toán:** Viết tài liệu nghiên cứu 4 phần: Mở đầu, Lịch sử, Phân tích, Kết luận.

**❌ Không có Prompt:** Sau khi viết phần 1, bạn nói "Viết tiếp đi" → AI quên mất dàn ý 4 phần → Tự viết luôn Kết luận ngắn.

**✅ Với Continuous Todo Tracing:**

```
Bạn: "Viết tiếp đi."

AI viết Phần 1, cuối câu trả lời in ra:
---
TODO LIST:
[x] 1. Mở đầu (DONE)
[ ] 2. Lịch sử hình thành
[ ] 3. Phân tích chuyên sâu
[ ] 4. Kết luận
---

Bạn: "Tốt, đi tiếp."
AI nhìn list → Biết ngay cần viết Phần 2 → Viết xong → Update list...
```

## Lưu ý triển khai

- **Một bước/lần:** Chỉ thực thi MỘT step mỗi phản hồi để đảm bảo quality gate.
- **Never forget:** Không bao giờ được bỏ Todo List khỏi cuối câu trả lời cho đến khi xong.
- **Ứng dụng:** Dự án nhiều phần, code feature phức tạp, multi-turn research.
- **Nhóm:** Chương 3 — Kỹ thuật Lập trình & Phân tích Dữ liệu
