---
name: tri-agent-deliberation
description: Kỹ thuật Tree of Thoughts (ToT) — ép LLM phân vai thành 3+ chuyên gia độc lập, tranh luận phản biện chéo, biểu quyết chọn phương án tối ưu. Dùng khi thiết kế hệ thống phức tạp, ra quyết định kinh doanh quan trọng, hoặc cần giải pháp đa chiều.
---

# Tri-Agent Deliberation

## Khái niệm

Dựa trên nền tảng lý thuyết **Tree of Thoughts (ToT)**, kỹ thuật này không yêu cầu AI đưa ra một luồng suy nghĩ duy nhất. Thay vào đó, nó ép LLM phải phân vai thành 3 (hoặc nhiều) chuyên gia độc lập. Các "chuyên gia" sẽ đưa ra các hướng giải quyết khác nhau, tự tranh luận, phản biện chéo và cuối cùng biểu quyết để chọn ra phương án tối ưu nhất.

## Bản chất hoạt động

Điểm yếu lớn nhất của AI là hội chứng "đâm lao thì phải theo lao" (Greedy Decoding). Nếu từ khóa đầu tiên AI sinh ra bị sai lệch, toàn bộ câu trả lời phía sau sẽ bị bẻ cong theo cái sai đó. Bằng cách tạo ra nhiều "chuyên gia" cùng suy nghĩ song song, AI phải **rẽ nhánh tư duy** và tự nhận thức được lỗ hổng logic.

## Sơ đồ luồng

```
[Bài toán hóc búa]
  ➔ [Chuyên gia A đề xuất] + [Chuyên gia B đề xuất] + [Chuyên gia C đề xuất]
  ➔ [Hội đồng phản biện: A đánh giá B, C tìm lỗi A...]
  ➔ [Loại bỏ hướng đi sai, tổng hợp điểm ưu việt]
  ➔ [Kết luận hoàn hảo nhất]
```

## System Prompt mẫu

```
Bạn hãy đóng vai một hội đồng gồm 3 chuyên gia độc lập để giải quyết vấn đề sau.
● Bước 1: Mỗi chuyên gia hãy đưa ra một hướng suy luận và cách giải quyết của riêng mình.
● Bước 2: Các chuyên gia hãy đọc kỹ giải pháp của nhau, chỉ ra các lỗ hổng logic, những rủi ro tiềm ẩn hoặc điểm chưa tối ưu.
● Bước 3: Sau khi tranh luận, hội đồng hãy thống nhất và đưa ra một giải pháp cuối cùng hoàn chỉnh nhất, loại bỏ mọi sai sót đã được phát hiện.
```

## Ví dụ trước/sau

**Bài toán:** Thiết kế cơ chế debuff "Injured" cho game chiến thuật theo lượt.

- **Chuyên gia 1 (Hệ thống):** Trừ thẳng HP mỗi khi dính đòn.
- **Chuyên gia 2 (UX):** *Phản đối* — trừ HP ở đầu lượt tiếp theo, cho phép đồng đội cứu chữa kịp thời.
- **Chuyên gia 3 (Cân bằng):** *Bổ sung* — class Rookie chữa debuff này nhận thêm kinh nghiệm thăng cấp.
- **Kết luận:** Cơ chế chốt kết hợp ưu điểm của Chuyên gia 2 + 3.

## Lưu ý triển khai

- **Ứng dụng tốt nhất:** Thiết kế hệ thống phức tạp, ra quyết định kinh doanh, phân tích rủi ro đa chiều.
- **Biến thể:** Có thể dùng 2 chuyên gia (đối lập nhau) hoặc 5+ chuyên gia (cho bài toán cực phức tạp).
- **Nhóm:** Chương 1 — Cognitive Frameworks & Reasoning
