#!/usr/bin/env python3
"""
Render data/contributions.json (from fetch_contributions.py) as a GitHub-style
contribution heatmap in the README's navy and sky-blue palette.

Cells slide in once, left to right and top to bottom, then hold. Colour levels
are GitHub's own (data-level 0-4 from the profile calendar), so the graph matches
what GitHub shows. Animations turn off under prefers-reduced-motion.

    python scripts/render_heatmap_svg.py            # animated
    STATIC=1 python scripts/render_heatmap_svg.py   # final frame, for screenshots
"""
import datetime
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
IN_PATH = os.path.join(HERE, "..", "data", "contributions.json")
OUT_PATH = os.path.join(HERE, "..", "contrib-heatmap.svg")
STATIC = bool(os.environ.get("STATIC"))

# Light paper card, with the README's blue (#1565c0) as the colour ramp
PALETTE = ["#e2e2de", "#cfe0f5", "#87b6e6", "#3f86d4", "#1565c0"]
BG = "#f3f3f1"
BG2 = "#f3f3f1"
FRAME = "#dcdcd7"
MUTED = "#6e6e73"
TEXT = "#111111"
SKY = "#1565c0"
ICE = "#1565c0"
FONT = "'Fira Code', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"

CELL = 12
GAP = 3
STEP = CELL + GAP
PAD = 22
LEFT_LABEL_W = 30
TOP_LABEL_H = 20
TITLEBAR_H = 30

COL_T = 0.018   # left -> right sweep
ROW_T = 0.045   # top -> bottom cascade
CELL_DUR = 0.42


def build_grid(days):
    first = datetime.date.fromisoformat(days[0]["date"])
    col = [None] * ((first.weekday() + 1) % 7)  # sunday = row 0
    grid = []
    for d in days:
        weekday = (datetime.date.fromisoformat(d["date"]).weekday() + 1) % 7
        while len(col) < weekday:
            col.append(None)
        col.append((d["date"], d["count"], max(0, min(4, int(d.get("level", 0))))))
        if len(col) == 7:
            grid.append(col)
            col = []
    if col:
        grid.append(col + [None] * (7 - len(col)))
    return grid


def render(data):
    days = data["days"]
    grid = build_grid(days)
    art_w, art_h = len(grid) * STEP, 7 * STEP

    month_labels, seen = [], set()
    for ci, column in enumerate(grid):
        cell = next((c for c in column if c), None)
        if not cell:
            continue
        date = datetime.date.fromisoformat(cell[0])
        if (date.year, date.month) not in seen and date.day <= 7:
            seen.add((date.year, date.month))
            month_labels.append((ci, date.strftime("%b")))

    canvas_w = PAD + LEFT_LABEL_W + art_w + PAD
    footer_h = 64
    canvas_h = TITLEBAR_H + TOP_LABEL_H + art_h + footer_h + PAD

    css = "" if STATIC else (
        "@keyframes cell{0%{opacity:0;transform:translateY(-6px)}100%{opacity:1;transform:none}}"
        f".c{{opacity:0;animation:cell {CELL_DUR:.2f}s cubic-bezier(.2,.8,.2,1) both}}"
        "@media (prefers-reduced-motion:reduce){.c{opacity:1!important;transform:none!important;animation:none!important}}"
    )

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{canvas_w}" height="{canvas_h}" '
        f'viewBox="0 0 {canvas_w} {canvas_h}" font-family="{FONT}">',
        f'<style>{css}</style>',
        f'<defs><linearGradient id="hbg" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0" stop-color="{BG2}"/><stop offset="1" stop-color="{BG}"/></linearGradient></defs>',
        f'<rect width="{canvas_w}" height="{canvas_h}" rx="12" fill="url(#hbg)"/>',
        f'<rect x="0.5" y="0.5" width="{canvas_w-1}" height="{canvas_h-1}" rx="12" '
        f'fill="none" stroke="{FRAME}"/>',
        f'<line x1="0" y1="{TITLEBAR_H}" x2="{canvas_w}" y2="{TITLEBAR_H}" stroke="{FRAME}"/>',
    ]
    for i, dot in enumerate(["#ff5f56", "#ffbd2e", "#27c93f"]):
        parts.append(f'<circle cx="{PAD + i*16}" cy="{TITLEBAR_H/2}" r="5" fill="{dot}"/>')
    parts.append(f'<text x="{canvas_w/2}" y="{TITLEBAR_H/2 + 4}" fill="{MUTED}" font-size="12" '
                 f'text-anchor="middle">aayush@github: ~/contributions --graph</text>')

    grid_top = TITLEBAR_H + TOP_LABEL_H
    grid_left = PAD + LEFT_LABEL_W
    for ci, label in month_labels:
        parts.append(f'<text x="{grid_left + ci*STEP}" y="{TITLEBAR_H + 14}" fill="{MUTED}" font-size="10">{label}</text>')
    for wi, name in [(1, "Mon"), (3, "Wed"), (5, "Fri")]:
        parts.append(f'<text x="{PAD}" y="{grid_top + wi*STEP + CELL*0.78:.1f}" fill="{MUTED}" font-size="9">{name}</text>')

    for ci, column in enumerate(grid):
        for ri, cell in enumerate(column):
            if cell is None:
                continue
            date_s, count, lvl = cell
            delay = "" if STATIC else f' class="c" style="animation-delay:{ci*COL_T + ri*ROW_T:.3f}s"'
            parts.append(
                f'<rect{delay} x="{grid_left + ci*STEP}" y="{grid_top + ri*STEP}" width="{CELL}" height="{CELL}" '
                f'rx="2.5" fill="{PALETTE[lvl]}"><title>{date_s}: {count} contribution{"" if count == 1 else "s"}</title></rect>')

    # legend, bottom right
    leg_y = grid_top + art_h + 6
    leg_x = canvas_w - PAD - (len(PALETTE) * CELL + 34)
    parts.append(f'<text x="{leg_x - 6}" y="{leg_y + CELL*0.8:.1f}" fill="{MUTED}" font-size="10" text-anchor="end">Less</text>')
    for k, color in enumerate(PALETTE):
        parts.append(f'<rect x="{leg_x + k*CELL}" y="{leg_y}" width="{CELL-1}" height="{CELL-1}" rx="2.2" fill="{color}"/>')
    parts.append(f'<text x="{leg_x + len(PALETTE)*CELL + 4}" y="{leg_y + CELL*0.8:.1f}" fill="{MUTED}" font-size="10">More</text>')

    sep_y = leg_y + CELL + 14
    parts.append(f'<line x1="0" y1="{sep_y}" x2="{canvas_w}" y2="{sep_y}" stroke="{FRAME}"/>')
    ly = sep_y + 26
    rng = data["range"]
    parts.append(f'<text x="{PAD}" y="{ly}" font-size="13" fill="{SKY}"><tspan font-weight="700">'
                 f'{data["total_contributions"]:,}</tspan><tspan fill="{MUTED}"> contributions in the last year</tspan></text>')
    parts.append(f'<text x="{canvas_w - PAD}" y="{ly}" font-size="12" fill="{MUTED}" text-anchor="end">'
                 f'{rng["start"]} <tspan fill="{ICE}">&#8594;</tspan> {rng["end"]}</text>')
    parts.append("</svg>")
    return "".join(parts)


if __name__ == "__main__":
    svg = render(json.load(open(IN_PATH)))
    with open(OUT_PATH, "w") as f:
        f.write(svg)
    print(f"wrote {OUT_PATH} ({len(svg)//1024} KB)")
