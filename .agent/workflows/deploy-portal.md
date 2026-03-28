---
description: Tự động khởi tạo Repository và Đẩy mã nguồn Web lên Github
---
This workflow triggers the Github Automation Agent. It utilizes local `git` combined with `gh` (Github CLI) to orchestrate local staging, remote repository creation, and code pushing directly to the cloud without manual user interaction.

// turbo-all
1. Kích hoạt luồng Agent Đẩy Code Github (Deploy Portal)
```bash
cd "e:\Antigravity\e-learning\Internal Portal (Vercel Deploy)"
python deploy_portal.py
```
