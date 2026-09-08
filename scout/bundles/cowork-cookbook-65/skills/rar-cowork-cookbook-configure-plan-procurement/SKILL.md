---
name: "rar-cowork-cookbook-configure-plan-procurement"
description: "Applies a bulk plan procurement configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and returns a before/after"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_plan_procurement", "rar_sha256": "5cab0e5f551106b73084ff99da86a415095a06ce2a553bd429919b04db25e84d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
