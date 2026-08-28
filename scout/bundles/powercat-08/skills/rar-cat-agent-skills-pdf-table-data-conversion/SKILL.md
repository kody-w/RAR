---
name: "rar-cat-agent-skills-pdf-table-data-conversion"
description: "Extract tables from a PDF document (e.g. contract rebate or pricing schedules) and convert them into a clean, workable Excel spreadsheet or CSV."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/pdf_table_data_conversion", "rar_sha256": "111afc6de615d21bd7a889670fe83fb7a8c062d7eced5a34668f69aad0e6d049", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Lewis Baybutt", "tags": ["documents", "extraction", "pdf", "csv", "xlsx", "tables", "sharepoint"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/pdf_table_data_conversion`. The original RAPP
agent is preserved byte-for-byte in `pdf_table_data_conversion_agent.py` and in the RCI capsule.

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
