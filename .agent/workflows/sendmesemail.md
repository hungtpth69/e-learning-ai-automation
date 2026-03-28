---
description: Khởi chạy luồng Agent xuất bản Offer Letter/Marketing qua Gmail ngầm (SMTP)
---
This workflow triggers the Email Automation script which reads the CSV, injects dynamic data into an HTML CSS template, and pushes rich emails via the Google SMTP server (using an App Password).

// turbo-all
1. Khởi chạy luồng Agent Gửi Email Marketing
```bash
cd "e:\Antigravity\e-learning\Email Automation (SMTP)"
python email_auto_workflow.py
```
