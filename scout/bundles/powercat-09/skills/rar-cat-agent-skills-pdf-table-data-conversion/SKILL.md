---
name: "rar-cat-agent-skills-pdf-table-data-conversion"
description: "Extract tables from a PDF document (e.g. contract rebate or pricing schedules) and convert them into a clean, workable Excel spreadsheet or CSV."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/pdf_table_data_conversion", "rar_sha256": "111afc6de615d21bd7a889670fe83fb7a8c062d7eced5a34668f69aad0e6d049", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "pdf_table_data_conversion_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/pdf-table-data-conversion:53186306ec688a18af56abad0783899beac9658c988f013092c59794c50e712f", "kind": "skill"}, "version": "2.0.0", "author": "Lewis Baybutt", "tags": ["documents", "extraction", "pdf", "csv", "xlsx", "tables", "sharepoint"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/pdf_table_data_conversion`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `pdf_table_data_conversion_agent.py` is
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

PDF Table Data Conversion — Extract tables from a PDF document (e.g. contract rebate or pricing schedules) and convert them into a clean, workable Excel spreadsheet or CSV.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a convert capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#pdf-table-data-conversion
  Upstream author: Lewis Baybutt
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
      "description": "The input to convert \u2014 path, URL or payload.",
      "type": "string"
    },
    "target_format": {
      "description": "Optional. The desired output format.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `pdf_table_data_conversion_agent.py` and embedded as the fenced Python below (sha256 111afc6de615d21b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `pdf_table_data_conversion_agent.py` first:

```bash
python3 pdf_table_data_conversion_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 pdf_table_data_conversion_agent.py   # or on stdin
python3 pdf_table_data_conversion_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
PDF Table Data Conversion — Extract tables from a PDF document (e.g. contract rebate or pricing schedules) and convert them into a clean, workable Excel spreadsheet or CSV.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a convert capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#pdf-table-data-conversion
  Upstream author: Lewis Baybutt
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/pdf_table_data_conversion',
    "version": '2.0.0',
    "display_name": 'PDF Table Data Conversion',
    "description": 'Extract tables from a PDF document (e.g. contract rebate or pricing schedules) and convert them into a clean, workable Excel spreadsheet or CSV.',
    "author": 'Lewis Baybutt',
    "tags": ['documents', 'extraction', 'pdf', 'csv', 'xlsx', 'tables', 'sharepoint'],
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
        "upstream_slug": 'pdf-table-data-conversion',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#pdf-table-data-conversion',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'a997eb9d6266624c',
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
_SPEC = {'archetype': 'convert', 'checks': ['Record counts reconcile between input and output.', 'Every unmapped field is listed with its disposition.', 'A round-trip on the sample is lossless, or the loss is documented and intended.', 'The conversion is rerunnable and produces identical output.'], 'confidence': 0.625, 'deliverable': 'Converted output plus a mapping table, an unmapped-field list, and a reconciliation showing nothing was lost silently.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The input to convert — path, URL or payload.', 'target_format': 'Optional. The desired output format.'}, 'refined_by': 'rules', 'signals': ['tag:extraction', 'word:convert', 'word:extract', 'word:into'], 'steps': ['Characterise the input completely before writing any mapping: schema, encoding, size, and every optional field actually present.', 'Define the target contract with the same rigour, including what the consumer requires versus merely accepts.', 'Map field by field, and write down the fields with no counterpart — silent drops are how conversions lose data.', 'Decide the policy for the unmappable: fail, default, or carry through as an extension. Never drop by accident.', 'Convert a representative sample first and diff it against the input on the fields that matter.', 'Run the whole set, then reconcile counts and checksums between input and output.'], 'subject_label': 'input to convert', 'verb': 'Convert'}


class PdfTableDataConversion(BasicAgent):
    """Convert agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PdfTableDataConversion'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The input to convert — path, URL or payload.', 'type': 'string'}, 'target_format': {'description': 'Optional. The desired output format.', 'type': 'string'}},
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
    print(PdfTableDataConversion().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
