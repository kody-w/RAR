---
name: "rar-kody-w-prompt-extractor"
description: "Extract the prompts shown on screen in a video (YouTube URL or local file) by OCRing it frame by frame, so they don't have to be copied down by hand. Returns each distinct prompt once with its timestamp."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/prompt_extractor", "rar_sha256": "9b03c1b6d286d219e1f19966eea18eb2ef9c980213455963226b264c038440ba", "source_kind": "rar-agent", "source_commit": "9999f14cefcf8304a191538a68016a06fb59a4c8", "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["ocr", "video", "prompts", "extraction", "vision"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `prompt_extractor_agent.py` and embedded as the fenced Python below (sha256 9b03c1b6d286d219…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `prompt_extractor_agent.py` first:

```bash
python3 prompt_extractor_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 prompt_extractor_agent.py   # or on stdin
python3 prompt_extractor_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
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
