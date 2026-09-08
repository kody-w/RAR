---
name: "rar-cowork-cookbook-report-manage-customer-holds"
description: "Generates a read-only customer holds summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_customer_holds", "rar_sha256": "a4ab6f34a4a37eac03e59166bd0aba808bc4c27ee9063044ca3a1f1c99b55bc8", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_manage_customer_holds`. The original RAPP
agent is preserved byte-for-byte in `report_manage_customer_holds_agent.py` and in the RCI capsule.

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

Manage customer holds Summary Report — Generates a read-only customer holds summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-customer-holds
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
      "description": "Name of the Excel workbook to produce, e.g. report-manage-customer-holds-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to report on; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_customer_holds_agent.py` and embedded as the fenced Python below (sha256 a4ab6f34a4a37eac…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_customer_holds_agent.py` first:

```bash
python3 report_manage_customer_holds_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_manage_customer_holds_agent.py   # or on stdin
python3 report_manage_customer_holds_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage customer holds Summary Report — Generates a read-only customer holds summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-customer-holds
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_manage_customer_holds',
    "version": '3.0.3',
    "display_name": 'Manage customer holds Summary Report',
    "description": 'Generates a read-only customer holds summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-manage-customer-holds',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-manage-customer-holds',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '295373ee63d64286',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-credit-and-collections/manage-customer-holds'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/report-manage-customer-holds', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-manage-customer-holds-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where manage customer holds stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of manage customer holds for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-manage-customer-holds-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage customer holds records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only customer holds summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a customer holds summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-manage-customer-holds-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a totals/trends/breakdown report of customer holds activity from D365 ERP, with no data modification.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportManageCustomerHolds(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportManageCustomerHolds'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-manage-customer-holds-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportManageCustomerHolds().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
