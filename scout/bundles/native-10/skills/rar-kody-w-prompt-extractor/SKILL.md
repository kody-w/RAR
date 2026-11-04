---
name: "rar-kody-w-prompt-extractor"
description: "Extract the prompts shown on screen in a video (YouTube URL or local file) by OCRing it frame by frame, so they don't have to be copied down by hand. Returns each distinct prompt once with its timestamp."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/prompt_extractor", "rar_sha256": "ece05fd7f282eb9dc85f002df0fd03cd09ba82cfcb8c2acb1a54eaf83279747d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["ocr", "video", "prompts", "extraction", "vision"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/prompt_extractor`. The original RAPP
agent is preserved byte-for-byte in `prompt_extractor_agent.py` and in the RCI capsule.

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

Prompt Extractor — pull the prompts out of a video so nobody has to transcribe them.

ARK PARITY. This file and the single-file SKILL.md distribution carry the same
code. The canonical body digests to:

    sha256 = 65dbdc01b9e712c2fd4cfc19df2036ce2ad1d91c84c83d78065f940466b1a0bf

If your copy differs, you are not running what the registry published.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "all_text": {
      "description": "Return every text block, not just prompt-like ones",
      "type": "boolean"
    },
    "fps": {
      "description": "Frames sampled per second (default 1.0; 0.5 is faster, 2 catches quick cuts)",
      "type": "number"
    },
    "min_score": {
      "description": "Prompt-likeness threshold, default 2.0. Lower to catch more.",
      "type": "number"
    },
    "save_to": {
      "description": "Optional path to write the full markdown result",
      "type": "string"
    },
    "url": {
      "description": "Video URL or local file path",
      "type": "string"
    }
  },
  "required": [
    "url"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `prompt_extractor_agent.py` and embedded as the fenced Python below (sha256 ece05fd7f282eb9d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `prompt_extractor_agent.py` first:

```bash
python3 prompt_extractor_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 prompt_extractor_agent.py   # or on stdin
python3 prompt_extractor_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/prompt_extractor.py -o ~/.brainstem/src/rapp_brainstem/agents/prompt_extractor.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/prompt_extractor/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""Prompt Extractor — pull the prompts out of a video so nobody has to transcribe them.

ARK PARITY. This file and the single-file SKILL.md distribution carry the same
code. The canonical body digests to:

    sha256 = 65dbdc01b9e712c2fd4cfc19df2036ce2ad1d91c84c83d78065f940466b1a0bf

If your copy differs, you are not running what the registry published.
"""

from __future__ import annotations

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/prompt_extractor",
    "version": "1.0.1",
    "display_name": "Prompt Extractor",
    "description": "Extract the prompts shown on screen in a video by OCRing it frame by frame, merging scrolled and repeated views into one entry each, so prompts demoed in a screen recording do not have to be transcribed by hand.",
    "author": "Kody Wildfeuer",
    "tags": ["ocr", "video", "prompts", "extraction", "vision"],
    "category": "productivity",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


import argparse
import difflib
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    from agents.basic_agent import BasicAgent
except ImportError:
  try:
    from basic_agent import BasicAgent
  except ImportError:  # standalone / different host layout
    class BasicAgent:  # type: ignore
        def __init__(self, name=None, metadata=None):
            if name is not None:
                self.name = name
            if metadata is not None:
                self.metadata = metadata

        def perform(self, **kwargs):
            return "Not implemented."


CACHE = Path.home() / ".rapp" / "cache" / "prompt-extractor"

# ---------------------------------------------------------------------------
# OCR backend: macOS Vision, embedded so this stays one portable file.
# ---------------------------------------------------------------------------

_SWIFT = r'''
import Foundation
import Vision
import AppKit
setvbuf(stdout, nil, _IOLBF, 0)
func q(_ s: String) -> String {
    var o = "\""
    for c in s.unicodeScalars {
        switch c {
        case "\"": o += "\\\""
        case "\\": o += "\\\\"
        case "\n": o += "\\n"
        case "\r": o += "\\r"
        case "\t": o += "\\t"
        default:
            if c.value < 0x20 { o += String(format: "\\u%04x", c.value) }
            else { o.unicodeScalars.append(c) }
        }
    }
    return o + "\""
}
func ocr(_ path: String) -> String {
    guard let img = NSImage(contentsOfFile: path),
          let cg = img.cgImage(forProposedRect: nil, context: nil, hints: nil) else {
        return "{\"path\":\(q(path)),\"lines\":[]}"
    }
    let req = VNRecognizeTextRequest()
    req.recognitionLevel = .accurate
    req.usesLanguageCorrection = false
    req.recognitionLanguages = ["en-US"]
    let h = VNImageRequestHandler(cgImage: cg, options: [:])
    do { try h.perform([req]) } catch { return "{\"path\":\(q(path)),\"lines\":[]}" }
    var parts: [String] = []
    for obs in (req.results ?? []) {
        guard let t = obs.topCandidates(1).first else { continue }
        let bb = obs.boundingBox
        let y = 1.0 - Double(bb.origin.y) - Double(bb.size.height)
        parts.append("{\"text\":\(q(t.string)),\"conf\":\(round(Double(t.confidence)*1000)/1000),\"y\":\(round(y*10000)/10000),\"x\":\(round(Double(bb.origin.x)*10000)/10000)}")
    }
    return "{\"path\":\(q(path)),\"lines\":[\(parts.joined(separator: ","))]}"
}
while let line = readLine(strippingNewline: true) {
    let p = line.trimmingCharacters(in: .whitespaces)
    if !p.isEmpty { print(ocr(p)) }
}
'''


def _vision_binary(log=print) -> Path | None:
    """Compile the Vision helper once; reuse it forever after."""
    if sys.platform != "darwin" or not shutil.which("swiftc"):
        return None
    CACHE.mkdir(parents=True, exist_ok=True)
    stamp = hashlib.sha256(_SWIFT.encode()).hexdigest()[:12]
    binary = CACHE / f"vision_ocr_{stamp}"
    if binary.exists():
        return binary
    src = CACHE / f"vision_ocr_{stamp}.swift"
    src.write_text(_SWIFT)
    log("  compiling the Vision OCR helper (one time)...")
    r = subprocess.run(
        ["swiftc", "-O", str(src), "-o", str(binary)],
        capture_output=True, text=True,
    )
    if r.returncode != 0:
        log("  swiftc failed:", r.stderr.strip().splitlines()[:3])
        return None
    return binary


def _ocr_vision(binary: Path, frames: list[Path], log=print) -> dict[str, list[dict]]:
    proc = subprocess.Popen(
        [str(binary)], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
        text=True, bufsize=1,
    )
    out: dict[str, list[dict]] = {}
    assert proc.stdin and proc.stdout
    for i, f in enumerate(frames, 1):
        proc.stdin.write(str(f) + "\n")
        proc.stdin.flush()
        line = proc.stdout.readline()
        try:
            rec = json.loads(line)
            out[rec["path"]] = rec.get("lines", [])
        except Exception:
            out[str(f)] = []
        if i % 25 == 0 or i == len(frames):
            log(f"  OCR {i}/{len(frames)} frames")
    proc.stdin.close()
    proc.wait(timeout=30)
    return out


def _ocr_tesseract(frames: list[Path], log=print) -> dict[str, list[dict]]:
    out: dict[str, list[dict]] = {}
    for i, f in enumerate(frames, 1):
        r = subprocess.run(
            ["tesseract", str(f), "stdout", "--psm", "6"],
            capture_output=True, text=True,
        )
        lines = [
            {"text": t, "conf": 0.8, "y": n / 100.0, "x": 0.0}
            for n, t in enumerate(r.stdout.splitlines()) if t.strip()
        ]
        out[str(f)] = lines
        if i % 25 == 0 or i == len(frames):
            log(f"  OCR {i}/{len(frames)} frames")
    return out


# ---------------------------------------------------------------------------
# Frame extraction + near-duplicate rejection
# ---------------------------------------------------------------------------

def _fetch(url_or_path: str, workdir: Path, log=print) -> Path:
    p = Path(url_or_path).expanduser()
    if p.exists():
        log(f"  local file: {p.name}")
        return p
    if not shutil.which("yt-dlp"):
        raise RuntimeError("yt-dlp is not on PATH — needed to download a URL")
    log("  downloading (capped at 1080p for legible text)...")
    out = workdir / "video.%(ext)s"
    r = subprocess.run(
        ["yt-dlp", "-q", "--no-warnings", "-N", "4",
         "-f", "bestvideo[height<=1080][ext=mp4]/bestvideo[height<=1080]/best[height<=1080]/best",
         "-o", str(out), url_or_path],
        capture_output=True, text=True,
    )
    hits = sorted(workdir.glob("video.*"))
    if r.returncode != 0 or not hits:
        raise RuntimeError(f"yt-dlp failed: {r.stderr.strip()[:400]}")
    log(f"  downloaded {hits[0].name} ({hits[0].stat().st_size/1048576:.1f} MB)")
    return hits[0]


def _frames(video: Path, workdir: Path, fps: float, log=print) -> list[Path]:
    d = workdir / "frames"
    d.mkdir(exist_ok=True)
    log(f"  extracting frames at {fps} fps...")
    subprocess.run(
        ["ffmpeg", "-v", "error", "-i", str(video),
         "-vf", f"fps={fps},scale=1600:-2:flags=lanczos",
         "-q:v", "2", str(d / "f%06d.jpg")],
        check=True, capture_output=True,
    )
    fr = sorted(d.glob("f*.jpg"))
    log(f"  {len(fr)} frames")
    return fr


def _dedupe(frames: list[Path], log=print) -> list[Path]:
    """Drop frames visually identical to the one before.

    Prompts sit on screen for seconds at a time, so most sampled frames are
    redundant. An 8x8 average hash is enough to spot 'nothing changed' and
    cuts OCR work dramatically, which is the expensive stage.
    """
    try:
        from PIL import Image
        import numpy as np
    except Exception:
        return frames

    kept, prev = [], None
    for f in frames:
        try:
            im = Image.open(f).convert("L").resize((16, 16))
            a = np.asarray(im, dtype=float)
            bits = a > a.mean()
        except Exception:
            kept.append(f)
            continue
        if prev is None or (bits ^ prev).sum() > 6:  # >6 of 256 cells changed
            kept.append(f)
            prev = bits
    log(f"  {len(kept)} visually distinct frames (skipped {len(frames)-len(kept)})")
    return kept


# ---------------------------------------------------------------------------
# Turning OCR lines into candidate prompts
# ---------------------------------------------------------------------------

STRONG = [
    "i want you to", "you are", "your task", "your job", "build me", "create a",
    "write a", "make me", "generate a", "implement", "refactor", "fan out",
    "sub-agent", "subagent", "ultrathink", "ultracode", "/loop", "don't stop",
    "do not stop", "step by step", "act as", "pretend you", "please write",
    "should be", "make sure", "at the level of",
]
IMPERATIVE = re.compile(
    r"^\s*(build|create|make|write|add|fix|implement|generate|design|refactor|"
    r"convert|turn|explain|summarize|analyze|analyse|give|show|find|take|use|"
    r"produce|draft|rewrite|extract|optimize|optimise)\b",
    re.I,
)
# lines that are almost always chrome, not prompt text
CHROME = re.compile(
    r"^(\d{1,2}:\d{2}(:\d{2})?|[\u2022\-\u2013]|\W{0,3})$|"
    r"^(file|edit|view|run|terminal|help|search|share|subscribe|like|comment|"
    r"settings|home|back|next|play|pause|menu|copy|paste|save|open|close|"
    r"sign in|log in|new chat|send|stop|cancel)$",
    re.I,
)

# Browser/app furniture that rides along in a screen recording. Left in, it
# both pollutes the prompt text and blocks merging, because the chrome differs
# frame to frame while the prompt underneath is identical.
FURNITURE = re.compile(
    r"(https?://|www\.|\b[\w-]+\.(com|ai|dev|io|org|net)/)"          # urls
    r"|^\s*[+*\u2022\u00b0]?\s*(ask\s+\w+|new\s+conversation|finish\s+update"
    r"|new\s+chat|share|export|copy\s+link|sign\s+in|log\s+in|upgrade"
    r"|expert\s*v?|fast\s*v?|auto\s*v?|thinking|searching|worked\s+for"
    r"|ask\s+anything|send\s+message|regenerate|continue)\s*[:\u00b7|]?\s*$"
    r"|^\s*\d+\s*(result|match|file|line)s?\b"                        # result counters
    r"|^[\w./\\-]+\.(kt|ts|js|py|java|json|html|css|tsx|jsx|md)\b"    # file paths
    r"|^\s*(def|import|package|class|const|let|var|function|return|@)\b",  # code
    re.I,
)


def _is_furniture(line: dict) -> bool:
    t = line.get("text", "").strip()
    if not t:
        return True
    # top strip of the window is the tab bar / address bar in nearly every
    # screen recording; nothing a person typed as a prompt lives up there.
    if line.get("y", 1.0) < 0.075:
        return True
    if FURNITURE.search(t):
        return True
    # tab titles: short, title-cased, often ending in a close glyph
    if len(t.split()) <= 8 and re.search(r"[×x]\s*$", t) and t[:1].isupper():
        return True
    return False


def _blocks(lines: list[dict]) -> list[str]:
    """Group OCR lines into visual paragraphs by vertical gap."""
    good = [
        l for l in lines
        if l.get("conf", 0) >= 0.3
        and l.get("text", "").strip()
        and not CHROME.match(l["text"].strip())
        and not _is_furniture(l)
    ]
    if not good:
        return []
    good.sort(key=lambda l: (l.get("y", 0), l.get("x", 0)))

    # Adaptive paragraph break. A fixed gap threshold is wrong: line spacing
    # scales with font size, so a constant that works for a dense chat panel
    # splits every single line of a large-text slide into its own block. Break
    # only where the gap is clearly larger than this frame's own line spacing.
    gaps = [
        good[i + 1].get("y", 0) - good[i].get("y", 0)
        for i in range(len(good) - 1)
    ]
    gaps = [g for g in gaps if g > 0]
    if gaps:
        med = sorted(gaps)[len(gaps) // 2]
        brk = max(med * 2.2, 0.02)
    else:
        brk = 0.045

    out, cur, last_y = [], [], None
    for l in good:
        y = l.get("y", 0)
        if last_y is not None and (y - last_y) > brk:
            out.append(" ".join(cur))
            cur = []
        cur.append(l["text"].strip())
        last_y = y
    if cur:
        out.append(" ".join(cur))
    return [re.sub(r"\s+", " ", b).strip() for b in out if b.strip()]


def _score(text: str) -> float:
    """How much does this read like a prompt someone typed at a model?"""
    t = text.lower().strip()
    words = t.split()
    if len(words) < 6:
        return 0.0
    s = 0.0
    s += min(len(words) / 40.0, 1.6)                    # длина: prompts are wordy
    s += 2.4 * sum(1 for k in STRONG if k in t)         # explicit prompt markers
    if IMPERATIVE.match(text):
        s += 1.5
    if re.search(r"\b(should|must|don'?t|never|always|until|so that)\b", t):
        s += 0.7
    if t.count(".") >= 2 or t.count(",") >= 3:
        s += 0.4
    # penalties: mostly-symbol OCR noise, or shouty UI
    letters = sum(c.isalpha() or c.isspace() for c in text)
    if letters / max(len(text), 1) < 0.72:
        s -= 1.6
    if _readable(text) < 0.75:      # OCR noise, not language
        s -= 2.5
    if text.isupper() and len(words) < 14:
        s -= 1.0
    return s


def _norm(s: str) -> str:
    """Comparison form: lowercase alphanumerics only, so OCR punctuation
    wobble ('16x16' vs '16×16', '•' vs '.') stops splitting one prompt in two."""
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def _overlap(a: str, b: str, min_chars: int = 40) -> int:
    """Length of the longest suffix of `a` that is also a prefix of `b`."""
    limit = min(len(a), len(b))
    for n in range(limit, min_chars - 1, -1):
        if a[-n:] == b[:n]:
            return n
    return 0


def _stitch(a: str, b: str) -> str | None:
    """Reassemble two views of the same scrolling text, or None if unrelated.

    A long prompt is usually revealed by scrolling, so each frame shows a
    different *window* of it. Whole-string similarity fails on that (the windows
    start at different points), which is why naive dedupe returns the same
    prompt a dozen times. Containment and suffix/prefix overlap recover the
    full text instead.
    """
    na, nb = _norm(a), _norm(b)
    if not na or not nb:
        return None
    if na in nb:
        return b
    if nb in na:
        return a
    if _overlap(na, nb) >= 40:          # a scrolled down into b
        keep = len(_norm(a)) - _overlap(na, nb)
        return a + " " + b[_tail_index(b, _overlap(na, nb)):] if keep else b
    if _overlap(nb, na) >= 40:          # b scrolled down into a
        return _stitch(b, a)
    return None


def _tail_index(s: str, norm_chars: int) -> int:
    """Map a count of normalized chars back to an index in the raw string."""
    seen = 0
    for i, ch in enumerate(s):
        if re.match(r"[a-z0-9]", ch.lower()):
            seen += 1
        if seen > norm_chars:
            return i
    return len(s)


STOP = {
    "the", "and", "for", "with", "that", "this", "from", "have", "must", "should",
    "will", "your", "you", "are", "not", "but", "all", "any", "can", "use", "using",
    "into", "when", "each", "them", "then", "than", "also", "only", "over", "make",
}


# ~200 words that dominate ordinary English prose. OCR garble almost never
# produces them, so the hit rate is a reliable "is this language?" signal.
COMMON = set("""
the be to of and a in that have it for not on with he as you do at this but his
by from they we say her she or an will my one all would there their what so up
out if about who get which go me when make can like time no just him know take
people into year your good some could them see other than then now look only come
its over think also back after use two how our work first well way even new want
because any these give day most us is are was were been has had did does said
build create write add fix implement generate design should must never always
game player world block file code project stack simple complete playable
""".split())


def _readable(text: str) -> float:
    """How much does this look like real language rather than OCR garble?

    Frames caught mid-scroll or mid-fade OCR into noise. Left in, that garbage
    pollutes output and blocks merging. Vowel-presence alone is not enough —
    'Dreaks ue largeted DIOCK' passes that — so score on how many tokens are
    actually common English words, and penalize non-ASCII lookalike glyphs.
    """
    if not text.strip():
        return 0.0
    non_ascii = sum(1 for c in text if ord(c) > 127 and c.isalpha())
    if non_ascii / max(len(text), 1) > 0.08:      # Cyrillic/Greek lookalikes
        return 0.0
    toks = re.findall(r"[A-Za-z][A-Za-z'-]*", text)
    if len(toks) < 4:
        return 1.0 if toks else 0.0
    hits = sum(1 for t in toks if t.lower().strip("'-") in COMMON)
    # ordinary prose lands well above 0.25; garble lands near zero
    return min(hits / len(toks) / 0.25, 1.0)


def _tokens(text: str) -> set[str]:
    """Distinctive content words — the fingerprint of a given prompt."""
    return {
        w for w in re.findall(r"[a-z][a-z0-9]{3,}", text.lower())
        if w not in STOP and w not in COMMON
    }


def _same_prompt(a: str, b: str) -> bool:
    """Do two text blocks come from the same prompt?

    Scrolling means two views of one prompt may share no contiguous run at all,
    while OCR noise means they may not match character-for-character either.
    Shared distinctive vocabulary survives both. Normalize by the smaller set so
    a short window still matches the long prompt it came from, but also demand a
    meaningful absolute overlap so two unrelated prompts about the same subject
    don't collapse into one.

    Short blocks carry too few distinctive tokens to fingerprint, so they fall
    back to plain string similarity — that is the frame-to-frame OCR wobble case.
    """
    ta, tb = _tokens(a), _tokens(b)
    if len(ta) >= 4 and len(tb) >= 4:
        inter = len(ta & tb)
        if inter >= 4 and inter / min(len(ta), len(tb)) >= 0.40:
            return True
    na, nb = _norm(a), _norm(b)
    if min(len(na), len(nb)) < 400:
        return difflib.SequenceMatcher(None, na, nb).ratio() >= 0.82
    return False


def _merge(seq: list[tuple[float, str]], thresh: float = 0.72) -> list[dict]:
    """Collapse every view of the same on-screen text into one entry.

    Three things break naive dedupe: OCR wobbles frame to frame, long prompts
    are *scrolled* (so no two frames show the same window), and some frames OCR
    into noise. Contiguous stitching is tried first because it can rebuild the
    full text; vocabulary overlap is the fallback that still groups correctly
    when stitching cannot.
    """
    runs: list[dict] = []
    for ts, text in seq:
        placed = False
        for r in runs:
            merged = _stitch(r["best"], text)
            if merged is None:
                if not _same_prompt(r["best"], text):
                    continue
                # same prompt, non-contiguous view: keep the cleaner reading
                cand = [(r["best"], _readable(r["best"]) * len(r["best"])),
                        (text, _readable(text) * len(text))]
                merged = max(cand, key=lambda x: x[1])[0]
            r["best"] = merged
            r["first"] = min(r["first"], ts)
            r["last"] = max(r["last"], ts)
            r["seen"] += 1
            placed = True
            break
        if not placed:
            runs.append({"first": ts, "last": ts, "seen": 1, "best": text})

    # second pass: fold any run now subsumed by another
    changed = True
    while changed and len(runs) > 1:
        changed = False
        for i in range(len(runs)):
            for j in range(len(runs)):
                if i == j:
                    continue
                merged = _stitch(runs[i]["best"], runs[j]["best"])
                if merged is None and _same_prompt(runs[i]["best"], runs[j]["best"]):
                    cand = [(runs[i]["best"], _readable(runs[i]["best"]) * len(runs[i]["best"])),
                            (runs[j]["best"], _readable(runs[j]["best"]) * len(runs[j]["best"]))]
                    merged = max(cand, key=lambda x: x[1])[0]
                if merged is not None:
                    runs[i]["best"] = merged
                    runs[i]["first"] = min(runs[i]["first"], runs[j]["first"])
                    runs[i]["last"] = max(runs[i]["last"], runs[j]["last"])
                    runs[i]["seen"] += runs[j]["seen"]
                    runs.pop(j)
                    changed = True
                    break
            if changed:
                break
    return runs


def _hhmmss(sec: float) -> str:
    sec = int(sec)
    h, m, s = sec // 3600, (sec % 3600) // 60, sec % 60
    return f"{h:d}:{m:02d}:{s:02d}" if h else f"{m:d}:{s:02d}"


# ---------------------------------------------------------------------------
# Pipeline
# ---------------------------------------------------------------------------

def extract(source: str, fps: float = 1.0, min_score: float = 2.0,
            all_text: bool = False, keep: bool = False, log=print) -> dict:
    if not shutil.which("ffmpeg"):
        raise RuntimeError("ffmpeg is not on PATH")

    workdir = Path(tempfile.mkdtemp(prefix="promptex-"))
    try:
        video = _fetch(source, workdir, log)
        frames = _frames(video, workdir, fps, log)
        if not frames:
            return {"source": source, "prompts": [], "error": "no frames extracted"}
        frames = _dedupe(frames, log)

        binary = _vision_binary(log)
        if binary:
            log("  OCR backend: macOS Vision")
            per_frame = _ocr_vision(binary, frames, log)
        elif shutil.which("tesseract"):
            log("  OCR backend: tesseract")
            per_frame = _ocr_tesseract(frames, log)
        else:
            raise RuntimeError("no OCR backend (need macOS swiftc, or tesseract on PATH)")

        idx = {f: int(re.search(r"f(\d+)\.jpg", f.name).group(1)) for f in frames}
        candidates: list[tuple[float, str]] = []
        everything: list[tuple[float, str]] = []
        for f in frames:
            ts = (idx[f] - 1) / fps
            for b in _blocks(per_frame.get(str(f), [])):
                everything.append((ts, b))
                if all_text or _score(b) >= min_score:
                    candidates.append((ts, b))

        runs = _merge(candidates)
        runs.sort(key=lambda r: r["first"])
        prompts = [
            {
                "at": _hhmmss(r["first"]),
                "at_seconds": round(r["first"], 1),
                "on_screen_seconds": round(max(r["last"] - r["first"], 1 / fps), 1),
                "score": round(_score(r["best"]), 2),
                "text": r["best"],
            }
            for r in runs
        ]
        return {
            "source": source,
            "video": video.name,
            "frames_sampled": len(frames),
            "distinct_text_blocks": len(_merge(everything)),
            "prompts": prompts,
        }
    finally:
        if keep:
            log(f"  workdir kept: {workdir}")
        else:
            shutil.rmtree(workdir, ignore_errors=True)


def to_markdown(res: dict) -> str:
    out = [f"# Prompts extracted from {res.get('source','')}", ""]
    out.append(
        f"_{len(res.get('prompts', []))} distinct prompts from "
        f"{res.get('frames_sampled', 0)} sampled frames._"
    )
    out.append("")
    for i, p in enumerate(res.get("prompts", []), 1):
        out.append(f"## {i}. `{p['at']}`  ({p['on_screen_seconds']}s on screen)")
        out.append("")
        out.append("```text")
        out.append(p["text"])
        out.append("```")
        out.append("")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# RAPP agent
# ---------------------------------------------------------------------------

class PromptExtractorAgent(BasicAgent):
    def __init__(self):
        self.name = "ExtractPrompts"
        self.metadata = {
            "name": self.name,
            "description": (
                "Extract the prompts shown on screen in a video (YouTube URL or local "
                "file) by OCRing it frame by frame, so they don't have to be copied "
                "down by hand. Returns each distinct prompt once with its timestamp."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {"type": "string", "description": "Video URL or local file path"},
                    "fps": {"type": "number", "description": "Frames sampled per second (default 1.0; 0.5 is faster, 2 catches quick cuts)"},
                    "min_score": {"type": "number", "description": "Prompt-likeness threshold, default 2.0. Lower to catch more."},
                    "all_text": {"type": "boolean", "description": "Return every text block, not just prompt-like ones"},
                    "save_to": {"type": "string", "description": "Optional path to write the full markdown result"},
                },
                "required": ["url"],
            },
        }
        super().__init__(self.name, self.metadata)

    def perform(self, **kwargs):
        url = (kwargs.get("url") or "").strip()
        if not url:
            return "Give me a video URL or a local file path."
        try:
            res = extract(
                url,
                fps=float(kwargs.get("fps") or 1.0),
                min_score=float(kwargs.get("min_score") or 2.0),
                all_text=bool(kwargs.get("all_text")),
                log=lambda *a: None,
            )
        except Exception as e:
            return f"Extraction failed: {e}"

        prompts = res.get("prompts", [])
        if not prompts:
            return (
                f"No prompt-like text found in {res.get('frames_sampled',0)} sampled "
                f"frames ({res.get('distinct_text_blocks',0)} text blocks seen). "
                "Try min_score=1.0, fps=2, or all_text=true."
            )

        if kwargs.get("save_to"):
            try:
                p = Path(kwargs["save_to"]).expanduser()
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(to_markdown(res))
            except Exception as e:
                return f"Extracted {len(prompts)} prompts but could not write file: {e}"

        lines = [f"{len(prompts)} prompt(s) found in {res.get('video','the video')}:", ""]
        for i, p in enumerate(prompts, 1):
            lines.append(f"[{i}] {p['at']} ({p['on_screen_seconds']}s on screen)")
            lines.append(p["text"])
            lines.append("")
        if kwargs.get("save_to"):
            lines.append(f"(full markdown written to {kwargs['save_to']})")
        return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(prog="extractprompts",
                             description="Extract on-screen prompts from a video.")
    ap.add_argument("source", help="YouTube URL or local video file")
    ap.add_argument("--fps", type=float, default=1.0, help="frames sampled per second (default 1.0)")
    ap.add_argument("--min-score", type=float, default=2.0, help="prompt-likeness threshold (default 2.0)")
    ap.add_argument("--all-text", action="store_true", help="dump every text block, not just prompts")
    ap.add_argument("--json", help="write raw JSON here")
    ap.add_argument("--md", help="write markdown here")
    ap.add_argument("--keep", action="store_true", help="keep the temp workdir")
    a = ap.parse_args()

    res = extract(a.source, fps=a.fps, min_score=a.min_score,
                  all_text=a.all_text, keep=a.keep)

    if a.json:
        Path(a.json).write_text(json.dumps(res, indent=2))
        print(f"  json -> {a.json}")
    if a.md:
        Path(a.md).write_text(to_markdown(res))
        print(f"  md   -> {a.md}")

    print(f"\n{len(res['prompts'])} prompt(s) from {res['frames_sampled']} sampled frames\n")
    for i, p in enumerate(res["prompts"], 1):
        print(f"[{i}] {p['at']}  ({p['on_screen_seconds']}s on screen, score {p['score']})")
        print(p["text"])
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
