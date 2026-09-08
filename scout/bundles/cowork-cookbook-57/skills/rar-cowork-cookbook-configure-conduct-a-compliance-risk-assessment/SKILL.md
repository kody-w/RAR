---
name: "rar-cowork-cookbook-configure-conduct-a-compliance-risk-assessment"
description: "Reads an attached configuration Excel file of compliance risk assessment targets, validates every row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, and applies changes only after your app"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_conduct_a_compliance_risk_assessment", "rar_sha256": "b75be2898fd11d6422184858a51d1ecf8fb9c6f6c412ccea7f2b7c746add32d1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_conduct_a_compliance_risk_assessment`. The original RAPP
agent is preserved byte-for-byte in `configure_conduct_a_compliance_risk_assessment_agent.py` and in the RCI capsule.

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

Conduct a compliance risk assessment Configuration Bulk Setup — Reads an attached configuration Excel file of compliance risk assessment targets, validates every row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, and applies changes only after your app

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-conduct-a-compliance-risk-assessment
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
      "description": "Explicit confirmation to apply changes after reviewing the validation workbook.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per compliance risk assessment target and the new field values.",
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
      "description": "D365 legal entity to run against (default USMF).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_conduct_a_compliance_risk_assessment_agent.py` and embedded as the fenced Python below (sha256 b75be2898fd11d64…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_conduct_a_compliance_risk_assessment_agent.py` first:

```bash
python3 configure_conduct_a_compliance_risk_assessment_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_conduct_a_compliance_risk_assessment_agent.py   # or on stdin
python3 configure_conduct_a_compliance_risk_assessment_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct a compliance risk assessment Configuration Bulk Setup — Reads an attached configuration Excel file of compliance risk assessment targets, validates every row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, and applies changes only after your app

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-conduct-a-compliance-risk-assessment
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_conduct_a_compliance_risk_assessment',
    "version": '3.0.3',
    "display_name": 'Conduct a compliance risk assessment Configuration Bulk Setup',
    "description": 'Reads an attached configuration Excel file of compliance risk assessment targets, validates every row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, and applies changes only after your app',
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
        "upstream_slug": 'configure-conduct-a-compliance-risk-assessment',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-conduct-a-compliance-risk-assessment',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '714e7ea770d01820',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-compliance/conduct-a-compliance-risk-assessment'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-conduct-a-compliance-risk-assessment', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit confirmation to apply changes after reviewing the validation workbook.', 'configuration_excel_file': 'Attached Excel file with one row per compliance risk assessment target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; sandbox first before production.', 'legal_entity': 'D365 legal entity to run against (default USMF).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for conduct a compliance risk assessment, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per conduct a compliance risk assessment target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached configuration Excel file of compliance risk assessment targets, validates every row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, and applies changes only after your app', 'example_request': 'Bulk-apply my compliance risk assessment config spreadsheet in D365 USMF sandbox — validate first and wait for my approval.', 'inputs': [{'description': 'Attached Excel file with one row per compliance risk assessment target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against (default USMF).', 'name': 'legal_entity'}, {'description': 'Target environment; sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit confirmation to apply changes after reviewing the validation workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-apply configuration changes for a compliance risk assessment in D365 F&SCM from a spreadsheet, with dry-run validation and approval first.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureConductAComplianceRiskAssessment(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureConductAComplianceRiskAssessment'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit confirmation to apply changes after reviewing the validation workbook.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per compliance risk assessment target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureConductAComplianceRiskAssessment().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
