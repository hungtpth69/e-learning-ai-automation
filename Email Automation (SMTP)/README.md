# 📧 Hướng Dẫn Thực Hành (Demo Usecase): Kênh Gửi Email Bằng AI Agent

> **Tình Huống Sử Dụng (Usecase): Gửi Thông Báo Kết Quả Phỏng Vấn (Offer Letter)**
> Dành cho bộ phận Tuyển dụng (HR). 
> Thay vì lụi cụi mở từng Email, gõ Tên Ứng viên, copy mức Lương đề xuất và tự tay bấm "Attach" từng cái File PDF riêng lẻ, bạn sẽ học cách giao phó việc này cho một "Thư ký ảo AI Agent". Chỉ cần một file Excel chứa toàn bộ data, AI sẽ giúp bạn cá nhân hóa nội dung và nhả 100 email gửi thành công chỉ trong 5 phút.

---

## 🎯 Bối Cảnh Thực Tiễn & Năng Lực Của Agent

**Bài Toán:** Công ty vừa kết thúc đợt phỏng vấn 100 Ứng viên. HR cần trả kết quả ngay trong ngày. File Danh sách Đậu/Rớt và Lương đã chốt nằm trên file Excel.

**🤖 Siêu Năng Lực của Antigravity Agent:**
Luồng Auto này sẽ cung cấp:
*   **Gán Tên và Điểm Xóa Nhòa Lỗi Con Người:** Tự động gọi đúng vị trí, tên, bộ phận từ Excel điền vào Template thư. Không bao giờ gửi nhầm Lương người này sang Email người kia.
*   **Tự Động Đọc Và Quét Tiềm Năng (Parsing):** Thậm chí AI có thể quét Hòm Inbox của bạn, tự gom các thư phản hồi *"Đồng ý nhận việc"* và đưa vào mục Đã chốt hợp đồng.

*(Lưu ý: Trước khi khởi chạy thực hành, cần đảm bảo bạn đã kết nối Cấu hình Mạng Lưới Gửi Email thành công theo hướng dẫn trong bài `SETUP_GUIDE.md`)*

---

## 🛠 Chuẩn Bị File Đầu Vào (Mockup Data)

Để Robot làm việc xuất sắc, hãy chuẩn bị nguyên liệu (Data Mồi) ở 3 lớp cốt lõi nằm trong chính thư mục dự án này:

### 1. Lớp Dữ Liệu (`email_contact_list.csv`)
- Mở file Excel này lên. Đây là cột xương sống của chiến dịch.
- Đảm bảo trong bảng có đủ Tên Ứng Viên, Địa chỉ Email, Vị trí ứng tuyển, Lương đề xuất. AI sẽ tự động hiểu cột nào ứng với chỗ trống nào trong bức thư để "lắp ghép".

### 2. Lớp Nội Dung Cốt (`email_template.html`)
- Gửi Email tuyển dụng cần sự chuyên nghiệp (Chữ in đậm, nghiêng, Logo công ty).
- Hệ thống đã thiết kế sẵn một khuôn mẫu Website (HTML) để Email gửi ra nhìn thật "xịn". Phím giữ nguyên cấu trúc file, chỉ thay đổi Câu chữ (Text) bên trong nếu bạn cần.

### 3. Lớp Test (Duyệt Trước Khi Kích Ráp)
Khuyến cáo người hành nghề: Luôn luôn yêu cầu Phầm mềm *"Hãy cho tôi xem 1 bản nháp điền dữ liệu của Bạn Nguyễn Văn A trước"*. AI sẽ tự xuất ảnh cho bạn đọc lại. Khớp Lương chưa? Đúng Tên chưa? Rồi mới "Khai Hỏa".

---

## 🚀 Kích Hoạt Luồng AI (Tiễn Chiến Dịch Lên Mạng)

Khi file danh bạ CSV của bạn đã hoàn tất, hãy triệu hồi AI Agent bằng một dòng lệnh duy nhất tại cửa sổ lệnh (Terminal):

```bash
/sendmesemail
```

**[Usecase Đính kèm File Nâng Cao]:** 
Trường hợp bạn không chỉ gửi nội dung thư mà còn đính kèm 1 file "Phụ Lục Hợp Đồng Đồng_Nguyễn_Văn_A.pdf" ném riêng vào từng mail, hãy dùng lệnh chuyên sâu:
```bash
/gui-offer-letter
```

### 📊 Xem Thành Quả (Report Ghi Nhận)
Gác tay lên bàn và quan sát màn hình IDE. Một loạt dòng thông báo `[➔] THÀNH CÔNG` sẽ nhấp nháy xanh lá. Khi Agent bảo vệ công việc của mình xong, bạn mở file **`email_sent_log.csv`** được sinh ra mới tinh để đối soát danh sách gửi thành công như một bản báo cáo hoàn hảo nộp Giám Đốc nhân sự!
