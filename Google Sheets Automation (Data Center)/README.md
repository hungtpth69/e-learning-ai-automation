# ☁️ Hướng Dẫn Thực Hành (Demo Usecase): Google Sheets Automation

> **Tình Huống Sử Dụng (Usecase): Tự Động Đồng Bộ Hồ Sơ Nhân Sự Từ Đám Mây**
> Công cụ ứng dụng Trí Tuệ Nhân Tạo (AI Agent) giúp khối Hành Chính Nhân Sự (HR) hoặc Data Analyst dễ dàng "Kéo" (Sync) các file theo dõi số liệu (Excel/CSV) từ Đám Mây Google Drive về máy tính cục bộ (Local) chỉ trong tích tắc, không cần phải thao tác "Chuột phải -> Tải xuống" thủ công.

---

## 🎯 Bối Cảnh Thực Tiễn
Vào cuối tháng, bộ phận HR cần tổng hợp dữ liệu từ file **Hồ sơ nhân sự** đang được lưu trữ bảo mật trên Google Drive của Sếp để tiến hành tính lương. Thay vì phải chui vào hàng chục lớp thư mục trên Drive, tìm đúng file và tải xuống, bạn hoàn toàn có thể ra lệnh cho Agent tìm và đồng bộ nó thẳng về máy tính của bạn thông qua Giao thức API. 

*(Chú ý: Đảm bảo bạn đã hoàn tất thủ tục liên kết chứng chỉ Cấu hình GWS ở bài `SETUP_GUIDE.md` trước khi thực hành)*

---

## 🛠 Chuẩn Bị (Nạp Dữ Liệu Lên Đám Mây)
Để thực hành giả lập bài toán, chúng ta sử dụng file dữ liệu mẫu đã có sẵn trong dự án: `mockup_hoso_nhansu.csv`. 

**Nhiệm vụ của bạn:**
1. Hãy tìm file `mockup_hoso_nhansu.csv` trong thư mục này.
2. Mở trình duyệt, đăng nhập vào **Google Drive** của bạn.
3. Tải (Upload) hẳn file `mockup_hoso_nhansu.csv` đó lên một thư mục bất kỳ trên Google Drive của bạn (Tuyệt đối **KHÔNG CẦN CHIA SẺ Public**, cứ để Private, vì Agent sử dụng chính quyền truy cập của chủ tài khoản).
4. Xóa file `mockup_hoso_nhansu.csv` trên máy tính đi (Để tí nữa kiểm chứng xem máy có kéo thành công từ Mây về hay không).

---

## 🚀 Kích Hoạt Luồng AI Kéo Dữ Liệu
Hãy xem Trí tuệ ảo lục lọi vũ trụ dữ liệu khổng lồ của Google nạp file về máy như thế nào. Bạn chỉ cần gõ 1 câu thần chú vào cửa sổ Chat của IDE (Terminal) để gọi Agent:

```bash
/sync-drive
```

**Quá Trình Vận Hành Mượt Mà:**
1. **Trí Tuệ Tiếp Nhận Lệnh:** Bảng lệnh sẽ phản hồi lại bạn bằng tiếng Việt: `🔍 Nhập Lệnh: Bạn muốn AI [Clone] Tệp / Thư mục nào trên Drive về máy?`.
2. **Ra Lệnh Kéo File:** Bạn chỉ cần gõ tên file mà bạn muốn kéo (Ở case này là: `mockup_hoso_nhansu.csv`) và gõ phím mạn Enter!
3. **Quét & Đồng Bộ Siêu Tốc:** Thuật toán AI lập tức kết nối tới nền tảng Đám mây Google, quét tất cả thư mục của bạn để trích ra đúng ID Ẩn của file. Lệnh Download API đẩy thẳng tốc độ cao kéo dữ liệu về và tự động đổi tên thành `Clone_mockup_hoso_nhansu.csv` (Để cảnh báo đây là bản sao từ vệ tinh).
4. Bạn có thể mở file đó ngay trên Ổ cứng máy tính thao tác thả ga mà không lo nhầm lẫn với file Gốc trên mạng!
