---
name: headless-shell-automation
description: Kỹ thuật CLI Agent — cấm AI đưa ra hướng dẫn thao tác bằng tay, buộc AI viết code Bash/Python/Playwright chạy ngầm (headless) với logging và error handling đầy đủ. Dùng để tự động hóa tác vụ tải file, xử lý ảnh hàng loạt, web scraping, hoặc bất kỳ quy trình lặp lại có thể script hóa.
---

# Headless Shell Automation

## Khái niệm

**"Headless"** nghĩa là hoạt động ngầm, không có giao diện đồ họa (GUI). Kỹ thuật này ép AI phải giải quyết bài toán bằng cách viết và thực thi các tập lệnh qua:

- **CLI** (Bash/PowerShell)
- **Trình duyệt ẩn** (Playwright/Puppeteer headless mode)

Thay vì hướng dẫn con người thao tác tay.

## Bản chất hoạt động

Giao diện đồ họa (cửa sổ, nút bấm) được thiết kế cho mắt và tay của con người, nhưng lại cực kỳ cồng kềnh và chậm chạp đối với máy móc. **Ngôn ngữ "mẹ đẻ" của máy tính là shell commands**. Khi AI tư duy theo hướng Headless, nó có thể tải file, đổi tên, gọi API, hoặc cào dữ liệu web với tốc độ ánh sáng ở chế độ background — bỏ qua hoàn toàn việc tải hình ảnh, CSS hay hiệu ứng giao diện không cần thiết.

## Sơ đồ luồng

```
[Yêu cầu Tự động hóa]
  ➔ [AI sinh ra Tập lệnh CLI/Bash hoặc Script Trình duyệt ẩn]
  ➔ [Thực thi ngầm trong Sandbox/Terminal]
  ➔ [Hệ thống trả về Output/Lỗi (Logs) cho AI]
  ➔ [AI đọc Log, sửa lỗi nếu có, hoặc hoàn thành tác vụ]
```

## System Prompt mẫu

```
Bạn là một Tác tử Tự động hóa Dòng lệnh (CLI Automation Agent). Nhiệm vụ của bạn là giải quyết yêu cầu dưới đây BẰNG CODE (Bash, Python, hoặc Node.js Playwright/Puppeteer).

Tuyệt đối không đưa ra hướng dẫn để tôi thao tác bằng tay (click chuột). Mọi giải pháp phải được thiết kế để chạy ngầm (headless), tự động hoàn toàn không cần sự can thiệp của con người.

Bắt buộc phải có cơ chế ghi log (logging) và xử lý lỗi (error handling) nếu lệnh bị nghẽn mạng hoặc thất bại.
```

## Ví dụ trước/sau

**Bài toán:** Tải thư mục ảnh PNG từ server, convert sang WebP, xóa ZIP gốc.

**❌ Không có Prompt:** "Bạn vào Chrome, truy cập link, tải file về, mở GIMP, export từng ảnh..."

**✅ Với Headless Shell Automation:**

```bash
#!/bin/bash
set -e  # Exit on error

LOG_FILE="./conversion.log"

# Bước 1: Tải im lặng không có giao diện
echo "[$(date)] Downloading assets..." | tee -a $LOG_FILE
curl -sO https://server.com/assets.zip || {
  echo "[ERROR] Download failed" | tee -a $LOG_FILE; exit 1;
}

# Bước 2: Giải nén im lặng
unzip -q assets.zip -d ./images/ 2>> $LOG_FILE

# Bước 3: Batch convert PNG → WebP
mogrify -format webp ./images/*.png 2>> $LOG_FILE

# Bước 4: Dọn dẹp
rm assets.zip ./images/*.png

echo "[$(date)] Done! Processed $(ls ./images/*.webp | wc -l) files" | tee -a $LOG_FILE
```

*→ Toàn bộ công việc được giải quyết trong 2 giây chỉ bằng một phím Enter*

## Lưu ý triển khai

- **Error handling:** Luôn include `set -e` (Bash) hoặc try/catch để dừng khi có lỗi thay vì tiếp tục với dữ liệu sai.
- **Logging:** Timestamp mọi bước để dễ debug.
- **Ứng dụng:** CI/CD pipeline, batch file processing, scheduled automation, web scraping.
- **Nhóm:** Chương 3 — Kỹ thuật Lập trình & Phân tích Dữ liệu
