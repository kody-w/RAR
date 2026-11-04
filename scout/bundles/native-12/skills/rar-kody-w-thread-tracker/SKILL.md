---
name: "rar-kody-w-thread-tracker"
description: "Routes remarks into durable local topic threads, lists open work, and parks or closes threads without deleting their history."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/thread_tracker_agent", "rar_sha256": "c6768a7a25c21f3047e8cb47a96528f83f126742bdbafb9f13e4df4ebb30aad5", "source_kind": "rar-agent", "source_commit": "working-tree", "author": "kody-w", "tags": ["threads", "notes", "routing", "append-only", "offline"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/thread_tracker_agent`. The original RAPP
agent is preserved byte-for-byte in `thread_tracker_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

Thread Tracker — local append-only topic routing that keeps work from getting lost.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "enum": [
        "place",
        "open",
        "list",
        "topics",
        "close",
        "park",
        "show"
      ],
      "type": "string"
    },
    "reason": {
      "type": "string"
    },
    "text": {
      "type": "string"
    },
    "thread": {
      "type": "string"
    }
  },
  "required": [
    "action"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `thread_tracker_agent.py` and embedded as the fenced Python below (sha256 c6768a7a25c21f30…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `thread_tracker_agent.py` first:

```bash
python3 thread_tracker_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 thread_tracker_agent.py   # or on stdin
python3 thread_tracker_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/thread_tracker_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/thread_tracker_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/thread_tracker_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""Thread Tracker — local append-only topic routing that keeps work from getting lost."""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/thread_tracker_agent",
    "version": "1.0.0",
    "display_name": "Thread Tracker",
    "description": "Routes remarks into durable local topic threads, lists open work, and parks or closes threads without deleting their history.",
    "author": "kody-w",
    "tags": ["threads", "notes", "routing", "append-only", "offline"],
    "category": "productivity",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import threading
import uuid

try:
    from agents.basic_agent import BasicAgent
except ImportError:
    try:
        from basic_agent import BasicAgent
    except ImportError:
        class BasicAgent:
            def __init__(self, name=None, metadata=None):
                if name is not None:
                    self.name = name
                if metadata is not None:
                    self.metadata = metadata

            def perform(self, **kwargs):
                return "Not implemented."


_LOCK = threading.RLock()
_WORDS = re.compile(r"[a-z0-9][a-z0-9_-]{1,}")
_STOP = {
    "about", "after", "again", "also", "been", "being", "from", "have",
    "into", "just", "more", "that", "their", "then", "this", "what", "when",
    "where", "which", "with", "would", "your",
}


def _store():
    configured = os.environ.get("RAPP_THREAD_STORE")
    if configured:
        return Path(configured).expanduser()
    return Path.home() / ".rapp" / "agent_data" / "thread_tracker.jsonl"


def _now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _terms(text):
    return {
        word for word in _WORDS.findall(text.casefold())
        if word not in _STOP
    }


def _load():
    path = _store()
    if not path.exists():
        return []
    events = []
    previous = ""
    with path.open(encoding="utf-8") as handle:
        for number, line in enumerate(handle, 1):
            event = json.loads(line)
            payload = {key: value for key, value in event.items() if key != "hash"}
            expected = hashlib.sha256(
                json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
            ).hexdigest()
            if event.get("previous") != previous or event.get("hash") != expected:
                raise ValueError(f"thread record is corrupt at line {number}")
            events.append(event)
            previous = event["hash"]
    return events


def _append(kind, payload):
    with _LOCK:
        events = _load()
        path = _store()
        path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
        if os.name != "nt":
            path.parent.chmod(0o700)
        event = {
            "utc": _now(),
            "kind": kind,
            "payload": payload,
            "previous": events[-1]["hash"] if events else "",
        }
        event["hash"] = hashlib.sha256(
            json.dumps(event, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest()
        with path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(event, sort_keys=True) + "\n")
        if os.name != "nt":
            path.chmod(0o600)
        return event


def _threads():
    threads = {}
    for event in _load():
        payload = event["payload"]
        identifier = payload.get("thread")
        if not identifier:
            continue
        item = threads.setdefault(identifier, {
            "thread": identifier,
            "topic": "",
            "notes": [],
            "state": "open",
            "opened": event["utc"],
            "touched": event["utc"],
            "terms": set(),
        })
        item["touched"] = event["utc"]
        if event["kind"] == "thread.opened":
            item["topic"] = payload["topic"]
            item["terms"].update(payload.get("terms", []))
        elif event["kind"] == "thread.note":
            item["notes"].append(payload["note"])
            item["terms"].update(payload.get("terms", []))
        elif event["kind"] == "thread.closed":
            item["state"] = "closed"
            item["reason"] = payload.get("reason", "")
        elif event["kind"] == "thread.parked":
            item["state"] = "parked"
    return threads


def _best_match(terms, threads, floor=2):
    candidates = []
    for item in threads.values():
        if item["state"] == "closed":
            continue
        score = len(terms & item["terms"])
        candidates.append((score, item["touched"], item["thread"], item))
    if not candidates:
        return None, 0
    score, _, _, item = max(candidates)
    return (item, score) if score >= floor else (None, score)


class ThreadTrackerAgent(BasicAgent):
    def __init__(self):
        self.name = "ThreadTracker"
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": [
                            "place", "open", "list", "topics",
                            "close", "park", "show",
                        ],
                    },
                    "text": {"type": "string"},
                    "thread": {"type": "string"},
                    "reason": {"type": "string"},
                },
                "required": ["action"],
            },
        }
        super().__init__(self.name, self.metadata)

    def perform(self, **kwargs) -> str:
        action = str(kwargs.get("action") or "list").strip().lower()
        threads = _threads()
        text = str(kwargs.get("text") or "").strip()
        if action in ("place", "open"):
            if not text:
                return "Provide a remark or topic."
            terms = _terms(text)
            match, score = (None, 0) if action == "open" else _best_match(
                terms, threads
            )
            if match:
                _append("thread.note", {
                    "thread": match["thread"],
                    "note": text[:1000],
                    "terms": sorted(terms),
                })
                return (
                    f"Placed on thread {match['thread']} "
                    f"({score} shared terms): {match['topic'][:100]}"
                )
            identifier = uuid.uuid4().hex[:10]
            _append("thread.opened", {
                "thread": identifier,
                "topic": text[:500],
                "terms": sorted(terms),
            })
            return f"Opened thread {identifier}: {text[:120]}"
        if action in ("close", "park"):
            identifier = str(kwargs.get("thread") or "").strip()
            if identifier not in threads:
                return f"No thread {identifier}."
            _append(
                "thread.closed" if action == "close" else "thread.parked",
                {
                    "thread": identifier,
                    "reason": str(kwargs.get("reason") or "")[:500],
                },
            )
            return f"Thread {identifier} {action}d. History was preserved."
        if action == "show":
            identifier = str(kwargs.get("thread") or "").strip()
            item = threads.get(identifier)
            if not item:
                return f"No thread {identifier}."
            safe = {**item, "terms": sorted(item["terms"])}
            return json.dumps(safe, indent=2, sort_keys=True)
        if action == "topics":
            if not threads:
                return "Nothing tracked yet."
            latest_day = max(item["touched"][:10] for item in threads.values())
            items = [
                item for item in threads.values()
                if item["touched"][:10] == latest_day
            ]
            counts = Counter()
            for item in items:
                counts.update(item["terms"])
            lines = [f"Covered on {latest_day}:"]
            lines.extend(
                f"[{item['state']}] {item['thread']} {item['topic'][:100]}"
                for item in sorted(items, key=lambda value: value["touched"])
            )
            recurring = [
                term for term, count in counts.most_common(8) if count > 1
            ]
            if recurring:
                lines.append("Recurring terms: " + ", ".join(recurring))
            return "\n".join(lines)
        active = [
            item for item in threads.values() if item["state"] != "closed"
        ]
        if not active:
            return "No open threads."
        return "\n".join(
            f"{item['thread']} [{item['state']}] "
            f"{len(item['notes'])} note(s): {item['topic'][:100]}"
            for item in sorted(active, key=lambda value: value["touched"])
        )


if __name__ == "__main__":
    print(ThreadTrackerAgent().perform(action="list"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/7VaWZObypL+K0zPg+1Lu8UmkHriTAyrhAQISYCWY8cxS4GQ2MQuPP7vU0hye2ufeydiph/cQGXl8uVSldn+/GBX5SHNH54fTql3ed88PD54oHDzMCvDNIGfV2lVggLJQWznpwIJkzJFvCq3nQggUeraEVKmWegi5SEHtlc8IlFYlAWSZiBBmjQ/PSJ24iHZdXOaI26UFpDdnRppQii9KhEPRKAMkwAugDBHDpBHml+eoDagteMsAsXD858fHx9C+Pzw/PnBjewCfnowrnyM3HZPIGcDkJRwS2QnAVzLLpB3At8zkPtpHsNPHvCR+9vbAkT+I/KPf5waOw+Kd8j7/0SKMn/+kCD3H9vtIUD+6D+/vVE9BaB8++HhtvLh4V1v0YeH3mL48gTpwuztu6cobUD+9t03Tl+t/QP56/74wypoy9ek9N9fZHzH/9vO0P+qZJggcEcW2S748PAI6Xv84Z7vzLlvSNLyKvGnlf4nB2WVJ3Cznqd16AHEvru9V+Hq5SeoyA/bSpDHN7v6h7c943c/UsR26R4ekcJNcwAJ32ppAh4R7N13yv/xx4vCCIgKgPzlgKL867rz7a9qXkU9fgX1x/V3v9h75fKKsX/ZGZTo9ThfGT1BYK7Yff6Vtv/5Svfh4fnG889vXz4+/m7PjenzFfE/n3EMw35Pe7WrJy7SvATe2+v7u1fIv7z7re/evs7chz7tY8NDINw3rZHPNyve3F7ffPyC/Ozc73a//Xx14BekONg5ZHPT7fkbkz463ny8mvjxy2uMfvaMB3M19EOQw6CoqtB76v+hYPYcQNuz+fgj/S/u6uMFeL9x2PfO+ibp8VXCXvNvLhq+7qF/0Ts/e+buFQjg4qruC/bflPoCQbxHB/ETdD+n97V23tK7r6evpPf3oP5aT+6Q/F1FuYv9jlFfL8KvQVP8vmpAG7X0Nft+qRkvrvyt256ulkJVfy4SdwRuVeKFugfjGgq/cvwXkvlv4+NGDEmLvt4//wrq16VvoP42hr48/m2t+oaj8SuIyOcbDF+8J2R6OxyRxi6QLAcFyGvgPb0eOFfUikPaQOX/X2KlBDHcf4+O6+ZvjN+9evj0W/4vwqiw/f5A+fyPf/QcH19J0f77ny+fP7778irgR+i/J6+Ks+Jtz/IRRnsv9Q/i8crnrxO4FH8YeQXe/Rbgaw0pfoX4ftr+s9TpTS4P19vP9SLjIRdQ/mJvZJf9qejZF2h1bLcv5qWVe+jD/1p9PyLwcnNzy7esfartqALw0vGK9/rT+89fVbty+DtWr2zxkd+oBEH6pv2PG38q825aJWWvEt8//HiLuh5F32l01f4VVG88nqrMgzJ/CYKfQA0TcEUAxh2f1iC/HZGfv6n75RnuemXTE6zZr1cxyOrPz1exb4oS8oFH60fk/uHbYfv1wz89OL83+bvAhjcgGJl/RHbseDZy9crz7dcPDnj3T2qOW+V5H3mvBkEP2lV+//B4A7ZX445wnEKI3DSO0+Tt6Hqhu1H8J4L/rZMh4YvgV/x3g/flvF+96Hj14TNMFwRFbsfg0zENk7cvzN69XlIhqh+Sr8RX7u9+vOXX4Ff7/2kCfBfvVzdDsJF/ezmkvO9d+fGHytHXhJvU59+oCyvgtX/6KvJ7Xq/Z9FOOfHj4Jdp+DcifQ63fFYHkli9v+ntr8QaWzF5b8PZ61ftXAvaVYL2Z+r+O1ncPX2C7l8BTp7pW2r7b+/d/R9TQzdMi9Utk7faNYw4DLowBxCIxYNeIhH1vCSBKMJeLsG9Sb3RZnh7BrWSnPvLpv27d7uCG0F+3upv/Zfcd5KcnxIAs0jwMwgT2tytW1z8k16We/cuRiziXEryHFr/vH3qLP73G7im7fLr2wNcYAsiKlxHXzooqAk+92psD9PRNSddOENDCaC6/9tZ+CFvfR2hOkUYwSsvexOIURhHihTDsr/eAnjeE4bln9unTJ8cuDh+SW/NLIrdWvhhAghd1kPfvoRF+FAaH8kMC3EOKvPn85Q3y38jf7boy72XosPW+gww1nK0XGgJvDlUM+srde6w/unuQP3+5QwnZJPCeAV3Sn+W3zTAP+0vbHdf1lH1PDGnEAX7fJ8I2HwZPn/Nh+YTIPvKiLxTaLxWwNz3A8oN4oC8TIHEvkKsNzXlBsk+zwi7Dwr88IlUBrlI/Obl9VTH+y4XknxCV12Frm/ZTjF7NKxHcnCYhhP/F67fvkEn+pkC4ryyeEK0Ps364YWeH3L7L8O2bX2AqfN0OmdtIApoPST/AAD1Udh+LN3ggEUTGvbv0fe9zpC+r0LHFV9lXGpi7HmKkNhSef0iKezzDhqyvp/3pdUEC2EXZiQv+4x5S8O5XRd4VP6hpz+nuBe/uladb6lzvW/c5CvKhIjCcuofgrRC/T5Poch/15JDxbVZjlzCtQVZcJz2In6cxVLS8LsIiWPbzmyh0AVT14TmpoujxIbFj8PPcph/RQAhjAM0q+ukOTNYMQP+D69vtptU/gaSKH57/vM054K6+SF5FFP3Y53YLgw/XAnxjeoK/+usvbNEfykvWi+7vsUnQV5fb3b1n/MtS35G9vnBV/JWlK79zBV3o9Srelf4mNnX6+tOzgNqXt3nU5wdosw2vKfbd6nuJguS5nb8veg8O8CcMGgHfb5kI1/6ueN1JYZsO0wnSujRDj2wGvrkE7pMYxYCR61CMPaaHxMgfkT5O0AxFOJ5j+87Yx0lAeT4FHIfEbNsb9vilVe6C60Ef9uJ7X0OT35c5AN+W4SfvrvdNkR6Rl1p59eNN/c8PDk1ByilVyOzthx+glu1s9WN5mKJ5hHLqUcXB3szQ8XlkcXFUWc2lM/HaPdA+QbaNtjrbB/4C5rLMLdVqfj4N0dV0ePBPESk1gr83ojFqrbUhtuTDkRVuh4x3ANRxXNS6PhL9ihzinmthkzM69E4aHa3PhCHoC0ooLpImjrvBxgz3l44xcxafF6QxJw1lomXGWdsuGGy9WGOKYi8Mn17oxKyICCpaF+lM4dziWILd7Hhkyw1vh4e5RXfz2egwqIdNKUqKzFzUDV1aw1mXHZc1zhm77c4p5m0cLZZtESuoWBmTJrS1ohP2q8GCGQ8nhB1RqF+gA0PnJEfbbP2aHDkH/iitYSIustNyZKap3nu31JXLLpvGFt2upoLkniVOzLeRmIDQwLv5cYbVOLS+lCguYCzZq3xnJDDWeSBXhmqJq5PVHg8zaeM6USvQkl1s0QZQYbmcAQXTidwTEqBRraOqJ65NZ3TkrFgCteUGlDS3qTsyjI+TDbucGLN8aBRoucXb+QX4k1M8o4+LuRSlk50kXNitdig2i2RZEx0WUUPG9uZcYjQrBz8tLOwgL1Z0sz91g/i4r8UzFndCtJsNS97MpVWrHzCBQIfCOLIYlmjOQGjLuFPZbV7S45oQjV2+JQNZcrNptLLjwbwWWLV29STj61lIXKZJ0AEqlWJ+KOZMJS1yWh8ZgrYfhs0mxghzRuVD0asvi4sOzp3PJePQNxmOxbAFlznyQmLkXJyO6WUh6XSy43fHptvo1GCA2WA4JpZUGWrmqmOGNvANs+lckQcz1A25RstNe9meaMW0t5RuBbKQH0+7cENIW2URSVxJdJ2l7StOkn3WO652ijqt6MOUcxQtVBnTT7MZPbfIxkhX5YrhMmG7223J8qgOx5MJhbbGIdlgAsriZzeEIXA09dnMlKwY23QHwBjaxpI6SQ0JbLhltaxRg1PIe1u+EDjslKVdzXJndZU25vHEKum6tViWMlfnYLLSJjB+dw4VmuKqUYfr4kJSyqZjxWzYnrE1WAdOmlJb92DS8ZldXkIw31FM2U49LJ8oJK4I41qYpWuZH6EbpQ52Iy1F+fPmcum0ygCks5jJI7LeCZ2bZuJxvpm7+tmjh86WStOmBVKXRzN2PXGyE8nzxiA1m0N3cEc+xg2HmVm5Fgray4l0E3qGZxjLzWENX8XL6Wl3HGXWjpXy6Xl6XI7o3dLM9W1aNHhE7FDWkPCqkiosJ/SJzzAyYYinPb5n3X1C73FmsGQDKqMltbjM1/xiRpGmlFND0UpgKp8mM+fMFhixxLBEJrOlup41Or8D2vJYRduFvpyvMGekAlvax+OUOhTZwVi682hnVbQ/lLVTu83WArzSZX06ccfRbMvIkjzdzeHxnichdhibYtMplECaE2J4TPnEdLBJvtpSoeeJx224qPZRtkgNaukOD9iSTltLSLQ27tDV5uSi58jWAbbmPEXeusRsMQbKFKzqGRD2rehG+Hwtkj7vzdr2CIJ5RousiB5bryTzwYgn8DUh0AM/TI4lR+vSGEWrmqR0czifiqwsRSxAxxP6OGpHdVePqHKMKqNBgrpJ1wR6N+6cKp9Uk3BBHaZ8YUerfM0dyFqmBuvlfDf1vWGXDMt6ohip6J/RYJZM2kMQirt2PF+BhlgmymhVBzhJscE4FEnykhwab7d2JomrylpSkGdmXamWvmRDzHGhS5e+ykmMNF8e3cNYnFVDJ3N34ZZ2yGy35N3APkimMspw5SS7PMoQ4qpijsNxfXYsHD0qZ3rA2taOHvu5XWm7lGBPaG2NRF2ZsiFr2g3p55PR8hBWLbuZ7jg11Q/cTk8uB0KqgnCsZQtpPeGXwB5i6CqkR8OQMDKT307nrFnu6GMgm5ftsr7MNIrOg5HbGtPJUhqymLvqhGpVn+z5mSJIEsdNMVB4b73Aji0bbmDM4C0fLNtofsY0Cju0OT8Yy1yAN6m92SldoCbLJj5f1ADdFItmFE6lozRxL9n04B+lRWCpQ9Mf822z6NxmhEGQistYGsqDbK6Ions8epzQSK6qYENMX/CjZjfZg/PeTxLyxJXcjm238Vpby043JLZxV0DUt/FmwnZCoLlBORwvOzyOhkQws6Jg161AKHumHlKLzWkllXOd4MxZ1W09Y3zgopntatTWKrakyOw5OzZFQaAtMVJVHFVHamNe6hrTGEq0L8XFwUszFSs5yYejtYcK+Eouz4YrqWfylF72bLoC7LTAq6EYJWLZwtoTqnJoox61a4j6zAEhPAtRIg/cWXOwBoY2Y86zJa1e+MtiuZBiR1VorliY1ml2LLEghfUvMOoVy2eT+d7Y+5iKm5bTRt2eaAQpdCNTCtZlxLun6fpIXMiS2Y0qVvK3VYZpS0/PcdyRTEYckWASJEm3C1pj1uYbfJjzs3mrMltcrGdCU5G0OduSRBbscItZC01BTtMZbk42jrefzf1GJWKLkI3LqHLFhetO7BMmxbLmEAR1UJsTJ/vVQTO18WIRjPdOy5cB0+rkTlvhIxLPJ7sVPNI2RmNnLWhyi90uTpFvq9ZKUhfxAN4vKjK2Mo/cD/0uw/bzg2ccJ34gzYbbvKOx1iY2OocdjiAM9v4YddhuuloCpWaDnc5Wy9FEnzRnTDR1Tl+vzg3ZTWuGScg5SlaCPpxhKKcZ9GgdzpNoavCMFUxGTXxA6fXccU+sMfKKwJ6Tx8GEA2FTWJVJb021EaI9RswnU8LOUPV0IvA0wZr1lFzushUe7ECwKa3FPFq5zXASqqWGdhvF9TYoQzPr1nC97dnd8l2h58bsEGcoRZ2DOJL3ZMDX6wkTpi5FRd1AquY5GdWXdmZjkSbGi4rjVGZ/VFsBg7c0x4WxmVUSIRN0OB3m7CFP9yeqTvcLIlnKxXZsKLWwP2rGSjRUZdEwCisWXj0ZMnF7FqarPOEK2heXpanzsVWoiR9ssWjCow43wKkLnU+m0sZx2QPMITvl5JjlRY0zzy3M2kBtgAuvvX6NYvRsd46dqminJ3UhLnKsCkZyu9XD6LTVRqQiqIfh4hLNRwF3sRRzd9aa5YgPGrHJ61C0ljQZChSzEu12g6VxauGstZujW9bn12BxIR233tDnPHIHzAFDs1bD5zB91MX4iKeRI+IFTml2B/tdXIzILChpdRTi/J4eL+oodxh+NZy3G3MbpUYCz+fF0c7Upe8sOHkp57HDOCR/3POX7bkeELTkAJqpt4GwKrAJAerWbZzpppouCO6sMO7ZOJAiXV44bT04OmVlbO02J6kSl45OPMwxesXKjMsuxUtC1LRuYPmRY33f5ehSXlhaOefW3NJOFtOSQ0fygA8JNiV0bWCvN9Fs4FvtOm5ldV64mcFd9pakdo4+U91OOHeDc8VNYFlRnVgqyCOPndqBMHUYc01c3E23A4lQ6MI0sVdneVAVu8G6unQjhjM3whAld7Egb1dF7AlWqnjBcLiZpEy0ioK9y+3g4XRUANlc1N3RZFzBmXZKG8hbGMfiUg/50368JIwlOUq3u4kWKRwhAq3hORVWsvzs2ZpXeIa1NdC5rm5JdM8PhBo47mriwvzmKZKcjI1cK7CVuJ/mA7rKlJAFaSmVce54l91A2BcZthaGjL6pTVsJFAVqlHLSIaiD1JFjMZJNeeF1m25zolGPLFPN9YHZzmeDleaey/BsjYzp6axfQCWY6+7ID+fbUq4c37hQlRIOkhWqLHDZWOq6IA3VVSiHKL8L/ZarT3XNx4SvLibrhVc4F3eg0uNk1CjNcT3AxjFI2FTUhUVXHHHFiAN22GjwKt8tx2PlgCmaXsg1d9JH+9EA1daBvBsTkpfiIY3nLaXNKGulYJNUOQoiOs0NyUW7ZbGbWoPxjFm1s419HkaLnTDPWTBy+Pgs0nvYLKET29LGurFuEi9o9SlrbUaksA1yuxFONirW9aKTsPTE7BaE6qkUlsOObuUEw4JpOlvbCr42d/lRmDhlqy0tsiSaOKnjyRhzS3mlMMdsTtVltz/pazdENWdgFRviNJL2iutHbH0xsO1StlZCgsLsnjL2zsHH5iigpyYsUKjZjFfYSmn9ehAe7HhbUdONE7CLJZOVpLIMtEGnz5yjx0y29aXayFpMHLR9hxrBkh/UYZdmY/fszhaEzOTdQewYlmwiau0xq4DWl9mBnOml5Y2X+MzH/VYQoOh2Uqczx2JtUyxKL66tWtPFCOxRXGdEoozD+bKakR44UoC3x6E+np5PbWdiTFXDM75xK8NXbJyQQZZhCo+nK7aA+pbCuhqThhf75vmk8LA5Y8y5x2okG6bdVie2nHsWBRbd7PelEilyrSuBj41Te9pQYoKFYjUrfT6oLEkrBRM9ylhsLuc5lmJsDXid4RVSb2qVISx5tNwwvjoPl5JTEjnYmHakNB6wwGTZnrWuNQ8LfqE3AVZeapRdC7EckgllLyvWLqk65sbUcITlNRM16GDihId4C+qZixPYWGq8WT0I0AkxOu2nwlgi/PkgWSd4PWIyZbRwBFGblnh7YqenXPbtc2XAqhtwld0MMNhRrp2QW9cSw26begxYPBeNI6lJTaWcgs3O8gtBai2OltITy7AdgS7FlBxx/nw6njJByrLsHw+PD/008D40+810+Tri+r8a99ymNmkNZSYu6CdZvcznq6zn3ynw8fEhd0Mo/jarKqIquI+CbpOq97eN78uXeV9xuc1g0+Q2absNB0s76P+f193QfpR3/TtEP9O6jRzh03fjyH4C6Pv9H3R6Da4D/+vsDGoB9fjyP+o2zkjcJgAA -->
