---
description: how to update skills from the awesome-skills repository
---
Khi người dùng yêu cầu cập nhật skill, hãy thực hiện lần lượt các bước sau:

1. Kéo repo lấy source mới nhất:
   Di chuyển vào thư mục `d:\Antigravity-awesome-skills` và chạy `git pull` để cập nhật repo. Nếu thư mục chưa tồn tại, hãy dùng `git clone https://github.com/sickn33/antigravity-awesome-skills .`
   // turbo

2. So sánh và kiểm tra, cập nhật skills còn thiếu:
   Cài đặt/Copy các thư mục kỹ năng từ `d:\Antigravity-awesome-skills\skills` sang `C:\Users\x1 carbon\.gemini\antigravity\skills` nếu như chúng chưa tồn tại.
   // turbo

3. Cập nhật file README quản lý skills:
   Đếm lại tổng số lượng thư mục trong `C:\Users\x1 carbon\.gemini\antigravity\skills`, sau đó tiến hành chỉnh sửa `C:\Users\x1 carbon\.gemini\antigravity\skills\README.md` để:
   - Cập nhật số lượng thư mục kỹ năng hiện tại
   - Cập nhật thời gian ngày cập nhật cuối.
   - Thêm vào log lịch sử cập nhật ở cuối file.

4. Cập nhật file skills.csv:
   Thực thi lệnh Python để chạy file `generate_skills_csv.py` đang được lưu trong `C:\Users\x1 carbon\.gemini\antigravity\skills` nhằm kết xuất toàn bộ dữ liệu mới nhất.
   // turbo

5. Đẩy các file trong folder skills lên GitHub:
   Di chuyển vào thư mục `C:\Users\x1 carbon\.gemini\antigravity\skills` và thực hiện đẩy lên kho lưu trữ từ xa:

   ```bash
   git add .
   git commit -m "chore: auto-update skills via Antigravity workflow"
   git push origin main
   ```

   *(Đảm bảo thư mục này đã kết nối remote `origin` trỏ tới `https://github.com/tranhieutt/antigravitySkills`)*
   // turbo
