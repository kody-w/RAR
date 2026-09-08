---
name: "rar-cowork-cookbook-report-develop-supplier-segments"
description: "Builds a read-only supplier segment summary report from Dynamics 365 F&SCM ERP data for a legal entity's most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_supplier_segments", "rar_sha256": "28085cdac678d4092f55444bf4649e5f7823e5f4e9787976ccb2fccb6402650a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
