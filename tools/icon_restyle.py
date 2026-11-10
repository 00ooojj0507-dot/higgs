"""Restyle open-source line icons (Lucide) into the Navy Retro reel style.

- Ivory stroke, round caps/joins, stroke width scaled so it lands at 10–14px on a 1080-wide frame.
- Chosen closed shapes get a solid accent fill (one accent per reel).
- Small dot details are filled ivory; nothing else (no gradients, shadows, glow).

Usage:
    # one icon -> transparent PNG
    python tools/icon_restyle.py icon user --size 360 --fill 1 --accent yuzu -o outputs/user.png

    # sample sheet (1080x1920, navy background)
    python tools/icon_restyle.py sheet --accent yuzu -o outputs/icon_sheet.png

--fill takes indexes of the drawable elements in the SVG (0-based, in file order).
Run `python tools/icon_restyle.py list user` to see them.
"""
import argparse
import io
import os
import re
import xml.etree.ElementTree as ET
from pathlib import Path

import cairosvg
from PIL import Image, ImageDraw, ImageFont

ICON_DIR = Path(__file__).resolve().parent.parent / "assets" / "icons" / "lucide"

NAVY = "#11192D"
PANEL = "#222F4C"
IVORY = "#F4EEDC"
ACCENTS = {"yuzu": "#F2C230", "custard": "#F3D68C", "soft-red": "#E2614A"}

STROKE_PX = 12  # target stroke width on the 1080-wide frame
SHAPES = {"path", "circle", "rect", "line", "polyline", "polygon", "ellipse"}

# Sample sheet: icon name -> element indexes filled with the accent
SHEET = [
    ("user", [1]),
    ("eye", [1]),
    ("sun", [0]),
    ("moon", [0]),
    ("star", [0]),
    ("clock", [0]),
    ("lightbulb", [0]),
    ("book-open", []),
    ("palette", [4]),
    ("frame", []),
    ("building-2", [0]),
    ("hand", []),
]

ET.register_namespace("", "http://www.w3.org/2000/svg")


def _tag(el):
    return el.tag.split("}")[-1]


def drawables(root):
    return [el for el in root.iter() if _tag(el) in SHAPES]


def restyle_svg(name, size, fill_idx, accent):
    root = ET.fromstring(re.sub(r"<!--.*?-->", "", (ICON_DIR / f"{name}.svg").read_text(), flags=re.S))
    for attr in ("class", "width", "height"):
        root.attrib.pop(attr, None)
    # pad the viewBox so thick strokes aren't clipped
    root.set("viewBox", "-2 -2 28 28")
    root.set("width", str(size))
    root.set("height", str(size))
    sw = STROKE_PX * 28 / size
    root.set("stroke", IVORY)
    root.set("stroke-width", f"{sw:.3f}")
    root.set("stroke-linecap", "round")
    root.set("stroke-linejoin", "round")
    root.set("fill", "none")
    dots = []
    for i, el in enumerate(drawables(root)):
        if el.get("fill") == "currentColor":
            dots.append(el)
        elif i in fill_idx:
            el.set("fill", accent)
    # tiny dot details: drawn last, as navy cutouts on a filled icon or ivory dots otherwise
    for el in dots:
        root.remove(el)
        el.set("fill", NAVY if fill_idx else IVORY)
        el.set("stroke", "none")
        el.set("r", "1.3")
        root.append(el)
    return ET.tostring(root, encoding="unicode")


def render_icon(name, size, fill_idx, accent):
    png = cairosvg.svg2png(bytestring=restyle_svg(name, size, fill_idx, accent).encode())
    return Image.open(io.BytesIO(png)).convert("RGBA")


def find_font(weight="ExtraBold"):
    candidates = [
        os.environ.get("PRETENDARD_DIR", ""),
        str(Path(__file__).resolve().parent.parent / "fonts"),
    ]
    for d in candidates:
        p = Path(d) / f"Pretendard-{weight}.otf"
        if d and p.exists():
            return str(p)
    return None


def build_sheet(accent, out):
    W, H = 1080, 1920
    img = Image.new("RGB", (W, H), NAVY)
    draw = ImageDraw.Draw(img)

    font_path = find_font()
    if font_path:
        title = ImageFont.truetype(font_path, 64)
        small = ImageFont.truetype(find_font("SemiBold") or font_path, 30)
        t1, t2 = "아이콘 ", "스타일 샘플"
        w1 = draw.textlength(t1, font=title)
        w2 = draw.textlength(t2, font=title)
        x = (W - w1 - w2) / 2
        draw.text((x, 150), t1, font=title, fill=IVORY)
        draw.text((x + w1, 150), t2, font=title, fill=accent)
    else:
        small = None

    # grid inside safe zone: x 120..930, y 280..1280
    cols, rows = 3, 4
    left, right, top, bottom = 120, 930, 280, 1280
    cw, ch = (right - left) / cols, (bottom - top) / rows
    icon = 170
    for k, (name, fills) in enumerate(SHEET):
        r, c = divmod(k, cols)
        ic = render_icon(name, icon, set(fills), accent)
        cx = left + cw * c + cw / 2
        cy = top + ch * r + ch / 2 - (16 if small else 0)
        img.paste(ic, (int(cx - icon / 2), int(cy - icon / 2)), ic)
        if small:
            tw = draw.textlength(name, font=small)
            draw.text((cx - tw / 2, cy + icon / 2 + 2), name, font=small, fill="#A9AFC0")

    # palette strip
    sw_y = 1340
    for i, col in enumerate([NAVY, PANEL, IVORY, accent]):
        x0 = 120 + i * 205
        draw.rounded_rectangle((x0, sw_y, x0 + 180, sw_y + 60), radius=18, fill=col,
                               outline=IVORY if col == NAVY else None, width=4)

    Path(out).parent.mkdir(parents=True, exist_ok=True)
    img.save(out)
    print(f"saved {out}")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_icon = sub.add_parser("icon")
    p_icon.add_argument("name")
    p_icon.add_argument("--size", type=int, default=360)
    p_icon.add_argument("--fill", type=int, nargs="*", default=[])
    p_icon.add_argument("--accent", choices=ACCENTS, default="yuzu")
    p_icon.add_argument("-o", "--out", required=True)

    p_sheet = sub.add_parser("sheet")
    p_sheet.add_argument("--accent", choices=ACCENTS, default="yuzu")
    p_sheet.add_argument("-o", "--out", default="outputs/icon_sheet.png")

    p_list = sub.add_parser("list")
    p_list.add_argument("name")

    a = ap.parse_args()
    if a.cmd == "icon":
        img = render_icon(a.name, a.size, set(a.fill), ACCENTS[a.accent])
        Path(a.out).parent.mkdir(parents=True, exist_ok=True)
        img.save(a.out)
        print(f"saved {a.out}")
    elif a.cmd == "sheet":
        build_sheet(ACCENTS[a.accent], a.out)
    else:
        root = ET.fromstring(re.sub(r"<!--.*?-->", "", (ICON_DIR / f"{a.name}.svg").read_text(), flags=re.S))
        for i, el in enumerate(drawables(root)):
            print(i, _tag(el), {k: v for k, v in el.attrib.items()})


if __name__ == "__main__":
    main()
