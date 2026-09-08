---
name: "rar-cowork-cookbook-configure-receive-service-requests"
description: "Bulk-applies receive service request configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies and returns a before/afte"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_receive_service_requests", "rar_sha256": "b5f757a2ac24faa08fbf3791cabe7b54ff8d33ebf657e66cefb61193da206b09", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
