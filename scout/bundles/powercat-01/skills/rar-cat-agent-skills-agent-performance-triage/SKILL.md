---
name: "rar-cat-agent-skills-agent-performance-triage"
description: "Turn a live agent's analytics and transcripts into a diagnosis and a prioritized improvement backlog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/agent_performance_triage", "rar_sha256": "b4505e9978715a93c24dfb8dbebb89acf753adf6af6bf41a6a862828d41f0096", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "agent_performance_triage_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/agent-performance-triage:0ef575b333b2318d9a0648150beac584750f522fabae8dd46d6d88fba4765e95", "kind": "skill"}, "version": "2.0.0", "author": "Marco Zama", "tags": ["copilot_studio", "analytics", "optimization", "operations", "post_launch", "backlog", "assessment", "monitoring"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/agent_performance_triage`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `agent_performance_triage_agent.py` is
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
