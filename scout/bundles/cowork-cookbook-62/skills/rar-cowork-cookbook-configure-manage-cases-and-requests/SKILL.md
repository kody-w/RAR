---
name: "rar-cowork-cookbook-configure-manage-cases-and-requests"
description: "Reads an attached configuration Excel file of case/request updates in Dynamics 365 (legal entity USMF), validates every row, returns a validation workbook, and after your approval applies changes with a before/after conf"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_cases_and_requests", "rar_sha256": "02e586f72c4db82a151e06279e255df6540015296658a9d178cba9422b92a84c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
