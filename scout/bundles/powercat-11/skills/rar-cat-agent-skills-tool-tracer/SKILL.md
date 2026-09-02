---
name: "rar-cat-agent-skills-tool-tracer"
description: "On-demand tool/action trace for Copilot Studio runs (`/special-debug tool-trace` \u2192 `tool_trace.json`)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/tool_tracer", "rar_sha256": "9bdbbbf6039d95cd831a928da5055dd9dec8dd45c1fc63c67142f4c8260c4e84", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "tool_tracer_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/tool-tracer:b18aaae64b6dc0c14360e82d0ce3a0f047984cdb5c8b526016809c51c8a9c622", "kind": "skill"}, "version": "2.0.0", "author": "Rafael Lopez Alcaraz", "tags": ["transparency", "observability", "debugging", "workflow", "logging", "json", "productivity"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/tool_tracer`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `tool_tracer_agent.py` is
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
