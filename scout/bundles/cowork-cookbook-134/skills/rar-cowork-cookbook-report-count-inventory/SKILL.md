---
name: "rar-cowork-cookbook-report-count-inventory"
description: "Builds a read-only count inventory summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_count_inventory", "rar_sha256": "96fa19d64a16f3e8a80640570dced7e8021323a62c307ea654872f839da3256d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_count_inventory`. The original RAPP
agent is preserved byte-for-byte in `report_count_inventory_agent.py` and in the RCI capsule.

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

Count inventory Summary Report — Builds a read-only count inventory summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-count-inventory
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
      "description": "Dimensions for breakdowns, e.g. department, category, responsible owner.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-count-inventory-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_count_inventory_agent.py` and embedded as the fenced Python below (sha256 96fa19d64a16f3e8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_count_inventory_agent.py` first:

```bash
python3 report_count_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_count_inventory_agent.py   # or on stdin
python3 report_count_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Count inventory Summary Report — Builds a read-only count inventory summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-count-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_count_inventory',
    "version": '3.0.3',
    "display_name": 'Count inventory Summary Report',
    "description": 'Builds a read-only count inventory summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-count-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-count-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd3e0f205eeefb8b0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/maintain-inventory-levels/count-inventory'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/report-count-inventory', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-count-inventory-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where count inventory stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of count inventory for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-count-inventory-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads count inventory records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only count inventory summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.', 'example_request': 'Build a count inventory summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-count-inventory-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a count inventory summary with totals, by-dimension breakdowns, and top-10-by-value as an Excel workbook from D365 ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportCountInventory(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportCountInventory'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-count-inventory-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportCountInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
