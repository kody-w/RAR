#!/usr/bin/env python3
"""Bundle an agent.py into one .agentcard that carries what it needs to run on a phone (status: staging).

Everything the agent imports that a phone's Python lacks rides INSIDE the card, fingerprinted:
  - a sibling agent file it imports (e.g. `from ez_sharpen_agent import ...`) -> lib/<name>.py
  - a package with a pure-Python wheel (py3-none-any)                        -> lib/<wheel>.whl (+ its dependencies)
Compiled packages cannot run on a phone, so they are left out and named in the report.
An import inside `try: ... except ImportError` whose block also needs a compiled package is skipped:
that block fails on the phone anyway, so carrying the rest would only add weight.

Usage: bundle_card.py <agent.py> --out <file.agentcard> [--name ToolName] [--author A] [--report r.json]
Needs: python3.13 (the phone's version) on the PATH as `python3.13` for pip, network for PyPI.
"""
import argparse, ast, base64, hashlib, json, shutil, subprocess, sys, tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
PHONE_PY = "3.13"
SHIMS = {"agents", "utils", "openrappter", "basic_agent", "local_storage", "__future__"}
IN_APP = {"requests", "urllib3", "idna", "certifi", "charset_normalizer"}   # the phone app already bundles these
# Import name -> PyPI name. ONLY these (or what an agent declares in its own PEP 723 block) are ever fetched:
# guessing a package from an import name is how dependency-confusion attacks get in (Birsan, 2021).
KNOWN = {"pypdf": "pypdf", "PyPDF2": "PyPDF2", "jsonschema": "jsonschema", "openai": "openai", "anthropic": "anthropic",
         "markdown": "markdown", "tabulate": "tabulate", "feedparser": "feedparser", "pytz": "pytz", "six": "six",
         "packaging": "packaging", "toml": "toml", "tomli": "tomli", "xmltodict": "xmltodict", "et_xmlfile": "et_xmlfile",
         "openpyxl": "openpyxl", "httpx": "httpx", "jinja2": "jinja2", "flask": "flask"}
DIST = {"yaml": "pyyaml", "docx": "python-docx", "pptx": "python-pptx", "PIL": "pillow", "bs4": "beautifulsoup4",
        "dateutil": "python-dateutil", "dotenv": "python-dotenv", "sklearn": "scikit-learn", "cv2": "opencv-python",
        "jwt": "pyjwt", "Crypto": "pycryptodome", "fitz": "pymupdf"}


def top(name): return name.split(".")[0]


def _mods(nodes):
    out = []
    for n in nodes:
        if isinstance(n, ast.Import): out += [top(a.name) for a in n.names]
        elif isinstance(n, ast.ImportFrom) and n.module and n.level == 0: out.append(top(n.module))
    return out


def import_groups(source: str):
    """[(modules, kind, group)]. kind: "required" (module-level import), "lazy" (inside a function: needed only
    when that feature runs), "try" (the body of a try/except), or
    "fallback" (an import inside that try's except branches, used only when the try body cannot be carried).
    group ties a try body to its fallbacks."""
    tree, groups, seen = ast.parse(source), [], set()

    def visit(node, gid=None, kind="required"):
        if isinstance(node, ast.Try) and node.handlers:
            g = id(node)
            body = [n for st in node.body for n in ast.walk(st) if isinstance(n, (ast.Import, ast.ImportFrom))]
            seen.update(id(n) for n in body)
            if _mods(body): groups.append((_mods(body), "fallback" if kind == "fallback" else "try", gid if kind == "fallback" else g))
            for h in node.handlers:
                for st in h.body: visit(st, gid if kind == "fallback" else g, "fallback")
            for st in node.orelse + node.finalbody: visit(st, gid, kind)
            return
        if isinstance(node, (ast.Import, ast.ImportFrom)) and id(node) not in seen:
            seen.add(id(node))
            if _mods([node]): groups.append((_mods([node]), kind, gid))
            return
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and kind == "required":
            kind = "lazy"     # imported only when that feature runs: optional for loading
        for child in ast.iter_child_nodes(node): visit(child, gid, kind)

    visit(tree)
    return groups


def declared(source: str) -> dict:
    """PEP 723 inline metadata: '# /// script' ... 'dependencies = [...]' ... '# ///' -> {import-ish name: dist}."""
    import re
    m = re.search(r"(?ms)^# /// script\s*$(.*?)^# ///\s*$", source)
    if not m: return {}
    body = "\n".join(l[2:] if l.startswith("# ") else l[1:] for l in m.group(1).splitlines())
    try:
        import tomllib
        deps = tomllib.loads(body).get("dependencies", [])
    except Exception:
        return {}
    out = {}
    for d in deps:
        name = re.split(r"[<>=!~;\[ ]", d, 1)[0].strip()
        if name: out[name.replace("-", "_").lower()] = d
    return out


def needs(m): return m not in sys.stdlib_module_names and m not in SHIMS and m not in IN_APP


def pure_wheels(dist: str, cache: Path):
    """Pure-Python wheels for dist and its dependencies, or None if any piece is compiled."""
    d = cache / dist
    if not d.exists():
        d.mkdir(parents=True)
        r = subprocess.run([sys.executable, "-m", "pip", "download", "-q", "-d", str(d), "--platform", "any",
                            "--python-version", PHONE_PY, "--only-binary=:all:", "--implementation", "py", dist],
                           capture_output=True, text=True)
        if r.returncode != 0:
            shutil.rmtree(d); d.mkdir(); (d / ".compiled").write_text(r.stderr[-400:])
    if (d / ".compiled").exists(): return None
    return sorted(d.glob("*.whl"))


def bundle(agent: Path, name=None, author="", cache=None):
    sys.path.insert(0, str(HERE / "vendor"))
    import pocket_host as h, agentcard_core as cards
    cache = cache or Path(tempfile.mkdtemp(prefix="wheels-"))
    home = Path(tempfile.mkdtemp(prefix="bundle-home-"))
    h.handle(json.dumps({"op": "init", "home": str(home)}))
    card = h.pack_file(agent, author=author, name=name)   # raises when the agent cannot even load here
    files, report, done = {}, {"carried": [], "left_out": [], "skipped_optional": []}, set()
    queue = [(agent, agent.read_text(encoding="utf-8"))]
    while queue:
        path, src = queue.pop(0)
        groups = import_groups(src)
        carried_try = set()      # try blocks whose body rides on the card: their fallbacks are not needed
        for mods, optional, gid in groups:
            mods = [m for m in dict.fromkeys(mods) if needs(m)]
            if not mods: continue
            plan, blocked = [], None
            for m in mods:
                sib = path.parent / f"{m}.py"
                if sib.is_file(): plan.append(("py", m, sib)); continue
                decl = declared(src)
                dist = decl.get(m.lower()) or decl.get(DIST.get(m, m).replace("-", "_").lower()) or KNOWN.get(m)
                if dist is None:
                    blocked = m; report.setdefault("unknown", []).append(m); break
                whl = pure_wheels(dist, cache)
                if whl is None: blocked = m; break
                plan.append(("whl", m, whl))
            if optional == "fallback" and gid in carried_try: continue
            if blocked:
                if not any(r["compiled"] == blocked for r in report["left_out"] + report["skipped_optional"]):
                    (report["left_out"] if optional == "required" else report["skipped_optional"]).append({"modules": mods, "compiled": blocked})
                continue
            if optional == "try": carried_try.add(gid)
            for kind, m, what in plan:
                if m in done: continue
                done.add(m)
                if kind == "py":
                    files[f"lib/{what.name}"] = what.read_bytes(); report["carried"].append(f"{m} (sibling file)")
                    queue.append((what, what.read_text(encoding="utf-8")))
                else:
                    for w in what: files[f"lib/{w.name}"] = w.read_bytes()
                    report["carried"].append(f"{m} ({', '.join(w.name for w in what)})")
    if files:
        card["files"] = [{"path": p, "sha256": hashlib.sha256(b).hexdigest(), "b64": base64.b64encode(b).decode()}
                         for p, b in sorted(files.items())]
    probs = cards.problems(card)
    if probs: raise SystemExit("card problems: " + "; ".join(probs))
    shutil.rmtree(home, ignore_errors=True)
    return card, report


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("agent"); ap.add_argument("--out", required=True); ap.add_argument("--name")
    ap.add_argument("--author", default=""); ap.add_argument("--report"); ap.add_argument("--cache")
    a = ap.parse_args()
    card, rep = bundle(Path(a.agent), a.name, a.author, Path(a.cache) if a.cache else None)
    sys.path.insert(0, str(HERE / "vendor")); import agentcard_core as cards
    Path(a.out).write_text(cards.to_json(card))
    if a.report: Path(a.report).write_text(json.dumps(rep, indent=1))
    print(json.dumps({"card": a.out, "files": [f["path"] for f in card.get("files", [])], **rep}))
