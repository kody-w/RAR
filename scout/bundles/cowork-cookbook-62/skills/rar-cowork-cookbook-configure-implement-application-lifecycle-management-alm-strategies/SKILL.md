---
name: "rar-cowork-cookbook-configure-implement-application-lifecycle-management-alm-strategies"
description: "Bulk-applies ALM configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a before/after confirm"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_implement_application_lifecycle_management_alm_strategies", "rar_sha256": "ed46f7580c88a45d85f34e32cdf72b4dc68c11d49a06c54267f24908e424a034", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_implement_application_lifecycle_management_alm_strategies`. The original RAPP
agent is preserved byte-for-byte in `configure_implement_application_lifecycle_management_alm_strategies_agent.py` and in the RCI capsule.

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

Implement application lifecycle management (ALM) strategies Configuration Bulk Setup — Bulk-applies ALM configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a before/after confirm

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-implement-application-lifecycle-management-alm-strategies
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
      "description": "Explicit go-ahead after reviewing the validation workbook, before changes are applied.",
      "type": "string"
    },
    "configuration_excel": {
      "description": "Excel file with one row per ALM target and the new field values.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_implement_application_lifecycle_management_alm_strategies_agent.py` and embedded as the fenced Python below (sha256 ed46f7580c88a45d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_implement_application_lifecycle_management_alm_strategies_agent.py` first:

```bash
python3 configure_implement_application_lifecycle_management_alm_strategies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_implement_application_lifecycle_management_alm_strategies_agent.py   # or on stdin
python3 configure_implement_application_lifecycle_management_alm_strategies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement application lifecycle management (ALM) strategies Configuration Bulk Setup — Bulk-applies ALM configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a before/after confirm

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-implement-application-lifecycle-management-alm-strategies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_implement_application_lifecycle_management_alm_strategies',
    "version": '3.0.3',
    "display_name": 'Implement application lifecycle management (ALM) strategies Configuration Bulk Setup',
    "description": 'Bulk-applies ALM configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a before/after confirm',
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
        "upstream_slug": 'configure-implement-application-lifecycle-management-alm-strategies',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-implement-application-lifecycle-management-alm-strategies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '836ad36ec58d2f3e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/implement-application-lifecycle-management-alm-strategies'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-implement-application-lifecycle-management-alm-strategies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'configuration_excel': 'Excel file with one row per ALM target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; run sandbox first before production.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for implement application lifecycle management (ALM) strategies, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per implement application lifecycle management (ALM) strategies target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Bulk-applies ALM configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a before/after confirm', 'example_request': 'Run the ALM bulk config update on USMF sandbox using this Excel file — validate first and show me the results before applying.', 'inputs': [{'description': 'Excel file with one row per ALM target and the new field values.', 'name': 'configuration_excel'}, {'description': 'D365 legal entity to run against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target environment; run sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to apply ALM configuration updates in bulk to D365 F&SCM from a spreadsheet, with row-level validation and an approval gate before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureImplementApplicationLifecycleManagementAlmStrategies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureImplementApplicationLifecycleManagementAlmStrategies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_excel': {'description': 'Excel file with one row per ALM target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; run sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureImplementApplicationLifecycleManagementAlmStrategies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
