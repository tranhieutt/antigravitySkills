---
name: master-plan-and-solve
description: Kỹ thuật Plan-and-Solve (PS) — ép AI thực hiện 2 pha tách biệt hoàn toàn: (1) Lập kế hoạch chi tiết, (2) Thực thi theo đúng kế hoạch. Dùng khi viết code phức tạp, lập kế hoạch nội dung dài hạn, hoặc bài toán vận hành nhiều ràng buộc.
---

# Master Plan-and-Solve

## Khái niệm

Dựa trên nền tảng lý thuyết Plan-and-Solve (PS), kỹ thuật này yêu cầu AI không được bắt tay vào giải quyết vấn đề ngay. Thay vào đó, nó buộc AI thực hiện 2 pha tách biệt hoàn toàn:

1. **Pha 1 — Plan:** Lập ra bản kế hoạch chi tiết các bước cần làm.
2. **Pha 2 — Solve:** Lần lượt giải quyết bài toán theo đúng bản kế hoạch đó.

## Bản chất hoạt động

Đây là bản nâng cấp khắc phục điểm yếu của Step-by-Step: khi bài toán quá dài và phức tạp, AI "vừa nghĩ vừa làm" dễ bị lạc hướng hoặc bỏ quên điều kiện ban đầu. Bằng cách ép AI "vẽ bản đồ" trước khi "đi đường", chúng ta cung cấp bird's-eye view, giúp duy trì tính nhất quán từ đầu đến cuối.

## Sơ đồ luồng

```
[Input phức tạp]
  ➔ [AI Tạo Bản Kế Hoạch: Bước 1 → Bước 2 → Bước n]
  ➔ [AI Thực thi giải quyết từng bước theo Kế hoạch]
  ➔ [Kết quả cuối cùng]
```

## System Prompt mẫu

```
Bạn là một chuyên gia giải quyết vấn đề cấp cao. Với mỗi yêu cầu được giao, bạn phải tuân thủ nghiêm ngặt 2 giai đoạn sau trước khi đưa ra kết luận:
● Pha 1 - Lập kế hoạch (Plan): Phân tích vấn đề và liệt kê rõ ràng, rành mạch các bước cần thiết để giải quyết.
● Pha 2 - Thực thi (Solve): Dựa vào bản kế hoạch vừa lập, lần lượt giải quyết từng bước một để đi đến đáp án cuối cùng.
```

## Ví dụ Before/After

**Câu hỏi:** Ba vòi nước cùng chảy vào bể. Vòi 1: đầy trong 4 giờ, Vòi 2: đầy trong 6 giờ. Cả 3 cùng mở thì sau 2 giờ đầy. Vòi 3 tốn bao lâu?

**✅ Pha 1 — Kế hoạch:**

1. Tính năng suất vòi 1
2. Tính năng suất vòi 2
3. Tính năng suất tổng 3 vòi
4. Tính năng suất vòi 3 = Tổng − (Vòi 1 + Vòi 2)
5. Nghịch đảo để ra thời gian

**✅ Pha 2 — Thực thi:**

1. Vòi 1: 1/4 bể/giờ
2. Vòi 2: 1/6 bể/giờ
3. Tổng 3 vòi: 1/2 bể/giờ
4. Vòi 3: 1/2 − 5/12 = 1/12 bể/giờ
5. **Kết luận: Vòi 3 cần 12 giờ.**

## Lưu ý triển khai

- **Ứng dụng tốt nhất:** Agent viết code, lập kế hoạch nội dung dài hạn, logistics nhiều ràng buộc.
- **Hạn chế:** Tốn token; nếu Plan ở Pha 1 sai, Pha 2 cũng sai theo (hiệu ứng domino).
- **Nhóm:** Chương 1 — Cognitive Frameworks & Reasoning
