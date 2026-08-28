---
name: "rar-cat-agent-skills-what-to-use-when"
description: "Routes single-output requests to the best-fit included Microsoft 365 Copilot 1p agents and reserves Cowork for long-running or multi-output work."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/what_to_use_when", "rar_sha256": "ad03b72ad9729dff9de3030e89da9b9ec4e10c326d6a8685d0557e30f5eafacf", "source_kind": "rar-agent", "source_commit": "d16979f79339ed06511e0bc50c363f1286d140c7", "version": "2.0.0", "author": "Gaurav Mahajan", "tags": ["productivity", "automation", "copilot", "routing"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/what_to_use_when`. The original RAPP
agent is preserved byte-for-byte in `what_to_use_when_agent.py` and in the RCI capsule.

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

What to Use When — Routes single-output requests to the best-fit included Microsoft 365 Copilot 1p agents and reserves Cowork for long-running or multi-output work.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#what-to-use-when
  Upstream author: Gaurav Mahajan
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
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `what_to_use_when_agent.py` and embedded as the fenced Python below (sha256 ad03b72ad9729dff…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `what_to_use_when_agent.py` first:

```bash
python3 what_to_use_when_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 what_to_use_when_agent.py   # or on stdin
python3 what_to_use_when_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
What to Use When — Routes single-output requests to the best-fit included Microsoft 365 Copilot 1p agents and reserves Cowork for long-running or multi-output work.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#what-to-use-when
  Upstream author: Gaurav Mahajan
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/what_to_use_when',
    "version": '2.0.0',
    "display_name": 'What to Use When',
    "description": 'Routes single-output requests to the best-fit included Microsoft 365 Copilot 1p agents and reserves Cowork for long-running or multi-output work.',
    "author": 'Gaurav Mahajan',
    "tags": ['productivity', 'automation', 'copilot', 'routing'],
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
        "upstream_slug": 'what-to-use-when',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#what-to-use-when',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'd9b46fe1f7df7e9f',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork'],
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class WhatToUseWhen(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'WhatToUseWhen'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
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
    print(WhatToUseWhen().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
