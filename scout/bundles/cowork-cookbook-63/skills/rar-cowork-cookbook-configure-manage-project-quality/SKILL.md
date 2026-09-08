---
name: "rar-cowork-cookbook-configure-manage-project-quality"
description: "Applies bulk manage-project-quality configuration changes in Dynamics 365 F&SCM from an Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a before/aft"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_project_quality", "rar_sha256": "7039ca51897c7f2d804b508c9d120337c68035d8e6cba97b9a35bc048d97a474", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
