---
name: "rar-cowork-cookbook-configure-manage-procurement-spend"
description: "Reads an attached configuration Excel file of procurement spend targets, validates every row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then applies approved changes with a before/afte"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_procurement_spend", "rar_sha256": "2296c435a75e55e869091072c4fda9012285270053b5cfbf09a169e93d1e9fc7", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_manage_procurement_spend`. The original RAPP
agent is preserved byte-for-byte in `configure_manage_procurement_spend_agent.py` and in the RCI capsule.

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

Manage procurement spend Configuration Bulk Setup — Reads an attached configuration Excel file of procurement spend targets, validates every row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then applies approved changes with a before/afte

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-procurement-spend
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
      "description": "Explicit user approval after reviewing the validation workbook, required before changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per procurement spend target and the new field values.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_procurement_spend_agent.py` and embedded as the fenced Python below (sha256 2296c435a75e55e8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_procurement_spend_agent.py` first:

```bash
python3 configure_manage_procurement_spend_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_manage_procurement_spend_agent.py   # or on stdin
python3 configure_manage_procurement_spend_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage procurement spend Configuration Bulk Setup — Reads an attached configuration Excel file of procurement spend targets, validates every row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then applies approved changes with a before/afte

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-procurement-spend
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_manage_procurement_spend',
    "version": '3.0.3',
    "display_name": 'Manage procurement spend Configuration Bulk Setup',
    "description": 'Reads an attached configuration Excel file of procurement spend targets, validates every row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then applies approved changes with a before/afte',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-manage-procurement-spend',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-manage-procurement-spend',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '739ecbca00efc4ab',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/source-and-contract-goods-and-services/manage-procurement-spend'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/configure-manage-procurement-spend', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the validation workbook, required before changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per procurement spend target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment — sandbox first before production.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for manage procurement spend, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per manage procurement spend target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached configuration Excel file of procurement spend targets, validates every row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then applies approved changes with a before/afte', 'example_request': 'Bulk-update procurement spend config in USMF sandbox from this attached Excel — validate rows first and show me the preview.', 'inputs': [{'description': 'Attached Excel file with one row per procurement spend target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Target environment — sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit user approval after reviewing the validation workbook, required before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-apply procurement spend configuration changes from a spreadsheet in D365 F&SCM, with row-level validation and an approval gate before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureManageProcurementSpend(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureManageProcurementSpend'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the validation workbook, required before changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per procurement spend target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment — sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureManageProcurementSpend().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
