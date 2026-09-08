---
name: "rar-cowork-cookbook-configure-reconcile-freight"
description: "Reads an attached Excel file of freight reconciliation configuration rows in Dynamics 365 F&SCM, validates every row, emits a validation workbook, waits for approval, then applies changes and emits a before/after confirm"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_reconcile_freight", "rar_sha256": "1329d772496eefc6670998b4f9ab09b4491aec1df2da989b1c1499387af37f21", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_reconcile_freight`. The original RAPP
agent is preserved byte-for-byte in `configure_reconcile_freight_agent.py` and in the RCI capsule.

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

Reconcile freight Configuration Bulk Setup — Reads an attached Excel file of freight reconciliation configuration rows in Dynamics 365 F&SCM, validates every row, emits a validation workbook, waits for approval, then applies changes and emits a before/after confirm

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-reconcile-freight
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
    "configuration_excel": {
      "description": "Attached Excel file with one row per reconcile freight target and the new field values.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_reconcile_freight_agent.py` and embedded as the fenced Python below (sha256 1329d772496eefc6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_reconcile_freight_agent.py` first:

```bash
python3 configure_reconcile_freight_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_reconcile_freight_agent.py   # or on stdin
python3 configure_reconcile_freight_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reconcile freight Configuration Bulk Setup — Reads an attached Excel file of freight reconciliation configuration rows in Dynamics 365 F&SCM, validates every row, emits a validation workbook, waits for approval, then applies changes and emits a before/after confirm

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-reconcile-freight
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_reconcile_freight',
    "version": '3.0.3',
    "display_name": 'Reconcile freight Configuration Bulk Setup',
    "description": 'Reads an attached Excel file of freight reconciliation configuration rows in Dynamics 365 F&SCM, validates every row, emits a validation workbook, waits for approval, then applies changes and emits a before/after confirm',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-reconcile-freight',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-reconcile-freight',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4b6b90436d45dd99',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-freight-and-transportation/reconcile-freight'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/configure-reconcile-freight', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'configuration_excel': 'Attached Excel file with one row per reconcile freight target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; sandbox first before production.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for reconcile freight, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per reconcile freight target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached Excel file of freight reconciliation configuration rows in Dynamics 365 F&SCM, validates every row, emits a validation workbook, waits for approval, then applies changes and emits a before/after confirm', 'example_request': 'Bulk-apply the freight reconciliation config in this Excel to USMF sandbox — validate first and show me the dry run.', 'inputs': [{'description': 'Attached Excel file with one row per reconcile freight target and the new field values.', 'name': 'configuration_excel'}, {'description': 'D365 legal entity to run against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target environment; sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants to bulk-apply freight reconciliation configuration changes in D365 from a spreadsheet, with dry-run validation and explicit approval before writes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureReconcileFreight(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureReconcileFreight'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel': {'description': 'Attached Excel file with one row per reconcile freight target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureReconcileFreight().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adPaSLbmX2HeGzFVdbEtIaHNHTdiJLQhhFYkQOUOl/Z9QRuIuv3fJwW8dlVXdd/uiPk0OGyQlHnyrM9z0spf39yhT+r27fObGbrVQnCLIk3CduFWwWJTX+s2B1917oG/C7+u+jb1hr5uu7cPb0HY+W3a9GldgelG6AYdmLZw+971kzBYcDc/LBZRWoSLOlpEbZjGSb9oQyDGT4vUnSfOMqM0HtrnVVtfu0VaLdipcsvU7xYoji34/21u9h8Wo1ukgduH3SIcw3aax35YhGXag1XfH84yZp1ndT8sru78MKqBNU3T1mDMh0WfhNV8WaRAkJ+4VRx2D2PfJXkhmBBCbtQDLzy0a0tgbHhzy6YIu7fPP//1w1sKfr99/vXNL9wO3HrbvKwIjZd1If80F8wswBpgSDMBP1fguglbsEIJbgVhtHhd/diFRfRh8Z//mV/dNu5++vylWrw+X97mP8ZQzbov+trteuBc321cD3ixnz4t6OLqTh3wbD+01WxDB8JUxZ+eM79LqpvFf83Pfnwu8ikO+x+/vNVAhYfnvrz9tAC++vLWDvPvT7OU5sefPhX1NWx//Om7nG7wstDvZ2FA609fX9cvsWDg96FptPhqatzmtRYIftqEQPhv7Js/T9Vf4l4u+foc/GPdfFj8ueTZnv8C+j4T0QNy/1ws8AGY+fYpq9Pqx9caIB3Cyq388Mef/pFYkMR+XqRd/y/J/fkpOAFlALz1cslPHx7h++ti+bLtm8x/vGwDEubfsQQMf1/um6P+kexHZP9OdJFWoATeY/mn4v5swvK/Fj//Q9v+2YQPi+jLGxsWKahi1yvCz4tfHyny8w/B95s//PVvQPT/KMash9Z/SPhaulUahV3/9evPP3SP2z/89ecfhgZkceiWX4e2+DOZf+bXxzq/8+Br1I+/nwvWt6q8qq/V4lsNLX6tm//V/u3Twp4B6fv97vPit5U4f5aL2Yj3RZ8u+E01dkDX3/jxp7e/AdipgDWD/3gM8OM//mOxT/227uqoX5h+PQB0Hao+LcNZ+UOSAiztHqjRzpDZpcCxr3Eg/+cIzxoDbP7l//gPqP/ov6Aeeofl8Os7XodfXwj+y6fFAYis2zROK7dYGLSmfancOKz6ebmmDbuwHQFEeVMffgSV/HH+MaP6L/9E6teHgE/N9MsDjdMn2hmb7Yx03VCEn2abjjN6Py3wAdWEt9AfgOyi9t0n03QfgK1dXYwAKWf7uzwtikWQgvUAa00P2cBHn2dhv/zyi+d2yZfqCc3o4klnHQQGfFNn8fEjsCgqZh2/VKGf1Isffv3bD4v/XvyzWQ/h8xoa4IdXBICGkqkqC1BRQwmGzUQHoNwNHhH49W8vvwIxFWAeEK80mjlqngwyMg+DdyebIv0RwfAXUy0AF9VtD/B+kfafFtto8U1fsOj8aGaEpO76RRA2YRWElT8BqS4w55snq7pfdCDtumj6sBi68LHqL17rPlQsQWm7/S+L/UYD/FMX4J9ZzccgMLmuUuD+bynwvA+EtD90C+ZdxKeFMufgonFbt0la97VG5D7jMnP0azoQ7i6q8Pqlmlk2nF31KIine8Ag4Bn/FdKPj+7Cr0tQ/UH3vvZjjDuz5OHBlu2Xqnslu9uGjw7k0UHEA+gZAAX85ZVSXVIPRfDwH9B0lvSKQvCKyiMHv1H8t5Zm87sehhmKfGECxGgWXwYEXq0X/z+3RrNHaEEwOIE+cOyCUw7G+RmpuVucI/psMEGj8ljuUZXfm5d3gHrH6S9VkYK0a6e/PEc+XPQa88Q+gB4BwBzjIR8kF1BllvvI/TmX23ZW3/1SvRPCh9kHM/oBBwCgAIU05+/7gvPTd00TgAbz9ffm4BGSNpi9APJ70QxeAXIvCsPAc/0caNXO9fsKMyiERzivSeonv7NqAaSDsAD5C6DE7ExAGp++gfTz6bvqv5v47IHmKY/+cADl2z4EAD3CWcE5Pte0BygGkuvRnAM7Pz+EADPKpp9t90D4yw+vm2EbXoa0S/sZLJ9+DRuA0R/n76el893w1oCaAc4CldEMwLuPWpphpgQdDtABwAnIgzKtAOMDp7yc8BDoljMwAOB9taRPiY/bL4OeeTpT1fvE2ZB5zsz+oCLqEtyZfosfhz9LEyCvnEc81v37TPu22ix7xtAO4CBY8f3ps0349GT6ZyuxeJf7+Q+7nx//vQ3Sg7ut3yfA50XS9033GYKefPtOt58AgkFPXbvv1PvxG0l+fCHE70Q+rf28+PfU+p2IV1l8Xqw+wZ/g+ZH8SqvXB3hh85E5f1zPT2fo+w6tYPm6BHk1x2wCXP+NB9+HADKM2zCeBz95sZvp9ApA5kEEIABfqt/m+VxnL9T5AELzm/p/NAQg55/x+sZX4FHVg7WDuWmMw0/zXmtWvwvfPldDUXx4A0gZ/g+7s5mPyjmRu3k/B0oG9F99Gj6u3qFx/v37zS53AyjpgxqYae4bhC6eyAiarTS8zpXyoJA/g98Xdc8Z/g1o5+sH+AazJf3UzKo/d3Jz7/c7NvgazgTyR73oPyGYGR0WMzQBVpi3m99o5juB9aAnCfuHn2eVAfmCqSGgQqD8EHb/SJ8+vPV/1EF9/HCLTws2BABddL+txBfFzi3GbwDjGX0QdR+4/8PiSWWgSIH+c2RmsHG7/MFXf6pLWI1pW1dzq/BHfQ5P434z5i8AiqrAq29ggRb0Ra9ogCAGz+b6TxcpQC4XX8F0ADB/XIWd6fgxZPEc8t4kufEDwQAff4o/LSxzz/+p9G99/x9FH0HzNUsL6s+zxA8vYAffYK/2YfFt2wUc99oIzyuE1VC+ff553vLNaf6YMv8Ac8DXt0nf/h/HC9/++ge9gGIPtgCcO8v6ruT3ofVjqzibAET3z//Z+PUNlJQLwui+iuq11wDDAbh+7OZuCwKYAxYH1090AM/+nV3Ia2qXuKAVBnNXKEIFBIGsKTwMIx/HCZiiSG8dUa4HU956Ta3c0F8FERK4FEl5K3+1piiUJNwIJSJkBeQ94eXr3E2mszqzLsALHwFChd8fg1vBy46n3rOTvm16HrARv/LQw9dgpLjutvTzs4GWKw9HCM+UvGWLh/Vap9udqRhlmMvwvinhM5ExNFe6vqIecC3hjHQnc0Vn4aZr2LXB0tqd01SOnA5EZSu2LQmptwkp9KQxTMx1uX2sDg0qBxNmk9k0BpOQadvBtLcNv3W04pKYVeg526KwjCIvw9QI7DCFB8cu+hsLLakquG195Zwe6MPZLgXYaoX1cMskXr1t6RarU8cU5J3UJNuVy3iYXec5N1Ho0UvUbXpcLrW6JcMLJOdQlHWGUm6c25GrC2wLd0FmIJKq4ztPuERWDvdVcdN86I5j4jkZjSk3/BQVpp0oKEJd3KVMxsuNnvCXO+OZwxYHGalIprc1vbh2XAHbUS6FdlW7ugVVC0NhRcCWs4TCE3SvU8hvTZeSS8dK231jn9JDkSV+a1+LbYL116xAU8HDEtvme5uvgMkrOUdzg2/7KkxZ+Xa9M/Gmvlyu8ma4p9hZk5K85rRtM1hjlRziijE4lUq826qcrN3Fzw9EsT6mdzfAgi3qOPZ6NBCyr/BeBxxIbCylPBuOZOe+kV8NPOQJBZ50czNVWWgkQTwFesqX1NHBbwLo0CS+XlGpQgthTXs6J5jbDFNGhRijEFYhVCX76Zw0x0Pm6tK+QPaGdOK7gW3OHGe6uGl79m4I2029bYpTo8ANfGUhHF5JJYax2HIwQjOWlyfVvtA6ss/kqZDGW8SG5UjceFBekFcalp4nmH1cXzaaTYmXepocJxV9j8vWcRHIlNrFpral1hR3HU+wmJ6bgfbVrrFaFLv0F7nn4ptU5QcShpLrPcOtFuJzabW2rE1+PpbdwS063t2tGlAVTn/pccncBVJfrrhL51+oEt1dljuTkxG9uE8GIjSHQSAxJlvnhIKme6FIZHXJVJAErKzSAU4c9twt5ZuuUyw5XqrbxU5tzHIUCVO3EuyUVQIV+LoobQ7pInK4BacrphRsbPU6UZ0b7UxeijN7i3cjUWvQMVp3SJQZpRNhLI1HGZ8t9yNpyOe+OVwvGLunubFysdi4HOsKy4akTmWnEJo0uR4Sv6i2ko4KxvIWLJ0uEGlh7MxYGgffVbzyQDtnQ1GltXpERJaf2o3nGs4pb3geKyTHVTmM8fQKDmHZPzGKC8UwTfKETyG1WcW7ewtL3a69braZUwabk9dlkUFcdx6HQDh6TO3sgqmUWEsuuxYNnYL2irHLcZuikwI6Y6iQKmW53kz3/nYNhbKWrX12siBMYZMAmZQycwk3dHppFSX5wCN2REnbrhUUf7DEascpcZRGOGnVsWzGp1jxpSi8OAwoAXu4nEdTd2tmaQeW6jAyv5/2I+LrHCFwOxxGMUAKo75Syq2yVRyab8blnaWP5+hqYkLS3pvJJZ1lm++k0Nq4Zn8lr0fed6o+Zlhlx9tbce+VqdhRzVZJtjeavpxGURuPd/k2HW6W6R6oe6aw0QSp+JUt0ytZDrF9o+OjLSKMAPPmbeezwdlPmeCOZejaqoRSamF1R6+tQ3aOSf0ocGTS2MJqogPpUpaquzSVnUvzt0iqR1MJCCmLUdBRB7XujixNQgEvWRERoA2Z7w3XohGNMJZqdyXOXbNUASYbcMcQpFIGjmodLrLhuoWrxpVXjdvwFML6Gt8dujMjZ0M2bMmrWUjHXTKGewq24qPpRCQXJlLtmtcxgRVTcqi1OvBZqyPBWVIqCd/xd3Inb7aCm1hHoYNYldNLvSx3vrKzap1Yhv5doDRPCVdkFWzOWp7TFEe2xFTq9xo9b3S4lK9OX94KudL0SC6rOMsj4AZXPBvlOku7NuduTOP2DsXEo7ru9VgYGOcMOu9qJx2EELsUEEedt5zNBgc/oEzyprZ2pRzbWORlGhUO8NrDJWgPVzBZN1hFLn20QbxR3q93J73EJkJSYtxTa66GJ0hKqmUE0KmOMDqE2NRARwg3af8UquJBNxL6fpmg6kQiyzAaK34FCacTebopFHke7rvDyFysMPTEPIUB93pOfgnZchUkl/SQuLJ0lnjBpsdlmeAbT8+RVaR7oE1rw20gCiVq21ZMy6mmLvf2LdaYK1zb3Eqrl8wd0QCjwcwOkK2hgwaiOl33Kg3Jo3pjoqWzxw6buyIYMF8LG2KrqrVbZPsuvSt6KcONAPllwpPUeUCMNNZhGzrmrdRUKHbE2HZwuLZvRwURMDiW27PahxzNGYxXNvhkKO5xQCE9vUx9QLHZMWWpah/6oe8jSXLcFSEaeWy62cemkZrsjZHPsXnJ073bnQaIGzBhXTNc7/KWwagMiZIuY+pnfGLEM30/7i/dZrvX8P01ro/eruCr3N3Kx0arO5kP1rHjTzJzK8/nkxMJ6Imzky1tdc2ODOMN4sirMaDuzPngd6k5XS7DReaU/Mal65s75JZqreNOqW/aBdNLSSwCa9u4pYJp+x3JNAc7Tg9Wtbuc7+3SAzHa2ZJzTBJfGkxquzORaZ+TUb2CT/LVcO2kgP1Wj4mx3MiqJ3HHMCqKo+/s5NRCI2nYTnRKs1vRVjyhXRNmownHnNkXGW0J27hppeREaZrjpneTrgtvh5V3zOSNgYkyd1Wn/ATv80KQTUplKbJUWCMqpDt0LNarFDPvaGTjmrEJyOIWJGpt3rqyNeRtmd3OI65wkhYWkkpHKdJ3ZFvImJxSEXaOjw58ZIQablzr1Enwrd1v0UKPdSYtI0vWlQAptHCfSC3D91Oq8ktZQ7LtAVd0iWejKxYhdX4+s1RqUc3a27Fev+qFcwG5tZMRVHbRgqXWJ7Tl46rAo+15PNS65B3ELWLKy+sZ48XTWkwQDposuhnYK6QS6ESJzEjFt11fTxp5nexTtQeI7FBe0+oX3gpLdBtKdQ6fJ4XJtXqAd6F2yevJRMZjus7um93NwNe7ElHO+5K4R+cJr/1hEplAOm2Ic0m49BSfJDeLiOow1DfCTBuDSYxBoSUG9csL12zSGL7VRLMrbfyQaoJZwIeMUCXf3R/oVVc051sLVT5WWuLAcvdjryAhrqL2gSZzTT/nV5KD7gxSbwmfz6j2Ut55lIkOGgJdyZHEEzfHBe8mCKmPR2DNljgBMOUvbLGHbnd1J27ipcnKkppSFd5oTXAd76uK39UI6CZOzcbMfR/GWTjVV+dmTx8LfxCFXnN8vKttflAcA1bcVS8t79mUXGpctzbSiUiLqNZbV1fWFdhiiYaYDa1jo2sffLegntxjWyBi0FoMTEv7wG3Fu2lFwt2yeYI7HnGEpUVCd1k23u+hvWFJbXjeFQKNHxPgJsPKeA/Lik45hxe5uLdsgPbVJG7b+/5wxCk3bOPB0CxfX1pZvYoFi9XOMWdZ1NVmAh9d0gUsF2ViYEZxybEAa4lmqu5rfdNCGrmF49grSkb3sdvNFuzJNevNSj2cDDqgEnu50wwWH5QNvmY6IinVRDNP45gtyQFuK3gHU0f7KEO+1+84WI2xjkGPUKyeeKmhS3w6ZJmz5bZ9xiqgQV3qe97KYm7t436ZVcq97m3Vq5jYbYTtpdkRl/NFS9rYSzOxOmT+DvBtcVnVR5+xp2LlISqtHPTYOMEDuy5Alz+spX4LuPKOGrfilq4DfDtBRFOIQpeREAdffT2QPZFuzBadxrY7o3YlVkIq1YLRupzfn1ernlSMtexBJc62Zc5ko+pG2/MxwnR5de+WpCDeeEpdIfeody8006n3M6j/YJ10S5a7nnbBGS5kN2tZk9LwCYqZM42f20m/8SdGTHLC20g+5GwsEOjjRfHG9Rml41TQbitt8Jdrx0903jMF6UhaylqGad++MOs6qfUSpSl9VWepM1iOjXgWj8Pc9QB7fuQPhkGU691SZe+X/fKO8+H5ph77Y+xpVt4iBqXKPU6FUeRi+73AYDwLtiMNowbH9eSkfoBqop4ia5XS4yDdtlnn3fcbiso9zJcxv2lkz1HNZiCuF5rud0edJhtk6tY+yfEMBPMoGUQU7YT7TLDyHaKpw4a+GRpCDIh7RuuiA8ivxXDJ7ZNyc8s47BhqYmFcrvu0h9ozPzJ2HQ5Brpf0gaWEtZXToyJq0CbQEHW1wzMkbTiJ59ltR4XDLiHJLaKInT/VgyXHvO9j17M8RsYKucDeWu31I1L2At7wh1SKy9WmuaQ9yTE3czyX4YgLa1uR9xHWFHLWQu3KvWkbb+zVlCAgkVqmDUWbbeY34tmNc8XE61KVyWDNEBScEOeGMq2OV7qGdgtkS8YXQnf2jC/5ynUv1/UGkfV2GI9L8npyTwQ7wRS0bTEusT2vBEUemGuoXN7IvHJSS4Xy0Ia5CDT2+3xYC052igwoRu6nrthWyMnnOJg5V5EVAsYOdIXBWDZNKTyAL90kche+9JNxQqyTijv+bcpDrBKO+rgl4MbslxjnW3Bg78xLKhG+n5aEksFIe+wuLe+Insbtcri7JHkaHlx+Y/mHnUfU3YFmBy2HrqG+vfKcHalRrtSCe4hR/rKTC+qMjde89WEnt0XIAr1OwKNjuhtGFuEjV6M9oqpvTS+mYUDy4TSUhuek5+U1SaP73XbB5jCi2wAJ+JuaJQOFO1CxK5bEKmExwjOIVhRX95NtRcoK4IWrmTvIbXG/P/rI4cJ4HLZCiVPh64qy4hRrvXLHyFqF/GFQ7quLj6rJjQk9uDMrpEbMjIVuBe14PT2UKIf2t+ASLY+5m3o7W9uLd3ZybxEqBlcYh1Cou7LHzt61UrSRY5QVuco+ge3MkqUMhNnn6+omO3CEXbnCurvV6LnnrX9wIEnhzAsoLuSi1B1aWevcRZElj9HjWUD6e30nIHdrIeL6rMYox02seVOVJEMPFwgSUWgpQMi2gK+ok0AE7kFidD12h7N1FaGqlrmVpXqF6g/OmZiSvVAlpZx3UGZL+tKVoeIA5WXq3Y4rDKd4KFYaHYZ9A2KZicYkBZrGHa8t++s+qVfNZMlaxeD1UVk2MEIR7TlUdNnYbGOVxyvYuSdoqe625hmqFZVoUXSVDx7wwZjYuIMG+XY7adBSXYHPOki24jrIA3HrVqiX7wU3xqWyJHcNw2pMcOomoimJ/QZ1s5XTq8ggZGdyGaagbUkwIaOk3Zi3eBeNOhx1llGS+sakzdJkrkuIXDs9Ela3rIm3G6lx8RtzNIvVLk9swrms2np5cmqbXam7bqPjUOVxoeapmNhCW1FWVSN2oAtiK6M0ruM2cUNOjs6c2Ut5XcOpXY2TZtzV/KLl0ZHW9/65aSJ/Ge6OXcmzCiWeVCzGa0k5wFuw47Fwlz6iaUbiQmeoyx0eF/7xSiQk6+QO14G9525LIw2GLvsKtGIwRpEo5UeDmmxVvq4iFpD6GiaOndxueRc91SRWKlB6Ds4IH3pRYMbergdbALAxx5wVF7CtRGHRauu42TB1N44Ijfyk5YMUh7i/KttCPFJkrHJ9l8ZVvuJg+z4ee8Td4VST3wYB0nCvdHYpq65dHb722P3q9bFpFwOTkZR/vO1P6FAtjewS7WCszUJUY0jBX2E1gjBLbWWoPkfsywkdDYKDVuVKygXg1Y4p1Ta5CKcW6vbiXtb5gwmL6P3iKdmRZrEaog5VabJll1wRcaQtHeMp05UxKzhIYAfslZy2V1FKO9w6SGBcEiXgXiJKtFGJAOQuY65c6iJEIoz1/pIwJE/lStsXNViLrSt1CUfBYFYUtxoi5X5PFG+4UGPNVWKLn7wLQW7IGtpgaLhrKSW7dbQihUN77q+Hy+p2ptvi7m6KO1Ma/rqkYLxWOVdRV9g9W64NNb/3KpFHKtgAuwE0aVghIrterRi09OIgjp2DOmUpa2/CsU+FTry6GSzdo4uWudlSieTNeqID374e5DVfW9nd7qxkA2qgujgbQSRzC9AXefMLVjyVphbslwy9OvCKs5L5GuLo0DcPpGC4gTsdI94ZB44qkCLUAIRe5cxvS1Yp0v1INW0pDb0BdbUB01R4ci6nOOb4ncT2VRAn1AUVnZgQuDV80fajAe80gsBaf4R1z+gNEXPIHYzIRp8FUFVyCDLSm+pu1/01wi9pc0oIjGqO48D7aJE0MOl0baSd7pu0OHusoOm3u8OTYbkqslzoJhDk07XLmNEkDlh2X+Up6edEvqzlM8kREb8CDZO4PRpbTM1wd3lY3s8HdClt4b5r+FzDyauhN5gnNurGoYb10BJpnzeHfqXsSlKayP1SX98geCCb1M6OyxWR7WB8mauFWEjZwcJ5KUuPBExiCr7kY86D7nbhNN3KgM0yPZQSxYl5zFG1cEgrMYbGaClSOu2nFNcLQ1dgm6k5ZSf1ECMIYRInlVpikTcIwUUYDtPA3gJv5S+xwxVNT6tdsM54bRC8XMh3AWlv2ZG91rixPda5jaKZW2jL9ejVTu/KiHanGx5FL6q1IqA1eRhpIu90t6nFjbNvhBXRMBSXejixrQbFvrFiw103G1Tj9Ji73NADfRi46E7RNcMqV09juxIPKnU4YLAg3HFx3aolX0DsJXQ74uQGsbju8BPjseJRW/cKTZ0BZRcFHx2gWxIFUzT17Qk94sF0jWAeysbOZsfxevKvy+w+4iv6EI2eqA8ho6PiVT074y4+BX2xuuW2gZ4Ox/5elhRpB0sXh6E1Bu0mBycyu2XEddTSKIKDZh9sQhDS8u6bkR9hlEUGI5MSniAHPWYPmlgKp6o5LnFcDovl+lQ2VAFje1TcnKada+U6LVutuPRh3Q5ohqNWXGhWS8dR2RsWrGSw8YZjWT1xfnBxSKneItxqW/EhTGlpHJmmHODKTSKKJAy4zTjcRc+QEwrCMaI7rzuKySKUVYbg3BGusdZ2Y6CrRZsFIV4EK2gb0ffNHfy2GP9219N6wsUlIW+G0L6TUBDRzQ3HaDi4LTOOoLijd5C38Z5rM3HZqVkBEEurj+KyLqqy18TIW/LTaXWS8M6gafrtw9v8/vX1DvpfOfo2v2T6f/Y+6/la6v0gy+NNYOgGnx9rff6XtPnrh7fWT2ddHm/qumKIXy++/u493cd/cmRhnjg9z5C9vzB+vpvv3Xg+TP2WVsHQ9e30tauLx+EVMMMbuvkMZjcf0/XB929fYH5b620+DwnMm8+Pfe3rr6/To4/b88GUMEjdPnxdxq/3lh/egtf5qa8ojn0N22Y283UOAliHfoI/oW9/+78n1VtGFy8AAA== -->
