---
name: "rar-kody-w-skill-toaster"
description: "Turns an aggregated third-party entry into a real, deterministic RAPP agent: licensed recipes are carried verbatim with attribution (prompt, prerequisites, steps, expected output), metadata-only entries get a method for their shape, and a model pass through the local Brainstem can enrich either into a cached, digest-keyed refinement the build consumes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/skill_toaster_agent", "rar_sha256": "e90d6b7dc0ffe83e5274346aeb17f79e94894ee345685f897fbd8aa0e9ea6508", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "2.0.0", "author": "Kody Wildfeuer", "tags": ["aggregation", "codegen", "engine", "rules_as_data", "toaster"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/skill_toaster_agent`. The original RAPP
agent is preserved byte-for-byte in `skill_toaster_agent.py` and in the RCI capsule.

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

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "What the toaster should do.",
      "enum": [
        "describe",
        "list_rules",
        "analyze",
        "toast",
        "census",
        "get_state"
      ],
      "type": "string"
    },
    "slug": {
      "description": "Aggregated entry to analyze or toast. Defaults to a built-in example.",
      "type": "string"
    }
  },
  "required": [
    "operation"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `skill_toaster_agent.py` and embedded as the fenced Python below (sha256 e90d6b7dc0ffe83e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `skill_toaster_agent.py` first:

```bash
python3 skill_toaster_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 skill_toaster_agent.py   # or on stdin
python3 skill_toaster_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
