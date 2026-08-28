---
name: "rar-cat-agent-skills-agent-performance-triage"
description: "Turn a live agent's analytics and transcripts into a diagnosis and a prioritized improvement backlog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/agent_performance_triage", "rar_sha256": "4e49cebc4376b3a98e567a12ccd7a0cb1dd6d4464d0d44c0de8e742ecb4356be", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Marco Zama", "tags": ["copilot_studio", "analytics", "optimization", "operations", "post_launch", "backlog", "assessment", "monitoring"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/agent_performance_triage`. The original RAPP
agent is preserved byte-for-byte in `agent_performance_triage_agent.py` and in the RCI capsule.

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

Agent Performance Triage — Turn a live agent's analytics and transcripts into a diagnosis and a prioritized improvement backlog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#agent-performance-triage
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
    "data_source": {
      "description": "Optional. Where the evidence comes from.",
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
      "description": "The question to answer, stated as a question.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `agent_performance_triage_agent.py` and embedded as the fenced Python below (sha256 4e49cebc4376b3a9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `agent_performance_triage_agent.py` first:

```bash
python3 agent_performance_triage_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 agent_performance_triage_agent.py   # or on stdin
python3 agent_performance_triage_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Agent Performance Triage — Turn a live agent's analytics and transcripts into a diagnosis and a prioritized improvement backlog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#agent-performance-triage
  Upstream author: Marco Zama
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/agent_performance_triage',
    "version": '2.0.1',
    "display_name": 'Agent Performance Triage',
    "description": "Turn a live agent's analytics and transcripts into a diagnosis and a prioritized improvement backlog.",
    "author": 'Marco Zama',
    "tags": ['copilot_studio', 'analytics', 'optimization', 'operations', 'post_launch', 'backlog', 'assessment', 'monitoring'],
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
        "upstream_slug": 'agent-performance-triage',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#agent-performance-triage',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '7498e78b8a1f891e',
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
_SPEC = {'archetype': 'analyze', 'checks': ['The question is falsifiable and answered directly.', 'The decision threshold was stated before the result.', 'Missing evidence is named rather than silently excluded.', 'Uncertainty is quantified.'], 'confidence': 0.4, 'deliverable': 'A decision-grade answer: one-sentence verdict, method, evidence, uncertainty, and what would change the conclusion.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'data_source': 'Optional. Where the evidence comes from.', 'subject': 'The question to answer, stated as a question.'}, 'refined_by': 'rules', 'signals': ['tag:assessment'], 'steps': ["Restate the question so it is falsifiable. 'Is X better?' becomes 'Does X reduce Y by more than Z?'", 'Declare in advance what result would change the decision — this is what separates analysis from justification.', 'Identify the evidence available and, explicitly, the evidence that is missing.', 'Compute the comparison, holding the method constant across every option.', 'Quantify uncertainty. A point estimate with no interval invites false confidence.', 'Answer the original question in one sentence, then show the working beneath it.'], 'subject_label': 'question under analysis', 'verb': 'Analyze'}


class AgentPerformanceTriage(BasicAgent):
    """Analyze agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AgentPerformanceTriage'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'data_source': {'description': 'Optional. Where the evidence comes from.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The question to answer, stated as a question.', 'type': 'string'}},
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
    print(AgentPerformanceTriage().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
