---
name: "rar-cowork-cookbook-configure-plan-product-transitions"
description: "Reads an attached Excel file of plan product transition changes for a Dynamics 365 legal entity, validates every row, emits a validation workbook, waits for approval, then applies changes with a before/after confirmation"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_plan_product_transitions", "rar_sha256": "a00133cde6fdcfdb09b50d2cdbddf5e01b7095b37fd72cffc0ee74b0f3785805", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_plan_product_transitions`. The original RAPP
agent is preserved byte-for-byte in `configure_plan_product_transitions_agent.py` and in the RCI capsule.

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

Plan product transitions Configuration Bulk Setup — Reads an attached Excel file of plan product transition changes for a Dynamics 365 legal entity, validates every row, emits a validation workbook, waits for approval, then applies changes with a before/after confirmation

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-product-transitions
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
    "configuration_excel": {
      "description": "Attached Excel file with one row per plan product transitions target and the new field values.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_plan_product_transitions_agent.py` and embedded as the fenced Python below (sha256 a00133cde6fdcfdb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_plan_product_transitions_agent.py` first:

```bash
python3 configure_plan_product_transitions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_plan_product_transitions_agent.py   # or on stdin
python3 configure_plan_product_transitions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan product transitions Configuration Bulk Setup — Reads an attached Excel file of plan product transition changes for a Dynamics 365 legal entity, validates every row, emits a validation workbook, waits for approval, then applies changes with a before/after confirmation

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-product-transitions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_plan_product_transitions',
    "version": '3.0.3',
    "display_name": 'Plan product transitions Configuration Bulk Setup',
    "description": 'Reads an attached Excel file of plan product transition changes for a Dynamics 365 legal entity, validates every row, emits a validation workbook, waits for approval, then applies changes with a before/after confirmation',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-plan-product-transitions',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-plan-product-transitions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f55cfe7f32946a10',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/retire-products/plan-product-transitions'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/configure-plan-product-transitions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the validation workbook, before changes are applied.', 'configuration_excel': 'Attached Excel file with one row per plan product transitions target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for plan product transitions, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per plan product transitions target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached Excel file of plan product transition changes for a Dynamics 365 legal entity, validates every row, emits a validation workbook, waits for approval, then applies changes with a before/after confirmation', 'example_request': 'Bulk-update plan product transitions in USMF sandbox from my attached config spreadsheet — validate first and show me the dry run.', 'inputs': [{'description': 'Attached Excel file with one row per plan product transitions target and the new field values.', 'name': 'configuration_excel'}, {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'name': 'legal_entity'}, {'description': 'Explicit user approval after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-apply plan product transition configuration changes in Dynamics 365 F&SCM from a spreadsheet, with dry-run validation and approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigurePlanProductTransitions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePlanProductTransitions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_excel': {'description': 'Attached Excel file with one row per plan product transitions target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigurePlanProductTransitions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
