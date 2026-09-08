---
name: "rar-cowork-cookbook-configure-schedule-production-jobs"
description: "Bulk-applies schedule production job configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_schedule_production_jobs", "rar_sha256": "648214b4b527bb7a0c5006eb743e41e48369b31558d4692f36871feab403dcc8", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_schedule_production_jobs`. The original RAPP
agent is preserved byte-for-byte in `configure_schedule_production_jobs_agent.py` and in the RCI capsule.

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

Schedule production jobs Configuration Bulk Setup — Bulk-applies schedule production job configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-schedule-production-jobs
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
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per schedule production jobs target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF; use a sandbox environment first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_schedule_production_jobs_agent.py` and embedded as the fenced Python below (sha256 648214b4b527bb7a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_schedule_production_jobs_agent.py` first:

```bash
python3 configure_schedule_production_jobs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_schedule_production_jobs_agent.py   # or on stdin
python3 configure_schedule_production_jobs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Schedule production jobs Configuration Bulk Setup — Bulk-applies schedule production job configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-schedule-production-jobs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_schedule_production_jobs',
    "version": '3.0.3',
    "display_name": 'Schedule production jobs Configuration Bulk Setup',
    "description": 'Bulk-applies schedule production job configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-schedule-production-jobs',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-schedule-production-jobs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd652b12462c9096f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/plan-production-operations/schedule-production-jobs'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/configure-schedule-production-jobs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per schedule production jobs target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for schedule production jobs, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per schedule production jobs target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Bulk-applies schedule production job configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a', 'example_request': 'Bulk update schedule production jobs in USMF sandbox from this Excel file — validate first and show me the dry run.', 'inputs': [{'description': 'Attached Excel file with one row per schedule production jobs target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to update many schedule production job configurations at once from a spreadsheet, with row-level validation and an approval gate before writes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureScheduleProductionJobs(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureScheduleProductionJobs'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per schedule production jobs target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureScheduleProductionJobs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
