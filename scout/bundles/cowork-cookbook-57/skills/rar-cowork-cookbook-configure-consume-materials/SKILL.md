---
name: "rar-cowork-cookbook-configure-consume-materials"
description: "Bulk-applies consume materials configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies changes and returns a before/af"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_consume_materials", "rar_sha256": "270d9b22663d1c09cd717ac69bc8859fa93f1aebea992c301a8d29b51bf8563d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
