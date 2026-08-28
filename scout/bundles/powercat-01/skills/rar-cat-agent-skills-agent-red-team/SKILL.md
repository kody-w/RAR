---
name: "rar-cat-agent-skills-agent-red-team"
description: "Adversarial assurance review for agents you own: prompt injection, oversharing, leakage and tool misuse, mapped to fixes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/agent_red_team", "rar_sha256": "c39b9166de102478dec3ddc39a765711e471bf743090479f27115e4ab207a879", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Marco Zama", "tags": ["copilot_studio", "security", "prompt_injection", "governance", "responsible_ai", "testing", "risk", "assessment"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `agent_red_team_agent.py` and embedded as the fenced Python below (sha256 c39b9166de102478…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `agent_red_team_agent.py` first:

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
    "version": '2.0.0',
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
