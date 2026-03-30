# ☁️ Google Sheets Automation (Data Center)

> **Rút Trích Dữ Liệu Tự Động Từ Google Drive**
> Công cụ giúp bạn tải và móc nối bộ nhớ (File Excel/CSV) từ Đám Mây Google về máy tính mà không cần phải tải tay từng file.

## 🎯 Mục Đích Hoạt Động
Việc vào Google Drive, tìm tên file, bấm chuột phải, bấm Tải xuống giải nén quá phiền phức. Agent (`gdrive_workflow.py`) được thiết kế đặc biệt không bó cứng vào file nào cả. Bạn chỉ việc nhập tên File bạn muốn lấy từ Google Drive của mình, Trí tuệ Nhân tạo sẽ tự tìm và kéo thẳng file đó về Ổ cứng (Local) cực kỳ linh hoạt.

## 🛠 Hướng Dẫn Cài Đặt Tài Khoản Dành Cho Người Mới (Step-by-Step)

Để kết nối máy tính của bạn với Đám mây Google, chúng ta cần một công cụ cầu nối mang tên `gws` (Google Workspace CLI) và một CHỨNG CHỈ TỪ MÁY CHỦ GOOGLE. Hãy làm lần lượt các bước này (Chỉ cần làm 1 lần duy nhất trong đời):

### Bước 1: Khởi Tạo Dự Án Trên Google Cloud (GCP)
*(Đây là nơi Google cho phép bạn lập trình tương tác với hệ thống của họ)*
1. Truy cập vào [Google Cloud Console](https://console.cloud.google.com/) và bằng tài khoản Gmail của bạn.
2. Tick chọn đồng ý các điều khoản (nếu có bảng hiện lên). Ngó lên Menu góc Trái Cùng trên đỉnh màn hình (Cạnh chữ Google Cloud), bấm vào ô **Select a project** -> Góc phải bảng bấm **New Project**.
3. Đặt Tên Dự án (Ví dụ: `Antigravity Automation 2026`) -> Nhấn **CREATE**.
4. Chờ 5 giây, nhấn vào biểu tượng Quả Chuông (Thông báo) -> Chọn **Select Project** để đi vào bên trong dự án vừa tạo.

### Bước 2: Bật Cầu Giao API (Enable Google Drive API)
1. Trong thanh tìm kiếm (Search) trên cùng của GCP, gõ chữ: `Google Drive` và Enter.
2. Bạn sẽ thấy biểu tượng hình tam giác Drive, bấm vào đó -> Nhấn nút màu xanh **ENABLE** để kích hoạt sức mạnh của Đám mây.

### Bước 3: Tạo Màn Hình Đồng Ý (OAuth Consent Screen)
*(Giống như bạn tạo một App điện thoại xin quyền truy cập ảnh của user, ở đây ta xin quyền truy cập Drive)*
1. Ở Menu Trái, tìm mục **APIs & Services** -> Chọn **OAuth consent screen**.
2. Tại phần User Type, đánh dấu tích vào ô **External** (Dành cho mọi User bên ngoài) -> Nhấn **CREATE**.
3. **App information**: Điền Tên App (Vd: `Antigravity BOT`) và Email của bạn.
4. Cuộn xuống cuối, chỗ **Developer contact information**: Điền lại Email của bạn lần nữa -> Nhấn **SAVE AND CONTINUE**.
5. Qua bước Scopes bỏ qua -> **SAVE AND CONTINUE**.
6. Tại bước **Test Users**: Bấm **ADD USERS** -> Gõ địa chỉ Gmail thực tế của bạn vào đó (Bắt buộc phải add chính bạn vào để test nhé). Nhấn **SAVE AND CONTINUE** và quay lại màn hình Dashboard.

### Bước 4: Tự Cấp Chìa Khóa Bí Mật (Create Credentials)
1. Ở Menu Trái, chuyển sang tab **Credentials**.
2. Bấm nút **+ CREATE CREDENTIALS** trên góc trên -> Chọn **OAuth client ID**.
3. Ở ô **Application type**, thả menu xuống và bắt buộc chọn **Desktop app**. Đặt tên tùy ý (Vd: `Toàn Quyền Windows`) -> Bấm **CREATE**.
4. Màn hình chúc mừng hiện ra với bảng thông số quý giá gồm `Client ID` và `Client Secret`. 
5. Bấm vào nút **DOWNLOAD JSON** để tải cái chìa khóa đó về máy tính, hoặc nhấn nút Copy lại hai cái mã `Client ID` và `Client Secret` này để dán vào cấu hình `gws`.

### Bước 5: Cài Đặt GWS CLI (Công Cụ Lõi Đám Mây)
Kho lưu trữ chính thức của công cụ: [Google Workspace CLI (GitHub)](https://github.com/googleworkspace/cli)

**Cách Dễ Nhất** cho người chưa từng học IT:
1. Mở cửa sổ Terminal (bảng gõ lệnh màu đen ở dưới cùng của phần mềm/IDE) ngay tại thư mục chứa file code `gdrive_workflow.py`.
2. Gõ nguyên đoạn lệnh cài đặt tự động dưới đây và nhấn phím **Enter**:
   ```bash
   npm install -g @googleworkspace/cli
   ```
3. Kê cao gối chờ hệ thống chạy trong vài giây. Khi thấy dòng trạng thái báo "added..." hiện ra, bộ cài đặt lõi GWS đã chính thức bám rễ thành công vào máy của bạn!

### Bước 6: Khởi tạo Cổng Xác Thực (Login Bằng GWS)
1. Mở cửa sổ Terminal (cửa sổ ruy-băng đen gõ chữ) của phần mềm.
2. (Tùy theo version GWS của giảng viên) Nếu bạn được yêu cầu nạp Client ID trước, hãy cấu hình `gws` bằng mã `Client ID` và `Client Secret` bạn vừa lấy ở Bước 4.
3. Gõ dòng lệnh quyền lực này và nhấn Enter:
   ```bash
   gws auth login
   ```
3. Lập tức, Trình duyệt Web (Chrome, Edge hoặc Cốc Cốc) của bạn sẽ tự bật lên 1 Tab mới. Màn hình Google quen thuộc hiện ra.
4. Google sẽ hỏi: "Công cụ này muốn truy cập vào Google Drive của bạn?". Bạn hãy **Click chọn Tài khoản Gmail** thân quen của bạn.
5. Tiếp tục bấm nút **Cho phép (Allow)** hoặc **Tiếp tục**.
6. XONG! Quay về màn hình Terminal đen, bạn sẽ thấy hiện dòng chữ "Login Thành Công" màu xanh. Từ nay máy tính của bạn đã được trao Vương miện thông suốt với Google.

### Bước 3: Chuẩn Bị Vùng Dữ Liệu
1. Bạn cứ sử dụng Google Drive trên mạng để tạo thư mục, tải file Excel lên bình thường.
2. Tuyệt đối **KHÔNG CẦN BẬT CHIA SẺ (Share Public)** vì file mang tính bảo mật cao. Máy tính của bạn đang đóng vai chính bạn nên nó đọc được tất cả. Hãy nhớ cái **Tên file** mà bạn vừa đẩy lên (Ví dụ: `Danh_Ba_Nhan_Vien_Thang_10.csv`).

## 🚀 Hướng Dẫn Kích Hoạt Phần Mềm
Bất cứ khi nào bạn cần lấy Dữ liệu Data Center từ Đám mây, hãy gõ 1 câu thần chú vào cửa sổ Chat của IDE:
```
/sync-drive
```

## 📊 Trải Nghiệm & Kết Quả 
1. **Trí Tuệ Mở Lời:** Bảng đen Console tĩnh lặng bỗng bật lên dòng chữ hỏi bạn: `🔍 Nhập Lệnh: Bạn muốn AI [Clone] Tệp / Thư mục nào trên Drive về máy?`.
2. **Khách hàng Trả lời:** Trả lời cho con Bot biết ý đồ của bạn. Gõ ngay tên file lúc nãy: `Danh_Ba_Nhan_Vien.csv` và gõ phím mạn Enter!
3. Hệ thống sẽ tự rà soát Đám mây, quét toàn bộ vũ trụ Google Drive của bạn, tìm ra ID Ẩn của file và tiến hành nhồi 1 cú tải ném thẳng vào máy tính của bạn (Ra tên dạng `Clone_Danh_Ba_Nhan_Vien.csv`).
4. File xuất hiện trên Ổ cứng chỉ trong tích tắc. Bạn có thể mở bằng Excel thao tác thả ga mà không lo treo dữ liệu Cloud.
