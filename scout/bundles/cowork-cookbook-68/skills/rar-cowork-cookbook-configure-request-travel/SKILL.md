---
name: "rar-cowork-cookbook-configure-request-travel"
description: "Applies bulk request-travel configuration changes in Dynamics 365 F&SCM from an Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a before/after confi"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_request_travel", "rar_sha256": "24b3ebe8020a83e39f9d7d347c08afae63d06573ec54abfd2064dc98bd8357a2", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_request_travel`. The original RAPP
agent is preserved byte-for-byte in `configure_request_travel_agent.py` and in the RCI capsule.

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

Request travel Configuration Bulk Setup — Applies bulk request-travel configuration changes in Dynamics 365 F&SCM from an Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a before/after confi

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-request-travel
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
      "description": "Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per request travel target and the new field values.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_request_travel_agent.py` and embedded as the fenced Python below (sha256 24b3ebe8020a83e3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_request_travel_agent.py` first:

```bash
python3 configure_request_travel_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_request_travel_agent.py   # or on stdin
python3 configure_request_travel_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Request travel Configuration Bulk Setup — Applies bulk request-travel configuration changes in Dynamics 365 F&SCM from an Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a before/after confi

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-request-travel
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_request_travel',
    "version": '3.0.3',
    "display_name": 'Request travel Configuration Bulk Setup',
    "description": 'Applies bulk request-travel configuration changes in Dynamics 365 F&SCM from an Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a before/after confi',
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
        "upstream_slug": 'configure-request-travel',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-request-travel',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a21194e14e01d0df',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-time-and-attendance/request-travel'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/configure-request-travel', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per request travel target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for request travel, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per request travel target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies bulk request-travel configuration changes in Dynamics 365 F&SCM from an Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a before/after confi', 'example_request': 'Bulk-update request travel config in USMF sandbox from this Excel file — validate first and show me the dry run.', 'inputs': [{'description': 'Attached Excel file with one row per request travel target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'name': 'legal_entity'}, {'description': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-update request travel configuration records in D365 F&SCM from a spreadsheet, with dry-run validation and approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureRequestTravel(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureRequestTravel'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per request travel target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureRequestTravel().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
