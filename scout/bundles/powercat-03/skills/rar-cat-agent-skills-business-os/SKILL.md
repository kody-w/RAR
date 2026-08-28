---
name: "rar-cat-agent-skills-business-os"
description: "A practical operating system for Copilot Studio that gives agents a consistent way to clarify outcomes, choose the right approach, solve problems, make decisions, plan projects, improve processes, handle incidents, and turn repeatable work into reusable skills. Unlike a standard Copilot experience that relies mainly on the prompt and available context, Business OS adds a structured way of working\u2026"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/business_os", "rar_sha256": "b455d3229e78336c3772968e71167a3aa49c2a131e16710432b069cef3bf77aa", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Matthew James Davis", "tags": ["business", "decision_making", "problem_solving", "project_planning", "process_improvement", "governance", "skill_generation"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/business_os`. The original RAPP
agent is preserved byte-for-byte in `business_os_agent.py` and in the RCI capsule.

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
