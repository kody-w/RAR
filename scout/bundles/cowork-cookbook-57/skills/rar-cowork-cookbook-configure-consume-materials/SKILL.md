---
name: "rar-cowork-cookbook-configure-consume-materials"
description: "Bulk-applies consume materials configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies changes and returns a before/af"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_consume_materials", "rar_sha256": "270d9b22663d1c09cd717ac69bc8859fa93f1aebea992c301a8d29b51bf8563d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_consume_materials`. The original RAPP
agent is preserved byte-for-byte in `configure_consume_materials_agent.py` and in the RCI capsule.

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

Consume materials Configuration Bulk Setup — Bulk-applies consume materials configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies changes and returns a before/af

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-consume-materials
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
      "description": "Explicit user approval after reviewing the validation/dry-run workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_workbook": {
      "description": "Attached Excel file with one row per consume materials target and the new field values.",
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
      "description": "D365 legal entity to run against, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_consume_materials_agent.py` and embedded as the fenced Python below (sha256 270d9b22663d1c09…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_consume_materials_agent.py` first:

```bash
python3 configure_consume_materials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_consume_materials_agent.py   # or on stdin
python3 configure_consume_materials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Consume materials Configuration Bulk Setup — Bulk-applies consume materials configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies changes and returns a before/af

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-consume-materials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_consume_materials',
    "version": '3.0.3',
    "display_name": 'Consume materials Configuration Bulk Setup',
    "description": 'Bulk-applies consume materials configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies changes and returns a before/af',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-consume-materials',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-consume-materials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c2e75b9110014329',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations/consume-materials'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/configure-consume-materials', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the validation/dry-run workbook, before any changes are applied.', 'configuration_workbook': 'Attached Excel file with one row per consume materials target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; sandbox first before production.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for consume materials, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per consume materials target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Bulk-applies consume materials configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies changes and returns a before/af', 'example_request': 'Bulk update consume materials config in USMF sandbox from my attached Excel — validate first and show me the dry run.', 'inputs': [{'description': 'Attached Excel file with one row per consume materials target and the new field values.', 'name': 'configuration_workbook'}, {'description': 'D365 legal entity to run against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target environment; sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit user approval after reviewing the validation/dry-run workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants to bulk-update consume materials configuration in D365 F&SCM from an Excel file, with row validation, approval gate, and before/after confirmation.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureConsumeMaterials(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureConsumeMaterials'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the validation/dry-run workbook, before any changes are applied.', 'type': 'string'}, 'configuration_workbook': {'description': 'Attached Excel file with one row per consume materials target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureConsumeMaterials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
