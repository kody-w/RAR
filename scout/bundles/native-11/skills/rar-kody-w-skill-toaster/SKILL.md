---
name: "rar-kody-w-skill-toaster"
description: "Turns an aggregated third-party skill entry into a real, callable RAPP agent by inferring the capability's shape from its metadata and generating a working procedure for it."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/skill_toaster_agent", "rar_sha256": "b05707e55b486c96363ae170a6ee0c755bc0c5b797b5e7ff9fcb57c9dc86d625", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "skill_toaster_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/skill-toaster:a09d5c3234ff86008313a412c8e10960a4a8f8a2cd405b1f51dd9d9a5f6e98c0", "kind": "skill"}, "author": "Kody Wildfeuer", "tags": ["aggregation", "codegen", "engine", "rules_as_data", "toaster"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/skill_toaster_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `skill_toaster_agent.py` is
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
