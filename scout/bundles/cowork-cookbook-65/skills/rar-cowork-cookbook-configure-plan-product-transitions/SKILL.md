---
name: "rar-cowork-cookbook-configure-plan-product-transitions"
description: "Reads an attached Excel file of plan product transition changes for a Dynamics 365 legal entity, validates every row, emits a validation workbook, waits for approval, then applies changes with a before/after confirmation"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_plan_product_transitions", "rar_sha256": "a00133cde6fdcfdb09b50d2cdbddf5e01b7095b37fd72cffc0ee74b0f3785805", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
