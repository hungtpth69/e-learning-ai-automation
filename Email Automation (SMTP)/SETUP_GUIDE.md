# ⚙️ Hướng Dẫn Kích Hoạt Cổng Gửi Email (Setup Guide)

Để Trợ lý AI có thể thay bạn gửi hàng ngàn Email một cách hợp pháp và bảo mật, hệ thống cần được cấp quyền truyền tải từ một trong các nhà cung cấp mạng lưới Email (SMTP/API). 
*Lưu ý: Bạn chỉ cần chọn **MỘT TRONG BA** phương án dưới đây tùy theo quy mô sử dụng của công ty.*

---

## Lựa chọn 1: Dùng Mạng Lưới Gmail Cá Nhân (SMTP)
*Phương án miễn phí, dễ làm nhất. Phù hợp cho nhu cầu nhỏ (dưới 300 mail/ngày).*

1. Đăng nhập Gmail trên trình duyệt. Truy cập trang [Bảo mật Google](https://myaccount.google.com/security) và đảm bảo bạn đã **Bật Xác minh 2 bước**.
2. Truy cập đường link cấp quyền truy cập ứng dụng: [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
3. Phần "Tên ứng dụng", gõ xuất xứ (Ví dụ: `Antigravity Agent`) rồi bấm **Tạo (Create)**.
4. Google sẽ cấp cho bạn một chuỗi **16 chữ cái mầu vàng**. (Ví dụ: `abcd efgh ijkl mnop`). Hãy Copy đoạn mã này.
5. Mở file `email_config.txt` trong thư mục dự án bằng Notepad. Dán 16 chữ cái đó (viết liền tắt khoảng trắng) vào dòng `GMAIL_APP_PASSWORD="..."`. Điền luôn User Gmail của bạn vào dòng `GMAIL_USER="..."`.

---

## Lựa chọn 2: Dùng Dịch Vụ Doanh Nghiệp RESEND (API)
*Trạm phát sóng hiện đại, tốc độ cực siêu tốc, tỷ lệ vào thẳng Inbox cực cao. Miễn phí gửi 3000 mail/tháng.*

1. Đăng ký tài khoản tại [Resend.com](https://resend.com/).
2. Tại màn hình điều khiển (Dashboard), nhấp vào menu **API Keys** -> Chọn **Create API Key**. Lựa chọn quyền **Full Access**.
3. Hệ thống sinh ra một chuỗi mã bắt đầu bằng chữ `re_` (Ví dụ: `re_123456789...`). Hãy Copy chuỗi này.
4. Mở file `email_config.txt`, dán vào dòng `RESEND_API_KEY="..."`.
5. *(Tùy chọn chuyên nghiệp)*: Vào mục **Domains** trên Resend để xác thực Tên miền Website của công ty, giúp bạn gửi email từ đuôi doanh nghiệp (Ví dụ: `tuyendung@tencongty.com`).

---

## Lựa chọn 3: Dùng Tổ Hợp SENDGRID (API Enterprise)
*Nền tảng già cỗi khủng long, phù hợp cho Siêu Chiến Dịch hàng triệu Data.*

1. Đăng ký tài khoản tại [SendGrid.com](https://sendgrid.com/).
2. Bật xác thực hai lớp (2FA) theo yêu cầu của hệ thống.
3. Ở menu bên trái, kéo thả mục **Settings** -> **API Keys** -> **Create API Key** -> Chọn **Full Access**.
4. Lấy chuỗi mã bắt đầu bằng `SG.` dán vào file `email_config.txt` tại dòng cấu hình SendGrid tương ứng.
5. Truy cập mục **Sender Authentication** để xác thực địa chỉ Email thực tế bạn muốn làm "Người Gửi" trước khi bắt hành lên chiến dịch.

---

🎉 **Hoàn Tất Nạp Năng Lượng!** 
Vui lòng lưu kỹ (Save) file `email_config.txt`. Bây giờ hãy quay lại file `README.md` để bắt đầu luyện tập luồng Gửi thư tự động hóa.
