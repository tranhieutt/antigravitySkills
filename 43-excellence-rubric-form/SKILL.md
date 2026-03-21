---
name: excellence-rubric-form
description: Kỹ thuật Quantified QA — định nghĩa Rubric với thang điểm 1-5 cho từng tiêu chí cụ thể, ép AI chấm điểm khách quan (không khen sáo), giải thích lý do trừ điểm, và đề xuất sửa đổi cụ thể để đạt 5/5. Dùng để review copywriting, landing page, báo cáo, hoặc bất kỳ output nào cần QA chặt chẽ.
---

# Excellence Rubric Form

## Khái niệm

Kỹ thuật này yêu cầu bạn định nghĩa rõ ràng một **bảng tiêu chí (Rubric)** với các thang điểm cụ thể (1 đến 5) cho từng khía cạnh của sản phẩm đầu ra. AI buộc phải chấm điểm chéo văn bản nháp dựa trên đúng các tiêu chí này, giải thích lý do cho từng mức điểm, và sau đó mới tiến hành sửa chữa những phần bị điểm liệt.

## Bản chất hoạt động

LLM vốn dĩ rất **"dễ dãi"** — nếu hỏi "Bài này hay không?", nó gần như luôn trả lời: "Bài viết rất hay, hấp dẫn và mạch lạc!" Sự khen ngợi sáo rỗng này không giúp ích gì. Bằng cách thiết lập một **Rubric**, bạn biến nhiệm vụ định tính (đánh giá cảm xúc) thành **nhiệm vụ định lượng** (chấm điểm theo barem). Khi phải ép mình vào logic chấm điểm, AI sẽ soi ra những lỗi sai chí mạng mà bình thường nó sẽ lướt qua.

## Sơ đồ luồng

```
[Nội dung cần đánh giá]
  ➔ [Kích hoạt Rubric: 3-5 tiêu chí kèm mô tả thang điểm]
  ➔ [AI Chấm điểm: Tiêu chí A (3/5), Tiêu chí B (4/5)]
  ➔ [Đưa ra lý lẽ bảo vệ điểm số]
  ➔ [Action Plan để nâng điểm tất cả lên 5/5]
```

## System Prompt mẫu

```
Bạn là một Giám khảo Đánh giá Chất lượng cấp cao. Hãy đánh giá bản nháp dưới đây bằng 'Bảng Tiêu chí Xuất sắc' (Excellence Rubric). Bắt buộc chấm điểm từ 1 đến 5 cho 3 tiêu chí sau:
○ [Tiêu chí 1 - VD: Tính chuyển đổi (Conversion)]: 1=Mờ nhạt, 5=Tạo sự khao khát và khan hiếm mạnh mẽ.
○ [Tiêu chí 2 - VD: Giọng văn Thương hiệu]: 1=Robot, 5=Chuyên nghiệp, đáng tin cậy.
○ [Tiêu chí 3 - VD: Scannability (Độ dễ đọc lướt)]: 1=Đoạn văn dài dòng, 5=Sử dụng bullet, in đậm, rõ cấu trúc.

Chỉ in ra điểm số, lý do trừ điểm, và ĐỀ XUẤT sửa đổi chính xác để đạt điểm tuyệt đối.
```

## Ví dụ trước/sau

**Bài toán:** Review copy Landing Page hợp tác Mắt Bão × VPBank.

**❌ Không có Prompt:** "Bản nháp rất hay, ngôn ngữ chuyên nghiệp và truyền tải ưu đãi rõ ràng!"

**✅ Với Excellence Rubric Form:**

| Tiêu chí | Điểm | Lý do trừ | Đề xuất cụ thể |
|---|---|---|---|
| Tính chuyển đổi | 3/5 | Thiếu yếu tố FOMO | Thêm đồng hồ đếm ngược + "Chỉ 100 chủ thẻ đầu tiên" |
| Giọng văn | 4/5 | Phần mở bài hơi dài dòng | Cắt 2 câu đầu, đi thẳng vào đặc quyền |
| Scannability | 2/5 | Toàn đoạn văn dài, không có bullet | Chia lợi ích thành 3-4 bullet points ngắn |

## Lưu ý triển khai

- **Mô tả thang điểm:** Quan trọng nhất — phải mô tả rõ điểm 1 và điểm 5 là gì để AI không tự suy diễn.
- **Output:** Chỉ cần điểm + lý do + đề xuất — không cần khen.
- **Kết hợp:** Dùng cùng Actor-Evaluator Dualism (#42) để tự động Apply đề xuất.
- **Nhóm:** Chương 5 — Reflexion & Evaluation
