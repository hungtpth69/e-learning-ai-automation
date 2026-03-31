# ⚙️ 02. HƯỚNG DẪN CÀI ĐẶT & SỬ DỤNG (SETUP GUIDE)

Đây là tài liệu chỉ dẫn các bước cài đặt thư viện cần thiết để sử dụng Playwright điều khiển Zalo Cá Nhân.

## Bước 1: Cài đặt thư viện Playwright
Playwright là thư viện của Microsoft giúp điều khiển trình duyệt Chromium qua dòng lệnh. Mở Terminal và gõ:
```bash
pip install pytest-playwright
# hoặc
pip install playwright
```

## Bước 2: Tải xuống Driver trình duyệt (Chromium)
Tiếp theo, tải về bộ Driver trình duyệt nền tảng để code có thể gọi và điều hướng nó:
```bash
playwright install chromium
```
*(Ghi chú: Bước này sẽ tải khoảng ~100MB cho bản headless-chromium).*

## Bước 3: Đăng nhập & Lưu trữ Session Zalo
1. Tại Terminal, chuyển hướng vào folder Zalo (UserBot):
   ```bash
   cd "e:\Antigravity\e-learning\Automatic Notification (Tele-Zalo)\Zalo (UserBot)"
   ```
2. Chạy script để đăng nhập lần đầu:
   - Hệ thống mở trình duyệt vào `chat.zalo.me`.
   - Màn hình sẽ hiển thị QR Code. Lấy ứng dụng Zalo trên điện thoại để quét mã.
   - Script sẽ lưu trữ Cookies lại thông qua cấu hình `Persistent Context`. Các lần chạy tự động sau này sẽ không cần quét lại (trừ khi Cookie hết hạn).
3. **Lưu ý quan trọng (Đồng bộ dữ liệu):** Zalo Web trên Playwright thiết lập một môi trường trình duyệt rỗng cô lập. Lần đầu đăng nhập, bạn cần chạy file `zalo_sync_data.py`. Sau đó bấm nút **"Đồng bộ ngay" (Sync Messages)** trên cửa sổ trình duyệt đó và xác nhận trên ứng dụng Zalo điện thoại để tải đoạn hội thoại cũ sang máy.

## Bước 4: Khởi Chạy Code Chính
Tùy vào nhu cầu (Gửi hay Đọc tin), bạn truy cập folder `Sender` hoặc `Reader` và chạy file python tương ứng:
```bash
cd "Sender"
python zalo_send_workflow.py
```
*(Tuyệt đối KHÔNG lăn chuột hoặc Click chuột vào thanh chat lúc Robot đang tự động type phím)*

## 🐛 Bắt Bệnh & Bảo Trì Code (Maintain)
- Các UI Web có thể thay đổi ID thẻ (HTML) theo thời gian. 
- Nếu Tool báo xuất hiện lỗi "Timeout", hãy nhấn F12 (Inspect Element) trên trình duyệt để kiểm tra ID HTML ô nhập liệu mới và cập nhật lại vào Script. Sự phụ thuộc vào DOM thay vì Auto-Click Tọa độ giúp script tự ổn định với mọi độ phân giải màn hình.
