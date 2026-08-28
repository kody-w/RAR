---
name: "rar-cat-agent-skills-vacation-urgent-forwarder"
description: "A Scout automation installer that, only during a configured vacation window, scans work email and Teams and forwards genuinely urgent items to your personal email."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/vacation_urgent_forwarder", "rar_sha256": "a945ea6ac53c04d6b788b7a61d287b33fed92bc1d34272178e5a7c74c2c66e7e", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Giorgio Ughini", "tags": ["automation", "email", "teams", "out_of_office"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/vacation_urgent_forwarder`. The original RAPP
agent is preserved byte-for-byte in `vacation_urgent_forwarder_agent.py` and in the RCI capsule.

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

Vacation Urgent Forwarder — A Scout automation installer that, only during a configured vacation window, scans work email and Teams and forwards genuinely urgent items to your personal email.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#vacation-urgent-forwarder
  Upstream author: Giorgio Ughini
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `vacation_urgent_forwarder_agent.py` and embedded as the fenced Python below (sha256 a945ea6ac53c04d6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `vacation_urgent_forwarder_agent.py` first:

```bash
python3 vacation_urgent_forwarder_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 vacation_urgent_forwarder_agent.py   # or on stdin
python3 vacation_urgent_forwarder_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Vacation Urgent Forwarder — A Scout automation installer that, only during a configured vacation window, scans work email and Teams and forwards genuinely urgent items to your personal email.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#vacation-urgent-forwarder
  Upstream author: Giorgio Ughini
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/vacation_urgent_forwarder',
    "version": '2.0.0',
    "display_name": 'Vacation Urgent Forwarder',
    "description": 'A Scout automation installer that, only during a configured vacation window, scans work email and Teams and forwards genuinely urgent items to your personal email.',
    "author": 'Giorgio Ughini',
    "tags": ['automation', 'email', 'teams', 'out_of_office'],
    "category": 'productivity',
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
        "upstream_slug": 'vacation-urgent-forwarder',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#vacation-urgent-forwarder',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'e2fd9f42fce2d9e9',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Scout'],
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.636, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'kind:automation'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class VacationUrgentForwarder(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'VacationUrgentForwarder'
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
    print(VacationUrgentForwarder().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
