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
