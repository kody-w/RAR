---
name: "rar-cowork-cookbook-configure-subcontract-project-components"
description: "Bulk-updates subcontract project components in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/after"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_subcontract_project_components", "rar_sha256": "8996e97975deea6f154f524cc80fbc177594e409b866ebfd741537d4f7155714", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
