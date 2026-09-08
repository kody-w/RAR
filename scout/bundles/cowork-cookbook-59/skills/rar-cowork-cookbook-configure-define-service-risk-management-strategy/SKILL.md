---
name: "rar-cowork-cookbook-configure-define-service-risk-management-strategy"
description: "Applies a bulk service risk management strategy configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and return"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_service_risk_management_strategy", "rar_sha256": "58794d4154246d58636224895bd9b4149da9da0a2074dc1dcab84f826b167bc6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_define_service_risk_management_strategy`. The original RAPP
agent is preserved byte-for-byte in `configure_define_service_risk_management_strategy_agent.py` and in the RCI capsule.

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

Define service risk management strategy Configuration Bulk Setup — Applies a bulk service risk management strategy configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and return

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-service-risk-management-strategy
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
      "description": "Attached Excel file with one row per define service risk management strategy target and the new field values.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_define_service_risk_management_strategy_agent.py` and embedded as the fenced Python below (sha256 58794d4154246d58…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_define_service_risk_management_strategy_agent.py` first:

```bash
python3 configure_define_service_risk_management_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_define_service_risk_management_strategy_agent.py   # or on stdin
python3 configure_define_service_risk_management_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define service risk management strategy Configuration Bulk Setup — Applies a bulk service risk management strategy configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and return

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-service-risk-management-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_define_service_risk_management_strategy',
    "version": '3.0.3',
    "display_name": 'Define service risk management strategy Configuration Bulk Setup',
    "description": 'Applies a bulk service risk management strategy configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and return',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-define-service-risk-management-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-define-service-risk-management-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0e312efec5f22ea6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/define-service-risk-management-strategy'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/configure-define-service-risk-management-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per define service risk management strategy target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for define service risk management strategy, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per define service risk management strategy target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk service risk management strategy configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and return', 'example_request': 'Bulk-update service risk management strategy config in USMF sandbox from this Excel file — validate first and wait for my approval.', 'inputs': [{'description': 'Attached Excel file with one row per define service risk management strategy target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to bulk-update define service risk management strategy config records in D365 F&SCM from a spreadsheet, with dry-run validation and approval before writes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureDefineServiceRiskManagementStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDefineServiceRiskManagementStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per define service risk management strategy target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureDefineServiceRiskManagementStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
