---
name: "rar-cat-agent-skills-what-to-use-when"
description: "Routes single-output requests to the best-fit included Microsoft 365 Copilot 1p agents and reserves Cowork for long-running or multi-output work."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/what_to_use_when", "rar_sha256": "ad03b72ad9729dff9de3030e89da9b9ec4e10c326d6a8685d0557e30f5eafacf", "source_kind": "rar-agent", "source_commit": "d16979f79339ed06511e0bc50c363f1286d140c7", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "what_to_use_when_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/what-to-use-when:d784aee25a3988be04119c8bbc898ce3d64262eee64a576d2a1ea2e245d1056b", "kind": "skill"}, "version": "2.0.0", "author": "Gaurav Mahajan", "tags": ["productivity", "automation", "copilot", "routing"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/what_to_use_when`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `what_to_use_when_agent.py` is
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
