---
name: "rar-cat-agent-skills-copilot-agent-advisor"
description: "Tells you which Microsoft 365 / Copilot Studio agent option fits your scenario \u2014 use M365 Copilot as-is, build a standard (declarative) agent, or build a custom (custom engine) agent \u2014 and which Copilot Studio harness (GitHub Copilot, standard, or Copilot chat) to build on."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_agent_advisor", "rar_sha256": "d5cab65242f9c79bd79a21ec4e81f0801c1a64324d0619408d61a25528cbba8d", "source_kind": "rar-agent", "source_commit": "871fe0c337dfb58aec623592c8890c66d9ee5bb0", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "copilot_agent_advisor_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/copilot-agent-advisor:a5a4e6c6a0767532a837967f5d40d1d001fc9c1dca64afa5d9859637317f55a1", "kind": "skill"}, "version": "2.0.0", "author": "Sandra Boucenna", "tags": ["copilot_studio", "agents", "decision_support", "architecture", "advisor"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/copilot_agent_advisor`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `copilot_agent_advisor_agent.py` is
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
