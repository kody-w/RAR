---
name: "rar-cat-agent-skills-mct-excellence-iq"
description: "An AI-powered Instructional Intelligence Skill that helps Microsoft Certified Trainers design, deliver, assess, localize, and continuously improve world-class Microsoft learning experiences across Azure, Business Applications, Data & AI, Modern Work, and Security."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/mct_excellence_iq", "rar_sha256": "5e72826d7dd23ae3dcbfa497f3d675289e23afbf850393f02b749d5e46912e14", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Faride Ilanda", "tags": ["mct", "instructional_intelligence", "microsoft_learning", "courseware", "microsoft_learn", "azure", "business_applications", "data_ai"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/mct_excellence_iq`. The original RAPP
agent is preserved byte-for-byte in `mct_excellence_iq_agent.py` and in the RCI capsule.

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

MCT Excellence IQ — An AI-powered Instructional Intelligence Skill that helps Microsoft Certified Trainers design, deliver, assess, localize, and continuously improve world-class Microsoft learning experiences across Azure, Business Applications, Data & AI, Modern Work, and Security.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#mct-excellence-iq
  Upstream author: Faride Ilanda
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "criteria": {
      "description": "Optional. The standard to review against, if narrower than the default.",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "What is being reviewed \u2014 a file path, URL, document or system.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `mct_excellence_iq_agent.py` and embedded as the fenced Python below (sha256 5e72826d7dd23ae3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `mct_excellence_iq_agent.py` first:

```bash
python3 mct_excellence_iq_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 mct_excellence_iq_agent.py   # or on stdin
python3 mct_excellence_iq_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/mct_excellence_iq_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/mct_excellence_iq_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/mct_excellence_iq/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
MCT Excellence IQ — An AI-powered Instructional Intelligence Skill that helps Microsoft Certified Trainers design, deliver, assess, localize, and continuously improve world-class Microsoft learning experiences across Azure, Business Applications, Data & AI, Modern Work, and Security.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#mct-excellence-iq
  Upstream author: Faride Ilanda
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/mct_excellence_iq',
    "version": '3.0.2',
    "display_name": 'MCT Excellence IQ',
    "description": 'An AI-powered Instructional Intelligence Skill that helps Microsoft Certified Trainers design, deliver, assess, localize, and continuously improve world-class Microsoft learning experiences across Azure, Business Applications, Data & AI, Modern Work, and Security.',
    "author": 'Faride Ilanda',
    "tags": ['mct', 'instructional_intelligence', 'microsoft_learning', 'courseware', 'microsoft_learn', 'azure', 'business_applications', 'data_ai'],
    "category": 'general',
    "quality_tier": "frontier",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cat-agent-skills',
        "source_name": 'CAT Agent Skills',
        "source_url": 'https://microsoft.github.io/cat-agent-skills/',
        "upstream_slug": 'mct-excellence-iq',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#mct-excellence-iq',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'dc7072f847ebe5f9',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio', 'Cowork'],
}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.6, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:security', 'word:assess'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class MctExcellenceIq(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'MctExcellenceIq'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'criteria': {'description': 'Optional. The standard to review against, if narrower than the default.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being reviewed — a file path, URL, document or system.', 'type': 'string'}},
                "required": ["operation"],
            },
        }
        super().__init__(self.name, self.metadata)

    # ── helpers ─────────────────────────────────────────────────────────

    def _subject(self, kwargs):
        for key in ("subject", "input", "target", "topic"):
            value = str(kwargs.get(key) or "").strip()
            if value:
                return value
        return ""

    def _header(self, subject):
        label = subject or f"<no {_SPEC['subject_label']} supplied>"
        return f"{_SPEC['verb']}: {label}"

    def _context(self, kwargs):
        extras = []
        for key in _SPEC["params"]:
            if key == "subject":
                continue
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _plan(self, subject, kwargs):
        lines = [self._header(subject)]
        extras = self._context(kwargs)
        if extras:
            lines += ["", "Context:"] + [f"  {e}" for e in extras]
        lines += ["", "Procedure:"]
        lines += [f"  {i}. {step}" for i, step in enumerate(_SPEC["steps"], 1)]
        if not subject:
            lines += [
                "",
                f"Pass subject=\u0022...\u0022 to bind this procedure to a "
                f"specific {_SPEC['subject_label']}.",
            ]
        return lines

    def _checklist(self):
        return ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]]

    def _provenance(self):
        src = __manifest__["source"]
        lines = [
            f"{__manifest__['display_name']} (v{__manifest__['version']})",
            "",
            __manifest__["description"],
            "",
            f"Capability shape: {_SPEC['archetype']} "
            f"(confidence {_SPEC['confidence']})",
        ]
        platforms = __manifest__.get("platforms") or []
        if platforms:
            lines.append("Runs on:          " + ", ".join(platforms))
        lines += [
            "",
            f"Indexed from:     {src['source_name']}",
            f"Upstream entry:   {src['upstream_url']}",
            f"Upstream author:  {__manifest__['author']}",
            "",
            "RAR indexes this capability and implements its method; the "
            "upstream library remains the authority for its own instructions. "
            "Open the link above to get those from the source.",
        ]
        return lines

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

        if op == "describe":
            return "\n".join(self._provenance())

        if op == "checklist":
            return "\n".join([self._header(subject), ""] + self._checklist())

        if op == "plan":
            return "\n".join(self._plan(subject, kwargs))

        if op == "run":
            lines = self._plan(subject, kwargs)
            lines += [""] + self._checklist()
            lines += ["", f"Deliverable: {_SPEC['deliverable']}"]
            lines += ["", f"Source: {__manifest__['source']['upstream_url']}"]
            return "\n".join(lines)

        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )


if __name__ == "__main__":
    print(MctExcellenceIq().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
