---
name: "rar-cowork-cookbook-configure-develop-a-disaster-recovery-plan"
description: "Reads an attached configuration Excel file of disaster recovery plan changes for a Dynamics 365 F&SCM legal entity, validates every row, returns a validation workbook, and after your approval applies changes with a befor"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_a_disaster_recovery_plan", "rar_sha256": "0e89dc5b0401f752cf0696ee5b0038b296fc893267ee41a04ab98b9980d72127", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_develop_a_disaster_recovery_plan`. The original RAPP
agent is preserved byte-for-byte in `configure_develop_a_disaster_recovery_plan_agent.py` and in the RCI capsule.

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

Develop a disaster recovery plan Configuration Bulk Setup — Reads an attached configuration Excel file of disaster recovery plan changes for a Dynamics 365 F&SCM legal entity, validates every row, returns a validation workbook, and after your approval applies changes with a befor

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-a-disaster-recovery-plan
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
      "description": "Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per disaster recovery plan target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF; use a sandbox environment first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_develop_a_disaster_recovery_plan_agent.py` and embedded as the fenced Python below (sha256 0e89dc5b0401f752…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_develop_a_disaster_recovery_plan_agent.py` first:

```bash
python3 configure_develop_a_disaster_recovery_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_develop_a_disaster_recovery_plan_agent.py   # or on stdin
python3 configure_develop_a_disaster_recovery_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop a disaster recovery plan Configuration Bulk Setup — Reads an attached configuration Excel file of disaster recovery plan changes for a Dynamics 365 F&SCM legal entity, validates every row, returns a validation workbook, and after your approval applies changes with a befor

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-a-disaster-recovery-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_develop_a_disaster_recovery_plan',
    "version": '3.0.3',
    "display_name": 'Develop a disaster recovery plan Configuration Bulk Setup',
    "description": 'Reads an attached configuration Excel file of disaster recovery plan changes for a Dynamics 365 F&SCM legal entity, validates every row, returns a validation workbook, and after your approval applies changes with a befor',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-develop-a-disaster-recovery-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-develop-a-disaster-recovery-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6dcea09dfb519ff7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/develop-a-disaster-recovery-plan'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-develop-a-disaster-recovery-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per disaster recovery plan target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for develop a disaster recovery plan, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per develop a disaster recovery plan target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached configuration Excel file of disaster recovery plan changes for a Dynamics 365 F&SCM legal entity, validates every row, returns a validation workbook, and after your approval applies changes with a befor', 'example_request': 'Bulk-apply the disaster recovery plan config in this Excel to USMF sandbox — validate first and show me the dry run.', 'inputs': [{'description': 'Attached Excel file with one row per disaster recovery plan target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.', 'name': 'legal_entity'}, {'description': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-apply disaster recovery plan configuration changes in Dynamics 365 F&SCM from a spreadsheet, with dry-run validation and approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureDevelopADisasterRecoveryPlan(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDevelopADisasterRecoveryPlan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per disaster recovery plan target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureDevelopADisasterRecoveryPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
