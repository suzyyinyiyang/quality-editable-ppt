#!/usr/bin/env python3
"""Validate registry JSON files used by quality-editable-ppt.
Usage:
  python scripts/validate_registry.py blueprint file.json
  python scripts/validate_registry.py asset file.json
  python scripts/validate_registry.py chart file.json
  python scripts/validate_registry.py table file.json
"""
import json
import sys
from pathlib import Path

STANDARD_CHARTS = {"donut", "pie", "column", "bar", "line", "area", "radar", "scatter"}
REAL_TABLES = {"data_table", "comparison_table", "risk_list", "asset_list", "capability_matrix"}


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(obj, keys, label):
    return [f"{label}: missing {k}" for k in keys if k not in obj]


def validate_blueprint(data):
    keys = ["slide", "title", "style", "background", "color_blocks", "text_regions", "cards", "charts", "icons", "layer_plan", "complexity_budget"]
    return require(data, keys, "blueprint")


def validate_asset(data):
    errors = []
    for a in data.get("assets", []):
        errors += require(a, ["id", "type", "output"], f"asset {a.get('id', '<unknown>')}")
        if a.get("type") == "full_slide_background" and "forbidden_content" not in a:
            errors.append(f"asset {a.get('id')}: full-slide background should record forbidden_content")
        if a.get("type") == "hero_illustration" and a.get("method") not in {"image_gen_transparent_png", "image2_transparent_png", "image_gen/image2"}:
            errors.append(f"asset {a.get('id')}: complex hero should default to image_gen/image2 transparent PNG")
    return errors


def validate_chart(data):
    charts = data.get("charts", data if isinstance(data, list) else [])
    errors = []
    if not charts:
        errors.append("chart registry: no charts found")
    for c in charts:
        label = f"chart {c.get('chart_id', '<unknown>')}"
        errors += require(c, ["chart_id", "slide", "chart_type", "data_source", "confidence", "implementation"], label)
        if c.get("chart_type") in STANDARD_CHARTS and c.get("confidence") in {"high", "medium"} and c.get("implementation") in {"shape_chart_with_data_file", "png_asset_plus_editable_labels"}:
            errors.append(f"{label}: standard chart with reliable data should prefer native PPT chart when supported")
    return errors


def validate_table(data):
    tables = data.get("tables", data if isinstance(data, list) else [])
    errors = []
    if not tables:
        errors.append("table registry: no tables found")
    for t in tables:
        label = f"table {t.get('table_id', '<unknown>')}"
        errors += require(t, ["table_id", "slide", "table_type", "headers", "rows", "implementation", "confidence"], label)
        if t.get("table_type") in REAL_TABLES and t.get("confidence") in {"high", "medium"} and t.get("implementation") in {"shape_table_with_data_file", "png_asset_plus_editable_labels"}:
            errors.append(f"{label}: real table with reliable data should prefer native PPT table when supported")
    return errors


def main():
    if len(sys.argv) < 3:
        print(__doc__.strip())
        return 2
    kind = sys.argv[1]
    funcs = {"blueprint": validate_blueprint, "asset": validate_asset, "chart": validate_chart, "table": validate_table}
    if kind not in funcs:
        print(f"Unknown registry type: {kind}")
        return 2
    errors = []
    for name in sys.argv[2:]:
        path = Path(name)
        errors.extend([f"{path}: {e}" for e in funcs[kind](load(path))])
    if errors:
        print(f"{kind} validation FAILED")
        for e in errors:
            print("-", e)
        return 1
    print(f"{kind} validation PASSED")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
