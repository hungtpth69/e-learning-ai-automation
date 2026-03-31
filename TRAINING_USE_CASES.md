# 📚 TÀI LIỆU TỔNG QUAN: CÁC TÌNH HUỐNG THỰC HÀNH LỚP HỌC ANTIGRAVITY

Tài liệu này mô tả lộ trình và các kịch bản (Use Case) chính sẽ được giảng dạy trong lớp học thực hành AI Tự động hóa. Mỗi công cụ sẽ bao gồm 4 phần tiêu chuẩn: Lợi ích khi đấu nối Antigravity, Hướng dẫn cài đặt, Tình huống giả lập (với Data Mockup) và Bài tập về nhà.

---

## 🟢 MODULE 1: ZALO TÀI KHOẢN CÁ NHÂN (ZALO USERBOT)
**Chủ đề:** Đọc và Phân loại Tin nhắn tự động

### 1. Lợi ích tính năng
Khi đấu nối Zalo cá nhân với Antigravity, AI có thể hoạt động như một thư ký ảo: Tự động mở Zalo, quét các đoạn hội thoại quan trọng, tóm tắt và phân loại tin nhắn. Điều này giúp người dùng không bỏ lỡ các thông tin quan trọng từ sếp, đối tác VIP hoặc các nhóm làm việc nhiều tin nhắn, tiết kiệm hàng giờ đồng hồ lướt điện thoại mỗi ngày.

### 2. Hướng dẫn cài đặt & Sử dụng
- Yêu cầu cài đặt thư viện điều khiển trình duyệt (ví dụ: Playwright hoặc Selenium).
- Hướng dẫn học viên đăng nhập Zalo Web và lưu giữ session.
- Thiết lập kịch bản Python để tự động hóa thao tác click và trích xuất HTML.

### 3. Tình huống giả lập (Use Cases)
*Giảng viên demo 2 tính năng chính:*
1. **Đọc theo đối tượng chỉ định:** Quét và lấy hội thoại từ các Nhóm (Group) hoặc Tài khoản cá nhân cụ thể đã được hardcode trong danh sách.
2. **Đọc tin nhắn chưa đọc (Unread):** Quét các tin nhắn chưa được đọc trong một giới hạn thời gian (ví dụ: trong vòng 1 đến 2 ngày gần đây).
* **Data Mockup cần chuẩn bị:** 
  - File danh sách mục tiêu (tên người/nhóm).
  - Khung câu lệnh (Prompt) chuẩn để yêu cầu AI đọc.
  - **Lưu ý Demo:** Trước giờ học, phải cố ý dùng một máy khác gửi một tin nhắn đến tài khoản nhận và *để nguyên trạng thái Chưa Đọc (Unread)* để kịch bản code có thể chạy và bắt được tin nhắn đó một cách thực tế nhất.

### 4. Bài tập về nhà
- Yêu cầu học viên cấu hình Zalo của cá nhân họ, viết kịch bản trích xuất 5 tin nhắn chưa đọc gần nhất và nhờ AI tóm tắt thành 1 file báo cáo `.txt`.

---

## 📧 MODULE 2: EMAIL TỰ ĐỘNG (GMAIL SMTP)
**Chủ đề:** Gửi thư Thông báo Phỏng vấn hàng loạt

### 1. Lợi ích tính năng
Thay vì phải cc/bcc hay gửi từng email thủ công, Antigravity giúp phòng Nhân sự (HR) hoặc Sale gửi hàng trăm email được cá nhân hóa cao độ (Tên, vị trí, giờ phỏng vấn riêng biệt cho từng người) chỉ bằng 1 câu lệnh. AI có thể đóng vai trò tự động soạn nội dung và tự động gửi thông qua SMTP.

### 2. Hướng dẫn cài đặt & Sử dụng
- Cài đặt App Password (Mật khẩu ứng dụng) trên tài khoản Google.
- Cấu hình file script gửi Email bằng thư viện `smtplib` hoặc API tương đương.

### 3. Tình huống giả lập (Use Cases)
Tự động gửi Thư mời Phỏng vấn (Interview Invitation) cho một danh sách ứng viên (nằm trong file Excel/CSV).
* **Data Mockup cần chuẩn bị:**
  - File CSV chứa danh sách ứng viên (Tên, Email, Vị trí ứng tuyển, Thời gian).
  - Phải chuẩn bị sẵn **2 Phiên bản Nội dung Email**:
    1. **Bản HTML Template:** Một giao diện email xịn xò, có đổ màu, chèn logo, định dạng bảng biểu đẹp mắt (HTML Format).
    2. **Bản Thuần Text (Plain Text):** Một phiên bản dự phòng, trình bày text rõ ràng, chuyên nghiệp, xuống dòng hợp lý.

### 4. Bài tập về nhà
- Học viên tự tạo một danh sách 3 người bạn, viết một Template Email HTML thông báo "Trúng thưởng" và lập trình tự động gửi thành công vào hòm thư của 3 người đó.

---

## 🌐 MODULE 3: VERCEL DEPLOY
**Chủ đề:** Xây dựng Website Nội bộ / Cổng thông tin (Web Portal)

### 1. Lợi ích tính năng
Chuyển hóa toàn bộ dữ liệu thô, vô hình (File Text, file Word, Markdown) của doanh nghiệp trở thành một Cổng Thông Tin Web hoàn chỉnh. Khi kết hợp với Antigravity, chỉ bằng một dòng lệnh, kho dữ liệu cá nhân sẽ tự động "biến hình" thành 1 website trên mạng (Vercel) để mọi người có thể truy cập, tra cứu thông tin nội bộ mọi lúc mọi nơi.

### 2. Hướng dẫn cài đặt & Sử dụng
- Hướng dẫn cài đặt Github CLI (`gh`) và cấp quyền đăng nhập.
- Hiểu về Git cơ bản và tạo tài khoản Vercel.com.

### 3. Tình huống giả lập (Use Cases)
Thu thập các tài liệu sẵn có (Quy định công ty, danh bạ nhân sự) để auto-generate ra một trang `index.html` và deploy lên mạng.
* **Data Mockup cần chuẩn bị:**
  - File dữ liệu JSON tĩnh chứa thông tin.
  - **Giao diện (UI):** Mã nguồn `index.html` phải được thiết kế **cực kỳ đẹp mắt**. Áp dụng thiết kế Dark Mode, Glassmorphism, tích hợp tính năng Tìm kiếm/Lọc trực tiếp bằng Javascript để mang lại trải nghiệm WOW cho người xem trong buổi học. (Giao diện phải được tối ưu sẵn trước).

### 4. Bài tập về nhà
- Học viên tự thiết kế một trang **Tuyển dụng (Job Description)** đơn giản bằng HTML/Tailwind, có chức năng hiển thị vị trí tuyển dụng từ Data JSON và tự động Deploy lên tài khoản Vercel cá nhân để lấy link báo cáo cho giảng viên. (Đã soạn sẵn bài tập chi tiết tại file `EXERCISE_RECRUITMENT.md`).

---
*(Tài liệu này được biên soạn bám sát theo các ghi âm yêu cầu hệ thống và định hướng giảng dạy thực chiến của dự án).*
