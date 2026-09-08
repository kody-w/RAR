---
name: "rar-cat-agent-skills-mct-excellence-iq"
description: "An AI-powered Instructional Intelligence Skill that helps Microsoft Certified Trainers design, deliver, assess, localize, and continuously improve world-class Microsoft learning experiences across Azure, Business Applications, Data & AI, Modern Work, and Security."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/mct_excellence_iq", "rar_sha256": "1212f8be9121002c644caf233cc50066c674863d108d1b5111a4768d38e5d5ba", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Faride Ilanda", "tags": ["mct", "instructional_intelligence", "microsoft_learning", "courseware", "microsoft_learn", "azure", "business_applications", "data_ai"]}
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
