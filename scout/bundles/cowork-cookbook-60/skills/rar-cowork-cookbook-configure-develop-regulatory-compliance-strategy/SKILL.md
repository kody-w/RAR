---
name: "rar-cowork-cookbook-configure-develop-regulatory-compliance-strategy"
description: "Validates a configuration Excel file of regulatory compliance strategy changes row by row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then applies approved rows and emits a before/after"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_regulatory_compliance_strategy", "rar_sha256": "73e41b24173f16784a5feccab74eae86b12ab70b616470476a109f19a2cb4351", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_develop_regulatory_compliance_strategy`. The original RAPP
agent is preserved byte-for-byte in `configure_develop_regulatory_compliance_strategy_agent.py` and in the RCI capsule.

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

Develop regulatory compliance strategy Configuration Bulk Setup — Validates a configuration Excel file of regulatory compliance strategy changes row by row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then applies approved rows and emits a before/after

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-regulatory-compliance-strategy
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
      "description": "Explicit user approval after reviewing the validation workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_file": {
      "description": "Excel file with one row per target record and the new field values to apply.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Target D365 environment, sandbox or production.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (default USMF; use sandbox first).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_develop_regulatory_compliance_strategy_agent.py` and embedded as the fenced Python below (sha256 73e41b24173f1678…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_develop_regulatory_compliance_strategy_agent.py` first:

```bash
python3 configure_develop_regulatory_compliance_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_develop_regulatory_compliance_strategy_agent.py   # or on stdin
python3 configure_develop_regulatory_compliance_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop regulatory compliance strategy Configuration Bulk Setup — Validates a configuration Excel file of regulatory compliance strategy changes row by row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then applies approved rows and emits a before/after

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-regulatory-compliance-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_develop_regulatory_compliance_strategy',
    "version": '3.0.3',
    "display_name": 'Develop regulatory compliance strategy Configuration Bulk Setup',
    "description": 'Validates a configuration Excel file of regulatory compliance strategy changes row by row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then applies approved rows and emits a before/after',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-develop-regulatory-compliance-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-develop-regulatory-compliance-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fdcc85ff2d5ebeec',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/develop-marketing-strategy/develop-regulatory-compliance-strategy'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/configure-develop-regulatory-compliance-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'configuration_file': 'Excel file with one row per target record and the new field values to apply.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target D365 environment, sandbox or production.', 'legal_entity': 'D365 legal entity to run against (default USMF; use sandbox first).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for develop regulatory compliance strategy, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per develop regulatory compliance strategy target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Validates a configuration Excel file of regulatory compliance strategy changes row by row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then applies approved rows and emits a before/after', 'example_request': 'Run the bulk compliance config update from my attached Excel file against USMF in sandbox and show me the validation results first.', 'inputs': [{'description': 'Excel file with one row per target record and the new field values to apply.', 'name': 'configuration_file'}, {'description': 'D365 legal entity to run against (default USMF; use sandbox first).', 'name': 'legal_entity'}, {'description': 'Target D365 environment, sandbox or production.', 'name': 'environment'}, {'description': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-apply regulatory compliance strategy configuration changes in D365 from a spreadsheet, with dry-run validation and explicit approval before writes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureDevelopRegulatoryComplianceStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDevelopRegulatoryComplianceStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_file': {'description': 'Excel file with one row per target record and the new field values to apply.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target D365 environment, sandbox or production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (default USMF; use sandbox first).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureDevelopRegulatoryComplianceStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
