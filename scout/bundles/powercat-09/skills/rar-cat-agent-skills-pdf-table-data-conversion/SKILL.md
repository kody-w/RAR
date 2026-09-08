---
name: "rar-cat-agent-skills-pdf-table-data-conversion"
description: "Extract tables from a PDF document (e.g. contract rebate or pricing schedules) and convert them into a clean, workable Excel spreadsheet or CSV."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/pdf_table_data_conversion", "rar_sha256": "8bcc954b577b135098beb82f05358cd014cd4bc96fd361763859a2762af5c0a3", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Lewis Baybutt", "tags": ["documents", "extraction", "pdf", "csv", "xlsx", "tables", "sharepoint"]}
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
