---
name: "rar-cat-agent-skills-agent-evaluation-designer"
description: "Design a rigorous, platform-aware evaluation for an AI agent - define what good looks like, pick the right grading method, build a test set, and turn results into a defensible go/no-go decision."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/agent_evaluation_designer", "rar_sha256": "20b0e309fde16bdfc1a363d270e1aec083d9c00b1a1d7735edd30dff9d6000a2", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "James Papadimitriou", "tags": ["evaluation", "testing", "quality_assurance", "go_live", "decision_making"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/agent_evaluation_designer`. The original RAPP
agent is preserved byte-for-byte in `agent_evaluation_designer_agent.py` and in the RCI capsule.

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

Agent Evaluation Designer — Design a rigorous, platform-aware evaluation for an AI agent - define what good looks like, pick the right grading method, build a test set, and turn results into a defensible go/no-go decision.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#agent-evaluation-designer
  Upstream author: James Papadimitriou
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `agent_evaluation_designer_agent.py` and embedded as the fenced Python below (sha256 20b0e309fde16bdf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `agent_evaluation_designer_agent.py` first:

```bash
python3 agent_evaluation_designer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 agent_evaluation_designer_agent.py   # or on stdin
python3 agent_evaluation_designer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Agent Evaluation Designer — Design a rigorous, platform-aware evaluation for an AI agent - define what good looks like, pick the right grading method, build a test set, and turn results into a defensible go/no-go decision.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#agent-evaluation-designer
  Upstream author: James Papadimitriou
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/agent_evaluation_designer',
    "version": '2.0.0',
    "display_name": 'Agent Evaluation Designer',
    "description": 'Design a rigorous, platform-aware evaluation for an AI agent - define what good looks like, pick the right grading method, build a test set, and turn results into a defensible go/no-go decision.',
    "author": 'James Papadimitriou',
    "tags": ['evaluation', 'testing', 'quality_assurance', 'go_live', 'decision_making'],
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
        "upstream_slug": 'agent-evaluation-designer',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#agent-evaluation-designer',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '5932d5f6ea50fb35',
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.308, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:quality_assurance', 'tag:testing'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AgentEvaluationDesigner(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AgentEvaluationDesigner'
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
    print(AgentEvaluationDesigner().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
