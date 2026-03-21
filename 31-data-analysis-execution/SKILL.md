---
name: data-analysis-execution
description: Kỹ thuật Data Scientist — cấm AI tính nhẩm hay ước lượng số liệu từ bảng tính, buộc AI viết code Python/SQL (Pandas, Matplotlib) thực tế để xử lý dữ liệu, rồi chỉ đưa kết luận dựa trên output của code. Dùng khi phân tích CSV/Excel lớn, tính KPI, tìm insight từ dữ liệu thực.
---

# Data Analysis Execution

## Khái niệm

Kỹ thuật này nghiêm cấm AI việc đọc lướt bảng tính (Excel, CSV) rồi tính nhẩm hoặc ước lượng bằng văn bản tự nhiên. Thay vào đó, ép AI phải đóng vai một **Data Scientist**, bắt buộc phải viết **code Python/SQL** để làm sạch, nhóm (group by), tính toán và trực quan hóa dữ liệu một cách chính xác tuyệt đối.

## Bản chất hoạt động

LLM vốn dĩ **cực kỳ kém trong việc làm toán** trên tập dữ liệu lớn. Nếu bạn đưa file Excel 10.000 dòng và hỏi "Tổng doanh thu là bao nhiêu?", AI dùng token prediction sẽ dễ sinh ra ảo giác và đưa ra con số hoàn toàn sai. Tuy nhiên, AI lại **rất giỏi viết code**. Ép nó viết Python để máy tính tự cộng các con số → loại bỏ 100% sai số do "ảo giác tính toán".

## Sơ đồ luồng

```
[Tập dữ liệu thô CSV/Excel]
  ➔ [Kích hoạt Nhân cách: Data Scientist]
  ➔ [AI Viết code Python/SQL để xử lý dữ liệu]
  ➔ [Thực thi code & Trích xuất con số thực tế]
  ➔ [Vẽ biểu đồ & Rút ra Insight từ kết quả Code]
```

## System Prompt mẫu

```
Bạn là một Chuyên gia Phân tích Dữ liệu (Data Scientist). Tôi có cung cấp một tập dữ liệu thô. TUYỆT ĐỐI KHÔNG tính nhẩm, ước lượng hay tự động suy diễn các con số. Bạn bắt buộc phải làm theo các bước sau:
○ Viết mã Python (sử dụng thư viện Pandas) để đọc, làm sạch (xử lý missing values) và định dạng lại dữ liệu.
○ Viết mã để tính toán các chỉ số cốt lõi (KPIs) mà tôi yêu cầu.
○ Trình bày đoạn mã dùng để vẽ biểu đồ trực quan hóa (Matplotlib/Seaborn).
○ Chỉ đưa ra phân tích và kết luận sau khi dựa trên kết quả đầu ra (output) chính xác của các đoạn mã trên.
```

## Ví dụ trước/sau

**Bài toán:** Tính tỷ lệ khách hàng quay lại mua thêm dịch vụ sau khi nhận ưu đãi tặng kèm.

**❌ Không có Prompt:** AI ước lượng "khoảng 15-20% khách hàng sẽ quay lại" — con số bịa.

**✅ Với Data Analysis Execution:**

```python
import pandas as pd

# Step 1: Load và clean data
df = pd.read_excel('transactions.xlsx')
df = df.dropna(subset=['customer_id', 'purchase_date'])

# Step 2: Tính tỷ lệ khách quay lại
promo_customers = df[df['promo_code'] == 'XYZ_BONUS']['customer_id'].unique()
returning = df[
    (df['customer_id'].isin(promo_customers)) &
    (df['product_type'].isin(['Hosting', 'CloudServer']))
]['customer_id'].nunique()

retention_rate = returning / len(promo_customers) * 100
print(f"Retention rate: {retention_rate:.2f}%")
# → Output: Retention rate: 2.47%
```

*"Kết luận: 2.47% — thấp hơn nhiều so với dự đoán thông thường."*

## Lưu ý triển khai

- **Thực thi:** Code do AI viết ra cần được chạy thực tế bởi người dùng hoặc môi trường có Python.
- **Biến thể:** SQL (cho database) hoặc R (cho statistical analysis).
- **Nhóm:** Chương 3 — Kỹ thuật Lập trình & Phân tích Dữ liệu
