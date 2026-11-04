---
name: "rar-kody-w-microsoft-deck-studio"
description: "Generate a polished, Microsoft-Fluent-styled PowerPoint (.pptx) from a JSON spec of slides. Supported layouts: title, hero, statement, bullets, steps, columns, content2col, feature, ecosystem, flow, processflow, quote, cta. Returns the saved .pptx path."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/microsoft_deck_studio_agent", "rar_sha256": "1ff2b23806ff4a7ce64b9b4d21f249ac53e9a6efd5b57b839e95a9077e2e68f0", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["powerpoint", "pptx", "deck", "slides", "presentation", "microsoft", "fluent", "generator", "design"]}
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
