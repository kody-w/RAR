---
name: "rar-cowork-cookbook-configure-plan-physical-capacity"
description: "Bulk-updates plan physical capacity records in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/after"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_plan_physical_capacity", "rar_sha256": "4b005629ea1ed4fd0f2ed8116fc5cb3a0e77ac34275f826ff7cfdf7fd3b8f9af", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
