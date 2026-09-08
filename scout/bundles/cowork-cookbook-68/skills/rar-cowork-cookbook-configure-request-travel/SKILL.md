---
name: "rar-cowork-cookbook-configure-request-travel"
description: "Applies bulk request-travel configuration changes in Dynamics 365 F&SCM from an Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a before/after confi"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_request_travel", "rar_sha256": "24b3ebe8020a83e39f9d7d347c08afae63d06573ec54abfd2064dc98bd8357a2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
