---
name: "rar-cowork-cookbook-configure-take-inventory-on-software-licenses"
description: "Validates an attached configuration Excel file of software license inventory rows against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, and after your approval applies the changes with a before/a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_take_inventory_on_software_licenses", "rar_sha256": "2ed84744b84948c92aba6131472f890a9f1537b6b94208beef3f4debd1477818", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_take_inventory_on_software_licenses`. The original RAPP
agent is preserved byte-for-byte in `configure_take_inventory_on_software_licenses_agent.py` and in the RCI capsule.

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

Take inventory on software licenses Configuration Bulk Setup — Validates an attached configuration Excel file of software license inventory rows against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, and after your approval applies the changes with a before/a

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-take-inventory-on-software-licenses
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
      "description": "Your explicit go-ahead after reviewing the validation workbook, before changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per software license inventory target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Target environment \u2014 sandbox first before production.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against; defaults to USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_take_inventory_on_software_licenses_agent.py` and embedded as the fenced Python below (sha256 2ed84744b84948c9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_take_inventory_on_software_licenses_agent.py` first:

```bash
python3 configure_take_inventory_on_software_licenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_take_inventory_on_software_licenses_agent.py   # or on stdin
python3 configure_take_inventory_on_software_licenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Take inventory on software licenses Configuration Bulk Setup — Validates an attached configuration Excel file of software license inventory rows against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, and after your approval applies the changes with a before/a

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-take-inventory-on-software-licenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_take_inventory_on_software_licenses',
    "version": '3.0.3',
    "display_name": 'Take inventory on software licenses Configuration Bulk Setup',
    "description": 'Validates an attached configuration Excel file of software license inventory rows against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, and after your approval applies the changes with a before/a',
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
        "upstream_slug": 'configure-take-inventory-on-software-licenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-take-inventory-on-software-licenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cd6eb1fce786fd45',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-licensing-and-entitlements/take-inventory-on-software-licenses'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-take-inventory-on-software-licenses', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Your explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per software license inventory target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment — sandbox first before production.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for take inventory on software licenses, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per take inventory on software licenses target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Validates an attached configuration Excel file of software license inventory rows against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, and after your approval applies the changes with a before/a', 'example_request': 'Bulk update our software license inventory in D365 USMF sandbox from this attached Excel — validate rows first and wait for my approval.', 'inputs': [{'description': 'Attached Excel file with one row per software license inventory target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Target environment — sandbox first before production.', 'name': 'environment'}, {'description': 'Your explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-apply software license inventory field changes in D365 F&SCM from a spreadsheet, with row-level validation and an approval gate before any writes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureTakeInventoryOnSoftwareLicenses(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureTakeInventoryOnSoftwareLicenses'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Your explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per software license inventory target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment — sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureTakeInventoryOnSoftwareLicenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
