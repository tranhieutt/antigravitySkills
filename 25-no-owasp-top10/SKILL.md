---
name: no-owasp-top10
description: Kỹ thuật Secure Coding — bật "công tắc DevSecOps" trong AI, cấm sinh code có lỗ hổng OWASP Top 10 (SQL Injection, XSS, Broken Auth...), bắt buộc dùng Parameterized queries, Input Sanitization, và giải thích ngắn biện pháp bảo mật đã dùng. Dùng cho mọi tác vụ viết code có xử lý user input hoặc database.
---

# No OWASP Top 10

## Khái niệm

**OWASP Top 10** là danh sách 10 lỗ hổng bảo mật ứng dụng web nguy hiểm và phổ biến nhất thế giới (SQL Injection, XSS, Broken Access Control...). Kỹ thuật này đóng vai trò như một **chốt chặn kiểm duyệt khắt khe**, cấm AI sinh ra bất kỳ đoạn mã nào có chứa các lỗ hổng này, ép tuân thủ tiêu chuẩn **Secure Coding** từ khâu thiết kế.

## Bản chất hoạt động

LLM được huấn luyện trên hàng tỷ dòng code từ GitHub, StackOverflow — trong đó có rất nhiều code "quick-and-dirty" hoặc đã lỗi thời. Nếu chỉ bảo AI "hãy viết code", nó sẽ chọn cách dễ nhất và thiếu an toàn nhất. Từ khóa **"OWASP Top 10"** bật "công tắc DevSecOps" trong não AI, ép nó truy xuất phân vùng dữ liệu bảo mật để tự kiểm duyệt code nháp.

## Sơ đồ luồng

```
[Yêu cầu viết Code tính năng]
  ➔ [AI sinh Code nháp]
  ➔ [Màng lọc Bảo mật: Quét đối chiếu OWASP Top 10]
  ➔ [Sửa lỗi: Thêm Input Validation, Prepared Statements...]
  ➔ [Mã nguồn Đạt chuẩn DevSecOps]
```

## System Prompt mẫu

```
Bạn là một Chuyên gia Bảo mật Phần mềm (DevSecOps Engineer) cấp cao. Khi tạo ra bất kỳ đoạn mã nguồn nào, bạn BẮT BUỘC phải tuân thủ nguyên tắc 'Secure by Design' (Bảo mật từ khâu thiết kế).

Tuyệt đối không được để xuất hiện bất kỳ lỗ hổng nào thuộc danh sách OWASP Top 10. Luôn luôn sử dụng các phương pháp an toàn như: Parameterized queries (để chống SQL Injection), Input Sanitization/Output Encoding (để chống XSS), và quản lý xác thực chặt chẽ.

Hãy giải thích ngắn gọn bằng 1 dòng về biện pháp bảo mật bạn đã dùng trong code.
```

## Ví dụ trước/sau

**Bài toán:** Viết hàm tìm kiếm user trong database theo username từ form web.

**❌ Không có Prompt — Code nguy hiểm:**

```sql
SELECT * FROM users WHERE username = '" + userInput + "'
```

(Dễ bị SQL Injection bằng cách nhập `' OR '1'='1`)

**✅ Với No OWASP Top 10:**

```javascript
// AI từ chối string concatenation, dùng Parameterized Query
const query = 'SELECT * FROM users WHERE username = ?';
db.execute(query, [sanitize(userInput)]);
// Ghi chú: "Đã dùng parameterized query để vô hiệu hóa SQL Injection (OWASP A03)"
```

## OWASP Top 10 tham khảo

| # | Lỗ hổng | Biện pháp |
|---|---|---|
| A01 | Broken Access Control | RBAC, deny by default |
| A02 | Cryptographic Failures | Mã hóa mạnh, HTTPS |
| A03 | Injection | Parameterized queries |
| A07 | Auth Failures | MFA, session management |
| A09 | Security Logging | Audit logs |

## Lưu ý triển khai

- **Ứng dụng:** Mọi tác vụ viết code backend, API, form xử lý user input.
- **Nhóm:** Chương 3 — Kỹ thuật Lập trình & Phân tích Dữ liệu
