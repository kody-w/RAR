---
name: "rar-cowork-cookbook-report-manage-procurement-spend"
description: "Builds a read-only procurement spend summary report from Dynamics 365 F&SCM for a given legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_procurement_spend", "rar_sha256": "729d62226722894e1effd4915a146b13e59f27f8823e2f565803378c6c388a70", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_manage_procurement_spend`. The original RAPP
agent is preserved byte-for-byte in `report_manage_procurement_spend_agent.py` and in the RCI capsule.

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

Manage procurement spend Summary Report — Builds a read-only procurement spend summary report from Dynamics 365 F&SCM for a given legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-procurement-spend
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
    "breakdown_dimensions": {
      "description": "Dimensions for breakdowns, such as department, category, or responsible owner.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report against, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-manage-procurement-spend-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_procurement_spend_agent.py` and embedded as the fenced Python below (sha256 729d62226722894e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_procurement_spend_agent.py` first:

```bash
python3 report_manage_procurement_spend_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_manage_procurement_spend_agent.py   # or on stdin
python3 report_manage_procurement_spend_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage procurement spend Summary Report — Builds a read-only procurement spend summary report from Dynamics 365 F&SCM for a given legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-procurement-spend
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_manage_procurement_spend',
    "version": '3.0.3',
    "display_name": 'Manage procurement spend Summary Report',
    "description": 'Builds a read-only procurement spend summary report from Dynamics 365 F&SCM for a given legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top 10 by value sheets.',
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
        "upstream_slug": 'report-manage-procurement-spend',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-manage-procurement-spend',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c3462b8a7d743d3e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/source-and-contract-goods-and-services/manage-procurement-spend'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/report-manage-procurement-spend', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, such as department, category, or responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-manage-procurement-spend-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where manage procurement spend stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of manage procurement spend for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-manage-procurement-spend-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage procurement spend records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only procurement spend summary report from Dynamics 365 F&SCM for a given legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top 10 by value sheets.', 'example_request': 'Build a procurement spend summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-manage-procurement-spend-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a procurement spend summary report from D365 ERP data with totals, by-dimension breakdowns, and a top-10 list, without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportManageProcurementSpend(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportManageProcurementSpend'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-manage-procurement-spend-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportManageProcurementSpend().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
