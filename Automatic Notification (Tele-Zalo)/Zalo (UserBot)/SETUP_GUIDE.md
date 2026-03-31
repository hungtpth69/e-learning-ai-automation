# 📖 Hướng Dẫn Cài Đặt - Zalo UserBot (DOM Playwright)

Đây là tài liệu chỉ dẫn các bước cài đặt thư viện cần thiết để sử dụng khả năng thao tác Browser qua **Playwright** cho mục tiêu là làm Automation Zalo Cá Nhân.

## Bước 1: Cài đặt thư viện Playwright
Playwright không được cài đặt sẵn kèm Python. Thư viện này của Microsoft sẽ giúp bạn điều khiển Chromium (Google Chrome) qua dòng lệnh.

Mở CMD/Terminal và gõ lệnh sau:
```bash
pip install pytest-playwright
# hoặc
pip install playwright
```

## Bước 2: Tải xuống các Driver trình duyệt (Chromium)
Sau khi cài đặt gói python, bạn cần tải về Driver của Browser để code có thể gọi và điều hướng nó. Gõ lệnh:
```bash
playwright install chromium
```
*Ghi chú: Bước này có thể tải khoảng trên dưới 100MB cho bản headless-chromium của hãng.*

## Bước 3: Chuẩn bị nội dung file danh sách 
Mở file `zalo_userbot_send_list.csv` (Dành cho việc Gửi tin) hoặc `zalo_userbot_read_list.csv` (Dành cho việc Đọc tin) ra bằng Excel hoặc Text Editor (Notepad/VS Code).
Thêm các số điện thoại bạn muốn gửi thử.

> **Mẹo**: Nếu bạn muốn gửi tin nhắn kèm cả Xuống Dòng (Line break) trong CSV, bạn hãy bao nội dung bên trong cặp ngoặc kép.
> Ví dụ:
> ```csv
> Phone Number,Name,Message Template
> 0912345678,Khải Hoàng,"Chào {name}, 
> Đây là tin nhắn Zalo Playwright ở dòng 2.
> Chúc một ngày tốt lành"
> ```

## Bước 4: Khởi chạy Code

Tại Terminal (nhớ chuyển hướng vào đúng folder **Zalo (UserBot)** trước bằng lệnh `cd e:\Antigravity\e-learning\Automatic Notification (Tele-Zalo)\Zalo (UserBot)`), hãy gõ:

```bash
python zalo_userbot_dom_workflow.py
```

### 🔑 Quá trình Đăng nhập diễn ra làm sao?
- Ngay khi script bật lên, trình duyệt Chromium do Bot điều khiển sẽ xuất hiện trên màn hình nền.
- Trình duyệt truy cập vào `chat.zalo.me`.
- **Nếu là lần chạy đầu tiên:** Màn hình sẽ có QR Code đăng nhập giống như khi bạn dùng máy mới nghiệm thu. Lấy điện thoại quét Zalo vào. Lúc này Script sẽ tự động chờ tối đa **60 Giây**.
- Quét xong, đăng nhập thành công là vào màn hình chat. Lúc này con Bot nhận hiệu lệnh là đã có Thanh Tìm Kiếm Search, nó sẽ bắt đầu gõ từng sdt trong file csv.
- Chú ý: **Tuyệt đối KHÔNG LĂN CHUỘT hoặc CLICK CHUỘT VÀO THANH CHAT** vào lúc tool đang gõ phím vì nó sẽ làm loạn dòng text mà Robot đang type.

### 🐛 Cách khắc phục lỗi phổ biến: Lỗi Selectors bị thay đổi (Maintain)
Các trang Web đôi khi sau 1 năm họ thay đổi thẻ HTML UI/UX lại. 

Trong source code python:
`#contact-search-input` là ID của thanh tìm kiếm.
`#richInput` là ID của ô nhập tin nhắn.

=> Nếu script báo lỗi Không Thấy (Timeout) khung chat, tức là Zalo đã đổi tên ID của HTML. Lúc đó hãy liên hệ Kỹ sư mở trình duyệt, nhấn F12 (Inspect Element) để lấy lại ID HTML mới chỉnh vào đoạn mã.  
Nhờ cách build DOM ID này nên Tool sẽ an toàn mà không phải phụ thuộc độ phân giải to/nhỏ của các máy tính như auto click cổ điển.
