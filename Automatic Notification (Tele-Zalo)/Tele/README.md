# 📱 Telegram Bot Marketing System

> **Cỗ Máy Bắn Tin Nhắn Hàng Loạt Qua Telegram**
> Cách chuyên nghiệp để quản lý và bắn tin nhắn Chăm Sóc Khách Hàng (CSKH) hay Cập nhật Khóa Học tới hàng nghìn học viên thông qua Bot mà không cần còng lưng Copy/Paste từ nick cá nhân.

## 🎯 Mục Đích Hoạt Động
Bạn sẽ thiết lập Cỗ máy tự động (`telegram_auto_workflow.py`). Nhờ Trí tuệ tự động, bất cứ ai từng chat với Bot của bạn, hệ thống này có thể lưu mã định danh (Danh bạ ngầm), và phát thanh Broadcast một kịch bản tới tất cả mọi người cùng một lúc chỉ với một lệnh Enter.

## 🛠 Hướng Dẫn Khai Sinh Bot Telegram Từng Bước (Cho Non-Tech)

Trong thế giới viễn thông này, bạn cần phải xin Trung tâm Telegram đẻ cho mình một con Robot. Hoàn toàn miễn phí, hãy làm như sau:
1. Mở ứng dụng **Telegram** trên Điện thoại iPhone/Android hoặc Máy tính (Bắt buộc phải Login Sẵn tài khoản chính chủ).
2. Tại thanh tìm kiếm (Biểu tượng Màn Kính Lúp), gõ chính xác: `@BotFather`.
3. Bạn sẽ thấy 1 con Bot tên BotFather có hình tích Xanh Dương uy tín. Bấm thẳng vào nó và chọn nút **Start** (Hoặc bắt đầu).
4. Gõ dòng lệnh này gửi cho Cha Bot: `/newbot`. Nó sẽ Rep lại: *"Alright, a new bot. How are we going to call it?"*
5. Nó hỏi tên Bot, bạn gõ luôn **Tên Bot bạn cực ưng** gởi đi (Ví dụ: `Trung Tâm Anh Ngữ AG` hoặc `Bot Chăm Sóc Lớp Học`).
6. Nó sẽ hỏi Username. Đây mới là tên Tên miền chuẩn của Bot. Phải viết Không dấu, dính liền, và BẮT BUỘC đuôi kết thúc là `bot`. Gõ ngay (Ví dụ: `ChamSoc_Ag_bot`) và ném vào.
7. BÙM!! Telegram sẽ rải tiền màn hình đoạn text dài: *"Done! Congratulations on your new bot..."*. Bạn chú ý sẽ thấy 1 dòng quan trọng bôi đậm: **`Use this token to access the HTTP API:`**.
8. Ngay dưới dòng giới thiệu đó DÒNG TOKEN BẢO MẬT màu Đỏ Đỏ (Ví dụ chữ xanh/đỏ: `123456789:AAH_Fdk3ls91l24...`). 
9. **CHÉP (COPY) CHẶT Dòng Mã Này.** Đây là thứ phần mềm Bot rất khát. Tuyệt đối không để rò rỉ kẻo người khác Hack mất Bot.

## ⚙️ Cấu Hình Khởi Chạy
Để tránh rò rỉ mã Token ra ngoài mạng Internet, hệ thống sử dụng cơ chế bảo quản bằng File Text Tĩnh (`.txt`).
1. Trong thư mục chạy code này có sẵn file mẫu `telegram_token.txt`.
2. Dùng con chuột Mở file `telegram_token.txt` bé con này bằng Notepad và dán Dòng Điện Token Thần Thánh vào. (Cứ paste chay 1 dòng vào, VD: `123456789:AAH_Fdk3ls91l2...`).
3. Mở file báo cáo `tele_contact_list.csv` (File Excel Data) và thêm tên Khách hàng mục tiêu của bạn.

*(Về phần yêu cầu kĩ thuật, hãy chắc chắn Python của bạn đã cài đặt công cụ HTTP bằng lệnh: `pip install requests`)*

*👉 Chú Ý Khắc Cốt Ghi Tâm Tránh Ngược Đời: Telegram cấm SPAM người lạ. Vì vậy, Khách Hàng Bắt Buộc Phải Ấn START với Bot Của Cty Lần Đầu Việc Bạn Triển Khai! Bạn gửi tên Con Bot (`@ChamSoc_Ag_bot`) vào Group Zalo để Học viên tự Nhấn Start đăng ký trước 1 lần nhé.*

## 🚀 Hướng Dẫn Kích Hoạt Automation
Để tiến hành nhắn tin quảng cáo tự động đến tay các học viên đã Start, bạn gõ vào Terminal Tool Lệnh Đại Bác:
```
/sendmestele
```

## 📊 Hệ Thống Hoạt Động Cụ Thể Thế Nào?
Quá trình này bùng phát 2 giai đoạn mượt mà:
1. **[Giai đoạn 1] Vét Dữ Liệu (Data Fetching)**: Thuật toán gọi API `getUpdates` để tìm kiếm List mã ID định danh của những người đã ấn "Start". Bạn không cần tự tay tra ID người dùng siêu cực khổ như Data cũ.
2. **[Giai đoạn 2] Xả Đạn (Notification Execute)**: Nó Map ID lượm được vào tên Khách hàng. Nó tự soạn Tin nhắn nội dung "Chào anh abc..." và nã lệnh `sendMessage` thẳng qua mạng cáp quang. Vặn trễ Timer 1s/1 người để tránh bị Telegram treo cổ do BOT SPAM. Mượt như lụa.
