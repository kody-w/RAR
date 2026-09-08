---
name: "rar-cowork-cookbook-report-manage-open-purchases"
description: "Builds a read-only summary report of open purchases from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_open_purchases", "rar_sha256": "58abff8d504971a2a7543b3d5cfad5d9ea7ac229073201770b5e6aa650a5dbe6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_manage_open_purchases`. The original RAPP
agent is preserved byte-for-byte in `report_manage_open_purchases_agent.py` and in the RCI capsule.

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

Manage open purchases Summary Report — Builds a read-only summary report of open purchases from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-open-purchases
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
      "description": "Dynamics 365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-manage-open-purchases-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to report on; defaults to the most recent posted period available in the tenant.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_open_purchases_agent.py` and embedded as the fenced Python below (sha256 58abff8d504971a2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_open_purchases_agent.py` first:

```bash
python3 report_manage_open_purchases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_manage_open_purchases_agent.py   # or on stdin
python3 report_manage_open_purchases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage open purchases Summary Report — Builds a read-only summary report of open purchases from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-open-purchases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_manage_open_purchases',
    "version": '3.0.3',
    "display_name": 'Manage open purchases Summary Report',
    "description": 'Builds a read-only summary report of open purchases from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.',
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
        "upstream_slug": 'report-manage-open-purchases',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-manage-open-purchases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'eda78ef3ec82e5be',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/procure-goods-and-services/manage-open-purchases'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/report-manage-open-purchases', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-manage-open-purchases-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available in the tenant.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where manage open purchases stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of manage open purchases for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-manage-open-purchases-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage open purchases records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of open purchases from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.', 'example_request': 'Build an open purchases summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available in the tenant.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-manage-open-purchases-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an open-purchases summary with totals, by-dimension breakdowns, and a top-10-by-value list exported to Excel, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportManageOpenPurchases(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportManageOpenPurchases'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-manage-open-purchases-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available in the tenant.', 'type': 'string'}},
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
    print(ReportManageOpenPurchases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
