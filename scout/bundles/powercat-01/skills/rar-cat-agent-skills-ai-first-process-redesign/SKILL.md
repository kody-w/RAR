---
name: "rar-cat-agent-skills-ai-first-process-redesign"
description: "Redesign your existing processes with AI-first thinking"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/ai_first_process_redesign", "rar_sha256": "6fcb40c0aefde81d18f04518bfc8826d717720562bf6014f8f96d11677b90bb9", "source_kind": "rar-agent", "source_commit": "d16979f79339ed06511e0bc50c363f1286d140c7", "version": "3.1.1", "author": "Tim Sparks", "tags": ["productivity", "process_improvement", "agentic_workflow"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/ai_first_process_redesign`. The original RAPP
agent is preserved byte-for-byte in `ai_first_process_redesign_agent.py` and in the RCI capsule.

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

AI-First Process Redesign — Redesign your existing processes with AI-first thinking

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#ai-first-process-redesign
  Upstream author: Tim Sparks
  Upstream version: 2.1.1
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
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
      "description": "What to apply this capability to.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ai_first_process_redesign_agent.py` and embedded as the fenced Python below (sha256 6fcb40c0aefde81d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ai_first_process_redesign_agent.py` first:

```bash
python3 ai_first_process_redesign_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ai_first_process_redesign_agent.py   # or on stdin
python3 ai_first_process_redesign_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
AI-First Process Redesign — Redesign your existing processes with AI-first thinking

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#ai-first-process-redesign
  Upstream author: Tim Sparks
  Upstream version: 2.1.1
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/ai_first_process_redesign',
    "version": '3.1.1',
    "display_name": 'AI-First Process Redesign',
    "description": 'Redesign your existing processes with AI-first thinking',
    "author": 'Tim Sparks',
    "tags": ['productivity', 'process_improvement', 'agentic_workflow'],
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
        "upstream_slug": 'ai-first-process-redesign',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#ai-first-process-redesign',
        "upstream_version": '2.1.1',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'ae3bcfad1b711034',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Copilot Studio'],
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
_SPEC = {'archetype': 'general', 'checks': ['The outcome is independently verifiable.', 'Assumptions are written down.', 'The result was checked against the original goal.'], 'confidence': 0.0, 'deliverable': 'A completed pass with the goal, the method, the result, and the assumptions it rests on.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'What to apply this capability to.'}, 'refined_by': 'rules', 'signals': [], 'steps': ['State the goal as an outcome someone else could verify without you.', 'List what you have and what is missing before starting.', 'Do the smallest version end to end, so unknowns surface while they are cheap.', 'Check the result against the goal as stated, not against what turned out to be convenient.', 'Record what would have to be true for this to be wrong.'], 'subject_label': 'task', 'verb': 'Run'}


class AiFirstProcessRedesign(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AiFirstProcessRedesign'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to apply this capability to.', 'type': 'string'}},
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
    print(AiFirstProcessRedesign().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
