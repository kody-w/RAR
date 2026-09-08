---
name: "rar-cowork-cookbook-configure-manage-active-services"
description: "Reads an attached configuration Excel file of manage-active-services rows, validates every row, emits a validation workbook, pauses for your approval, then applies changes in Dynamics 365 F&SCM and emits a before/after c"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_active_services", "rar_sha256": "69cc10e0a575db6567f356091d9621a44c22be9a5e02370978a6db091c741cca", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_manage_active_services`. The original RAPP
agent is preserved byte-for-byte in `configure_manage_active_services_agent.py` and in the RCI capsule.

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

Manage active services Configuration Bulk Setup — Reads an attached configuration Excel file of manage-active-services rows, validates every row, emits a validation workbook, pauses for your approval, then applies changes in Dynamics 365 F&SCM and emits a before/after c

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-active-services
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
    "configuration_workbook": {
      "description": "Attached Excel file with one row per manage active services target and the new field values.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_active_services_agent.py` and embedded as the fenced Python below (sha256 69cc10e0a575db65…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_active_services_agent.py` first:

```bash
python3 configure_manage_active_services_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_manage_active_services_agent.py   # or on stdin
python3 configure_manage_active_services_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage active services Configuration Bulk Setup — Reads an attached configuration Excel file of manage-active-services rows, validates every row, emits a validation workbook, pauses for your approval, then applies changes in Dynamics 365 F&SCM and emits a before/after c

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-active-services
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_manage_active_services',
    "version": '3.0.3',
    "display_name": 'Manage active services Configuration Bulk Setup',
    "description": 'Reads an attached configuration Excel file of manage-active-services rows, validates every row, emits a validation workbook, pauses for your approval, then applies changes in Dynamics 365 F&SCM and emits a before/after c',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-manage-active-services',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-manage-active-services',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c3ced901e26a381e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-service-offerings/manage-active-services'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/configure-manage-active-services', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_workbook': 'Attached Excel file with one row per manage active services target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for manage active services, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per manage active services target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached configuration Excel file of manage-active-services rows, validates every row, emits a validation workbook, pauses for your approval, then applies changes in Dynamics 365 F&SCM and emits a before/after c', 'example_request': 'Bulk-update manage active services in USMF sandbox from this Excel file — validate first and show me the dry run.', 'inputs': [{'description': 'Attached Excel file with one row per manage active services target and the new field values.', 'name': 'configuration_workbook'}, {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-apply manage active services configuration changes in Dynamics 365 F&SCM from a spreadsheet, with dry-run validation and approval first.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureManageActiveServices(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureManageActiveServices'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_workbook': {'description': 'Attached Excel file with one row per manage active services target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureManageActiveServices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
