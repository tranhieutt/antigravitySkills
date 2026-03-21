---
name: ooda-loop-analyzer
description: Kỹ thuật vòng lặp OODA (Observe-Orient-Decide-Act) — buộc AI phân tích tình huống theo 4 bước quân sự trước khi hành động. Đặc biệt mạnh ở bước Orient (định hướng nguyên nhân sâu xa). Dùng khi phân tích biến động dữ liệu, khủng hoảng truyền thông, hoặc tối ưu chiến lược kinh doanh.
---

# OODA Loop Analyzer

## Khái niệm

**OODA** (Observe - Orient - Decide - Act) vốn là học thuyết chiến thuật quân sự do phi công tiêm kích **John Boyd** phát triển. Khi chuyển hóa thành System Prompt, nó ép AI không được phản xạ theo thói quen hay bám cứng vào kế hoạch cũ. Thay vào đó, AI phải liên tục đánh giá lại môi trường, tìm ra căn nguyên của sự thay đổi, ra quyết định và hành động để thích ứng ngay lập tức.

## Bản chất hoạt động

Điểm "ăn tiền" nhất là chữ "O" thứ hai — **Orient (Định hướng)**. Các AI thông thường hay mắc bệnh "thấy hiện tượng là nhảy ngay vào giải pháp" (từ Observe nhảy thẳng sang Act). Bước Orient buộc AI phải lắp ghép dữ liệu thô vào bối cảnh hiện tại, phân tích tâm lý, đối chiếu ràng buộc hệ thống để tìm ra **nguyên nhân thực sự** trước khi hành động.

## Sơ đồ luồng

```
[Tín hiệu môi trường / Dữ liệu mới]
  ➔ [Observe: Gom dữ liệu thô]
  ➔ [Orient: Phân tích nguyên nhân sâu xa & Đặt vào bối cảnh]  ← QUAN TRỌNG NHẤT
  ➔ [Decide: Chốt chiến thuật]
  ➔ [Act: Thực thi & Lặp lại vòng lặp để đo lường kết quả]
```

## System Prompt mẫu

```
Bạn là một chuyên gia phân tích và tối ưu hóa hoạt động theo vòng lặp OODA. Đứng trước bất kỳ biến động dữ liệu hay tình huống nào, bạn bắt buộc phải trình bày quy trình 4 bước sau trước khi thực hiện:
○ Observe (Quan sát): Liệt kê các dữ kiện thực tế đang diễn ra.
○ Orient (Định hướng): Giải thích ý nghĩa của các dữ kiện này, tại sao nó lại xảy ra trong bối cảnh hiện tại? (Đây là bước quan trọng nhất).
○ Decide (Quyết định): Đề xuất một chiến thuật hoặc hướng giải quyết tối ưu.
○ Act (Hành động): Cụ thể hóa quyết định thành các bước triển khai ngay lập tức.
```

## Ví dụ trước/sau

**Tình huống:** Landing Page có traffic tốt nhưng tỷ lệ chuyển đổi (CR) tụt thê thảm sau 2 ngày.

**❌ Không có Prompt:** AI đề xuất ngay "cải thiện UI/UX" mà không phân tích nguyên nhân.

**✅ Với OODA Loop:**

- **Observe:** Tỷ lệ thoát trang tăng 45% ngay tại khu vực đọc thể lệ ưu đãi. Thời gian onsite giảm.
- **Orient:** Khách hàng đang bị confuse bởi điều kiện ưu đãi phức tạp — không phải vấn đề visual.
- **Decide:** Đơn giản hóa phần trình bày điều kiện, A/B test 2 phiên bản.
- **Act:** Rewrite thể lệ thành bullet points ≤5 dòng. Deploy ngay hôm nay. Đo lại sau 24h.

## Lưu ý triển khai

- **Ứng dụng tốt nhất:** Phân tích số liệu marketing, khủng hoảng truyền thông, tối ưu vận hành real-time.
- **Lặp lại vòng lặp:** OODA là vòng lặp liên tục — sau Act lại Observe để kiểm tra kết quả.
- **Nhóm:** Chương 1 — Cognitive Frameworks & Reasoning
