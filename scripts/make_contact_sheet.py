#!/usr/bin/env python3
from pathlib import Path
import sys, math
try:
    from PIL import Image, ImageDraw
except ImportError:
    print("Pillow required: pip install pillow", file=sys.stderr)
    raise

def main():
    if len(sys.argv) < 3:
        print("Usage: make_contact_sheet.py output.png image1 image2 ...")
        return 2
    out = Path(sys.argv[1])
    images = [Image.open(p).convert("RGB") for p in sys.argv[2:]]
    tw, th = 420, 236
    cols = min(3, len(images)) or 1
    rows = math.ceil(len(images) / cols)
    margin, label_h = 18, 28
    sheet = Image.new("RGB", (cols*(tw+margin)+margin, rows*(th+label_h+margin)+margin), "white")
    d = ImageDraw.Draw(sheet)
    for i, img in enumerate(images):
        thumb = img.resize((tw, th))
        x = margin + (i % cols)*(tw+margin)
        y = margin + (i // cols)*(th+label_h+margin)
        sheet.paste(thumb, (x,y))
        d.text((x, y+th+6), f"{i+1:02d}", fill=(0,0,0))
    out.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out)
    print(out)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
