#!/usr/bin/python3
"""Blackbox: a flight recorder for this Mac, plus a guard.

  run       watch forever (launchd keeps this alive): a full sample every minute, a cheap check every 5 s, and
            full samples every 5 s while memory is under pressure. Every line is flushed to disk at once.
  tick      the same, for one minute
  sample    take one full sample now and print it
  report    write the plain "why it restarted" page for a panic file (found automatically on the next start)
  top       the five biggest jobs by memory, in plain words
  why       one sentence: why this Mac last restarted itself
  note      what the guard did in the last day, in plain words (also written once each morning)
  install   keep the recorder running on this Mac from now on (uninstall switches it off)
  status    what the guard has paused
  resume    let a paused job carry on        (resume <id> | resume all)
  stop      end a paused job for good        (stop <id>)

Memory is the real footprint (what Activity Monitor shows, compressed memory included), added up per JOB: a job is
a program and everything it started. Standard library only; reads the system, changes nothing unless the guard is
set to "pause" and the Mac is about to run out of memory.
"""
import glob, html, json, os, re, signal, subprocess, sys, time

HOME = os.path.expanduser("~")
D = os.environ.get("BLACKBOX_DIR", HOME + "/.blackbox/logs")
CFG_PATH = os.environ.get("BLACKBOX_CONFIG", HOME + "/.blackbox/blackbox.json")
STATE, GUARD = D + "/state.json", D + "/guard.json"
HERE = os.path.abspath(__file__)
KEEP_DAYS = 7

DEFAULTS = {
    "guard": "pause",            # pause | watch (only say what it would do) | off
    "swap_grow_gb_min": 5.0,     # critical: swap growing this fast ...
    "swap_high_gb": 60.0,        # ... or this much swap in use ...
    "free_low_pct": 12,          # ... or this little memory free
    "job_grow_gb_min": 2.0,      # a job must be growing at least this fast to be paused
    "job_min_gb": 4.0,           # and be at least this big
    "hot_free_pct": 30,          # sample every 5 s below this much free memory ...
    "hot_swap_grow_gb_min": 0.5, # ... or when swap grows faster than this
    "carry_on_min": 30,          # after "let it carry on", leave that job alone this long
    "ask": "note",               # note = decide, act, and say it in one morning note | popup = ask on screen each time
    "precious": [],              # never frozen, never closed: parts of a name or command
    "disposable": [],            # safe to close without asking when memory runs short: parts of a name or command
    "thaw_min": 20,              # a frozen job is let go again after this long, once memory has recovered ...
    "thaw_free_pct": 25,         # ... to at least this much free
    "note_hour": 7,              # the morning note is written at the first look after this hour
    "ask_script": "",            # your own way to ask a question: a program taking title, message, then the choices; prints the pick
    "names": {},                 # your own plain names: {"part of the command": "What you call it"}
    "only_label": "",            # tests: the guard may only touch jobs whose name contains this
}
# Never paused: the things you need in order to see the warning and answer it.
PROTECTED = ("WindowServer", "loginwindow", "Finder", "Dock", "SystemUIServer", "ControlCenter", "NotificationCenter",
             "Terminal", "iTerm", "tmux", "sshd", "launchd", "osascript", "blackbox")
SHELLS = {"zsh", "bash", "sh", "fish", "dash", "login", "tmux", "screen", "sudo", "env", "nohup", "caffeinate"}


def cfg():
    c = dict(DEFAULTS)
    try:
        c.update(json.load(open(CFG_PATH)))
    except Exception:
        pass
    for k in list(c):
        v = os.environ.get("BLACKBOX_" + k.upper())
        if v is not None:
            c[k] = v if isinstance(DEFAULTS[k], str) else [x for x in v.split(",") if x] if isinstance(DEFAULTS[k], list) else json.loads(v) if isinstance(DEFAULTS[k], dict) else type(DEFAULTS[k])(v)
    return c


def run(cmd, timeout=20):
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout).stdout
    except Exception:
        return ""


def load(path, default):
    try:
        return json.load(open(path))
    except Exception:
        return default


def save(path, obj):
    tmp = path + ".tmp%d" % os.getpid()
    with open(tmp, "w") as f:
        json.dump(obj, f)
        f.flush(); os.fsync(f.fileno())
    os.replace(tmp, path)


def write(day_ext, text):
    """Append and force to disk, so the last seconds before a freeze survive."""
    os.makedirs(D, exist_ok=True)
    with open("%s/%s.%s" % (D, time.strftime("%F"), day_ext), "a") as f:
        f.write(text)
        f.flush(); os.fsync(f.fileno())


def probe():
    """The cheap check: percent of memory free and swap in use (MB). One sysctl call."""
    if os.environ.get("BLACKBOX_TEST_SWAP_MB"):
        return 50, float(os.environ["BLACKBOX_TEST_SWAP_MB"])
    out = run(["sysctl", "-n", "kern.memorystatus_level", "vm.swapusage"], 5)
    free = int((re.search(r"^\s*(\d+)\s*$", out, re.M) or [0, 0])[1])
    m = re.search(r"used = ([\d.]+)([MGK])", out)
    swap = float(m[1]) * {"K": 1 / 1024, "M": 1, "G": 1024}[m[2]] if m else 0.0
    return free, swap


def size_mb(s):
    m = re.match(r"([\d.]+)([BKMG])", s)
    return float(m[1]) * {"B": 1 / 1048576, "K": 1 / 1024, "M": 1, "G": 1024}[m[2]] if m else 0.0


def label_of(args):
    a = args.replace(HOME, "~")
    m = re.match(r"[/~][^*]*?/([^/]+)\.app/", a)
    if m and "/Python.app/" not in a and not re.match(r"[/~][^*]*?\.app/Contents/Developer/", a):   # git inside Xcode is git
        return m[1]
    parts = a.split()
    out = [os.path.basename(parts[0])] if parts else ["?"]
    for p in parts[1:6]:
        out.append(p if len(p) < 50 else "…" + p[-45:])
    return " ".join(out)[:110]


# ---------------------------------------------------------------- plain names
RUNNERS = {"python", "python3", "uv", "uvx", "node", "npm", "npx", "pnpm", "yarn", "bun", "deno", "ruby", "java", "uvicorn", "gunicorn",
           "flask", "cargo", "go", "sh", "bash", "zsh", "make", "tsx", "next", "vite"}
GENERIC = {"backend", "frontend", "src", "app", "server", "api", "bin", "build", "dist", "web", "scripts", "python", "typescript", "tests"}
TIDY = ("repack", "pack-objects", "gc", "maintenance", "prune-packed", "multi-pack-index", "commit-graph")
PLAIN = (("launchd_sim", "iPhone Simulator"), ("claude", "Claude Code"), ("codex", "Codex"), ("copilot", "Copilot"), ("ollama", "Ollama"),
         ("com.docker", "Docker"), ("qemu", "a virtual machine"), ("kernel_task", "macOS itself"), ("mds_stores", "Spotlight search"))


def cwd_of(pid):
    m = re.search(r"^n(/.*)$", run(["lsof", "-a", "-p", str(pid), "-d", "cwd", "-Fn"], 10), re.M)
    return m[1] if m else ""


def project_of(path):
    """The name a person would call the folder a job runs in: its project, not 'backend' or 'src'."""
    p = path.rstrip("/")
    for _ in range(6):                                  # a project root wins
        if not p or p in ("/", HOME) or os.path.dirname(p) == "/":
            break
        if os.path.exists(p + "/.git"):
            while os.path.basename(p).lower() in GENERIC and os.path.dirname(p) not in ("/", HOME):
                p = os.path.dirname(p)                # a project kept in a folder called "src" is named by the folder above
            return os.path.basename(p).lstrip(".")
        p = os.path.dirname(p)
    p = path.rstrip("/")
    while p and p not in ("/", HOME) and os.path.basename(p).lower() in GENERIC:
        p = os.path.dirname(p)
    return "" if p in ("", "/", HOME) or os.path.dirname(p) == "/" else os.path.basename(p)


def tidy(label):
    """git's own housekeeping. It can be closed at any moment: git keeps the old files until the new ones are whole."""
    w = label.split()
    return bool(w) and w[0] == "git" and any(x in TIDY for x in w[1:5])


def name_of(label, pid=0, names=None):
    """What a person would call this job. The command stays in the record; this is what is said out loud."""
    for k, v in (names or {}).items():
        if k.lower() in label.lower():
            return v
    w = label.split()
    first = w[0].lstrip("-") if w else ""
    where = project_of(cwd_of(pid)) if pid and (first == "git" or first in RUNNERS or re.match(r"[Pp]ython[\d.]*$", first)) else ""
    if first == "git":
        verb = next((x for x in w[1:] if not x.startswith("-")), "")
        return ("git tidy-up" if tidy(label) else ("git " + verb).strip()) + (" in " + where if where else "")
    if where:
        return where
    for k, v in PLAIN:
        if k in label:
            return v
    return label


def is_host(args):
    """A shell or an AI command line: what it starts counts as its own job, not as part of it."""
    first = os.path.basename(args.split()[0]) if args.split() else ""
    return first.lstrip("-") in SHELLS or bool(re.search(r"(^|/)(claude|codex|copilot)(\s|$)|/\.claude/|claude/versions/", args[:200]))


def processes():
    procs = {}
    for line in run(["ps", "-Ao", "pid=,ppid=,uid=,rss=,pcpu=,args="]).splitlines():
        p = line.split(None, 5)
        if len(p) < 6:
            continue
        procs[int(p[0])] = {"ppid": int(p[1]), "uid": int(p[2]), "mb": int(p[3]) / 1024, "cpu": float(p[4]), "args": p[5]}
    for line in run(["top", "-l", "1", "-stats", "pid,mem"], 30).splitlines():   # real footprint, compressed included
        p = line.split()
        if len(p) == 2 and p[0].isdigit() and int(p[0]) in procs:
            procs[int(p[0])]["mb"] = size_mb(p[1])
    return procs


def jobs_of(procs):
    jobs = {}
    for pid, p in procs.items():
        root, seen = pid, set()
        while True:
            par = procs[root]["ppid"]
            if par <= 1 or par not in procs or par in seen or is_host(procs[par]["args"]):
                break
            seen.add(root); root = par
        j = jobs.setdefault(root, {"pid": root, "mb": 0.0, "pids": [], "uid": procs[root]["uid"], "label": label_of(procs[root]["args"])})
        j["mb"] += p["mb"]; j["pids"].append(pid)
    return jobs


def sample(c, state):
    now = time.time()
    free, swap = probe()
    procs = processes()
    jobs = jobs_of(procs)
    prev, pt = state.get("jobs", {}), state.get("t", 0)
    dt = now - pt if pt and now - pt < 300 else 0
    for j in jobs.values():
        was = prev.get(str(j["pid"]), 0.0 if dt else j["mb"])
        j["rate"] = (j["mb"] - was) / 1024 / dt * 60 if dt else 0.0          # GB per minute
    hist = [h for h in state.get("hist", []) if now - h["t"] < 720]
    for j in jobs.values():                                                  # how much it grew over about ten minutes, in GB
        j["grew"] = (j["mb"] - hist[0]["jobs"].get(str(j["pid"]), j["mb"])) / 1024 if hist else 0.0
    if not hist or now - hist[-1]["t"] >= 120:
        hist.append({"t": now, "jobs": {str(j["pid"]): round(j["mb"]) for j in jobs.values() if j["mb"] >= 200}})
    state["hist"] = hist
    swap_rate = (swap - state.get("swap", swap)) / 1024 / dt * 60 if dt else 0.0
    hot = free <= c["hot_free_pct"] or swap_rate >= c["hot_swap_grow_gb_min"]
    big = sorted(jobs.values(), key=lambda j: -j["mb"])[:5]
    fast = [j for j in sorted(jobs.values(), key=lambda j: -j["rate"])[:3] if j["rate"] >= 0.2 and j not in big]
    cpu = sorted(procs.items(), key=lambda kv: -kv[1]["cpu"])[:3]
    rec = {"t": round(now, 1), "ts": time.strftime("%T"), "load": os.getloadavg()[0], "procs": len(procs), "free": free,
           "swap_mb": round(swap), "swap_rate": round(swap_rate, 2), "hot": hot,
           "jobs": [{"pid": j["pid"], "label": j["label"], "gb": round(j["mb"] / 1024, 2), "rate": round(j["rate"], 2), "n": len(j["pids"])} for j in big + fast]}
    text = "%s load=%.2f procs=%d mem_free=%d%% swap=%.2fM%s\n" % (rec["ts"], rec["load"], rec["procs"], free, swap, " HOT swap %+.1fGB/min" % swap_rate if hot else "")
    for pid, p in cpu:
        text += "   %.1f%% %dMB %s\n" % (p["cpu"], p["mb"], label_of(p["args"])[:60])
    for j in rec["jobs"]:
        text += "   job %6.1fGB %+5.1fGB/min n=%-3d pid %-6d %s\n" % (j["gb"], j["rate"], j["n"], j["pid"], j["label"])
    write("log", text); write("jsonl", json.dumps(rec) + "\n")
    state.update({"t": now, "swap": swap, "jobs": {str(j["pid"]): j["mb"] for j in jobs.values()}})
    guard(c, rec, jobs, swap, swap_rate, free, procs)
    return rec, text


# ---------------------------------------------------------------- the guard

def notify(title, msg):
    if os.environ.get("BLACKBOX_NO_ASK"):        # tests stay silent
        return
    subprocess.Popen(["osascript", "-e", "display notification %s with title %s sound name \"Submarine\"" % (json.dumps(msg), json.dumps(title))],
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def said(e):
    """The plain name of a paused job (older entries only have the command)."""
    return e.get("name") or name_of(e["label"])


def seen_now(pids):
    """pid -> (state, start time), for the ones still alive. One ps call."""
    out = {}
    if pids:
        for line in run(["ps", "-o", "pid=,stat=,lstart=", "-p", ",".join(str(p) for p in pids)], 10).splitlines():
            p = line.split(None, 2)
            if len(p) == 3:
                out[int(p[0])] = (p[1], p[2].strip())
    return out


def still_held(e):
    """The processes of a paused job that are still the same ones and still frozen. A number that now belongs to
    some other program (the old one ended, the number was handed out again) is never touched."""
    seen, born = seen_now(e["pids"]), e.get("born")
    return [p for p in e["pids"] if p in seen and seen[p][0].startswith("T") and (not born or born.get(str(p)) == seen[p][1])]


def prune(g):
    before = json.dumps(g["paused"])
    for e in g["paused"]:
        e["pids"] = still_held(e)
    g["paused"] = [e for e in g["paused"] if e["pids"]]
    return json.dumps(g["paused"]) != before


def folder_gone(pid):
    """The folder a process works in, if that folder has been deleted. Unreadable or unplugged is not deleted."""
    at = cwd_of(pid)
    if not at or at.startswith("/Volumes/"):
        return ""
    try:
        os.stat(at)
    except FileNotFoundError:
        return at
    except OSError:
        pass
    return ""


def lost(root, procs):
    """A leftover: nothing is waiting for it and the folder it was working in is gone. Its work can go nowhere."""
    p = procs.get(root)
    return folder_gone(root) if p and p["ppid"] <= 1 and p["uid"] == os.getuid() else ""


def end(pids):
    n = 0
    for pid in pids:
        try:
            os.kill(pid, signal.SIGKILL); n += 1
        except OSError:
            pass
    return n


def pick(cand):
    """Blame the job that grew most over the last ten minutes, not the one that happened to jump this second."""
    return max(cand, key=lambda j: (round(j.get("grew", 0.0), 1), j["rate"]))


def thaw(c, free, swap_rate):
    """A frozen job is let go again once memory has recovered. Nobody has to answer anything."""
    if free < c["thaw_free_pct"] or swap_rate >= c["hot_swap_grow_gb_min"]:
        return
    now = time.time()
    for e in load(GUARD, {"paused": []})["paused"]:
        try:
            age = now - time.mktime(time.strptime(e["at"], "%Y-%m-%d %H:%M:%S"))
        except ValueError:
            continue
        if age >= c["thaw_min"] * 60 and not e.get("keep") and (not c["only_label"] or c["only_label"] in e["label"]):
            release(e["id"], signal.SIGCONT, grace=False, why="memory recovered to %d%% free" % free)
            return                                    # one at a time; the next look sees what that did


def guard(c, rec, jobs, swap, swap_rate, free, procs):
    if c["guard"] == "off":
        return
    why = ("swap growing %.0f GB a minute" % swap_rate if swap_rate >= c["swap_grow_gb_min"] else
           "%.0f GB of swap in use" % (swap / 1024) if swap / 1024 >= c["swap_high_gb"] else
           "only %d%% of memory free" % free if free <= c["free_low_pct"] else
           "a test" if os.environ.get("BLACKBOX_TEST_FORCE") else "")
    if not why or os.environ.get("BLACKBOX_TEST_THAW"):
        thaw(c, free, swap_rate)
    if not why:
        return
    g = load(GUARD, {"paused": [], "warned": 0})
    changed = prune(g)
    # Frozen jobs keep their memory. A frozen leftover (nobody waiting, folder deleted) is closed so the memory returns.
    closed, freed = 0, 0.0
    for e in list(g["paused"]):
        where = lost(e.get("pid", e["pids"][0]), procs) if c["guard"] == "pause" else ""
        if where:
            freed += sum(procs[p]["mb"] for p in e["pids"] if p in procs) / 1024
            end(e["pids"]); g["paused"].remove(e); closed += 1
            write("log", "   GUARD closed leftover %s (%s); its folder %s was deleted\n" % (e["id"], said(e)[:60], where))
    if closed or changed:
        save(GUARD, g)
    if closed and c["ask"] != "popup":
        return
    if closed:
        notify("Blackbox gave memory back", "Closed %d leftover job%s holding %.0f GB. Their folder was already deleted, so nothing was lost." % (closed, "" if closed == 1 else "s", freed))
        return
    held = {p for e in g["paused"] for p in e["pids"]}
    me = os.getuid()
    now = time.time()
    g["let"] = {k: t for k, t in g.get("let", {}).items() if now - t < c["carry_on_min"] * 60}
    if why.endswith("of swap in use") and swap_rate < c["hot_swap_grow_gb_min"] and not os.environ.get("BLACKBOX_TEST_FORCE"):
        # Overflow is high but not rising: freezing one more job gives nothing back. Say what the frozen ones hold.
        if now - g.get("warned", 0) > (600 if c["ask"] == "popup" else 3600):
            g["warned"] = now; save(GUARD, g)
            gb = sum(procs[p]["mb"] for p in held if p in procs) / 1024
            write("log", "   GUARD %s, not rising; nothing new paused; %d frozen jobs hold %.0f GB\n" % (why, len(g["paused"]), gb))
            if c["only_label"]:
                pass
            elif g["paused"] and gb >= c["job_min_gb"] and not os.environ.get("BLACKBOX_NO_ASK"):
                subprocess.Popen([sys.executable, HERE, "ask", "held"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
            else:
                notify("Mac is running low on memory", "Blackbox sees %s, but nothing is growing. Close something big." % why)
        return
    cand = [j for j in jobs.values() if j["uid"] == me and j["rate"] >= c["job_grow_gb_min"] and j["mb"] / 1024 >= c["job_min_gb"]
            and not any(x.lower() in j["label"].lower() for x in list(PROTECTED) + c["precious"]) and j["pid"] not in held and str(j["pid"]) not in g["let"]
            and (not c["only_label"] or c["only_label"] in j["label"])]
    if not cand:
        if time.time() - g.get("warned", 0) > 600 and not c["only_label"]:
            g["warned"] = time.time(); save(GUARD, g)
            write("log", "   GUARD %s; no single growing job to pause\n" % why)
            notify("Mac is running low on memory", "Blackbox sees %s, but no one job is growing. Close something big." % why)
        return
    j = pick(cand)
    name = name_of(j["label"], j["pid"], c["names"])
    if any(x.lower() in name.lower() for x in c["precious"]):
        return
    what = "%s (%.0f GB, growing %.0f GB a minute)" % (name[:60], j["mb"] / 1024, j["rate"])
    if c["guard"] != "pause":
        write("log", "   GUARD would pause %s because %s\n" % (what, why))
        return
    where = lost(j["pid"], procs)
    if where:
        end(j["pids"])
        write("log", "   GUARD closed leftover %s because %s; its folder %s was deleted\n" % (what, why, where))
        if c["ask"] == "popup":
            notify("Blackbox gave memory back", "Closed a leftover job: %s. Its folder was already deleted, so nothing was lost." % what)
        return
    spare = "it is git's own housekeeping, which git simply redoes" if tidy(j["label"]) else next(
        ("you marked it safe to close" for x in c["disposable"] if x.lower() in (j["label"] + " " + name).lower()), "")
    if spare:
        end(j["pids"])
        write("log", "   GUARD closed spare %s because %s; %s; command: %s\n" % (what, why, spare, j["label"]))
        return
    done = []
    for pid in j["pids"]:
        try:
            os.kill(pid, signal.SIGSTOP); done.append(pid)
        except OSError:
            pass
    gid = "g%d" % (int(time.time()) % 100000)
    times = g.setdefault("count", {}); times[str(j["pid"])] = times.get(str(j["pid"]), 0) + 1
    g["count"] = {k: v for k, v in times.items() if int(k) in procs}
    again = times[str(j["pid"])] >= 3                 # frozen, let go, and it grew again, three times: now it is the person's call
    g["paused"].append({"keep": again,"id": gid, "at": time.strftime("%F %T"), "label": j["label"], "name": name, "gb": round(j["mb"] / 1024, 1), "why": why, "pids": done,
                        "pid": j["pid"], "born": {str(p): v[1] for p, v in seen_now(done).items()}})
    save(GUARD, g)
    write("log", "   GUARD paused %s because %s; id %s, %d processes; command: %s\n" % (what, why, gid, len(done), j["label"]))
    notify("Blackbox paused a job to save your Mac", "%s. Nothing is lost; it is frozen, not closed." % what)
    if not os.environ.get("BLACKBOX_NO_ASK") and (c["ask"] == "popup" or again):
        subprocess.Popen([sys.executable, HERE, "ask", gid], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)


def release(gid, sig, grace=True, why=""):
    g = load(GUARD, {"paused": []})
    keep, n = [], 0
    for e in g["paused"]:
        if gid in ("all", e["id"]):
            if sig == signal.SIGCONT and "pid" in e and grace:
                g.setdefault("let", {})[str(e["pid"])] = time.time()        # the person's answer stands for a while
            for pid in still_held(e):
                try:
                    if sig != signal.SIGCONT:
                        os.kill(pid, sig)
                    os.kill(pid, signal.SIGCONT); n += 1
                except OSError:
                    pass
            write("log", "   GUARD %s %s (%s), %d processes%s\n" % ("let go" if why else "resumed" if sig == signal.SIGCONT else "stopped", e["id"], said(e)[:60], n, "; " + why if why else ""))
        else:
            keep.append(e)
    g["paused"] = keep; save(GUARD, g)
    return n


def choose(script, a):
    """One question, a few choices; returns the pick. Your own asker if you set one, else the Mac's own pick list."""
    if script:
        return run([script] + a, 86400)
    q = lambda x: json.dumps(x)
    return run(["osascript", "-e", "choose from list {%s} with title %s with prompt %s default items {%s}" % (
        ", ".join(q(x) for x in a[2:]), q(a[0]), q(a[1]), q(a[2]))], 86400)


def ask_one(script, gid):
    if gid == "held":
        g = load(GUARD, {"paused": []}); prune(g)
        if not g["paused"]:
            return
        ans = choose(script, ["Frozen jobs are holding memory", "%d frozen jobs are holding memory and the Mac is still short. The biggest: %s." % (
                   len(g["paused"]), said(max(g["paused"], key=lambda e: e["gb"]))[:70]), "Leave them frozen", "Stop them all for good", "Let them all carry on"])
        if "Stop them" in ans:
            release("all", signal.SIGTERM)
        elif "carry on" in ans:
            release("all", signal.SIGCONT)
        return
    e = next((e for e in load(GUARD, {"paused": []})["paused"] if e["id"] == gid), None)
    if not e or not still_held(e):
        return
    ans = choose(script, ["Blackbox paused a job", "Your Mac was about to run out of memory (%s). I froze: %s, at %s GB. It is frozen, not closed." % (e["why"], said(e)[:70], e["gb"]),
               "Keep it paused", "Stop it for good", "Let it carry on"])
    if "Stop it" in ans:
        release(gid, signal.SIGTERM)
    elif "carry on" in ans:
        release(gid, signal.SIGCONT)


def ask(gid):
    """One question on screen at a time: each waits its turn, and is skipped if its job is no longer frozen by then."""
    script = os.environ.get("BLACKBOX_ASK") or cfg()["ask_script"]
    if not script or not os.path.exists(script):
        script = ""                                   # the built-in pick list
    import fcntl
    os.makedirs(D, exist_ok=True)
    with open(D + "/ask.lock", "w") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        ask_one(script, gid)


# ---------------------------------------------------------------- the note

def note(hours=24, since=0):
    """What the guard did, counted from its own record and said plainly. One note instead of a question each time."""
    now = time.time()
    start, froze, spare, left, let, back, stopped, when = max(since, now - hours * 3600), {}, {}, 0, 0, 0, 0, None
    for day in sorted({time.strftime("%F", time.localtime(start)), time.strftime("%F", time.localtime(now - 86400)), time.strftime("%F", time.localtime(now))}):
        base, clock = time.mktime(time.strptime(day, "%Y-%m-%d")), 0
        for line in open("%s/%s.log" % (D, day), errors="ignore") if os.path.exists("%s/%s.log" % (D, day)) else []:
            t = re.match(r"(\d\d):(\d\d):(\d\d) ", line)
            if t:
                clock = base + int(t[1]) * 3600 + int(t[2]) * 60 + int(t[3]); continue
            if "GUARD" not in line or clock < start:
                continue
            m = re.search(r"GUARD paused (.+?) \((\d+) GB", line)
            if m:
                n = name_of(m[1]); froze[n] = froze.get(n, 0) + 1; when = when or clock
            m = re.search(r"GUARD closed spare (.+?) \(\d+ GB", line)
            if m:
                n = re.sub(r" in \S+$", "", name_of(m[1])); spare[n] = spare.get(n, 0) + 1; when = when or clock
            left += "GUARD closed leftover" in line
            let += "GUARD let go" in line
            back += "GUARD resumed" in line
            stopped += "GUARD stopped" in line
    held = load(GUARD, {"paused": []})["paused"]
    if not (froze or spare or left or held):
        return "Nothing needed doing. The guard froze nothing and closed nothing."
    s = lambda n: "" if n == 1 else "s"
    part = []
    if froze or spare or left:
        day = "" if time.strftime("%F", time.localtime(when or now)) == time.strftime("%F") else " yesterday"
        part.append("The guard stepped in %d time%s since %s%s to keep the computer from running out of memory." % (
            sum(froze.values()) + sum(spare.values()) + left, s(sum(froze.values()) + sum(spare.values()) + left), time.strftime("%-I:%M %p", time.localtime(when or now)), day))
    if froze:
        part.append("It froze: %s." % ", ".join("%s (%d time%s)" % (n[:50], k, s(k)) for n, k in sorted(froze.items(), key=lambda kv: -kv[1])[:4]))
    if spare:
        part.append("It closed, without needing to ask: %s. Nothing was lost." % ", ".join("%s (%d time%s)" % (n[:50], k, s(k)) for n, k in sorted(spare.items(), key=lambda kv: -kv[1])[:4]))
    if left:
        part.append("It closed %d leftover job%s whose folder was already deleted." % (left, s(left)))
    if let:
        part.append("%d frozen job%s let go again by the guard once memory came back." % (let, " was" if let == 1 else "s were"))
    if back or stopped:
        part.append("You let %d carry on and stopped %d." % (back, stopped))
    part.append("Right now nothing is frozen." if not held else "Still frozen and waiting for your word: %s. Say carry on, or stop." % ", ".join(said(e)[:50] for e in held))
    return " ".join(part)


def morning(c, state):
    """Once a day, after the note hour: write the note, and show it once if anything happened."""
    day = time.strftime("%F")
    if state.get("noted") == day or time.localtime().tm_hour < c["note_hour"]:
        return
    text = note(since=state.get("noted_t", 0))
    state["noted"], state["noted_t"] = day, time.time()
    os.makedirs(D + "/notes", exist_ok=True)
    open("%s/notes/%s.txt" % (D, day), "w").write(text + "\n")
    write("log", "   NOTE %s\n" % text)
    if not text.startswith("Nothing needed doing"):
        notify("Blackbox morning note", text[:240])


# ---------------------------------------------------------------- the "why it restarted" page

def panic_facts(path):
    raw = open(path, errors="replace").read()
    try:
        s = json.loads(raw[raw.index("\n") + 1:]).get("panicString", "")
    except Exception:
        s = raw
    m = re.search(r"Calendar:\s*0x([0-9a-f]+)", s)
    t = int(m[1], 16) if m else os.path.getmtime(path)
    first = s.strip().split("\n")[0][:300]
    comp = (re.search(r"Compressor Info:.*", s) or [""])[0]
    return t, first, comp


def samples_before(t, minutes=12):
    out = []
    for day in sorted({time.strftime("%F", time.localtime(t - 86400)), time.strftime("%F", time.localtime(t))}):
        got = False
        for line in open("%s/%s.jsonl" % (D, day)) if os.path.exists("%s/%s.jsonl" % (D, day)) else []:
            try:
                r = json.loads(line)
            except Exception:
                continue
            if t - minutes * 60 <= r["t"] <= t + 5:
                out.append(r); got = True
        if not got and os.path.exists("%s/%s.log" % (D, day)):      # lines written before per-job tracking existed
            base = time.mktime(time.strptime(day, "%Y-%m-%d"))
            for line in open("%s/%s.log" % (D, day)):
                m = re.match(r"(\d\d):(\d\d):(\d\d) load=([\d.]+) procs=(\d+) mem_free=(\d+)% swap=([\d.]+)M", line)
                if m:
                    rt = base + int(m[1]) * 3600 + int(m[2]) * 60 + int(m[3])
                    if t - minutes * 60 <= rt <= t + 5:
                        out.append({"t": rt, "ts": line[:8], "load": float(m[4]), "procs": int(m[5]), "free": int(m[6]), "swap_mb": float(m[7]), "jobs": []})
    return sorted(out, key=lambda r: r["t"])


def report(path, show=True):
    t, first, comp = panic_facts(path)
    rows = samples_before(t)
    when = time.strftime("%H:%M on %A %B %-d", time.localtime(t))
    memory = "BAD" in comp or (rows and (rows[-1]["swap_mb"] - rows[0]["swap_mb"] > 8000 or rows[-1]["free"] <= 15))
    grown = {}
    for r in rows:
        for j in r.get("jobs", []):
            g = grown.setdefault(j["pid"], {"label": j["label"], "lo": j["gb"], "hi": j["gb"], "t0": r["t"]})
            g["hi"] = j["gb"]; g["lo"] = min(g["lo"], j["gb"])
    top = max(grown.values(), key=lambda g: g["hi"] - g["lo"], default=None)
    if memory and top and top["hi"] - top["lo"] >= 2:
        line = "Your Mac restarted at %s because it ran out of memory. The biggest cause was <b>%s</b>, which grew from %.0f to %.0f GB in the last %d minutes." % (
            when, html.escape(top["label"]), top["lo"], top["hi"], max(1, round((t - top["t0"]) / 60)))
    elif memory:
        line = "Your Mac restarted at %s because it ran out of memory. %s" % (when, "No single job stood out in the last minutes." if grown else "The recorder was not yet tracking memory per job at that time, so the cause is not named.")
    else:
        line = "Your Mac restarted itself at %s. It does not look like a memory problem; the technical reason is under Details." % when
    trs = "".join("<tr><td>%s</td><td>%d%%</td><td>%.0f GB</td><td>%s</td></tr>" % (
        r["ts"], r["free"], r["swap_mb"] / 1024, html.escape(max(r["jobs"], key=lambda j: j["gb"])["label"][:50] + " %.0f GB" % max(r["jobs"], key=lambda j: j["gb"])["gb"]) if r.get("jobs") else "") for r in rows[-14:])
    page = """<!doctype html><meta charset="utf-8"><title>Why your Mac restarted</title>
<style>body{font:18px -apple-system,sans-serif;max-width:760px;margin:8vh auto;padding:0 24px;color:#1d1d1f}
h1{font-size:15px;color:#86868b;font-weight:600;letter-spacing:.04em;text-transform:uppercase}
p.big{font-size:30px;line-height:1.3;margin:.4em 0 1.2em}table{border-collapse:collapse;width:100%%;font-size:15px}
td,th{text-align:left;padding:6px 10px;border-bottom:1px solid #e5e5ea}details{margin-top:28px;color:#515154;font-size:14px}
pre{white-space:pre-wrap}</style>
<h1>Why your Mac restarted</h1><p class="big">%s</p>
<table><tr><th>Time</th><th>Memory free</th><th>Overflow in use</th><th>Biggest job</th></tr>%s</table>
<details><summary>Details</summary><pre>%s
%s
Source: %s</pre></details>""" % (line, trs or "<tr><td colspan=4>No samples were recorded in the minutes before.</td></tr>", html.escape(first), html.escape(comp), html.escape(path))
    os.makedirs(D + "/reports", exist_ok=True)
    out = "%s/reports/restart-%s.html" % (D, time.strftime("%Y-%m-%d-%H%M", time.localtime(t)))
    open(out, "w").write(page)
    write("log", "   REPORT %s -> %s\n" % (os.path.basename(path), out))
    if show:
        notify("Why your Mac restarted", re.sub(r"<[^>]+>", "", line))
        subprocess.Popen(["open", out])
    return out, re.sub(r"<[^>]+>", "", line)


def new_panics(state):
    seen = state.setdefault("reported", [])
    for p in glob.glob("/Library/Logs/DiagnosticReports/panic*.panic"):
        if p not in seen and time.time() - os.path.getmtime(p) < 3 * 86400:
            seen.append(p)
            try:
                report(p)
            except Exception as e:
                write("log", "   REPORT failed for %s: %s\n" % (p, e))
    state["reported"] = seen[-50:]


def tick(forever=False):
    """Watch: a full sample every minute, a cheap check every 5 s, full samples every 5 s under pressure.
    `run` does this forever (launchd keeps it alive); `tick` does one minute."""
    c, state = cfg(), load(STATE, {})
    end = time.time() + 47
    full = swept = 0
    last_swap, last = probe()[1], time.time()
    while forever or time.time() < end:
        now = time.time()
        free, swap = probe()
        rate = (swap - last_swap) / 1024 / max(1, now - last) * 60
        last_swap, last = swap, now
        hot = free <= c["hot_free_pct"] or rate >= c["hot_swap_grow_gb_min"] or bool(os.environ.get("BLACKBOX_TEST_FORCE"))
        if hot or now - full >= 60:
            if now - full >= 60:
                c = cfg(); new_panics(state); morning(c, state)
            try:
                sample(c, state); save(STATE, state)
            except Exception as e:
                write("log", "%s sample failed: %s\n" % (time.strftime("%T"), e))
            full = now
        if now - swept > 3600:
            swept = now
            for f in glob.glob(D + "/*.log") + glob.glob(D + "/*.jsonl"):
                if now - os.path.getmtime(f) > KEEP_DAYS * 86400:
                    os.remove(f)
        time.sleep(5)


LABEL = "com.blackbox.recorder"
PLIST = HOME + "/Library/LaunchAgents/%s.plist" % LABEL


def install():
    """Copy this file to ~/.blackbox and keep it running: started at sign-in, restarted if it ever stops."""
    home = HOME + "/.blackbox"
    os.makedirs(home, exist_ok=True); os.makedirs(os.path.dirname(PLIST), exist_ok=True)
    dest = home + "/blackbox.py"
    if os.path.realpath(dest) != os.path.realpath(HERE):
        open(dest, "w").write(open(HERE).read())
    open(PLIST, "w").write("""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict><key>Label</key><string>%s</string>
<key>ProgramArguments</key><array><string>/usr/bin/python3</string><string>%s</string><string>run</string></array>
<key>RunAtLoad</key><true/><key>KeepAlive</key><true/><key>ProcessType</key><string>Interactive</string>
<key>StandardErrorPath</key><string>%s/recorder.err</string></dict></plist>
""" % (LABEL, dest, home))
    run(["launchctl", "bootout", "gui/%d/%s" % (os.getuid(), LABEL)])
    run(["launchctl", "bootstrap", "gui/%d" % os.getuid(), PLIST])
    print("The recorder is running and will start by itself from now on. Ask it: python3 %s top" % dest)


def main(a):
    cmd = a[0] if a else "tick"
    if cmd in ("tick", "run"):
        tick(forever=cmd == "run")
    elif cmd == "sample":
        state = load(STATE, {}); print(sample(cfg(), state)[1], end=""); save(STATE, state)
    elif cmd == "report":
        print(*report(a[1], show="--quiet" not in a), sep="\n")
    elif cmd == "note":
        print(note())
    elif cmd == "status":
        held = load(GUARD, {"paused": []})["paused"]
        if not held:
            print("Nothing is paused.")
        for e in held:
            print(e["id"], e["at"], "%sGB" % e["gb"], said(e), "(%d processes)" % len(e["pids"]))
    elif cmd == "top":
        jobs, names = sorted(jobs_of(processes()).values(), key=lambda j: -j["mb"])[:5], cfg()["names"]
        print("The five biggest jobs by memory right now:")
        for i, j in enumerate(jobs, 1):
            print("%d. %s, %.1f GB" % (i, name_of(j["label"], j["pid"], names), j["mb"] / 1024))
    elif cmd == "why":
        found = sorted(glob.glob("/Library/Logs/DiagnosticReports/panic*.panic"), key=os.path.getmtime)
        print(report(found[-1], show=False)[1] if found else "No forced restart is on record.")
    elif cmd == "resume":
        print(release(a[1] if len(a) > 1 else "all", signal.SIGCONT), "processes resumed")
    elif cmd == "stop":
        print(release(a[1], signal.SIGTERM), "processes stopped")
    elif cmd == "install":
        install()
    elif cmd == "uninstall":
        run(["launchctl", "bootout", "gui/%d/%s" % (os.getuid(), LABEL)])
        if os.path.exists(PLIST):
            os.remove(PLIST)
        print("The recorder is switched off. Its record stays in %s; delete that folder to remove everything." % os.path.dirname(D))
    elif cmd == "ask":
        ask(a[1])
    else:
        print(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
