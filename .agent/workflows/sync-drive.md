---
description: Khởi chạy luồng Agent đồng bộ Data với Google Drive thay vì Google Sheets.
---
This workflow triggers the python agent which utilizes the Google Workspace CLI (gws) to seamlessly fetch files from Google Cloud Storage, process them locally, and push the updated structure straight back synchronously.

// turbo-all
1. Kích hoạt luồng Agent quét Google Drive
```bash
cd "e:\Antigravity\e-learning\Google Sheets Automation (Data Center)"
python gdrive_workflow.py
```
