# UC1: 📩 Tự Động Hóa Gửi Thư Mời Nhận Việc (Offer Letter)

## 🎯 Bối Cảnh Demo
Bạn là trưởng phòng Tuyển dụng cho một công ty công nghệ lớn. Bạn vừa hoàn thành đợt phỏng vấn cho 10 ứng viên xuất sắc. Nhiệm vụ của bạn là:
- Gửi Thư mời nhận việc (Offer Letter) cá nhân hóa.
- Mỗi thư mời phải ghi đúng tên, vị trí công việc, và mức lương thỏa thuận.
- Mỗi thư phải có file đính kèm là biểu mẫu Hợp đồng thử việc riêng.

## 🚀 Các Bước Thực Hiện
1. **Chuẩn bị dữ liệu:** Mở file `candidates.csv` và kiểm tra 10 ứng viên mẫu.
2. **Cấu hình File:** Dán `GMAIL_APP_PASSWORD` đã lấy từ phần SMTP vào file `email_config.txt`.
3. **Kích hoạt Robot:** Bạn có thể gõ câu lệnh hoặc sử dụng **Prompt** trực tiếp với Agent:

> [!TIP]
> **🤖 Prompt Mẫu Để Kích Hoạt:**
> - *"Đọc danh sách 10 ứng viên trong file candidates.csv và soạn nội dung Offer Letter cá nhân hóa cho từng người, kèm mức lương và vị trí tương ứng."*
> - *"Tiến hành gửi hàng loạt Offer cho các ứng viên này qua Gmail, nhớ đính kèm file Hợp đồng mẫu chuẩn."*

4. **Kiểm tra kết quả:** Robot sẽ tự động quét file Excel, tạo nội dung thư thông minh và gửi đi. Sau khi chạy xong, hãy kiểm tra file `email_sent_log.csv` để thấy lịch sử gửi chi tiết.

## 📊 Dấu Ấn "Siêu Năng Lực"
- **Tốc độ:** Gửi 10 offer letter chuẩn 100% trong vòng dưới 10 giây.
- **Không sai sót:** Tên, vị trí, lương được khớp chính xác, không lo nhầm lẫn giữa các ứng viên.
