---
name: "rar-cat-agent-skills-copilot-studio-agent-test"
description: "Test a Copilot Studio agent against your own Q&A set and get a graded pass/fail report \u2014 no browser automation."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_studio_agent_test", "rar_sha256": "6f7094123eb0552125abc477d11ace64488fb220132b6687d3b97322dd477ab7", "source_kind": "rar-agent", "source_commit": "d16979f79339ed06511e0bc50c363f1286d140c7", "version": "2.0.0", "author": "Matteo Pagani", "tags": ["copilot_studio", "testing", "evaluation", "quality", "agents", "power_platform"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/copilot_studio_agent_test`. The original RAPP
agent is preserved byte-for-byte in `copilot_studio_agent_test_agent.py` and in the RCI capsule.

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

Copilot Studio Agent Test — Test a Copilot Studio agent against your own Q&A set and get a graded pass/fail report — no browser automation.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#copilot-studio-agent-test
  Upstream author: Matteo Pagani
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `copilot_studio_agent_test_agent.py` and embedded as the fenced Python below (sha256 6f7094123eb05521…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `copilot_studio_agent_test_agent.py` first:

```bash
python3 copilot_studio_agent_test_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 copilot_studio_agent_test_agent.py   # or on stdin
python3 copilot_studio_agent_test_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Copilot Studio Agent Test — Test a Copilot Studio agent against your own Q&A set and get a graded pass/fail report — no browser automation.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#copilot-studio-agent-test
  Upstream author: Matteo Pagani
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/copilot_studio_agent_test',
    "version": '2.0.0',
    "display_name": 'Copilot Studio Agent Test',
    "description": 'Test a Copilot Studio agent against your own Q&A set and get a graded pass/fail report — no browser automation.',
    "author": 'Matteo Pagani',
    "tags": ['copilot_studio', 'testing', 'evaluation', 'quality', 'agents', 'power_platform'],
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
        "upstream_slug": 'copilot-studio-agent-test',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#copilot-studio-agent-test',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'ac86f61bb9663d51',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Scout'],
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.556, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:quality', 'tag:testing', 'word:against'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class CopilotStudioAgentTest(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CopilotStudioAgentTest'
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
    print(CopilotStudioAgentTest().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
