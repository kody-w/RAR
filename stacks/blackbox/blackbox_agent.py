"""Blackbox: plain answers about this computer's memory, from the recorder that watches it.
What is using the most memory, why the computer last restarted itself, what the guard has frozen, what the guard did
in the last day, and letting a frozen job carry on or stopping it. No model, no guessing: it reads the recorder's own
answers and record. The recorder itself is a separate always-on job; this file is only its voice."""
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rapp/blackbox_agent",
    "version": "1.0.0",
    "display_name": "Blackbox",
    "description": "Plain answers about this computer's memory: what is biggest, why it restarted, what is frozen, what the guard did, and letting a frozen job carry on or stopping it.",
    "author": "RAPP",
    "tags": ["computer", "memory", "guard", "morning"],
    "category": "general",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

import os, re, subprocess, sys
from pathlib import Path
try:
    from agents.basic_agent import BasicAgent
except Exception:
    class BasicAgent:
        def __init__(self, name=None, metadata=None): self.name, self.metadata = name, metadata

ASKS = ["biggest", "why_restarted", "frozen", "what_it_did", "carry_on", "stop"]


def _recorder():
    p = Path(os.environ.get("BLACKBOX_PATH", str(Path.home() / ".blackbox/blackbox.py")))
    return p if p.is_file() else None


def _say(*args):
    r = subprocess.run(["/usr/bin/python3", str(_recorder())] + list(args), capture_output=True, text=True, timeout=90)
    return r.stdout.strip()


def _frozen():
    """[(id, when, size, name)] of what the guard holds frozen right now."""
    out = []
    for line in _say("status").splitlines():
        m = re.match(r"(g\w+) (\S+ \S+) ([\d.]+)GB (.*?) \(\d+ processes\)$", line)
        if m:
            out.append((m[1], m[2], float(m[3]), m[4]))
    return out


class BlackboxAgent(BasicAgent):
    def __init__(self):
        self.name = "Blackbox"
        self.metadata = {"name": self.name, "description": (
            "Answers questions about THIS computer's memory from its own recorder, in plain words. Use it when the owner asks what is "
            "slowing the computer down or using the most memory, why the computer restarted or crashed, what was frozen or paused, what "
            "happened overnight, or asks to let a frozen job carry on or to stop one. Say its answer back as it is; do not add numbers of your own. "
            "It never stops a job unless asked with ask='stop' and that job's id."),
            "parameters": {"type": "object", "properties": {
                "ask": {"type": "string", "enum": ASKS, "description": (
                    "Which answer is wanted. 'biggest' = the five jobs using the most memory now. 'why_restarted' = one sentence on why the "
                    "computer last restarted itself. 'frozen' = what the guard holds frozen now, each with an id. 'what_it_did' = what the guard "
                    "did in the last day (use this for 'what happened overnight' or a morning catch-up). 'carry_on' = let a frozen job run again. "
                    "'stop' = end a frozen job for good. If unsure, use 'what_it_did'.")},
                "job": {"type": "string", "description": (
                    "Only for 'carry_on' and 'stop': the id of the frozen job, exactly as 'frozen' gave it (it looks like g12345). For 'carry_on' "
                    "you may give 'all' to let every frozen job run again. 'stop' needs one id and never accepts 'all'. Leave empty otherwise.")}},
                "required": ["ask"]}}
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kw):
        try:
            if not _recorder():
                return "The Blackbox recorder is not on this computer yet, so I have nothing to read."
            ask, job = str(kw.get("ask") or "what_it_did").strip(), str(kw.get("job") or "").strip()
            if ask == "biggest":
                return _say("top") or "The recorder gave no answer."
            if ask == "why_restarted":
                return _say("why") or "The recorder gave no answer."
            if ask == "what_it_did":
                return _say("note") or "The recorder gave no answer."
            held = _frozen()
            if ask == "frozen":
                if not held:
                    return "Nothing is frozen."
                return "Frozen right now: " + "; ".join("%s, %s GB, since %s (id %s)" % (n[:50], ("%.0f" if gb >= 10 else "%.1f") % gb, at[11:16], i) for i, at, gb, n in held) + "."
            if ask in ("carry_on", "stop"):
                if not held:
                    return "Nothing is frozen, so there is nothing to %s." % ("let go" if ask == "carry_on" else "stop")
                ids = {i: n for i, _, _, n in held}
                if ask == "stop" and job not in ids:
                    return "To stop a job I need its id. Frozen right now: " + "; ".join("%s (id %s)" % (n[:50], i) for i, n in ids.items()) + "."
                if ask == "carry_on" and job not in ids and job != "all":
                    if len(ids) > 1:
                        return "Which one? Frozen right now: " + "; ".join("%s (id %s)" % (n[:50], i) for i, n in ids.items()) + ". Or say all."
                    job = next(iter(ids))
                _say("resume" if ask == "carry_on" else "stop", job)
                left = {i for i, _, _, _ in _frozen()}
                gone = [n for i, n in ids.items() if i not in left]
                if not gone:
                    return "I asked, but it is still frozen. Nothing changed."
                return "%s: %s." % ("Running again" if ask == "carry_on" else "Stopped for good", ", ".join(n[:50] for n in gone))
            return "I can answer: " + ", ".join(ASKS) + "."
        except Exception as e:
            return "I could not read the recorder (%s)." % type(e).__name__


if __name__ == "__main__":      # self-test: every read-only answer comes back as plain words
    a, ok = BlackboxAgent(), 0
    for ask in ["biggest", "why_restarted", "frozen", "what_it_did"]:
        out = a.perform(ask=ask); good = bool(out) and "could not read" not in out and "{" not in out
        ok += good; print("%s %s: %s" % ("PASS" if good else "FAIL", ask, out.replace("\n", " | ")[:150]))
    out = a.perform(ask="stop", job="all"); good = "need its id" in out or "Nothing is frozen" in out
    ok += good; print("%s stop refuses 'all': %s" % ("PASS" if good else "FAIL", out[:100]))
    print("%d of 5" % ok); sys.exit(0 if ok == 5 else 1)
