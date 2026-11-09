#!/usr/bin/env python3
"""
run.py - lets any AI that can run a shell command use agent files as its own tools.

  python3 run.py list [folder]                 -> every tool: name, description, parameters (JSON)
  python3 run.py fire <Name> '<json>' [folder] -> runs that tool, prints its result

folder defaults to ./agents next to this file, or this file's own folder. An agent file is any *_agent.py
holding a class with `metadata` (a function schema) and `perform(**kwargs)`.
Files are read fresh on every call, so a new file is a new tool immediately.
Standard library only. Python 3.8+.
"""
import glob
import importlib.util
import json
import os
import sys
import types

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT = os.path.join(HERE, "agents") if os.path.isdir(DEFAULT) else HERE

BASE = '''
class BasicAgent:
    def __init__(self, name=None, metadata=None):
        if name is not None: self.name = name
        elif not hasattr(self, "name"): self.name = "BasicAgent"
        if metadata is not None: self.metadata = metadata
        elif not hasattr(self, "metadata"):
            self.metadata = {"name": self.name, "description": "", "parameters": {"type": "object", "properties": {}}}
    def perform(self, **kwargs): return "Not implemented."
    def system_context(self): return None
'''


def _base(folder):
    """The shared base class: the folder's basic_agent.py if present, else the built-in one."""
    mod = types.ModuleType("agents.basic_agent")
    path = os.path.join(folder, "basic_agent.py")
    code = open(path).read() if os.path.exists(path) else BASE
    exec(compile(code, path, "exec"), mod.__dict__)
    pkg = types.ModuleType("agents")
    pkg.__path__ = [folder]
    pkg.basic_agent = mod
    sys.modules["agents"], sys.modules["agents.basic_agent"] = pkg, mod
    sys.modules["basic_agent"] = mod
    # Agents written for the cloud import utils.azure_file_storage; map it to a
    # local_storage.py beside the folder (as the Brainstem does) when one exists.
    for d in (folder, os.path.dirname(folder)):
        ls = os.path.join(d, "local_storage.py")
        if os.path.exists(ls) and "utils.azure_file_storage" not in sys.modules:
            spec = importlib.util.spec_from_file_location("utils.azure_file_storage", ls)
            store = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(store)
            utils = types.ModuleType("utils")
            utils.azure_file_storage = store
            sys.modules["utils"], sys.modules["utils.azure_file_storage"] = utils, store
            break
    return mod.BasicAgent


def load(folder):
    folder = os.path.abspath(folder)
    sys.path.insert(0, folder)
    Base = _base(folder)
    files = sorted(glob.glob(os.path.join(folder, "*_agent.py")))
    files = [f for f in files if os.path.basename(f) != "basic_agent.py"]
    tools, broken = {}, {}
    # Two passes, like a server that reloads files on every request: an agent that
    # watches other agents sees all of them, whatever order the files sort in.
    for _ in range(2):
        tools = {}
        for f in files:
            try:
                spec = importlib.util.spec_from_file_location("agent_" + os.path.basename(f)[:-3], f)
                m = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(m)
                for v in vars(m).values():
                    if isinstance(v, type) and issubclass(v, Base) and v is not Base and v.__module__ == m.__name__:
                        a = v()
                        tools[a.metadata.get("name", a.name)] = a
            except Exception as e:
                broken[os.path.basename(f)] = f"{type(e).__name__}: {e}"
    return tools, broken


def main(argv):
    if len(argv) < 2 or argv[1] not in ("list", "fire"):
        print(__doc__)
        return 2
    if argv[1] == "list":
        tools, broken = load(argv[2] if len(argv) > 2 else DEFAULT)
        out = {"tools": [t.metadata for t in tools.values()]}
        context = [c for c in (t.system_context() for t in tools.values()) if c]
        if context:
            out["context"] = context
        if broken:
            out["broken"] = broken
        print(json.dumps(out, indent=2))
        return 0
    if len(argv) < 3:
        print("usage: run.py fire <Name> '<json args>' [folder]")
        return 2
    args = json.loads(argv[3]) if len(argv) > 3 and argv[3].strip() else {}
    tools, broken = load(argv[4] if len(argv) > 4 else DEFAULT)
    if argv[2] not in tools:
        print(json.dumps({"error": f"no tool named {argv[2]!r}", "tools": sorted(tools)}))
        return 1
    try:
        result = tools[argv[2]].perform(**args)
    except Exception as e:
        print(json.dumps({"error": f"{type(e).__name__}: {e}"}))
        return 1
    print(result if isinstance(result, str) else json.dumps(result, indent=2, default=str))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
