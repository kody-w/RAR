---
name: "rar-cowork-cookbook-report-comply-with-customer-data-regulations"
description: "Builds a read-only summary report of customer data regulation compliance activity from Dynamics 365 F&SCM for a legal entity's most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 she"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_comply_with_customer_data_regulations", "rar_sha256": "014d21469ff85179a3d7b91a81e96b749e3ea62785027286a892d68581fdd12e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_comply_with_customer_data_regulations`. The original RAPP
agent is preserved byte-for-byte in `report_comply_with_customer_data_regulations_agent.py` and in the RCI capsule.

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

Comply with customer data regulations Summary Report — Builds a read-only summary report of customer data regulation compliance activity from Dynamics 365 F&SCM for a legal entity's most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 she

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
  Upstream entry : https://coworkcookbook.com/recipes/report-comply-with-customer-data-regulations
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
      "description": "Dimensions for breakdowns where applicable: department, category, responsible owner.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-comply-with-customer-data-regulations-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to cover; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_comply_with_customer_data_regulations_agent.py` and embedded as the fenced Python below (sha256 014d21469ff85179…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_comply_with_customer_data_regulations_agent.py` first:

```bash
python3 report_comply_with_customer_data_regulations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_comply_with_customer_data_regulations_agent.py   # or on stdin
python3 report_comply_with_customer_data_regulations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Comply with customer data regulations Summary Report — Builds a read-only summary report of customer data regulation compliance activity from Dynamics 365 F&SCM for a legal entity's most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 she

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
  Upstream entry : https://coworkcookbook.com/recipes/report-comply-with-customer-data-regulations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_comply_with_customer_data_regulations',
    "version": '3.0.3',
    "display_name": 'Comply with customer data regulations Summary Report',
    "description": "Builds a read-only summary report of customer data regulation compliance activity from Dynamics 365 F&SCM for a legal entity's most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 she",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-comply-with-customer-data-regulations',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-comply-with-customer-data-regulations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9a6a71f21af0fca4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/comply-with-customer-data-regulations'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/report-comply-with-customer-data-regulations', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-comply-with-customer-data-regulations-2026-05-24.xlsx.', 'period': 'Posted period to cover; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where comply with customer data regulations stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of comply with customer data regulations for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-comply-with-customer-data-regulations-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads comply with customer data regulations records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Builds a read-only summary report of customer data regulation compliance activity from Dynamics 365 F&SCM for a legal entity's most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 she", 'example_request': 'Build a compliance summary report for USMF from D365 for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-comply-with-customer-data-regulations-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write Excel summary of comply-with-customer-data-regulations activity from D365 ERP, with totals, dimension breakdowns, and top 10 by value.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportComplyWithCustomerDataRegulations(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportComplyWithCustomerDataRegulations'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-comply-with-customer-data-regulations-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportComplyWithCustomerDataRegulations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
