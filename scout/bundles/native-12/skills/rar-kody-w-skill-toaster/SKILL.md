---
name: "rar-kody-w-skill-toaster"
description: "Turns an aggregated third-party entry into a real, deterministic RAPP agent: licensed recipes are carried verbatim with attribution (prompt, prerequisites, steps, expected output), metadata-only entries get a method for their shape, and a model pass through the local Brainstem can enrich either into a cached, digest-keyed refinement the build consumes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/skill_toaster_agent", "rar_sha256": "48aea57c434c6992922172546b2ae02f219015377a34be1ce5dfdb837d9d2b0c", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "2.0.0", "author": "Kody Wildfeuer", "tags": ["aggregation", "codegen", "engine", "rules_as_data", "toaster"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/8S7abejRrY2+Ff05v1g+yVtARKT7627WgiEQCBGCUG5VhazEPM8uP3fO5DOSTvttKu6+/bq40wfiYjYsWOPz95B/vzB6dp7UX/48cOp8KeVGad+GHRB/eHjBz9ovDou27jIwbDR1XmzcvKVE0V1EDlt4K/ae1z735dO3U6rIG/raRXnbbFyVnXgpB9XftAGdRbncdPG3krbKQpYDOb9uEpjL8gbQKEOvLgMAN06WHlOXcfgWR/UrtPG2WqI2/vKads6druFi9W3ZV1kZftxVdZBHVRd3MRt0HxcNW1Qgl/BWAbewlfRtWXXfvdxlQWt4zut832Rpy8WY7BZFLSARzB2L/xVWNTgHEFcr5q7UwYfwRH9ZbTwg3RVOk0DRuuii+7LrFVaeE66omsnzsGmGeA5B2Tr2LuvAsBtUL9LwHO8e+ADGcRR0LTfJ8H0PG0Y50EG+HgSczsg7ZVX5E2XBc0PQOTB6GRlGjQffvz7Pz5+iMHnDz/+/MFLARtABXoSp6lROGDnms0jQAosSZ08AmPlBE6Tg+9lUIMjZeCRH4Srt2/fNkEaflz97/+dDE4dNd/9+FO+evv56cPy3y4dnKkBDLYvNQOR1nEe/fAa/XV2Ua7+tvr2ReUHIMdvf/pQgD2cRT0/ffhuBYT505vhuAF48MNCp/z2u5/yX2nE4ZPM376Y+RuOlp8XI6tvv3y6/IQ/ffh5Oc0P7Jnjz+yn805if1n91KEwsl39/OlT5uRxCET+6dPfv/mNBX/zj19+AkyAPx++SnNXA321E7DFH1c/p0H+lNgP2kVk9e9+Wf3Jom9//ubj6psfHkUM5hc1ML3fLvvul+/+fD/5XWrNKsjidrFa8GTVPrXrv/vJnyz+7bbLfrLCajuDl8+A1z/Z8qcPzG+98cenATZOFrw5rvMygOf+y69fx5+s/PCnZMX/R678n79zza/T/ncc9j9X/3y51T+f3ho8Y9TrTO+O+3XiX3Pnxfefnts8z18HTZe27zu+/PWH31P7M9tOgaA/1R3w5j9YdwrYbYAj/f2vjfkPZuh8NtKfPvzjS5ILj04MAs6yIwhCq18X/gCCZNZ8+92Pf5TCk5EfnLIMcv8rvvZmbqvVz4D0j/9F/bL6eSH/928WvX7zjx//i/y6a7ytG4I4urd/e655BotvXk+A9SLf/eXKZ0D/21MArw2fD775B1gFJOAlX4y9niyDX6P43VcDC5i5GPTLh55S+DM1OrmTTvMfI9Qi1I+rvGgDoMinsD8BcynSPvgyPDZpF4FA+Ds2nPdFb+S/Xch99ydW8vUYsKx4STUHbrpEhKfVf/Pd04AQCgVa+/s3n01mCYAfPn6VVOMVwGeX2c9PYOZqyUph7Ae59xr49euf0QFk4ggcplmi1goCofvDx9W7hJ2/fx4GlvuWJvIiX1LE72j9zq6BJpbFdZfnQd186kqw/l8a8vv077vyjZvfMvOnVvdz/aW8vl0evIvkO0BncbIlw/+Rpd/rF7C9mMa/4nSZ8//WQJ8h+3/YPBsApN7XPen/f2OfyzZfivzPM+1r7ivw/PLxC/t8DX1hoh//jFAfO+8LXmnD/+ROL/V+3Tk+w5sFGPwm7z5J/Dr4Cj9fJwEAMpAAyL5fI/Ec/PPlC/z66mMAhb3A72pgYx/+2oVeeoJe6QbE8viXH4AIfnmz5xjA58WkgxyAUHCY4MXXWwwGpr0E6z+l+GRviZKeF5StA4T/4x9S0+/2/371s/e+uffMVK/9XmEcrP4Xm4ULbExjYAmOmwY/vmvzN8+eIeof/7855Muu/oc98sX/6ltQ8gCosgj6288Otmy5YK8lmIKCw2u/ewKZZfzvv479423uq4ZadviKMN4O+6X/ggMBr/0RMPAZ2L2IrlxQM/7n6ongflfSfS62Fjj45ml/gE4gHHyFhxd4e5PRa+kn4Laf3HeY9u1LlABXBqDS+xuouL6U4NvAWz2CkPDvhRmMi7Wuvu3qNI3dH4K6LuofLprILh8+rmT97cPVSbvg+RlItFmW/aXIXryuQidOgxdO/YoQfwZU/gBUnkdtnD749GuJ+HbKpzS+bpLfft7T/+NOq2eke67++zfPanYJr9++6tHPAyBotuDjp9fjZxz8OtB/C2W/qah+/Ezkj2XWX2DCe5B/aotPXRP8SuA3D/8lgTgHpf2XgTT++yvF/OMV0F7R7En4NfmbF+L4ZgEc3/wL8m8V+K+8vT34tPQbXiICdvWXnv/JSdOvQH5Q5QGj/oOxPgfeTBXFfqfo/1gNRZ08E8ezFVGEYRMAi3+W537wt3yp1M6rZy54q32WrkwwrZamTPxsmoCvvye6lCbPkgx4CcikRe3HufMqy5Y651kBrYYamNQqbpYiKVlaGU2xhKB7nEevpw2oCr8g/OLu4xtzXzvsa8bbaeGlQeOM3yIf/zjxReLdg3/vvz5Q5Mc3PwPbJTEI3v6CRECyWv7CX073gFRiUGu+0Er8KujAr/cqKS0c/9NbkfR1w/is6S/C718H378KvV8p3pb9F45+ZfbvL2n9+ONLGF+DvYCjpQ5a5PEdQLnL55dUvlv9999eNvfj10/k1oGTfJXgUySv9tXvo9F3f0LsXQMgSSNfn7HEmTjvgj+Ofj0H/Iug+D+ZGv5E5YtM31EBUMCX2TZc0udXFv6PJpanZTy1+c7H19PyW0b5VzliCUtvva2nvfzynpY/vh6+Gc4vn/3q5ze1/rJyUmAt/rQKAWC5/0X8hL5ESU+4B61+rn/5be30bqzfvs1dbG55tgrSJnji3e/+fer/a/Vz+E49XKi/neLPIvSCUbo/NmSASz9h2c+//C5qF9HnMij2km+f8/5c0LtXMQ+y8XPiS03PwPLprc73QdaCl07Or030N6D0f1OsPy8Q9P3ky+fl8IDdPz054OXTk6s/PfyvsfDRFG+dJ93YGeynAy+yX8ejz7V/DoqAjs/FW1OzfttoCtofVtpnj34hxOKJHpz0lYD+TBDvXcHoBbPStFm5jpcsSTAGhJ7Nto+r4b604+NXC88PQqdLQab6o3+ESzr4VVHvfvJk6i1A/N4efqNr47eHevOrhebSonoGz990+79tvvv4V+2urvSfpvBbs3l79slZ2mXfdHmSF0P+zXe/Rx+/4ejymrP6XJSufi7K/1WDag+Em9hf/baS/XpL9L0d/3H1a/NyuRB5mu7Hlx4/vp3r/fcSVkA5/vSrj6vfWNl3H375+GGJynXnPXf98OOH//iPlRR7ddEUYbvSvQV+1F2+BOXlTMYdKC1+b72CYq6JQTX3Ng/kzkfwJARwxuqf/0cCSo/vh3Wz3Il8erOwT89e9T9/WBmAQlHHwE6c9Hnx9FP+HFqolyCIBXUPxO1ObfA98J/vlw+L//zzK9R+KKd/vjL6E0qttD0PFFw2S09zYdoE2PWNxedl0Bh4XfveWQ7jpwTf6rzlvqxZPfcASAGAg7ZYOu+ANhDCjwuxf/7zn64DQmz+us7ZrF7AulmDCZ/ZWX3/PThDmC6t1J/ywLsXq29+/uWb1f+5+qtVT+LLHsrrTit4XtKtBF0+Aw+MupcvPrOo4z9F/PMvb5J8dbqWZn4cxm+tcRByACh8F6t+3H2PYvjKDcKllRhnZQHg5wIUga/z4eozv2DTZWi5YboDAAncc0lsQe4t3XoHHOezJJ/RBZhrE04fV6AweO76z8+J/pMHpv9zJe0VYJZFuoQAwOYbfAVAPwbi/6z013NApP6m+bXb/8PqvBjZApWd8l47b3uEzksvS0P9bfnzRi8Php/y5Uru6dJPR3qJB0wCkvHeVPr9onOAd7IMKLZ53/s55+njb3HjJ1Arv6z5VSB7BWBlWkUdwH4AXf7nm0k1AKKn/lN+wesS4k0L/ptWnjb4vBh8p/x+fdD+iwvblx3+4dr2N/e0T9raTgPDPrDrN9NtAAwoslXxvO0EKKd2lvQF1LxMWnTupEs2B/7qd95Skqzcokgyp05+XDk/5Uul9nF5mHa1u3xYLOmH1e7zrMVHF+U/OV+4WPGfDcJdtJs+0QnA762TgLwJBla/dtg+vqHvz1eZ7yUL2PGLW1tgDT98DjpvKeUt9rz5/3PjBfi8nr5fWK0WiaRBBKqrDAg1nYAlp2CO4y4KcwDJrgRBL3CyN+G+6SMBUgQx1Ima5Wb8c8X8cVWmTrtc0jbvM+McKPu1KXAshV288VnFgbjjuHEat9PrmMvN4SLgpUhczvi5J/h2ZeW075fagLelMixAcgQ89y9bWggCYdbvF2dx/pLIUDyZXcrN99vBuo5B/AIaDxZV/fFafVp9C9Tw7AF5iwCfjaLptcnSJPruKdu3y82n/SycP0/34yJQ4JdL6vriig9wv7CxcLEcEGz8U/65y/S26X6/oq2nLEJghYDnj8t14FJ1/fMV6IH/vmrgp4/V/m8Z+Sn/zAktM9brTvSz8l7F2ucrzI9/uMNcNNc1y3IQr7/yQsJLRV++k/DZOV8MPXtogK/s6SdfvC/x8aWdpZ/57gfGIpI3Gy0BEmyfhrGcBSgfONc7y+9vL4AZQQ04Wxj04xAYFSCzKOwZapas+3lzDyx4ifzdbz7f/77c59c1TxvZvW2ROdNiYjWI4u8vQLx01j2ZcxcRvB35X13T/pT/GzeyLzQBLNx/v5z91gE+FafF8ui3bvUi92oALQbpNMliVws8DJ5tkyWnxKBaf72a4T6N9cXRN83qrS/29vrGM87/lNMXXmRAHljcx3uizzdJ//gKOO+R4snvs18C4u4r8C+BHmjuiTgAPnoqNfdfPPogoLerJUAvYHJqgBc4OZB52KU/rPTWSd87Mu/Nuwzkipchx1G+HPyVBJ6X9QtWaxaUAww1AMDQeWOpA0wsFVjQx8EAAODrzu8Z8N+9GdgzqHGe3vlT/sR+3zvN96+Rd3y+NHqDXy3sXfW/XpZ/fOLyz7D8OfC8A8+fcgdB4s02gfB6oLdFFD+svng3YdHFG2z/igxBPPlSiKt/JcMXXNYWLhZxPGP4E+++7NLx/Weueb+FWrYHz145oy6G/3z2vYE91ABmhGkxrAD0yIEint2vLzn/Ddmn7zzN7+ObH73Q8wKQ+mfeXq12b8EE2N87Bn8tBiEz/t2rFM9Q+4xXTdHVS2IdAIIKPsdcIPViWKLR87yXBsSMt7rshQpXX8e2X62x/mP1Xgm8OcWSHf8dYm+lwuq/lkuM/34nBkDMsHp5I4hBi6M+s9K/Q/D54AtyXxD8FVYtl0D/DsG3Hv0XFP9j9QQs/+pdr+//++WH//42S220+vv5H+/bvG3ela+27fsVyTPupovHOK8Wy29Kx+UNr1fO+/Bj3oFS68MCoH73Mtjy2tdnBLS8MQYSASj22jh4fvtc+C1fvnyrz1y2/g3meQecfvF8HS3vsg8//v1zXfhk5r0wBF/e1A0+PZeD3686EHz4XAh++AcYBW4FNnu9U7aUhYv0/8jM7sumyPQM228WVby9G7XEimdoeAX15zs57fdLx//Vp1/Y/t12YL9nbgaGtxzmV2n8ylnhLrXlwtk7GFu4ew+MbxJ9Kz/BdAB5v28WfL5GfoDBhuD7S/Vg7C8K07eZwPhBrQSmbkkncDDC2262Hk5RKIWiCIFiW9xFnQBGQxShYATbEISz2boB4gWYH/ouuSF8ykdd2AP0XrHg01JuxMvurgeHCE4hZBgElIuiGxwmAzjcUDgROniwQQOfhGHY/XXpkq7fjvRicpHX5xp5OfrbyX7+4OJbMPO4bfjd62e/hq4UvnEfWilm4bw9ZI9tkJjo6VLeiHNtXDe309XlOsKtOn2kpIdHJVGma/dI3Z9jRGseoSvVG3SnhDK71lX3BqtJstvRenpLNyUM4ZQ0C6rIz9KDn8R7ju3DYLMmZgW6rzfNrcxmPzg0U2eYVmg7TURpNu0wM45gXr8+mUJTsjeNdIibd4Px3vB0HGIkRd/HAgShplPLspCp0KYYQgpR+qN8oLbofD/3Fna6ZH1ftnb+iO3wcLs/CG9a83S5DV3jEIiEGwLx2scBHnzRPj2Uoz5zs87ebhtbvlNpeKe13dq8ZRRNDO5l9gaFpggnJxAoWKtxrAib2+YR0hRL9gly3PR+f1vrx4g7XW2712DtsO752nAVw91SJCRfC1shR3PzGNBKCw/chdM3ZcHy68O6mQeh984HqLcOLQyVEdRu+wdKHnWccYWrcocPZKrELuAuIhtFFdgQR2YaZNh1Z4QIrN1g6nirw7FN7tijiyx3ZmHGEwqjR9ztRBzpw124drZXbI+VM0ihtj+S64AlZBHeJnfnuEa0250YkwSf0FMoJ0O2PnI4usmOzdqDHltfl4NSzSSMuJXHKTkCs+APtM92uhbYPtZgZhiYnVH2anCC8vR0gTuOEvJ8gChiHR1hv+Y0aSNK/Z5nW5wM87483g43H9lUvJCwsO4qXSz38jjI3doPpZOlN0O2KTg5TnXi7mvnYxWkccn5kC/QmK5hWLOJKao6Y3h/JQnKlmh3Nsj1Nuw5cj/UlJhTWlp1Kkqdtyp0ko6w2CgN7LGjft5MPRSuoRbuqI1sQtaUbvktga7XpE2BXTwNNpAxhi6TdGnWPGbT2aTbRxQrEHS6iiO3T3Ck4ew1P+xIX3u4jc/dEVy+ef1J9mcVKfbTbUSLtow1qWf4eEpIRj2V60cx0U6Qb3ml9oVtnkASupfgOYZufS9Q3mOWMW4tpDYzkzyZBSdF4uPuTmElqR2KCxPzUbf3bZymFKGNDyO9Kc5waB+I7IZ1sIpOOzuRKbgajYbdD2pZHQ0Bc2otymoqpv1Y0TZ7gpYuE8zshWzrR0c9j8hTfHiICVT6m3VnQ8x4QLAiPjrM2eEMP5rHQKm5nLQwVSaSbNYfdtYfTql7z+rdhuf2N/q88UpRSlBOo43DiLHr2uYTwjzdSFPbdc6OX6NU2xtn1A96aa/MzRxCZylixFNrSHgTDSPfW6jhkJNEMsNMzsM4nhPdSQ6ulG4wDuan4WKEMCEGcHKerVFsGWi6eoKT0XXjO2J85rziYg11FJZCpFOSzk2TnIfU/QhGMFsKLGMr2bHj7MyORSw1sAq1dAMV2mLnUdZ8fOerZKNxqq4M277YqMQErA3bMftoT08+tz0G23WpY/DEhUp/WkMzd7fYM6uNO6UXt5lNa/18gHm2sYeC3BoELIvnbWZ0Q8uWW+VRUaG0fqzj2qph/hG0Z+zOmeVj2xLNnhBCIoGumUmfFa9Og6DIs6OW1JKxyVS6TO574SFOfkWiWGTbyXxR96N5ro47Nd7pkMYfMQ0eacLsounO645kkUK9vYyCp/fcbeAvOra3ZOmUHWZeMPOjo919d4P0R08VzYiIoirK4EDkY7mig4YlUS6NNSuFFQU/tnTrw3duL6dEoAhanLssx3lOT9Xh0MV6TBeGtHNviFXZZJxlTJ/pWTcW4gY+wK3fng/J9vIgYkVJq0KhTVbF0Mhz5vVg79WJFi79xFkHzjyph9mTJBiEt2hmOH7jMZ5JNhPBsBc+3emiNp2Gk3Es4oE49jc7adoSnrxdQ9Isy2550pCj6VKylz2G32ZkE2YiNmlYczUH4ZQeSPZuxd2FY/ZoK4+qaj72BsTvjvvZ9e3OUX1aCCb0IbMSbljCAduKW/i8gVy2PRKsc8ATy2eIaVPK5+qOjGfLkSKX36quuFekLHVj8eryj/U4ZJQ4Mz6X6s7usH8MmHqh3RPDbiKLm9K7WHLQMfU7T4dssZvSbkwg/a6ra4o60MHIj3LWQaZ5aIXr0aXv1n5ko3OvXteal4LYl9Hjddxwssgy5cXdowPccuJuoAScKHnsmgnd4YHefO0K5SDN9XyoIXKJbRYj2QeuAu2gCy6tc5FldTWb0NEn3G2Z8VGsQ2tVjKLI0WVFNa3bINq6FVM7qJymmm+TPhDYsdtR8IAKOwamh4KOECW9wmoXpGuHfZDSbs/HJptx1m4d8fAkw6XgWKeLwMn0dL5NF5ifHR9t8NyEorW1wav95uFHsuiVObyBQpzHba66QpNYHinJTEDifYR2xkGhuGkrCtasWL9dfInuO03z4AfUSUCQ22qtJ3bBKnHBrwtjvJ9b76yg4naPE0dyzPr4vA3W6XqD4gc245WqvqISERe47xI74fY4HPf2HWOv3rkxfNJMS8YvWrI7WYrJHmtabs85ZwRW4npoiFmJeWX00qAgXSrntdvL4nUteC6Umrh4R/XtRZLu9UX2EAGj5Tubs9bhCJGngTnTPSGTtLfO1mxDJDLKV5GkQVRhQ/6jMvZmTg4Wj2fwRLIQJCe+fd7fkPo4WiyHonHJkPYx947kHTsdW6KDAYorCW2+tDUFKXVJio/GuuNJSVOtQFg1kmHXTkehk3WhlTol1fPGv9zU49VIPSnYifPlnPibG2HGyF2D8yGITzaN4MbjsS9Ow4NSrXNGX0tnf6fQVpcM4eCMO7SDb0pJeyU0siy+R73q5DaXnTuIusHeqiNfXUQ2M2Wsz1QjOubwOMN3nDv0B8godumgZKHDcxQBZY+7l4t34A+Axb7LrbRheaYe+jai9qKyvRhbnTR5DRiqujsHJxqG70jtzmdnMk3PZY7B5jwmnjZlfqWH3h2qSF0VGUkyxNGlRYVmIIBPIsZ9jKy6ibi7l+xwoX3ko9nwqLoujxdF1BAWYjL9piY5MTKlWqtyS+BdBcHrvKLkjY0pOUabsEwIj8De8crIGXoJo9bYcWc8NI/akYh2joHiZYAmLj4eN+pJHj2ZmU4blu8JBp3MsDtRvMXrA3w+6ySX+JPNXcdKRAbLTc/O2aQBrOPxhkzuo+DYx5SdKOoSMZNwH2cHS88jl3M1HUZ3lcLpWhwFaJYvIhERLoIWXhBt4ROjXiGeSgnH2G0QgcSV7kTvWHFIeF7NkjPKZ2xOE+rJlbnzUYb0I4XtGTifYlE/MFUybyKVMqF6B/c3nK/3wtaLQogl7WoNzDaBGx4aLjV5WB/9engUOoF0mYwdThviKNKzZSfBybedJEDWMGdeivV1Z/lbOToeD3Bx6EkGIo6XHAkOxQ5n+rC6itajIhRfYNBG0YVN3W/DNeLDO1vqt8autHYJY1FQFeKFHaUcFxTtUTDxeM423qSiN4Vbj4zEDz7m+LWtGYl47rktY6OUa4fxaR5wTA8SlSUKGzW9dJgf1fwguNKFOVVrUffaGNl2jlJLHY01xkNrrN7i4VV2GYxh75dYpdGkPXf0fbuNTuNDhFC7GBoom3hw+it0CrGI5HPvKsKCdlen81bfhJ6lZAHfIGGYiySeEQMe3lKOcOsrcX3oiHfdiCQRqC0RpmsD09AJsvb2vgoU+YEnYZZ0yt6xcF6/1naBExSrsowUysdYQGP+FHk2ZV7rGj059D1IWgzec1ILp9kmM6nwbu78UnSO7vxYcwbMNkHH7vNzs2Wv3XH2PeNIFbOIGonHz+cbbysVtX8IMFDJrGjh7ZCqMk428R6brpyf3UGxxjQEh6qH+hpJkWnFJh5ZRZ0n5H1bB7cS8/MEXys3aMecNrFQEPwOD/jeV8vzePIwWjrwMHXu+zrZQlvHUVCqNrvqZtTnvEYgSBEhr2cyak1bBAZXkIIWjt0M577iek3bgKSsdTnBEOFwCIN61NA5Rtx7ilS7xIjWd3F7yyk5j46aiVX2AyOP9Xara0r76GBdeih8pwRGzCPKFq95uMyJXTD4pIED7DwL+OznBzy4YTgVTt7IkwlL8D3itWJ1za7osT2G44BV7llK5bstXSC8qN2o1rtuWwU4QjhbMd3nnDAP4fWA7DeFP/q6pDjorIfr5H6idAMuJ5e1qV166HGp3h918jTeyjNWEWYwI+pWKtqNPO1pZTcdLrOUKxh8MGdaq8TUsCndkkJGNEmzsdntpK21C1c88MpLC7erThs4cU8s1ctqUq7pIEHWyeYssuRl3xaap6zv89hWCh20XSsioYnq7YadDKTJOlNlIsc73hAUl6mj71x5Ed2TXS021GnDeJEIoJXoEpFp9KHaXbratpBgfRXmAvFkkSdZvVYgTXlga3Ifg7yNziw+hIE/ev10mgR7zl3JUwmNZ71zchBHtpR4lH5Q9QUf2sjdc5QBIK1BVYzoCdvY9eg4RmcaEmzERMjLNb82iBWUM+afVT/yOnLvNQFZ64ew2l8vu0PC7g8QCEE+71wra9/kigXB7kk92TwfbN3hAWyXfVSVuaFouyOUHTdeJ8XhvMnHMi0X5KmPtw87EYS9WkuCHoQaY7LToYcgex3ekrPKqY/Dtg35nLNuvj+npcKpZ3Yj3TG74KN+e4+2nY+qSh3ILUPY2B2f9hDn0jVDNTTh5Lf0cun2jEq3KLonbL1E5nMye1XUJdH1sNvCR2kPUpDuK5i/PY99Oxw8sjQOnXXuCcvcNqaV9OguAMXWDmNQ2+ZHQ+Hpk4BwCaIqin2IsCMqbYbxzHScu3ck2CRxwY4M1TRiaOcbt74IL2bECzGzVTrF4zgDKCR/qDKlm8IQGgwmC5UmRbxog8gRXaaDsHMRrkExCcFa/84cdV2AaCz3xYDHxZ3PYiDB4B7vSfemAPE4U8U9K2c7VLBzPVSjTVOWqhR7cbxjsvN1OM1JpWP3fQPcYrqdm1gBEfCYHU7wnOINvLvQV+TiWQh73m+GkOh3s95nsIB0wFJSZIQRWi8Pu5JHqlrtdfgRHg+PzKMYi7y24s408HthIC1bHKPjvsJhlEBO86FVDcwJRtPFtVkt8Xtlpuqd19Y6bc3DYyjrw5GFACiIEixJmT1NX7ydqK6VY8IToqnuyjMD7eaGbK932XevR/Fx4uGIaE8RQ2ij62obSzzSbMlINeVqh3p9DYRSh7Lj6KF3VDbryt1cNScQ1ts4QOjb6aSy0i07myJ0LCPmuENRIQuUaFvF+lrM7c0d2DBnKFeHcXbXPMjqS3hnUZEJDvvcxwf2jOxmhsmxAwlkqVOXvToihYPQIW2HkUvPa7La0VAjqA/0qrFR30rwIcTchkWdhKv7XVYYan65I1mz3odYJQpGhiGSPlVXYKFKpDA2vyWdPVzIrelfdn26PnA9+0gcUY8OyM4bDK7RZRMVj2wFSxOVxtWcXYyhY/GzRjuBKtfBQLXRWcPxOWaOALmN7GOr4sNDTCFdhK2uqcgkba6j3WdoSF/sYSzO0hrL1tE1w48P5s7lLsUAMFoERRk5tAiTJXNKcy7ZyRdSFqxC35jUPWVoWmOoQyuXe9XP6GzsbMw6Ap0kdIAhCV8gJfNQZ05nLudLMdm604oyCW/QHQCPzKE+g2/BzZUOj3GPxHyOHo2W399pfjIyqXQ8QepOMqPzsRHFpJnrxuXRnxw7KCQBgvdjTjazzJ9Mit5vglPmOLXN0jp+VFB1sNeCsT+k2UP3djHfEHNBo4OhzOepkK9jkfDTfm9nmk3RbLE/DbSU7rY+q2mYvA9OW3qaI70ndfqitwcHBudH8bX9KBU3rar9Q22nKsf8w+2RUKwr70LutrfLW1+z/N7ZQMY1i5PGQ+uQQVJhAGVsJnd8LAp9xt/Cg+TueLTZVdF8yvBDETK745mAdnx6wh+wztmRrGnQZs8dCxqfJJMS8l1xAEV7tS/xYnMoa7hLr4MeGZvdZOSVa5P60Z4eNFvzR5DqLtj2CHeEw51akHiUstbHaxIdWbS/GDNf39l7Ve6FRrgCD8XbNChlJMQ3OgIzveiocKb6u50KEec00Wd6pKsYjmybpUiZi2FU1M4une4ai56MaDfZ5GaQS32zvYN0e98fh/DOD5dcFxHL2GqKfIQ2w306UVuEoK1mTCzkesD14WzEUTE5tICnPKmM1B2kYYlL7tWuBvUpeST2Vwvac7a15ZKCnrySwtds63NwM4RMUXoVr+QsX6/1fNC6QgSFwD3HsZgujQ3qbsitI6jhPbfLXa3sSMjbePzARyCTrQUbq8gyvCLlzefvOyq8XaxjbkU1VyrBoKwNLsf1aa/4riiD/BMRiK2ak+ZHZ0660c2dPSIdPFKnoInu1tg31trMkHk0IZzYWSHD8yQsamJn+tHG5iJDxorUMys/tQUTOT82IUlRkbHNHeEkCYcJvRvFozMxS0e12z4PJCtJ+wJYNrlVWsUZuoIvTKk6ZNE2FTKZkxJ0Z7O8LapVWkpTuY03wyVDRsGVoii8H5Lj1JNTydbjKfGONr0/7dQBJs9tNatVtcvL9T4zowyGcHLQekeTUK5uMPzSBElyvkgG6XuIbmzPajI8wtkTyE0nkJCDecrGmBN8rElxf+gnySK8AQSBU40NwaDzwSGvLnLGH/WNs7eGZpeWLFfG3brR+rsEcn8LO5f63CUiF7suPzthWzzONlVPvHsUTqbuSX7vWSeI4vyUzC6scCo04dDzawIfSl2o/KwFCV4fHzfSEM2asIhb44vCea+2QmcgF/XyoLQ4wk9H6HgMbMxv5H7o4t3+guSSWtK0NF8LP+9QWMhCQzcApCkn0hMVhmsfW5TUKK73eDAmsjAKqzeLNDij07aJ7QIUpVia2rO2c6lYrZQizznwj/GiJPKBpK7ozKg1fO/lkwDCxKMtbZEm2HQ/wobRbgKmGEH9/+D1fi8HwblK5RgNTrrPZDKwFnRUYJFGNvdC1kg9E/WSWUctzW8Z4AgGHZ5Vlh+0tYChvHHaGgdZ2nesy1ht2Ey3deLSuUmkDHRRSaZSuZtWz9qeMY7b2kPtcU7ya1jnxXAXBG9LbqzE35ml5kr9zcIKPkb409EE9WjWns9entYs0fGByQrDDlRzdLOfk/5x2Z3CDcEJlC3Ggmk5ruYZsaZEB7crdpqRd9J20KX2dOL9eIP0pVaXd4o+U9X+wm32e3Fz6jG4MC/bqEJN4WB5sz01A4ml5Do9HcZKupswKdlHCdYaTlrHl7ulZRWpbcm0e1gprDPQxEHa467sDvTANMH+snuMG7ExxrT37+6e4OPBCQNzsgJOdvlbMRvF4ULL/UXvOEuZQtcyBaPiI03S0JwHuT1lmXm3h/quMdhgki4ofBtKlHRwLhIl2cse1XmHx5GEG8yObiIrvEOmQxyc6lQnVo4pg3jtR1lACP7A5oPf3bc7IElsA4LD1hmLXXyvXRTa4ZcjK+yvVZS6Ae8yx4sdWjFh0gUkiMPhuMs20/WerR9bTqTSejzerJrUMrd8GEZqKHUjyttAEyoJC81y3J9yhRO2fbqxt9qDpy72WTnZOYdurncjLVSDt7fUSBeYKJaSBD9MLHSZ+ToQxdYtRcZgGmyyDC2PNjypF5KlBgG3g+aOfUAb/WwFrOVto3C2xWoUCXOmNAsGMm3YYQ58sWFsotj1JIqtmchQhilicG37QAgkvZiXQ6GhoVa6x/sFQ/WNf7laJN3SYoocHTbNkTzwjlhWDZsU4oV5Lsrdba3sspTm89itI3wsH7F5uqjO1aRg825KVxq7bXD13tNcvbUvMpMMou1aI1sI46DLJ0o+6yzLBJo0bEXeqVomqzU90/Z365bcodEWHhaMQHFdz/fqfPOpwQ9wvrc8bJfN20YlkWS21G1ni3OSJBzE5VHE39QWYxSVR/GdwhV+MDrqlmH0ZkrFyq+vVwnCjrMWhjq9VQnJmJzgYFg7j22n0dtv0mkgzzn1oEerExL84tNQEve7XFB3eVzL9mk86WL6EPRroaIe3522tk/W62g76RtdT4QGAGw30FB+XWFse2AsPWBBTjN09mLBxjSONeboqVYe6yS1Drlu+paDClvdJjSu4Mi1Ogj9lffZ7ezPs1N6ctreYOOahs0tk719bAtFICbrHTQU94tb8FctvbltLrUCk6vtFt5R/A6duVG3Dh2inoTMzEWCuSku65rS1jMIdo1OrhLrEhTc61MRrs22bhLyKnJbFzlvD4myYcPydvFhM9LX9uQa2r2P0X3e6ayh7pHLBXucGcNFHqdr9zicC5HL2kBDGl66t4mic7Jtn5w5161K3iJz7FKP490krydJI29OKh3mVqOjGeUZ+Z6Zc2uJ8eVK5IcIVFTXjbvvhg08IADbHQ/gf1pZuEbg7/ORy+46SsXSdHusuR2+4R7q9SbHKsrWUt9mZey0sR7k0vl2tGWt0dPz5HDkA1L22EFgi9bSrXZum1NxUOHUG+36iE1pcnYS/qIFerA/ZHp74hrsNpON1diTsC0ls9kdcvtoJN6pg1E/vGmJercjv7ZqVEjUG21d9YLK5yYu46RH6HWJzRuel5kKLvmeHoKJKIxL1xKtSD/Ozv0uXZRbJlTXcDwXjFpxtq49mM2edEmFQ6RC0a8pfto6pOtEx/rGovH8eDAOxTdDrKm4qZ8aGz2IUWs4Z16N5kep+3g+GIj3SKaopCwDb7EDotoeyu0husg8DSt1ZrIqYJnSnabO1vjAFLXZ5tbMTaBoaNmpvWw53gv2cpM3zOVEooKAD6DwQmhRiSrD2e2wXhesUticWHS7VpC7uNfpjXPi71dlJ+HBleY74Xp1hqrXQeqZ85qRUgtvk6a3kvZmMjLYbw7SNL+CxACfL1uJ0E9tlZqdM+oudY2EwpcvlmiZeWFjmoM2AMkQ+3WtJ9W6dVxqd3f5w+Qb8cHdsSKE5ypIVO34SB6DTFlFclw/hP3YMkRAnUIUt5STypTpQy8CaVPpbOcqar3bsOM8eajeljkXhSlbe3fBcxyB0OBDuZuKRLSLPcAx3XhuWuLKX7z0zAYUktNydUHErTIVbTXgWGXt24kc13RHOlFTdNx+3l2pLjRuritcWfmKqynaj44RrHcWjgVaUCetF+ZL9+FiWMFwUTeqJhzrI4zcBYs5HggrOobuxJNQG4oNDxukOWzUOMqaCySpotoHBxvE5+3pcVDOZFz7d7gTS6EoosplgvOu16W+cdEJukD7HdnaTt7QTG7JMagyQbnWZzrsPBDPGbLilF7RiZ/zXZpVt+u8j9e8VIXUniAuDyXod9BNu7EPziCsx1m3qYm7OBJ1Ba5t7FqZKagHut7FaMZ2nTpMyZ3Dbybul1V9g6+8iByh9IGP0haLd0FkmesQ4lPOQI9Xj+D0Q05umsBEkG7e4fxj8JATbzLGiYFZKqxOMoFoa97M5eI8XvcoEaQ+Wp3Y23lvmPJF3z8Ydt9dBFTqY73D8Di5sUx57naxcLkghwRNPWMI9PwSchsIHekuce5ojBSC3uLIITL3KiwambGz28qLz5iY9Fk42NtLlh7YEsnEq1WWiWkX2W1CmKmwLuuDckm5PSbfhjUV+hjcZP5gxwE63STtjtqdy17SW5BvWjw49INbVswQFULkXWULqjiA5dGddsfEIo1QYD9OtQ3HYsSvcWVaBsijYYbq18O5HR4oTcG5szvlEHun+iPsnDPerpz67Pfs9XwmqO3sjGF+JRydv8rB4aTejqSy2w9hJsWOrzlCrp1rfseVgLWKFny/Ry/3UdyKF9Y8kf22S0B12pdJdLlrR8NuCgqhZvXsEY3sZnctKzecbkyJgKoaNCGifVZdJAD4K4Fy/H6sG5M68VqawHzVlfMhfsQDwkIVMd3wrOlsVc0YYzazw+7a5u0g4uS+8R5UmU0mJl4VznbzgRBsFloLj85u/YuDhQ7XEPyxOyDzuWj1q7yfQq8uunEDQkB1JTpLbY7lxZzYG0Ns7vPx3tX5pc0esbB/NFvO8BmzQDhzMiRtgzVnndZsUMiIYm8gbRUFRjzocIjdH9NugoxK0JtLrm6v1dDyR9igKZJC+KNdIo/ejZrkslHaJGwVip0b94Cg5N6EkX1z2eKn1hl2aIDf1g/+wOg25MuoeTorQcZe8HEjbWSnxSpG5K42mZxVwdcUtRuMTBTxcUY37gFWEaJ4eKBuM7YIrPRFEinzwEOptEu1idYxf2hZ5ypgjGrotwngZHsvsVylmFlb6/vJNpP1cU2gDc6pY7e0tpV+JvE1FLq6vOZASbLGtmHQixh+M7B1Ac+Q3+MFuXZvcHNoxt35si8ed5va7C6bOS/qbVjplxPwqCjdOP16q60hKnwM+RQ+ZnQfGWLNayyaIAbDBvY96GdKYg2ih/0OejTeEUZ7Jr5mLh+Z+XnogTtBmFe4nV+3eZLPSclU+HyHdfeUXx/UOMPwyIV7hzqx8e5szCORxVbhTZNIDfJecoZhugi6k8nw4NM3CxmTUsttUNaJaOOBfLDddBhyn9ec6huMD196BCDjdmoeN05m81bzuXR5wS1HmEKVDeR+YfFyDIqOZVr6jHLAJsho36NXRuztzfZ+m09dsD8jsKjnMFYGVvqY60jprSbBbbGdNpqJY4VAdKMo11mTIjbTFpp9TRmlE+6c38t6eolgKsNGSdhdD7vB0zieJs+wOhWnC7oLT2RCNYZLoylty1tJJKvLdlPmNOuh17NqdyD1NsV9HeVc0UHjUSXpbUDeczpILxJXDBAFY/LxeB00pLjPU8WTWU0lB1M1bE29jOMxC0OAqdbjdAgqvNgQMoqeukvzgMzUjTXRgtlyrLawJyi4geCNhCsIUTuts9buwXqUe4CABLU0mCrHBWmGKZnMQekQhJ4q3x72pQ1ASSvEuHLC2khrLyZz24O4o5kWvqN7vEZ8gDqIXUDAROtEB0giapFwm1QkFINjXFrfkePDPwa1aGLtHsMCfVQka6Nt6gvauZpEHtsgu64nT01hqtAzEkdyvH+4bkLRoQEFELaFTpNFYR4Z9ai2PcC2RUgtZtGnm2SC/L6Ujcc+9J0k3BJSYxDE/UQop9Y/HODZQkSHWY/5/YZtWzcNAbihTpsL33A0vjNvfbaLsOQ6STZf67nC4pc1Qzyih3PE9WlH3jBWv/sqbpS901ytGq9ubNryh6oGeJ25w6y91xojZ6wqD5lqs2eu171Eimm7jcTdYG02Abmm9TLhDBzGamc4GvQoPAalJ4ltxLTwTMZtEemSfc1PozZ1PBFeh+bQJoyCTfzhhI77RozOWr/mG+NWoI4QPNQxvJ0nufFvLeUpWmL0/ugdLch31+2twMOHkaIyIs1e1EPG2Az1jZC4nQZRp3Q3kgJhMr4EsjiqRSSNGxN/xmnFLyPsfis2dagXmbBOOL8pffoyri+8V9NXY3PwtIre4sLlEOqumkfhOKT9dRORCEhD4uZMT1Uq7/sEZGbp4jtRbF8TcuvUVuBrmDatHQX1sinGG0cttbRp76cHcpCafSxfJgDqYHmj0j4c3/QZD+VjFSpyPaVRqvcttHNO+AYaDpXUYLwPGT4o3gWE3UKJB6XI8trmPS/y4shbd00pd4kiUQzK3KWeYDAtOg3ONb1C5j7BvJuqPzjKvT2yi5F2OCTH1VbSHvY8HtpczZTJSuesf+jZrWVROGlGO2fwztP39FW8nAI5qvhgN1aub54vHNQ8EHgYb9JB8ZDxKuU3vFWd0/zA/ZYpxkLsq3R9JYvoqt+RLRqersd7e1VuKaEFaMQ7TArNDI+l18rfkSdJGR9rfn+7CIcgMOpgRM+iJMzHLWJD5gbr8i3aazVUhsjaHKFKthmEvnLmWKX2plRmbZuYl0sFt+s4xCycNLQN81CqnhFDFcrhUYNbPTVQm3YSbDR9o3vE01Y+tui6sxs4PWn6/NhbaDufQyHdajujUmt3LEF2jjk27mX0rKBVzaMi3lO658SFwDZuZLV7x09r0tEvTqydpp0bG7A8lfettDb6+ZLqzKgQmVoc51BEhGDjW5mMF1JT7BX/IWtRLRQHDO+4UWvcGZgxytdZuoNah/XzK+6VeVIJfALb0Va/UPhGPZoOpDoEUV/bKwEnjGGWxBoyLCiXApWRcfc2u8phG0AFfKPTTZfsk8RFMCZ83CF9OGjiwbsHelGLTbk2p4lDblwbVVM6JcXRmdU4l6HT1RDqrLBRSPAbJsQV+BTc4T17cw4yg/HFYabTtSBT53JDMO1IO83DqoiL3x2V2mqzmYOqYF2cT71i+wwjtUTMgABIoYE2YKSej1G/5Y5rBxSij0OwZmt9Op6momOQ9mw+NvrI3x4mEShwrhoKQ5KUV+IEe6bLaYqqy94j935nr92rxu1vRDsokkIKmZ3xCO0HAtOzdRzl8to876g131FdMbg1rR112UL8sInpi+bUsCzrTXRL++hSPIYTUkB6jjhY78vwtu3NLK7SIz+MMIQohhCx5sWrTrVny9UQmMymNaejsHU3R1zr7oFQHRLBJYR5vMSSnPmJbdH0HKaXwBpja892wEB183p58Cpjq146qM3cdULpMfe2FdnuysORm+kmAXzj1I4nJgKxP+LkW1dnutg453WL1rADyf4M30gxuq/Z67A9kMJx30DaFm1avBRxLzrnh1ZInFmz0NAjGz64jurVgBA0UNftzFbmY/u4nRr4ch8yN8CHwoIhbsRRB8HM/fkg+FY3UlhvdrVU67YVIE06pJiCP1qR9/sAQL2bYB46WnGZndLMCJ+6pDxFEhzEUz/W2MZUjEcq5pwGio24cIfuJKxb6Xyp/etti9lnjeSr/jgmkKk8Lk5rEmzBXQtUSzf3BjrGDkt4g2OASIbcGIYrQoXjs4ORjSh0CCT/dDmj21ghi0xarzmIhYu6xtYa7+tCgW6YdT0hJofyyKb1Ead7lP2p3IhsltPtiTC6oQ7nyZR5NUhuIqdEWqmi4SXYm6mVHQ1HXQ+yzZ1uMWI7AN3WZ+5M+NIFboI9dc24WB9tiTyrqN+ZZAjbKTaSfi9sSkRP5COlkwHsZKcwt454csnE49lL/CQ8n9jUkUJ+beCPqLtiJ29TD3UTdylccM1YT+F4F2pHZIQA883W6PG1GIs9oejEGdHljlAyIoi9fq4xTgoPeY1Q/q0coA4fWcst14/8LDP7hKwJ4jqEqpmqzkzDB375txrQDt4YYnZSKB6/1SROrgkXpYK+P58s3LOaTWB61nUwEVnh9bhMDU9pQZyx4FNjNn0+YXJuWLgmbh8u2zz0QlQruUKvug9r58zaJExNDrbkAcVCBzJtuAQixNyslneOAubGNepaPaatgJ8OGXY3/J2YuHir+3Oljqiw8UJZZsLDWDYXjzKtKZBFz3ROiH/SD8fwcL9OsXaR+2vrcOnpkFxOQoQWs9LO/aMKGf7aPFSNs8R5ZNbhEblHan2bt2pmbCvhekPPlbvFGO9wSI/5YAejAOqIGiuMI0bOR/mE3rnZ0+hTLTdV/rDq4WLuKnIq5c2ePjr9naH4s3n1s9uMMJ4150Iy7ivE3DqaOik72Zcm1KXwToTX55s7EfItgcjuVjBAaVtTx4bmYm0Ih6M47ZbZhGXY6g7lc7Oxs3NcnxHpjOtBV5u3a8NUDyXOvJuLKN2+3VyFo+mFYtLJ69GxShjelIcdFl+8Ncv0nSkeNzW19eeLsleJG8g0w+OIUccTn+f9FSnpAWBfmhHnm7s2lXDLxsOG3MhL2Oh9fNPHaGP3O3E+NkGmnq4KiEFyZQbO5pan+fpw2m4r4qx26t66tY+JOCp3JbTQM92yjY/igWbI9GY6xY/6QFgYvinUIRecgy5r0DXvXb4lQyoMN5jHMaAQ34AqNrIwc02wPrvxaDOnUDSAiKot0uuidtLjurLeHAtKiJFZ3wJFnYPeDyi4ANjGubrbtY/mQdoqaN0zjEMXdLUtBbSi7igPCQEltWPFCf6FhflS3WXhoxCjUu5D2852gZ/nj3Hc2M0aVneImLP3NWI/4AxudoMRtO6NNupqS9VVVjs8PMP5YXvtMKbuSc+H+g7R66ODbpOsxL3Ce9CPmPducUk9ptv27OHocb7dcQWX+dQK5ihe6/im6wl36MtLZjzGY5PDeJmm7qkdjhsnBCk5lIfUd9a3uycdhVsrUluT2E7jujubrNR34h2FK4fODKdrrNNgqJ7RJnXmnPx4B98TmaB7Nrnsd57UBwSf6YQmVdk5o/BRmhu5bvKmox9GRDiH/ZzowZpuN+teDzY1CdO6x/NBnWTXUZSuUEZNRwgdaLg5KSNE1Swf36omaU6ngaZH7jASAkwYhKn2D0TFt60zIVEMYcVehTHuHOFclutXALHZue9paN0qVRszBMlrF0jBUW57C7txPPMQjhyHW9A16G3byJuZDxLdsqvQGHL8oiAFaQDg14g+zlTKts28nrrPGWqNR1OmhXrdl/lArm8aBcn1mqTOvVZO1DEnCKpFsfU4a/Vc8SntX87VfK/2QXO4WheWash7fasG9P9q7Tx2qFW2a/0up4vPJSf3YMEi54x0ZZEXOUfJ727+vY/d8u3dLhI1S9QMYzT4iiUVoaxqh2uaos8dFf7NDqjYCUnQbJrVmMpyQkKwzi6mE3MC8RmXekto0h2kzTO70yqCSK2lkfP4auH1TzCPNVOvB9so4UJgx4SJrxYDkG+VDYiTXHpJrfTDMeKn/uKLb6zm2T52qUoyehSYJaLxAsoEXtA813Qw0idg48WhSTHBdZ5+QTPWQO3ul0BysJ8eOgHBX0B/Wl3BmCAnDb8KYqXk9qMV4nBgCEEdq2aiJ9WdQ6QQorfx0AcpTr7j64GnjGXYpL1HJFKKzvjvCBxPVAcjPMfczeAFLAJpB3asL0Vj0oMxv9W8tCEAN07kpoug9onYEPhimFqpK8hpe2gGoY9cmk0KmT3XW593PnJn0yGEoslwkpHnmVUofDtlVZzuZzx9ki5/4vnLAbJTjZBecHKzDbPr/C2+7rcl9EEnKeFWWksBaPuOC1ZeN5Jy48/z5Pwni0vkOrKbcKIbUGtkm33Sp6rPFp+Hexi/ib1yAbJEPSKTH7yNu1pZIcpckaKu1CqrH7RMHxnmgDYnhMPLXcF/dUJ6RIwUSguG2TZ9lv0v/EGTDL8VsUHTsQlZPMfh1a/rTC4L8El4rPvqqEG6VfKh76DQ4fnhtIv8xtD09J15uoeVwKfqVHM72pfahAwXVdlh+7lVxSHaSR5TJvCiwH7Xp5le6SuyGHm5tzhEfSn8bAMrFHB2eQR6YrrymGBiVHKCSupsSMPJ8ci5guD3kKh2BXyvU84b358Vr2TvEFf1VltqBNWL6AmKPspfafgIvOuyBx3fE0nmh+xnjmKDVc6G5wHV3pHyFYiiATomNsRc5+jwPshLhfL7xZuwqYhwNK+MBA6GO8+asORd4NfflmuAccOfs43zbyv8Vd5iiA4YmQYaPJIHYVYq8B6HrZFwW6IWULOAcq+raah+d1Xu1UqGPDxw5qeeW/WWg+FElWU6uelgyYx6rXFAt9t4eum3p2Pi+a7IFQi+C0Au/X7fzTu++Qf76jaovmchER9fnw1qYEPa8HPE7609qMtRAIxvAQOSPQUFscRptcL6Tqdi0rH+HylGK6CzPhXYI+qXFdUVePJPSsa59xhbY3p6nGjPLkn+DeMIAdP3pytHvVfInkQhC7uHULOMvMCtE+oNH+wmQfFmWjjjaKFDUQGU31eG4Rz42d2nw62wrfD8xjTgty/I9Bmn+XQ0wyMsdyoWs4E8Na2Go3xL10YCKabGRjSDuBA2TCtpoG1vuTlxKOBt7CI/J9tqQ+7BTy9CCWTLzudxR4AYD3C3c6S0ee0Ru8waMS/0JjUw058bwtf941WiTI8yk7jgz0QKaBME377fSA01+yhG7mJw0BOuwQPmqVJ1uXcchrGjcQe62apSzRWSzSS+iL9ycVI1hxvol85FczjmTieiJzTLcbXwZH4/cUCNQKABOnBECQQnlhXZVhBoJmzfDdxSbyKLYurcKcrJuVv4KLm/VbtCCbkfX9vsk4yoFVfYAc5u8C1WX2XVBrV57OQK2duM3fftEDt/MeosFfqTr7c77GvF4cDNLZtGakCJVUOdlP2aQT+YRLGwfVMbiSxooW0ybddVq9ZGTLbKH3vzR2MELJeSyAxyMcmKfiUwqZbhVmkUhDpfK/ObhEw1cz42RFY+cnZ+yBboBFNX0B2UenhVxk/xSi8wXmEecRdoMhIPGw6m89k3v5Fv4n8D0ECXfGSPC5JsBjkGHKBLDsKP5yKNkglQv7yW+UZ/BHdoZnS0x3rUg3q0m7Pe4FmMHS1+uy+WZ5dcb4qSJtJnPIjq1+bJcQZLOj5CCJI3sMVm17cb4SKUbSffJf/w54jJX1S/NlYDinx24VluusTquiFleW9WERg6cpGrS90fkwIpuDqNn2+FF6CnV4NyuB1QOJ76DSO/EZ+KpHuWCu8o8c2V2MpR9ebPLxi4spTrpQQoeCuaXLRuioGgnn/tWJIbIPlkJq3POCLjau8Nv2t9HcxsCkyOXpr8cV10KfVvgnq/rvW/GDL287B8IHNQJ9jiHHciRfVLew+vx7ac8ktBXewIaPFSetADVkG6rjq3dTIkQHP+yWfeVvdS3PFuGe2qdTysBqgDa0TMATU1ujL2llf/MUZhmHZnXmrlKbBOnVJRac6gbdpjR9cc6u9mqJc5pCVqclbQjWo0ES5r1I0d0PKWtB2R+K7wcM3LyDHz/NGt3rRp9xo3QjtAcCh2wHCDM4/OyLzeRyWaltIieQHSLL+32+ccYMl8UbjlsD7cfpeUcnWKiJ+aEvXtsqzHpA2F+o6AlLruyJH8MBIecrvWaFIld4MR/Kea16DG1oFjiwRtHl9qE5pRT+QbfZM8ozeQFVvz+J6+FcF4poKCYAAmAbJz1ZxIGulL5hpmyycxgQAkVFMZw5pSRArJEcnFpGGSdIB25fIcbEM619rW/NRkr+aAjQTLRoBrLqpyy2OLUsxmtOUK7mZS56GeokzMj5g2bMOlWOTrexxhEFIxgxhTmE1b3Z3R6XfZ5CTGqhXS/szWfEw2ipg57VZ+QM/xMWTA+/BY4Qe/3fs26lOwKUntr7I+P01qF2F/VqvzSGeBl2XvBF7sArQEJUh1TDeeIEOckqoT90UhC2GIklYcNxkdcb/PwxWEqAsevf38EbfMyPXv2cE+10QOrJuvBEFK1xVn3slnBLFjKZ1/yB7oLfJVVl5xXyQKc6r+PNJtkIGGPZRsXiAA63Lm3hQAzXTBQeUUWU4K5pn4Qd9PyuobIpHw5KJZ17+pKEdd4hBrri9R2lI3NB7CO9DaqTH0Uxh+1dIEfQBbjypp42zo5jCuYwOminJUtMRDYTXgy2bFYW8q7D37NkBfs5VDOQ2bFjf0Gh1mpg4LNaQaF0bRsG0ascPXGIEZVd8rqoBjYwh7jF98a5esb+1Wv4LdemJuG51fZrOGmsq1ktwRQV1DpB9wlJbWchut2xQDD0wOcncR4nYReKZgRwN+jpNrpVgAulIdNHmO0nI2nlYJcRV4ru3hXDfzgOHjSinIvuPWvueaLVSYZV7JDhH6XWR4CSpdj6F2LvZL/kiS1r3CyVw0wJ4nfCo1bMUbA1FdX+tpry7cm8NVPlG6bWw4URlCP9G1qnv9XbBFMXlX3gPtHFhZnW6yzV464ZH3ZJAbEX19MXOV0laIVpOd5uOqTPDYjaWXkffUByUwq/4uXSEzc2ItDnYXr22LCIWEK1DAM/lkYzasZs52OM4ahTAp+YiP23q7dOBTkyQKXMZvAZJRlIswNV6tkrP3vRC4gm1QO/9MoaHH5auG9zqWkciDIpYfYS9U0LicU+sMqB+BE8pWwc58c0l6Ul/+mYQmHjB/cLgpHnEwMGg/5qJcpjJGhllDYn0CswlRpb0hDU+vcF/nfKiaOoZM46HdNcNTuKcx7OKaREui2Y/7m5Olpf7K0Wu/e6yqs5WAeEoHaNDun/b81D1bZYRmD2leUXDIZFiSS0nTj/Y+GjxzUyn2A007RnOa4fMkyQrbPhvlwqc+4Eexv92oVVO/q+dffkNw7E/Wq2svfsB8AflVIOv7Bk7qKCs1DgEQ0ujQX6pVJJj2BcrYk1ET9/j+zUhQK2F1hpwYymj7a1J+hJPucJ0hOna+fG0AhrTj063sXVZIZ33c4HW0fBITTOXbykZABA7nkeZ0Btgefh7lNJ4fZve1mtQ7oB8rZllLqlG+4VCiuNDllecUWngLWREhgOshMEa8klfJdrjsWnY5vTOl/U1SaSMCviY8us48y8T0I+eYxNLh0jDk6ywmWPBZ4GfgeYBgSDiSa27IBlOrEV+I0gV/uDyhtz//Bdo0AfSdWOcOIssTA+Gyd99kKW1f1wdjbQdO7FYj+q0aZaz64UcuzpIf27Dr+6s3qLpW4bZ3OGaSyaRyF0/dK1i9BmbUPLzvPxh7fAl09y90jT56UUJ761mxVhPCzT057Io7pF1g8VWM8A7fHgSjAteE6hed+cls7gx+iNW2lU68XZ/NVqz2BIaeXGeMQG7oyLjD0ZFIB4LokTKUpSjzHg3iyPa1UhIQe3nGNAGldAUotcqwOA6P25ZLfHAn89bdgyFpKQSJvzD3HVp3KEYlJ/+Gcauci9Xldbq7SNwkd3JMgWSGJZ14kS5Mu5fPNb9kEast5wHc0a55e6k57PsDgN5d/RCiZN0zAEDePm2dM1Qk4BQW0AAZLf5JKh1iFInDdswx+NMHkvG2bbXUclYMslolHaRyEaxrFJTJZLlpWyJFL+TJjD3KEPPCJQOGsDR6Tr8ubbp42gKlA4FBuH5MqNw0XtcILP9NB6iDzLdKJnBtNoZh/vFv//iD8vwXbul/5zz9wej8f6P5/A3eGY835JAVf1BFf5By//73VXD/j/j/99/+sWT1G/1vENHfXKW/YD5/Y4j++dd7/9z+hxO13n/TU//w7a7tv5lSf6iUfwL+Nyq0/usqwT9QwDfQXyCof902+Bf56T+S9T/+4iL9i/v0Lvzu4y9e7194JOT/QO9u/vO/AGNgW0dccgAA -->
