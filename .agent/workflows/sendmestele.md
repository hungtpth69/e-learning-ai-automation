---
description: Khởi chạy luồng Agent tương tác Telegram (Bot API hoặc Tài khoản cá nhân UserBot)
---
Quy trình (Workflow) này hỗ trợ 2 kịch bản tự động hóa Telegram khác biệt. Tùy thuộc vào yêu cầu của bạn, hệ thống Agent sẽ chọn lệnh khởi chạy phù hợp:

1. [Trường hợp Telegram Bot] Khởi chạy luồng tự động lấy ID và gửi tin bằng Bot Token:
```bash
cd "e:\Antigravity\e-learning\Automatic Notification (Tele-Zalo)\Tele"
python telegram_auto_workflow.py
```

2. [Trường hợp Telegram Cá Nhân UserBot] Khởi chạy luồng gửi tin nhắn bằng tài khoản chính chủ qua Telethon:
```bash
cd "e:\Antigravity\e-learning\Automatic Notification (Tele-Zalo)\Tele (UserBot)"
python telegram_userbot_workflow.py
```