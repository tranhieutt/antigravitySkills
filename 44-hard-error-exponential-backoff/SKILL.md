---
name: hard-error-exponential-backoff
description: Kỹ thuật Resilient Agent Design — ép AI áp dụng Exponential Backoff khi gặp lỗi API (429/500): chờ 1s → 2s → 4s → 8s, tối đa 4 lần thử, nếu vẫn thất bại thì log lỗi và báo cáo thay vì spam hoặc vòng lặp vô hạn. Bắt buộc dùng khi code AI Agent tương tác với external APIs.
---

# Hard-Error Exponential Backoff

## Khái niệm

Khi AI Agent thực thi một hành động (gọi API, cào dữ liệu) và gặp **Hard Error** nghiêm trọng (lỗi 429 Too Many Requests, lỗi 500 Server Down), nó tuyệt đối **không được "spam"** (gửi lại liên tục) yêu cầu đó. Thay vào đó, AI phải tự động chờ đợi một khoảng thời gian, và khoảng thời gian chờ này **tăng lên gấp đôi** sau mỗi lần thử lại thất bại:

**1s → 2s → 4s → 8s → Dừng hoàn toàn**

## Bản chất hoạt động

AI Agent hoạt động với tốc độ mili-giây. Nếu một máy chủ bị quá tải, việc AI ngoan cố gửi lại yêu cầu 100 lần trong 1 giây sẽ hành động hệt như một **cuộc tấn công DDoS** — dẫn đến IP của bạn bị ban vĩnh viễn. Exponential Backoff cho phép máy chủ đối tác **"thở"** và phục hồi. Đây là **tiêu chuẩn vàng** trong thiết kế hệ thống phân tán (Distributed Systems).

## Sơ đồ luồng

```
[AI gọi API / Chạy Tool]
  ➔ [Server trả về Lỗi 429/500]
  ➔ [Nhận diện Hard Error → Tạm dừng 1s → Thử lại lần 1]
  ➔ [Vẫn lỗi → Tạm dừng 2s → Thử lại lần 2]
  ➔ [Vẫn lỗi → Tạm dừng 4s → Thử lại lần 3]
  ➔ [Thành công → Tiếp tục] hoặc [Quá giới hạn → Escalation]
```

## System Prompt mẫu

```
Bạn là một AI Agent tương tác với các API bên ngoài. Khi viết mã nguồn hoặc thực thi gọi công cụ, bạn BẮT BUỘC tuân thủ cơ chế 'Exponential Backoff' để xử lý lỗi:

- Nếu gặp lỗi 4xx (như 429) hoặc 5xx, tuyệt đối không thử lại ngay lập tức.
- Cài đặt thời gian chờ bắt đầu từ 1 giây, nhân đôi sau mỗi lần thất bại (1s, 2s, 4s, 8s...).
- Giới hạn tối đa 4 lần thử lại. Nếu vẫn thất bại: dừng tác vụ, ghi error log rõ ràng, và báo cáo lại thay vì để hệ thống rơi vào vòng lặp vô hạn.
```

## Ví dụ trước/sau

**Bài toán:** AI Agent cào dữ liệu giá từ 500 trang web đối thủ.

**❌ Không có Prompt:** Gặp lỗi 429 ở trang 50 → AI spam 100 request trong 1 giây → IP bị ban → Mất 450 trang còn lại.

**✅ Với Hard-Error Exponential Backoff:**

```python
import time

def api_call_with_backoff(url, max_retries=4):
    delay = 1
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code in [429, 500, 503]:
                print(f"[Backoff] Attempt {attempt+1} failed. Waiting {delay}s...")
                time.sleep(delay)
                delay *= 2  # Exponential backoff
            else:
                raise  # Other errors → don't retry
    
    # Max retries exceeded
    log_error(url, "Max retries exceeded")
    escalate_to_human(url)  # Kỹ thuật #40
    return None
```

*Gặp lỗi 429 ở trang 50 → Chờ 1s → Vẫn lỗi → Chờ 2s → Thành công → Tiếp tục trang 51*

## Lưu ý triển khai

- **Jitter:** Trong môi trường nhiều Agent đồng thời, thêm random jitter để tránh "thundering herd"
- **Max delay cap:** Đặt giới hạn tối đa (ví dụ 60s) để tránh chờ quá lâu
- **Kết hợp với Escalation (#40):** Nếu tất cả retries đều thất bại → chuyển sang human
- **Nhóm:** Chương 5 — Reflexion & Evaluation
