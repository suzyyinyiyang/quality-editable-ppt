#!/usr/bin/env python3
from pathlib import Path
import sys

REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "MANIFEST.md",
    "agents/openai.yaml",
    "workflows/WORKFLOW.md",
    "workflows/RECONSTRUCTION_RULES.md",
    "workflows/QA_AND_CONFIRMATION.md",
    "style-profiles/STYLES.md",
    "templates/BLUEPRINT_TEMPLATE.md",
    "templates/REGISTRY_TEMPLATES.md",
    "templates/ASSET_PROMPT_TEMPLATES.md",
    "templates/QA_REPORT_TEMPLATES.md",
    "quality-control/CHECKLISTS.md",
    "quality-control/QUALITY_GATES.md",
    "scripts/validate_skill_package.py",
    "scripts/validate_registry.py",
    "scripts/make_contact_sheet.py",
    "scripts/inspect_pptx_editability.py",
    "examples/EXAMPLES.md",
]

REQUIRED_PHRASES = [
    "description:",
    "90%+",
    "Restored Detail-Replica Core",
    "Screenshot-Only Output Rejection",
    "Primary Asset and Component Reconstruction Rules",
    "Full Background Asset Rule",
    "Hero Asset Edge Blending Rule",
    "Icon Reconstruction Rule",
    "Native Table Styling Rule",
    "Micro Chart and Sparkline Reconstruction Rule",
    "Card and Component Box Model Rule",
    "Quick Outline Confirmation",
    "Page Information Structure and Visual Strategy",
    "Optional Asset Confirmation",
    "Editable Fidelity Delivery Gate",
    "Background Integration Strategy",
    "Card Color Sampling Rule",
    "Icon Badge Registry",
    "Native Table Reconstruction Rule",
    "Chart Reconstruction Rule",
    "Hero Illustration Fallback",
    "Asset Seamless Integration Check",
    "蓝绿产品发布风",
    "蓝黑科技运营风",
    "紫色科技色块风",
    "紫蓝AI科技风",
    "深蓝深红攻防风",
    "深灰绿色监控风",
    "深灰金色年会风",
    "自动推荐",
    "Micro Icon, Card, and Text Precision Lock",
    "Editable Text Position Anchor Rule",
]
def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    errors = []
    for f in REQUIRED_FILES:
        if not (root / f).is_file():
            errors.append(f"missing required file: {f}")
    skill = root / "SKILL.md"
    if skill.exists():
        text = skill.read_text(encoding="utf-8")
        for phrase in REQUIRED_PHRASES:
            if phrase not in text:
                errors.append(f"SKILL.md missing phrase: {phrase}")
        if "name: quality-editable-ppt" not in text:
            errors.append("SKILL.md missing correct name")
    # Ensure old clutter has not been packaged
    for bad in ["__pycache__", ".DS_Store"]:
        if any(bad in str(p) for p in root.rglob("*")):
            errors.append(f"package contains {bad}")
    if errors:
        print("Skill package validation FAILED")
        for e in errors:
            print("-", e)
        return 1
    print("Skill package validation PASSED")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
