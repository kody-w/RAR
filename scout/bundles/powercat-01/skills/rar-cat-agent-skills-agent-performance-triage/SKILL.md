---
name: "rar-cat-agent-skills-agent-performance-triage"
description: "Turn a live agent's analytics and transcripts into a diagnosis and a prioritized improvement backlog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/agent_performance_triage", "rar_sha256": "b4505e9978715a93c24dfb8dbebb89acf753adf6af6bf41a6a862828d41f0096", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Marco Zama", "tags": ["copilot_studio", "analytics", "optimization", "operations", "post_launch", "backlog", "assessment", "monitoring"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `agent_performance_triage_agent.py` and embedded as the fenced Python below (sha256 b4505e9978715a93…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `agent_performance_triage_agent.py` first:

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
    "version": '2.0.0',
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
