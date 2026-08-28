---
name: "rar-cat-agent-skills-agent-red-team"
description: "Adversarial assurance review for agents you own: prompt injection, oversharing, leakage and tool misuse, mapped to fixes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/agent_red_team", "rar_sha256": "280484bfe400b535a392cd1698820ce6f638f1e4b304f00aac2c0ecaf78b7abb", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Marco Zama", "tags": ["copilot_studio", "security", "prompt_injection", "governance", "responsible_ai", "testing", "risk", "assessment"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/agent_red_team`. The original RAPP
agent is preserved byte-for-byte in `agent_red_team_agent.py` and in the RCI capsule.

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

Agent Red Team — Adversarial assurance review for agents you own: prompt injection, oversharing, leakage and tool misuse, mapped to fixes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#agent-red-team
  Upstream author: Marco Zama
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `agent_red_team_agent.py` and embedded as the fenced Python below (sha256 280484bfe400b535…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `agent_red_team_agent.py` first:

```bash
python3 agent_red_team_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 agent_red_team_agent.py   # or on stdin
python3 agent_red_team_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Agent Red Team — Adversarial assurance review for agents you own: prompt injection, oversharing, leakage and tool misuse, mapped to fixes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#agent-red-team
  Upstream author: Marco Zama
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/agent_red_team',
    "version": '2.0.1',
    "display_name": 'Agent Red Team',
    "description": 'Adversarial assurance review for agents you own: prompt injection, oversharing, leakage and tool misuse, mapped to fixes.',
    "author": 'Marco Zama',
    "tags": ['copilot_studio', 'security', 'prompt_injection', 'governance', 'responsible_ai', 'testing', 'risk', 'assessment'],
    "category": 'analysis',
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
        "upstream_slug": 'agent-red-team',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#agent-red-team',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'a8a2bcecd245a7bb',
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.818, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:governance', 'tag:risk', 'tag:security', 'tag:testing', 'word:review'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AgentRedTeam(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AgentRedTeam'
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
    print(AgentRedTeam().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
