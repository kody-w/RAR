---
name: "rar-cowork-cookbook-report-engage-in-conversations-with-customers"
description: "Builds a read-only summary report of customer conversation engagement activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_engage_in_conversations_with_customers", "rar_sha256": "43871b997437209ce79870c7ebac85ad79c6be3dd3031cc89183f739d3161766", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_engage_in_conversations_with_customers`. The original RAPP
agent is preserved byte-for-byte in `report_engage_in_conversations_with_customers_agent.py` and in the RCI capsule.

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

Engage in conversations with customers Summary Report — Builds a read-only summary report of customer conversation engagement activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-engage-in-conversations-with-customers
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
      "description": "Name of the Excel workbook to produce, e.g. report-engage-in-conversations-with-customers-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to cover; defaults to the most recent posted period available in the tenant.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_engage_in_conversations_with_customers_agent.py` and embedded as the fenced Python below (sha256 43871b997437209c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_engage_in_conversations_with_customers_agent.py` first:

```bash
python3 report_engage_in_conversations_with_customers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_engage_in_conversations_with_customers_agent.py   # or on stdin
python3 report_engage_in_conversations_with_customers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Engage in conversations with customers Summary Report — Builds a read-only summary report of customer conversation engagement activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-engage-in-conversations-with-customers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_engage_in_conversations_with_customers',
    "version": '3.0.3',
    "display_name": 'Engage in conversations with customers Summary Report',
    "description": 'Builds a read-only summary report of customer conversation engagement activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-engage-in-conversations-with-customers',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-engage-in-conversations-with-customers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'be50ccbe2898d7a5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/engage-in-conversations-with-customers'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/report-engage-in-conversations-with-customers', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-engage-in-conversations-with-customers-2026-05-24.xlsx.', 'period': 'Posted period to cover; defaults to the most recent posted period available in the tenant.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where engage in conversations with customers stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of engage in conversations with customers for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-engage-in-conversations-with-customers-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads engage in conversations with customers records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of customer conversation engagement activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a USMF summary report of engage in conversations with customers for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to cover; defaults to the most recent posted period available in the tenant.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-engage-in-conversations-with-customers-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a totals/trends/breakdown report of engage-in-conversations-with-customers activity from D365 ERP, exported to Excel, with no data changes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportEngageInConversationsWithCustomers(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportEngageInConversationsWithCustomers'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-engage-in-conversations-with-customers-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to cover; defaults to the most recent posted period available in the tenant.', 'type': 'string'}},
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
    print(ReportEngageInConversationsWithCustomers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
