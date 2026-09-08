---
name: "rar-cowork-cookbook-configure-plan-loads"
description: "Reads an attached Excel file of plan load configuration changes for a D365 F&SCM legal entity, validates every row, emits a validation workbook, waits for your approval, then applies changes and emits a before/after conf"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_plan_loads", "rar_sha256": "88d0029306e0e9c68e05a8ab9b06c9e0121aa9c09a9014f2990eddf43b1e1e75", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_plan_loads`. The original RAPP
agent is preserved byte-for-byte in `configure_plan_loads_agent.py` and in the RCI capsule.

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

Plan loads Configuration Bulk Setup — Reads an attached Excel file of plan load configuration changes for a D365 F&SCM legal entity, validates every row, emits a validation workbook, waits for your approval, then applies changes and emits a before/after conf

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-loads
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
      "description": "Explicit confirmation after reviewing the validation workbook, before changes are applied.",
      "type": "string"
    },
    "configuration_file": {
      "description": "Excel file with one row per plan loads target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (e.g. USMF); use a sandbox first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_plan_loads_agent.py` and embedded as the fenced Python below (sha256 88d0029306e0e9c6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_plan_loads_agent.py` first:

```bash
python3 configure_plan_loads_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_plan_loads_agent.py   # or on stdin
python3 configure_plan_loads_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan loads Configuration Bulk Setup — Reads an attached Excel file of plan load configuration changes for a D365 F&SCM legal entity, validates every row, emits a validation workbook, waits for your approval, then applies changes and emits a before/after conf

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-loads
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_plan_loads',
    "version": '3.0.3',
    "display_name": 'Plan loads Configuration Bulk Setup',
    "description": 'Reads an attached Excel file of plan load configuration changes for a D365 F&SCM legal entity, validates every row, emits a validation workbook, waits for your approval, then applies changes and emits a before/after conf',
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
        "upstream_slug": 'configure-plan-loads',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-plan-loads',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1d701e722f6fa709',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-freight-and-transportation/plan-loads'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/configure-plan-loads', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit confirmation after reviewing the validation workbook, before changes are applied.', 'configuration_file': 'Excel file with one row per plan loads target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); use a sandbox first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for plan loads, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per plan loads target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached Excel file of plan load configuration changes for a D365 F&SCM legal entity, validates every row, emits a validation workbook, waits for your approval, then applies changes and emits a before/after conf', 'example_request': 'Bulk update plan loads config in USMF sandbox from this Excel file - validate first and show me the dry run.', 'inputs': [{'description': 'Excel file with one row per plan loads target and the new field values.', 'name': 'configuration_file'}, {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox first.', 'name': 'legal_entity'}, {'description': 'Explicit confirmation after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-update plan loads configuration in Dynamics 365 F&SCM from a spreadsheet, with row-level validation and an approval gate before any writes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigurePlanLoads(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePlanLoads'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit confirmation after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_file': {'description': 'Excel file with one row per plan loads target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigurePlanLoads().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
