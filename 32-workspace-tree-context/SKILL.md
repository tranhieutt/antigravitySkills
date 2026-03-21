---
name: workspace-tree-context
description: Kỹ thuật cung cấp bản đồ dự án — yêu cầu cung cấp cây thư mục (directory tree) cho AI trước khi thảo luận phát triển tính năng, ép AI định vị chính xác vị trí file cần tạo/sửa và đường dẫn import/export đúng với cấu trúc thực tế. Dùng cho mọi dự án lập trình đa file để tránh AI "lạc đường".
---

# Workspace Tree Context

## Khái niệm

Kỹ thuật này yêu cầu bạn phải cung cấp **toàn bộ sơ đồ cấu trúc thư mục** (Directory Tree) của dự án cho AI **trước khi** bắt đầu thảo luận về việc thêm tính năng hay sửa đổi hệ thống. Nó ép AI phải nhận thức được bức tranh tổng thể về:

- Nơi lưu trữ tài nguyên
- Nơi đặt logic lõi
- Nơi chứa giao diện

Từ đó đưa ra các đề xuất vị trí file và đường dẫn (import paths) chính xác tuyệt đối.

## Bản chất hoạt động

LLM mặc định bị **"mù không gian"** (spatial blindness). Nếu chỉ đưa cho nó một đoạn code và bảo "Tạo thêm module mới", nó sẽ không biết nên đặt file đó ở đâu — có thể xúi bạn tạo file linh tinh ở thư mục gốc (root), hoặc gọi sai đường dẫn thư viện. Bằng cách cung cấp Workspace Tree, bạn đang **cấp cho AI một bản vẽ thi công** — nó sẽ biết tận dụng lại các file utils đã có sẵn.

## Sơ đồ luồng

```
[Dán Cây Thư mục Dự án (Workspace Tree)]
  ➔ [AI lập bản đồ tư duy về kiến trúc hiện tại]
  ➔ [Yêu cầu thảo luận ý tưởng/tính năng mới]
  ➔ [AI định vị chính xác vị trí cần thao tác]
  ➔ [Đề xuất file cần sửa/tạo mới với đường dẫn liên kết 100% chính xác]
```

## System Prompt mẫu

```
Đây là cấu trúc cây thư mục (Workspace Tree) hiện tại của dự án:
[Dán output của lệnh `tree` vào đây]

Khi chúng ta thảo luận và chốt các ý tưởng phát triển tính năng mới, bạn BẮT BUỘC phải:
○ Đánh giá xem tính năng này nên được đặt ở thư mục nào để đảm bảo tính module hóa.
○ Chỉ ra chính xác tên các file cần tạo mới hoặc cần cập nhật (dựa trên cây thư mục trên).
○ Đảm bảo mọi đường dẫn liên kết (import/export paths) giữa các file là hoàn toàn khớp với cấu trúc thực tế.
```

## Ví dụ trước/sau

**Bài toán:** Phân tách cơ chế nâng cấp: Basic Upgrade (mọi lúc) vs Station Upgrade (chỉ ở Space Station).

**❌ Không có Prompt:** AI xúi tạo file `upgrade.js` ở thư mục gốc, import sai path → Build error.

**✅ Với Workspace Tree Context:**

```
Cây thư mục:
src/
  modules/
    ResourceModule.js
    SpaceStationModule.js
  systems/
    Upgrade/
      BasicUpgrade.js
  entities/
    Ship.js
```

AI phân tích và phản hồi:

- *"Interface `IStationUpgrade` nên tạo trong `src/systems/Upgrade/`*
- *Logic kiểm tra `isAtStation` nên đặt ở `src/modules/SpaceStationModule.js`*
- *Import trong Ship.js: `import { IStationUpgrade } from '../systems/Upgrade/IStationUpgrade'`"*

## Lưu ý triển khai

- **Lệnh lấy tree:** Windows: `tree /F`, Linux/macOS: `find . -type f | head -50`
- **Khi tree quá dài:** Có thể chỉ dán phần liên quan đến tính năng đang thảo luận.
- **Nhóm:** Chương 3 — Kỹ thuật Lập trình & Phân tích Dữ liệu
