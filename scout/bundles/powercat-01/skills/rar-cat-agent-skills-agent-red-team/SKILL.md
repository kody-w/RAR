---
name: "rar-cat-agent-skills-agent-red-team"
description: "Adversarial assurance review for agents you own: prompt injection, oversharing, leakage and tool misuse, mapped to fixes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/agent_red_team", "rar_sha256": "c39b9166de102478dec3ddc39a765711e471bf743090479f27115e4ab207a879", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "agent_red_team_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/agent-red-team:b386c6fba2e42bab0a278a74e587b2c6cff8ddb6b42b46c9afbecc68f3152a52", "kind": "skill"}, "version": "2.0.0", "author": "Marco Zama", "tags": ["copilot_studio", "security", "prompt_injection", "governance", "responsible_ai", "testing", "risk", "assessment"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/agent_red_team`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `agent_red_team_agent.py` is
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
