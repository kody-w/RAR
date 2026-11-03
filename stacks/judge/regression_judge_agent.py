"""Regression Judge — tells you when a change made your Brainstem worse.

Record a baseline once: a set of questions and the answers your Brainstem gives today.
After any change (a new model, a new or edited agent, a new distro) run a check: every
question is replayed against the live Brainstem, and a teacher grades the new answer
against the original one: same, better, worse or broken.

Lessons from those who did this before:
- Snapshot tests (Jest, insta): a new baseline is only ever accepted on purpose ("accept").
  Old baselines are kept, never overwritten.
- LLM judges favour whichever answer they read first: each pair is graded twice with the
  order swapped; if the two grades disagree the verdict is "unsure", not a guess.
- Facts beat opinions: a change in which agents were called, or an empty/error answer, is
  reported without asking a model.
The Brainstem kernel is never edited: replays and grading go through its own /chat.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/regression_judge_agent",
    "version": "1.0.0",
    "display_name": "RegressionJudge",
    "description": "Records a baseline of questions and answers, then after any change replays them on the live Brainstem and grades each new answer against the original: same, better, worse or broken.",
    "author": "kody-w",
    "tags": ["regression", "judge", "testing", "teacher-learner", "replay"],
    "category": "core",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

import html
import json
import os
import re
import time
import urllib.request
from pathlib import Path

from agents.basic_agent import BasicAgent

MAX_QUESTIONS = 25
NAME = re.compile(r"^[a-z0-9][a-z0-9_-]{0,47}$")
VERDICTS = ("same", "better", "worse", "broken")


def _home():
    d = Path(__file__).resolve().parent.parent / "judge-data"
    d.mkdir(exist_ok=True)
    return d


def _own_url():
    return f"http://127.0.0.1:{os.getenv('PORT', '7071')}"


def _target_url(target):
    """'' = this Brainstem; a distro name = that summoned distro; or a loopback URL."""
    t = (target or "").strip()
    if not t or t == "this":
        return _own_url()
    if re.match(r"^http://(127\.0\.0\.1|localhost):\d+/?$", t):
        return t.rstrip("/")
    st = Path.home() / ".brainstem" / "distros" / t / "state.json"
    if NAME.match(t) and st.exists():
        return f"http://127.0.0.1:{json.loads(st.read_text())['port']}"
    raise ValueError(f"I can't find a Brainstem called {t!r}. Use a summoned distro's name or http://127.0.0.1:<port>.")


def _chat(url, text, history=None, timeout=300):
    body = json.dumps({"user_input": text, "conversation_history": history or []}).encode()
    req = urllib.request.Request(f"{url}/chat", body, {"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            d = json.load(r)
    except Exception as e:  # a failed call is a result, not a crash
        return {"answer": "", "agents": [], "error": str(e)[:200]}
    return {"answer": (d.get("response") or "").strip(), "agents": _agents(d.get("agent_logs")), "error": d.get("error")}


def _agents(logs):
    """Names of the agents that ran, from the kernel's agent_logs (a list or text)."""
    if isinstance(logs, list):
        return sorted({str(l.get("agent") or l.get("name") or "") for l in logs if isinstance(l, dict)} - {""})
    return sorted(set(re.findall(r"\[([A-Za-z0-9_]+)\]", str(logs or ""))))


class _Busy:
    """One check at a time. Grading goes through this Brainstem's own /chat, so a model that
    tries to call the judge from inside a grading turn gets 'busy' instead of a loop."""
    def __init__(self):
        self.f = _home() / "busy.lock"

    def __enter__(self):
        if self.f.exists() and time.time() - self.f.stat().st_mtime < 3600:
            raise RuntimeError("busy")
        self.f.write_text(str(os.getpid()))
        return self

    def __exit__(self, *a):
        self.f.unlink(missing_ok=True)


GRADE = """You are a strict teacher grading a student's answer for a regression test. Do not use any tools.
Question: {q}

Answer A:
{a}

Answer B:
{b}

Is Answer B the same as, better than, or worse than Answer A at answering the question? "same" means
the same facts and usefulness even if worded differently. Reply with ONLY one JSON object:
{{"verdict": "same" | "better" | "worse", "why": "<one short sentence>"}}"""


def _grade_once(q, a, b):
    out = _chat(_own_url(), GRADE.format(q=q, a=a or "(empty)", b=b or "(empty)"), timeout=180)["answer"]
    m = re.search(r"\{.*\}", out, re.S)
    try:
        g = json.loads(m.group(0)) if m else {}
    except ValueError:
        g = {}
    v = str(g.get("verdict", "")).lower()
    return (v if v in ("same", "better", "worse") else None), str(g.get("why", ""))[:400]


def _grade(q, old, new):
    """Grade twice with the order swapped (position bias). Disagreement = unsure."""
    if not new["answer"] or new.get("error"):
        return "broken", "No answer came back" + (f": {new['error']}" if new.get("error") else ".")
    v1, why1 = _grade_once(q, old["answer"], new["answer"])   # B = new
    v2, why2 = _grade_once(q, new["answer"], old["answer"])   # B = old: flip the result back
    v2 = {"better": "worse", "worse": "better"}.get(v2, v2)
    if v1 is None or v2 is None:
        return "unsure", "The teacher did not give a clear grade."
    if v1 != v2:
        return "unsure", f"The two readings disagreed ({v1} vs {v2})."
    # Say it in the reader's words: in the first reading A was the original, B the new answer.
    why = re.sub(r"\bAnswer A\b", "Before", why1)
    return v1, re.sub(r"\bAnswer B\b", "Now", why)


class RegressionJudgeAgent(BasicAgent):
    def __init__(self):
        self.name = "RegressionJudge"
        self.metadata = {
            "name": self.name,
            "description": (
                "Catches regressions. 'record' a baseline (name + questions, or name + room to use a Rooms "
                "conversation) on a Brainstem; after any change, 'check' replays it and grades every new answer "
                "against the original (same/better/worse/broken); 'accept' makes the latest answers the new "
                "baseline on purpose; 'list' shows baselines. target = this Brainstem (default), a summoned "
                "distro's name, or http://127.0.0.1:<port>."),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string", "enum": ["record", "check", "accept", "list"]},
                    "name": {"type": "string", "description": "baseline name, lowercase, e.g. daily"},
                    "questions": {"type": "array", "items": {"type": "string"},
                                  "description": "questions to record (for record)"},
                    "room": {"type": "string", "description": "a Rooms room to take the owner's questions and the seats' answers from"},
                    "target": {"type": "string", "description": "which Brainstem to replay on"},
                },
                "required": ["action"],
            },
        }
        super().__init__(self.name, self.metadata)

    def perform(self, **kw) -> str:
        try:
            with _Busy():
                return getattr(self, "_" + kw.get("action", "list"))(**kw)
        except RuntimeError as e:
            if str(e) == "busy":
                return "The judge is busy with another check. Grade without tools."
            return f"The judge hit a problem: {e}"
        except (AttributeError, TypeError):
            return "Unknown action. Use record, check, accept or list."
        except Exception as e:
            return f"The judge hit a problem: {e}"

    # -- storage -------------------------------------------------------------------------
    def _dir(self, name):
        if not NAME.match(name or ""):
            raise ValueError("A baseline needs a short lowercase name.")
        d = _home() / name
        d.mkdir(exist_ok=True)
        return d

    def _latest(self, d):
        bs = sorted(d.glob("baseline-v*.json"), key=lambda p: int(p.stem.split("-v")[1]))
        return bs[-1] if bs else None

    def _save_baseline(self, d, data):
        last = self._latest(d)
        n = int(last.stem.split("-v")[1]) + 1 if last else 1
        p = d / f"baseline-v{n}.json"
        p.write_text(json.dumps(data, indent=1))  # never overwrites: every version is kept
        return n

    # -- actions -------------------------------------------------------------------------
    def _record(self, name="", questions=None, room="", target="", **_):
        d = self._dir(name)
        if self._latest(d):
            return f"A baseline called {name} already exists. Run 'check', or 'accept' to replace it on purpose."
        url = _target_url(target)
        cases = []
        if room:  # a Rooms conversation: the owner's turns, answered by the first seat that replied
            t = (target or "").strip()
            home = (Path.home() / ".brainstem" / "distros" / t) if NAME.match(t) \
                else Path(__file__).resolve().parent.parent
            log = home / "rooms-data" / "rooms" / f"{room}.jsonl"
            if not log.exists():
                return f"There is no Rooms conversation called {room} here."
            msgs = [json.loads(l) for l in log.read_text().splitlines() if l.strip()]
            for i, m in enumerate(msgs):
                if m["from"] == "owner":
                    reply = next((x for x in msgs[i + 1:] if x.get("reply_to") == m["id"]), None)
                    if reply:
                        cases.append({"question": m["text"], "history": [],
                                      "answer": reply["text"], "agents": [], "from": f"room {room}"})
        else:
            qs = [q.strip() for q in (questions or []) if q and q.strip()]
            if not qs:
                return "Give me some questions to record, or a room to take them from."
            for q in qs[:MAX_QUESTIONS]:
                r = _chat(url, q)
                cases.append({"question": q, "history": [], **r})
        if not cases:
            return "I found nothing to record."
        cases = cases[:MAX_QUESTIONS]
        self._save_baseline(d, {"target": target or "this", "recorded": time.strftime("%Y-%m-%d %H:%M"),
                                "cases": cases})
        return f"Baseline {name} recorded: {len(cases)} questions. After your next change, ask me to check {name}."

    def _check(self, name="", target="", **_):
        d = self._dir(name)
        base = self._latest(d)
        if not base:
            return f"There is no baseline called {name}. Record one first."
        b = json.loads(base.read_text())
        url = _target_url(target or (b["target"] if b["target"] != "this" else ""))
        rows = []
        for c in b["cases"]:
            new = _chat(url, c["question"], c.get("history"))
            verdict, why = _grade(c["question"], c, new)
            gained = sorted(set(new["agents"]) - set(c.get("agents", [])))
            lost = sorted(set(c.get("agents", [])) - set(new["agents"]))
            rows.append({"question": c["question"], "old": c["answer"], "new": new["answer"],
                         "agents": new["agents"], "verdict": verdict, "why": why,
                         "agents_gained": gained, "agents_lost": lost})
        stamp = time.strftime("%Y%m%d-%H%M%S")
        run = {"baseline": base.name, "target": url, "at": stamp, "rows": rows}
        (d / "runs").mkdir(exist_ok=True)
        (d / "runs" / f"{stamp}.json").write_text(json.dumps(run, indent=1))
        report = self._report(name, run)
        counts = {v: sum(r["verdict"] == v for r in rows) for v in VERDICTS + ("unsure",)}
        head = ", ".join(f"{n} {v}" for v, n in counts.items() if n)
        bad = [r for r in rows if r["verdict"] in ("worse", "broken")]
        lines = [f"Checked {name}: {len(rows)} questions. {head}."]
        for r in bad[:5]:
            lines.append(f"- {r['verdict'].upper()}: \"{r['question'][:80]}\": {r['why']}")
        moved = [r for r in rows if r["agents_gained"] or r["agents_lost"]]
        if moved:
            lines.append(f"{len(moved)} answer(s) used different agents than before.")
        lines.append("Nothing got worse." if not bad else
                     "If the new answers are what you want, say 'accept' to make them the baseline.")
        lines.append(f"Full side-by-side report: {report}")
        return "\n".join(lines)

    def _accept(self, name="", **_):
        d = self._dir(name)
        runs = sorted((d / "runs").glob("*.json")) if (d / "runs").is_dir() else []
        if not runs:
            return f"Run a check of {name} first; then I can accept its answers."
        run = json.loads(runs[-1].read_text())
        if any(r["verdict"] == "broken" for r in run["rows"]):
            return "The latest check has broken answers, so I won't make it the baseline."
        old = json.loads(self._latest(d).read_text())
        cases = [{**c, "answer": r["new"], "agents": r["agents"]} for c, r in zip(old["cases"], run["rows"])]
        n = self._save_baseline(d, {**old, "recorded": time.strftime("%Y-%m-%d %H:%M"), "cases": cases,
                                    "accepted_from": runs[-1].name})
        return f"The latest answers are now baseline v{n} of {name}. Earlier versions are kept."

    def _list(self, **_):
        names = sorted(p.name for p in _home().iterdir() if p.is_dir())
        if not names:
            return "No baselines yet. Ask me to record one."
        out = []
        for n in names:
            last = self._latest(_home() / n)
            if last:
                b = json.loads(last.read_text())
                out.append(f"{n}: {len(b['cases'])} questions, {last.stem.replace('baseline-', '')}, recorded {b['recorded']}")
        return "\n".join(out)

    def _report(self, name, run):
        """One self-contained page: the verdict first, then each question side by side."""
        color = {"same": "#6e7781", "better": "#1a7f37", "worse": "#cf222e", "broken": "#cf222e", "unsure": "#9a6700"}
        rows = sorted(run["rows"], key=lambda r: ["broken", "worse", "unsure", "better", "same"].index(r["verdict"]))
        cards = "".join(
            f"<section><h3><span style='background:{color[r['verdict']]}'>{r['verdict']}</span> {html.escape(r['question'])}</h3>"
            f"<p class=why>{html.escape(r['why'])}</p><div class=two><div><b>Before</b><p>{html.escape(r['old'])}</p></div>"
            f"<div><b>Now</b><p>{html.escape(r['new'])}</p></div></div>"
            + (f"<p class=why>Agents now: {html.escape(', '.join(r['agents']) or 'none')}"
               f"{' (new: ' + html.escape(', '.join(r['agents_gained'])) + ')' if r['agents_gained'] else ''}"
               f"{' (no longer: ' + html.escape(', '.join(r['agents_lost'])) + ')' if r['agents_lost'] else ''}</p>"
               if r["agents_gained"] or r["agents_lost"] else "")
            + "</section>" for r in rows)
        bad = sum(r["verdict"] in ("worse", "broken") for r in rows)
        title = "Nothing got worse" if not bad else f"{bad} answer{'s' if bad > 1 else ''} got worse"
        page = f"""<!doctype html><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1">
<title>{html.escape(name)}: {title}</title><style>
body{{font:16px -apple-system,Segoe UI,sans-serif;max-width:960px;margin:32px auto;padding:0 16px;color:#1f2328}}
h1{{margin:0}}.sub{{color:#656d76;margin:4px 0 24px}}section{{border:1px solid #d0d7de;border-radius:12px;padding:16px;margin:12px 0}}
h3{{margin:0 0 6px;font-size:17px}}h3 span{{color:#fff;border-radius:6px;padding:2px 8px;font-size:13px;margin-right:6px;text-transform:uppercase}}
.why{{color:#656d76;margin:4px 0}}.two{{display:grid;grid-template-columns:1fr 1fr;gap:16px}}.two p{{white-space:pre-wrap;margin:4px 0}}
@media(max-width:640px){{.two{{grid-template-columns:1fr}}}}</style>
<h1>{title}</h1><p class=sub>{html.escape(name)} &middot; {len(rows)} questions &middot; checked {run['at']} against {html.escape(run['baseline'])}</p>{cards}"""
        p = _home() / name / "runs" / f"{run['at']}.html"
        p.write_text(page)
        return str(p)
