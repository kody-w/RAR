---
name: "rar-cat-agent-skills-copilot-studio-agent-test"
description: "Test a Copilot Studio agent against your own Q&A set and get a graded pass/fail report \u2014 no browser automation."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_studio_agent_test", "rar_sha256": "6f7094123eb0552125abc477d11ace64488fb220132b6687d3b97322dd477ab7", "source_kind": "rar-agent", "source_commit": "d16979f79339ed06511e0bc50c363f1286d140c7", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "copilot_studio_agent_test_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/copilot-studio-agent-test:005f16c4e9385fd7d9b75d15d1346e87519a593ae07c4cf23ab619fe3668d27f", "kind": "skill"}, "version": "2.0.0", "author": "Matteo Pagani", "tags": ["copilot_studio", "testing", "evaluation", "quality", "agents", "power_platform"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/copilot_studio_agent_test`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `copilot_studio_agent_test_agent.py` is
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
