---
name: "rar-cowork-cookbook-configure-create-solution-blueprint"
description: "Applies bulk create-solution-blueprint configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, pauses for approval, then applies and reports before/after"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_create_solution_blueprint", "rar_sha256": "cfaec654b9cfd690b514a2a076297047ec26e05fb920f7df0f1e3cb9d5f2b2b7", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
