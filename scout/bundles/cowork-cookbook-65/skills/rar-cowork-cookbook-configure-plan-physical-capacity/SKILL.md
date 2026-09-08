---
name: "rar-cowork-cookbook-configure-plan-physical-capacity"
description: "Bulk-updates plan physical capacity records in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/after"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_plan_physical_capacity", "rar_sha256": "4b005629ea1ed4fd0f2ed8116fc5cb3a0e77ac34275f826ff7cfdf7fd3b8f9af", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_plan_physical_capacity`. The original RAPP
agent is preserved byte-for-byte in `configure_plan_physical_capacity_agent.py` and in the RCI capsule.

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

Plan physical capacity Configuration Bulk Setup — Bulk-updates plan physical capacity records in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/after

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-physical-capacity
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
    "approval": {
      "description": "Explicit go-ahead after reviewing the validation workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per plan physical capacity target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (e.g. USMF); use a sandbox environment first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_plan_physical_capacity_agent.py` and embedded as the fenced Python below (sha256 4b005629ea1ed4fd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_plan_physical_capacity_agent.py` first:

```bash
python3 configure_plan_physical_capacity_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_plan_physical_capacity_agent.py   # or on stdin
python3 configure_plan_physical_capacity_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan physical capacity Configuration Bulk Setup — Bulk-updates plan physical capacity records in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/after

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-physical-capacity
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_plan_physical_capacity',
    "version": '3.0.3',
    "display_name": 'Plan physical capacity Configuration Bulk Setup',
    "description": 'Bulk-updates plan physical capacity records in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/after',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-plan-physical-capacity',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-plan-physical-capacity',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7537866123cf2649',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/plan-physical-capacity'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/configure-plan-physical-capacity', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per plan physical capacity target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for plan physical capacity, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per plan physical capacity target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Bulk-updates plan physical capacity records in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/after', 'example_request': 'Bulk update plan physical capacity in USMF sandbox from this Excel file - validate first and show me the preview.', 'inputs': [{'description': 'Attached Excel file with one row per plan physical capacity target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to apply many plan physical capacity field changes at once from a spreadsheet, with row-level validation and an approval gate before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigurePlanPhysicalCapacity(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePlanPhysicalCapacity'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per plan physical capacity target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigurePlanPhysicalCapacity().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
