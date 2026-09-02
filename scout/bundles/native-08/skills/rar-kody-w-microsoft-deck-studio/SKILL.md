---
name: "rar-kody-w-microsoft-deck-studio"
description: "Generate a polished, Microsoft-Fluent-styled PowerPoint (.pptx) from a JSON spec of slides. Supported layouts: title, hero, statement, bullets, steps, columns, content2col, feature, ecosystem, flow, processflow, quote, cta. Returns the saved .pptx path."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/microsoft_deck_studio_agent", "rar_sha256": "6aa3761fd90b1be592520185359a02a0bc0651c0c0bd86edb8fe9ff879138445", "source_kind": "rar-agent", "source_commit": "7dd246d78931ed3ded58456e382d2d064469a6cf", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "microsoft_deck_studio_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/microsoft-deck-studio:015e24f699fd002f99d2cb9acebb70d0d5df2680a5fe6480bdf660125615171f", "kind": "skill"}, "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["powerpoint", "pptx", "deck", "slides", "presentation", "microsoft", "fluent", "generator", "design"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/microsoft_deck_studio_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `microsoft_deck_studio_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `microsoft_deck_studio_agent.py` and embedded as the fenced Python below (sha256 6aa3761fd90b1be5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `microsoft_deck_studio_agent.py` first:

```bash
python3 microsoft_deck_studio_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 microsoft_deck_studio_agent.py   # or on stdin
python3 microsoft_deck_studio_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
