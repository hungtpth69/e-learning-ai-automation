# 📱 Thông Báo Tự Động (Zalo/Telegram Notification Bot)

> **Hệ Thống Gửi Tin Nhắn Tự Động Cho Hệ Sinh Thái OTT (Over-The-Top)**
> Dành cho người vận hành (Non-tech). Ứng dụng AI Agent để tự động hóa việc rải tin nhắn thông báo (Push Notification) đến hàng ngàn Nhân sự hoặc Khách hàng trực tiếp vào điện thoại (Telegram/Zalo) cực kỳ cá nhân hóa.

---

## 🎯 Bối Cảnh Thực Tiễn (Dành cho Khối Back-Office)
**Tình huống thường nhật:**
Đến cuối tháng, Bộ phận Hành chính/Nhân sự (HR) cần gửi thông báo *Lương, Thưởng Tết, Lịch khám sức khỏe* cho 500 Cán bộ Nhân viên. Việc copy-paste cùng một đoạn văn bản (nhưng phải đổi Tên và Số tiền cho từng người) trên Zalo hoặc Telegram là một cơn ác mộng cực kỳ tốn thời gian và dễ gửi nhầm người.

**👉 Giải pháp AI Agent:**
Hãy để Agent trở thành "Cô văn thư" mẫn cán của bạn. Bạn chỉ cần đưa một file bảng lương (Excel/CSV) và một khuôn mẫu tin nhắn. AI sẽ tự động đọc bảng dữ liệu, lắp ráp nội dung chuẩn xác cho từng người và tự động ấn nút "Gửi" tới đích danh Zalo/Telegram của hàng trăm nhân viên chỉ trong nháy mắt.

---

## 🛠 Hướng Dẫn Chuẩn Bị (3 "Lớp" Cốt Lõi)

Khác với gửi Email, nhắn tin trên các nền tảng Chat (Tele/Zalo) yêu cầu tính "tức thời" và "ngắn gọn".

### 1. Lớp Dữ Liệu (File Danh bạ Excel/CSV)
- Luôn phải có tên, bộ phận chuyên trách và **Số điện thoại** (đối với Zalo) hoặc **Chat ID / Username** (đối với Telegram).
- Với nội bộ, bạn có thể thiết lập thêm các cột như Lương, Xếp loại KPI để Agent bốc tách dữ liệu gửi đi cho đa dạng.

### 2. Lớp Nội Dung (Mẫu Tin Nhắn)
- Chỉ nên dùng **Text File (.txt)** thuần túy để nạp đạn cho tin nhắn. Zalo và Telegram không thể gửi giao diện HTML đè nặng nề.
- Có thể hướng dẫn Agent chèn các Emoji (🚀, 📄, ⚠️) vào nội dung Text để tin nhắn trở nên thân thiện và bớt nhàm chán cho môi trường nội bộ.

### 3. Lớp Kênh Gửi (Chọn Trạm Phát Sóng)
Tùy vào nhu cầu bảo mật và quy định của công ty, bạn có 3 lựa chọn trạm phát:
- **Telegram Bot API:** Mức độ bảo mật cao, tốc độ bá đạo. Không bao giờ sợ rớt mạng. Rất phù hợp nếu Công ty sử dụng Telegram làm công cụ làm việc chính.
- **Telegram User Bot:** Biến thẳng tài khoản Telegram cá nhân (số điện thoại) của bạn thành Bot đi rải tin. (Cấm lạm dụng Spam).
- **Zalo Doanh Nghiệp (Zalo OA):** Chuyên nghiệp số 1 tại Việt Nam. Sử dụng hệ thống API chính thống qua mạng lưới Zalo để nhận diện số điện thoại và báo cáo độ chuyển đổi.

---

## ⚙️ Cấu Hình Khởi Chạy
*Việc chèn mã khóa (Token/API) rất nhạy cảm. Bạn hãy điền chúng vào file Cấu hình nằm ẩn sâu phía bên trong các thư mục Zalo/Tele thay vì để lộ thẳng ra ngoài.*

Tuỳ thuộc vào lựa chọn của công ty, hãy di chuyển vào 1 trong 3 thư mục con: `Tele`, `Tele (UserBot)` hoặc `Zalo` để khai báo:
1. Mở file thư mục của mạng xã hội bạn muốn nhắn.
2. Nhập các ID/Token do Telegram BotFather hoặc Zalo OA cung cấp vào các file `.env` hoặc `config.txt`.
3. Chuẩn bị file `contacts.csv` có đầy đủ thông tin nhân sự muốn thông báo.

---

## 🚀 Kích Hoạt Phần Mềm Bằng AI Agent
Bạn không cần học lệnh lập trình phức tạp. Khi mọi thứ đã sẵn sàng, hãy nhờ trợ lý ảo kích hoạt luồng tự động:

1. Để phát động **Hệ thống gửi tin nhắn Telegram hàng loạt:**
```bash
/sendmestele
```

2. Để phát động **Hệ thống gửi thông báo Zalo Official Account:**
```bash
/sendmeszalo
```

## 📊 Kết Quả Đầu Ra
Ngay sau khi Agent hoàn tất chiến dịch, toàn bộ trạng thái "Đã gửi / Thất bại" của từng nhân viên sẽ được ghi chú lại rành mạch trong một báo cáo CSV mới. Bạn chỉ việc mở lên và kiểm tra xem ai chưa nhận được thông báo quan trọng cuối năm!
