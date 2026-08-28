---
name: "rar-cat-agent-skills-agent-harness-explorer"
description: "Discover, document, and monitor what the agent harness can do \u2014 Python libraries, tools, MCP servers, and runtime capabilities \u2014 with repeatable, comparable snapshots."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/agent_harness_explorer", "rar_sha256": "77aeeb418357389bf065c769985559925b8f7165557d4f2b63421baa21bcc4b7", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "1.1.0", "author": "Chris Garty and Andrew Hess", "tags": ["diagnostics", "runtime", "python", "capabilities", "snapshots", "scripts"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/agent_harness_explorer`. The original RAPP
agent is preserved byte-for-byte in `agent_harness_explorer_agent.py` and in the RCI capsule.

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
