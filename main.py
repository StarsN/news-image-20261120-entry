#!/usr/bin/env python3
"""THE WORLD IN ONE PICTURE — Friday 20 November 2026.

Draws a 1024x1024 newspaper front page summing up the day's world news.
Every word is rendered as vector type with PIL; there is no generated
imagery, so nothing can come out garbled. Layout flows from measured
text heights, so blocks can never overlap. Output is deterministic:
the same bytes on every run.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (250, 247, 239)
INK = (24, 24, 26)
MUTE = (84, 84, 88)
RED = (168, 44, 32)
SLATE = (43, 74, 96)
GOLD = (176, 132, 44)
PANEL = (240, 234, 220)
CARD = (255, 253, 248)

FONT_DIR = "/usr/share/fonts/truetype/noto"
SERIF_B = os.path.join(FONT_DIR, "NotoSerif-Bold.ttf")
SANS_B = os.path.join(FONT_DIR, "NotoSans-Bold.ttf")
SANS_SB = os.path.join(FONT_DIR, "NotoSans-SemiBold.ttf")
SANS_R = os.path.join(FONT_DIR, "NotoSans-Regular.ttf")


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def block(draw, x, y, text, fnt, max_w, leading, fill=INK):
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def kick(draw, x, y, text, color, size=19):
    draw.text((x, y), text, font=font(SANS_B, size), fill=color)
    return y + size + 8


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
MX = 38
RIGHT = W - MX
CW = RIGHT - MX  # 948

# ---------------------------------------------------------------- masthead
d.line([(MX, 26), (RIGHT, 26)], fill=INK, width=3)
title = "THE WORLD IN ONE PICTURE"
tf = font(SERIF_B, 63)
d.text(((W - d.textlength(title, font=tf)) / 2, 40), title, font=tf, fill=INK)
d.line([(MX, 122), (RIGHT, 122)], fill=INK, width=5)
d.line([(MX, 131), (RIGHT, 131)], fill=INK, width=1)
date = "FRIDAY 20 NOVEMBER 2026"
df = font(SANS_B, 31)
d.text(((W - d.textlength(date, font=df)) / 2, 143), date, font=df, fill=INK)
side_f = font(SANS_SB, 16)
d.text((MX, 151), "ONE DAY'S WORLD NEWS", font=side_f, fill=MUTE)
r = "IN A SINGLE PAGE"
d.text((RIGHT - d.textlength(r, font=side_f), 151), r, font=side_f, fill=MUTE)
d.line([(MX, 184), (RIGHT, 184)], fill=INK, width=2)

# ---------------------------------------------------------------- lead
y = 198
y = kick(d, MX, y, "THE HAGUE — WORLD COURT", RED)
hf = font(SERIF_B, 44)
# display leading: 50/44 (~1.14x) — tighter than body ratios, as
# headlines are set in print, and it buys air for the foot of the page
y = block(d, MX, y,
          "World Court: Myanmar committed genocide against the Rohingya",
          hf, CW, 50)
y += 8
# scales glyph panel at right of the lead body
GW, GH = 252, 96
GX, GY = RIGHT - GW, y
d.rectangle([GX, GY, GX + GW, GY + GH], fill=PANEL, outline=INK, width=2)
cx = GX + GW // 2
d.line([(cx, GY + 10), (cx, GY + 58)], fill=SLATE, width=5)
d.line([(cx - 46, GY + 20), (cx + 46, GY + 20)], fill=SLATE, width=5)
for sgn in (-1, 1):
    px = cx + sgn * 46
    d.line([(px, GY + 20), (px - 14, GY + 52)], fill=SLATE, width=3)
    d.line([(px, GY + 20), (px + 14, GY + 52)], fill=SLATE, width=3)
    d.arc([px - 17, GY + 44, px + 17, GY + 66], start=0, end=180, fill=SLATE, width=4)
d.rectangle([cx - 27, GY + 58, cx + 27, GY + 64], fill=SLATE)
cap = "THE ICJ · THE HAGUE"
cf = font(SANS_B, 13)
d.text((GX + (GW - d.textlength(cap, font=cf)) / 2, GY + 74), cap, font=cf, fill=SLATE)
lead_body = (
    "The International Court of Justice rules that Myanmar's military "
    "waged a campaign of genocide against the Rohingya in 2017 — the "
    "first time the court has found a state committed genocide.")
y_body = block(d, MX, y, lead_body, font(SANS_R, 20), GX - MX - 24, 27)
y = max(y_body, GY + GH) + 12
d.line([(MX, y), (RIGHT, y)], fill=INK, width=2)
y += 14

# ---------------------------------------------------------------- row 2
COLW = (CW - 30) // 2
RX = MX + COLW + 30
hf2 = font(SERIF_B, 30)
bf2 = font(SANS_R, 19)
# left column: summit
yl = kick(d, MX, y, "SHENZHEN — APEC SUMMIT", SLATE)
yl = block(d, MX, yl,
           "Trump, Xi, Putin end summit with peace declaration", hf2, COLW, 37)
yl += 4
yl = block(d, MX, yl,
           "The first US–China–Russia leaders' meeting closes on four "
           "points: nuclear-risk talks, UN reform, curbing the ICC, "
           "steady energy. No Ukraine deal.",
           bf2, COLW, 25)
# right column: markets
yr = kick(d, RX, y, "MARKETS — GLOBAL SELL-OFF", RED)
yr = block(d, RX, yr,
           "AI doubts drag stocks lower: Nikkei -4.8%", hf2, COLW, 37)
yr += 4
yr = block(d, RX, yr,
           "The S&P 500 falls 2%, a fifth straight day, as investors "
           "question AI valuations. Gold slides 4.2%; Anthropic's "
           "Nasdaq debut jumps 17% but tech stays down.",
           bf2, COLW, 25)
y = max(yl, yr) + 12
d.line([(MX, y), (RIGHT, y)], fill=INK, width=1)
y += 12

# ---------------------------------------------------------------- row 3 cards
cards = [
    ("RIYADH — MIDDLE EAST", RED,
     "Houthi missiles hit wealth-fund tower",
     "Missiles damage Riyadh's Public Investment Fund tower. "
     "Tanker attacks intensify in Hormuz; Israeli troops cross "
     "Gaza's Yellow Line."),
    ("KYIV — UKRAINE WAR", SLATE,
     "Embassies damaged in Kyiv barrage",
     "A daytime Russian barrage blows out windows at the Austrian "
     "and Dutch embassies, damages a cathedral. Brussels summons "
     "Moscow's envoy."),
    ("ANTALYA — COP31 CLIMATE", GOLD,
     "Climate deal drops fossil-fuel exit",
     "Negotiators strip fossil-fuel phase-out from the draft as "
     "the summit wraps. Pacific nations call the text an outrage."),
]
CW3 = (CW - 24) // 3
hf3 = font(SERIF_B, 24)
bf3 = font(SANS_R, 15)
# measure first so all three boxes share one height
measured = []
for kick_t, color, head, body in cards:
    hl = wrap(d, head, hf3, CW3 - 28)
    bl = wrap(d, body, bf3, CW3 - 28)
    measured.append((hl, bl))
card_h = 14 + 24 + len(max(measured, key=lambda m: len(m[0]))[0]) * 29 + 3 \
    + len(max(measured, key=lambda m: len(m[1]))[1]) * 20 + 12
for i, (kick_t, color, head, body) in enumerate(cards):
    x = MX + i * (CW3 + 12)
    d.rectangle([x, y, x + CW3, y + card_h], fill=CARD, outline=(200, 194, 178), width=1)
    d.rectangle([x, y, x + CW3, y + 6], fill=color)
    yy = kick(d, x + 14, y + 13, kick_t, color, size=16)
    for line in measured[i][0]:
        d.text((x + 14, yy), line, font=hf3, fill=INK)
        yy += 29
    yy += 3
    for line in measured[i][1]:
        d.text((x + 14, yy), line, font=bf3, fill=INK)
        yy += 20
y += card_h + 10

# ---------------------------------------------------------------- row 4 minis
# set slightly tighter (10px rule gap, 23px leading) so the closing
# stories end with clear air above the ticker bar instead of crowding it
HALF = (CW - 24) // 2
bf4 = font(SANS_R, 18)
ym = kick(d, MX, y, "KENYA — HEALTH", SLATE, size=17)
block(d, MX, ym,
      "Last Ebola patient goes home in Nairobi — discharged 37 days "
      "after the country's first case.", bf4, HALF, 23)
x2 = MX + HALF + 24
ym2 = kick(d, x2, y, "GAMES — RECORD LAUNCH", RED, size=17)
y_end = block(d, x2, ym2,
              "GTA 6 earns $2.36bn in one day: 24.6m copies, an "
              "entertainment record (Sensor Tower est.).",
              bf4, HALF, 23)
print("content ends at y =", y_end, "(ticker starts 972)")

# ---------------------------------------------------------------- ticker
TY = 972
d.rectangle([0, TY, W, H], fill=INK)
items = ["WHITE HOUSE FIRES CYBER DIRECTOR",
         "BEPICOLOMBO REACHES MERCURY",
         "SUDAN GOLD-MINE STRIKE KILLS 10",
         "GEORGIA GAS BLAST KILLS 6"]
tkf = font(SANS_B, 14)
tick = "  ·  ".join(items)
while d.textlength(tick, font=tkf) > W - 24 and len(items) > 1:
    items.pop()
    tick = "  ·  ".join(items)
tw2 = d.textlength(tick, font=tkf)
d.text(((W - tw2) / 2, TY + 19), tick, font=tkf, fill=(250, 247, 239))

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
img.save(os.path.join(out_dir, "entry.png"))
print("wrote", os.path.join(out_dir, "entry.png"))
