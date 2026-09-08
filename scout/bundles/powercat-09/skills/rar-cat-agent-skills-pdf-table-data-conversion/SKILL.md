---
name: "rar-cat-agent-skills-pdf-table-data-conversion"
description: "Extract tables from a PDF document (e.g. contract rebate or pricing schedules) and convert them into a clean, workable Excel spreadsheet or CSV."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/pdf_table_data_conversion", "rar_sha256": "8bcc954b577b135098beb82f05358cd014cd4bc96fd361763859a2762af5c0a3", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Lewis Baybutt", "tags": ["documents", "extraction", "pdf", "csv", "xlsx", "tables", "sharepoint"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `pdf_table_data_conversion_agent.py` and embedded as the fenced Python below (sha256 8bcc954b577b1350…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `pdf_table_data_conversion_agent.py` first:

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
    "version": '3.0.2',
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
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

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

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
