#!/usr/bin/env python3
"""cartridge.py check <file> | repair <file> <out> | next <file> | join <old> <continuation> <out> | grew <older> <newer> | from-claude <session.jsonl> <out.json>

The checker and tools for a chat cartridge (SKILL.md): the Brainstem chat export shape, carrying the NEXT sense.
  check        CARTRIDGE ok | CARTRIDGE fail <reason>   (shape, roles, the handover turn, exactly three next jobs)
  next         prints the three jobs, one per line
  join         old cartridge + a continuation (new turns only) -> one cartridge; the tool copies the old turns, never an AI
  grew         RELAY ok when <newer> starts with every turn of <older>, unchanged, and adds at least one turn
  from-claude  turns a Claude Code session file into a cartridge with no AI in the loop (the person's words verbatim,
               tool calls dropped, hook and system text dropped); the file stays local: shipping it is stream.py's job

Prior art, applied: mbox and IMAP (your mail outlives the mail program because the file is plain and every program
reads it), Google Takeout (an export nobody can import is a dead copy, so the format here is one a running system
already imports), vCard (one small file, any vendor)."""
import json, re, sys, time, uuid

def load(p):
    t = open(p, encoding="utf-8").read().strip()
    try: return json.loads(t)                      # a saved file is the object itself
    except ValueError: pass
    m = re.search(r"```(?:json)?\s*(\{.*\})\s*```", t, re.S)   # an AI that cannot write files prints one json code block
    if m:
        try: return json.loads(m.group(1))
        except ValueError: pass
    i, j = t.find("{"), t.rfind("}")               # a chatty AI says a line before or after: take the outermost object
    if i < 0 or j < i: raise ValueError("no JSON object found")
    return json.loads(t[i:j + 1])

def repair(c):
    """Be liberal in what you accept (Postel). An AI that only got a summary of the page drifts in known ways: a made-up
    'handover' role with its own fields, extra keys on turns, jobs as plain strings. The person's and assistant's words
    are never touched; only the handover is put back into shape. Returns the cartridge and a list of what was repaired."""
    fixed = []
    if not isinstance(c, dict) or not isinstance(c.get("turns"), list): return c, fixed
    T = []
    for t in c["turns"]:
        if not isinstance(t, dict): continue
        if t.get("role") in ("user", "assistant") and isinstance(t.get("content"), str): T.append(t); continue
        said, jobs = [], None   # a turn in some other shape: read its fields as the handover
        for k, v in t.items():
            if k == "role": continue
            if isinstance(v, list) and "next" in k.lower(): jobs = v
            elif isinstance(v, list): said.append("%s: %s" % (k.replace("_", " ").capitalize(), "; ".join(str(x) for x in v) or "nothing"))
            elif isinstance(v, str) and v.strip(): said.append(v.strip() if k == "content" else "%s: %s" % (k.replace("_", " ").capitalize(), v.strip()))
        body = "\n".join(said)
        if jobs is not None: body += "\n|||NEXT|||" + json.dumps([j if isinstance(j, dict) else {"n": i + 1, "job": str(j)} for i, j in enumerate(jobs)], ensure_ascii=False)
        T.append({"role": "assistant", "content": body or "(empty)"}); fixed.append("a '%s' turn was read as the handover" % t.get("role"))
    for k in ("next", "next_jobs", "NEXT"):   # jobs left at the top of the file
        if isinstance(c.get(k), list) and T and T[-1]["role"] == "assistant" and "|||NEXT|||" not in T[-1]["content"]:
            T[-1] = dict(T[-1], content=T[-1]["content"] + "\n|||NEXT|||" + json.dumps([j if isinstance(j, dict) else {"n": i + 1, "job": str(j)} for i, j in enumerate(c[k])], ensure_ascii=False)); fixed.append("jobs at the top of the file were moved into the handover")
    c = dict(c, turns=T)
    if fixed: c["repaired"] = fixed
    return c, fixed

def split_next(text):
    if "|||NEXT|||" not in text:   # be liberal in what you accept (Postel): a plain 1. 2. 3. list at the very end is read as the three jobs
        L = text.rstrip().split("\n"); got = []
        while L and re.match(r"\s*(\d)[.)]\s+\S", L[-1]): got.insert(0, L.pop())
        if [int(re.match(r"\s*(\d)", g).group(1)) for g in got] == [1, 2, 3]:
            return "\n".join(L).strip(" \n-"), [{"n": i + 1, "job": re.sub(r"^\s*\d[.)]\s+", "", g).strip()} for i, g in enumerate(got)]
        return text.strip(), None
    a, b = text.split("|||NEXT|||", 1); m = re.search(r"\[.*\]", b, re.S)
    try:
        if m: return a.strip(), json.loads(m.group(0))
    except Exception: pass
    got = [l for l in b.split("\n") if re.match(r"\s*\d[.)]\s+\S", l)]   # the marker, then a plain 1. 2. 3. list
    return a.strip(), [{"n": i + 1, "job": re.sub(r"^\s*\d[.)]\s+", "", g).strip()} for i, g in enumerate(got)] if got else None

def check(c):
    if not isinstance(c, dict): return "not one JSON object"
    for k in ("exported_at", "session_id", "model", "turns"):
        if k not in c: return "missing " + k
    T = c["turns"]
    if not isinstance(T, list) or len(T) < 2: return "turns must hold the chat (at least 2)"
    for i, t in enumerate(T):
        if not isinstance(t, dict) or t.get("role") not in ("user", "assistant"): return "turn %d: role must be user or assistant" % i
        if not isinstance(t.get("content"), str) or not t["content"].strip(): return "turn %d: content must be a non-empty string" % i
    if not any(t["role"] == "user" for t in T): return "no user turn"
    if c.get("source") and "|||NEXT|||" not in T[-1]["content"]: return ""   # a converted transcript: the chat as it was, no handover yet
    if T[-1]["role"] != "assistant": return "the last turn must be the assistant's handover"
    stand, jobs = split_next(T[-1]["content"])
    if jobs is None: return "the handover has no readable |||NEXT||| list"
    if len(stand) < 20: return "the handover does not say where things stand"
    if not isinstance(jobs, list) or len(jobs) != 3: return "NEXT must be exactly three jobs"
    for j in jobs:
        if not isinstance(j, dict) or not str(j.get("job", "")).strip(): return "each next job needs a job sentence"
    return ""

def grew(a, b):
    A, B = a["turns"], b["turns"]; keep = [t for t in A]
    if len(B) <= len(A): return "the newer cartridge adds no turns"
    for i, t in enumerate(keep):
        if (B[i].get("role"), B[i].get("content")) != (t.get("role"), t.get("content")): return "turn %d of the older cartridge was changed or dropped" % i
    if a.get("session_id") != b.get("session_id"): return "session_id was not kept"
    return ""

def join(a, b):
    """Old cartridge + a continuation (new turns only) -> one cartridge. The old turns are copied by this tool, never by an AI."""
    if b.get("continues") != a.get("session_id"): raise ValueError("the continuation does not name this cartridge (continues != session_id)")
    if b.get("after_turns") != len(a["turns"]): raise ValueError("the continuation says it follows %s turns; the cartridge has %d" % (b.get("after_turns"), len(a["turns"])))
    c = dict(a); c["turns"] = a["turns"] + b["turns"]; c["exported_at"] = b.get("exported_at", a["exported_at"]); c["model"] = b.get("model", a.get("model"))
    c["carried_by"] = (a.get("carried_by") or [a.get("model")]) + [b.get("model")]; return c

def from_claude(src, out):
    turns = []
    for l in open(src, encoding="utf-8"):
        try: x = json.loads(l)
        except Exception: continue
        if x.get("type") not in ("user", "assistant") or x.get("isSidechain") or x.get("isMeta"): continue
        c = (x.get("message") or {}).get("content"); role = x["type"]
        if isinstance(c, list): c = "\n".join(p.get("text", "") for p in c if isinstance(p, dict) and p.get("type") == "text")
        if not isinstance(c, str): continue
        c = re.sub(r"<system-reminder>.*?</system-reminder>", "", c, flags=re.S).strip()
        if not c or c.startswith("<") or "tool_use_id" in c[:80]: continue
        if role == "user" and (c.startswith("This session is being continued from a previous conversation") or c.startswith("[SYSTEM NOTIFICATION")): continue   # the tool's own summary, not the person
        if turns and turns[-1]["role"] == role: turns[-1]["content"] += "\n\n" + c
        else: turns.append({"role": role, "content": c})
    cart = {"exported_at": time.strftime("%Y-%m-%dT%H:%M:%S.000Z", time.gmtime()), "session_id": str(uuid.uuid4()), "model": "claude-code session", "source": "claude-code", "turns": turns}
    json.dump(cart, open(out, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print("wrote %s: %d turns (%d the person's), %d bytes" % (out, len(turns), sum(t["role"] == "user" for t in turns), len(json.dumps(cart))))

if __name__ == "__main__":
    a = sys.argv[1:]
    try:
        if a[:1] == ["check"]:
            c, fx = repair(load(a[1])); w = check(c); print(("CARTRIDGE ok" + (" after repair (%s)" % "; ".join(fx) if fx else "")) if not w else "CARTRIDGE fail " + w); sys.exit(1 if w else 0)
        elif a[:1] == ["repair"]:
            c, fx = repair(load(a[1])); w = check(c)
            if w: print("CARTRIDGE fail " + w); sys.exit(1)
            json.dump(c, open(a[2], "w", encoding="utf-8"), indent=1, ensure_ascii=False); print("REPAIRED %s: %s" % (a[2], "; ".join(fx) or "nothing needed"))
        elif a[:1] == ["next"]: print("\n".join("%s. %s" % (j.get("n", i + 1), j["job"]) for i, j in enumerate(split_next(load(a[1])["turns"][-1]["content"])[1] or [])))
        elif a[:1] == ["grew"]: w = grew(load(a[1]), load(a[2])); print("RELAY ok" if not w else "RELAY fail " + w); sys.exit(1 if w else 0)
        elif a[:1] == ["join"]:
            c = join(load(a[1]), load(a[2])); w = check(c)
            if w: print("CARTRIDGE fail " + w); sys.exit(1)
            json.dump(c, open(a[3], "w", encoding="utf-8"), indent=1, ensure_ascii=False); print("JOINED %s: %d turns, carried by %s" % (a[3], len(c["turns"]), " -> ".join(str(m) for m in c["carried_by"])))
        elif a[:1] == ["from-claude"]: from_claude(a[1], a[2])
        else: print(__doc__)
    except (OSError, ValueError, IndexError) as e: print("CARTRIDGE fail %s: %s" % (type(e).__name__, str(e)[:120])); sys.exit(1)
