"""Exit when governed runs need the governor: a run settles, pauses or is interrupted, a unit is proven, finally
held or declined, a subagent errors, or the native Copilot run settles. Events that arrive within BATCH_S of the
first are reported together (one wake, not many). For every PROVEN unit it runs the governor's A/B (gov_ab.py)
on the exact commit the prover proved, and logs it to gov-ledger.jsonl. Remembers what it reported (watch.seen).
State (seen events, the governor ledger) lives in ~/.rapp/workflows/governor/.
Usage: python3 scripts/dynamic_workflow/governor/watch.py [max_seconds]    (RAPP_WORKFLOWS_AGENT=<agent.py> overrides)"""
import calendar
import json
import os
import re
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
AGENT = os.environ.get("RAPP_WORKFLOWS_AGENT") or os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(HERE))), "agents", "@kody-w", "dynamic_workflow_agent.py")
STATE = os.path.join(os.environ.get("RAPP_WORKFLOWS_HOME") or os.path.expanduser("~/.rapp/workflows"), "governor")
os.makedirs(STATE, exist_ok=True)
RUNS = os.path.join(os.environ.get("RAPP_WORKFLOWS_HOME") or os.path.expanduser("~/.rapp/workflows"), "runs")
SEEN = os.path.join(STATE, "watch.seen")
LEDGER = os.path.join(STATE, "gov-ledger.jsonl")
NATIVE = os.environ.get("RAPP_WORKFLOWS_NATIVE_LOG") or os.path.join(STATE, "native-monitor.log")
ACT = re.compile(r"-> PROVEN|-> held \((?!0\))|-> declined|-> error|ERROR at|Ledger:|Paused for the governor|No hook|halting|interrupted by")  # held (0) is revised inside the workflow
PROVEN = re.compile(r"^prove:(.+?) -> PROVEN")
MAX = float(sys.argv[1]) if len(sys.argv) > 1 else 1500
BATCH_S = 240

seen = set()
if os.path.exists(SEEN):
    seen = set(open(SEEN).read().split("\n"))


def status(run_id):
    out = subprocess.run(["/usr/bin/python3", AGENT, "status", "--run-id", run_id, "--lines", "1"], capture_output=True, text=True, timeout=60).stdout
    try:
        return json.loads(out).get("status")
    except ValueError:
        return None


def started_at(run_id):
    """When the run's first attempt started (epoch s). A line logged within REPLAY_S of it is a result replayed from
    another run's journal (replay takes no time; a real agent takes minutes): already reported where it happened."""
    try:
        st = json.load(open(os.path.join(RUNS, run_id, "state.json")))
        return calendar.timegm(time.strptime(st["started_at"][:19], "%Y-%m-%dT%H:%M:%S"))
    except (OSError, ValueError, KeyError):
        return None


def line_time(e):
    try:
        return calendar.timegm(time.strptime(e["t"][:19], "%Y-%m-%dT%H:%M:%S"))
    except (KeyError, ValueError):
        return None


REPLAY_S = 5


def events():
    found = []
    for run_id in sorted(os.listdir(RUNS)):
        st = status(run_id)
        t0 = started_at(run_id)
        if st in ("completed", "error", "paused", "interrupted", "cancelled", "halted"):
            found.append(("status %s %s" % (run_id, st), run_id, "%s is %s" % (run_id, st)))
        try:
            with open(os.path.join(RUNS, run_id, "progress.jsonl")) as f:
                for n, line in enumerate(f):
                    try:
                        e = json.loads(line)
                    except ValueError:
                        continue
                    if ACT.search(e.get("text", "")):
                        lt = line_time(e)
                        replayed = t0 is not None and lt is not None and 0 <= lt - t0 < REPLAY_S and "-> " in e["text"]
                        found.append(("%s#%d" % (run_id, n), run_id, e["text"] if not replayed else None))
        except OSError:
            pass
    if os.path.exists(NATIVE):
        for n, line in enumerate(open(NATIVE)):
            if "settled" in line:
                found.append(("native#%d" % n, "native", "NATIVE " + line.strip()))
    return found


def proven_commit(run_id, slug):
    commit = None
    try:
        with open(os.path.join(RUNS, run_id, "journal.jsonl")) as f:
            for line in f:
                e = json.loads(line)
                lab = e.get("label", "")
                if (lab == "build:" + slug or lab.startswith("revise:" + slug + ":")) and isinstance(e.get("value"), dict) and e["value"].get("commit"):
                    commit = e["value"]["commit"]
    except (OSError, ValueError):
        pass
    return commit


def gov_ab(run_id, slug):
    spec = json.load(open(os.path.join(RUNS, run_id, "run.json")))
    args = spec.get("args") or {}
    commit = proven_commit(run_id, slug)
    if not commit or not args.get("repo") or not args.get("base"):
        return "GOVERNOR A/B SKIPPED for %s: no commit or repo/base in the run" % slug
    if os.path.exists(LEDGER):  # the same commit against the same base was already checked: the answer stands
        for line in open(LEDGER):
            try:
                g = json.loads(line).get("governor") or ""
            except ValueError:
                continue
            if g.startswith("GOVERNOR A/B HOLDS") and (" %s " % commit[:7]) in (" " + g.replace("  ", " ")) and ("base %s:" % args["base"]) in g:
                return g + "  (already checked)"
    r = subprocess.run(["/usr/bin/python3", os.path.join(HERE, "gov_ab.py"), args["repo"], args["base"], commit, os.path.join(STATE, "ab")],
                       capture_output=True, text=True, timeout=7200)
    return "GOVERNOR " + ((r.stdout or r.stderr).strip().splitlines() or ["?"])[-1] + "  [unit %s]" % slug


def log(entry):
    with open(LEDGER, "a") as f:
        f.write(json.dumps(dict(entry, t=time.strftime("%Y-%m-%dT%H:%M:%S"))) + "\n")


start = time.time()
first = None
out = []
while True:
    new = [ev for ev in events() if ev[0] not in seen]
    for key, run_id, text in new:
        seen.add(key)
        with open(SEEN, "a") as f:
            f.write(key + "\n")
        if text is None:  # replayed from another run's journal: reported where it happened
            continue
        out.append("%s  %s" % (run_id[-9:], text[:230]))
        log({"run": run_id, "event": text[:600]})
        m = PROVEN.match(text)
        if m and run_id != "native":
            verdict = gov_ab(run_id, m.group(1))
            out.append("    " + verdict)
            log({"run": run_id, "unit": m.group(1), "governor": verdict})
    if out and first is None:
        first = time.time()
    if out and time.time() - first >= BATCH_S:
        print("\n".join(out))
        break
    if not out and time.time() - start > MAX:
        print("no event in %d s (heartbeat)" % MAX)
        break
    time.sleep(20)
