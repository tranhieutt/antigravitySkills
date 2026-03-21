---
name: code-readability-baseline
description: Kỹ thuật Clean Code — cấm AI viết code "chạy được là xong", buộc tuân thủ 3 quy tắc: đặt tên biến/hàm có ý nghĩa đầy đủ, tách biệt logic thành hàm riêng (Single Responsibility), và chú thích giải thích TẠI SAO (why) chứ không LÀM GÌ (what). Dùng cho mọi tác vụ viết code cần bảo trì lâu dài.
---

# Code Readability Baseline

## Khái niệm

Kỹ thuật này thiết lập một **"mức sàn"** (baseline) khắt khe về chất lượng mã nguồn. Nó cấm AI viết code theo kiểu **"chạy được là xong"** (quick-and-dirty) hay viết tắt (code golfing). Thay vào đó, AI bắt buộc phải tuân thủ các nguyên tắc **Clean Code**:

- Đặt tên biến/hàm có ý nghĩa
- Cấu trúc rõ ràng
- Chú thích (comments/docstrings) đầy đủ cho các khối logic phức tạp

## Bản chất hoạt động

LLM mặc định tối ưu hóa để đưa ra câu trả lời **ngắn nhất và tốn ít token nhất**. Nó thích dùng biến đơn âm tiết (`x`, `y`, `i`, `data`) hoặc gộp nhiều logic vào một dòng. Bằng cách cài đặt Code Readability Baseline, bạn ép AI chuyển từ tư duy của "Hacker đua tốc độ" sang tư duy của **"Kỹ sư bảo trì hệ thống"** — hy sinh độ ngắn gọn để đổi lấy sự tường minh.

## Sơ đồ luồng

```
[Yêu cầu logic/Thuật toán]
  ➔ [AI phân tích và sinh Code nháp]
  ➔ [Bộ lọc Clean Code: Xóa tên biến tối nghĩa, tách hàm quá dài, bổ sung Docstring]
  ➔ [Mã nguồn Dễ đọc, Chuẩn công nghiệp]
```

## System Prompt mẫu

```
Bạn là một Kỹ sư phần mềm theo trường phái Clean Code. Mọi đoạn mã bạn sinh ra phải vượt qua 'Code Readability Baseline'. Bắt buộc tuân thủ 3 quy tắc:
○ Không dùng tên biến/hàm viết tắt (ví dụ: dùng calculateTotalCost thay vì calcTot).
○ Tách biệt các logic độc lập thành các hàm riêng biệt (Single Responsibility).
○ Thêm chú thích (Comments) để giải thích TẠI SAO (Why) logic này lại được viết như vậy, không phải nó LÀM GÌ (What - vì bản thân đoạn code đã thể hiện điều đó).
```

## Ví dụ trước/sau

**Bài toán:** Hàm tính tiêu hao năng lượng tàu vũ trụ khi di chuyển.

**❌ Không có Prompt:**

```javascript
function calc(d, isS) {
  let e = d * 10;
  if (isS) e = e * 2;
  return e;
}
```

*(1 tháng sau bạn không biết `d`, `isS`, `e` là gì)*

**✅ Với Code Readability Baseline:**

```javascript
const BASE_ENERGY_PER_CELL = 10; // Baseline từ game balance spreadsheet v2.3

/**
 * Calculates energy consumption for ship movement.
 * @param {number} distanceInCells - Number of grid cells to traverse
 * @param {boolean} isInMagneticStorm - True if path crosses storm zone
 * @returns {number} Total energy consumed
 */
function calculateMovementEnergyCost(distanceInCells, isInMagneticStorm) {
  const baseEnergy = distanceInCells * BASE_ENERGY_PER_CELL;
  
  // Storm zones double energy drain because the ship's magnetic shields
  // must work overtime to counter interference (game design doc, section 4.2)
  if (isInMagneticStorm) {
    return baseEnergy * 2;
  }
  return baseEnergy;
}
```

## Lưu ý triển khai

- **Why vs What:** Comments giải thích WHY — không giải thích WHAT vì code tự nó nói lên điều đó.
- **Magic numbers:** Luôn đặt tên constant cho các con số "ma thuật" (`10` → `BASE_ENERGY_PER_CELL`).
- **Nhóm:** Chương 3 — Kỹ thuật Lập trình & Phân tích Dữ liệu
