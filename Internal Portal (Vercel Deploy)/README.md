# 🌐 Web Portal Deployment (Github + Vercel Cloud)

> **Hệ Thống Tự Động Hóa Xuất Bản Website Tĩnh Lên Cloud**
> Công cụ giúp dân Văn phòng (Non-tech) hô biến hàng đống văn bản luật, quy chế, danh bạ cồng kềnh thành một "Cổng Thông Tin Công Ty (Website)" và phóng lên mạng cực kỳ Pro với đầy đủ đường link chia sẻ.

## 🎯 Mục Đích Hoạt Động
Combo Agent thực hiện 3 Pha hoàn toàn ẩn giấu:
- **Pha 1 (`generate_portal.py`)**: Đọc nhai các File Văn bản Rác (.txt, .docx), Agent sẽ Tự code lại HTML để tạo thành trang Web có Giao Diện.
- **Pha 2 (`deploy_portal.py`)**: Dùng lệnh Git ngầm bắn Data sang nhà Kho Github.
- **Pha 3**: Cập bến Vercel (Máy chủ Mỹ) và chạy Server online Mãi Mãi với giá 0 VNĐ.

## 🛠 Hướng Dẫn Setup Các Tài Khoản Máy Chủ (Step-by-Step)
*Để bot làm việc thay bạn, bạn cần Đăng ký Vercel và GitHub rồi cấp quyền 1 lần duy nhất.*

### Bước 1: Cài đặt Dụng Cụ Nghề Trắng (Trên Máy Tính)
1. Bạn vào [git-scm.com/downloads](https://git-scm.com/downloads), click dòng `Download for Windows`. Tải về cài đặt, cứ bấm `Next` liên tục đến lúc xong.
2. Tiếp tục vào [cli.github.com](https://cli.github.com/), chọn tải bản `Windows`. Cài đặt bình thường.

### Bước 2: Thiết lập Tài khoản Nhà Kho (Github)
1. Lên trình duyệt vào [Github.com](https://github.com/) đăng ký một tài khoản miễn phí. (Nhớ lưu User và Pass cẩn thận).
2. Xong xuôi, quay lại Máy tính, Mở Terminal (Cửa sổ Đen gõ lệnh phần mềm), nhập lệnh gõ cửa:
   ```bash
   gh auth login
   ```
3. Màn hình console hiện ra 1 dãy các lựa chọn. Bạn lấy **Mũi tên Lên/Xuống trên bàn phím** -> Chọn dòng chữ **GitHub.com** -> Bấm phím **Enter**.
4. Chọn giao thức mạng: Chọn **HTTPS** -> **Enter**.
5. Nó hỏi: `Authenticate Git with your GitHub credentials?` -> Gõ chữ **Y** -> **Enter**.
6. Chọn chức năng **Login with a web browser** (Mở bằng trình duyệt). Màn hình sẽ sinh ra 1 dãy số mật mã, vd: `ABCD-1234`. Nhấn **Enter** thì Tab Chrome sẽ nảy lên, bạn chép mã đó dán vô Github trên web. -> Báo Successful là Bạn đã kết nối não bộ Github vào Máy tính!

### Bước 3: Đăng ký Máy Chủ Lưu Trữ VERCEL
1. Bạn đăng ký tài khoản hosting tại cổng [Vercel.com/signup](https://vercel.com/signup).
2. Tới màn hình đăng ký, bạn nhấp luôn nút Đen chữ Trắng: **"Continue with GitHub"** (CỰC KỲ QUAN TRỌNG ĐỂ CẢ HỆ THỐNG ĐỒNG BỘ).

## 🚀 Hướng Dẫn Chạy Liên Hoàn Cước
Khi phần mềm và mạng nhện đã thắt chặt, công việc của bạn chỉ còn là:

**Pha 1: Nhào nặn Giao Diện Web**
Ném toàn bộ Văn bản Quy chế cty vào Folder con có tên `Raw_Documents`. Sau đó gõ dòng lệnh này vào Chat Terminal:
```
/build-portal
```
*(Bạn không cần Code. Thuật toán tự đẻ ra cả hệ thống file mã nguồn CSS, HTML siêu đẹp ở màn hình bên cạnh).*

**Pha 2: Tiễn Code Lên Mây Github**
Gõ tiếp câu lệnh sau để con Bot lập trình gom hết mã đẩy lên Cloud:
```
/deploy-portal
```
*(Code báo chạy Progress %... 100%. Nó sẽ tạo sẵn một kho báu tên là `antigravity-hub-2026`).*

**Pha 3: Kích Hoạt Nổ Đường Link Vercel**
Máy tính bạn có Web, Github có Data, giờ đưa nó lên mạng ảo:
1. Mở trang chủ Vercel, nhìn góc phải bấm nút Đen: **Add New** -> chọn **Project**.
2. Ở mục "Import Git Repository", nhãn quang của bạn sẽ thấy ngay tên dự án `antigravity-hub-2026` lù lù ở đó. Bấm chữ **Import**.
3. Góc dưới cùng, nhấn **DEPLOY**. Mất tầm 7-10 giây để Vercel phóng Web lên. 

Thành Quả: Pháo hoa Confetti sẽ bung lụa rợp màn hình Web. Máy chủ sinh ra một dòng URL (Đường Link) có đuôi `.vercel.app`. Hãy copy gửi qua ĐT cho đồng nghiệp để khoe thành quả Code-free Portal Mê mẩn này!!
