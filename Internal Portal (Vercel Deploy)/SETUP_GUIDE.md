# ⚙️ Hướng Dẫn Thiết Lập Hạ Tầng Triển Khai Web (Setup Guide)

Để trợ lý AI có thể tự động đẩy mã nguồn từ máy tính của bạn lên internet và biến nó thành một trang web hoàn chỉnh, hệ thống cần được liên kết với 2 nền tảng máy chủ lớn nhất thế giới: **Github** (Kho lưu trữ mã nguồn) và **Vercel** (Trạm phát sóng website).

*Lưu ý: Quá trình thiết lập hạ tầng này chỉ cần làm **một lần duy nhất** trên máy tính.*

---

## Bước 1: Cài đặt Dụng Cụ Giao Tiếp Mã Nguồn (Local)
Đây là các bộ phần mềm giúp máy tính của bạn biết cách "nói chuyện" với hệ thống máy chủ Github.
1. Bạn vào [git-scm.com/downloads](https://git-scm.com/downloads), click dòng `Download for Windows`. Tải về cài đặt, cứ liên tục bấm `Next` đến lúc hoàn thành.
2. Tiếp tục vào [cli.github.com](https://cli.github.com/), chọn tải bản cho `Windows` và cài đặt bình thường.

## Bước 2: Thiết lập Tài khoản Nhà Kho (Github)
1. Lên trình duyệt web truy cập [Github.com](https://github.com/) đăng ký một tài khoản hoàn toàn miễn phí (Hãy ghi nhớ ID và Password cẩn thận).
2. Trở lại Máy tính, Mở Terminal (Cửa sổ dòng lệnh của IDE), nhập lệnh kết nối:
   ```bash
   gh auth login
   ```
3. Màn hình console hiện ra 1 dãy các lựa chọn. Bạn lấy **Mũi tên Lên/Xuống trên bàn phím** -> Chọn dòng chữ **GitHub.com** -> Bấm phím **Enter**.
4. Chọn giao thức mạng: Chọn **HTTPS** -> **Enter**.
5. Hệ thống hỏi xác thực bằng thông tin đăng nhập: `Authenticate Git with your GitHub credentials?` -> Gõ phím **Y** -> **Enter**.
6. Chọn chức năng **Login with a web browser** (Mở bằng trình duyệt). Màn hình Terminal sẽ sinh ra 1 dãy mật mã (VD: `ABCD-1234`). Mở bằng phím Enter thì Trình duyệt Web của bạn sẽ tự bật lên, hãy điền mã xác thực vào trang web Github.
7. Khi trình duyệt báo **Successful**, nghĩa là bạn đã kết nối não bộ Github vào máy tính thành công!

## Bước 3: Đăng ký Trạm Phát Sóng VERCEL
1. Bạn đăng nhập vào cổng cung cấp dịch vụ Hosting miễn phí tại: [Vercel.com/signup](https://vercel.com/signup).
2. Tại màn hình đăng ký, hãy lựa chọn phương thức **"Continue with GitHub"** (CỰC KỲ QUAN TRỌNG ĐỂ CẢ HỆ THỐNG ĐỒNG BỘ NHAU).
3. Cho phép Vercel liên kết với tài khoản Github mà bạn vừa tạo. 

---
*(Trình cài đặt kết cấu đã xong! Bây giờ hãy quay lại file `README.md` để bắt đầu luyện tập luồng biến thư mục thành Website với AI Agent).*
