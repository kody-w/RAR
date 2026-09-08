---
name: "rar-cowork-cookbook-configure-subcontract-project-components"
description: "Bulk-updates subcontract project components in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/after"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_subcontract_project_components", "rar_sha256": "8996e97975deea6f154f524cc80fbc177594e409b866ebfd741537d4f7155714", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_subcontract_project_components`. The original RAPP
agent is preserved byte-for-byte in `configure_subcontract_project_components_agent.py` and in the RCI capsule.

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

Subcontract project components Configuration Bulk Setup — Bulk-updates subcontract project components in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/after

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-subcontract-project-components
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
      "description": "Explicit go-ahead after reviewing the validation workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per subcontract project component target and the new field values.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_subcontract_project_components_agent.py` and embedded as the fenced Python below (sha256 8996e97975deea6f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_subcontract_project_components_agent.py` first:

```bash
python3 configure_subcontract_project_components_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_subcontract_project_components_agent.py   # or on stdin
python3 configure_subcontract_project_components_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Subcontract project components Configuration Bulk Setup — Bulk-updates subcontract project components in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/after

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-subcontract-project-components
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_subcontract_project_components',
    "version": '3.0.3',
    "display_name": 'Subcontract project components Configuration Bulk Setup',
    "description": 'Bulk-updates subcontract project components in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/after',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-subcontract-project-components',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-subcontract-project-components',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ea370a4df8e5f584',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/subcontract-project-components'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/configure-subcontract-project-components', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per subcontract project component target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for subcontract project components, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per subcontract project components target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Bulk-updates subcontract project components in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/after', 'example_request': 'Bulk-update subcontract project components in USMF sandbox from this Excel file - validate first and show me the dry run.', 'inputs': [{'description': 'Attached Excel file with one row per subcontract project component target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to apply field changes to many subcontract project components at once from a spreadsheet, with dry-run validation and approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureSubcontractProjectComponents(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureSubcontractProjectComponents'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per subcontract project component target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureSubcontractProjectComponents().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
