---
name: "rar-cowork-cookbook-configure-receive-service-requests"
description: "Bulk-applies receive service request configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies and returns a before/afte"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_receive_service_requests", "rar_sha256": "b5f757a2ac24faa08fbf3791cabe7b54ff8d33ebf657e66cefb61193da206b09", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_receive_service_requests`. The original RAPP
agent is preserved byte-for-byte in `configure_receive_service_requests_agent.py` and in the RCI capsule.

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

Receive service requests Configuration Bulk Setup — Bulk-applies receive service request configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies and returns a before/afte

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-receive-service-requests
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
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per receive service requests target and the new field values.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_receive_service_requests_agent.py` and embedded as the fenced Python below (sha256 b5f757a2ac24faa0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_receive_service_requests_agent.py` first:

```bash
python3 configure_receive_service_requests_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_receive_service_requests_agent.py   # or on stdin
python3 configure_receive_service_requests_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Receive service requests Configuration Bulk Setup — Bulk-applies receive service request configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies and returns a before/afte

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-receive-service-requests
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_receive_service_requests',
    "version": '3.0.3',
    "display_name": 'Receive service requests Configuration Bulk Setup',
    "description": 'Bulk-applies receive service request configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies and returns a before/afte',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-receive-service-requests',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-receive-service-requests',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '97b0fab425675e2f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work/receive-service-requests'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/configure-receive-service-requests', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per receive service requests target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; sandbox first before production.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for receive service requests, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per receive service requests target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Bulk-applies receive service request configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies and returns a before/afte', 'example_request': 'Run the receive service request bulk config update in USMF sandbox from this Excel file — validate first.', 'inputs': [{'description': 'Attached Excel file with one row per receive service requests target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target environment; sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to update many receive service request configuration records at once from a spreadsheet, with dry-run validation and approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureReceiveServiceRequests(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureReceiveServiceRequests'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per receive service requests target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureReceiveServiceRequests().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
