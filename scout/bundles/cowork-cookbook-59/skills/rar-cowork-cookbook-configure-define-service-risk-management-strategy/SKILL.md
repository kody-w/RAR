---
name: "rar-cowork-cookbook-configure-define-service-risk-management-strategy"
description: "Applies a bulk service risk management strategy configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and return"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_service_risk_management_strategy", "rar_sha256": "58794d4154246d58636224895bd9b4149da9da0a2074dc1dcab84f826b167bc6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
