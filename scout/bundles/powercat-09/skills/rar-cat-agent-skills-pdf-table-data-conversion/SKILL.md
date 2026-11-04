---
name: "rar-cat-agent-skills-pdf-table-data-conversion"
description: "Extract tables from a PDF document (e.g. contract rebate or pricing schedules) and convert them into a clean, workable Excel spreadsheet or CSV."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/pdf_table_data_conversion", "rar_sha256": "c2f7ffba47f5e99eb59ff6fe2453844e159de3085d334c9748b900508c361d04", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Lewis Baybutt", "tags": ["documents", "extraction", "pdf", "csv", "xlsx", "tables", "sharepoint"]}
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
