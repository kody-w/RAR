---
name: "rar-kody-w-skill-toaster"
description: "Turns an aggregated third-party skill entry into a real, callable RAPP agent by inferring the capability's shape from its metadata and generating a working procedure for it."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/skill_toaster_agent", "rar_sha256": "b05707e55b486c96363ae170a6ee0c755bc0c5b797b5e7ff9fcb57c9dc86d625", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "author": "Kody Wildfeuer", "tags": ["aggregation", "codegen", "engine", "rules_as_data", "toaster"]}
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

It never copies upstream content. It cannot: RAR's aggregation policy is
index-only, and the upstream body is never fetched. What it produces is RAR's own
method for the capability's shape, which is why the output is ours to publish.

Same analysis pattern as the curator reviews: score real metadata, pick from
rules-as-data, optionally let a model sharpen the result, fall back to the rules
when no model is available. Deterministic by default so regeneration is
byte-stable and the drift gate stays meaningful.

  Rules as data     — add an archetype by adding a row; no control flow changes.
  Deterministic     — same input, same toast, forever.
  Never reproduces  — synthesises method from shape, never mirrors upstream text.

Usage:
    python skill_toaster_agent.py                     # describe the engine
    python skill_toaster_agent.py analyze <slug>      # show the inferred shape
    python skill_toaster_agent.py toast <slug>        # show the generated spec

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `skill_toaster_agent.py` and embedded as the fenced Python below (sha256 b05707e55b486c96…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `skill_toaster_agent.py` first:

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

It never copies upstream content. It cannot: RAR's aggregation policy is
index-only, and the upstream body is never fetched. What it produces is RAR's own
method for the capability's shape, which is why the output is ours to publish.

Same analysis pattern as the curator reviews: score real metadata, pick from
rules-as-data, optionally let a model sharpen the result, fall back to the rules
when no model is available. Deterministic by default so regeneration is
byte-stable and the drift gate stays meaningful.

  Rules as data     — add an archetype by adding a row; no control flow changes.
  Deterministic     — same input, same toast, forever.
  Never reproduces  — synthesises method from shape, never mirrors upstream text.

Usage:
    python skill_toaster_agent.py                     # describe the engine
    python skill_toaster_agent.py analyze <slug>      # show the inferred shape
    python skill_toaster_agent.py toast <slug>        # show the generated spec
"""

import json
import os
import re
import sys
from pathlib import Path

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/skill_toaster_agent",
    "version": "1.0.0",
    "display_name": "SkillToaster",
    "description": "Turns an aggregated third-party skill entry into a real, callable RAPP agent by inferring the capability's shape from its metadata and generating a working procedure for it.",
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
                "Never reproduces upstream content — it generates a method for "
                "the capability's shape."
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
                "describe, list_rules, analyze, toast, census, get_state")


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
    print(engine.perform(operation=op, slug=slug))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
