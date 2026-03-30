---
description: Tự động khởi tạo kho lưu trữ và Đẩy Cổng Thông Tin lên Github
---

Quy trình này hướng dẫn Agent (trợ lý ảo) tự động thực hiện các thao tác kết nối và đẩy toàn bộ dữ liệu Cổng Thông Tin (Web Portal) từ máy tính cá nhân lên kho lưu trữ trực tuyến (Github). Việc này giúp người dùng không cần phải gõ các dòng lệnh Git kỹ thuật phức tạp.

// turbo-all

1. Khởi chạy quá trình đẩy dữ liệu lên mây (Đồng bộ Github)
- Agent phải phân tích Prompt của User để lấy được **Tên Nhà Kho (Repo Name)** và xác định đây là tác vụ **Tạo mới** hay **Cập nhật** kho cũ.
- Chạy file `deploy_portal.py` và truyền Tên Nhà Kho vào làm tham số dòng lệnh. Ví dụ, nếu kho tên là "my-portal":
```bash
cd "e:\Antigravity\e-learning\Internal Portal (Vercel Deploy)"
python deploy_portal.py "my-portal"
```

2. Tạo Báo Cáo & Phản Hồi (DEPLOY_REPORT.md)
Sau khi script Python chạy xong, Agent phải:
- Tự động tạo một file tên là `DEPLOY_REPORT.md` ngay trong thư mục hiện tại.
- Trong file báo cáo, ghi rõ các thông tin:
  + Tình trạng: Tạo mới hay Cập nhật thành công.
  + Tên Kho Git: <Tên do user đặt>
  + Đường dẫn Github: `https://github.com/<username-của-bạn>/<Tên-Repo>`
  + Đường dẫn Vercel: `https://<Tên-Repo>.vercel.app` (ghi chú: Trạng thái chờ user tự Deploy trên web Vercel).
- Báo cáo lại cho người dùng bằng ngôn ngữ dễ hiểu: *"Nhà kho đã sẵn sàng! Tôi đã tạo xong file `DEPLOY_REPORT.md` để sếp lưu trữ link. Bây giờ sếp hãy qua Vercel.com để Import và xuất bản thành web nhé!"*
