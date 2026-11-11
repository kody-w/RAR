#!/usr/bin/env python3
"""walkthrough.py - the walkthrough SDK. Optional: anyone publishing an agent.py, stack or distro can add a
simulated Windows 11 click-through that shows it working, so people follow it instead of reading.

  python3 walkthrough.py new <name> <file it shows>   start walkthroughs/<name>.json, pinned to that file
  python3 walkthrough.py check [file.json ...]        check walkthroughs (default: all in walkthroughs/)
  python3 walkthrough.py repin <file.json>            after the shown file changed and you re-checked the steps

A walkthrough is data only. player.html shows its words as text, so it can never run code.
Play one: player.html?w=<name>"""
import hashlib, json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent  # repo root when this lives at stacks/walkthroughs/
SCHEMA = "rapp-walkthrough/0.1"
WINDOWS = {"browser", "terminal", "chat", "explorer", "desktop"}
STEP_KEYS = {"caption", "window", "title", "rows", "chat", "lines", "files", "button", "click", "type", "toast"}
MAX_STEPS, MAX_TEXT = 20, 400

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def texts(step):
    for k in ("caption", "title", "button", "type", "toast"):
        if k in step: yield step[k]
    for k in ("rows", "chat", "files"):
        for item in step.get(k, []):
            yield from item
    yield from step.get("lines", [])

def check(path, root=ROOT):
    """Return (errors, warnings). Errors block a merge; a stale pin is a warning ("may be out of date")."""
    errs, warns = [], []
    try:
        d = json.loads(Path(path).read_text())
    except Exception as e:
        return [f"not valid JSON: {e}"], []
    name = Path(path).stem
    if d.get("schema") != SCHEMA: errs.append(f"schema must be {SCHEMA}")
    if d.get("name") != name or not re.fullmatch(r"[a-z0-9-]+", name): errs.append("name must match the file name (a-z, 0-9, -)")
    if not d.get("title"): errs.append("needs a title")
    if d.get("machine") != "windows-11": errs.append("machine must be windows-11")
    if d.get("simulated") is not True: errs.append("simulated must be true (walkthroughs are drawn, never recordings)")
    shows = d.get("shows") or {}
    target = root / str(shows.get("file", ""))
    if not shows.get("file") or not target.is_file(): errs.append(f"shows.file not found in this repo: {shows.get('file')}")
    elif shows.get("sha256") != sha(target): warns.append(f"{shows['file']} changed since this walkthrough was made: may be out of date (re-check the steps, then repin)")
    steps = d.get("steps")
    if not isinstance(steps, list) or not 1 <= len(steps) <= MAX_STEPS: errs.append(f"needs 1 to {MAX_STEPS} steps"); steps = []
    for n, s in enumerate(steps, 1):
        if not isinstance(s, dict): errs.append(f"step {n}: must be an object"); continue
        extra = set(s) - STEP_KEYS
        if extra: errs.append(f"step {n}: unknown keys {sorted(extra)}")
        if not s.get("caption"): errs.append(f"step {n}: needs a caption")
        if s.get("window") not in WINDOWS: errs.append(f"step {n}: window must be one of {sorted(WINDOWS)}")
        if s.get("click") not in (None, "button"): errs.append(f"step {n}: click can only be \"button\"")
        if s.get("click") == "button" and not s.get("button"): errs.append(f"step {n}: click needs a button to click")
        for k, width in (("rows", (2, 3)), ("chat", (2,)), ("files", (2,))):
            for item in s.get(k, []):
                if not isinstance(item, list) or len(item) not in width or not all(isinstance(x, str) for x in item):
                    errs.append(f"step {n}: each {k} entry must be a list of {' or '.join(map(str, width))} strings")
        for item in s.get("chat", []):
            if item and item[0] not in ("you", "ai"): errs.append(f"step {n}: chat speaker must be you or ai")
        for t in texts(s):
            if not isinstance(t, str): errs.append(f"step {n}: all text must be strings"); continue
            if len(t) > MAX_TEXT: errs.append(f"step {n}: text over {MAX_TEXT} characters")
    return errs, warns

def main(argv):
    if not argv or argv[0] in ("-h", "--help"): print(__doc__); return 0
    cmd, rest = argv[0], argv[1:]
    if cmd == "new":
        name, shows = rest[0], rest[1]
        out = HERE / "walkthroughs" / f"{name}.json"
        if out.exists(): sys.exit(f"{out} already exists")
        d = {"schema": SCHEMA, "name": name, "title": "Show it working", "machine": "windows-11",
             "shows": {"file": shows, "sha256": sha(ROOT / shows)}, "simulated": True,
             "steps": [{"caption": "What the person does first, in one plain sentence.", "window": "chat", "title": "Your AI",
                        "chat": [["you", "What they say"], ["ai", "What comes back"]]}]}
        out.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n"); print(f"wrote {out}\nplay: player.html?w={name}"); return 0
    if cmd == "repin":
        p = Path(rest[0]); d = json.loads(p.read_text()); d["shows"]["sha256"] = sha(ROOT / d["shows"]["file"])
        p.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n"); print(f"repinned {p.name}"); return 0
    if cmd == "check":
        files = [Path(f) for f in rest] or sorted((HERE / "walkthroughs").glob("*.json"))
        bad = 0
        for f in files:
            errs, warns = check(f)
            for w in warns: print(f"{f.name}: warning: {w}")
            for e in errs: print(f"{f.name}: {e}")
            bad += bool(errs)
            if not errs: print(f"{f.name}: ok ({len(json.loads(f.read_text())['steps'])} steps)")
        print(f"{len(files) - bad} of {len(files)} walkthroughs pass"); return 1 if bad else 0
    print(__doc__); return 2

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
