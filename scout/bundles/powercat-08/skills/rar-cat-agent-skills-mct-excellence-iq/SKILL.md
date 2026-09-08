---
name: "rar-cat-agent-skills-mct-excellence-iq"
description: "An AI-powered Instructional Intelligence Skill that helps Microsoft Certified Trainers design, deliver, assess, localize, and continuously improve world-class Microsoft learning experiences across Azure, Business Applications, Data & AI, Modern Work, and Security."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/mct_excellence_iq", "rar_sha256": "1212f8be9121002c644caf233cc50066c674863d108d1b5111a4768d38e5d5ba", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Faride Ilanda", "tags": ["mct", "instructional_intelligence", "microsoft_learning", "courseware", "microsoft_learn", "azure", "business_applications", "data_ai"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `mct_excellence_iq_agent.py` and embedded as the fenced Python below (sha256 1212f8be9121002c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `mct_excellence_iq_agent.py` first:

```bash
python3 mct_excellence_iq_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 mct_excellence_iq_agent.py   # or on stdin
python3 mct_excellence_iq_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
