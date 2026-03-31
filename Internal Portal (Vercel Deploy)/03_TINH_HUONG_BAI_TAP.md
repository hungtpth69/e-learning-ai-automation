# 🎓 03. TÌNH HUỐNG GIẢ LẬP & BÀI TẬP (DEMO & EXERCISES)

## 📌 Tình Huống Giả Lập Tại Giờ Học
Giảng viên sẽ tiến hành Demo kịch bản: **Thu thập các tài liệu sẵn có (Quy định công ty, danh bạ nhân sự) để Auto-generate ra một trang `index.html` (Portal Nội Bộ) và Deploy lên mạng.**

### Chuẩn Bị File Đầu Vào (Data Mockup)
- File dữ liệu JSON tĩnh chứa thông tin (`data.js`).
- **Giao diện (UI):** Mã nguồn `index.html` đã được thiết kế cực kỳ đẹp mắt. Áp dụng thiết kế Dark Mode, Glassmorphism, tích hợp tính năng Tìm kiếm/Lọc trực tiếp bằng Javascript để mang lại trải nghiệm WOW cho người xem trong buổi học. (Giao diện phải được tối ưu sẵn trước).

---

## 📝 BÀI TẬP THỰC HÀNH: XÂY DỰNG TRANG TUYỂN DỤNG CÔNG TY (RECRUITMENT PORTAL)

> **Mục tiêu:** Áp dụng kiến thức về HTML, Tailwind CSS (giao diện Glassmorphism/Dark Mode) và lưu trữ dữ liệu JSON tĩnh để tạo ra một trang mô tả công việc (Job Description) hiện đại, chuyên nghiệp nhằm thu hút ứng viên cho doanh nghiệp.

### 🎯 Yêu cầu chung
Học viên được đóng vai là một **Chuyên viên Lập trình Hệ thống (System Admin/Developer)** của công ty hiện tại. Phòng Nhân sự (HR) vừa yêu cầu bạn tạo gấp một trang web Tuyển dụng (Landing Page) cho một vị trí công việc mà công ty đang cần gấp (Ví dụ: Trưởng phòng Marketing, Chuyên viên Lập trình...).
Sản phẩm cuối cùng phải là một file `tuyen-dung.html` có thể chạy trực tiếp trên trình duyệt hoặc đưa lên Vercel.

### 🛠 Hướng dẫn triển khai (Các bước thực hiện)

**Bước 1: Chuẩn bị nội dung (Data)**
Tạo file `jobs-data.js` chứa cấu trúc Data tĩnh (JSON) của vị trí tuyển dụng. Nội dung cần bao gồm:
1. Title công việc.
2. Mô tả (Responsibilities).
3. Yêu cầu (Requirements).
4. Quyền lợi (Benefits).
5. Liên hệ (Email).

*Gợi ý cấu trúc:*
```javascript
const jobData = {
    title: "Chuyên viên Digital Marketing",
    location: "Quận 1, TP.HCM",
    salary: "15.000.000 - 25.000.000 VNĐ",
    responsibilities: ["Lên kế hoạch FB Ads.", "Phân tích số liệu."],
};
```

**Bước 2: Thiết kế Giao diện (UI/UX)**
Đảo mã trang `tuyen-dung.html` dựa theo phong cách **Dark Mode & Glassmorphism** tương tự cổng thông tin nội bộ (Internal Portal).
- Tích hợp **Tailwind CSS**.
- Background Gradient đẹp mắt.

**Bước 3: Lập trình Logic hiển thị (Javascript)**
- Liên kết file `jobs-data.js` vào HTML.
- Dùng `<script>` truy xuất `jobData` để Render chữ.
- Tạo nút **"Ứng tuyển ngay" (Apply Now) nổi bật**, bấm vào hiện Alert thông báo email nộp CV. 

**Bước 4: Kiểm thử và Xuất bản (Vercel)**
1. Mở file bằng trình duyệt để fix lỗi UI/Web Mobile.
2. Tự động cập nhật số liệu `jobs-data` để xem Web tự đổi chữ.
3. Kéo thả lên Vercel lấy URL khoe bạn bè.
