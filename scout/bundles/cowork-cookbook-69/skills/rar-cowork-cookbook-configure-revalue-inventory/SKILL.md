---
name: "rar-cowork-cookbook-configure-revalue-inventory"
description: "Reads an attached configuration Excel file of inventory revaluation targets in Dynamics 365 F&SCM, validates every row, returns a validation workbook, and after your approval applies the changes with a before/after confi"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_revalue_inventory", "rar_sha256": "3fde02e455ccaef7d9e060ffbe8355373d9eb850f597f4d7baccc1ca061dcdd7", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_revalue_inventory`. The original RAPP
agent is preserved byte-for-byte in `configure_revalue_inventory_agent.py` and in the RCI capsule.

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

Revalue inventory Configuration Bulk Setup — Reads an attached configuration Excel file of inventory revaluation targets in Dynamics 365 F&SCM, validates every row, returns a validation workbook, and after your approval applies the changes with a before/after confi

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-revalue-inventory
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
      "description": "Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_excel": {
      "description": "Attached Excel file with one row per revalue inventory target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF; use a sandbox environment first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_revalue_inventory_agent.py` and embedded as the fenced Python below (sha256 3fde02e455ccaef7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_revalue_inventory_agent.py` first:

```bash
python3 configure_revalue_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_revalue_inventory_agent.py   # or on stdin
python3 configure_revalue_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Revalue inventory Configuration Bulk Setup — Reads an attached configuration Excel file of inventory revaluation targets in Dynamics 365 F&SCM, validates every row, returns a validation workbook, and after your approval applies the changes with a before/after confi

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-revalue-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_revalue_inventory',
    "version": '3.0.3',
    "display_name": 'Revalue inventory Configuration Bulk Setup',
    "description": 'Reads an attached configuration Excel file of inventory revaluation targets in Dynamics 365 F&SCM, validates every row, returns a validation workbook, and after your approval applies the changes with a before/after confi',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-revalue-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-revalue-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1c24e720fe29eb73',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/revalue-inventory'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/configure-revalue-inventory', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_excel': 'Attached Excel file with one row per revalue inventory target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for revalue inventory, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per revalue inventory target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached configuration Excel file of inventory revaluation targets in Dynamics 365 F&SCM, validates every row, returns a validation workbook, and after your approval applies the changes with a before/after confi', 'example_request': 'Bulk revalue inventory in USMF sandbox from this config spreadsheet - validate first and show me the dry run.', 'inputs': [{'description': 'Attached Excel file with one row per revalue inventory target and the new field values.', 'name': 'configuration_excel'}, {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.', 'name': 'legal_entity'}, {'description': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-apply inventory revaluation configuration changes in D365 F&SCM from a spreadsheet, with dry-run validation and explicit approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureRevalueInventory(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureRevalueInventory'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel': {'description': 'Attached Excel file with one row per revalue inventory target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureRevalueInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
