---
name: "rar-cowork-cookbook-report-engage-in-conversations-with-customers"
description: "Builds a read-only summary report of customer conversation engagement activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_engage_in_conversations_with_customers", "rar_sha256": "43871b997437209ce79870c7ebac85ad79c6be3dd3031cc89183f739d3161766", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
