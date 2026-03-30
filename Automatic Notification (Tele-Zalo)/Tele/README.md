# 📱 Hướng Dẫn Kích Hoạt (Demo Usecase): Telegram Bot Notification

> **Tình Huống Sử Dụng (Usecase): Gửi Thông Báo Kèm Tên Tự Động**
> Sau khi đã cài đặt thành công Bot (Xem `SETUP_GUIDE.md`), bạn có thể biến Bot thành một "Thư ký Truyền thông" để phát đi thông báo Lịch họp, Nhắc nhở chấm công, hoặc Cập nhật Chính sách đến từng cá nhân.
> Ưu điểm của Telegram Bot là tính tức thời, hoàn toàn miễn phí và không bao giờ trôi tin nhắn.

---

## 🎯 Luồng Hoạt Động (Cơ Chế Khởi Động)

> **⚠️ QUY TẮC BẮT BUỘC CỦA TELEGRAM:**
> Telegram cấm triệt để việc Bot chủ động nhắn tin (Spam) người lạ. 
> Do đó, Khách hàng hoặc Nhân viên **BẮT BUỘC** phải chủ động ấn "START" (Bắt đầu) với Bot của công ty ít nhất 1 lần để hệ thống có thể kết nối. 
> *Ví dụ: Gửi link Bot (VD: `@ThongBao_AG_bot`) vào nhóm chat Zalo chung của công ty và yêu cầu mọi người truy cập.*

Bộ Agent sẽ tự động hóa qua 2 Giai đoạn chính:
- **Giai đoạn 1 (Lấy Dữ Liệu Tự Động):** Thuật toán tự kích hoạt (API `getUpdates`) để thu thập Danh sách Mã Định Danh (`Chat ID`) của toàn bộ những nhân viên đã từng ấn nút "START". Bạn không cần dò dẫm tìm thủ công.
- **Giai đoạn 2 (Xử Lý Thông Báo):** Thay vì gửi đồng loạt như nhóm Chat thông thường, AI Agent sẽ "Map" (Gắn khớp) ID vừa thu thập được với Tên thật của nhân viên đó. AI sẽ tự động đóng vai người gửi, chào bằng đích danh Tên để tăng sự thân thiện. (Chế độ chống Spam: Delay 1s cho mỗi tin nhắn gửi đi).

---

## 🛠 Chuẩn Bị File Dữ Liệu (Data Mồi)
Hệ thống AI chỉ cần bạn chuẩn bị một "danh sách" cực kỳ cơ bản.
1. Hãy tìm và mở file danh sách Excel đang có trong thư mục: `tele_contact_list.csv`
2. **Cập nhật danh bạ**: Thêm các nhân viên/khách hàng vào với cú pháp đơn giản. Cột username (nếu có) hoặc thông tin cần cá nhân hóa. AI sẽ tự động Map thông tin từ Cột Tên vào nội dung tin nhắn.
3. Nội dung tin cần gửi hãy để gọn gàng trong file chữ (`message_template.txt`).

---

## 🚀 Kích Hoạt Luồng Bắn Tin (Tự Động)
Một khi danh sách đã được thiết lập, hãy để Agent làm việc thay bạn:
Tại màn hình dòng lệnh của Công cụ Antigravity (Terminal), hãy gõ phím tắt kích hoạt:
```bash
/sendmestele
```

**Kết quả:**
Nhấp Enter và chiêm ngưỡng hệ thống xử lý. Trí tuệ ảo sẽ mở cổng API, chèn dữ liệu cá nhân hóa (Tên người dùng) vào template rồi gửi chớp nhoáng thẳng qua mạng di động mà bạn không cần phải nhấc một ngón tay. File trạng thái (Thành công/Lỗi) sẽ được trả về ngay lặp tức để bạn đối soát!
