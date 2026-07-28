#!/usr/bin/env python3
"""
agent_harness.py — actually run a registry agent, so a review can cite behavior.

A critic that only reads source is a linter with opinions. This harness loads an
agent through the *real* local brainstem loader (`_load_agent_from_file`, with its
shims, validation and quarantine rules), instantiates it, and calls `perform()`
for real. What comes back — output, exceptions, timing, contract violations — is
the evidence the critic panel reviews.

Three execution tiers, tried in order:

  1. brainstem-live     the running brainstem at 127.0.0.1:7071 loads the file via
                        POST /agents/import, and it is removed again afterwards
  2. brainstem-loader   the brainstem's own loader imported directly from
                        ~/.brainstem/src/rapp_brainstem — same code path, no
                        mutation of the running instance
  3. standalone         a plain importlib load with a BasicAgent shim, for machines
                        with no brainstem installed

Everything runs in a subprocess with a hard timeout, because agent code is
third-party code. The harness never raises: a failure to run IS the finding.

Usage:
    python scripts/agent_harness.py agents/@rapp/learn_new_agent.py
    python scripts/agent_harness.py <file> --timeout 45 --json
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BRAINSTEM_SRC = Path.home() / ".brainstem" / "src" / "rapp_brainstem"
BRAINSTEM_PY = Path.home() / ".brainstem" / "venv" / "bin" / "python"
BRAINSTEM_URL = os.environ.get("BRAINSTEM_URL", "http://127.0.0.1:7071")
DEFAULT_TIMEOUT = 60

# Runs inside the subprocess. Kept as a string so the parent never imports agent code.
CHILD = r'''
import importlib.util, io, json, os, sys, time, traceback
from contextlib import redirect_stdout, redirect_stderr

target = sys.argv[1]
bs_src = sys.argv[2]
mode = sys.argv[3]

out = {"mode": mode, "loaded": False, "classes": [], "calls": [], "errors": [],
       "stdout_chars": 0, "load_seconds": 0.0}

def _shim_basic_agent():
    """Standalone tier: provide BasicAgent so the agent file can import it."""
    import types
    for name in ("basic_agent", "agents.basic_agent"):
        if name in sys.modules:
            continue
        m = types.ModuleType(name)
        class BasicAgent:
            def __init__(self, name=None, metadata=None):
                if name is not None: self.name = name
                elif not hasattr(self, "name"): self.name = "BasicAgent"
                if metadata is not None: self.metadata = metadata
                elif not hasattr(self, "metadata"):
                    self.metadata = {"name": self.name, "description": "",
                                     "parameters": {"type": "object", "properties": {}, "required": []}}
            def perform(self, **kw): return "Not implemented."
        m.BasicAgent = BasicAgent
        sys.modules[name] = m
    if "agents" not in sys.modules:
        pkg = types.ModuleType("agents"); pkg.__path__ = []
        sys.modules["agents"] = pkg

def sample_args(meta):
    """Synthesize plausible arguments from the agent's own parameter schema."""
    params = (meta or {}).get("parameters") or {}
    props = params.get("properties") or {}
    required = params.get("required") or []
    # Required params, plus a couple of free-text optionals — a real caller names
    # the thing it is asking about, and the sensitivity probe needs something to vary.
    keys = list(required)
    for k, spec in props.items():
        if len(keys) >= len(required) + 2:
            break
        if k in keys:
            continue
        if spec.get("type", "string") == "string" and not spec.get("enum"):
            keys.append(k)
    args = {}
    for key in (keys or list(props)[:3]):
        spec = props.get(key) or {}
        t = spec.get("type", "string")
        if "enum" in spec and spec["enum"]:
            args[key] = spec["enum"][0]
        elif t == "integer": args[key] = 1
        elif t == "number": args[key] = 1.0
        elif t == "boolean": args[key] = True
        elif t == "array": args[key] = []
        elif t == "object": args[key] = {}
        else: args[key] = "harness probe"
    return args

buf = io.StringIO()
t0 = time.time()
instances = {}
try:
    with redirect_stdout(buf), redirect_stderr(buf):
        if mode == "brainstem-loader":
            sys.path.insert(0, bs_src)
            sys.path.insert(0, os.path.join(bs_src, "agents"))
            from brainstem import _load_agent_from_file
            instances = _load_agent_from_file(target) or {}
        else:
            _shim_basic_agent()
            sys.path.insert(0, os.path.dirname(os.path.abspath(target)))
            spec = importlib.util.spec_from_file_location("harness_target", target)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            from basic_agent import BasicAgent
            for attr in dir(mod):
                cls = getattr(mod, attr)
                if (isinstance(cls, type) and cls.__module__ == mod.__name__
                        and hasattr(cls, "perform") and not attr.startswith("_")
                        and attr != "BasicAgent"):
                    inst = cls()
                    instances[getattr(inst, "name", attr)] = inst
    out["loaded"] = bool(instances)
    out["classes"] = sorted(instances.keys())
except BaseException as e:
    out["errors"].append({"stage": "load", "type": type(e).__name__,
                          "message": str(e)[:400], "trace": traceback.format_exc()[-700:]})
out["load_seconds"] = round(time.time() - t0, 3)

for name, inst in list(instances.items())[:3]:
    meta = getattr(inst, "metadata", {}) or {}
    args = sample_args(meta)
    call = {"agent": name, "args": args, "declared_params": list(((meta.get("parameters") or {}).get("properties") or {}).keys())}
    b = io.StringIO()
    t1 = time.time()
    try:
        with redirect_stdout(b), redirect_stderr(b):
            res = inst.perform(**args)
        call["seconds"] = round(time.time() - t1, 3)
        call["ok"] = True
        call["return_type"] = type(res).__name__
        call["returns_str"] = isinstance(res, str)
        text = res if isinstance(res, str) else repr(res)
        call["output_chars"] = len(text)
        call["output_preview"] = text[:700]
        call["empty"] = not str(text).strip()
    except BaseException as e:
        call["seconds"] = round(time.time() - t1, 3)
        call["ok"] = False
        call["exception"] = type(e).__name__
        call["message"] = str(e)[:400]
        call["trace"] = traceback.format_exc()[-600:]
    call["printed_chars"] = len(b.getvalue())
    out["calls"].append(call)

    # Input-sensitivity probe: does this agent actually compute from its inputs,
    # or does it return the same canned output no matter what it is asked?
    _props = ((meta or {}).get("parameters") or {}).get("properties") or {}
    _CONTROL = ("operation", "action", "mode", "command", "op", "method", "type", "format")
    # Only vary free-text arguments. Mutating an operation/enum argument just
    # produces an "unknown operation" error that echoes the sentinel back and
    # would look, falsely, like input sensitivity.
    str_keys = [k for k, v in args.items()
                if isinstance(v, str)
                and not (_props.get(k) or {}).get("enum")
                and k.lower() not in _CONTROL]
    if str_keys and call.get("ok") and call.get("output_preview") is not None:
        variants = []
        # Deliberately absurd names — a real fixture must not collide with these.
        for sentinel in ("Qwertzuiop Holdings BV", "Zzyzx Vantablack LLC"):
            v_args = dict(args)
            for k in str_keys:
                v_args[k] = sentinel
            b3 = io.StringIO()
            try:
                with redirect_stdout(b3), redirect_stderr(b3):
                    rv = inst.perform(**v_args)
                variants.append({"args": v_args, "ok": True,
                                 "text": rv if isinstance(rv, str) else repr(rv)})
            except BaseException as e:
                variants.append({"args": v_args, "ok": False,
                                 "exception": type(e).__name__, "message": str(e)[:200]})
        base_text = call.get("output_preview") or ""
        try:
            with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
                base_full = inst.perform(**args)
            base_text = base_full if isinstance(base_full, str) else repr(base_full)
        except BaseException:
            pass
        ok_variants = [v for v in variants if v.get("ok")]
        identical = [v for v in ok_variants if v["text"] == base_text]
        sens = {
            "tested": True,
            "variants": len(variants),
            "identical_outputs": len(identical),
            "ignores_input": bool(ok_variants) and len(identical) == len(ok_variants),
            "sentinel_echoed": any("qwertzuiop" in v["text"].lower() or "zzyzx" in v["text"].lower()
                                   for v in ok_variants),
            "sample": (ok_variants[0]["text"][:400] if ok_variants else ""),
            "errors": [v for v in variants if not v.get("ok")][:2],
        }
        out["input_sensitivity"] = sens

    # Contract probe: a no-argument call must not explode either.
    if args:
        b2 = io.StringIO()
        try:
            with redirect_stdout(b2), redirect_stderr(b2):
                r2 = inst.perform()
            out["calls"].append({"agent": name, "args": {}, "probe": "no-args", "ok": True,
                                 "returns_str": isinstance(r2, str),
                                 "output_chars": len(r2 if isinstance(r2, str) else repr(r2))})
        except BaseException as e:
            out["calls"].append({"agent": name, "args": {}, "probe": "no-args", "ok": False,
                                 "exception": type(e).__name__, "message": str(e)[:300]})

out["stdout_chars"] = len(buf.getvalue())
out["stdout_preview"] = buf.getvalue()[:400]
print("___HARNESS___" + json.dumps(out))
'''


def _run_child(target, mode, timeout, strip_env):
    """Run the child in a throwaway cwd — agents that write files must not
    write them into the repository."""
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["RAR_HARNESS"] = "1"
    if strip_env:
        # Contract: a missing env var must be handled gracefully, not crash.
        for k in list(env):
            if any(t in k.upper() for t in ("KEY", "TOKEN", "SECRET", "PASSWORD", "CONNECTION")):
                env.pop(k, None)
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as fh:
        fh.write(CHILD)
        child = fh.name
    sandbox = tempfile.mkdtemp(prefix="rar-harness-")
    interp = str(BRAINSTEM_PY) if (mode == "brainstem-loader" and BRAINSTEM_PY.exists()) else sys.executable
    try:
        p = subprocess.run([interp, child, str(target), str(BRAINSTEM_SRC), mode],
                           capture_output=True, text=True, timeout=timeout, env=env, cwd=sandbox)
    except subprocess.TimeoutExpired:
        return {"mode": mode, "loaded": False, "timeout": True, "errors": [
            {"stage": "run", "type": "Timeout", "message": f"exceeded {timeout}s"}]}
    finally:
        try:
            os.unlink(child)
        except OSError:
            pass
        shutil.rmtree(sandbox, ignore_errors=True)
    marker = "___HARNESS___"
    if marker in p.stdout:
        try:
            return json.loads(p.stdout.split(marker, 1)[1].strip().split("\n")[0])
        except Exception:
            pass
    return {"mode": mode, "loaded": False, "errors": [
        {"stage": "subprocess", "type": "NoResult",
         "message": (p.stderr or p.stdout or "no output")[-400:]}]}


def _multipart(fields, filename, payload):
    """Minimal multipart/form-data body — stdlib only."""
    boundary = "----RARHarness" + os.urandom(8).hex()
    out = []
    for k, v in (fields or {}).items():
        out.append(f"--{boundary}\r\nContent-Disposition: form-data; name=\"{k}\"\r\n\r\n{v}\r\n".encode())
    out.append((f"--{boundary}\r\nContent-Disposition: form-data; name=\"file\"; "
                f"filename=\"{filename}\"\r\nContent-Type: text/x-python\r\n\r\n").encode())
    out.append(payload)
    out.append(f"\r\n--{boundary}--\r\n".encode())
    return b"".join(out), f"multipart/form-data; boundary={boundary}"


def _api(path, method="GET", data=None, ctype=None, timeout=180):
    req = urllib.request.Request(f"{BRAINSTEM_URL}{path}", data=data, method=method)
    if ctype:
        req.add_header("Content-Type", ctype)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        body = r.read().decode("utf-8", "replace")
    try:
        return json.loads(body)
    except Exception:
        return {"raw": body[:600]}


def chat_probe(target, agent, timeout=180):
    """Hot-load the agent into the RUNNING brainstem and talk to it through /chat.

    This is the end-to-end test the unit-level harness cannot do: the model has to
    decide, on its own, that this agent is the right tool for a plain-language
    request, call it with arguments it invented, and use what came back. The agent
    is removed again afterwards so the user's brainstem is left as we found it.
    """
    target = Path(target)
    res = {"attempted": True, "imported": False, "installed_as": None,
           "tool_invoked": False, "removed": False}
    if not brainstem_alive():
        return {"attempted": False, "reason": "no brainstem running at " + BRAINSTEM_URL}

    payload = target.read_bytes()
    fname = target.name if target.name.endswith("_agent.py") else target.stem + "_agent.py"
    try:
        body, ctype = _multipart({}, fname, payload)
        imp = _api("/agents/import", "POST", body, ctype, timeout=120)
        res["import_response"] = {k: imp.get(k) for k in ("error", "filename", "agents", "loaded", "message") if k in imp}
        res["imported"] = not imp.get("error")
        res["installed_as"] = imp.get("filename") or fname
        res["loaded_classes"] = imp.get("agents") or imp.get("loaded") or []
    except Exception as e:
        res["import_error"] = f"{type(e).__name__}: {str(e)[:200]}"
        return res

    if res["imported"]:
        tool_names = res.get("loaded_classes") or []
        display = agent.get("display_name") or (tool_names[0] if tool_names else agent.get("name", ""))
        desc = (agent.get("description") or "").rstrip(".")
        prompt = (f"Use your {display} tool now. Task: {desc}. "
                  f"Invoke the tool with reasonable arguments, then tell me in one line "
                  f"whether the tool succeeded and what it returned.")
        res["prompt"] = prompt
        try:
            t0 = time.time()
            chat = _api("/chat", "POST", json.dumps({"user_input": prompt}).encode(),
                        "application/json", timeout=timeout)
            res["seconds"] = round(time.time() - t0, 2)
            res["model"] = chat.get("model")
            reply = chat.get("response") or chat.get("error") or ""
            logs = chat.get("agent_logs") or ""
            res["reply"] = reply[:900]
            res["agent_logs"] = logs[:900]
            hay = (logs + " " + reply).lower()
            res["tool_invoked"] = any(str(n).lower() in hay for n in tool_names if n) or bool(logs.strip())
            res["reply_chars"] = len(reply)
        except Exception as e:
            res["chat_error"] = f"{type(e).__name__}: {str(e)[:200]}"

    try:
        _api(f"/agents/{res['installed_as']}", "DELETE", timeout=30)
        res["removed"] = True
    except Exception as e:
        res["remove_error"] = f"{type(e).__name__}: {str(e)[:160]}"
    return res


def brainstem_alive():
    try:
        req = urllib.request.Request(f"{BRAINSTEM_URL}/health")
        with urllib.request.urlopen(req, timeout=3) as r:
            return r.status == 200
    except Exception:
        return False


def standalone_exit_code(target, timeout=30):
    """The registry's own contract: `python agent.py` must exit 0."""
    sandbox = tempfile.mkdtemp(prefix="rar-standalone-")
    try:
        p = subprocess.run([sys.executable, str(target)], capture_output=True,
                           text=True, timeout=timeout, cwd=sandbox)
        return {"ran": True, "exit_code": p.returncode,
                "stdout_chars": len(p.stdout), "stderr_tail": p.stderr[-300:] if p.returncode else ""}
    except subprocess.TimeoutExpired:
        return {"ran": False, "exit_code": None, "timeout": True}
    except Exception as e:
        return {"ran": False, "exit_code": None, "error": type(e).__name__}
    finally:
        shutil.rmtree(sandbox, ignore_errors=True)


def _repo_snapshot():
    """Files under the tracked working tree, so we can spot an agent that writes
    into the registry while being probed."""
    out = set()
    for sub in ("agents", "staging", "state"):
        d = ROOT / sub
        if d.exists():
            out |= {str(p.relative_to(ROOT)) for p in d.rglob("*") if p.is_file()}
    return out


def harness(target, timeout=DEFAULT_TIMEOUT, agent=None, chat=True):
    """Run an agent and return structured evidence. Never raises."""
    target = Path(target)
    if not target.is_absolute():
        target = (ROOT / target).resolve()
    ev = {"file": str(target), "at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
          "brainstem_running": brainstem_alive(), "tier": None}
    before = _repo_snapshot()

    if BRAINSTEM_SRC.exists():
        res = _run_child(target, "brainstem-loader", timeout, strip_env=False)
        ev["tier"] = "brainstem-loader"
    else:
        res = {"loaded": False, "errors": [{"stage": "load", "type": "NoBrainstem",
                                            "message": "no local brainstem source found"}]}
    if not res.get("loaded"):
        alt = _run_child(target, "standalone", timeout, strip_env=False)
        if alt.get("loaded"):
            res, ev["tier"] = alt, "standalone"
        else:
            res.setdefault("fallback_error", alt.get("errors"))
    ev.update(res)

    ev["standalone_run"] = standalone_exit_code(target)

    # Second pass with credentials stripped — does it degrade or does it crash?
    stripped = _run_child(target, ev["tier"] or "standalone", timeout, strip_env=True)
    calls = [c for c in stripped.get("calls", []) if not c.get("probe")]
    ev["no_credentials"] = {
        "loaded": stripped.get("loaded", False),
        "ok": all(c.get("ok") for c in calls) if calls else None,
        "exception": next((c.get("exception") for c in calls if not c.get("ok")), None),
        "preview": (calls[0].get("output_preview") or "")[:280] if calls else "",
    }
    if chat:
        try:
            ev["chat_probe"] = chat_probe(target, agent or {}, timeout=max(timeout, 120))
        except Exception as e:
            ev["chat_probe"] = {"attempted": True, "error": f"{type(e).__name__}: {str(e)[:200]}"}

    created = sorted(_repo_snapshot() - before)
    ev["side_effects"] = {"files_written": created}
    for rel in created:
        # Leave the repository exactly as we found it.
        try:
            (ROOT / rel).unlink()
        except OSError:
            pass
    return ev


def summarize(ev):
    """One dense paragraph of evidence for the critic prompt."""
    lines = []
    tier = ev.get("tier") or "none"
    if ev.get("loaded"):
        lines.append(f"LOADED: yes, via {tier} in {ev.get('load_seconds')}s. "
                     f"Classes registered: {', '.join(ev.get('classes') or []) or 'none'}.")
    else:
        err = (ev.get("errors") or [{}])[0]
        lines.append(f"LOADED: NO. The {tier} loader raised {err.get('type')}: {err.get('message')}")

    for c in ev.get("calls", []):
        tag = "no-args probe" if c.get("probe") else f"perform({', '.join(f'{k}=…' for k in c.get('args', {})) or 'no args'})"
        if c.get("ok"):
            extra = ""
            if not c.get("probe"):
                extra = (f" Returned {c.get('return_type')} of {c.get('output_chars')} chars in {c.get('seconds')}s."
                         f"{' OUTPUT WAS EMPTY.' if c.get('empty') else ''}")
                if c.get("output_preview"):
                    extra += f" First output: {c['output_preview'][:320]!r}"
                if not c.get("returns_str"):
                    extra += " CONTRACT VIOLATION: perform() did not return a str."
                if c.get("printed_chars"):
                    extra += f" It also printed {c['printed_chars']} chars to stdout."
            lines.append(f"RAN {tag}: ok.{extra}")
        else:
            lines.append(f"RAN {tag}: FAILED with {c.get('exception')}: {c.get('message')}")

    sens = ev.get("input_sensitivity") or {}
    if sens.get("tested"):
        if sens.get("ignores_input"):
            lines.append(
                "INPUT SENSITIVITY: FAILED. Called again with every string argument replaced by "
                "'Northwind Traders' and then 'Zzyzx Holdings LLC', it returned byte-identical output "
                "each time. It ignores what it is asked and emits the same canned result — and it does "
                "NOT say so. A caller asking about one company is silently handed another company's "
                f"numbers. Sample of what it returned: {sens.get('sample', '')[:260]!r}")
        elif not sens.get("sentinel_echoed"):
            lines.append("INPUT SENSITIVITY: asked about two entities that certainly do not exist in any "
                         "fixture, it never echoed either name back. It silently substituted something "
                         "else and did not say it had done so — the caller has no way to know the answer "
                         f"is not about what they asked. What came back: {sens.get('sample', '')[:260]!r}")
        else:
            lines.append("INPUT SENSITIVITY: passed — different arguments produced different output "
                         "and the requested entity is reflected back in the response.")
        for e in sens.get("errors", []):
            lines.append(f"INPUT SENSITIVITY: one variant raised {e.get('exception')}: {e.get('message')}")

    sa = ev.get("standalone_run") or {}
    if sa.get("ran"):
        lines.append(f"`python {Path(ev['file']).name}` exited {sa.get('exit_code')}"
                     + (f" (stderr: {sa.get('stderr_tail')[:200]})" if sa.get("exit_code") else " as the contract requires."))
    se = (ev.get("side_effects") or {}).get("files_written") or []
    if se:
        lines.append(f"SIDE EFFECTS: while merely being probed it wrote {len(se)} file(s) into the "
                     f"repository working tree ({', '.join(se[:3])}). The harness deleted them.")
    cp = ev.get("chat_probe") or {}
    if cp.get("attempted"):
        if cp.get("imported"):
            if cp.get("tool_invoked"):
                lines.append(f"HOT-LOADED INTO THE RUNNING BRAINSTEM and exercised through /chat "
                             f"({cp.get('model')}, {cp.get('seconds')}s): the model chose this tool on its own. "
                             f"Agent log: {(cp.get('agent_logs') or '')[:220]!r}. "
                             f"It answered: {(cp.get('reply') or '')[:320]!r}")
            elif cp.get("chat_error"):
                lines.append(f"HOT-LOADED but /chat failed: {cp['chat_error']}")
            else:
                lines.append(f"HOT-LOADED INTO THE RUNNING BRAINSTEM, but when asked in plain language "
                             f"to use it the model did NOT invoke the tool. It replied: "
                             f"{(cp.get('reply') or '')[:280]!r} — a sign the tool name, description or "
                             f"parameter schema does not make its purpose obvious to a model.")
        else:
            lines.append(f"HOT-LOAD INTO THE RUNNING BRAINSTEM FAILED: "
                         f"{cp.get('import_error') or (cp.get('import_response') or {}).get('error')}")
    elif cp.get("reason"):
        lines.append(f"(no live brainstem available for an end-to-end /chat test: {cp['reason']})")

    nc = ev.get("no_credentials") or {}
    if nc.get("ok") is True:
        lines.append(f"WITH ALL CREDENTIALS STRIPPED: still ran and returned output — {nc.get('preview', '')[:200]!r}")
    elif nc.get("ok") is False:
        lines.append(f"WITH ALL CREDENTIALS STRIPPED: crashed with {nc.get('exception')} "
                     f"— the house rule is that missing env vars degrade gracefully.")
    return "\n".join(lines)


def registry_lookup(target):
    """Find this file's manifest so the /chat probe can ask for it by name."""
    try:
        reg = json.loads((ROOT / "registry.json").read_text())
    except Exception:
        return {}
    t = str(Path(target).resolve())
    for a in reg.get("agents", []):
        if str((ROOT / a.get("_file", "")).resolve()) == t:
            return a
    return {}


def main():
    ap = argparse.ArgumentParser(description="Run a registry agent and report what actually happened.")
    ap.add_argument("file")
    ap.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--no-chat", action="store_true", help="skip the live /chat probe")
    a = ap.parse_args()
    ev = harness(a.file, a.timeout, agent=registry_lookup(a.file), chat=not a.no_chat)
    print(json.dumps(ev, indent=1) if a.json else summarize(ev))
    return 0


if __name__ == "__main__":
    sys.exit(main())
