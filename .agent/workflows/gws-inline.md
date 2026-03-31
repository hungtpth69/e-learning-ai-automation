---
description: How to use the gws CLI securely and intelligently
---
When the user asks you to interact with Google Workspace (Docs, Drive, etc.) via the `gws` CLI:

1. **TEMPORARY SCRIPT CREATION**: You ARE ALLOWED to create temporary `.py` (Python) or `.js` script files to write logic handling complex `gws` CLI commands (like deleting multiple files, uploading with metadata, parsing errors, etc.).
2. **MANDATORY CLEANUP**: If you create any temporary script to run `gws` commands, you **MUST IMMEDIATELY DELETE** them (along with any temporary `.json` or `.txt` debug files) right after execution. The user absolutely hates clutter and leaving trash in their folder.
3. **INLINE POWERSHELL FOR SIMPLE TASKS**: For short or single interactions, you can still use inline PowerShell. When passing complex JSON, use an environment variable first (e.g., `$env:BODY = '{\"key\": \"val\"}'`) to avoid PowerShell quote stripping.
4. Always prioritize solving the problem effectively, but never leave behind residual script files (`test.py`, `temp.py`, etc.) unless the user explicitly requested specifically formatted reusable source code.
