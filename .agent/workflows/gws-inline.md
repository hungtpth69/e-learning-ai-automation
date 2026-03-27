---
description: How to use the gws CLI securely and inline
---
When the user asks you to interact with Google Workspace (Docs, Drive, etc.) via the `gws` CLI:

1. **NEVER** create temporary `.js`, `.py`, or `.ps1` script files to run these commands. The user hates this as it clutters up their Temp directory.
2. **ALWAYS** use inline PowerShell commands via `run_command`.
3. To safely pass complex JSON with double quotes to `gws` in PowerShell without breaking the escape characters, ALWAYS use an environment variable first, using single quotes for the outer definition, double single quotes `''` to represent inner single quotes, and `\` for double quotes.
4. **Example structure**:
   ```powershell
   $env:QUERY = '{\"q\": \"fileExtension=''apk'' and trashed=false\"}'
   gws drive files list --params $env:QUERY
   ```
5. Use exactly this pattern for every `gws` interaction to ensure it securely bypasses PowerShell quote stripping and keeps the user's computer clean.
