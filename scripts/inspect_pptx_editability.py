#!/usr/bin/env python3
from pathlib import Path
import sys, zipfile, re

def main():
    if len(sys.argv) < 2:
        print("Usage: inspect_pptx_editability.py deck.pptx")
        return 2
    pptx = Path(sys.argv[1])
    with zipfile.ZipFile(pptx) as z:
        names = z.namelist()
        slides = [n for n in names if re.match(r"ppt/slides/slide\d+\.xml", n)]
        media = [n for n in names if n.startswith("ppt/media/")]
        charts = [n for n in names if n.startswith("ppt/charts/")]
        tables = 0
        text_runs = 0
        pics = 0
        shapes = 0
        connectors = 0
        warnings = []
        for s in slides:
            xml = z.read(s).decode("utf-8", errors="ignore")
            text_runs += xml.count("<a:t>")
            pics += xml.count("<p:pic")
            shapes += xml.count("<p:sp>")
            connectors += xml.count("<p:cxnSp>")
            tables += xml.count("<a:tbl>")
            # Screenshot-only warning: one or more pictures but too few native/editable objects.
            if xml.count("<p:pic") >= 1 and xml.count("<p:sp>") < 10 and xml.count("<a:t>") < 20 and xml.count("<c:chart") == 0 and xml.count("<a:tbl>") == 0:
                warnings.append(f"{s}: possible screenshot-only slide")
        print(f"slides: {len(slides)}")
        print(f"media: {len(media)}")
        print(f"text_runs: {text_runs}")
        print(f"picture_objects: {pics}")
        print(f"shape_objects: {shapes}")
        print(f"connector_objects: {connectors}")
        print(f"native_charts: {len(charts)}")
        print(f"native_tables: {tables}")
        if warnings:
            print("warnings:")
            for w in warnings:
                print(f"- {w}")
        else:
            print("warnings: none")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
