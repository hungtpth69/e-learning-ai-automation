---
description: Khởi chạy luồng Agent Gửi Offer Letter (Kèm Đính kèm File) - 10 Ứng Viên
---
This workflow triggers the specialized Demo Offer workflow. It reads a list of 10 candidates, generates HTML emails dynamically mapping specific salary variables, encodes an attachment payload (Onboarding Docs), and pushes all 10 custom emails natively through the SMTP channel.

// turbo-all
1. Kích hoạt luồng Agent Nhận diện trúng tuyển và Gửi Thư Sinh Việc
```bash
cd "e:\Antigravity\e-learning\Email Automation (SMTP)\Demo Offer Letter"
python demo_offer_workflow.py
```
