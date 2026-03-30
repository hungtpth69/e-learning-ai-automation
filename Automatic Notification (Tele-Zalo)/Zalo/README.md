# 💬 Hướng Dẫn Kích Hoạt (Demo Usecase): Zalo OA Notification

> **Tình Huống Sử Dụng (Usecase): Gửi Tin Nhắn Chăm Sóc Hàng Loạt**
> Giả định phòng Nhân sự (HR) cần gửi thông báo Lịch Hoạt Động hoặc Lương Thưởng nội bộ tới 300 nhân viên đã "Quan Tâm" trang Zalo OA của công ty. Hoặc một đội ngũ Sales cần Broadcast bản cập nhật khóa học mới.
> Sau khi đã liên kết cổng API (Xem `SETUP_GUIDE.md`), Agent của bạn có thể vận hành luồng xả tin tự động, xử lý 300 tin nhắn chỉ trong vòng hơn 1 phút.

---

## 🎯 Luồng Hoạt Động (Cơ Chế Thay Thế Nút Truyền Thống)
Thông thường với Zalo OA, bộ phận nhân sự phải đăng nhập tài khoản Zalo, chọn chức năng Broadcast và gặp nhiều trở ngại với giới hạn hiển thị.
Nhưng với Trí Tuệ Nhân Tạo (AI Agent):
- Agent sẽ nạp file danh sách của bạn (VD: Ai là Sale, ai là Marketing).
- Agent gọi thẳng vào Lõi Máy Chủ Zalo (Zalo API) để ném lên lệnh Gửi riêng lẻ từng người. Nhạc điệu là mỗi tin mang một Tên gọi chuyên biệt (Cá nhân hóa). Đảm bảo thông báo điện thoại chớp lên liên tục.

---

## 🛠 Chuẩn Bị (Nạp "Đạn" Dữ Liệu)
> **⚠️ QUY TẮC HIỂN THỊ ID DUY NHẤT TRÊN ZALO:**
> Bạn không thể gửi tin Zalo dựa trên Số Điện Thoại để phòng chống rủi ro bảo mật thông tin.
> Thay vào đó, Zalo cấp cho mỗi khách hàng/nhân sự một dải số duy nhất (Zalo User ID) ví dụ `549210341829...`.

1. Khởi tạo danh bạ Zalo ở file mẫu `zalo_contact_list.csv`. Điền chuẩn xác `Zalo_User_ID` và tên của nhân sự nhận tin.
2. Thiết kế đoạn thông báo của mình tại file `message_template.txt`. Hãy giữ cho tin nhắn ngắn gọn, có gạch đầu dòng rõ ràng để người dùng Zalo xem được trọn vẹn trên màn hình bé của điện thoại.

*(Để chạy luồng thực tiễn, máy cần có bộ thư viện chuẩn của bộ môn Lập trình mạng. Nếu bạn có thông báo lỗi thư viện, hãy chạy lệnh `pip install requests` hoặc nhờ Agent làm việc này thay bạn).*

---

## 🚀 Kích Hoạt Luồng AI (Execute)
Khi dữ liệu Data đã nạp, hãy triệu hồi trợ lý tự động bằng một dòng lệnh cực kỳ tinh giản:
```bash
/sendmeszalo
```

Khi nhấn phím Enter, hãy gác tay lên bàn quan sát. Trợ lý Bot sẽ quét mọi dòng trong file `.csv`, tích hợp vào API của Zalo OA và "bắn" thông báo. 
Một dải log `Code 200 - OK` sẽ chạy dọc màn hình, báo hiệu tin nhắn nội bộ của bạn đã đáp xuống điện thoại từng cá nhân thật mượt mà. Đội ngũ nhân sự bạn sẽ thật ngạc nhiên về tốc độ này!
