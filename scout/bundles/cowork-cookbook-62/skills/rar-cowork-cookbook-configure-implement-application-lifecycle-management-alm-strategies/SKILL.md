---
name: "rar-cowork-cookbook-configure-implement-application-lifecycle-management-alm-strategies"
description: "Bulk-applies ALM configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a before/after confirm"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_implement_application_lifecycle_management_alm_strategies", "rar_sha256": "ed46f7580c88a45d85f34e32cdf72b4dc68c11d49a06c54267f24908e424a034", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
