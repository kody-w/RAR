---
name: "rar-cowork-cookbook-configure-take-inventory-on-software-licenses"
description: "Validates an attached configuration Excel file of software license inventory rows against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, and after your approval applies the changes with a before/a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_take_inventory_on_software_licenses", "rar_sha256": "2ed84744b84948c92aba6131472f890a9f1537b6b94208beef3f4debd1477818", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
