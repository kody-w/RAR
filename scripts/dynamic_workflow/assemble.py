"""Assemble agents/@kody-w/dynamic_workflow_agent.py from its parts: agent.src.py, the engine (runner.mjs), the Copilot
extension (extension.mjs) and the built-in workflows (workflows/<name>.run.js + .meta.json + .version).
Usage: python3 scripts/dynamic_workflow/assemble.py [out.py] [workflow names...]"""
import json, os, sys
here = os.path.dirname(os.path.abspath(__file__))
wf = os.path.join(here, "workflows")
repo = os.path.dirname(os.path.dirname(here))
out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(repo, "agents", "@kody-w", "dynamic_workflow_agent.py")
read = lambda p: open(p, encoding="utf-8").read()
src = read(os.path.join(here, "agent.src.py"))
parts = {"__RUNNER_JS__": read(os.path.join(here, "runner.mjs")), "__EXTENSION_JS__": read(os.path.join(here, "extension.mjs"))}
names = sys.argv[2:] or ["adversarial-fleet", "reflect"]
entries = []
for name in names:
    mp, rp = os.path.join(wf, name + ".meta.json"), os.path.join(wf, name + ".run.js")
    if not (os.path.exists(mp) and os.path.exists(rp)):
        print("skip builtin (not written yet):", name); continue
    meta, run = read(mp).strip(), read(rp).rstrip("\n")
    json.loads(meta)
    assert "'''" not in meta and "'''" not in run, name
    vp = os.path.join(wf, name + ".version")
    version = read(vp).strip() if os.path.exists(vp) else "1.0.0"
    entries.append('    %r: {\n        "version": %r,\n        "meta": json.loads(r\'\'\'%s\'\'\'),\n        "run": r\'\'\'%s\'\'\',\n    },\n' % (name, version, meta, run))
parts["__BUILTINS__"] = "{\n" + "".join(entries) + "}"
for k, v in parts.items():
    assert src.count(k) == 1, k
    if k != "__BUILTINS__":
        assert "'''" not in v, k
    src = src.replace(k, v)
open(out, "w", encoding="utf-8").write(src)
print("wrote", out, len(src), "chars; builtins:", [n for n in names if os.path.exists(os.path.join(wf, n + ".run.js"))])
