---
name: "rar-cowork-cookbook-report-route-loads"
description: "Builds a read-only route loads summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_route_loads", "rar_sha256": "c7ea746278b74a2953305416988ba976e27da6b0eec9de771f1d42bf32ab3bd9", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_route_loads`. The original RAPP
agent is preserved byte-for-byte in `report_route_loads_agent.py` and in the RCI capsule.

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

Route loads Summary Report — Builds a read-only route loads summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-route-loads
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
      "description": "D365 legal entity to query, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-route-loads-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_route_loads_agent.py` and embedded as the fenced Python below (sha256 c7ea746278b74a29…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_route_loads_agent.py` first:

```bash
python3 report_route_loads_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_route_loads_agent.py   # or on stdin
python3 report_route_loads_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Route loads Summary Report — Builds a read-only route loads summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-route-loads
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_route_loads',
    "version": '3.0.3',
    "display_name": 'Route loads Summary Report',
    "description": 'Builds a read-only route loads summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.',
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
        "upstream_slug": 'report-route-loads',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-route-loads',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '61c05dfc125819bb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-freight-and-transportation/route-loads'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/report-route-loads', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-route-loads-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where route loads stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of route loads for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-route-loads-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads route loads records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only route loads summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.', 'example_request': 'Build a route loads summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-route-loads-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a route loads summary report with totals, dimension breakdowns, and a top-10-by-value list exported to Excel from D365 ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportRouteLoads(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportRouteLoads'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-route-loads-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportRouteLoads().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
