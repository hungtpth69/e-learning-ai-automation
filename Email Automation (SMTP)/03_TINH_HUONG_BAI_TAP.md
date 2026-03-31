# 🎓 03. TÌNH HUỐNG GIẢ LẬP & BÀI TẬP (DEMO & EXERCISES)

## 🎯 Tình Huống Giả Lập Mẫu (Data Mockup)
Hệ thống dự kiến tự động gửi **Thư mời Nhận việc (Offer Letter)** cho danh sách trúng tuyển.

### 1. Chuẩn Bị Lớp Data Cột (`email_contact_list.csv`)
Nằm trong Folder chương trình, file CSV gốc bao gồm:
- **Tên Ứng Viên**: Tự động ghép nội dung lời chào (`Dear {name}`).
- **Mức Lương**: Cột chuyên dụng lấy số ghép vào Template.
- **Email**: Hòm thư người nhận thực tế.
- **Vị trí Ứng tuyển**: (Ví dụ Sale Manager).

### 2. Chuẩn Bị Khung Giao Diện (`email_template.html`)
Mở file `email_template.html`. Đây không phải file script mail text thông thường. Nếu bạn biết một chút HTML, bạn có thể thay đổi màu logo công ty hoặc font chữ của mình vào đây. Nếu không, chỉ cần sửa đoạn văn tiếng việt bình thường bên trong (các từ khóa dạng `{name}` thì phải giữ nguyên để Tool map data).

### 3. Kiểm Soát Log Output
Sau khi chạy tool xong, tiến hành mở file `email_sent_log.csv` nằm trong Folder để xem lịch sử gửi có ai bị sót hay rớt do sai Email không. Hệ thống in dấu Timestamp chính xác.

---

## 📝 Bài Tập Thực Hành (Homework)
Học viên được giao nhiệm vụ tự lập một vòng khép kín:
1. Bạn hãy tự tạo 1 file Excel thu nhỏ lưu 3 cái tên bạn bè hoặc 3 Email clone (khác nhau) của mình. Cài đặt App Password.
2. Thiết kế lại file `email_template` để sửa cái Offer Lương thành thông báo **"Trúng Thưởng Minigame"**. (Cấu trúc có Tên và Món quà trúng giải).
3. Viết script hoặc triệu hồi thủ công Agent tự động gửi chính xác template phần thưởng vào hòm thư 3 đồng nghiệp đó. 
4. Sinh thành công 1 file đính kèm dạng hình ảnh hoặc file PDF cho bài thưởng. Chạy được lệnh Send và chụp lại màn hình Report Success.
