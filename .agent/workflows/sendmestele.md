---
description: Kích hoạt toàn bộ quy trình nhận diện ID tự động và gửi tin nhắn Telegram hàng loạt
---

This workflow automatically triggers the unified Python script that fetches new Chat IDs from the Telegram API, appends them to the CSV contact list, and then sends personalized messages to everyone on the list.

// turbo-all
1. Khởi chạy cỗ máy Telegram Auto Workflow kép (Quét Data & Bóp Cò Gửi)
```bash
cd "e:\Antigravity\e-learning\Automatic Notification (Tele-Zalo)\Tele or \Tele (UserBot)"
python telegram_auto_workflow.py
```