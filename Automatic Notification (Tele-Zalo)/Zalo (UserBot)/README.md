# Gửi Tin Nhắn Zalo Cá Nhân (DOM Automation UserBot)

Thư mục này chứa một bộ công cụ sử dụng khái niệm **DOM Automation** (Tự động hóa trình duyệt web/Browser Automation) bằng thư viện `Playwright`.

Lý do ra đời script này là vì tính năng tự động gửi tin nhắn của Zalo OA (Zalo Doanh Nghiệp) cần có pháp lý của công ty và phải trả phí mua ZCA, hoặc phải qua các đợt duyệt API rất khắt khe. Trong một số quy trình như Gửi thông báo thực tập nội bộ, gửi tin cho Học Viên, gửi tin đồng nghiệp, chúng ta chỉ cần dùng thẳng **Tài khoản Zalo Cá Nhân** (chạy ngầm). 

Do Zalo Cá Nhân không cấp "API Key", phương án duy nhất và tối ưu nhất là dùng "Robot" Playwright:
1. Tự động mở Chrome lên.
2. Tự động tìm danh bạ (Search sdt).
3. Tự động gõ tin nhắn.
4. Tự động ấn Gửi.

Mọi thứ chính xác y như khi mình lướt web bằng tay thay vì dùng API gọi Server Zalo.

---

### Mức Độ An Toàn
- **Cookie Persistent**: Lần đầu chạy script, trình duyệt sẽ mở bình thường và yêu cầu quét QR Code (đăng nhập vào `chat.zalo.me`). Các lần chạy tiếp theo, Playwright sẽ tự động "nhớ" nhờ cấu hình `Persistent Context`. Nếu tài khoản của bạn bị Cookie Expired (hết hạn), Zalo sẽ tự bắt bạn quét QR lại, rất an toàn.
- **Human Typing**: Script sử dụng luồng "Gõ từng ký tự" trên bàn phím (Typing Delay 20-50ms) thay vì copy-paste thẳng toàn bộ nội dung để qua mặt bộ máy Anti-Spam (chống spam) của Zalo Web.
- **Break Time (Thời gian chờ)**: Script tự động Random chờ 5 tới 10 giây giữa 2 lượt tin nhắn liên tiếp nhằm mô phỏng hành vi xử lý của con người thực.

### Cấu trúc File
- `zalo_userbot_dom_workflow.py`: File python chính để chạy mã kịch bản tự động trên Zalo.
- `zalo_userbot_send_list.csv`: File CSV chứa danh sách Phone Number, Tên, Nội dung cần gửi...
- `zalo_userbot_read_list.csv`: File CSV chứa danh sách Phone Number cần thu thập và đọc tin nhắn.
- `SETUP_GUIDE.md`: Hướng dẫn cài đặt và thiết lập với chi tiết 3 bước đơn giản.

Hãy truy cập [SETUP_GUIDE.md](./SETUP_GUIDE.md) để tiến hành set-up và khởi chạy thư viện nhé!
