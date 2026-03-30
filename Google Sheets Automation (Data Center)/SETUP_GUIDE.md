# ⚙️ Hướng Dẫn Kích Hoạt Google Workspace (Setup Guide)

Để trợ lý AI có thể kết nối với kho tài liệu Google Drive của phòng ban một cách bảo mật nhất, bạn cần thực hiện cấp quyền truy cập (OAuth) từ hệ thống máy chủ Google và cài đặt công cụ GWS CLI. 
*Lưu ý: Quá trình thiết lập hạ tầng này chỉ cần làm **một lần duy nhất** trên máy tính.*

---

## Bước 1: Khởi Tạo Dự Án Trên Google Cloud (GCP)
1. Truy cập vào cổng quản trị [Google Cloud Console](https://console.cloud.google.com/) bằng tài khoản Gmail cá nhân/công ty.
2. Đồng ý các điều khoản (nếu có). Trên thanh Menu trên cùng (cạnh logo Google Cloud), bấm vào **Select a project** -> Ở cửa sổ hiện ra, bấm **New Project**.
3. Khai báo Tên Dự án (Ví dụ: `Antigravity Automation 2026`) -> Nhấn **CREATE**.
4. Chờ hệ thống khởi tạo trong vài giây, nhấn vào biểu tượng Quả Chuông (Thông báo) -> Chọn **Select Project** để đi vào giao diện dự án vừa tạo.

## Bước 2: Kích Hoạt Dịch Vụ Google Drive API
1. Trong thanh Tìm kiếm (Search) trên cùng, gõ từ khóa: `Google Drive API` và Enter.
2. Bạn sẽ thấy thẻ kết quả **Google Drive API**, bấm vào đó -> Nhấn nút màu xanh **ENABLE** để kích hoạt đường hẻm liên kết với Đám mây.

## Bước 3: Đăng Ký Màn Hình Xét Duyệt (OAuth Consent Screen)
1. Tại thanh Menu bên trái, tìm cụm **APIs & Services** -> Chọn **OAuth consent screen**.
2. Ở phần User Type, hãy chọn **External** (Cho phép tài khoản bên ngoài truy cập) -> Nhấn **CREATE**.
3. **App information**: Điền Tên Ứng dụng (Vd: `Antigravity BOT`) và Email hỗ trợ của bạn.
4. Cuộn xuống cuối trang, tại ô **Developer contact information**: Nhập lại Email của bạn một lần nữa -> Nhấn **SAVE AND CONTINUE**.
5. Bước Scopes: Bỏ qua và nhấn **SAVE AND CONTINUE**.
6. Tại bước **Test Users**: Nhấn **ADD USERS** -> Gõ địa chỉ Gmail thực tế của bạn vào đó (Giới hạn tài khoản được cấp quyền test). Nhấn **SAVE AND CONTINUE** để hoàn tất.

## Bước 4: Khởi Tạo Khóa Bí Mật (Credentials)
1. Nhìn Menu Trái, chuyển sang mục **Credentials**.
2. Bấm nút **+ CREATE CREDENTIALS** ở trên cùng -> Chọn **OAuth client ID**.
3. Khung **Application type**: Bắt buộc chọn hệ sinh thái **Desktop app**. Đặt tên dễ nhớ (Vd: `Toan Quyen Windows`) -> Bấm **CREATE**.
4. Hệ thống sẽ sinh ra một bảng chứa `Client ID` và `Client Secret`. Hãy Copy (sao chép) hoặc tải file JSON chứa hai đoạn thông số quan trọng này.

## Bước 5: Cài Đặt Lõi GWS CLI Cục Bộ
1. Quay trở lại Máy tính của bạn, mở cửa sổ Terminal (dòng lệnh dòng lệnh đen).
2. Gõ lệnh cài đặt GWS tự động qua cấu trúc NPM và nhấn Enter:
   ```bash
   npm install -g @googleworkspace/cli
   ```
3. Đợi vài giây để hệ thống cấu hình lõi GWS bám rễ vào thiết bị.

## Bước 6: Khởi Tạo Cổng Xác Thực (Login Bằng GWS)
1. Sau khi cài đặt xong công cụ, gõ câu lệnh mở cổng xác thực:
   ```bash
   gws auth login
   ```
2. (Tùy phiên bản), nếu cửa sổ yêu cầu nhập `Client ID` và `Client Secret`, hãy dán 2 đoạn mã bạn lấy ở Bước 4 vào.
3. Lập tức, Trình duyệt Web của bạn sẽ bật lên trang Đăng nhập Google. Nhấp chọn tài khoản Gmail của bạn.
4. Google cảnh báo ứng dụng yêu cầu truy cập, bấm **Tiếp tục** và **Cho phép (Allow)**.
5. Khi trình duyệt báo thành công, quay về màn hình Terminal bạn sẽ thấy xác nhận. Từ nay hệ thống máy tính của bạn đã được trao quyền đồng bộ an toàn tuyệt đối với Google Drive!

---
*(Trở lại file `README.md` để bắt đầu luyện tập luồng thao tác kéo dữ liệu bằng AI Agent)*
