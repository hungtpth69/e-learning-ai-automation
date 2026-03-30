# ⚙️ Hướng Dẫn Cài Đặt Khóa Zalo OA (Setup Guide)

Để hệ thống đủ quyền gửi tin dưới tư cách Doanh nghiệp, chúng ta cần tiến hành cấp phép theo 3 bước bảo mật tiêu chuẩn của Zalo. 
*Lưu ý quan trọng: Doanh nghiệp của bạn bắt buộc phải đang sở hữu một trang Zalo Official Account (Zalo OA).*

---

## Bước 1: Khởi tạo Ứng Dụng Liên Kết
1. Truy cập trang dành cho nhà phát triển của Zalo: [Zalo For Developers (developers.zalo.me)](https://developers.zalo.me/).
2. Đăng nhập bằng tài khoản Zalo cá nhân có quyền Quản trị viên (Admin) của trang Zalo OA. Hãy nhìn lên góc trên bên phải màn hình, bấm vào Tên tài khoản của bạn -> Chọn **Ứng Dụng Của Tôi**.
3. Bấm vào nút **Tạo Ứng Dụng (Thêm ứng dụng mới)**. 
4. Điền tên ứng dụng của bạn để dễ phân biệt (VD: `He Thong Thong Bao Noi Bo`). Danh mục chọn `Dịch Vụ` rồi bấm **Tạo ID Ứng Dụng**.
5. Sau khi tạo xong, hệ thống sẽ chuyển đến Bảng Cấu Hình. Tại Menu bên trái màn hình, nhấp chọn mục **Cấp Quyền Ứng Dụng**.
6. Tại danh sách quyền, hãy tích chọn 2 ô quan trọng nhất: **"Gửi tin nhắn OA"** và **"Lấy danh sách người quan tâm OA"**.

## Bước 2: Liên Kết Ứng Dụng Với Trang Zalo OA
Bộ máy kết nối đã có, bây giờ bạn cần ghép nối nó vào Fanpage Zalo của công ty.
1. Tiếp tục ở Menu bên trái, chọn **Quản Lý Tài Khoản** -> **Zalo Official Account**.
2. Nhấn vào nút xanh có chữ **Liên kết Zalo OA**.
3. Một hộp thoại chứa danh sách các Zalo OA mà bạn quản lý sẽ hiện ra. Bấm chọn trang Zalo của công ty bạn rồi xác nhận để hoàn tất đồng bộ hóa.

## Bước 3: Lấy Mã Cấp Phép (Access Token)
Mã Access Token đóng vai trò như "chìa khóa" để cho phép Agent của bạn truyền lệnh gửi đi một cách tự động.
1. Tại khu vực Menu bên trái, chọn mục **Công Cụ > API Explorer** (Biểu tượng cờ-lê).
2. Thiết lập 3 trường thông tin ở phần trên màn hình như sau:
   - **Ứng Dụng**: Mở danh sách và chọn Tên Ứng dụng bạn vừa tạo ở Bước 1.
   - **Loại Token**: Bắt buộc chọn **"OA Access Token"**.
   - **Official Account**: Chọn trang Zalo OA của công ty bạn.
3. Bấm nút **Lấy Access Token**. Hệ thống có thể gửi một thông báo xác nhận về ứng dụng Zalo trên điện thoại của bạn, hãy bấm Chấp nhận.
4. Ở khu vực bảng kết quả phía dưới, hệ thống sẽ sinh ra một chuỗi ký tự rất dài. **Đây chính là Mã Access Token.** (Lưu ý: Mã này có hiệu lực trong vòng 25 tiếng theo cơ chế bảo mật của Zalo). Hãy bấm nút Copy (Sao chép) toàn bộ đoạn mã này!

---

## Bước 4: Khai Báo Vào Hệ Thống Local
Hệ thống sử dụng file cục bộ để giữ tính an toàn.
1. Mở file `zalo_token.txt` trong thư mục `Zalo` bằng phần mềm Notepad. 
2. Dán toàn bộ chuỗi mã Access Token vừa copy ở Bước 3 vào đây và bấm Save. (Chỉ dán chuỗi bảo mật).
3. Đọc tiếp `README.md` để khởi chạy Demo.
