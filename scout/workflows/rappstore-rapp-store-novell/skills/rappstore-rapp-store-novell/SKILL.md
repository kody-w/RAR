---
name: "rappstore-rapp-store-novell"
description: "Adversarial pre-review. Twelve skeptic lenses roast your artifact and tell you the evidence that kills each objection. Archetype only \u2014 models no real person, stores no names."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp-store/novell", "rar_sha256": "3c49a6cb033ecdc343190e57d36476840b11af4eb7500eb5638df5f9d5fccf91", "source_kind": "federated-rapplication", "source_commit": null, "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "novell_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@rapp-store/novell:e19a5b124593405cad999a800e504baee7745ed8319e22691791281e1e8062f0", "kind": "skill"}, "tags": ["rapplication", "review", "adversarial", "local-first", "has-ui"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@rapp-store/novell`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `novell_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
