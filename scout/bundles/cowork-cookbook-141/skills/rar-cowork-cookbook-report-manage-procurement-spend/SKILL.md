---
name: "rar-cowork-cookbook-report-manage-procurement-spend"
description: "Builds a read-only procurement spend summary report from Dynamics 365 F&SCM for a given legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_procurement_spend", "rar_sha256": "729d62226722894e1effd4915a146b13e59f27f8823e2f565803378c6c388a70", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
