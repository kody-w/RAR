"""
Skill Toaster — turns an aggregated third-party skill entry into a real RAPP agent.

RAR indexes skills from other libraries. Indexing alone produces a bookmark: a
name, a blurb, a link. A bookmark is not an agent. It cannot be called, it takes
no parameters, and it returns nothing a brainstem can use.

This engine is the toaster. It reads the metadata RAR legitimately holds about an
upstream entry — kind, tags, description, platforms — infers the SHAPE of the
capability, and emits a working procedure for that shape, bound to whatever the
caller passes in.

Two kinds of entry arrive here. A metadata-only entry (no licence to carry the
body) is toasted from its SHAPE: RAR's own method for that kind of work. A
licensed entry (CC BY and friends, `recipe` present on the record) is toasted
from its BODY: the upstream prompt verbatim, with attribution, plus its
prerequisites, steps and expected output — the recipe becomes a deterministic,
callable agent. That is the point of toasting: a prompt a model interprets
differently every time becomes code that returns the same thing every time.

A model may sharpen either kind out of band — `refine` passes an entry through
the local Brainstem and caches the structured result (a tailored description,
the inputs to ask for, when to use it) keyed by the entry's content digest. The
BUILD never calls a model: it reads the cache, so regeneration is byte-stable and
the drift gate stays meaningful. Stale cache (digest moved) is ignored.

Same analysis pattern as the curator reviews: score real metadata, pick from
rules-as-data, optionally let a model sharpen the result, fall back to the rules
when no model is available. Deterministic by default so regeneration is
byte-stable and the drift gate stays meaningful.

  Rules as data     — add an archetype by adding a row; no control flow changes.
  Deterministic     — same input, same toast, forever.
  Attributed        — bodies are carried only from sources whose licence allows it.

Usage:
    python skill_toaster_agent.py                     # describe the engine
    python skill_toaster_agent.py analyze <slug>      # show the inferred shape
    python skill_toaster_agent.py toast <slug>        # show the generated spec
    python skill_toaster_agent.py refine <slug>       # one pass through the local Brainstem -> cache
    python skill_toaster_agent.py refine_all [N]      # refine up to N entries that lack a fresh refinement
"""

import fcntl
import hashlib
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/skill_toaster_agent",
    "version": "2.0.0",
    "display_name": "SkillToaster",
    "description": "Turns an aggregated third-party entry into a real, deterministic RAPP agent: licensed recipes are carried verbatim with attribution (prompt, prerequisites, steps, expected output), metadata-only entries get a method for their shape, and a model pass through the local Brainstem can enrich either into a cached, digest-keyed refinement the build consumes.",
    "author": "Kody Wildfeuer",
    "tags": ["aggregation", "codegen", "engine", "rules_as_data", "toaster"],
    "category": "devtools",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent", "@kody-w/rappter_engine_agent"],
}

BASE_DIR = Path(__file__).resolve().parent
RAR_DIR = BASE_DIR.parent.parent


# ── base class ──────────────────────────────────────────────────────────────
# Prefer the real Rappter Engine so this participates in the engine ecosystem
# (state, ticks, export, commit). Degrade to a minimal shim when loaded outside
# the repo, so the single-file promise holds: this file always runs.

def _load_engine_base():
    try:
        import importlib.util

        path = BASE_DIR / "rappter_engine_agent.py"
        if path.exists():
            spec = importlib.util.spec_from_file_location("_rappter_engine", path)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            return mod.RappterEngine
    except Exception:
        pass

    try:
        from agents.basic_agent import BasicAgent as _Base
    except ModuleNotFoundError:
        class _Base:  # noqa: D401
            def __init__(self, name, metadata):
                self.name = name
                self.metadata = metadata

    class _Shim(_Base):
        ENGINE_NAME = "Rappter Engine"
        RULES = {}

        @staticmethod
        def load_json(path):
            path = Path(path)
            if not path.exists():
                return {}
            try:
                return json.loads(path.read_text())
            except Exception:
                return {}

    return _Shim


RappterEngine = _load_engine_base()


# ── the toaster ─────────────────────────────────────────────────────────────

class SkillToasterEngine(RappterEngine):
    """Infers a capability's shape from metadata and generates a method for it."""

    ENGINE_NAME = "Skill Toaster"
    STATE_FILE = RAR_DIR / "state" / "toasted_skills.json"
    AGGREGATED = RAR_DIR / "state" / "aggregated.json"
    COMMIT_PATHS = ["state/toasted_skills.json"]
    GIT_DIR = RAR_DIR

    # The four operations every toasted agent exposes. Fixed, because a caller
    # that has learned one aggregated agent has learned all of them.
    OPERATIONS = ["run", "plan", "checklist", "describe"]

    RULES = {
        "review": {
            "weight": 3,
            "verb": "Review",
            "subject_label": "artifact under review",
            "match": {
                "accessibility", "audit", "checker", "compliance", "governance", "lint", "quality",
                "quality_assurance", "review", "risk", "security", "testing", "validation"
            },
            "words": {
                "against", "assess", "audit", "check", "compliance", "inspect", "review",
                "validate", "verify"
            },
            "params": {
                "subject": "What is being reviewed \u2014 a file path, URL, document or system.",
                "criteria": "Optional. The standard to review against, if narrower than the default.",
            },
            "steps": [
                "Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.",
                "Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.",
                "Assess each unit against the standard, recording rule ID, location and observed value \u2014 never a bare verdict.",
                "Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.",
                "Propose a concrete remediation per finding, with the corrected value where one exists.",
                "Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.",
            ],
            "checks": [
                "Every finding cites a rule ID and an exact location.",
                "Coverage is stated as a fraction of the inventory, not as 'reviewed'.",
                "Severity reflects consequence, and blocking items are listed first.",
                "A clean result explicitly says what was checked and found compliant.",
            ],
            "deliverable": "A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.",
        },
        "author": {
            "weight": 3,
            "verb": "Draft",
            "subject_label": "document to produce",
            "match": {
                "communication", "content", "copywriting", "deck", "documents", "email",
                "narrative", "powerpoint", "presentations", "report", "slides", "word", "writing"
            },
            "words": {
                "author", "compose", "deck", "document", "draft", "generate", "produce",
                "summarize", "write"
            },
            "params": {
                "subject": "What to produce, and about what.",
                "audience": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
            },
            "steps": [
                "Fix the reader and the decision. A document that does not change a decision does not need to exist.",
                "State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.",
                "Outline to the claim: every section either supports it or is cut.",
                "Draft at full length without editing, so structure problems surface before sentence problems.",
                "Cut to the shortest version that still lands, then check each remaining paragraph earns its place.",
                "Close with what the reader should do next, stated as an action rather than a summary.",
            ],
            "checks": [
                "The claim is stated in the first paragraph, not withheld.",
                "Every section maps to the claim.",
                "Numbers are sourced and current.",
                "The ask is explicit and actionable.",
            ],
            "deliverable": "A finished draft with a stated claim, an outline that serves it, and an explicit ask.",
        },
        "analyze": {
            "weight": 3,
            "verb": "Analyze",
            "subject_label": "question under analysis",
            "match": {
                "analysis", "assessment", "benchmark", "chart", "comparison", "data",
                "decision_making", "evaluation", "insights", "metrics", "reporting", "research"
            },
            "words": {
                "analyze", "assess", "compare", "evaluate", "insight", "investigate", "measure",
                "research"
            },
            "params": {
                "subject": "The question to answer, stated as a question.",
                "data_source": "Optional. Where the evidence comes from.",
            },
            "steps": [
                "Restate the question so it is falsifiable. 'Is X better?' becomes 'Does X reduce Y by more than Z?'",
                "Declare in advance what result would change the decision \u2014 this is what separates analysis from justification.",
                "Identify the evidence available and, explicitly, the evidence that is missing.",
                "Compute the comparison, holding the method constant across every option.",
                "Quantify uncertainty. A point estimate with no interval invites false confidence.",
                "Answer the original question in one sentence, then show the working beneath it.",
            ],
            "checks": [
                "The question is falsifiable and answered directly.",
                "The decision threshold was stated before the result.",
                "Missing evidence is named rather than silently excluded.",
                "Uncertainty is quantified.",
            ],
            "deliverable": "A decision-grade answer: one-sentence verdict, method, evidence, uncertainty, and what would change the conclusion.",
        },
        "convert": {
            "weight": 2,
            "verb": "Convert",
            "subject_label": "input to convert",
            "match": {
                "conversion", "convert", "etl", "export", "extraction", "format", "import",
                "migration", "parsing", "transform", "translation"
            },
            "words": {
                "convert", "export", "extract", "import", "into", "migrate", "transform",
                "translate"
            },
            "params": {
                "subject": "The input to convert \u2014 path, URL or payload.",
                "target_format": "Optional. The desired output format.",
            },
            "steps": [
                "Characterise the input completely before writing any mapping: schema, encoding, size, and every optional field actually present.",
                "Define the target contract with the same rigour, including what the consumer requires versus merely accepts.",
                "Map field by field, and write down the fields with no counterpart \u2014 silent drops are how conversions lose data.",
                "Decide the policy for the unmappable: fail, default, or carry through as an extension. Never drop by accident.",
                "Convert a representative sample first and diff it against the input on the fields that matter.",
                "Run the whole set, then reconcile counts and checksums between input and output.",
            ],
            "checks": [
                "Record counts reconcile between input and output.",
                "Every unmapped field is listed with its disposition.",
                "A round-trip on the sample is lossless, or the loss is documented and intended.",
                "The conversion is rerunnable and produces identical output.",
            ],
            "deliverable": "Converted output plus a mapping table, an unmapped-field list, and a reconciliation showing nothing was lost silently.",
        },
        "design": {
            "weight": 3,
            "verb": "Design",
            "subject_label": "thing being designed",
            "match": {
                "architecture", "blueprint", "design", "go_live", "ideation", "modeling",
                "planning", "prototyping", "roadmap", "specification", "strategy"
            },
            "words": {
                "architect", "blueprint", "define", "design", "plan", "shape", "specify",
                "structure"
            },
            "params": {
                "subject": "What is being designed.",
                "constraints": "Optional. Hard constraints \u2014 budget, platform, deadline, compliance.",
            },
            "steps": [
                "Write the constraints down first. A design produced before the constraints are known is a preference.",
                "State the success condition in terms someone else could measure without you present.",
                "Produce at least two genuinely different approaches; a single option is a decision already made, not a design.",
                "Compare them against the constraints, and name what each one gives up. Every design gives something up.",
                "Choose, and record why the rejected options were rejected \u2014 that record is what survives the next reorganisation.",
                "Identify the riskiest assumption and the cheapest way to test it before committing.",
            ],
            "checks": [
                "Constraints are written down and the design respects them.",
                "At least two options were genuinely considered.",
                "The trade-off accepted is stated explicitly.",
                "The riskiest assumption has a cheap test attached.",
            ],
            "deliverable": "A design record: constraints, options considered, the choice, the trade-off accepted, and the first thing to de-risk.",
        },
        "automate": {
            "weight": 3,
            "verb": "Automate",
            "subject_label": "process to automate",
            "match": {
                "agents", "api", "automation", "connector", "deployment", "devops", "integration",
                "mcp", "orchestration", "pipeline", "provisioning", "scripts", "workflow"
            },
            "words": {
                "automate", "connect", "integrate", "orchestrate", "pipeline", "schedule",
                "trigger", "workflow"
            },
            "params": {
                "subject": "The process to automate.",
                "trigger": "Optional. What starts it \u2014 schedule, event or manual.",
            },
            "steps": [
                "Run the process manually once and write down every step, including the ones people do without noticing.",
                "Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.",
                "Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.",
                "Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.",
                "Add an observable signal \u2014 a log line, a status file, a notification \u2014 so a broken run is noticed without being looked for.",
                "Run it alongside the manual process until they agree, then retire the manual path deliberately.",
            ],
            "checks": [
                "Every step is idempotent and the whole run is safely retryable.",
                "Failure behaviour is defined per step, and failures are loud.",
                "A completion condition exists and is checked.",
                "The first production run was reconciled against the manual process.",
            ],
            "deliverable": "A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.",
        },
        "diagnose": {
            "weight": 2,
            "verb": "Diagnose",
            "subject_label": "symptom to diagnose",
            "match": {
                "debug", "diagnostics", "error", "incident", "monitoring", "observability",
                "runtime", "support", "troubleshooting"
            },
            "words": {
                "debug", "diagnose", "error", "failure", "fix", "investigate", "troubleshoot", "why"
            },
            "params": {
                "subject": "The symptom \u2014 what was observed, not what you think caused it.",
                "environment": "Optional. Where it happens, and where it does not.",
            },
            "steps": [
                "Separate the symptom from the theory. Write down only what was observed, with timestamps.",
                "Establish a reliable reproduction. An intermittent bug you cannot trigger is not yet being debugged, it is being guessed at.",
                "Find the boundary: the nearest case that works and the nearest that fails. The cause lives between them.",
                "Bisect that gap, changing one variable at a time.",
                "Confirm the cause by making the failure appear and disappear on demand.",
                "Fix the cause, then add the check that would have caught it \u2014 otherwise it returns under a different symptom.",
            ],
            "checks": [
                "The symptom is recorded separately from any theory about it.",
                "A reliable reproduction exists.",
                "Causation was demonstrated by toggling it, not inferred from correlation.",
                "A regression check now covers the failure.",
            ],
            "deliverable": "A diagnosis: observed symptom, reproduction, the boundary that isolated it, demonstrated cause, fix, and the check that pins it.",
        },
        "general": {
            "weight": 1,
            "verb": "Run",
            "subject_label": "task",
            "match": set(),
            "words": set(),
            "params": {
                "subject": "What to apply this capability to.",
            },
            "steps": [
                "State the goal as an outcome someone else could verify without you.",
                "List what you have and what is missing before starting.",
                "Do the smallest version end to end, so unknowns surface while they are cheap.",
                "Check the result against the goal as stated, not against what turned out to be convenient.",
                "Record what would have to be true for this to be wrong.",
            ],
            "checks": [
                "The outcome is independently verifiable.",
                "Assumptions are written down.",
                "The result was checked against the original goal.",
            ],
            "deliverable": "A completed pass with the goal, the method, the result, and the assumptions it rests on.",
        },
    }

    # ── analysis ────────────────────────────────────────────────────────
    #
    # Deterministic, and deliberately so. The same entry must toast to the same
    # agent on every run or the drift gate is noise. Tags outrank description
    # words because a publisher chose the tags on purpose; the description is a
    # tiebreak. Remaining ties resolve by RULES insertion order, which is
    # stable in Python 3.7+.

    TAG_WEIGHT = 2.0
    WORD_WEIGHT = 1.0
    KIND_WEIGHT = 1.5

    @staticmethod
    def norm(text):
        return re.sub(r"[^a-z0-9_]+", "_", str(text).lower()).strip("_")

    @classmethod
    def signals_for(cls, item):
        """Extract the comparable signal sets from an aggregated entry."""
        tags = {cls.norm(t) for t in item.get("tags") or [] if str(t).strip()}
        text = " ".join(str(item.get(k) or "") for k in ("name", "description"))
        words = set(re.findall(r"[a-z]+", text.lower()))
        kind = cls.norm(item.get("kind") or "")
        return tags, words, kind

    @classmethod
    def analyze(cls, item):
        """Score every archetype against the entry. Returns the full analysis."""
        tags, words, kind = cls.signals_for(item)
        kind_words = set(kind.split("_")) if kind else set()

        scores, matched = {}, {}
        for aid, rule in cls.RULES.items():
            if aid == "general":
                continue
            hit_tags = sorted(tags & rule["match"])
            hit_words = sorted(words & rule["words"])
            hit_kind = sorted(kind_words & (rule["match"] | rule["words"]))
            score = (
                cls.TAG_WEIGHT * len(hit_tags)
                + cls.WORD_WEIGHT * len(hit_words)
                + cls.KIND_WEIGHT * len(hit_kind)
            )
            scores[aid] = score
            matched[aid] = (
                [f"tag:{t}" for t in hit_tags]
                + [f"word:{w}" for w in hit_words]
                + [f"kind:{k}" for k in hit_kind]
            )

        best = max(scores, key=lambda a: scores[a]) if scores else "general"
        top = scores.get(best, 0.0)
        if top <= 0:
            best, top = "general", 0.0

        # Confidence is the winner's share of all scored evidence. A capability
        # that reads equally as three things should say so rather than pretend.
        total = sum(v for v in scores.values() if v > 0)
        confidence = round(top / total, 3) if total else 0.0

        runners = sorted(
            ((a, s) for a, s in scores.items() if s > 0 and a != best),
            key=lambda kv: (-kv[1], kv[0]),
        )[:2]

        return {
            "archetype": best,
            "score": round(top, 2),
            "confidence": confidence,
            "signals": matched.get(best, []),
            "runners_up": [{"archetype": a, "score": round(s, 2)} for a, s in runners],
        }

    # ── toasting ────────────────────────────────────────────────────────

    @classmethod
    def toast(cls, item):
        """Produce the full agent spec for an aggregated entry.

        Pure function of the entry plus RULES plus any cached model refinement,
        so regeneration is byte-stable.
        """
        recipe = item.get("recipe") if isinstance(item.get("recipe"), dict) else {}
        if recipe.get("prompt"):
            return cls.toast_recipe(item, recipe)

        analysis = cls.analyze(item)
        rule = cls.RULES.get(analysis["archetype"], cls.RULES["general"])

        cached = cls.cached_refinement(item)
        steps = cached.get("steps") or list(rule["steps"])
        checks = cached.get("checks") or list(rule["checks"])

        params = {"subject": rule["params"].get("subject", "What to apply this to.")}
        for key, desc in rule["params"].items():
            params[key] = desc

        return {
            "archetype": analysis["archetype"],
            "verb": rule["verb"],
            "subject_label": rule["subject_label"],
            "confidence": analysis["confidence"],
            "signals": analysis["signals"][:6],
            "operations": list(cls.OPERATIONS),
            "params": params,
            "steps": steps,
            "checks": checks,
            "deliverable": rule["deliverable"],
            "refined_by": cached.get("model") or "rules",
        }

    RECIPE_OPERATIONS = ["run", "prompt", "plan", "checklist", "describe"]

    @classmethod
    def recipe_digest(cls, item):
        """Fingerprint of the carried body; a refinement is valid only for the
        body it was made from."""
        recipe = item.get("recipe") if isinstance(item.get("recipe"), dict) else {}
        basis = json.dumps({"ref": item.get("ref"), "recipe": recipe, "description": item.get("description")},
                           sort_keys=True, separators=(",", ":"))
        return hashlib.sha256(basis.encode("utf-8")).hexdigest()[:16]

    @classmethod
    def toast_recipe(cls, item, recipe):
        """A licensed recipe becomes a deterministic agent: its prompt verbatim,
        its prerequisites as the checklist, its steps as the plan."""
        cached = cls.cached_refinement(item)
        steps = [str(x) for x in (recipe.get("steps") or []) if str(x).strip()] or [
            "Paste the prompt into the target platform and answer what it asks for.",
            "Review the output against the expected result below.",
        ]
        prereqs = [str(x) for x in (recipe.get("prerequisites") or []) if str(x).strip()]
        expected = str(recipe.get("expected_output") or recipe.get("what_it_does") or "").strip()
        checks = [f"Prerequisite: {p}" for p in prereqs]
        if expected:
            checks.append(f"Output matches: {expected}")
        inputs = cached.get("inputs") if isinstance(cached.get("inputs"), list) else []
        params = {"context": "Optional. Details the recipe should use — the record, scope, dates or filters it asks for."}
        for inp in inputs[:6]:
            if isinstance(inp, dict) and inp.get("name"):
                key = re.sub(r"[^a-z0-9_]+", "_", str(inp["name"]).lower()).strip("_")[:40]
                if key and key not in params:
                    params[key] = str(inp.get("description") or "")[:200]
        platforms = item.get("platforms") or []
        return {
            "archetype": "recipe",
            "verb": "Run",
            "subject_label": "context for the recipe",
            "confidence": 1.0,
            "signals": ["recipe:prompt"] + (["refined"] if cached else []),
            "operations": list(cls.RECIPE_OPERATIONS),
            "params": params,
            "steps": steps,
            "checks": checks,
            "deliverable": expected or "The recipe's output, produced on the target platform.",
            "refined_by": cached.get("model") or "recipe",
            "recipe": {
                "prompt": str(recipe.get("prompt") or "").strip(),
                "prerequisites": prereqs,
                "steps": steps,
                "expected_output": expected,
                "business_value": str(recipe.get("business_value") or "").strip(),
                "what_it_does": str(recipe.get("what_it_does") or "").strip(),
                "tenant_caveat": str(recipe.get("tenant_caveat") or "").strip(),
                "authors": [str(a) for a in (recipe.get("authors") or [])],
                "verified_against": str(recipe.get("verified_against") or "").strip(),
                "platform": ", ".join(str(p) for p in platforms) or "the target platform",
            },
            "refinement": {
                "description": str(cached.get("description") or "").strip(),
                "when_to_use": str(cached.get("when_to_use") or "").strip(),
                "example_request": str(cached.get("example_request") or "").strip(),
                "inputs": [{"name": str(i.get("name")), "description": str(i.get("description") or "")}
                           for i in inputs if isinstance(i, dict) and i.get("name")][:6],
                "model": str(cached.get("model") or ""),
            } if cached else {},
        }

    # ── the pass through the local Brainstem ─────────────────────────────

    REFINE_CONTRACT = (
        "You are toasting a recipe into a deterministic agent. Read the recipe below and answer with ONE JSON "
        "object and nothing else, keys exactly: description (one sentence, <=220 chars, says what a caller gets "
        "and when to call this; no marketing), when_to_use (<=200 chars), inputs (array of up to 5 objects "
        "{name, description} — the concrete things the prompt asks the user for, e.g. warehouse id, account "
        "name, date range; empty array if none), example_request (<=160 chars, how a user would ask for this "
        "in chat). Do not invent capabilities the prompt does not have.\n\n"
    )

    @classmethod
    def brainstem_url(cls):
        return os.environ.get("BRAINSTEM_URL", "http://localhost:7071").rstrip("/")

    @classmethod
    def _brainstem_model(cls):
        try:
            with urllib.request.urlopen(cls.brainstem_url() + "/health", timeout=10) as resp:
                return str(json.loads(resp.read().decode("utf-8")).get("model") or "brainstem")
        except (urllib.error.URLError, OSError, ValueError):
            return "brainstem"

    @classmethod
    def refine_via_brainstem(cls, item, timeout=180):
        """One pass: recipe -> local Brainstem /chat -> validated JSON -> cache entry.
        Returns the cache entry, or raises with a reason. Never called by the build."""
        recipe = item.get("recipe") if isinstance(item.get("recipe"), dict) else {}
        body = {
            "title": item.get("name"), "summary": item.get("description"),
            "prompt": recipe.get("prompt"), "prerequisites": recipe.get("prerequisites"),
            "steps": recipe.get("steps"), "expected_output": recipe.get("expected_output"),
            "platform": ", ".join(item.get("platforms") or []),
        }
        user_input = cls.REFINE_CONTRACT + "RECIPE:\n" + json.dumps(body, ensure_ascii=False, indent=1)
        req = urllib.request.Request(
            cls.brainstem_url() + "/chat", method="POST",
            data=json.dumps({"user_input": user_input}).encode("utf-8"),
            headers={"Content-Type": "application/json"},
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            answer = json.loads(resp.read().decode("utf-8"))
        text = str(answer.get("response") or "")
        m = re.search(r"\{.*\}", text, re.S)
        if not m:
            raise ValueError("brainstem answer carried no JSON object")
        data = json.loads(m.group(0))
        desc = str(data.get("description") or "").strip()
        if len(desc) < 20:
            raise ValueError("refinement description too short")
        inputs = [{"name": str(i.get("name"))[:60], "description": str(i.get("description") or "")[:200]}
                  for i in (data.get("inputs") or []) if isinstance(i, dict) and i.get("name")][:5]
        return {
            "model": cls._brainstem_model(),
            "content_digest": cls.recipe_digest(item),
            "archetype": "recipe",
            "description": desc[:220],
            "when_to_use": str(data.get("when_to_use") or "").strip()[:200],
            "example_request": str(data.get("example_request") or "").strip()[:160],
            "inputs": inputs,
            "refined_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        }

    @classmethod
    def save_refinement(cls, item, entry):
        """Read-modify-write of the cache under an exclusive file lock, so
        several refine workers can run side by side without losing entries."""
        cls.STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
        lock_path = cls.STATE_FILE.with_suffix(".lock")
        with open(lock_path, "w") as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            try:
                state = cls.load_json(cls.STATE_FILE) or {}
                refs = state.setdefault("refinements", {})
                refs[str(item.get("ref"))] = entry
                state["updated_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
                state["schema"] = "rar-toasted-skills/2"
                tmp = cls.STATE_FILE.with_suffix(".tmp")
                tmp.write_text(json.dumps(state, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
                os.replace(tmp, cls.STATE_FILE)
            finally:
                fcntl.flock(lock, fcntl.LOCK_UN)
        return entry

    @classmethod
    def cached_refinement(cls, item):
        """Model refinements are cached in state, keyed by upstream digest.

        The build reads the cache; it never calls a model. That keeps codegen
        deterministic and offline while still letting a model improve the
        wording out of band — exactly how curator reviews accumulate.
        """
        digest = str(item.get("ref") or item.get("content_digest") or "").strip()
        if not digest:
            return {}
        state = cls.load_json(cls.STATE_FILE)
        entry = (state.get("refinements") or {}).get(digest)
        if not isinstance(entry, dict):
            return {}
        if isinstance(item.get("recipe"), dict) and item["recipe"].get("prompt"):
            # a refinement is only valid for the body it was made from
            return entry if entry.get("content_digest") == cls.recipe_digest(item) else {}
        if entry.get("archetype") and entry["archetype"] != cls.analyze(item)["archetype"]:
            return {}
        return entry

    # ── engine surface ──────────────────────────────────────────────────

    def load_items(self):
        data = self.load_json(self.AGGREGATED)
        items = [dict(it) for it in (data.get("items") or []) if isinstance(it, dict)]
        if not items:
            # Older snapshot shape nested items under each source.
            for src in data.get("sources") or []:
                for it in src.get("items") or []:
                    merged = dict(it)
                    merged.setdefault("source_id", src.get("id"))
                    items.append(merged)
        return items

    def find_item(self, slug):
        want = self.norm(slug)
        for it in self.load_items():
            if want in {self.norm(it.get("source_slug")), self.norm(it.get("ref")),
                        self.norm(it.get("name"))}:
                return it
        return None

    def tick(self, state, ctx=None):
        """One cycle: analyse every aggregated entry and record its shape."""
        items = self.load_items()
        counts, log = {}, []
        for it in items:
            a = self.analyze(it)
            counts[a["archetype"]] = counts.get(a["archetype"], 0) + 1
        state.setdefault("shape_census", {}).update(counts)
        state["items_analyzed"] = len(items)
        for aid in sorted(counts, key=lambda k: (-counts[k], k)):
            log.append(f"{aid}: {counts[aid]}")
        if not log:
            log.append("no aggregated entries found")
        return log

    # ── agent surface ───────────────────────────────────────────────────

    def __init__(self):
        self.name = __manifest__["display_name"]
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "description": "What the toaster should do.",
                        "enum": ["describe", "list_rules", "analyze", "toast",
                                 "census", "get_state"],
                    },
                    "slug": {
                        "type": "string",
                        "description": "Aggregated entry to analyze or toast. "
                                       "Defaults to a built-in example.",
                    },
                },
                "required": ["operation"],
            },
        }
        try:
            super().__init__(self.name, self.metadata)
        except TypeError:
            pass
        self._state = None

    def _resolve(self, slug):
        if slug:
            found = self.find_item(slug)
            if found:
                return found, None
            return DEMO_ITEM, f"No aggregated entry matched {slug!r}; showing the example."
        items = self.load_items()
        return (items[0] if items else DEMO_ITEM), None

    def perform(self, **kwargs):
        """Always returns a string."""
        op = (kwargs.get("operation") or "describe").strip()

        if op == "describe":
            return (
                f"{self.ENGINE_NAME} — {__manifest__['description']}\n\n"
                f"Archetypes: {len(self.RULES)} "
                f"({', '.join(sorted(self.RULES))})\n"
                f"Operations emitted per toasted agent: "
                f"{', '.join(self.OPERATIONS)}\n"
                "Deterministic: the same entry always toasts to the same agent.\n"
                "Licensed recipes are carried verbatim with attribution; metadata-only "
                "entries get a method for their shape; `refine` passes an entry through "
                "the local Brainstem and caches the result for the build."
            )

        if op == "list_rules":
            lines = [f"{self.ENGINE_NAME} — {len(self.RULES)} archetypes"]
            for aid, rule in self.RULES.items():
                lines.append(
                    f"  {aid:<9} {rule['verb']:<8} "
                    f"weight={rule.get('weight', 1)} "
                    f"steps={len(rule['steps'])} checks={len(rule['checks'])}"
                )
            return "\n".join(lines)

        if op == "analyze":
            item, note = self._resolve(kwargs.get("slug"))
            a = self.analyze(item)
            lines = [
                f"{item.get('name', 'entry')} → {a['archetype']}",
                f"score {a['score']}  confidence {a['confidence']}",
                "signals: " + (", ".join(a["signals"]) or "none"),
            ]
            if a["runners_up"]:
                lines.append("runners-up: " + ", ".join(
                    f"{r['archetype']}({r['score']})" for r in a["runners_up"]))
            if note:
                lines.append(note)
            return "\n".join(lines)

        if op == "toast":
            item, note = self._resolve(kwargs.get("slug"))
            spec = self.toast(item)
            lines = [
                f"{item.get('name', 'entry')} → {spec['archetype']} "
                f"({spec['verb']}, confidence {spec['confidence']}, "
                f"via {spec['refined_by']})",
                f"operations: {', '.join(spec['operations'])}",
                f"parameters: {', '.join(spec['params'])}",
                "",
                "procedure:",
            ]
            lines += [f"  {i}. {s}" for i, s in enumerate(spec["steps"], 1)]
            lines += ["", "acceptance:"]
            lines += [f"  - {c}" for c in spec["checks"]]
            lines += ["", f"deliverable: {spec['deliverable']}"]
            if note:
                lines.append(note)
            return "\n".join(lines)

        if op == "refine":
            item, note = self._resolve(kwargs.get("slug"))
            if not (isinstance(item.get("recipe"), dict) and item["recipe"].get("prompt")):
                return f"{item.get('ref')}: no carried recipe body; only licensed recipe entries are refined."
            try:
                entry = self.refine_via_brainstem(item, timeout=int(kwargs.get("timeout") or 180))
            except (urllib.error.URLError, OSError, ValueError) as exc:
                return f"refine failed for {item.get('ref')}: {exc}"
            self.save_refinement(item, entry)
            return (f"refined {item.get('ref')} via {entry['model']} (digest {entry['content_digest']})\n"
                    f"description: {entry['description']}\n"
                    f"when_to_use: {entry['when_to_use']}\n"
                    f"inputs: {', '.join(i['name'] for i in entry['inputs']) or 'none'}\n"
                    f"example: {entry['example_request']}")

        if op == "refine_all":
            limit = int(kwargs.get("limit") or 25)
            # workers: pass offset=i stride=n to N processes and they partition the
            # list without coordination; the cache write is locked, so nothing is lost.
            offset, stride = int(kwargs.get("offset") or 0), max(1, int(kwargs.get("stride") or 1))
            done, failed, skipped = [], [], 0
            candidates = [it for it in self.load_items()
                          if isinstance(it.get("recipe"), dict) and it["recipe"].get("prompt")]
            for item in candidates[offset::stride]:
                if len(done) + len(failed) >= limit:
                    break
                if self.cached_refinement(item):
                    skipped += 1
                    continue
                try:
                    self.save_refinement(item, self.refine_via_brainstem(item, timeout=int(kwargs.get("timeout") or 180)))
                    done.append(str(item.get("ref")))
                except (urllib.error.URLError, OSError, ValueError) as exc:
                    failed.append(f"{item.get('ref')}: {exc}")
            return (f"refine_all: {len(done)} refined, {len(failed)} failed, {skipped} already fresh\n"
                    + "\n".join(f"  + {r}" for r in done) + ("\n" if done else "")
                    + "\n".join(f"  ! {f}" for f in failed))

        if op == "census":
            state = {}
            log = self.tick(state)
            return (f"Analyzed {state.get('items_analyzed', 0)} aggregated entries\n"
                    + "\n".join(f"  {line}" for line in log))

        if op == "get_state":
            state = self.load_json(self.STATE_FILE)
            if not state:
                return ("No toaster state yet. Refinements are optional; the "
                        "engine falls back to its rules, which is the default.")
            refs = state.get("refinements") or {}
            return (f"Toaster state: {len(refs)} cached refinement(s), "
                    f"updated {state.get('updated_at', 'unknown')}")

        return (f"Unknown operation {op!r}. Valid operations: "
                "describe, list_rules, analyze, toast, refine, refine_all, census, get_state")


# ── module-level helpers, used by scripts/generate_aggregated_agents.py ─────

_ENGINE = None


def _engine():
    global _ENGINE
    if _ENGINE is None:
        _ENGINE = SkillToasterEngine()
    return _ENGINE


def analyze_skill(item):
    """Infer the capability shape of an aggregated entry."""
    return SkillToasterEngine.analyze(item)


def toast_skill(item):
    """Generate the full agent spec for an aggregated entry."""
    return SkillToasterEngine.toast(item)


DEMO_ITEM = {
    "name": "Agent Evaluation Designer",
    "slug": "agent-evaluation-designer",
    "description": "Design a rigorous, platform-aware evaluation for an AI agent.",
    "kind": "skill",
    "tags": ["evaluation", "testing", "quality_assurance", "decision_making"],
}


if __name__ == "__main__":
    engine = SkillToasterEngine()
    argv = sys.argv[1:]
    op = argv[0] if argv else "describe"
    slug = argv[1] if len(argv) > 1 else None
    if op == "refine_all":
        # refine_all [limit] [offset] [stride]
        print(engine.perform(operation=op, limit=int(slug or 25),
                             offset=int(argv[2]) if len(argv) > 2 else 0,
                             stride=int(argv[3]) if len(argv) > 3 else 1))
    else:
        print(engine.perform(operation=op, slug=slug))
