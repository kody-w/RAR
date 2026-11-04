---
name: "rar-kody-w-microsoft-deck-studio"
description: "Generate a polished, Microsoft-Fluent-styled PowerPoint (.pptx) from a JSON spec of slides. Supported layouts: title, hero, statement, bullets, steps, columns, content2col, feature, ecosystem, flow, processflow, quote, cta. Returns the saved .pptx path."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/microsoft_deck_studio_agent", "rar_sha256": "1ff2b23806ff4a7ce64b9b4d21f249ac53e9a6efd5b57b839e95a9077e2e68f0", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["powerpoint", "pptx", "deck", "slides", "presentation", "microsoft", "fluent", "generator", "design"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/microsoft_deck_studio_agent`. The original RAPP
agent is preserved byte-for-byte in `microsoft_deck_studio_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

Microsoft Deck Studio — generate a polished, Microsoft-Fluent-styled PowerPoint (.pptx)
from a plain JSON spec of slides. Give it a deck spec; it renders a branded 16:9 deck
(Segoe UI, Fluent palette, Microsoft 4-square mark, brand bar + page footer) and returns
the saved file path. python-pptx is imported lazily (auto-installed if missing).

SPEC SHAPE (pass as the `spec` param, JSON string or object):
{
  "deck": { "wordmark":"RAPP · Rapid Agent Prototype Platform",
             "footLeft":"Microsoft · MCAPS", "pageLabel":"Business Overview" },
  "slides": [ { "layout":"<name>", ... }, ... ]
}

LAYOUTS (each slide is one object; {h}...{/h} in a headline highlights that span in the accent color):
  title      : title, titleSize?, expand?, tag?, one?            (navy hero cover)
  hero       : kicker, hook, subhead?, proofChips[]?, closingLine?   (dark hook slide)
  statement  : kicker?, headline({h}), sub? OR points[]           (big statement + supports)
  bullets    : kicker?, headline, points[]  ("Lead||rest" bolds the lead)
  steps      : kicker?, headline, steps[{n?,t,d}] (<=3), footnote?  (numbered cards)
  columns    : kicker?, headline, columns[{tag,title,points[],alt?}] (<=2), footnote?
  content2col: kicker?, headline, intro?, accent?, columns[{title,points[],accent?}], highlight?
  feature    : kicker, headline({h}), points[], accent?, side?(left|right),
               visual?(bubble|number|file), hook?, hookSub?, bubbleText?
  ecosystem  : kicker?, headline({h}), subhead?, icons[{file,label}]  (file = local PNG path)
  flow       : kicker?, headline, subhead?, stages[{name,sub,owner?,accent?}], footer?
  processflow: kicker?, headline, steps[{title,desc}], highlights[<=2], footer?
  quote      : quote, by?, role?
  cta        : kicker?, headline, points[]?, doorLabel?, link?
Colors accept hex like "#0078D4" (blue), "#8661C5" (purple), "#D83B01" (orange), "#107C10" (green).

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "output_path": {
      "description": "Absolute .pptx path to write. Optional; defaults to ~/Downloads/<title>.pptx (or CWD).",
      "type": "string"
    },
    "spec": {
      "description": "Deck spec as a JSON object or JSON string: {deck:{wordmark,footLeft,pageLabel}, slides:[{layout, ...}]}. See the agent docstring for each layout's fields; {h}...{/h} highlights a headline span.",
      "type": "string"
    }
  },
  "required": [
    "spec"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `microsoft_deck_studio_agent.py` and embedded as the fenced Python below (sha256 1ff2b23806ff4a7c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `microsoft_deck_studio_agent.py` first:

```bash
python3 microsoft_deck_studio_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 microsoft_deck_studio_agent.py   # or on stdin
python3 microsoft_deck_studio_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/microsoft_deck_studio_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/microsoft_deck_studio_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/microsoft_deck_studio_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""Microsoft Deck Studio — generate a polished, Microsoft-Fluent-styled PowerPoint (.pptx)
from a plain JSON spec of slides. Give it a deck spec; it renders a branded 16:9 deck
(Segoe UI, Fluent palette, Microsoft 4-square mark, brand bar + page footer) and returns
the saved file path. python-pptx is imported lazily (auto-installed if missing).

SPEC SHAPE (pass as the `spec` param, JSON string or object):
{
  "deck": { "wordmark":"RAPP · Rapid Agent Prototype Platform",
             "footLeft":"Microsoft · MCAPS", "pageLabel":"Business Overview" },
  "slides": [ { "layout":"<name>", ... }, ... ]
}

LAYOUTS (each slide is one object; {h}...{/h} in a headline highlights that span in the accent color):
  title      : title, titleSize?, expand?, tag?, one?            (navy hero cover)
  hero       : kicker, hook, subhead?, proofChips[]?, closingLine?   (dark hook slide)
  statement  : kicker?, headline({h}), sub? OR points[]           (big statement + supports)
  bullets    : kicker?, headline, points[]  ("Lead||rest" bolds the lead)
  steps      : kicker?, headline, steps[{n?,t,d}] (<=3), footnote?  (numbered cards)
  columns    : kicker?, headline, columns[{tag,title,points[],alt?}] (<=2), footnote?
  content2col: kicker?, headline, intro?, accent?, columns[{title,points[],accent?}], highlight?
  feature    : kicker, headline({h}), points[], accent?, side?(left|right),
               visual?(bubble|number|file), hook?, hookSub?, bubbleText?
  ecosystem  : kicker?, headline({h}), subhead?, icons[{file,label}]  (file = local PNG path)
  flow       : kicker?, headline, subhead?, stages[{name,sub,owner?,accent?}], footer?
  processflow: kicker?, headline, steps[{title,desc}], highlights[<=2], footer?
  quote      : quote, by?, role?
  cta        : kicker?, headline, points[]?, doorLabel?, link?
Colors accept hex like "#0078D4" (blue), "#8661C5" (purple), "#D83B01" (orange), "#107C10" (green).
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/microsoft_deck_studio_agent",
    "version": "1.0.1",
    "display_name": "Microsoft Deck Studio",
    "description": "Generate a polished, Microsoft-Fluent-styled PowerPoint (.pptx) deck from a JSON spec of slides and layouts.",
    "author": "Kody Wildfeuer",
    "tags": ["powerpoint", "pptx", "deck", "slides", "presentation", "microsoft", "fluent", "generator", "design"],
    "category": "productivity",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

import os, sys, json, math, re

try:
    from agents.basic_agent import BasicAgent            # RAPP runtime
except ImportError:
    try:
        from basic_agent import BasicAgent
    except ImportError:                                   # standalone fallback
        class BasicAgent:
            def __init__(self, name=None, metadata=None):
                self.name = name or "BasicAgent"; self.metadata = metadata or {}
            def perform(self, **kwargs): return "Not implemented."
            def system_context(self): return None

# ---- brand strings (set per-render from spec["deck"]) ----
FONT = "Segoe UI"; FONT_SB = "Segoe UI Semibold"
WORDMARK = "RAPP · Rapid Agent Prototype Platform"
FOOT_LEFT = "Microsoft · MCAPS"; FOOT_RIGHT = "Business Overview · v1"; PAGE_LABEL = "Business Overview"
_ENGINE_READY = False


def _ensure_engine():
    """Import python-pptx (auto-install if missing) and bind pptx symbols + palette as globals."""
    global _ENGINE_READY, Presentation, Inches, Pt, Emu, RGBColor, PP_ALIGN, MSO_ANCHOR, MSO_SHAPE, qn
    global BLUE, BLUE_DK, NAVY, NAVY_DEEP, CYAN, INK, INK_SOFT, MUTED, LINE, SURFACE, WHITE, PAPER, SQ, LIGHTBLUE, PALEBLUE
    if _ENGINE_READY:
        return True, ""

    def _imp():
        global Presentation, Inches, Pt, Emu, RGBColor, PP_ALIGN, MSO_ANCHOR, MSO_SHAPE, qn
        from pptx import Presentation
        from pptx.util import Inches, Pt, Emu
        from pptx.dml.color import RGBColor
        from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
        from pptx.enum.shapes import MSO_SHAPE
        from pptx.oxml.ns import qn
    try:
        _imp()
    except ImportError:
        try:
            import subprocess
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--quiet", "python-pptx"])
            _imp()
        except Exception as e:
            return False, ("[MicrosoftDeckStudio] needs python-pptx and could not auto-install it. "
                           "Run:  pip install python-pptx   (%s)" % e)
    BLUE = RGBColor(0x00, 0x78, 0xD4); BLUE_DK = RGBColor(0x00, 0x5A, 0x9E); NAVY = RGBColor(0x10, 0x3A, 0x6B)
    NAVY_DEEP = RGBColor(0x0B, 0x2A, 0x4A); CYAN = RGBColor(0x50, 0xE6, 0xFF); INK = RGBColor(0x1B, 0x1A, 0x19)
    INK_SOFT = RGBColor(0x3B, 0x3A, 0x39); MUTED = RGBColor(0x60, 0x5E, 0x5C); LINE = RGBColor(0xE1, 0xDF, 0xDD)
    SURFACE = RGBColor(0xF3, 0xF2, 0xF1); WHITE = RGBColor(0xFF, 0xFF, 0xFF); PAPER = RGBColor(0xFF, 0xFF, 0xFF)
    SQ = [RGBColor(0xF2, 0x50, 0x22), RGBColor(0x7F, 0xBA, 0x00), RGBColor(0x00, 0xA4, 0xEF), RGBColor(0xFF, 0xB9, 0x00)]
    LIGHTBLUE = RGBColor(0xBF, 0xE6, 0xFF); PALEBLUE = RGBColor(0xDC, 0xEE, 0xFF)
    _ENGINE_READY = True
    return True, ""


# ---------- color helpers ----------
def _rgb(h):
    h = h.lstrip('#'); return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))
def C(h):
    r, g, b = _rgb(h); return RGBColor(r, g, b)
def lighten(h, f):
    r, g, b = _rgb(h); return RGBColor(int(r + (255 - r) * f), int(g + (255 - g) * f), int(b + (255 - b) * f))
def darken(h, f):
    r, g, b = _rgb(h); return RGBColor(int(r * (1 - f)), int(g * (1 - f)), int(b * (1 - f)))

def slide():
    return prs.slides.add_slide(BLANK)

def rect(s, x, y, w, h, fill=None, line=None, line_w=None, shape=None, shadow=False):
    if shape is None: shape = MSO_SHAPE.RECTANGLE
    sp = s.shapes.add_shape(shape, x, y, w, h)
    if fill is None: sp.fill.background()
    else: sp.fill.solid(); sp.fill.fore_color.rgb = fill
    if line is None: sp.line.fill.background()
    else: sp.line.color.rgb = line; sp.line.width = line_w or Pt(1)
    sp.shadow.inherit = False
    if shadow: _soft_shadow(sp)
    return sp

def _soft_shadow(sp):
    spPr = sp._element.spPr
    for ex in spPr.findall(qn('a:effectLst')): spPr.remove(ex)
    el = spPr.makeelement(qn('a:effectLst'), {})
    sh = el.makeelement(qn('a:outerShdw'), {'blurRad': '90000', 'dist': '40000', 'dir': '5400000', 'rotWithShape': '0'})
    clr = sh.makeelement(qn('a:srgbClr'), {'val': '000000'})
    alpha = clr.makeelement(qn('a:alpha'), {'val': '22000'})
    clr.append(alpha); sh.append(clr); el.append(sh); spPr.append(el)

def grad(sp, c1, c2, angle=45):
    sp.fill.gradient(); stops = sp.fill.gradient_stops
    stops[0].position = 0.0; stops[0].color.rgb = c1
    stops[1].position = 1.0; stops[1].color.rgb = c2
    try: sp.fill.gradient_angle = angle
    except Exception: pass

def txt(s, x, y, w, h, runs, align=None, anchor=None, space_after=None, line_spacing=None, wrap=True):
    if align is None: align = PP_ALIGN.LEFT
    if anchor is None: anchor = MSO_ANCHOR.TOP
    tb = s.shapes.add_textbox(x, y, w, h); tf = tb.text_frame; tf.word_wrap = wrap
    tf.vertical_anchor = anchor
    tf.margin_left = 0; tf.margin_right = 0; tf.margin_top = 0; tf.margin_bottom = 0
    for i, para in enumerate(runs):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        al = para.get("align"); p.alignment = al if al is not None else align
        if line_spacing: p.line_spacing = line_spacing
        if para.get("line_spacing"): p.line_spacing = para["line_spacing"]
        if space_after is not None: p.space_after = Pt(space_after)
        if para.get("space_before") is not None: p.space_before = Pt(para["space_before"])
        if para.get("space_after") is not None: p.space_after = Pt(para["space_after"])
        for rdef in para["runs"]:
            r = p.add_run(); r.text = rdef["t"]; f = r.font
            f.size = Pt(rdef.get("sz", 18)); f.name = rdef.get("font") or FONT
            f.bold = rdef.get("b", False); f.color.rgb = rdef.get("c") if rdef.get("c") is not None else INK
            if rdef.get("spacing") is not None: _letter_spacing(r, rdef["spacing"])
    return tb

def _letter_spacing(run, pts):
    run._r.get_or_add_rPr().set('spc', str(int(pts * 100)))

def R(t, sz=18, c=None, b=False, font=None, spacing=None):
    return {"t": t, "sz": sz, "c": c, "b": b, "font": font, "spacing": spacing}
def P(runs, align=None, sa=None, sb=None, ls=None):
    d = {"runs": runs, "align": align}
    if sa is not None: d["space_after"] = sa
    if sb is not None: d["space_before"] = sb
    if ls is not None: d["line_spacing"] = ls
    return d

def squares(s, x, y, size, gap=None):
    g = Emu(int(size * 0.14)); pos = [(0, 0), (1, 0), (0, 1), (1, 1)]
    for i, (cx, cy) in enumerate(pos):
        rect(s, x + cx * (size + g), y + cy * (size + g), size, size, fill=SQ[i], shape=MSO_SHAPE.RECTANGLE)

def brandbar(s, dark=False):
    x = Inches(0.55); y = Inches(0.42)
    squares(s, x, y, Inches(0.13))
    name, _, desc = WORDMARK.partition(" · ")
    txt(s, x + Inches(0.42), y - Inches(0.04), Inches(6.5), Inches(0.4),
        [P([R(name + " ", 14, INK if not dark else WHITE, True),
            R(("· " + desc) if desc else "", 12, MUTED if not dark else LIGHTBLUE)])], anchor=MSO_ANCHOR.MIDDLE)

def pagenum(s, i, dark=False):
    txt(s, SW - Inches(3.1), SH - Inches(0.55), Inches(2.6), Inches(0.35),
        [P([R("%s · %02d" % (PAGE_LABEL, i), 10.5, MUTED if not dark else LIGHTBLUE, spacing=0.6)], align=PP_ALIGN.RIGHT)],
        anchor=MSO_ANCHOR.MIDDLE)

def kicker(s, x, y, text, dark=False):
    rect(s, x, y + Inches(0.10), Inches(0.30), Inches(0.045), fill=BLUE if not dark else CYAN)
    txt(s, x + Inches(0.42), y, Inches(9), Inches(0.35),
        [P([R(text.upper(), 13, BLUE if not dark else CYAN, True, spacing=1.6)])], anchor=MSO_ANCHOR.MIDDLE)

def bg(s, color): rect(s, 0, 0, SW, SH, fill=color)
def bg_grad(s, c1, c2, angle=45):
    sp = rect(s, 0, 0, SW, SH, fill=c1); grad(sp, c1, c2, angle); return sp

def check_list(s, x, y, w, items, gap=None, size=20, dark=False, line_h=None, chk_color=None, chk_bg=None):
    if line_h is None: line_h = Inches(0.72)
    cc = chk_color or (WHITE if dark else BLUE)
    cbg = chk_bg or (RGBColor(0x1C, 0x4E, 0x82) if dark else RGBColor(0xE5, 0xF1, 0xFB))
    cy = y
    for it in items:
        rect(s, x, cy + Inches(0.03), Inches(0.34), Inches(0.34), fill=cbg, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
        txt(s, x, cy + Inches(0.03), Inches(0.34), Inches(0.34),
            [P([R("✓", 14, cc, True)], align=PP_ALIGN.CENTER)], anchor=MSO_ANCHOR.MIDDLE)
        lead, rest = (it.split("||", 1) + [""])[:2] if "||" in it else ("", it)
        runs = []
        if lead: runs.append(R(lead + " ", size, (INK if not dark else WHITE), True))
        runs.append(R(rest, size, (INK_SOFT if not dark else PALEBLUE)))
        txt(s, x + Inches(0.52), cy - Inches(0.02), w - Inches(0.52), line_h, [P(runs, ls=1.08)], anchor=MSO_ANCHOR.TOP)
        cy = cy + line_h
    return cy

# ============================ layout renderers ============================
def render_title(s, d, i):
    bg_grad(s, NAVY_DEEP, RGBColor(0x0E, 0x5A, 0xA7), angle=60)
    rect(s, 0, SH - Inches(0.18), SW, Inches(0.18), fill=BLUE)
    x = Inches(1.0); squares(s, x, Inches(1.1), Inches(0.32))
    tsize = d.get("titleSize", 100); title = d.get("title", "RAPP")
    lh = tsize * 1.08 / 72.0; cpl = max(1, int(11.2 / ((tsize * 0.52) / 72.0)))
    tlines = max(1, math.ceil(len(title) / cpl))
    txt(s, x, Inches(1.62), Inches(11.5), Inches(tlines * lh + 0.3),
        [P([R(title, tsize, WHITE, True, font=FONT_SB)], ls=1.06)])
    cur = 1.62 + tlines * lh + 0.34
    txt(s, x + Inches(0.03), Inches(cur), Inches(11), Inches(0.5),
        [P([R(d.get("expand", "Rapid Agent Prototype Platform"), 20, LIGHTBLUE, True, spacing=0.8)])])
    cur += 0.6
    if d.get("tag"):
        txt(s, x, Inches(cur), Inches(10.8), Inches(1.0), [P([R(d["tag"], 24, RGBColor(0xEA, 0xF6, 0xFF), True)], ls=1.2)]); cur += 0.9
    if d.get("one"):
        txt(s, x, Inches(cur), Inches(10.6), Inches(1.3), [P([R(d["one"], 15.5, RGBColor(0x9F, 0xCB, 0xEE))], ls=1.3)])
    txt(s, x, SH - Inches(0.72), Inches(6.5), Inches(0.4), [P([R(FOOT_LEFT, 13, RGBColor(0x9F, 0xC6, 0xE8), True, spacing=0.8)])])
    txt(s, SW - Inches(4.0), SH - Inches(0.72), Inches(3.0), Inches(0.4),
        [P([R(FOOT_RIGHT, 13, RGBColor(0x9F, 0xC6, 0xE8), spacing=0.8)], align=PP_ALIGN.RIGHT)])

def render_statement(s, d, i):
    bg(s, PAPER); rect(s, 0, 0, Inches(0.16), SH, fill=BLUE); brandbar(s); pagenum(s, i)
    x = Inches(1.0)
    if d.get("kicker"): kicker(s, x, Inches(2.0), d["kicker"])
    head = d.get("headline", ""); runs = []
    for part in re.split(r"(\{h\}.*?\{/h\})", head):
        if part.startswith("{h}"): runs.append(R(part[3:-4], 46, BLUE, True, font=FONT_SB))
        elif part: runs.append(R(part, 46, INK, True, font=FONT_SB))
    txt(s, x, Inches(2.45), Inches(11.4), Inches(1.9), [P(runs, ls=1.06)])
    plain = re.sub(r"\{/?h\}", "", head); hlines = max(1, math.ceil(len(plain) / 34))
    body_top = 2.45 + hlines * 0.70 + 0.42
    if d.get("sub"):
        txt(s, x, Inches(body_top), Inches(10.6), Inches(1.2), [P([R(d["sub"], 22, MUTED)], ls=1.3)])
    if d.get("points"):
        cy = Inches(body_top)
        for pt in d["points"]:
            nl = max(1, math.ceil(len(pt) / max(1, int(10.7 / ((18.5 * 0.52) / 72.0)))))
            rect(s, x, cy + Inches(0.12), Inches(0.13), Inches(0.13), fill=BLUE, shape=MSO_SHAPE.OVAL)
            txt(s, x + Inches(0.34), cy, Inches(10.7), Inches(0.32 * nl + 0.1), [P([R(pt, 18.5, INK_SOFT)], ls=1.15)], anchor=MSO_ANCHOR.TOP)
            cy = cy + Inches(0.30 * nl + 0.32)

def render_bullets(s, d, i):
    bg(s, PAPER); brandbar(s); pagenum(s, i); x = Inches(1.0)
    if d.get("kicker"): kicker(s, x, Inches(1.15), d["kicker"])
    txt(s, x, Inches(1.65), Inches(11.2), Inches(1.4), [P([R(d.get("headline", ""), 38, INK, True, font=FONT_SB)], ls=1.05)])
    pts = d.get("points", []); n = len(pts)
    if n <= 3:   size, line_h, y0 = 23, Inches(1.02), Inches(3.45)
    elif n == 4: size, line_h, y0 = 21, Inches(0.88), Inches(3.15)
    else:        size, line_h, y0 = 19.5, Inches(0.76), Inches(3.0)
    check_list(s, x, y0, Inches(11.0), pts, size=size, line_h=line_h)

def render_steps(s, d, i):
    bg(s, PAPER); brandbar(s); pagenum(s, i); x = Inches(1.0)
    if d.get("kicker"): kicker(s, x, Inches(1.15), d["kicker"])
    txt(s, x, Inches(1.65), Inches(11.2), Inches(1.2), [P([R(d.get("headline", ""), 36, INK, True, font=FONT_SB)], ls=1.05)])
    steps = d.get("steps", []); gap = Inches(0.4); total_w = Inches(11.33); cw = (total_w - gap * 2) / 3
    y = Inches(3.1); ch = Inches(3.3)
    for idx, st in enumerate(steps[:3]):
        cx = x + idx * (cw + gap)
        rect(s, cx, y, cw, ch, fill=WHITE, line=LINE, line_w=Pt(1), shape=MSO_SHAPE.ROUNDED_RECTANGLE, shadow=True)
        rect(s, cx, y + Inches(0.2), Inches(0.09), ch - Inches(0.4), fill=BLUE)
        rect(s, cx + Inches(0.42), y + Inches(0.4), Inches(0.7), Inches(0.7), fill=BLUE, shape=MSO_SHAPE.OVAL)
        txt(s, cx + Inches(0.42), y + Inches(0.4), Inches(0.7), Inches(0.7),
            [P([R(st.get("n", str(idx + 1)), 24, WHITE, True)], align=PP_ALIGN.CENTER)], anchor=MSO_ANCHOR.MIDDLE)
        txt(s, cx + Inches(0.42), y + Inches(1.28), cw - Inches(0.84), Inches(0.82),
            [P([R(st.get("t", ""), 21, INK, True, font=FONT_SB)], ls=1.05)], anchor=MSO_ANCHOR.TOP)
        txt(s, cx + Inches(0.42), y + Inches(2.18), cw - Inches(0.84), Inches(0.9),
            [P([R(st.get("d", ""), 15.5, MUTED)], ls=1.18)], anchor=MSO_ANCHOR.TOP)
    if d.get("footnote"):
        fy = y + ch + Inches(0.32); rect(s, x, fy + Inches(0.04), Inches(0.30), Inches(0.045), fill=BLUE)
        txt(s, x + Inches(0.42), fy - Inches(0.08), Inches(8.3), Inches(0.6), [P([R(d["footnote"], 17, INK_SOFT, True)], ls=1.15)])

def render_columns(s, d, i):
    bg(s, PAPER); brandbar(s); pagenum(s, i); x = Inches(1.0)
    if d.get("kicker"): kicker(s, x, Inches(1.15), d["kicker"])
    txt(s, x, Inches(1.65), Inches(11.2), Inches(1.2), [P([R(d.get("headline", ""), 36, INK, True, font=FONT_SB)], ls=1.05)])
    cols = d.get("columns", []); gap = Inches(0.45); total = Inches(11.33); cw = (total - gap) / 2
    y = Inches(2.9); ch = Inches(3.55); pad = Inches(0.5); inner_w_in = (cw - pad * 2) / 914400.0
    for idx, c in enumerate(cols[:2]):
        cx = x + idx * (cw + gap); alt = c.get("alt", False)
        card = rect(s, cx, y, cw, ch, fill=(NAVY if alt else WHITE), line=(None if alt else LINE), line_w=Pt(1),
                    shape=MSO_SHAPE.ROUNDED_RECTANGLE, shadow=True)
        if alt: grad(card, NAVY, RGBColor(0x0E, 0x5A, 0xA7), 60)
        txt(s, cx + pad, y + Inches(0.42), cw - pad * 2, Inches(0.35),
            [P([R(c.get("tag", "").upper(), 12.5, (CYAN if alt else BLUE), True, spacing=1.4)])])
        txt(s, cx + pad, y + Inches(0.82), cw - pad * 2, Inches(0.7),
            [P([R(c.get("title", ""), 25, (WHITE if alt else INK), True, font=FONT_SB)], ls=1.05)])
        cy = y + Inches(1.65)
        for pt in c.get("points", []):
            nl = max(1, math.ceil(len(pt) / max(1, int(inner_w_in / ((17.5 * 0.52) / 72.0)))))
            rect(s, cx + pad, cy + Inches(0.10), Inches(0.13), Inches(0.13), fill=(CYAN if alt else BLUE), shape=MSO_SHAPE.OVAL)
            txt(s, cx + pad + Inches(0.34), cy - Inches(0.02), cw - pad * 2 - Inches(0.34), Inches(0.34 * nl + 0.1),
                [P([R(pt, 17.5, (PALEBLUE if alt else INK_SOFT))], ls=1.12)], anchor=MSO_ANCHOR.TOP)
            cy = cy + Inches(0.30 * nl + 0.30)
    if d.get("footnote"):
        fy = y + ch + Inches(0.28); rect(s, x, fy + Inches(0.04), Inches(0.30), Inches(0.045), fill=BLUE)
        txt(s, x + Inches(0.42), fy - Inches(0.06), Inches(8.6), Inches(0.5), [P([R(d["footnote"], 16, INK_SOFT, True)], ls=1.1)])

def render_quote(s, d, i):
    bg_grad(s, RGBColor(0xF3, 0xF8, 0xFE), WHITE, 60); brandbar(s); pagenum(s, i); x = Inches(1.35)
    bar = rect(s, Inches(1.0), Inches(2.05), Inches(0.13), Inches(3.0), fill=BLUE, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
    grad(bar, BLUE, CYAN, 90); squares(s, x, Inches(2.0), Inches(0.13))
    txt(s, x, Inches(2.55), Inches(10.6), Inches(2.6), [P([R(d.get("quote", ""), 38, INK, True, font=FONT_SB)], ls=1.16)], anchor=MSO_ANCHOR.TOP)
    by = d.get("by", ""); role = d.get("role", "")
    rect(s, x, Inches(5.6), Inches(0.30), Inches(0.045), fill=BLUE)
    txt(s, x + Inches(0.42), Inches(5.4), Inches(11), Inches(0.6),
        [P([R(by, 19, BLUE_DK, True), R(("   ·   " + role) if role else "", 17, MUTED)])], anchor=MSO_ANCHOR.MIDDLE)

def render_cta(s, d, i):
    bg_grad(s, NAVY_DEEP, RGBColor(0x0E, 0x5A, 0xA7), 60); rect(s, 0, SH - Inches(0.18), SW, Inches(0.18), fill=BLUE)
    squares(s, Inches(0.55), Inches(0.5), Inches(0.12)); x = Inches(1.0)
    if d.get("kicker"):
        txt(s, x, Inches(1.5), Inches(9), Inches(0.4), [P([R(d["kicker"].upper(), 13, CYAN, True, spacing=1.6)])])
    head = d.get("headline", "")
    txt(s, x, Inches(1.95), Inches(11.4), Inches(1.5), [P([R(head, 48, WHITE, True, font=FONT_SB)], ls=1.05)])
    hlines = max(1, math.ceil(len(head) / 32)); pts_top = 1.95 + hlines * 0.72 + 0.34
    if d.get("points"):
        check_list(s, x, Inches(pts_top), Inches(11.0), d["points"], size=19, dark=True, line_h=Inches(0.66))
    if d.get("link"):
        by = Inches(5.95)
        rect(s, x, by, Inches(7.4), Inches(0.95), fill=WHITE, shape=MSO_SHAPE.ROUNDED_RECTANGLE, shadow=True)
        rect(s, x + Inches(0.28), by + Inches(0.235), Inches(0.48), Inches(0.48), fill=BLUE, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
        txt(s, x + Inches(0.28), by + Inches(0.20), Inches(0.48), Inches(0.52),
            [P([R("↓", 22, WHITE, True)], align=PP_ALIGN.CENTER)], anchor=MSO_ANCHOR.MIDDLE)
        txt(s, x + Inches(0.95), by, Inches(6.3), Inches(0.95),
            [P([R((d.get("doorLabel", "Start here") + "   "), 19, BLUE_DK, True), R(d.get("link", ""), 18, BLUE, font="Consolas")])], anchor=MSO_ANCHOR.MIDDLE)

def _feature_visual(s, d, px, py, pw, ph, ah):
    accent = C(ah); v = d.get("visual", "number")
    if v == "number":
        txt(s, px, py + Inches(1.25), pw, Inches(2.0), [P([R(d.get("hook", "~30"), 132, WHITE, True, font=FONT_SB)], align=PP_ALIGN.CENTER)])
        if d.get("hookSub"):
            txt(s, px, py + Inches(3.5), pw, Inches(0.7), [P([R(d["hookSub"], 22, WHITE, True)], align=PP_ALIGN.CENTER)], anchor=MSO_ANCHOR.MIDDLE)
    elif v == "bubble":
        bw = pw - Inches(1.0); bx = px + Inches(0.5); byy = py + Inches(1.1); bh = Inches(2.35)
        cb = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGULAR_CALLOUT, bx, byy, bw, bh)
        cb.fill.solid(); cb.fill.fore_color.rgb = WHITE; cb.line.fill.background(); cb.shadow.inherit = False; _soft_shadow(cb)
        tf = cb.text_frame; tf.word_wrap = True
        tf.margin_left = Inches(0.3); tf.margin_right = Inches(0.3); tf.margin_top = Inches(0.2); tf.margin_bottom = Inches(0.35)
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE; p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
        r = p.add_run(); r.text = d.get("bubbleText", "“What's my biggest risk today?”")
        r.font.size = Pt(21); r.font.name = FONT_SB; r.font.bold = True; r.font.color.rgb = darken(ah, 0.15)
        if d.get("hookSub"):
            txt(s, px, py + ph - Inches(1.15), pw, Inches(0.8), [P([R(d["hookSub"], 20, WHITE, True)], align=PP_ALIGN.CENTER)], anchor=MSO_ANCHOR.MIDDLE)
    elif v == "file":
        cwd = Inches(2.3); chh = Inches(2.85); cxm = px + pw / 2; fy = py + Inches(1.0)
        rect(s, cxm - cwd / 2 + Inches(0.42), fy + Inches(0.4), cwd, chh, fill=lighten(ah, 0.72), shape=MSO_SHAPE.ROUNDED_RECTANGLE)
        fx = cxm - cwd / 2 - Inches(0.18)
        rect(s, fx, fy, cwd, chh, fill=WHITE, shape=MSO_SHAPE.ROUNDED_RECTANGLE, shadow=True)
        rect(s, fx, fy, cwd, Inches(0.6), fill=accent, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
        rect(s, fx, fy + Inches(0.3), cwd, Inches(0.3), fill=accent)
        txt(s, fx + Inches(0.22), fy, cwd - Inches(0.4), Inches(0.6), [P([R(d.get("fileName", "solution.rapp"), 14, WHITE, True, font=FONT_SB)])], anchor=MSO_ANCHOR.MIDDLE)
        ly = fy + Inches(0.92)
        for wln in [1.7, 1.85, 1.45, 1.75]:
            rect(s, fx + Inches(0.24), ly, Inches(wln), Inches(0.12), fill=lighten(ah, 0.55), shape=MSO_SHAPE.ROUNDED_RECTANGLE); ly += Inches(0.42)
        if d.get("hookSub"):
            txt(s, px, py + ph - Inches(1.0), pw, Inches(0.7), [P([R(d["hookSub"], 20, WHITE, True)], align=PP_ALIGN.CENTER)], anchor=MSO_ANCHOR.MIDDLE)

def render_feature(s, d, i):
    bg(s, PAPER); ah = d.get("accent", "#0078D4"); accent = C(ah); side = d.get("side", "right")
    pw = Inches(4.7); ph = Inches(5.3); ptop = Inches(1.1)
    if side == "left": px = Inches(0.5); cx = Inches(5.7); cw = Inches(6.9)
    else: px = SW - Inches(5.2); cx = Inches(1.0); cw = Inches(6.6)
    panel = rect(s, px, ptop, pw, ph, fill=accent, shape=MSO_SHAPE.ROUNDED_RECTANGLE, shadow=True); grad(panel, accent, darken(ah, 0.30), 60)
    _feature_visual(s, d, px, ptop, pw, ph, ah); brandbar(s); pagenum(s, i)
    ky = Inches(1.5); rect(s, cx, ky + Inches(0.10), Inches(0.30), Inches(0.045), fill=accent)
    txt(s, cx + Inches(0.42), ky, Inches(6), Inches(0.35), [P([R(d.get("kicker", "").upper(), 13, accent, True, spacing=1.6)])], anchor=MSO_ANCHOR.MIDDLE)
    head = d.get("headline", ""); runs = []
    for part in re.split(r"(\{h\}.*?\{/h\})", head):
        if part.startswith("{h}"): runs.append(R(part[3:-4], 40, accent, True, font=FONT_SB))
        elif part: runs.append(R(part, 40, INK, True, font=FONT_SB))
    txt(s, cx, Inches(2.05), cw, Inches(1.7), [P(runs, ls=1.05)])
    plain = re.sub(r"\{/?h\}", "", head); cwin = cw / 914400.0
    hlines = max(1, math.ceil(len(plain) / max(1, int(cwin / ((40 * 0.52) / 72.0)))))
    body_top = 2.05 + hlines * 0.62 + 0.44
    check_list(s, cx, Inches(body_top), cw, d.get("points", []), size=19, line_h=Inches(0.82), chk_color=accent, chk_bg=lighten(ah, 0.86))

def render_hero(s, d, i):
    bg_grad(s, NAVY_DEEP, RGBColor(0x0E, 0x3E, 0x72), angle=55); rect(s, 0, SH - Inches(0.18), SW, Inches(0.18), fill=BLUE)
    brandbar(s, dark=True); pagenum(s, i, dark=True); x = Inches(1.0)
    txt(s, x, Inches(1.5), Inches(10), Inches(0.4), [P([R(d.get("kicker", "THE BIG IDEA").upper(), 14, CYAN, True, spacing=2.2)])])
    hook = d.get("hook", ""); hs = 46
    while hs > 30:
        cpl = max(1, int(11.3 / ((hs * 0.52) / 72.0)))
        if math.ceil(len(hook) / cpl) <= 2: break
        hs -= 2
    cpl = max(1, int(11.3 / ((hs * 0.52) / 72.0))); hlines = max(1, math.ceil(len(hook) / cpl))
    txt(s, x, Inches(2.12), Inches(11.5), Inches(hlines * 0.85 + 0.3), [P([R(hook, hs, WHITE, True, font=FONT_SB)], ls=1.06)])
    cur = 2.12 + hlines * (hs * 1.06 / 72.0) + 0.42
    if d.get("subhead"):
        txt(s, x, Inches(cur), Inches(10.9), Inches(1.0), [P([R(d["subhead"], 20, RGBColor(0xBF, 0xE6, 0xFF))], ls=1.3)])
        cur += 0.42 * max(1, math.ceil(len(d["subhead"]) / 95)) + 0.35
    chip_cols = [BLUE, C("#107C10"), C("#D83B01"), C("#8661C5")]; cxp = Inches(1.0); cyp = Inches(cur + 0.05)
    for idx, ch in enumerate(d.get("proofChips", [])):
        w = Inches(0.55 + 0.125 * len(ch))
        rect(s, cxp, cyp, w, Inches(0.56), fill=chip_cols[idx % len(chip_cols)], shape=MSO_SHAPE.ROUNDED_RECTANGLE)
        txt(s, cxp, cyp, w, Inches(0.56), [P([R(ch, 15, WHITE, True)], align=PP_ALIGN.CENTER)], anchor=MSO_ANCHOR.MIDDLE); cxp = cxp + w + Inches(0.22)
    if d.get("closingLine"):
        txt(s, x, SH - Inches(1.28), Inches(11), Inches(0.7), [P([R(d["closingLine"], 18, CYAN, True)], ls=1.2)])

def render_ecosystem(s, d, i):
    bg(s, PAPER); brandbar(s); pagenum(s, i); x = Inches(1.0)
    if d.get("kicker"): kicker(s, x, Inches(1.05), d["kicker"])
    head = d.get("headline", ""); runs = []
    for part in re.split(r"(\{h\}.*?\{/h\})", head):
        if part.startswith("{h}"): runs.append(R(part[3:-4], 38, BLUE, True, font=FONT_SB))
        elif part: runs.append(R(part, 38, INK, True, font=FONT_SB))
    txt(s, x, Inches(1.5), Inches(11.5), Inches(1.3), [P(runs, ls=1.05)])
    plain = re.sub(r"\{/?h\}", "", head); hlines = max(1, math.ceil(len(plain) / max(1, int(11.5 / ((38 * 0.52) / 72.0)))))
    cur = 1.5 + hlines * 0.58 + 0.22; pw = Inches(4.9)
    rect(s, x, Inches(cur), pw, Inches(0.5), fill=C("#0B2A4A"), shape=MSO_SHAPE.ROUNDED_RECTANGLE)
    txt(s, x, Inches(cur), pw, Inches(0.5), [P([R(d.get("badge", "●  Runs LOCAL · one file · no cloud to babysit"), 13, WHITE, True)], align=PP_ALIGN.CENTER)], anchor=MSO_ANCHOR.MIDDLE)
    cur += 0.66
    if d.get("subhead"):
        subl = max(1, math.ceil(len(d["subhead"]) / 88))
        txt(s, x, Inches(cur), Inches(11.2), Inches(0.42 * subl + 0.2), [P([R(d["subhead"], 18, MUTED)], ls=1.25)]); cur += 0.42 * subl + 0.26
    txt(s, x, Inches(cur), Inches(11), Inches(0.35), [P([R(d.get("rail", "TRANSLATES INTO"), 13, BLUE, True, spacing=2.2)])])
    icons = d.get("icons", []); n = max(1, len(icons)); band_x = 1.0; band_w = 11.33; colw = band_w / n; iy = cur + 0.48
    for idx, ic in enumerate(icons):
        cxc = band_x + colw * idx + colw / 2
        try:
            pic = s.shapes.add_picture(ic["file"], Inches(cxc - 0.4), Inches(iy), height=Inches(0.8)); pic.left = int(Inches(cxc) - pic.width / 2)
        except Exception:
            rect(s, Inches(cxc - 0.4), Inches(iy), Inches(0.8), Inches(0.8), fill=lighten("#0078D4", 0.85), line=LINE, line_w=Pt(1), shape=MSO_SHAPE.ROUNDED_RECTANGLE)
        txt(s, Inches(band_x + colw * idx), Inches(iy + 0.92), Inches(colw), Inches(0.5), [P([R(ic.get("label", ""), 11, INK_SOFT, True)], align=PP_ALIGN.CENTER)], anchor=MSO_ANCHOR.TOP)

def render_flow(s, d, i):
    bg(s, PAPER); brandbar(s); pagenum(s, i); x = Inches(1.0)
    if d.get("kicker"): kicker(s, x, Inches(1.0), d["kicker"])
    txt(s, x, Inches(1.42), Inches(11.4), Inches(0.9), [P([R(d.get("headline", ""), 40, INK, True, font=FONT_SB)])])
    if d.get("subhead"): txt(s, x, Inches(2.4), Inches(11), Inches(0.6), [P([R(d["subhead"], 19, MUTED)], ls=1.2)])
    stages = d.get("stages", []); n = max(1, len(stages)); band_w = 11.33; arrow_w = 0.34; chip_w = (band_w - (n - 1) * arrow_w) / n
    cy = 3.35; chh = 1.28; cxp = 1.0
    for idx, st in enumerate(stages):
        ah = st.get("accent"); acc = C(ah) if ah else None; fill = lighten(ah, 0.86) if ah else RGBColor(0xF3, 0xF2, 0xF1)
        rect(s, Inches(cxp), Inches(cy), Inches(chip_w), Inches(chh), fill=fill, line=(acc if acc else LINE), line_w=Pt(1.75 if acc else 1), shape=MSO_SHAPE.ROUNDED_RECTANGLE)
        txt(s, Inches(cxp), Inches(cy + 0.2), Inches(chip_w), Inches(0.4), [P([R(st["name"].upper(), 13.5, (acc if acc else INK), True, font=FONT_SB)], align=PP_ALIGN.CENTER)])
        txt(s, Inches(cxp + 0.1), Inches(cy + 0.62), Inches(chip_w - 0.2), Inches(0.55), [P([R(st.get("sub", ""), 10.5, MUTED)], align=PP_ALIGN.CENTER, ls=1.05)])
        if st.get("owner"):
            txt(s, Inches(cxp - 0.1), Inches(cy + chh + 0.1), Inches(chip_w + 0.2), Inches(0.35), [P([R("▲ " + st["owner"], 12, acc, True)], align=PP_ALIGN.CENTER)])
        cxp += chip_w
        if idx < n - 1:
            txt(s, Inches(cxp), Inches(cy + 0.32), Inches(arrow_w), Inches(0.5), [P([R("→", 19, MUTED, True)], align=PP_ALIGN.CENTER)], anchor=MSO_ANCHOR.MIDDLE); cxp += arrow_w
    if d.get("footer"):
        fby = 5.5; rect(s, x, Inches(fby), Inches(11.33), Inches(1.2), fill=RGBColor(0xF3, 0xF8, 0xFE), shape=MSO_SHAPE.ROUNDED_RECTANGLE)
        rect(s, x, Inches(fby), Inches(0.09), Inches(1.2), fill=BLUE)
        txt(s, x + Inches(0.34), Inches(fby), Inches(10.7), Inches(1.2), [P([R(d["footer"], 14.5, INK_SOFT)], ls=1.25)], anchor=MSO_ANCHOR.MIDDLE)

def render_content2col(s, d, i):
    bg(s, PAPER); brandbar(s); pagenum(s, i); ah = d.get("accent", "#0078D4"); accent = C(ah); x = Inches(1.0)
    if d.get("kicker"): kicker(s, x, Inches(1.0), d["kicker"])
    head = d.get("headline", "")
    txt(s, x, Inches(1.42), Inches(11.4), Inches(1.0), [P([R(head, 29, INK, True, font=FONT_SB)], ls=1.03)])
    hl = max(1, math.ceil(len(head) / max(1, int(11.4 / ((29 * 0.52) / 72.0))))); hy = 1.42 + hl * 0.45 + 0.14
    if d.get("intro"):
        il = max(1, math.ceil(len(d["intro"]) / 108))
        txt(s, x, Inches(hy), Inches(11.2), Inches(0.36 * il + 0.15), [P([R(d["intro"], 15, MUTED)], ls=1.22)]); hy += 0.34 * il + 0.2
    hi = d.get("highlight", ""); hib = max(1, math.ceil(len(hi) / 118)) if hi else 0
    hbar_h = (0.32 * hib + 0.3) if hi else 0; hbar_y = 6.86 - hbar_h; cards_top = hy + 0.05
    cards_bot = (hbar_y - 0.22) if hi else 6.62; ch_in = cards_bot - cards_top
    cols = d.get("columns", []); gap = 0.4; total = 11.33; cw = (total - gap) / 2; inner_w = cw - 0.8
    for idx, c in enumerate(cols[:2]):
        cah = c.get("accent", ah); cac = C(cah); cx = x + Inches(idx * (cw + gap))
        rect(s, cx, Inches(cards_top), Inches(cw), Inches(ch_in), fill=WHITE, line=LINE, line_w=Pt(1), shape=MSO_SHAPE.ROUNDED_RECTANGLE, shadow=True)
        rect(s, cx, Inches(cards_top), Inches(cw), Inches(0.5), fill=cac, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
        rect(s, cx, Inches(cards_top + 0.25), Inches(cw), Inches(0.25), fill=cac)
        txt(s, cx + Inches(0.32), Inches(cards_top), Inches(cw - 0.6), Inches(0.5), [P([R(c.get("title", ""), 14.5, WHITE, True, font=FONT_SB)], ls=1.0)], anchor=MSO_ANCHOR.MIDDLE)
        by = cards_top + 0.72
        for pt in c.get("points", []):
            nl = max(1, math.ceil(len(pt) / max(1, int((inner_w - 0.3) / ((13 * 0.52) / 72.0)))))
            rect(s, cx + Inches(0.34), Inches(by + 0.07), Inches(0.1), Inches(0.1), fill=cac, shape=MSO_SHAPE.OVAL)
            txt(s, cx + Inches(0.58), Inches(by), Inches(cw - 0.9), Inches(0.24 * nl + 0.1), [P([R(pt, 13, INK_SOFT)], ls=1.16)], anchor=MSO_ANCHOR.TOP); by += 0.225 * nl + 0.16
    if hi:
        rect(s, x, Inches(hbar_y), Inches(11.33), Inches(hbar_h), fill=lighten(ah, 0.86), shape=MSO_SHAPE.ROUNDED_RECTANGLE)
        rect(s, x, Inches(hbar_y), Inches(0.09), Inches(hbar_h), fill=accent)
        txt(s, x + Inches(0.32), Inches(hbar_y), Inches(10.7), Inches(hbar_h), [P([R(hi, 13.5, darken(ah, 0.12), True)], ls=1.18)], anchor=MSO_ANCHOR.MIDDLE)

def render_processflow(s, d, i):
    bg(s, PAPER); brandbar(s); x = Inches(1.0)
    if d.get("kicker"): kicker(s, x, Inches(1.05), d["kicker"])
    txt(s, x, Inches(1.52), Inches(11.6), Inches(0.8), [P([R(d.get("headline", ""), 34, INK, True, font=FONT_SB)])])
    steps = d.get("steps", []); n = max(1, len(steps)); aw = 0.28; total = 11.33; cw = (total - (n - 1) * aw) / n
    cy = 2.9; chh = 2.95; cxp = 1.0; pal = [C("#0078D4"), C("#8661C5"), C("#D83B01"), C("#107C10"), C("#0E5AA7"), C("#5C2D91")]
    for idx, st in enumerate(steps):
        acc = pal[idx % len(pal)]
        rect(s, Inches(cxp), Inches(cy), Inches(cw), Inches(chh), fill=WHITE, line=LINE, line_w=Pt(1), shape=MSO_SHAPE.ROUNDED_RECTANGLE, shadow=True)
        rect(s, Inches(cxp), Inches(cy), Inches(cw), Inches(0.09), fill=acc, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
        rect(s, Inches(cxp + 0.28), Inches(cy + 0.3), Inches(0.5), Inches(0.5), fill=acc, shape=MSO_SHAPE.OVAL)
        txt(s, Inches(cxp + 0.28), Inches(cy + 0.3), Inches(0.5), Inches(0.5), [P([R(str(idx + 1), 19, WHITE, True)], align=PP_ALIGN.CENTER)], anchor=MSO_ANCHOR.MIDDLE)
        txt(s, Inches(cxp + 0.26), Inches(cy + 0.92), Inches(cw - 0.48), Inches(0.55), [P([R(st.get("title", ""), 15, INK, True, font=FONT_SB)], ls=1.02)])
        txt(s, Inches(cxp + 0.26), Inches(cy + 1.46), Inches(cw - 0.48), Inches(1.35), [P([R(st.get("desc", ""), 10.5, MUTED)], ls=1.18)])
        cxp += cw
        if idx < n - 1:
            txt(s, Inches(cxp), Inches(cy + chh / 2 - 0.28), Inches(aw), Inches(0.55), [P([R("›", 27, C("#BFBFBF"), True)], align=PP_ALIGN.CENTER)], anchor=MSO_ANCHOR.MIDDLE); cxp += aw
    hs = d.get("highlights", [])
    if hs:
        hy = 6.15; hgap = 0.4; hw = (11.33 - hgap) / 2
        for j, ht in enumerate(hs[:2]):
            hx = 1.0 + j * (hw + hgap)
            rect(s, Inches(hx), Inches(hy), Inches(hw), Inches(0.75), fill=RGBColor(0xF3, 0xF8, 0xFE), shape=MSO_SHAPE.ROUNDED_RECTANGLE)
            rect(s, Inches(hx), Inches(hy), Inches(0.08), Inches(0.75), fill=BLUE)
            txt(s, Inches(hx + 0.28), Inches(hy), Inches(hw - 0.52), Inches(0.75), [P([R(ht, 12.5, INK_SOFT, True)], ls=1.15)], anchor=MSO_ANCHOR.MIDDLE)
    txt(s, SW - Inches(4.5), SH - Inches(0.62), Inches(4.0), Inches(0.35), [P([R(d.get("footer", "Confidential"), 10.5, MUTED, spacing=0.5)], align=PP_ALIGN.RIGHT)], anchor=MSO_ANCHOR.MIDDLE)


def _render_dict():
    return {
        "title": render_title, "statement": render_statement, "bullets": render_bullets, "steps": render_steps,
        "columns": render_columns, "quote": render_quote, "cta": render_cta, "feature": render_feature,
        "hero": render_hero, "ecosystem": render_ecosystem, "flow": render_flow,
        "content2col": render_content2col, "processflow": render_processflow,
    }

def _build_deck(spec, out_path):
    global prs, SW, SH, BLANK, WORDMARK, FOOT_LEFT, FOOT_RIGHT, PAGE_LABEL
    deck = spec.get("deck", {}) or {}
    WORDMARK = deck.get("wordmark", "RAPP · Rapid Agent Prototype Platform")
    FOOT_LEFT = deck.get("footLeft", "Microsoft · MCAPS")
    FOOT_RIGHT = deck.get("footRight", "Business Overview · v1")
    PAGE_LABEL = deck.get("pageLabel", "Business Overview")
    prs = Presentation(); prs.slide_width = Inches(13.333); prs.slide_height = Inches(7.5)
    BLANK = prs.slide_layouts[6]; SW, SH = prs.slide_width, prs.slide_height
    R_ = _render_dict()
    for idx, sd in enumerate(spec.get("slides", []), start=1):
        s = slide(); layout = sd.get("layout", "bullets")
        if layout == "title":
            merged = dict(deck); merged.update(sd); render_title(s, merged, idx)
        else:
            R_.get(layout, render_bullets)(s, sd, idx)
    prs.save(out_path)
    return len(spec.get("slides", []))

def _default_path(spec):
    deck = spec.get("deck", {}) or {}; slides = spec.get("slides", []) or [{}]
    title = deck.get("title") or slides[0].get("headline") or slides[0].get("title") or "RAPP_Deck"
    base = re.sub(r"[^A-Za-z0-9]+", "_", str(title)).strip("_")[:48] or "RAPP_Deck"
    dl = os.path.expanduser("~/Downloads")
    return os.path.join(dl if os.path.isdir(dl) else os.getcwd(), base + ".pptx")


class MicrosoftDeckStudio(BasicAgent):
    def __init__(self):
        self.name = "MicrosoftDeckStudio"
        self.metadata = {
            "name": self.name,
            "description": ("Generate a polished, Microsoft-Fluent-styled PowerPoint (.pptx) from a JSON spec of slides. "
                            "Supported layouts: title, hero, statement, bullets, steps, columns, content2col, feature, "
                            "ecosystem, flow, processflow, quote, cta. Returns the saved .pptx path."),
            "parameters": {
                "type": "object",
                "properties": {
                    "spec": {"type": "string", "description": "Deck spec as a JSON object or JSON string: {deck:{wordmark,footLeft,pageLabel}, slides:[{layout, ...}]}. See the agent docstring for each layout's fields; {h}...{/h} highlights a headline span."},
                    "output_path": {"type": "string", "description": "Absolute .pptx path to write. Optional; defaults to ~/Downloads/<title>.pptx (or CWD)."},
                },
                "required": ["spec"],
            },
        }
        super().__init__(self.name, self.metadata)

    def perform(self, **kwargs):
        spec = kwargs.get("spec")
        if spec is None:
            return "[MicrosoftDeckStudio] 'spec' is required — a JSON object (or string) with a 'slides' array."
        if isinstance(spec, str):
            try:
                spec = json.loads(spec)
            except Exception as e:
                return "[MicrosoftDeckStudio] could not parse 'spec' JSON: %s" % e
        if not isinstance(spec, dict) or not spec.get("slides"):
            return "[MicrosoftDeckStudio] 'spec' must be an object with a non-empty 'slides' array."
        ok, msg = _ensure_engine()
        if not ok:
            return msg
        out = kwargs.get("output_path") or _default_path(spec)
        try:
            out = os.path.abspath(os.path.expanduser(out))
            d = os.path.dirname(out)
            if d and not os.path.isdir(d):
                os.makedirs(d, exist_ok=True)
            n = _build_deck(spec, out)
        except Exception as e:
            return "[MicrosoftDeckStudio] render failed: %s: %s" % (type(e).__name__, e)
        return "[MicrosoftDeckStudio] Generated a %d-slide Microsoft-styled deck -> %s" % (n, out)
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
