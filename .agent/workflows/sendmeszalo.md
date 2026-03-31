---
description: Khởi chạy luồng Agent tương tác Zalo (Zalo OA hoặc Zalo Cá Nhân UserBot)
---
Quy trình (Workflow) này hỗ trợ 3 kịch bản tự động hóa Zalo khác nhau tùy theo mục đích sử dụng. Hệ thống Agent sẽ căn cứ vào mong muốn của bạn để kích hoạt lệnh chạy phù hợp:

1. [Trường hợp Zalo OA Doanh Nghiệp] Khởi chạy luồng Gửi tin nhắn qua API ẩn danh:
```bash
cd "e:\Antigravity\e-learning\Automatic Notification (Tele-Zalo)\Zalo"
python zalo_oa_workflow.py
```

2. [Trường hợp Zalo Cá Nhân - Gửi Tin] Khởi chạy luồng DOM giả lập để gửi tin (Sender):
```bash
cd "e:\Antigravity\e-learning\Automatic Notification (Tele-Zalo)\Zalo (UserBot)\Sender"
python zalo_send_workflow.py
```

3. [Trường hợp Zalo Cá Nhân - Đọc Tin] Khởi chạy luồng DOM giả lập để kết xuất tin nhắn (Reader):
```bash
cd "e:\Antigravity\e-learning\Automatic Notification (Tele-Zalo)\Zalo (UserBot)\Reader"
python zalo_read_workflow.py
```
