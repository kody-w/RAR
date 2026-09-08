---
name: "rar-cowork-cookbook-report-develop-supplier-segments"
description: "Builds a read-only supplier segment summary report from Dynamics 365 F&SCM ERP data for a legal entity's most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_supplier_segments", "rar_sha256": "28085cdac678d4092f55444bf4649e5f7823e5f4e9787976ccb2fccb6402650a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_develop_supplier_segments`. The original RAPP
agent is preserved byte-for-byte in `report_develop_supplier_segments_agent.py` and in the RCI capsule.

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

Develop supplier segments Summary Report — Builds a read-only supplier segment summary report from Dynamics 365 F&SCM ERP data for a legal entity's most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-supplier-segments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on (e.g. USMF).",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, prompt, plan, checklist, describe.",
      "enum": [
        "run",
        "prompt",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "output_filename": {
      "description": "Name of the Excel workbook to produce, e.g. report-develop-supplier-segments-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to summarize; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_develop_supplier_segments_agent.py` and embedded as the fenced Python below (sha256 28085cdac678d409…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_develop_supplier_segments_agent.py` first:

```bash
python3 report_develop_supplier_segments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_develop_supplier_segments_agent.py   # or on stdin
python3 report_develop_supplier_segments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop supplier segments Summary Report — Builds a read-only supplier segment summary report from Dynamics 365 F&SCM ERP data for a legal entity's most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-supplier-segments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_develop_supplier_segments',
    "version": '3.0.3',
    "display_name": 'Develop supplier segments Summary Report',
    "description": "Builds a read-only supplier segment summary report from Dynamics 365 F&SCM ERP data for a legal entity's most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'report-develop-supplier-segments',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-develop-supplier-segments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5b92e83086c074a3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/develop-procurement-and-sourcing-strategy/develop-supplier-segments'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/report-develop-supplier-segments', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Microsoft 365 Copilot Cowork'],
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on (e.g. USMF).', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-develop-supplier-segments-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where develop supplier segments stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of develop supplier segments for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-develop-supplier-segments-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop supplier segments records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Builds a read-only supplier segment summary report from Dynamics 365 F&SCM ERP data for a legal entity's most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.", 'example_request': 'Build a supplier segment summary report for USMF from D365 with totals and a Top 10 by value sheet.', 'inputs': [{'description': 'D365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-develop-supplier-segments-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a supplier segmentation summary report from Dynamics 365 ERP with totals, dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportDevelopSupplierSegments(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDevelopSupplierSegments'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-develop-supplier-segments-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportDevelopSupplierSegments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
