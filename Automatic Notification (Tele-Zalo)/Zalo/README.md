# 💬 Zalo OA (Zalo Official Doanh Nghiệp) API System

> **Hệ Thống Rải Tin ZNS Siêu Tốc Doanh Nghiệp Cấp Độ Enterprise**
> Vứt qua tính cồng kềnh chậm chạp của Tool Click chuột (Do hay treo máy chậm). Agent này mang giao thức API HTTPs thẳng từ Máy Chủ về nhà để Bắn Tin nhắn Zalo cực mạnh qua hạ tầng của Doanh nghiệp.

## 🎯 Mục Đích Hoạt Động
Với Khách hàng, họ nhận tin qua Zalo từ "Kênh Fanpage Zalo", ta gọi Zalo OA. Tool tự động này (`zalo_oa_workflow.py`) sẽ đọc File CSV, nắn nội dung rồi Bắn hàm trực tiếp qua tổng đài Zalo. Thao tác mất dưới 0.2 giây một người, tỷ lệ khách mở tin nhắn trên Điện Thoại là 100%. Không bao giờ lo khóa nick cá nhân.

## 🛠 Hướng Dẫn Setup Cổng Zalo Cho Dân Non-tech (Step-by-Step)

Quy trình Zalo API khá bảo mật vì nó liên quan đến Uy tín công ty, hãy làm từng bước thật chậm rãi theo hướng dẫn sau.
*(Chú ý 1: Công ty bạn BẮT BUỘC Đã SỞ HỮU sẵn tài khoản Page Zalo OA).*

### Bước 1: Khởi Tạo Trạm Ứng Dụng Liên Kết Tại "Developers Zalo"
1. Mở trình duyệt Web truy cập Zalo Cấp Độ Nâng Cao: [Zalo For Developers (developers.zalo.me)](https://developers.zalo.me/).
2. Đăng nhập nick Zalo cá nhân của bạn vô đó (Quản lý Admin). Ngó hướng góc phải màn hình bên trên, Bấm vào cụm Tên tài khoản -> Chọn **Ứng Dụng Của Tôi**.
3. Bấm vào nút khoang Tím To Đùng: **Tạo Ứng Dụng (Hoặc Thêm Ứng dụng mới)**. 
4. App nó hỏi vài dòng thủ tục. Ở ô Tên Ứng Dụng, Điền đại một cái gì đó chuyên nghiệp, VD: (`Phan Mem Cham Soc Auto 2026`). Danh Mục chọn `Dịch Vụ`. Bấm **TẠO ID ỨNG DỤNG**. 
5. Sau khi tạo xong, nó sẽ chuyển trang vào "Bảng Cấu Hình Ứng Dụng" của riêng tool đó. Tại Menu Bên Trái (Panel), chọn dòng thần tích: **Cấp Quyền Ứng Dụng**.
6. Mục này chứa Đạo Quyền. Kéo xuống cái danh sách ô vuông cấp quyền, chọn và tick Xanh cho 2 thẻ sau: **"Gửi tin nhắn OA"** và **"Lấy danh sách người quan tâm OA"**.

### Bước 2: Ghép Mảnh Ứng Dụng Với Kênh Zalo OA Thực Tế
Bot đã có, Quyền đã có. Khuyết một thứ, đó là Bắt Cặp nó vô đúng cái Tên Zalo Công ty.
1. Nhìn bảng Panel Menu Trái lần nữa, Click sổ ra mục **Quản Lý Tài Khoản** -> Chọn **Zalo Official Account**.
2. Phía giữa màn hình xuất hiện một Giao Diện Động, Bảng Trắng Trắng. Một ô nút bấm ghi chữ: **Liên kết Zalo OA** màu Xanh. Nhấn Thẳng Nhé.
3. Nó đẻ ra danh sách những cục Zalo Cty mà bạn đang làm Sếp (Admin). Bấm chọn vô OA muốn phát triển, Rồi Submit -> Vĩnh cữu đồng bộ.

### Bước 3: Rút Chìa Khóa Lõi (Access Token)
Mọi cánh cửa mở hết. Bước này ta xin "Kim Bài Miễn Tử" để đi qua biên giới Zalo. Chiếc thẻ tên `Access Token`.
1. Nhìn Panel Trái 1 lần chót, kéo nhẹ xuống, click dòng **Công Cụ > API Explorer** (Hình cờ-lê ốc vít).
2. Góc trên màn hình chia làm 3 cột rõ rệt. Chỉnh theo mốc chuẩn như sau:
   - **Ứng Dụng**: Click mũi tên thả, chọn đúng Tên Ứng dụng vừa Đẻ ra (VD: `Phan Mem Cham Soc...`).
   - **Loại Token**: Bắt buộc tuân lệnh chọn **"OA Access Token"** (Nhạy cảm 100%).
   - **Official Account**: Chọn Tên cái Page Zalo công ty của bạn.
3. Bên Cạnh Nó (Hoặc dưới), Bấm ngay Cục Nút **"LẤY ACCESS TOKEN"**. Trình duyệt có thể bắt bạn phải Mở điện thoại Click uỷ quyền thêm 1 nhịp - Chấp nhận ngay.
4. Điều Kỳ Diệu Xảy ra tại bảng Result Trắng chữ to. Dãy chữ dài màu đen đậm (dài miên man kéo mệt lử) xuất hiện. **NÓ CHÍNH LÀ ACCESS TOKEN.** Nó chính là Năng Lượng cấp cho Code Python. Mã này tồn tại 25 Tiếng đồng hồ. Nhấn Copy toàn khối dài ngoằng đó!

## ⚙️ Cấu Hình Của Script
Hệ thống nay đã dùng file lưu trữ bảo mật cục bộ (File `.txt`) để tránh rủi ro bảo mật lộ mã OA dán trực tiếp trong code.
1. Mở file có tên `zalo_token.txt` trong thư mục giải nén bằng Notepad.
2. Dán ngay cái bắp chuối Access Token Dài Ngoằng lúc nãy vào toàn bộ file đó (Chỉ cần 1 dòng duy nhất, không cần dấu ngoặc kép hay gì khác). Mở ra lưu lại.
3. Mở cửa Data File Mồi: `zalo_contact_list.csv`. 
   Vào Cột ID Khách hàng sửa. **Vô Cũng Đặc Biệt Chú Ý:** Tại Hệ Sinh Thái Zalo ZNS, Người ta KHÔNG LẤY Số Điện Thoại đi làm ID (Do sợ bảo mật lộ info), mà Mã để gọi Tín Hiệu Là Các Chuỗi Mã Căn Cước Rác, Nó giống như `"351838192837"` ấy!!

*(Về phần yêu cầu kĩ thuật, hệ thống gọi cổng API chuẩn quốc tế nên yêu cầu bạn chạy lệnh: `pip install requests` nếu máy chưa có)*

## 🚀 Hướng Dẫn Kích Nổ Ánh Sáng API
Khi tất cả khớp với Form mẫu, Bạn văng đạn lên màn Command đen bằng lệnh cực Ngắn:
```
/sendmeszalo
```

BÙNG CƯỚC!! Robot gõ máy trong bóng đêm xả liên thanh hàng loạt Code 200 (Success). Lệnh HTTP POST đâm mạnh vào mạng cục bộ, trễ chỉ `0.2 Giây` xong một Người thay vì tốn `6 Giá` để đợi Giao diện Web Load Load như công cụ lỏm. Chúc mừng!! Chiếc điện thoại người nhận sẽ lập tức hiện Thông Báo đỏ của Page Doanh nghiệp Zalo.
