---
name: "rar-cat-agent-skills-mct-excellence-iq"
description: "An AI-powered Instructional Intelligence Skill that helps Microsoft Certified Trainers design, deliver, assess, localize, and continuously improve world-class Microsoft learning experiences across Azure, Business Applications, Data & AI, Modern Work, and Security."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/mct_excellence_iq", "rar_sha256": "1b62ce1f0c3641b283c403b6a6c3146f554f5222346d9d7a2d127ea6bdc61875", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Faride Ilanda", "tags": ["mct", "instructional_intelligence", "microsoft_learning", "courseware", "microsoft_learn", "azure", "business_applications", "data_ai"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `mct_excellence_iq_agent.py` and embedded as the fenced Python below (sha256 1b62ce1f0c3641b2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `mct_excellence_iq_agent.py` first:

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
    "version": '2.0.0',
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
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

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

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
