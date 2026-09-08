---
name: "rar-cowork-cookbook-report-configure-and-manage-mobile-apps-and-devices"
description: "Builds a read-only summary report of configure-and-manage-mobile-apps-and-devices activity from Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_configure_and_manage_mobile_apps_and_devices", "rar_sha256": "855f13c8b6b0d1fb20b930d3fc5b6620361246ba2bf388c9ea24aba454bd18cc", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_configure_and_manage_mobile_apps_and_devices`. The original RAPP
agent is preserved byte-for-byte in `report_configure_and_manage_mobile_apps_and_devices_agent.py` and in the RCI capsule.

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

Configure and manage mobile apps and devices Summary Report — Builds a read-only summary report of configure-and-manage-mobile-apps-and-devices activity from Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-configure-and-manage-mobile-apps-and-devices
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
      "description": "Dimensions for by-dimension breakdowns, such as department, category, or responsible owner.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-configure-and-manage-mobile-apps-and-devices-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_configure_and_manage_mobile_apps_and_devices_agent.py` and embedded as the fenced Python below (sha256 855f13c8b6b0d1fb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_configure_and_manage_mobile_apps_and_devices_agent.py` first:

```bash
python3 report_configure_and_manage_mobile_apps_and_devices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_configure_and_manage_mobile_apps_and_devices_agent.py   # or on stdin
python3 report_configure_and_manage_mobile_apps_and_devices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage mobile apps and devices Summary Report — Builds a read-only summary report of configure-and-manage-mobile-apps-and-devices activity from Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-configure-and-manage-mobile-apps-and-devices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_configure_and_manage_mobile_apps_and_devices',
    "version": '3.0.3',
    "display_name": 'Configure and manage mobile apps and devices Summary Report',
    "description": 'Builds a read-only summary report of configure-and-manage-mobile-apps-and-devices activity from Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-configure-and-manage-mobile-apps-and-devices',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-configure-and-manage-mobile-apps-and-devices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f087610de10b8558',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-mobile-apps-and-devices'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-configure-and-manage-mobile-apps-and-devices', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for by-dimension breakdowns, such as department, category, or responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-configure-and-manage-mobile-apps-and-devices-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where configure and manage mobile apps and devices stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of configure and manage mobile apps and devices for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-configure-and-manage-mobile-apps-and-devices-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads configure and manage mobile apps and devices records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of configure-and-manage-mobile-apps-and-devices activity from Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': "Build a summary report of mobile app and device configuration for USMF's latest posted period as an Excel workbook.", 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-configure-and-manage-mobile-apps-and-devices-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for by-dimension breakdowns, such as department, category, or responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a totals/trends/breakdown report of mobile app and device configuration activity from D365 ERP data for a posted period, as an Excel file.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportConfigureAndManageMobileAppsAndDevices(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportConfigureAndManageMobileAppsAndDevices'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for by-dimension breakdowns, such as department, category, or responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-configure-and-manage-mobile-apps-and-devices-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportConfigureAndManageMobileAppsAndDevices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
