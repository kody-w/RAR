---
name: "rar-cat-agent-skills-business-os"
description: "A practical operating system for Copilot Studio that gives agents a consistent way to clarify outcomes, choose the right approach, solve problems, make decisions, plan projects, improve processes, handle incidents, and turn repeatable work into reusable skills. Unlike a standard Copilot experience that relies mainly on the prompt and available context, Business OS adds a structured way of working\u2026"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/business_os", "rar_sha256": "b455d3229e78336c3772968e71167a3aa49c2a131e16710432b069cef3bf77aa", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "business_os_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/business-os:78be1562549d7da4cf9a015cffa58f8ad36342ba198121ce9ec2dbe2eb8f5396", "kind": "skill"}, "version": "2.0.0", "author": "Matthew James Davis", "tags": ["business", "decision_making", "problem_solving", "project_planning", "process_improvement", "governance", "skill_generation"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/business_os`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `business_os_agent.py` is
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

Business OS — A practical operating system for Copilot Studio that gives agents a consistent way to clarify outcomes, choose the right approach, solve problems, make decisions, plan projects, improve processes, handle incidents, and turn repeatable work into reusable skills. Unlike a standard Copilot experience that relies mainly on the prompt and available context, Business OS adds a structured way of working…

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#business-os
  Upstream author: Matthew James Davis
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `business_os_agent.py` and embedded as the fenced Python below (sha256 b455d3229e78336c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `business_os_agent.py` first:

```bash
python3 business_os_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 business_os_agent.py   # or on stdin
python3 business_os_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Business OS — A practical operating system for Copilot Studio that gives agents a consistent way to clarify outcomes, choose the right approach, solve problems, make decisions, plan projects, improve processes, handle incidents, and turn repeatable work into reusable skills. Unlike a standard Copilot experience that relies mainly on the prompt and available context, Business OS adds a structured way of working…

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#business-os
  Upstream author: Matthew James Davis
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/business_os',
    "version": '2.0.0',
    "display_name": 'Business OS',
    "description": 'A practical operating system for Copilot Studio that gives agents a consistent way to clarify outcomes, choose the right approach, solve problems, make decisions, plan projects, improve processes, handle incidents, and turn repeatable work into reusable skills. Unlike a standard Copilot experience that relies mainly on the prompt and available context, Business OS adds a structured way of working…',
    "author": 'Matthew James Davis',
    "tags": ['business', 'decision_making', 'problem_solving', 'project_planning', 'process_improvement', 'governance', 'skill_generation'],
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
        "upstream_slug": 'business-os',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#business-os',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '0f102cac2f8ea262',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio'],
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.333, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:governance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class BusinessOs(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BusinessOs'
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
    print(BusinessOs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
