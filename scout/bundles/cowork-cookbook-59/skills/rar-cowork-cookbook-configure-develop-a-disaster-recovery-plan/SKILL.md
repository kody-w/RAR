---
name: "rar-cowork-cookbook-configure-develop-a-disaster-recovery-plan"
description: "Reads an attached configuration Excel file of disaster recovery plan changes for a Dynamics 365 F&SCM legal entity, validates every row, returns a validation workbook, and after your approval applies changes with a befor"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_a_disaster_recovery_plan", "rar_sha256": "0e89dc5b0401f752cf0696ee5b0038b296fc893267ee41a04ab98b9980d72127", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
