---
name: "rar-cowork-cookbook-configure-manage-active-services"
description: "Reads an attached configuration Excel file of manage-active-services rows, validates every row, emits a validation workbook, pauses for your approval, then applies changes in Dynamics 365 F&SCM and emits a before/after c"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_active_services", "rar_sha256": "69cc10e0a575db6567f356091d9621a44c22be9a5e02370978a6db091c741cca", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
