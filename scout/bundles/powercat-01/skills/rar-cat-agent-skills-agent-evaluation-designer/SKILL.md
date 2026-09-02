---
name: "rar-cat-agent-skills-agent-evaluation-designer"
description: "Design a rigorous, platform-aware evaluation for an AI agent - define what good looks like, pick the right grading method, build a test set, and turn results into a defensible go/no-go decision."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/agent_evaluation_designer", "rar_sha256": "20b0e309fde16bdfc1a363d270e1aec083d9c00b1a1d7735edd30dff9d6000a2", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "agent_evaluation_designer_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/agent-evaluation-designer:ba57b8c3997f8f73b464f98eeea1eaa24330082833e6c3f893fb8bd4b2684100", "kind": "skill"}, "version": "2.0.0", "author": "James Papadimitriou", "tags": ["evaluation", "testing", "quality_assurance", "go_live", "decision_making"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/agent_evaluation_designer`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `agent_evaluation_designer_agent.py` is
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
