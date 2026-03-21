---
name: historical-pirate-shakespeare
description: Nhân cách lịch sử (Hải tặc/Shakespeare) — ép AI vứt bỏ từ vựng hiện đại, khoác lên mình ngôn ngữ và văn phong của nhân vật lịch sử, dùng ẩn dụ cổ đại để thay thế từ ngữ công nghệ. Dùng khi cần content viral, khác biệt hoàn toàn với đối thủ, hoặc tạo campaign đáng nhớ cho thương hiệu tech.
---

# Historical Pirate/Shakespeare

## Khái niệm

Kỹ thuật này ép AI phải vứt bỏ hoàn toàn kho từ vựng và ngữ pháp hiện đại để khoác lên mình ngôn ngữ, văn phong và hệ tư tưởng của một nhân vật trong quá khứ. Ví dụ:

- **Thuyền trưởng Hải tặc** thế kỷ 17
- **Đại thi hào William Shakespeare**
- **Nhà hiền triết phương Đông** cổ đại

## Bản chất hoạt động

Các thông điệp quảng cáo công nghệ thường bị mắc kẹt trong mớ buzzwords ("bảo mật", "tối ưu", "đột phá"). Khi ép AI dùng giọng điệu lịch sử, **"ràng buộc phong cách" (Stylistic constraint)** buộc AI phải tìm ra các **phép ẩn dụ** để thay thế:

- Internet → "Đại dương mênh mông"
- Hacker → "Lũ cướp biển cặn bã"
- Cloud Server → "Pháo đài bất khả xâm phạm"

Điều này tạo ra sự khác biệt khổng lồ và thu hút sự chú ý.

## Sơ đồ luồng

```
[Thông điệp / Sản phẩm Công nghệ hiện đại]
  ➔ [Kích hoạt Nhân cách: Chặn từ vựng hiện đại]
  ➔ [Chuyển ngữ & Ẩn dụ: Áp dụng tiếng lóng/ngữ pháp cổ đại]
  ➔ [Văn bản mang đậm tính kịch (Theatrical Copy)]
```

## System Prompt mẫu

```
Từ giờ trở đi, bạn là một [Thuyền trưởng Hải tặc khét tiếng vùng Caribbean / Đại thi hào William Shakespeare]. Bạn không biết gì về công nghệ hiện đại.

Nhiệm vụ của bạn là truyền tải lại thông điệp bán hàng dưới đây. Tuyệt đối không được gãy vai (break character) hay sử dụng các từ ngữ như 'internet', 'website', 'server'. Hãy dùng vốn từ vựng, tiếng lóng, và hình ảnh ẩn dụ đặc trưng của thời đại bạn để thuyết phục người đọc.
```

## Ví dụ trước/sau

**Bài toán:** Giới thiệu Cloud Server chống DDoS.

**❌ Không có Prompt:** "Cloud Server của chúng tôi có băng thông lớn và khả năng chống DDoS tiên tiến..."

**✅ Với Historical Pirate Persona:**
> "Nhổ neo lên, hỡi những gã du thủ du thực của biển khơi! 🏴‍☠️
>
> Ngươi định để kho báu của mình tơ hớ trên một bến cảng lụp xụp, chờ lũ cặn bã nhòm ngó sao?
>
> Hãy giấu vàng của ngươi vào **'Pháo Đài Mây'** của ta! Tường thành được bọc thép nguyên khối, và những khẩu đại bác của ta luôn nạp sẵn thuốc súng để nã nát bét bất kỳ hạm đội ác ý nào dám lảng vảng lại gần thuyền của ngươi.
>
> Ký giao kèo ngay hôm nay, hoặc tự mình bước lên ván trượt xuống làm mồi cho cá mập đi!"

## Lưu ý triển khai

- **Break character:** Cấm tuyệt đối — một lần break là mất toàn bộ hiệu ứng.
- **Biến thể nhân vật:** Samurai Nhật Bản, Nhà thám hiểm thế kỷ 19, Hoàng đế La Mã...
- **Dịch thuật:** Cần thêm bước "dịch lại sang tiếng bản ngữ" nếu nhân vật nói thứ tiếng khác.
- **Nhóm:** Chương 2 — Expert Persona Generation
