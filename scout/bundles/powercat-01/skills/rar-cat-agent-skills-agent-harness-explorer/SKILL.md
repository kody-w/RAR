---
name: "rar-cat-agent-skills-agent-harness-explorer"
description: "Discover, document, and monitor what the agent harness can do \u2014 Python libraries, tools, MCP servers, and runtime capabilities \u2014 with repeatable, comparable snapshots."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/agent_harness_explorer", "rar_sha256": "77aeeb418357389bf065c769985559925b8f7165557d4f2b63421baa21bcc4b7", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "agent_harness_explorer_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/agent-harness-explorer:73c3d8f12e39626797dcf8f0f7289d5bca3487a96477a8c084ca393022f992e4", "kind": "skill"}, "version": "1.1.0", "author": "Chris Garty and Andrew Hess", "tags": ["diagnostics", "runtime", "python", "capabilities", "snapshots", "scripts"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/agent_harness_explorer`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `agent_harness_explorer_agent.py` is
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

Agent Harness Explorer — Discover, document, and monitor what the agent harness can do — Python libraries, tools, MCP servers, and runtime capabilities — with repeatable, comparable snapshots.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a diagnose capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#agent-harness-explorer
  Upstream author: Chris Garty and Andrew Hess
  Upstream version: 0.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "environment": {
      "description": "Optional. Where it happens, and where it does not.",
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
      "description": "The symptom \u2014 what was observed, not what you think caused it.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `agent_harness_explorer_agent.py` and embedded as the fenced Python below (sha256 77aeeb418357389b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `agent_harness_explorer_agent.py` first:

```bash
python3 agent_harness_explorer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 agent_harness_explorer_agent.py   # or on stdin
python3 agent_harness_explorer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Agent Harness Explorer — Discover, document, and monitor what the agent harness can do — Python libraries, tools, MCP servers, and runtime capabilities — with repeatable, comparable snapshots.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a diagnose capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#agent-harness-explorer
  Upstream author: Chris Garty and Andrew Hess
  Upstream version: 0.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/agent_harness_explorer',
    "version": '1.1.0',
    "display_name": 'Agent Harness Explorer',
    "description": 'Discover, document, and monitor what the agent harness can do — Python libraries, tools, MCP servers, and runtime capabilities — with repeatable, comparable snapshots.',
    "author": 'Chris Garty and Andrew Hess',
    "tags": ['diagnostics', 'runtime', 'python', 'capabilities', 'snapshots', 'scripts'],
    "category": 'devtools',
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
        "upstream_slug": 'agent-harness-explorer',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#agent-harness-explorer',
        "upstream_version": '0.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '61ae6c239cb9c236',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio', 'Cowork', 'Scout'],
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
_SPEC = {'archetype': 'diagnose', 'checks': ['The symptom is recorded separately from any theory about it.', 'A reliable reproduction exists.', 'Causation was demonstrated by toggling it, not inferred from correlation.', 'A regression check now covers the failure.'], 'confidence': 0.571, 'deliverable': 'A diagnosis: observed symptom, reproduction, the boundary that isolated it, demonstrated cause, fix, and the check that pins it.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'environment': 'Optional. Where it happens, and where it does not.', 'subject': 'The symptom — what was observed, not what you think caused it.'}, 'refined_by': 'rules', 'signals': ['tag:diagnostics', 'tag:runtime'], 'steps': ['Separate the symptom from the theory. Write down only what was observed, with timestamps.', 'Establish a reliable reproduction. An intermittent bug you cannot trigger is not yet being debugged, it is being guessed at.', 'Find the boundary: the nearest case that works and the nearest that fails. The cause lives between them.', 'Bisect that gap, changing one variable at a time.', 'Confirm the cause by making the failure appear and disappear on demand.', 'Fix the cause, then add the check that would have caught it — otherwise it returns under a different symptom.'], 'subject_label': 'symptom to diagnose', 'verb': 'Diagnose'}


class AgentHarnessExplorer(BasicAgent):
    """Diagnose agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AgentHarnessExplorer'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'environment': {'description': 'Optional. Where it happens, and where it does not.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The symptom — what was observed, not what you think caused it.', 'type': 'string'}},
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
    print(AgentHarnessExplorer().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
