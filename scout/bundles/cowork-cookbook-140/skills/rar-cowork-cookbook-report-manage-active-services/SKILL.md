---
name: "rar-cowork-cookbook-report-manage-active-services"
description: "Builds a read-only summary report of manage active services activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_active_services", "rar_sha256": "dcd71cc44469342e8b593b3db5c26ac3200cb9b6b710138f08e2217868ad7f87", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_manage_active_services`. The original RAPP
agent is preserved byte-for-byte in `report_manage_active_services_agent.py` and in the RCI capsule.

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

Manage active services Summary Report — Builds a read-only summary report of manage active services activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-active-services
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
      "description": "Name of the Excel workbook to produce, e.g. report-manage-active-services-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_active_services_agent.py` and embedded as the fenced Python below (sha256 dcd71cc44469342e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_active_services_agent.py` first:

```bash
python3 report_manage_active_services_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_manage_active_services_agent.py   # or on stdin
python3 report_manage_active_services_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage active services Summary Report — Builds a read-only summary report of manage active services activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-active-services
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_manage_active_services',
    "version": '3.0.3',
    "display_name": 'Manage active services Summary Report',
    "description": 'Builds a read-only summary report of manage active services activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets.',
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
        "upstream_slug": 'report-manage-active-services',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-manage-active-services',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5a4e6acea0a3c9dc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-service-offerings/manage-active-services'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/report-manage-active-services', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-manage-active-services-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where manage active services stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of manage active services for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-manage-active-services-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage active services records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of manage active services activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': "Build a manage active services summary report for USMF's latest posted period as an Excel workbook.", 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-manage-active-services-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-modify summary of manage active services activity from D365 ERP with totals, dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportManageActiveServices(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportManageActiveServices'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-manage-active-services-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportManageActiveServices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
