---
name: "rar-cowork-cookbook-configure-manage-project-quality"
description: "Applies bulk manage-project-quality configuration changes in Dynamics 365 F&SCM from an Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a before/aft"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_project_quality", "rar_sha256": "7039ca51897c7f2d804b508c9d120337c68035d8e6cba97b9a35bc048d97a474", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_manage_project_quality`. The original RAPP
agent is preserved byte-for-byte in `configure_manage_project_quality_agent.py` and in the RCI capsule.

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

Manage project quality Configuration Bulk Setup — Applies bulk manage-project-quality configuration changes in Dynamics 365 F&SCM from an Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a before/aft

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-project-quality
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
      "description": "Attached Excel file with one row per manage project quality target and the new field values.",
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
      "description": "D365 legal entity to run against (e.g. USMF).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_project_quality_agent.py` and embedded as the fenced Python below (sha256 7039ca51897c7f2d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_project_quality_agent.py` first:

```bash
python3 configure_manage_project_quality_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_manage_project_quality_agent.py   # or on stdin
python3 configure_manage_project_quality_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage project quality Configuration Bulk Setup — Applies bulk manage-project-quality configuration changes in Dynamics 365 F&SCM from an Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a before/aft

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-project-quality
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_manage_project_quality',
    "version": '3.0.3',
    "display_name": 'Manage project quality Configuration Bulk Setup',
    "description": 'Applies bulk manage-project-quality configuration changes in Dynamics 365 F&SCM from an Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a before/aft',
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
        "upstream_slug": 'configure-manage-project-quality',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-manage-project-quality',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f22e816b9457aa70',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/analyze-project-performance/manage-project-quality'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/configure-manage-project-quality', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per manage project quality target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; sandbox first before production.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for manage project quality, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per manage project quality target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies bulk manage-project-quality configuration changes in Dynamics 365 F&SCM from an Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a before/aft', 'example_request': 'Bulk-apply this project quality config spreadsheet in USMF sandbox — validate first and show me the dry run before applying.', 'inputs': [{'description': 'Attached Excel file with one row per manage project quality target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Target environment; sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you have an Excel file of manage project quality config rows to validate and bulk-apply in D365 F&SCM, with an approval gate; run against sandbox first.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureManageProjectQuality(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureManageProjectQuality'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per manage project quality target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureManageProjectQuality().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
