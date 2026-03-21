---
name: browser-element-chunking
description: Kỹ thuật Web Data Extraction — thay vì nhồi toàn bộ HTML thô vào AI, "băm nhỏ" trang web theo thẻ HTML logic, gọt bỏ script/style/quảng cáo, đưa từng chunk cho AI trích xuất dữ liệu sạch dạng JSON/CSV. Dùng khi scraping web, price monitoring, competitive intelligence.
---

# Browser Element Chunking

## Khái niệm

Khi bạn muốn AI phân tích một trang web, việc copy-paste toàn bộ mã nguồn HTML (hàng chục ngàn dòng) thường dẫn đến thất bại. Kỹ thuật **"Chunking"** yêu cầu phải **"băm nhỏ"** trang web thành các khối (chunks) logic dựa trên thẻ HTML (`<article>`, `<table>`, `<div class="product">`), đồng thời gọt bỏ toàn bộ "rác" (`<script>`, `<style>`, quảng cáo) **trước khi** đưa cho AI đọc từng phần.

## Bản chất hoạt động

Mã nguồn trang web có tỷ lệ **"Nhiễu/Tín hiệu" (Noise-to-Signal)** rất cao: 80% là code định dạng giao diện, chỉ có 20% là dữ liệu thực sự. Nhồi toàn bộ mã thô vào LLM → nhanh chóng cạn kiệt **Context Window**, AI bỏ sót thông tin quan trọng ở giữa trang (Lost in the Middle) hoặc hallucinate. Bằng cách phân mảnh và làm sạch, chúng ta cô đặc 100% "tín hiệu" để AI xử lý chính xác.

## Sơ đồ luồng

```
[Mã nguồn HTML Trang web]
  ➔ [Parser: Xóa bỏ CSS, Javascript, Header, Footer]
  ➔ [Chunking: Cắt Body thành các khối nhỏ theo <section> hoặc <li>]
  ➔ [Đưa từng khối cho AI phân tích]
  ➔ [AI Trích xuất Dữ liệu Sạch (JSON/CSV)]
```

## System Prompt mẫu

```
Bạn là một Chuyên gia Trích xuất Dữ liệu Web (Web Data Extractor). Dưới đây là các phần mã nguồn HTML đã được phân mảnh (chunked) và làm sạch từ một trang web. Tuyệt đối không giải thích hay phân tích giao diện. Bạn bắt buộc phải:
○ Quét qua từng khối (chunk) được cung cấp.
○ Trích xuất chính xác các thông tin: [Tên Sản phẩm], [Giá tiền], [Thông số kỹ thuật].
○ Trả về kết quả duy nhất dưới định dạng mảng JSON hợp lệ, bỏ qua mọi thẻ HTML còn sót lại.
```

## Ví dụ trước/sau

**Bài toán:** Cào 50 sản phẩm máy tính từ trang e-commerce để phân tích giá đối thủ.

**❌ Không có Prompt:** Nhồi 500KB HTML → AI bị ngợp, hallucinate thông số, bỏ sót sản phẩm.

**✅ Với Browser Element Chunking:**

```python
# Script Python lọc trước khi đưa cho AI
from bs4 import BeautifulSoup

html = get_page_content(url)
soup = BeautifulSoup(html, 'html.parser')

# Gọt bỏ script và style
for tag in soup(['script', 'style', 'header', 'footer']): tag.decompose()

# Lấy đúng 50 product chunks
products = soup.find_all('div', class_='product-item')

# Gửi từng batch 10 chunks cho AI
for batch in chunks(products, 10):
    ai_extract(batch)  # → JSON hoàn hảo
```

**Output AI:** `[{"name": "Laptop A", "price": "15,000,000đ", "ram": "16GB"}, ...]`

## Lưu ý triển khai

- **Tool:** BeautifulSoup (Python), Cheerio (Node.js), hoặc bất kỳ HTML parser nào.
- **Batch size:** 10-20 chunks/lần gọi AI là tối ưu — vừa đủ để AI xử lý mà không quá tải.
- **Nhóm:** Chương 3 — Kỹ thuật Lập trình & Phân tích Dữ liệu
