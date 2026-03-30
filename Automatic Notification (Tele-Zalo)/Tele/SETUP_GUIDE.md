# ⚙️ Hướng Dẫn Cài Đặt Telegram Bot (Setup Guide)

Để trợ lý AI có thể tự động gửi tin nhắn qua Telegram, bạn cần tạo một "Tài khoản Bot" miễn phí trên Telegram. Quá trình này rất nhanh và an toàn, thực hiện ngay trên ứng dụng Telegram của bạn.

---

## Bước 1: Khai Báo Bot Mới Với BotFather
1. Mở ứng dụng **Telegram** trên điện thoại hoặc máy tính.
2. Tại thanh tìm kiếm (biểu tượng kính lúp), gõ chính xác: `@BotFather` (Lưu ý: Chọn nick có dấu tích xanh dương uy tín).
3. Bấm vào BotFather và chọn **Start** (Bắt đầu).
4. Gõ lệnh khởi tạo gửi cho Bot: `/newbot`.
5. Bot sẽ yêu cầu bạn đặt tên cho Bot (Tên hiển thị với khách hàng). VD: `Bot Thông Báo Công Ty AG`.
6. Tiếp theo, Bot yêu cầu đặt **Username** (Tên đăng nhập không dấu, viết liền và bắt buộc phải kết thúc bằng chữ `bot`). VD: `ThongBao_AG_bot`.

## Bước 2: Lấy Mã Bảo Mật (Token API)
1. Ngay khi tạo thành công, BotFather sẽ gửi một tin nhắn chúc mừng dài. 
2. Hãy tìm dòng chữ **`Use this token to access the HTTP API:`**. Ngay phía dưới là dòng mã màu đỏ (Ví dụ: `123456789:AAH_Fdk3ls91l24...`). 
3. Đây là **Mã Token** bảo mật cấp quyền điều khiển Bot. Hãy sao chép (Copy) toàn bộ chuỗi mã này. *Lưu ý: Không bao giờ chia sẻ mã này cho người lạ để tránh bị mất quyền điều khiển Bot.*

## Bước 3: Cấu Hình Token Vào Hệ Thống
Để hệ thống AI có thể kết nối với Bot vừa tạo:
1. Trong thư mục `Tele` của dự án, mở file có tên `telegram_token.txt` bằng phần mềm Notepad.
2. Dán đoạn mã Token bạn vừa copy ở Bước 2 vào file này (Chỉ dán chuỗi chữ số, không xuống dòng, không thêm ký tự lạ).
3. Lưu (Save) file lại.

---

🎉 **Hoàn tất Cài đặt!** Trở lại file `README.md` để xem hướng dẫn sử dụng (Usage) và cách kích hoạt luồng tự động.
