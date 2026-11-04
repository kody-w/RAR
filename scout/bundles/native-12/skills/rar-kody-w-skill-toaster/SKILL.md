---
name: "rar-kody-w-skill-toaster"
description: "Turns an aggregated third-party entry into a real, deterministic RAPP agent: licensed recipes are carried verbatim with attribution (prompt, prerequisites, steps, expected output), metadata-only entries get a method for their shape, and a model pass through the local Brainstem can enrich either into a cached, digest-keyed refinement the build consumes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/skill_toaster_agent", "rar_sha256": "48aea57c434c6992922172546b2ae02f219015377a34be1ce5dfdb837d9d2b0c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "2.0.0", "author": "Kody Wildfeuer", "tags": ["aggregation", "codegen", "engine", "rules_as_data", "toaster"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `skill_toaster_agent.py` and embedded as the fenced Python below (sha256 48aea57c434c6992…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `skill_toaster_agent.py` first:

```bash
python3 skill_toaster_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 skill_toaster_agent.py   # or on stdin
python3 skill_toaster_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/skill_toaster_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/skill_toaster_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/skill_toaster_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
