---
name: "rar-cat-agent-skills-tool-tracer"
description: "On-demand tool/action trace for Copilot Studio runs (`/special-debug tool-trace` \u2192 `tool_trace.json`)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/tool_tracer", "rar_sha256": "9bdbbbf6039d95cd831a928da5055dd9dec8dd45c1fc63c67142f4c8260c4e84", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Rafael Lopez Alcaraz", "tags": ["transparency", "observability", "debugging", "workflow", "logging", "json", "productivity"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/tool_tracer`. The original RAPP
agent is preserved byte-for-byte in `tool_tracer_agent.py` and in the RCI capsule.

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

Tool Tracer — On-demand tool/action trace for Copilot Studio runs (`/special-debug tool-trace` → `tool_trace.json`).

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a diagnose capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#tool-tracer
  Upstream author: Rafael Lopez Alcaraz
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `tool_tracer_agent.py` and embedded as the fenced Python below (sha256 9bdbbbf6039d95cd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `tool_tracer_agent.py` first:

```bash
python3 tool_tracer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 tool_tracer_agent.py   # or on stdin
python3 tool_tracer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Tool Tracer — On-demand tool/action trace for Copilot Studio runs (`/special-debug tool-trace` → `tool_trace.json`).

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a diagnose capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#tool-tracer
  Upstream author: Rafael Lopez Alcaraz
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/tool_tracer',
    "version": '2.0.0',
    "display_name": 'Tool Tracer',
    "description": 'On-demand tool/action trace for Copilot Studio runs (`/special-debug tool-trace` → `tool_trace.json`).',
    "author": 'Rafael Lopez Alcaraz',
    "tags": ['transparency', 'observability', 'debugging', 'workflow', 'logging', 'json', 'productivity'],
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
        "upstream_slug": 'tool-tracer',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#tool-tracer',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '5fcd9f882c958e11',
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
_SPEC = {'archetype': 'diagnose', 'checks': ['The symptom is recorded separately from any theory about it.', 'A reliable reproduction exists.', 'Causation was demonstrated by toggling it, not inferred from correlation.', 'A regression check now covers the failure.'], 'confidence': 0.6, 'deliverable': 'A diagnosis: observed symptom, reproduction, the boundary that isolated it, demonstrated cause, fix, and the check that pins it.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'environment': 'Optional. Where it happens, and where it does not.', 'subject': 'The symptom — what was observed, not what you think caused it.'}, 'refined_by': 'rules', 'signals': ['tag:observability', 'word:debug'], 'steps': ['Separate the symptom from the theory. Write down only what was observed, with timestamps.', 'Establish a reliable reproduction. An intermittent bug you cannot trigger is not yet being debugged, it is being guessed at.', 'Find the boundary: the nearest case that works and the nearest that fails. The cause lives between them.', 'Bisect that gap, changing one variable at a time.', 'Confirm the cause by making the failure appear and disappear on demand.', 'Fix the cause, then add the check that would have caught it — otherwise it returns under a different symptom.'], 'subject_label': 'symptom to diagnose', 'verb': 'Diagnose'}


class ToolTracer(BasicAgent):
    """Diagnose agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ToolTracer'
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
    print(ToolTracer().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
