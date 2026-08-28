---
name: "rappstore-rapp-store-novell"
description: "Adversarial pre-review. Twelve skeptic lenses roast your artifact and tell you the evidence that kills each objection. Archetype only \u2014 models no real person, stores no names."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp-store/novell", "rar_sha256": "3c49a6cb033ecdc343190e57d36476840b11af4eb7500eb5638df5f9d5fccf91", "source_kind": "federated-rapplication", "source_commit": null, "tags": ["rapplication", "review", "adversarial", "local-first", "has-ui"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@rapp-store/novell`. The original RAPP
agent is preserved byte-for-byte in `novell_agent.py` and in the RCI capsule.

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

Novell — the hater you run before the real one shows up.

Novell is an adversarial pre-review rapplication. You hand him an artifact
(a pitch, a README, an architecture claim, a demo script) and he returns the
objections a hostile-but-competent skeptic would raise — ranked, quotable,
and each paired with the specific evidence that kills it.

He is not a person
------------------
Novell is an ARCHETYPE, not a portrait. He is assembled from twelve reusable
*stances* — the objection patterns that recur in every enterprise-AI review,
regardless of who is sitting in the chair. He ingests no transcripts, models
no individual, and stores no names. That is a hard design constraint, not a
disclaimer: `_scrub()` strips person-shaped tokens from every custom lens
before it is ever persisted, so a user cannot accidentally turn their own
copy of Novell into a caricature of a colleague. See `PII_POLICY`.

Named for Novell, Inc. — the company that owned the network and still lost
the shift. The archetype's whole personality is "I have seen this before and
I was right last time." Sometimes he still is. That's the point.

He attacks artifacts, never people
----------------------------------
Every barb in the catalog is aimed at a claim. None is aimed at a human.
The `defend` action exists because the goal is a stronger artifact, not a
funnier insult.

Local-first
-----------
The heuristic path (`gate`, `score`, and the objection ranking inside `roast`)
is pure Python — no network, no key, no LLM. It works on a plane. If the host
brainstem provides `utils.llm.call_llm`, `roast` additionally renders the
objections as prose in Novell's voice; without it you get the structured
findings and the deterministic verdict, which is the part a pipeline needs.

Pipeline use
------------
    novell(action="gate", artifact=open("PITCH.md").read(), threshold=40)

`gate` returns `{"ok": ..., "verdict": "PASS"|"FAIL", "exit_code": 0|1, ...}`
so it drops straight into CI as a pre-review check: fix what Novell finds
before the real reviewer ever sees it.

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `novell_agent.py` and embedded as the fenced Python below (sha256 3c49a6cb033ecdc3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `novell_agent.py` first:

```bash
python3 novell_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 novell_agent.py   # or on stdin
python3 novell_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""Novell — the hater you run before the real one shows up.

Novell is an adversarial pre-review rapplication. You hand him an artifact
(a pitch, a README, an architecture claim, a demo script) and he returns the
objections a hostile-but-competent skeptic would raise — ranked, quotable,
and each paired with the specific evidence that kills it.

He is not a person
------------------
Novell is an ARCHETYPE, not a portrait. He is assembled from twelve reusable
*stances* — the objection patterns that recur in every enterprise-AI review,
regardless of who is sitting in the chair. He ingests no transcripts, models
no individual, and stores no names. That is a hard design constraint, not a
disclaimer: `_scrub()` strips person-shaped tokens from every custom lens
before it is ever persisted, so a user cannot accidentally turn their own
copy of Novell into a caricature of a colleague. See `PII_POLICY`.

Named for Novell, Inc. — the company that owned the network and still lost
the shift. The archetype's whole personality is "I have seen this before and
I was right last time." Sometimes he still is. That's the point.

He attacks artifacts, never people
----------------------------------
Every barb in the catalog is aimed at a claim. None is aimed at a human.
The `defend` action exists because the goal is a stronger artifact, not a
funnier insult.

Local-first
-----------
The heuristic path (`gate`, `score`, and the objection ranking inside `roast`)
is pure Python — no network, no key, no LLM. It works on a plane. If the host
brainstem provides `utils.llm.call_llm`, `roast` additionally renders the
objections as prose in Novell's voice; without it you get the structured
findings and the deterministic verdict, which is the part a pipeline needs.

Pipeline use
------------
    novell(action="gate", artifact=open("PITCH.md").read(), threshold=40)

`gate` returns `{"ok": ..., "verdict": "PASS"|"FAIL", "exit_code": 0|1, ...}`
so it drops straight into CI as a pre-review check: fix what Novell finds
before the real reviewer ever sees it.
"""

from __future__ import annotations

import json
import re
import uuid
from datetime import datetime, timezone
from typing import Any

try:
    from agents.basic_agent import BasicAgent
except ImportError:  # pragma: no cover - host-dependent import path
    from basic_agent import BasicAgent


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "id": "novell",
    "name": "Novell",
    "version": "1.0.0",
    "publisher": "@kody-w",
    "description": (
        "Adversarial pre-review. Twelve skeptic lenses roast your artifact "
        "and tell you the evidence that kills each objection. Archetype "
        "only — models no real person, stores no names."
    ),
    "summary": "The hater you run before the real one shows up.",
    "category": "analysis",
    "tags": ["rapplication", "review", "adversarial", "local-first", "has-ui"],
    "agent": "singleton/novell_agent.py",
    "ui": "ui/index.html",
}


PII_POLICY = (
    "Novell is an archetype. He ingests no transcripts and models no "
    "individual. Custom lenses are scrubbed of email addresses, @handles, "
    "phone numbers, URLs and capitalised name-pairs before persistence. "
    "If you want a critic modelled on a specific person, this is not that "
    "tool, on purpose."
)


# ── The lens catalogue ──────────────────────────────────────────────────────
# Each lens is one recurring objection. Fields:
#   id        stable slug
#   name      the stance, as Novell would title it
#   barb      the quotable one-liner (aimed at the claim, never the author)
#   asks      the legitimate question hiding inside the barb
#   killed_by what evidence actually closes it
#   weight    severity contribution to the Novell score (0-100 total scale)
#   answered  regexes that, if present in the artifact, mean you already
#             addressed this lens — the deterministic offline signal
#   provoked  optional regexes that make the lens land HARDER when present

LENSES: list[dict[str, Any]] = [
    {
        "id": "not_ga",
        "name": "The GA Gate",
        "barb": "Cool. Is it GA? Because I can't put a preview on a customer's roadmap.",
        "asks": "Is this generally available and supported, or is it a prototype "
                "wearing product clothes?",
        "killed_by": "A GA/roadmap citation — or an explicit 'this is a prototype "
                     "accelerator, not a shipped product' framing that doesn't pretend "
                     "otherwise. Either is fine. Ambiguity is not.",
        "weight": 10,
        "answered": [r"\bgenerally available\b", r"\bGA\b", r"\broadmap\b",
                     r"\bprototype\b", r"\bpreview\b", r"\bnot a product\b",
                     r"\bunsupported\b"],
        "provoked": [r"\bproduction[- ]ready\b", r"\benterprise[- ]grade\b"],
    },
    {
        "id": "body_parts",
        "name": "Body Parts",
        "barb": "You've stitched five things together and called it a platform. I count five things.",
        "asks": "Is this one coherent product, or an integration diagram in a trenchcoat?",
        "killed_by": "One install command, one artifact, one failure domain — "
                     "demonstrated on a machine that didn't build it.",
        "weight": 9,
        "answered": [r"\bsingle[- ]file\b", r"\bone command\b", r"\bone-liner\b",
                     r"\binstaller\b", r"\bself-contained\b", r"\bclean machine\b",
                     r"\bcurl .*\| *(bash|sh)\b"],
        "provoked": [r"\bglue\b", r"\bintegrat(e|ion|es) (with|between)\b.*\band\b.*\band\b"],
    },
    {
        "id": "who_pays",
        "name": "The Meter",
        "barb": "Who's the billed party? Show me the meter or it's shelfware.",
        "asks": "What consumes budget, whose budget is it, and does it land on an "
                "invoice somebody already signed?",
        "killed_by": "A named existing entitlement it rides on, with the consumption "
                     "path stated plainly. 'It's free' is not an answer; it's an "
                     "unexamined cost.",
        "weight": 9,
        "answered": [r"\bmeter\b", r"\bbilling\b", r"\bentitlement\b", r"\bseat\b",
                     r"\blicen[cs]e\b", r"\bconsum(es|ption)\b", r"\bcost\b",
                     r"\bexisting subscription\b"],
        "provoked": [r"\bfree\b", r"\bno cost\b", r"\bzero (cost|spend)\b"],
    },
    {
        "id": "already_exists",
        "name": "The Roadmap Eraser",
        "barb": "The platform ships this in two quarters. You've built a wrapper with an expiry date.",
        "asks": "What survives when the platform absorbs this capability?",
        "killed_by": "Naming the layer you own that the platform is structurally "
                     "not going to build — or accepting the expiry date openly and "
                     "pricing the work accordingly.",
        "weight": 8,
        "answered": [r"\bcomplement", r"\brides on\b", r"\bupstream\b",
                     r"\bwhen .{0,20}ships\b", r"\bdifferentiat", r"\bthe layer we own\b",
                     r"\bdeprecat"],
        "provoked": [r"\bfirst\b.*\bever\b", r"\bnobody else\b", r"\bunique\b"],
    },
    {
        "id": "wont_scale",
        "name": "Laptop Physics",
        "barb": "Beautiful on your laptop. Now do 5,000 seats and tell me about tenant isolation.",
        "asks": "What breaks between one user and n users?",
        "killed_by": "A run at real n with numbers — or an honestly stated ceiling. "
                     "A stated limit is credible; an unstated one is a landmine.",
        "weight": 8,
        "answered": [r"\bscal(e|es|ing|ability)\b", r"\btenan(t|cy)\b", r"\bconcurren",
                     r"\bload test", r"\b\d{3,}\s*(users|seats|requests)\b",
                     r"\bisolat(ion|ed)\b", r"\blimits?\b"],
        "provoked": [r"\bworks on my (machine|laptop)\b", r"\blocally\b"],
    },
    {
        "id": "no_support",
        "name": "The 2AM Question",
        "barb": "It breaks at 2am on a Sunday. Who gets paged? Because it isn't me.",
        "asks": "Who owns the pager, what's the SLA, and what's the rollback?",
        "killed_by": "A named owner plus a rollback path — or an 'unsupported, use "
                     "at your own risk' label nobody could miss.",
        "weight": 8,
        "answered": [r"\bSLA\b", r"\bon[- ]call\b", r"\bpager\b", r"\brollback\b",
                     r"\bsupport\b", r"\bowner\b", r"\bmaintainer\b",
                     r"\bat your own risk\b", r"\brevert\b"],
        "provoked": [],
    },
    {
        "id": "compliance",
        "name": "The Auditor",
        "barb": "Where does the data sit, who can read it, and what does the audit log say?",
        "asks": "Residency, DLP, retention, audit trail.",
        "killed_by": "A data-flow description naming every hop — and, more "
                     "persuasively, naming what is never transmitted at all.",
        "weight": 9,
        "answered": [r"\bresidency\b", r"\bDLP\b", r"\baudit\b", r"\bretention\b",
                     r"\bencrypt", r"\bnever leaves\b", r"\blocal[- ]first\b",
                     r"\bon[- ]prem", r"\bcompliance\b", r"\bGDPR\b", r"\bPII\b"],
        "provoked": [r"\bupload", r"\bcloud\b", r"\bsend(s|ing)? .{0,20}to (our|the) (server|api)\b"],
    },
    {
        "id": "just_a_demo",
        "name": "Demo Gravity",
        "barb": "Great demo. Name one production user.",
        "asks": "Has anyone run this in anger, for longer than a meeting?",
        "killed_by": "One production instance with a duration and a number. "
                     "Anonymised is fine — 'a national retailer, 11 weeks, 40 seats' "
                     "beats a logo you can't cite.",
        "weight": 9,
        "answered": [r"\bin production\b", r"\bproduction (user|instance|deployment)\b",
                     r"\b\d+\s*(weeks|months)\b", r"\blive since\b", r"\bcustomers? (are|is) using\b",
                     r"\bdeployed\b"],
        "provoked": [r"\bdemo\b", r"\bproof of concept\b", r"\bPoC\b", r"\bimagine\b"],
    },
    {
        "id": "lock_in",
        "name": "Bus Factor One",
        "barb": "One maintainer, one proprietary format. What happens when you're on vacation?",
        "asks": "Can somebody else operate, fork, and exit this?",
        "killed_by": "A published spec, an independent implementation, and a "
                     "documented export path. Two of three is arguable. Zero is fatal.",
        "weight": 7,
        "answered": [r"\bspec(ification)?\b", r"\bopen[- ]source\b", r"\bAPACHE\b",
                     r"\bMIT\b", r"\bexport\b", r"\bfork\b", r"\bconformance\b",
                     r"\bindependent implementation\b", r"\binteroperab"],
        "provoked": [r"\bproprietary\b", r"\bour format\b"],
    },
    {
        "id": "so_what",
        "name": "The So-What",
        "barb": "Okay. What number moved?",
        "asks": "Which business metric changed, by how much, measured how?",
        "killed_by": "A before/after with a unit and a timeframe. One real number "
                     "outranks a page of adjectives.",
        "weight": 10,
        "answered": [r"\b\d+\s*%", r"\bfrom \d+ to \d+\b", r"\breduced\b.*\b\d+",
                     r"\bsaved\b.*\b\d+", r"\bbaseline\b", r"\bmeasured\b",
                     r"\b\d+\s*(hours|days|minutes)\b"],
        "provoked": [r"\btransformative\b", r"\bgame[- ]chang", r"\brevolutionary\b",
                     r"\bunlock(s|ing)?\b"],
    },
    {
        "id": "novelty_tax",
        "name": "Novelty Tax",
        "barb": "You invented five nouns. Now I have to teach my team five nouns. Why?",
        "asks": "Does the new vocabulary earn the cost of learning it?",
        "killed_by": "Each coined term names a thing that genuinely had no name — "
                     "plus a glossary short enough to read in one sitting.",
        "weight": 6,
        "answered": [r"\bglossary\b", r"\bterminology\b", r"\bdefinitions?\b",
                     r"\bin other words\b", r"\bi\.e\.", r"\bwhich means\b"],
        "provoked": [],
    },
    {
        "id": "blast_radius",
        "name": "Attack Surface",
        "barb": "You gave an agent hands. What's the blast radius when it's wrong?",
        "asks": "What is the capability boundary, how scoped are the credentials, "
                "and where is the human in the loop?",
        "killed_by": "An enumerated capability boundary — specifically, the list of "
                     "things it structurally cannot do, not the list of things it "
                     "promises not to.",
        "weight": 9,
        "answered": [r"\bcapability boundar", r"\bleast privilege\b", r"\bscoped\b",
                     r"\bhuman[- ]in[- ]the[- ]loop\b", r"\bapproval\b", r"\bsandbox",
                     r"\bread[- ]only\b", r"\bcannot\b", r"\bpermission"],
        "provoked": [r"\bautonomous\b", r"\bagentic\b", r"\bself[- ]heal",
                     r"\bfull access\b"],
    },
]

_TOTAL_WEIGHT = sum(lens["weight"] for lens in LENSES)


def _active(customs: list[dict[str, Any]] | None = None
            ) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]]]:
    """The catalogue for THIS call: shipped lenses plus the caller's customs.

    Deliberately builds a fresh list rather than mutating `LENSES`. The module
    is imported once and shared by every request a brainstem serves, so a
    global mutation would leak one workspace's custom lenses into everybody
    else's scores — and silently change a gate verdict.
    """
    merged = list(LENSES)
    seen = {lens["id"] for lens in merged}
    for lens in customs or []:
        if lens.get("id") and lens["id"] not in seen:
            merged.append(lens)
            seen.add(lens["id"])
    return merged, {lens["id"]: lens for lens in merged}


# ── PII scrubbing (the constraint that makes Novell shippable) ──────────────

_EMAIL_RE = re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.]+\b")
_HANDLE_RE = re.compile(r"(?<![\w/])@[A-Za-z][\w-]{2,}")
_PHONE_RE = re.compile(r"\+?\d[\d\s().-]{7,}\d")
_URL_RE = re.compile(r"https?://\S+")
# Greedy: match a RUN of 2+ capitalised words, not just a pair. A pair-only
# regex eats "Dorian Ashgrove" out of "Dorian Ashgrove Vex" and orphans the surname.
_NAMEPAIR_RE = re.compile(r"\b[A-Z][a-z]{1,15}(?:\s+[A-Z][a-z]{1,15})+\b")
# A capitalised word left stranded beside a redaction marker is almost always
# the tail of a name the run-regex couldn't reach. Swept to a fixed point.
_ORPHAN_RE = re.compile(r"\[name redacted\](\s+[A-Z][a-z]{1,15})+")

# Capitalised pairs that are obviously not people.
_NAMEPAIR_ALLOW = {
    "General Availability", "Attack Surface", "Body Parts", "Bus Factor",
    "Demo Gravity", "Laptop Physics", "Novelty Tax", "Machine Learning",
    "Data Loss", "Service Level", "Single Sign", "Open Source", "United States",
}


def _scrub(text: str) -> tuple[str, list[str]]:
    """Strip person-shaped tokens. Returns (clean_text, what_was_removed)."""
    removed: list[str] = []

    def _kill(pattern: re.Pattern[str], label: str, replacement: str, s: str) -> str:
        def sub(m: re.Match[str]) -> str:
            if label == "name" and m.group(0) in _NAMEPAIR_ALLOW:
                return m.group(0)
            removed.append(label)
            return replacement
        return pattern.sub(sub, s)

    out = text or ""
    out = _kill(_EMAIL_RE, "email", "[email redacted]", out)
    out = _kill(_URL_RE, "url", "[url redacted]", out)
    out = _kill(_HANDLE_RE, "handle", "[handle redacted]", out)
    out = _kill(_PHONE_RE, "phone", "[phone redacted]", out)
    out = _kill(_NAMEPAIR_RE, "name", "[name redacted]", out)
    # Sweep orphaned name tails to a fixed point (bounded — each pass strictly
    # shortens the string, so this terminates).
    for _ in range(8):
        swept = _ORPHAN_RE.sub("[name redacted]", out)
        if swept == out:
            break
        removed.append("name")
        out = swept
    return out, sorted(set(removed))


# ── Heuristic engine (offline, deterministic) ───────────────────────────────

def _hits(patterns: list[str], text: str) -> list[str]:
    found = []
    for p in patterns:
        if re.search(p, text, re.IGNORECASE):
            found.append(p)
    return found


def _evaluate(artifact: str, lens_ids: list[str] | None,
              catalogue: list[dict[str, Any]],
              by_id: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """Score every lens against the artifact. Lands = objection is unanswered."""
    text = artifact or ""
    selected = lens_ids or [lens["id"] for lens in catalogue]
    findings = []
    for lid in selected:
        lens = by_id.get(lid)
        if not lens:
            continue
        answered = _hits(lens["answered"], text)
        provoked = _hits(lens.get("provoked", []), text)
        lands = not answered
        # An unanswered lens that is also actively provoked hits harder.
        severity = lens["weight"]
        if lands and provoked:
            severity = min(100, int(round(severity * 1.5)))
        findings.append({
            "id": lens["id"],
            "name": lens["name"],
            "barb": lens["barb"],
            "asks": lens["asks"],
            "killed_by": lens["killed_by"],
            "lands": lands,
            "severity": severity if lands else 0,
            "weight": lens["weight"],
            "answered_by_signals": answered,
            "provoked_by_signals": provoked,
        })
    findings.sort(key=lambda f: (-f["severity"], f["id"]))
    return findings


def _score(findings: list[dict[str, Any]]) -> dict[str, Any]:
    landed = [f for f in findings if f["lands"]]
    possible = sum(f["weight"] for f in findings) or 1
    raw = sum(f["severity"] for f in landed)
    # `severity` can exceed `weight` (the 1.5x provoked multiplier), so the raw
    # total can overshoot the weight budget. The score is a 0-100 scale by
    # definition — clamp rather than report 137/100.
    pct = min(100, int(round(100 * raw / possible)))
    return {
        "novell_score": pct,
        "landed": len(landed),
        "evaluated": len(findings),
        "raw": raw,
        "possible": possible,
        "reading": _reading(pct),
    }


def _reading(pct: int) -> str:
    if pct >= 75:
        return "He hasn't stopped talking. Nothing here is defended."
    if pct >= 50:
        return "He's enjoying himself. Half your claims are undefended."
    if pct >= 25:
        return "He got a few in. Fixable before anyone else reads this."
    if pct > 0:
        return "He's bored. One or two loose threads."
    return "He has nothing. Suspicious — check you gave him a real artifact."


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _render(findings: list[dict[str, Any]], score: dict[str, Any]) -> str:
    landed = [f for f in findings if f["lands"]]
    if not landed:
        return (f"NOVELL SCORE {score['novell_score']}/100 — {score['reading']}\n"
                "\nNo objection landed. Every lens found its counter-evidence.")
    lines = [f"NOVELL SCORE {score['novell_score']}/100 — {score['reading']}",
             f"{len(landed)} of {score['evaluated']} lenses landed.", ""]
    for f in landed:
        lines.append(f"[{f['severity']:>2}] {f['name']}")
        lines.append(f'     "{f["barb"]}"')
        lines.append(f"     He's really asking: {f['asks']}")
        lines.append(f"     Kill it with: {f['killed_by']}")
        lines.append("")
    return "\n".join(lines).rstrip()


# ── Optional LLM voice layer ────────────────────────────────────────────────

def _call_llm(prompt: str) -> str | None:
    """Best-effort prose in Novell's voice. Never required."""
    try:
        from utils.llm import call_llm  # type: ignore
    except Exception:
        return None
    try:
        return call_llm(prompt)
    except Exception:
        return None


_VOICE = (
    "You are Novell: a senior, tired, technically competent skeptic reviewing "
    "an artifact. You are dry, brief and condescending about CLAIMS. You never "
    "insult the author, never speculate about any person, and never reference "
    "anyone's identity. You attack the argument only. Two sentences per "
    "objection, maximum. No preamble."
)


# ── State (custom lenses) ───────────────────────────────────────────────────

_FALLBACK_STORE: list[dict[str, Any]] = []


def _load_custom(context: dict | None) -> list[dict[str, Any]]:
    if context and callable(context.get("workspace_read")):
        try:
            raw = context["workspace_read"]("custom_lenses.json")
            if raw:
                data = json.loads(raw)
                if isinstance(data, list):
                    return data
        except (json.JSONDecodeError, OSError, RuntimeError):
            pass
    return list(_FALLBACK_STORE)


def _save_custom(lenses: list[dict[str, Any]], context: dict | None) -> None:
    global _FALLBACK_STORE
    if context and callable(context.get("workspace_write")):
        try:
            context["workspace_write"]("custom_lenses.json",
                                       json.dumps(lenses, indent=2))
            return
        except (OSError, RuntimeError):
            pass
    _FALLBACK_STORE = lenses


# ── Actions ─────────────────────────────────────────────────────────────────

def _do_lenses(catalogue: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "ok": True,
        "count": len(catalogue),
        "total_weight": _TOTAL_WEIGHT,
        "pii_policy": PII_POLICY,
        "lenses": [{k: lens[k] for k in ("id", "name", "barb", "asks",
                                         "killed_by", "weight") if k in lens}
                   for lens in catalogue],
    }


def _do_roast(artifact: str, lens_ids: list[str] | None, use_llm: bool,
              catalogue: list[dict[str, Any]],
              by_id: dict[str, dict[str, Any]]) -> dict[str, Any]:
    if not (artifact or "").strip():
        return {"ok": False, "error": "artifact is required and non-empty"}
    findings = _evaluate(artifact, lens_ids, catalogue, by_id)
    score = _score(findings)
    result: dict[str, Any] = {
        "ok": True,
        "ts": _now_iso(),
        "findings": findings,
        **score,
        "rendered": _render(findings, score),
        "voice": None,
    }
    landed = [f for f in findings if f["lands"]]
    if use_llm and landed:
        bullets = "\n".join(f"- {f['name']}: {f['asks']}" for f in landed[:6])
        prose = _call_llm(
            f"{_VOICE}\n\nThe artifact under review:\n---\n{artifact[:6000]}\n---\n"
            f"These objections are unanswered by the text:\n{bullets}\n\n"
            "Voice each one. Format each as a single dash-prefixed line."
        )
        if prose:
            result["voice"] = prose.strip()
    return result


def _do_defend(objection_id: str, evidence: str,
               by_id: dict[str, dict[str, Any]]) -> dict[str, Any]:
    lens = by_id.get(objection_id)
    if not lens:
        return {"ok": False, "error": f"unknown lens id: {objection_id!r}",
                "known": sorted(by_id)}
    ev = (evidence or "").strip()
    if not ev:
        return {"ok": False, "error": "evidence is required — describe what you "
                                      "actually have, not what you intend to have"}
    answered = _hits(lens["answered"], ev)
    holds = bool(answered)
    return {
        "ok": True,
        "lens": lens["id"],
        "name": lens["name"],
        "killed_by": lens["killed_by"],
        "evidence_holds": holds,
        "matched_signals": answered,
        "verdict": ("That closes it. Put this sentence in the artifact itself — "
                    "Novell only reads what's written down."
                    if holds else
                    "Doesn't close it. He'll re-ask. What he needs: "
                    + lens["killed_by"]),
    }


def _do_gate(artifact: str, threshold: int, lens_ids: list[str] | None,
             catalogue: list[dict[str, Any]],
             by_id: dict[str, dict[str, Any]]) -> dict[str, Any]:
    if not (artifact or "").strip():
        return {"ok": False, "error": "artifact is required and non-empty"}
    findings = _evaluate(artifact, lens_ids, catalogue, by_id)
    score = _score(findings)
    passed = score["novell_score"] <= threshold
    blockers = [{"id": f["id"], "name": f["name"], "severity": f["severity"],
                 "fix": f["killed_by"]}
                for f in findings if f["lands"]][:5]
    return {
        "ok": True,
        "verdict": "PASS" if passed else "FAIL",
        "exit_code": 0 if passed else 1,
        "threshold": threshold,
        **score,
        "top_blockers": blockers,
        "summary": (f"Novell score {score['novell_score']} vs threshold "
                    f"{threshold} — {'PASS' if passed else 'FAIL'}. "
                    f"{score['landed']} objection(s) unanswered."),
    }


def _do_add_lens(customs: list[dict[str, Any]], lens_id: str, name: str,
                 barb: str, asks: str, killed_by: str, weight: int,
                 by_id: dict[str, dict[str, Any]]) -> dict[str, Any]:
    lens_id = (lens_id or "").strip().lower().replace(" ", "_")
    if not re.match(r"^[a-z][a-z0-9_]*$", lens_id or ""):
        return {"ok": False, "error": "id must be snake_case: ^[a-z][a-z0-9_]*$"}
    if lens_id in by_id:
        return {"ok": False, "error": f"lens {lens_id!r} already exists"}
    if not (barb or "").strip():
        return {"ok": False, "error": "barb is required"}

    scrubbed_fields = {}
    removed_all: list[str] = []
    for key, val in (("name", name), ("barb", barb), ("asks", asks),
                     ("killed_by", killed_by)):
        clean, removed = _scrub(val or "")
        scrubbed_fields[key] = clean
        removed_all.extend(removed)

    lens = {
        "id": lens_id,
        "name": scrubbed_fields["name"] or lens_id,
        "barb": scrubbed_fields["barb"],
        "asks": scrubbed_fields["asks"] or "(unstated)",
        "killed_by": scrubbed_fields["killed_by"] or "(unstated)",
        "weight": max(1, min(int(weight or 5), 20)),
        "answered": [],
        "provoked": [],
        "custom": True,
        "uid": str(uuid.uuid4()),
    }
    customs.append(lens)
    return {
        "ok": True,
        "lens": lens,
        "total_lenses": len(by_id) + 1,
        "redacted": sorted(set(removed_all)),
        "note": ("Person-shaped tokens were stripped before saving. " + PII_POLICY)
                if removed_all else PII_POLICY,
    }


def _do_export(customs: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "ok": True,
        "blob": json.dumps({"schema": "novell-lenses/1.0",
                            "exported_at": _now_iso(),
                            "lenses": customs}, indent=2),
        "count": len(customs),
    }


def _do_import(customs: list[dict[str, Any]], blob: str) -> dict[str, Any]:
    try:
        data = json.loads(blob or "")
    except json.JSONDecodeError as e:
        return {"ok": False, "error": f"blob is not valid JSON: {e}"}
    incoming = data.get("lenses") if isinstance(data, dict) else data
    if not isinstance(incoming, list):
        return {"ok": False, "error": "blob must contain a list of lenses"}
    known = {lens["id"] for lens in customs}
    added = 0
    redacted: list[str] = []
    for raw in incoming:
        if not isinstance(raw, dict) or not raw.get("id") or raw["id"] in known:
            continue
        clean_barb, r1 = _scrub(raw.get("barb") or "")
        clean_asks, r2 = _scrub(raw.get("asks") or "")
        clean_kb, r3 = _scrub(raw.get("killed_by") or "")
        clean_name, r4 = _scrub(raw.get("name") or raw["id"])
        redacted.extend(r1 + r2 + r3 + r4)
        if not clean_barb:
            continue
        lens = {"id": raw["id"], "name": clean_name, "barb": clean_barb,
                "asks": clean_asks or "(unstated)",
                "killed_by": clean_kb or "(unstated)",
                "weight": max(1, min(int(raw.get("weight") or 5), 20)),
                "answered": [], "provoked": [], "custom": True,
                "uid": raw.get("uid") or str(uuid.uuid4())}
        customs.append(lens)
        known.add(lens["id"])
        added += 1
    return {"ok": True, "added": added, "total": len(customs),
            "redacted": sorted(set(redacted))}


def run(context: dict | None = None, **kwargs: Any) -> str:
    """Entry point. Returns a JSON string; `rendered` holds the human view."""
    action = (kwargs.get("action") or "").strip()
    if not action:
        return json.dumps({"ok": False, "error": "action is required",
                           "actions": ["roast", "gate", "score", "lenses",
                                       "defend", "add_lens", "export",
                                       "import_json", "policy"]}, indent=2)

    customs = _load_custom(context)
    catalogue, by_id = _active(customs)

    artifact = kwargs.get("artifact") or kwargs.get("text") or ""
    lens_ids = kwargs.get("lenses") if isinstance(kwargs.get("lenses"), list) else None
    use_llm = bool(kwargs.get("voice", True))
    persistent = {"add_lens", "import_json"}

    if action == "roast":
        result = _do_roast(artifact, lens_ids, use_llm, catalogue, by_id)
    elif action == "gate":
        result = _do_gate(artifact, int(kwargs.get("threshold") or 25),
                          lens_ids, catalogue, by_id)
    elif action == "score":
        if not (artifact or "").strip():
            result = {"ok": False, "error": "artifact is required and non-empty"}
        else:
            findings = _evaluate(artifact, lens_ids, catalogue, by_id)
            result = {"ok": True, **_score(findings)}
    elif action == "lenses":
        result = _do_lenses(catalogue)
    elif action == "defend":
        result = _do_defend(kwargs.get("objection") or kwargs.get("lens") or "",
                            kwargs.get("evidence") or "", by_id)
    elif action == "add_lens":
        result = _do_add_lens(customs, kwargs.get("id") or "",
                              kwargs.get("name") or "", kwargs.get("barb") or "",
                              kwargs.get("asks") or "",
                              kwargs.get("killed_by") or "",
                              int(kwargs.get("weight") or 5), by_id)
    elif action == "export":
        result = _do_export(customs)
    elif action == "import_json":
        result = _do_import(customs, kwargs.get("blob") or "")
    elif action == "policy":
        result = {"ok": True, "pii_policy": PII_POLICY,
                  "archetype": True, "models_real_person": False}
    else:
        result = {"ok": False, "error": f"unknown action: {action!r}"}

    if result.get("ok") and action in persistent:
        _save_custom(customs, context)

    return json.dumps(result, indent=2)


AGENT = {
    "name": "Novell",
    "metadata": {
        "name": "Novell",
        "description": (
            "Adversarial pre-review. Runs twelve skeptic lenses over an "
            "artifact and returns the objections a hostile reviewer would "
            "raise, each paired with the evidence that kills it. Use `gate` "
            "in a pipeline to fail a draft before a human sees it. Novell is "
            "an archetype: he models no real person and stores no names."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "enum": ["roast", "gate", "score", "lenses", "defend",
                             "add_lens", "export", "import_json", "policy"],
                    "description": "The action to perform.",
                },
                "artifact": {
                    "type": "string",
                    "description": "The text under review (pitch, README, "
                                   "architecture claim, demo script).",
                },
                "lenses": {
                    "type": "array", "items": {"type": "string"},
                    "description": "Optional subset of lens ids to apply.",
                },
                "threshold": {
                    "type": "integer",
                    "description": "gate: max acceptable Novell score (default 25).",
                },
                "voice": {
                    "type": "boolean",
                    "description": "roast: render prose via the host LLM if "
                                   "available (default true). Findings are "
                                   "always returned regardless.",
                },
                "objection": {
                    "type": "string",
                    "description": "defend: the lens id you are answering.",
                },
                "evidence": {
                    "type": "string",
                    "description": "defend: the evidence you actually have.",
                },
                "id": {"type": "string", "description": "add_lens: snake_case id."},
                "name": {"type": "string", "description": "add_lens: display name."},
                "barb": {"type": "string", "description": "add_lens: the one-liner."},
                "asks": {"type": "string", "description": "add_lens: the real question."},
                "killed_by": {"type": "string",
                              "description": "add_lens: the evidence that closes it."},
                "weight": {"type": "integer",
                           "description": "add_lens: severity 1-20 (default 5)."},
                "blob": {"type": "string",
                         "description": "import_json: exported lens JSON."},
            },
            "required": ["action"],
        },
    },
}


class NovellAgent(BasicAgent):
    """BasicAgent wrapper for brainstem auto-discovery."""

    def __init__(self) -> None:
        super().__init__(name=AGENT["name"], metadata=AGENT["metadata"])

    def perform(self, **kwargs: Any) -> str:
        return run(kwargs.pop("_context", None), **kwargs)
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
