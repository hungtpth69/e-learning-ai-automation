# 🎓 03. TÌNH HUỐNG GIẢ LẬP & BÀI TẬP (DEMO & EXERCISES)

## 📌 Tình Huống Giả Lập Tại Giờ Học
Giảng viên sẽ tiến hành Demo 2 kịch bản tính năng chính, sử dụng File Danh sách (Data Mockup) được chuẩn bị sẵn:

1. **Đọc theo đối tượng chỉ định:**
   - Đọc, quét, lấy hội thoại từ các Nhóm (Group) hoặc Trò chuyện Cá Nhân cụ thể đã được khai báo hardcode trong file danh sách.
2. **Đọc tin nhắn chưa đọc (Unread):**
   - Quét thu thập các tin nhắn chưa được đọc trong một giới hạn thời gian (Ví dụ 1-2 ngày gần đây).
   - **Lưu ý Demo thực tế:** Giảng viên cần sử dụng tài khoản/máy khác gửi một tin nhắn đến tài khoản nhận và *cố tình để nguyên trạng thái Chưa Đọc (Unread)* trước khi script chạy. Điều này chứng minh cho học viên độ nhạy bắt tin nhắn của hệ thống Playwright.

## 📋 Data Mockup Cần Chuẩn Bị
- Hệ thống hỗ trợ lấy data từ file Excel/CSV (như `send_list.csv` / `read_list.csv`).
- Định dạng File cho phép chèn ký tự xuống dòng bằng cách bao trọn chuỗi text trong cặp ngoặc kép `""`.
  *Ví dụ template gửi tin file csv:*
  ```csv
  Phone Number,Name,Message Template
  0912345678,Khải Hoàng,"Chào {name},
  Đây là dòng 2 của tin nhắn tự động từ DOM.
  Chúc ngày tốt lành!"
  ```

## 📝 Bài Tập Về Nhà (Homework)
Học viên được giao nhiệm vụ:
1. **Cấu hình thành công** Profile Playwright Chromium trên máy tính cá nhân.
2. Tự vượt qua phần quét QR Code và **Đồng bộ tin nhắn lịch sử (Sync Data)**.
3. **Viết kịch bản khởi chạy:** Chỉnh sửa file `zalo_read_workflow.py` để trích xuất 5 tin nhắn MỚI NHẤT chưa đọc và kết nối nhờ AI Agent tóm tắt thành 1 file báo cáo `.txt`.
