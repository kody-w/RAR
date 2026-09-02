---
name: "rar-kody-w-prompt-extractor"
description: "Extract the prompts shown on screen in a video (YouTube URL or local file) by OCRing it frame by frame, so they don't have to be copied down by hand. Returns each distinct prompt once with its timestamp."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/prompt_extractor", "rar_sha256": "9b03c1b6d286d219e1f19966eea18eb2ef9c980213455963226b264c038440ba", "source_kind": "rar-agent", "source_commit": "9999f14cefcf8304a191538a68016a06fb59a4c8", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "prompt_extractor_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/prompt-extractor:b224bc39293bd414700e2914c429c62d9ebbc52f6d2452017c3f0fdd59a02a03", "kind": "skill"}, "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["ocr", "video", "prompts", "extraction", "vision"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/prompt_extractor`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `prompt_extractor_agent.py` is
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
