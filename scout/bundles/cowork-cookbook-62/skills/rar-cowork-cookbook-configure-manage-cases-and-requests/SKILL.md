---
name: "rar-cowork-cookbook-configure-manage-cases-and-requests"
description: "Reads an attached configuration Excel file of case/request updates in Dynamics 365 (legal entity USMF), validates every row, returns a validation workbook, and after your approval applies changes with a before/after conf"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_cases_and_requests", "rar_sha256": "02e586f72c4db82a151e06279e255df6540015296658a9d178cba9422b92a84c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_manage_cases_and_requests`. The original RAPP
agent is preserved byte-for-byte in `configure_manage_cases_and_requests_agent.py` and in the RCI capsule.

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

Manage cases and requests Configuration Bulk Setup — Reads an attached configuration Excel file of case/request updates in Dynamics 365 (legal entity USMF), validates every row, returns a validation workbook, and after your approval applies changes with a before/after conf

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-cases-and-requests
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
      "description": "Explicit go-ahead after reviewing the validation workbook, required before changes are applied.",
      "type": "string"
    },
    "configuration_excel": {
      "description": "Attached Excel file with one row per manage cases and requests target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Target environment \u2014 run sandbox first before production.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against; recipe default is USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_cases_and_requests_agent.py` and embedded as the fenced Python below (sha256 02e586f72c4db82a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_cases_and_requests_agent.py` first:

```bash
python3 configure_manage_cases_and_requests_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_manage_cases_and_requests_agent.py   # or on stdin
python3 configure_manage_cases_and_requests_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage cases and requests Configuration Bulk Setup — Reads an attached configuration Excel file of case/request updates in Dynamics 365 (legal entity USMF), validates every row, returns a validation workbook, and after your approval applies changes with a before/after conf

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-cases-and-requests
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_manage_cases_and_requests',
    "version": '3.0.3',
    "display_name": 'Manage cases and requests Configuration Bulk Setup',
    "description": 'Reads an attached configuration Excel file of case/request updates in Dynamics 365 (legal entity USMF), validates every row, returns a validation workbook, and after your approval applies changes with a before/after conf',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-manage-cases-and-requests',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-manage-cases-and-requests',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '613e559157853cc8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-workplace-compliance/manage-cases-and-requests'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/configure-manage-cases-and-requests', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, required before changes are applied.', 'configuration_excel': 'Attached Excel file with one row per manage cases and requests target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment — run sandbox first before production.', 'legal_entity': 'D365 legal entity to run against; recipe default is USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for manage cases and requests, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per manage cases and requests target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached configuration Excel file of case/request updates in Dynamics 365 (legal entity USMF), validates every row, returns a validation workbook, and after your approval applies changes with a before/after conf', 'example_request': 'Bulk-update our case and request config in USMF sandbox from this Excel file — validate first and show me the dry run.', 'inputs': [{'description': 'Attached Excel file with one row per manage cases and requests target and the new field values.', 'name': 'configuration_excel'}, {'description': 'D365 legal entity to run against; recipe default is USMF.', 'name': 'legal_entity'}, {'description': 'Target environment — run sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, required before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-update manage cases and requests configuration in D365 F&SCM from a spreadsheet, with dry-run validation and approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureManageCasesAndRequests(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureManageCasesAndRequests'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, required before changes are applied.', 'type': 'string'}, 'configuration_excel': {'description': 'Attached Excel file with one row per manage cases and requests target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment — run sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; recipe default is USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureManageCasesAndRequests().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
