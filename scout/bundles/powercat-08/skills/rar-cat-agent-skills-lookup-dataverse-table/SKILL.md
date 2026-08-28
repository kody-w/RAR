---
name: "rar-cat-agent-skills-lookup-dataverse-table"
description: "Search any Microsoft Dataverse table, browse matching records, and drill into full record details \u2014 sourced live via the Dataverse MCP Server."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/lookup_dataverse_table", "rar_sha256": "6525511bf6ee244af3473793a5042254fed4e36052023cb062438af1f3636eb4", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Chris Garty", "tags": ["dataverse", "mcp", "data_lookup", "power_platform", "crm"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/lookup_dataverse_table`. The original RAPP
agent is preserved byte-for-byte in `lookup_dataverse_table_agent.py` and in the RCI capsule.

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

Dataverse Table Lookup — Search any Microsoft Dataverse table, browse matching records, and drill into full record details — sourced live via the Dataverse MCP Server.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#lookup-dataverse-table
  Upstream author: Chris Garty
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `lookup_dataverse_table_agent.py` and embedded as the fenced Python below (sha256 6525511bf6ee244a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `lookup_dataverse_table_agent.py` first:

```bash
python3 lookup_dataverse_table_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 lookup_dataverse_table_agent.py   # or on stdin
python3 lookup_dataverse_table_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Dataverse Table Lookup — Search any Microsoft Dataverse table, browse matching records, and drill into full record details — sourced live via the Dataverse MCP Server.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#lookup-dataverse-table
  Upstream author: Chris Garty
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/lookup_dataverse_table',
    "version": '2.0.0',
    "display_name": 'Dataverse Table Lookup',
    "description": 'Search any Microsoft Dataverse table, browse matching records, and drill into full record details — sourced live via the Dataverse MCP Server.',
    "author": 'Chris Garty',
    "tags": ['dataverse', 'mcp', 'data_lookup', 'power_platform', 'crm'],
    "category": 'integrations',
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
        "upstream_slug": 'lookup-dataverse-table',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#lookup-dataverse-table',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '9a79dc859cb36791',
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:mcp'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class LookupDataverseTable(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'LookupDataverseTable'
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
    print(LookupDataverseTable().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
