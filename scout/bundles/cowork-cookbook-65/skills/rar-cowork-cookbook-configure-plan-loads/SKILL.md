---
name: "rar-cowork-cookbook-configure-plan-loads"
description: "Reads an attached Excel file of plan load configuration changes for a D365 F&SCM legal entity, validates every row, emits a validation workbook, waits for your approval, then applies changes and emits a before/after conf"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_plan_loads", "rar_sha256": "88d0029306e0e9c68e05a8ab9b06c9e0121aa9c09a9014f2990eddf43b1e1e75", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
