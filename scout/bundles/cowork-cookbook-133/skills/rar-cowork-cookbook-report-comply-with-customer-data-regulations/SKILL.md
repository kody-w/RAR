---
name: "rar-cowork-cookbook-report-comply-with-customer-data-regulations"
description: "Builds a read-only summary report of customer data regulation compliance activity from Dynamics 365 F&SCM for a legal entity's most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 she"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_comply_with_customer_data_regulations", "rar_sha256": "014d21469ff85179a3d7b91a81e96b749e3ea62785027286a892d68581fdd12e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
