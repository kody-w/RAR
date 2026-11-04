---
name: "rar-kody-w-prompt-extractor"
description: "Extract the prompts shown on screen in a video (YouTube URL or local file) by OCRing it frame by frame, so they don't have to be copied down by hand. Returns each distinct prompt once with its timestamp."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/prompt_extractor", "rar_sha256": "ece05fd7f282eb9dc85f002df0fd03cd09ba82cfcb8c2acb1a54eaf83279747d", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["ocr", "video", "prompts", "extraction", "vision"]}
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
