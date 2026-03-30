# 📧 Email Automation (Hệ Thống Gửi Email API/SMTP)

> **Hệ thống Gửi Email Tự Động Hóa Tốc Độ Cao**
> Quản lý bởi Agent. Dành cho người vận hành (Non-tech) thiết lập và gửi hàng ngàn Email cá nhân hóa mà không cần biết code.

## 🎯 Mục Đích Hoạt Động
Phần mềm này giúp bạn kết nối thẳng vào các Trạm viễn thông Gửi thư lớn nhất thế giới để cá nhân hóa nội dung (thay tên, thay mức lương, đính kèm file riêng) và gửi hàng loạt một cách hoàn toàn tự động.

## 🛠 Hướng Dẫn Cài Đặt Tài Khoản Dành Cho Người Mới (Step-by-Step)
*Để code hiểu được mộc dấu của công ty bạn, bạn cần Đăng ký và Lấy Chìa Khóa (Mật khẩu/API Key) từ 1 trong 3 nhà mạng bên dưới:*

### Lựa chọn 1: Dùng Mạng Lưới Gmail Cá Nhân (SMTP)
*Phù hợp cho nhu cầu bé (dưới 300 mail/ngày).*
Google không cho phép phần mềm đăng nhập bằng Mật khẩu thường của bạn. Bạn phải tạo "Mật khẩu Ứng dụng":
1. Truy cập [Bảo mật Google](https://myaccount.google.com/security) và **Bật Xác minh 2 bước**.
2. **[TUYỆT CHIÊU ẨN]** Google gần đây đã giấu ô này cực kỳ kỹ. Bạn hãy copy nguyên đường link bí mật này dán lên Trình duyệt để vào thẳng: [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
   *(Hoặc gõ chữ "Mật khẩu ứng dụng" / "App passwords" vào ô Kính Lúp tìm kiếm ở trên đỉnh trang web).*
3. Ở màn hình hiện ra, phần "Tên ứng dụng", gõ xuất xứ (Ví dụ: `Antigravity Agent`) rồi bấm **Tạo (Create)**.
4. Google sẽ hiện ra một cái bảng vàng có **16 chữ cái** (VD: `abcd efgh ijkl mnop`). Hãy **COPY** mật khẩu này.
5. Trở về thư mục, mở file `email_config.txt` lên, dán vào dòng `GMAIL_APP_PASSWORD="..."`.

### Lựa chọn 2: Dùng Dịch Vụ Cấp Doanh Nghiệp RESENDS
*Tốc độ cực nhanh, tỷ lệ vào Inbox gần 100%, không lo khóa tài khoản.*
1. Vào trang web [Resend.com](https://resend.com/) và bấm nút đen **Get Started** để đăng ký tài khoản (Nên bấm Continue with Github/Google cho nhanh).
2. Khi vào giao diện chính (Dashboard), nhìn sang menu Trái, chọn nút chìa khóa **API Keys**.
3. Bấm nút đen **Create API Key** ở góc phải trên. Cửa sổ hỏi tên, hãy gõ (VD: `Email Agent`), Chọn mục `Full Access` rồi nhấn tạo.
4. Màn hình sẽ hiện ra một chuỗi cực dài bắt đầu bằng `re_` (Ví dụ: `re_123456789_xxxxxxxx`). **BẤM COPY NGAY LẬP TỨC** vì nó chỉ hiện 1 lần.
5. (Tuỳ chọn) Mở menu Trái, chọn **Domains**. Bấm **Add Domain** và làm theo hướng dẫn để thêm Tên miền Website của công ty bạn (Ví dụ `tencongty.com`). Nếu không có Domain, Resend cho phép test gửi qua cổng ảo `<onboarding@resend.dev>` nhưng chỉ thư sẽ chỉ bay vào email của chính bạn.
6. Trở lại file `email_config.txt`. Dán chuỗi `API Key` cực dài này vào dòng `RESEND_API_KEY="..."`. Đồng thời trỏ súng bằng cách đổi cấu hình `EMAIL_PROVIDER="resend"`.

### Lựa chọn 3: Dùng SENDGRID (Cho Siêu Chiến Dịch Hàng Triệu Data)
1. Đăng ký tài khoản tại [SendGrid.com](https://sendgrid.com/).
2. Chọn menu Settings -> API Keys -> Create API Key -> Full Access. Lấy chuỗi mã bắt đầu bằng `SG.xxxx`.
3. Nhớ vào Sender Authentication để verify một Email thực gửi của bạn. Điền thông tin mã hóa vào dòng `SENDGRID_API_KEY="..."` trong file `email_config.txt`.

## ⚙️ Cấu Hình Khởi Chạy
Để đảm bảo bảo mật tuyệt đối, chúng ta KỴ việc dán Mật khẩu thẳng vào File lập trình. Hãy làm như sau:
1. Nhìn vào thư mục này, bạn sẽ thấy 1 file có tên là `email_config.txt`.
2. Mở file `email_config.txt` bằng Notepad. Bạn sẽ thấy các dòng điền sẵn.
3. Dán các Mã/Chìa Khóa bạn vừa lấy ở trên vào đúng dòng tương ứng trong ngoặc kép. (Ví dụ: `GMAIL_APP_PASSWORD="abcd efgh kh"`).
4. Tiếp theo, mở file Excel/ CSV `email_contact_list.csv` và nhập thông tin người nhận thật của bạn.

*(Lưu ý: Mọi code đã sử dụng thư viện điện toán tiêu chuẩn, không yêu cầu người dùng phải gõ lệnh cài đặt thêm bất kỳ thư viện nào (`Zero pip install`)).*

## 🚀 Hướng Dẫn Kích Hoạt Phần Mềm
Sau khi đã gắn khóa vào code, ở cửa sổ lệnh (Terminal), bạn chỉ cần gõ 1 câu lệnh này để Bot bắt đầu xả xúng:
```
/sendmesemail
```

*[Đặc biệt] Để chạy luồng Gửi Thư Mời Nhận Việc (Có đính kèm File PDF/Docs)*:
```
/gui-offer-letter
```

## 📊 Hệ Thống Hoạt Động & Kết Quả
Màn hình Máy tính sẽ hiện từng dòng báo cáo `[➔] THÀNH CÔNG`. Khi màn hình dừng lại, tức là Agent đã gửi xong 100% tệp. Hãy mở file `email_sent_log.csv` để đối soát xem thư nào gửi thành công, thư nào thất bại do sai Email ngay trên máy tính của bạn rành rọt như một Thư ký Excel.
