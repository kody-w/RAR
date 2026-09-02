---
name: "rar-cat-agent-skills-vacation-urgent-forwarder"
description: "A Scout automation installer that, only during a configured vacation window, scans work email and Teams and forwards genuinely urgent items to your personal email."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/vacation_urgent_forwarder", "rar_sha256": "a945ea6ac53c04d6b788b7a61d287b33fed92bc1d34272178e5a7c74c2c66e7e", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "vacation_urgent_forwarder_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/vacation-urgent-forwarder:2c117443d0b1c6a3d4c18b2ac9f9945de1c429dce77b9f2c469a4ed127fa4c44", "kind": "skill"}, "version": "2.0.0", "author": "Giorgio Ughini", "tags": ["automation", "email", "teams", "out_of_office"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/vacation_urgent_forwarder`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `vacation_urgent_forwarder_agent.py` is
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
