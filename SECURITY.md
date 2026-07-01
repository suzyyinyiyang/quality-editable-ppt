# Security Notes

This repository is a ChatGPT/Codex Skill package for generating high-visual, editable PowerPoint files.

## Expected behavior

- The Skill itself is prompt/workflow documentation plus local helper scripts.
- Helper scripts are intended for local validation and PPT/package inspection.
- The package does not require background services, system daemons, drivers, launch agents, cron jobs, or elevated privileges.
- The package should be used inside a project/workspace directory.

## Before publishing updates

Before pushing new changes to a public repository, check that the repository does not include:

- API keys, tokens, passwords, private keys, cookies, or credentials.
- Customer files, proprietary source slides, internal screenshots, meeting notes, logs, or private assets.
- Absolute local paths that expose usernames or internal directories.
- Generated PPT/render artifacts unless they are intentionally sanitized examples.
- macOS metadata such as `__MACOSX/`, `.DS_Store`, or `._*` files.

## Reporting issues

If you find a security issue in this Skill package, open a private security advisory or contact the repository owner through the preferred GitHub contact method.
