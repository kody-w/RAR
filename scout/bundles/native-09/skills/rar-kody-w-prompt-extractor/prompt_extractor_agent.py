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
