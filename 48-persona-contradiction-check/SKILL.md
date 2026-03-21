---
name: persona-contradiction-check
description: Kỹ thuật Voice Consistency — ép AI tự rà soát bản nháp để phát hiện và loại bỏ các đoạn "thoát vai" (break character), từ ngữ sáo rỗng kiểu AI hoặc quá trang trọng không khớp với persona đã định. Dùng khi viết content cần giữ giọng nhất quán: blog cá nhân, social media, storytelling.
---

# Persona Contradiction Check

## Khái niệm

Kỹ thuật này thiết lập một bước **"tự phản tỉnh"** (self-reflection) chuyên biệt về mặt cảm xúc và văn phong. Nó buộc AI phải rà soát lại toàn bộ bản nháp vừa viết, dò tìm từng câu chữ xem có bất kỳ đoạn nào:

- **"Thoát vai"** (break character)
- Mâu thuẫn với thiết lập nhân vật ban đầu
- Sử dụng từ vựng không nhất quán với phong cách đã định trước

## Bản chất hoạt động

LLM có một lực hút vô hình gọi là **"Regression to the Mean"** (Trở về mức trung bình). Dù bạn ép nó đóng vai gã cướp biển hay ông chú hài hước, khi văn bản càng dài, LLM càng dễ **"quên mất" vai diễn** và trượt dần về giọng văn mặc định: lịch sự, khách quan, sáo rỗng và an toàn. Persona Contradiction Check ép AI đánh thức lại thiết lập nhân vật ở giây phút cuối, gọt bỏ "từ vựng AI" trước khi xuất bản.

## Sơ đồ luồng

```
[Yêu cầu Nội dung + Thiết lập Persona gốc]
  ➔ [AI sinh bản nháp]
  ➔ [Bộ lọc Mâu thuẫn: Quét toàn bộ văn bản đối chiếu với Persona gốc]
  ➔ [Phát hiện lỗi 'Thoát vai' (từ ngữ quá học thuật, quá robot)]
  ➔ [Viết lại đoạn lỗi để đồng bộ 100% cảm xúc và giọng điệu]
  ➔ [Bản cuối cùng hoàn hảo]
```

## System Prompt mẫu

```
Trước khi đưa ra kết quả cuối cùng, bạn BẮT BUỘC phải thực hiện 'Persona Contradiction Check' (Kiểm tra Mâu thuẫn Nhân cách).
○ Soi chiếu lại bản nháp của bạn với thiết lập [Tên/Đặc điểm Persona gốc của bạn].
○ Tìm kiếm và loại bỏ ngay lập tức những câu văn mang đậm 'mùi AI', sáo rỗng, quá trang trọng hoặc có dấu hiệu 'thoát vai'.
○ Đảm bảo 100% bài viết từ chữ đầu tiên đến chữ cuối cùng đều nhất quán với mạch cảm xúc và phong cách kể chuyện đã được yêu cầu.

Chỉ in ra bản đã được kiểm tra và chỉnh sửa.
```

## Ví dụ trước/sau

**Bài toán:** Viết bài cho Facebook cá nhân phong cách storytelling tâm tình, gần gũi, không giáo điều.

**❌ Phần kết luận trong bản nháp (Thoát vai):**
> "Tóm lại, trong thế giới hiện đại đầy biến động, chúng ta cần học cách thích nghi và phát triển bản thân mỗi ngày."

*(Quá học thuật, giống sách giáo khoa — không phải giọng tâm tình của blog cá nhân)*

**✅ Sau Persona Contradiction Check:**
> "Mưa ngớt rồi. Ly cà phê cũng vừa cạn. Tự nhiên thấy nhẹ bẫng. Có lẽ, những ngày chông chênh nhất lại là lúc mình học được cách tự che ô cho chính mình. Thôi, về dọn dẹp lại mấy mớ suy nghĩ ngổn ngang thôi..."

## Dấu hiệu "Thoát vai" cần loại bỏ

| Từ/Cụm "Mùi AI" | Thay thế theo Persona |
|---|---|
| "Tóm lại", "Kết luận" | Câu chốt tự nhiên theo cảm xúc |
| "Thế giới hiện đại" | Tình huống cụ thể, gần gũi |
| "Điều quan trọng là" | Câu kể chuyện, không thuyết giáo |
| "Hy vọng câu trả lời..." | Câu kết phù hợp persona |

## Lưu ý triển khai

- **Kết hợp:** Dùng sau Actor (#42) — Actor tạo nháp, Persona Check gọt lại giọng văn.
- **Ứng dụng:** Blog cá nhân có thương hiệu riêng, social media persona, ghostwriting.
- **Nhóm:** Chương 5 — Reflexion & Evaluation
