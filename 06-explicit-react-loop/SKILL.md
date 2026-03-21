---
name: explicit-react-loop
description: Kỹ thuật ReAct (Reasoning + Acting) — ép AI luân phiên liên tục giữa Thought (suy luận), Action (gọi tool/API), Observation (đọc kết quả) cho đến khi có Final Answer. Dùng khi xây dựng AI Agent, tích hợp external tools, hoặc cần dữ liệu thực tế thay vì hallucination.
---

# Explicit ReAct Loop

## Khái niệm

**ReAct** là viết tắt của **Re**asoning (Suy luận) và **Act**ing (Hành động). Kỹ thuật này buộc AI không được đoán mò dựa trên dữ liệu tĩnh có sẵn. Thay vào đó, nó phải liên tục luân phiên giữa:

- **Thought:** Phân tích vấn đề
- **Action:** Sử dụng công cụ/API bên ngoài lấy dữ kiện thực tế
- **Observation:** Đọc kết quả trả về
- Lặp lại cho đến khi hoàn thành nhiệm vụ

## Bản chất hoạt động

Điểm yếu cốt tử của LLM là **hallucination** và dữ liệu lỗi thời. ReAct Loop giống như cắm cáp internet cho AI và cấp cho nó bộ công cụ làm việc. Bước "Observation" neo giữ các suy luận vào thực tế nguyên bản, ngăn chặn AI tự bịa dữ liệu để lấp liếm lỗ hổng kiến thức.

## Sơ đồ luồng

```
[Nhiệm vụ]
  ➔ LẶP:
    [Thought: Mình đang thiếu thông tin gì?]
    ➔ [Action: Gọi Tool/API]
    ➔ [Observation: Đọc kết quả từ Tool]
  ➔ ĐẾN KHI ĐỦ DỮ LIỆU
  ➔ [Final Answer]
```

## System Prompt mẫu

```
Bạn là một AI Agent có khả năng tự động hóa luồng công việc. Bạn có quyền truy cập vào các công cụ sau: [Tool_1: Mô tả], [Tool_2: Mô tả]. Để giải quyết yêu cầu, bạn bắt buộc phải sử dụng định dạng nghiêm ngặt sau:
○ Thought: Suy nghĩ xem bạn cần làm gì tiếp theo.
○ Action: Tên công cụ bạn chọn sử dụng.
○ Action Input: Tham số truyền vào công cụ.
○ Observation: (Hệ thống sẽ trả về kết quả cho bạn).
Bạn phải lặp lại chu kỳ Thought/Action/Observation này cho đến khi chắc chắn 100% có thể đưa ra 'Final Answer'.
```

## Ví dụ trước/sau

**❌ Không có Prompt:** AI bịa ra thông tin về điều kiện khuyến mãi.

**✅ Với ReAct Loop:**

- Thought 1: Cần xác minh điều kiện chương trình trước khi viết copy.
- Action 1: `query_campaign_database("Promotion rules for free .XYZ or .LOL")`
- Observation 1: *[Chỉ áp dụng khi mua .VN hoặc .COM. Không đề cập ưu đãi khác]*
- Thought 2: Đủ dữ liệu. Bắt đầu soạn thảo nháp.
- Action 2: `generate_copy("rhyming style, buy .VN/.COM get free .XYZ/.LOL")`
- Final Answer: [Nội dung chính xác 100%]

## Lưu ý triển khai

- **Bắt buộc có tool:** Prompt này chỉ phát huy tối đa khi AI được tích hợp với real tools (search engine, database, API).
- **Ứng dụng:** LangChain agents, AutoGPT-style agents, chatbot tra cứu dữ liệu thực tế.
- **Nhóm:** Chương 1 — Cognitive Frameworks & Reasoning
