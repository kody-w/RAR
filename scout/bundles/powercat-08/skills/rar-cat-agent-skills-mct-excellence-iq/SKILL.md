---
name: "rar-cat-agent-skills-mct-excellence-iq"
description: "An AI-powered Instructional Intelligence Skill that helps Microsoft Certified Trainers design, deliver, assess, localize, and continuously improve world-class Microsoft learning experiences across Azure, Business Applications, Data & AI, Modern Work, and Security."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/mct_excellence_iq", "rar_sha256": "1b62ce1f0c3641b283c403b6a6c3146f554f5222346d9d7a2d127ea6bdc61875", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "mct_excellence_iq_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/mct-excellence-iq:33e597d62762828b1ecae34d2847ec747c0e418ac9ed5abb90c8cce9d8b13f54", "kind": "skill"}, "version": "2.0.0", "author": "Faride Ilanda", "tags": ["mct", "instructional_intelligence", "microsoft_learning", "courseware", "microsoft_learn", "azure", "business_applications", "data_ai"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/mct_excellence_iq`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `mct_excellence_iq_agent.py` is
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
