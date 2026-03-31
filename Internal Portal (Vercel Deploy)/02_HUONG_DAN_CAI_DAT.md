# ⚙️ 02. HƯỚNG DẪN CÀI ĐẶT & SỬ DỤNG (SETUP DEPLOY VERCEL)

Đây là tài liệu chỉ dẫn để đưa Portal nội bộ của bạn từ "Máy tính bàn" lên "Mạng Internet toàn cầu" sử dụng Github CLI và Vercel.

## Bước 1: Cài đặt Github CLI & Đăng nhập
1. Tải và cài đặt phần mềm [Github CLI](https://cli.github.com/).
2. Mở Terminal và gõ lệnh sau để đăng nhập tài khoản Github của bạn vào máy:
   ```bash
   gh auth login
   ```
3. Làm theo các bước: Chọn `GitHub.com` -> `HTTPS` -> `Y` (Authenticate with web browser). Trình duyệt sẽ bật lên, bạn copy dãy số Terminal cho vào trình duyệt để xác thực.

## Bước 2: Chuẩn Bị File Dữ Liệu (Mô hình tách biệt Data)
1. Thư mục `Internal Portal (Vercel Deploy)` chứa file `index.html` (Giao diện chuẩn Glassmorphism Tuyệt đẹp). Đừng quan tâm sửa code HTML trừ phi bạn biết lập trình.
2. Mở file **`data.js`**. Đây là trái tim nội dung. Bạn chỉ cần sửa hoặc thêm Text vào các trường `documents` (Tài liệu nội bộ) và `contacts` (Danh bạ) theo đúng cấu trúc JSON tĩnh đang có.

## Bước 3: Đẩy Dữ Liệu Lên Mạng (Deploy)
1. Mở Terminal tại folder này:
   ```bash
   cd "e:\Antigravity\e-learning\Internal Portal (Vercel Deploy)"
   ```
2. Gọi Script tự động Python đẩy toàn bộ folder thành 1 kho lưu trữ (Repo) lên Github của bạn:
   ```bash
   python deploy_portal.py "ten-du-an-cua-ban"
   ```
   *(Script sẽ tự dọn dẹp Git cũ, tự Commit và đẩy thẳng lên Repository mới mang tên `ten-du-an-cua-ban` ở chế độ Private).*

## Bước 4: Trỏ Nguồn Tại Vercel.com
1. Truy cập [Vercel.com](https://vercel.com/) và đăng nhập bằng tài khoản Github của bạn.
2. Bấm nút **Add New...** -> Chọn **Project**.
3. Bạn sẽ thấy Repositiory `ten-du-an-cua-ban` vừa được tool python đẩy lên. Bấm nút **Import**.
4. Giữ nguyên mọi cấu hình mặc định, bấm **Deploy**.
5. Chờ 30 giây màn hình hiện pháo hoa. Copy đường Link sống (Live URL) mà Vercel cấp để gửi cho nội bộ công ty truy cập!

*(Mẹo: Bạn có thể chạy lệnh `/build-portal` hoặc `/deploy-portal` từ Agent để tự động hóa trọn gói quá trình này)*.
