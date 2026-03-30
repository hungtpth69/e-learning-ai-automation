# Bài Giảng: Tự Động Hóa Đồng Bộ Dữ Liệu Lên Google Drive

## 1. Thông Tin Buổi Học
- **Chủ đề**: Tự động hóa quy trình sao lưu và đồng bộ dữ liệu cục bộ (Local) lên hệ thống lưu trữ đám mây (Google Drive).
- **Thời lượng dự kiến**: 45 phút.
- **Đối tượng**: Học viên khóa Tự động hóa Doanh nghiệp / Trợ lý AI.
- **Công cụ sử dụng**: Agent AI, File CSV, Google Drive API.

---

## 2. Tình Huống Thực Tế (Hoàn Cảnh Giả Định)
Hãy tưởng tượng bạn đang là một nhân sự phòng HR (Nhân sự) tại công ty. 

Hàng tuần, bạn phải cập nhật danh sách hồ sơ nhân viên mới, trạng thái làm việc (thử việc, nghỉ phép), thay đổi phòng ban, v.v. Tất cả dữ liệu này được bạn quản lý và chỉnh sửa trực tiếp trên máy tính cá nhân bằng phần mềm Excel hoặc lưu dưới dạng file `.csv`.

💡 **Vấn đề đặt ra:** 
Sếp và các phòng ban khác cần truy cập vào bản cập nhật mới nhất của file này liên tục. Tuy nhiên, nếu bạn cứ chỉnh sửa xong lại phải đăng nhập vào file trên Drive, copy/paste thủ công hoặc phải tạo lại file mới tải lên, thì rất mất thời gian và dễ xảy ra sai sót.

🚀 **Giải pháp tự động hóa:**
Chúng ta sẽ triển khai một **Agent Tự động hóa Đồng bộ dữ liệu**. Ngay sau khi bạn chỉnh sửa file CSV trên máy tính xong, Agent này sẽ tự động thay bạn upload, hoặc đẩy dữ liệu mới nhất đó ghi thẳng lên môi trường Google Drive để sếp có thể xem ngay lập tức.

---

## 3. Mục Tiêu Học Tập
Kết thúc bài học này, học viên có khả năng:
1. Hiểu cách thức một hệ thống tự động hóa giao tiếp giữa máy tính cá nhân và môi trường Cloud (Google Drive).
2. Nắm được luồng dữ liệu (Data Pipeline): `Input (File CSV cục bộ)` ➔ `Agent Xử lý` ➔ `Output (Cập nhật trên Google Drive)`.
3. Tự tay thực hành cấu hình và ra lệnh cho Agent chạy lệnh đồng bộ.

---

## 4. Tài Liệu Thực Hành (Mockup Data)
Giảng viên đã chuẩn bị sẵn một file dữ liệu mẫu cho bài thực hành này.
- **Tên file**: `mockup_hoso_nhansu.csv`
- **Nội dung file**: Chứa 10 dòng dữ liệu nhân sự cơ bản với các cột: *Mã NV, Họ và Tên, Phòng Ban, Chức Vụ, Email, Số Điện Thoại, Trạng Thái*.
- **Hành động**: Các học viên sẽ thay đổi một vài thông tin trên file của máy mình (ví dụ: đổi trạng thái của `NV009` từ Thử việc sang Đang làm việc).

---

## 5. Kịch Bản Demo Trên Lớp (Dành Cho Giảng Viên & Học Viên)

### Bước 1: Mở và Chỉnh sửa dữ liệu (Local)
1. Học viên mở file `mockup_hoso_nhansu.csv` bằng Excel hoặc trình soạn thảo văn bản.
2. Thực hiện hành động **cập nhật dữ liệu**.
   *Ví dụ: Cập nhật chức vụ cho nhân sự Trần Thị Bình thành "Kế toán trưởng" và lưu lại.*

### Bước 2: Kích hoạt Agent Đồng Bộ
Giảng viên hướng dẫn học viên gọi Agent tự động hóa bằng lệnh ngắn (Slash command) ngay trong môi trường làm việc:
> **Lệnh kích hoạt:** `/sync-drive`

*Hoặc chạy trực tiếp script bằng lệnh:* `python gdrive_workflow.py`

### Bước 3: Quan sát quá trình Agent làm việc
Học viên theo dõi màn hình Terminal. Agent sẽ báo cáo các tương tác nó đang thực hiện:
- 🟢 *[Agent]* Đang đọc dữ liệu từ file `mockup_hoso_nhansu.csv`...
- 🟢 *[Agent]* Kết nối xác thực với Google Drive (Service Account)...
- 🟢 *[Agent]* Tìm thấy thư mục đích, tiến hành tải/cập nhật dữ liệu...
- ✅ *[Agent]* Hoàn tất đồng bộ! File của bạn đã khả dụng trên Google Drive.

### Bước 4: Kiểm tra kết quả (Cloud)
1. Giảng viên cấp link trỏ đến thư mục Google Drive của công ty (Giả lập).
2. Học viên truy cập link và mở file vừa được đẩy lên để thấy rằng sự thay đổi ở *Bước 1* đã xuất hiện hoàn hảo trên môi trường làm việc chung.

---

## 6. Bài Tập Về Nhà
- **Yêu cầu 1**: Thêm 3 nhân sự mới vào file `mockup_hoso_nhansu.csv` của bản thân.
- **Yêu cầu 2**: Lưu file dưới một tên khác (ví dụ: `danhsach_thang12.csv`).
- **Yêu cầu 3**: Hiệu chỉnh lại cài đặt của Agent để hệ thống nhận diện đúng tên file mới và đồng bộ thành công. Chụp ảnh màn hình kết quả trên Google Drive gửi lên nhóm lớp.
