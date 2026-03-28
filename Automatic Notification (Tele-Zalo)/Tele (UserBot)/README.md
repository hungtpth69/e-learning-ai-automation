# 🦸‍♂️ Telegram UserBot (Tự động hóa Tài khoản Cá nhân)

> **CẢNH BÁO ĐỎ (Dành cho Học viên):** 
> Khác với con Bot (@BotFather) sinh ra để tự động hóa Doanh nghiệp, việc dùng Tài Khoản Cá Nhân đi gửi tin nhắn hàng loạt bằng phần mềm có rủi ro **BỊ KHÓA TÀI KHOẢN (BAN NICK/SĐT) VĨNH VIỄN** nếu bạn dùng để SPAM người lạ. Thuật toán của mạng Telegram giám sát hệ thống UserBot rất gắt gao. Hãy chỉ dùng module này để nhắn tin cho Khách hàng đã quen biết hoặc xử lý nghiệp vụ nội bộ Công ty!

## ⚙️ Cấu Hình Ban Đầu (Lấy Khóa API Cá nhân)
Đối với Tài khoản thật, hệ thống không dùng Token. Chúng ta phải đi cửa sau vào hệ thống MTProto:
1. Truy cập cổng điện toán phát triển mạng: [https://my.telegram.org/auth](https://my.telegram.org/auth) -> Đăng nhập bằng Số điện thoại của bạn.
2. Bấm vào mục **API development tools**.
3. Điền đại một cái Tên Ứng dụng bất kỳ vào form (Ví dụ: `AutoSend`). Cuối cùng bạn sẽ khai thác được 2 thông số tối mật:
   - `App api_id` (Một con số, VD: `2134567`)
   - `App api_hash` (Một chuỗi ký tự bảo mật rất dài)
4. Mở file `telethon_config.txt` bằng Notepad, dán 2 mỏ vàng này vào đúng vị trí của chúng.

## 👥 Cấu hình Danh bạ (Siêu Ưu Điểm)
Ưu điểm khổng lồ nhất của hệ thống UserBot so với Bot doanh nghiệp là: Bạn **Không cần đi quét lấy Chat ID cực nhọc**. UserBot là tài khoản người, nên nó bề trên và có thể gửi tin nhắn thẳng bằng Số điện thoại (Thêm `+84` ở đầu) hoặc Username (`@ten_nguoi_dung_telegram`).
Mở file Excel `userbot_contact_list.csv` và điền danh sách bạn muốn nhắn.

## 🚀 Hướng Dẫn Kích Hoạt Phần Mềm
Khác với Bot API chuẩn, phần mềm này cần công cụ mô phỏng giao thức MTProto cực nặng có tên là (Telethon). Ở màn hình đen Terminal, chạy lệnh cài đặt:
```bash
pip install telethon
```

Sau khi cài đặt xong, thực thi phần mềm Python: Cứ mở file `telegram_userbot_workflow.py`. 
**(TRONG LẦN CHẠY ĐẦU TIÊN)**: Góc lệnh màn hình đen (Terminal) sẽ dừng lại và hiển thị yêu cầu bạn gõ `Số điện thoại` và `Mã Code Telegram` được gửi về máy điện thoại của bạn để đăng nhập xác thực. 

Khi đã login thành công, máy tính sẽ sinh ra 1 file vô hình `.session` trên folder. Ở các lần chạy chiến dịch sau này, phần mềm sẽ không bao giờ hỏi code nữa mà tự động chạy rẹt rẹt đi gửi tin nhắn cho mọi người!
