---
name: "rar-cat-agent-skills-copilot-agent-advisor"
description: "Tells you which Microsoft 365 / Copilot Studio agent option fits your scenario \u2014 use M365 Copilot as-is, build a standard (declarative) agent, or build a custom (custom engine) agent \u2014 and which Copilot Studio harness (GitHub Copilot, standard, or Copilot chat) to build on."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_agent_advisor", "rar_sha256": "d5cab65242f9c79bd79a21ec4e81f0801c1a64324d0619408d61a25528cbba8d", "source_kind": "rar-agent", "source_commit": "871fe0c337dfb58aec623592c8890c66d9ee5bb0", "version": "2.0.0", "author": "Sandra Boucenna", "tags": ["copilot_studio", "agents", "decision_support", "architecture", "advisor"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/copilot_agent_advisor`. The original RAPP
agent is preserved byte-for-byte in `copilot_agent_advisor_agent.py` and in the RCI capsule.

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

Copilot Agent Advisor — Tells you which Microsoft 365 / Copilot Studio agent option fits your scenario — use M365 Copilot as-is, build a standard (declarative) agent, or build a custom (custom engine) agent — and which Copilot Studio harness (GitHub Copilot, standard, or Copilot chat) to build on.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#copilot-agent-advisor
  Upstream author: Sandra Boucenna
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
    "constraints": {
      "description": "Optional. Hard constraints \u2014 budget, platform, deadline, compliance.",
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
      "description": "What is being designed.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `copilot_agent_advisor_agent.py` and embedded as the fenced Python below (sha256 d5cab65242f9c79b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `copilot_agent_advisor_agent.py` first:

```bash
python3 copilot_agent_advisor_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 copilot_agent_advisor_agent.py   # or on stdin
python3 copilot_agent_advisor_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Copilot Agent Advisor — Tells you which Microsoft 365 / Copilot Studio agent option fits your scenario — use M365 Copilot as-is, build a standard (declarative) agent, or build a custom (custom engine) agent — and which Copilot Studio harness (GitHub Copilot, standard, or Copilot chat) to build on.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#copilot-agent-advisor
  Upstream author: Sandra Boucenna
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/copilot_agent_advisor',
    "version": '2.0.0',
    "display_name": 'Copilot Agent Advisor',
    "description": 'Tells you which Microsoft 365 / Copilot Studio agent option fits your scenario — use M365 Copilot as-is, build a standard (declarative) agent, or build a custom (custom engine) agent — and which Copilot Studio harness (GitHub Copilot, standard, or Copilot chat) to build on.',
    "author": 'Sandra Boucenna',
    "tags": ['copilot_studio', 'agents', 'decision_support', 'architecture', 'advisor'],
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
        "upstream_slug": 'copilot-agent-advisor',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#copilot-agent-advisor',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'b04c9390fef8539e',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Copilot Studio', 'Scout'],
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
_SPEC = {'archetype': 'design', 'checks': ['Constraints are written down and the design respects them.', 'At least two options were genuinely considered.', 'The trade-off accepted is stated explicitly.', 'The riskiest assumption has a cheap test attached.'], 'confidence': 0.5, 'deliverable': 'A design record: constraints, options considered, the choice, the trade-off accepted, and the first thing to de-risk.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'constraints': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'subject': 'What is being designed.'}, 'refined_by': 'rules', 'signals': ['tag:architecture'], 'steps': ['Write the constraints down first. A design produced before the constraints are known is a preference.', 'State the success condition in terms someone else could measure without you present.', 'Produce at least two genuinely different approaches; a single option is a decision already made, not a design.', 'Compare them against the constraints, and name what each one gives up. Every design gives something up.', 'Choose, and record why the rejected options were rejected — that record is what survives the next reorganisation.', 'Identify the riskiest assumption and the cheapest way to test it before committing.'], 'subject_label': 'thing being designed', 'verb': 'Design'}


class CopilotAgentAdvisor(BasicAgent):
    """Design agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CopilotAgentAdvisor'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'constraints': {'description': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being designed.', 'type': 'string'}},
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
    print(CopilotAgentAdvisor().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
