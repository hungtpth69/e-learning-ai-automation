# ⚙️ 02. HƯỚNG DẪN CÀI ĐẶT & SỬ DỤNG (SETUP GUIDE)

Để AI có thể tự động thay bạn gửi ngàn Email hợp pháp, hệ thống cần được cấp quyền và bảo mật qua ứng dụng Mạng lưới (SMTP/API). 

## Cách 1: Dùng Mạng Lưới Gmail Cá Nhân (SMTP) [Đề Cử]
*Hoàn toàn miễn phí, phù hợp cho quy mô nội bộ (dưới 300 mail/ngày).*

1. Đăng nhập Gmail trên trình duyệt. Truy cập trang [Bảo mật Google](https://myaccount.google.com/security) và đảm bảo bạn đã **Bật Xác minh 2 bước**.
2. Truy cập đường link cài đặt mật khẩu ứng dụng: [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
3. Phần "Tên ứng dụng", gõ xuất xứ (Ví dụ: `Antigravity HR`) rồi bấm **Tạo (Create)**.
4. Google sẽ cấp cho bạn một chuỗi **16 chữ cái màu vàng**. (Ví dụ: `gdzl qtxx xxxx zzzz`). Copy đoạn mã này.
5. Mở file `email_config.txt` nằm trong thư mục cài đặt dự án. Dán 16 chữ cái (viết liền tắt khoảng trắng) vào `GMAIL_APP_PASSWORD="..."`. Vẫn trong file này, điền Username Gmail vào `GMAIL_USER="..."`.

## Cách 2: Dùng Dịch Vụ API Resend.com
*Tốc độ truy xuất siêu tốc, tỷ lệ vào thẳng thẻ Inbox chính rất cao. Cho phép gửi 3000 mail/tháng.*
1. Đăng ký tài khoản tại [Resend.com](https://resend.com/).
2. Nhấp vào menu **API Keys** -> **Create API Key** -> Cấp quyền **Full Access**.
3. Hệ thống trả chuỗi `re_xxxxxxxxxxxx`. Copy chuỗi này báo lưu vào dòng `RESEND_API_KEY="..."` ở file `email_config.txt`.
4. Nếu có Tên miền Doanh nghiệp (Ví dụ `.vn`), nhớ truy cập mục **Domains** để xác thực bản quyền gửi thư.

## Khởi chạy chiến dịch
Sau khi cài đặt App Password, bạn thiết lập file CSV `email_contact_list.csv` và template `email_template.html`. Chạy ở Terminal bằng dòng: 
```bash
cd "e:\Antigravity\e-learning\Email Automation (SMTP)"
python email_auto_workflow.py
```
*(Sử dụng thêm các slash command từ Agent nếu muốn triển khai đính kèm File hoặc Automation nâng cao)*
