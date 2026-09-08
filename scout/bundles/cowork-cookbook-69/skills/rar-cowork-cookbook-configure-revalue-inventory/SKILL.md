---
name: "rar-cowork-cookbook-configure-revalue-inventory"
description: "Reads an attached configuration Excel file of inventory revaluation targets in Dynamics 365 F&SCM, validates every row, returns a validation workbook, and after your approval applies the changes with a before/after confi"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_revalue_inventory", "rar_sha256": "3fde02e455ccaef7d9e060ffbe8355373d9eb850f597f4d7baccc1ca061dcdd7", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
