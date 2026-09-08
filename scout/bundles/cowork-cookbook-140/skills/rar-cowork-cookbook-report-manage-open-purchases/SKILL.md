---
name: "rar-cowork-cookbook-report-manage-open-purchases"
description: "Builds a read-only summary report of open purchases from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_open_purchases", "rar_sha256": "58abff8d504971a2a7543b3d5cfad5d9ea7ac229073201770b5e6aa650a5dbe6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
