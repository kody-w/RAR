---
name: "rar-cowork-cookbook-configure-develop-regulatory-compliance-strategy"
description: "Validates a configuration Excel file of regulatory compliance strategy changes row by row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then applies approved rows and emits a before/after"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_regulatory_compliance_strategy", "rar_sha256": "73e41b24173f16784a5feccab74eae86b12ab70b616470476a109f19a2cb4351", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
