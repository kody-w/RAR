---
name: "rar-cat-agent-skills-lookup-dataverse-table"
description: "Search any Microsoft Dataverse table, browse matching records, and drill into full record details \u2014 sourced live via the Dataverse MCP Server."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/lookup_dataverse_table", "rar_sha256": "6525511bf6ee244af3473793a5042254fed4e36052023cb062438af1f3636eb4", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "lookup_dataverse_table_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/lookup-dataverse-table:820c3f0a819ad8f8d3c10770e50445bcc62062724fe13a580eebe147e3bb00c8", "kind": "skill"}, "version": "2.0.0", "author": "Chris Garty", "tags": ["dataverse", "mcp", "data_lookup", "power_platform", "crm"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/lookup_dataverse_table`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `lookup_dataverse_table_agent.py` is
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
