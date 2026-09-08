---
name: "rar-cowork-cookbook-configure-plan-procurement"
description: "Applies a bulk plan procurement configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and returns a before/after"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_plan_procurement", "rar_sha256": "5cab0e5f551106b73084ff99da86a415095a06ce2a553bd429919b04db25e84d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_plan_procurement`. The original RAPP
agent is preserved byte-for-byte in `configure_plan_procurement_agent.py` and in the RCI capsule.

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

Plan procurement Configuration Bulk Setup — Applies a bulk plan procurement configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and returns a before/after

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-procurement
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
      "description": "Explicit user approval after reviewing the validation workbook, before changes are applied.",
      "type": "string"
    },
    "config_workbook": {
      "description": "Excel file with one row per plan procurement target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Target environment; sandbox first before production.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (e.g. USMF).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_plan_procurement_agent.py` and embedded as the fenced Python below (sha256 5cab0e5f551106b7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_plan_procurement_agent.py` first:

```bash
python3 configure_plan_procurement_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_plan_procurement_agent.py   # or on stdin
python3 configure_plan_procurement_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan procurement Configuration Bulk Setup — Applies a bulk plan procurement configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and returns a before/after

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-procurement
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_plan_procurement',
    "version": '3.0.3',
    "display_name": 'Plan procurement Configuration Bulk Setup',
    "description": 'Applies a bulk plan procurement configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and returns a before/after',
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
        "upstream_slug": 'configure-plan-procurement',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-plan-procurement',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '426ecb072ec220db',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/execute-sales-and-operations/plan-procurement'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/configure-plan-procurement', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the validation workbook, before changes are applied.', 'config_workbook': 'Excel file with one row per plan procurement target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; sandbox first before production.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for plan procurement, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per plan procurement target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk plan procurement configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and returns a before/after', 'example_request': 'Bulk-update plan procurement in USMF sandbox from this config spreadsheet — validate first and show me the dry run.', 'inputs': [{'description': 'Excel file with one row per plan procurement target and the new field values.', 'name': 'config_workbook'}, {'description': 'D365 legal entity to run against (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Target environment; sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit user approval after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants to bulk-update plan procurement fields in D365 F&SCM from a spreadsheet, with row validation and an approval gate before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigurePlanProcurement(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePlanProcurement'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'config_workbook': {'description': 'Excel file with one row per plan procurement target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigurePlanProcurement().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
