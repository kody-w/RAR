---
name: "rar-cowork-cookbook-configure-create-solution-blueprint"
description: "Applies bulk create-solution-blueprint configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, pauses for approval, then applies and reports before/after"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_create_solution_blueprint", "rar_sha256": "cfaec654b9cfd690b514a2a076297047ec26e05fb920f7df0f1e3cb9d5f2b2b7", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_create_solution_blueprint`. The original RAPP
agent is preserved byte-for-byte in `configure_create_solution_blueprint_agent.py` and in the RCI capsule.

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

Create solution blueprint Configuration Bulk Setup — Applies bulk create-solution-blueprint configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, pauses for approval, then applies and reports before/after

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-create-solution-blueprint
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
      "description": "Explicit user approval after reviewing the validation workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_excel": {
      "description": "Excel file with one row per create-solution-blueprint target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Target environment; run sandbox first before production.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_create_solution_blueprint_agent.py` and embedded as the fenced Python below (sha256 cfaec654b9cfd690…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_create_solution_blueprint_agent.py` first:

```bash
python3 configure_create_solution_blueprint_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_create_solution_blueprint_agent.py   # or on stdin
python3 configure_create_solution_blueprint_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create solution blueprint Configuration Bulk Setup — Applies bulk create-solution-blueprint configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, pauses for approval, then applies and reports before/after

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-create-solution-blueprint
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_create_solution_blueprint',
    "version": '3.0.3',
    "display_name": 'Create solution blueprint Configuration Bulk Setup',
    "description": 'Applies bulk create-solution-blueprint configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, pauses for approval, then applies and reports before/after',
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
        "upstream_slug": 'configure-create-solution-blueprint',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-create-solution-blueprint',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '50cbcd7721c52549',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/create-solution-blueprint'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-create-solution-blueprint', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'configuration_excel': 'Excel file with one row per create-solution-blueprint target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; run sandbox first before production.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for create solution blueprint, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per create solution blueprint target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies bulk create-solution-blueprint configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, pauses for approval, then applies and reports before/after', 'example_request': 'Bulk-apply this blueprint config Excel to USMF sandbox — validate rows first and show me the preview before writing.', 'inputs': [{'description': 'Excel file with one row per create-solution-blueprint target and the new field values.', 'name': 'configuration_excel'}, {'description': 'D365 legal entity to run against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target environment; run sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you have an Excel file of create-solution-blueprint config rows to validate and bulk-apply in D365 F&SCM, with a dry-run and approval step before writes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureCreateSolutionBlueprint(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureCreateSolutionBlueprint'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel': {'description': 'Excel file with one row per create-solution-blueprint target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; run sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureCreateSolutionBlueprint().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
