---
name: "rar-cat-agent-skills-pdf-table-data-conversion"
description: "Extract tables from a PDF document (e.g. contract rebate or pricing schedules) and convert them into a clean, workable Excel spreadsheet or CSV."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/pdf_table_data_conversion", "rar_sha256": "c2f7ffba47f5e99eb59ff6fe2453844e159de3085d334c9748b900508c361d04", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Lewis Baybutt", "tags": ["documents", "extraction", "pdf", "csv", "xlsx", "tables", "sharepoint"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `pdf_table_data_conversion_agent.py` and embedded as the fenced Python below (sha256 c2f7ffba47f5e99e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `pdf_table_data_conversion_agent.py` first:

```bash
python3 pdf_table_data_conversion_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 pdf_table_data_conversion_agent.py   # or on stdin
python3 pdf_table_data_conversion_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/pdf_table_data_conversion_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/pdf_table_data_conversion_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/pdf_table_data_conversion/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
