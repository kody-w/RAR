#!/usr/bin/env python3
"""A stand-in for `copilot -p ... --output-format json` so the engine can be tested without spending a model call.
Behaviour per agent label (env RAPP_WORKFLOW_AGENT) comes from FAKE_PLAN: {label: [step, ...]}, one step per
invocation of that label; a step is {"reply": str, "sleep": s, "exit": n}. Like the real CLI it holds a file open
in its session folder (so lsof can name the session) and ends with a `result` event carrying its sessionId."""
import json
import os
import sys
import time
import uuid

args = sys.argv[1:]
label = os.environ.get("RAPP_WORKFLOW_AGENT", "")
resume = args[args.index("--resume") + 1] if "--resume" in args else None
prompt = args[args.index("-p") + 1] if "-p" in args else ""
state_dir = os.environ["FAKE_STATE"]
os.makedirs(state_dir, exist_ok=True)
counter = os.path.join(state_dir, "count-" + (label.replace("/", "_").replace(":", "_") or "none"))
n = int(open(counter).read()) if os.path.exists(counter) else 0
open(counter, "w").write(str(n + 1))
plan = json.load(open(os.environ["FAKE_PLAN"])) if os.environ.get("FAKE_PLAN") else {}
steps = plan.get(label) or plan.get("*") or [{"reply": '{"ok": true}'}]
step = steps[min(n, len(steps) - 1)]
sid = resume or str(uuid.uuid4())
with open(os.environ["FAKE_LOG"], "a") as f:
    f.write(json.dumps({"label": label, "n": n, "resume": resume, "pid": os.getpid(), "cwd": os.getcwd(),
                        "prompt_head": prompt[:200], "continue": prompt.startswith("You were interrupted"),
                        "has_schema": "matches this JSON Schema" in prompt, "argv": args[2:]}) + "\n")
sess = os.path.join(os.environ["FAKE_HOME"], ".copilot", "session-state", sid)
os.makedirs(sess, exist_ok=True)
lock = open(os.path.join(sess, "inuse.%d.lock" % os.getpid()), "w")
time.sleep(float(step.get("sleep", 0)))
print(json.dumps({"type": "assistant.message", "data": {"content": step.get("reply", "")}}), flush=True)
print(json.dumps({"type": "result", "sessionId": sid, "exitCode": int(step.get("exit", 0))}), flush=True)
sys.exit(int(step.get("exit", 0)))
