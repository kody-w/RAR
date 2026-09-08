---
name: "rar-kody-w-skill-toaster"
description: "Turns an aggregated third-party entry into a real, deterministic RAPP agent: licensed recipes are carried verbatim with attribution (prompt, prerequisites, steps, expected output), metadata-only entries get a method for their shape, and a model pass through the local Brainstem can enrich either into a cached, digest-keyed refinement the build consumes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/skill_toaster_agent", "rar_sha256": "e90d6b7dc0ffe83e5274346aeb17f79e94894ee345685f897fbd8aa0e9ea6508", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "2.0.0", "author": "Kody Wildfeuer", "tags": ["aggregation", "codegen", "engine", "rules_as_data", "toaster"]}
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
