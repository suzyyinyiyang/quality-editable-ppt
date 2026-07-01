# GitHub Publishing Checklist

This package keeps the Skill workflow and constraints unchanged. The added files are repository housekeeping files only: `.gitignore`, `.gitattributes`, and this checklist/security note.

## Suggested publish steps

1. Create a new GitHub repository.
2. Upload the contents of this folder, not the parent zip file.
3. Confirm that `SKILL.md`, `README.md`, `MANIFEST.md`, `workflows/`, `quality-control/`, `templates/`, `style-profiles/`, `agents/`, `assets/`, and `scripts/` are present.
4. Run local validation:

```bash
python scripts/validate_skill_package.py .
```

5. Check GitHub's file list before publishing to ensure no private PPT files, screenshots, generated outputs, local logs, or customer materials were included.
6. Choose a license only after the repository owner confirms the desired usage scope. No open-source license is added by default to avoid changing redistribution/commercial-use rights.

## Repository description suggestion

High-fidelity editable PowerPoint reconstruction Skill for Codex/ChatGPT workflows, with preview-lock reconstruction, native editable charts/tables, asset handling, and QA gates.
