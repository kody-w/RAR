---
name: "rar-cowork-cookbook-configure-schedule-production-jobs"
description: "Bulk-applies schedule production job configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_schedule_production_jobs", "rar_sha256": "648214b4b527bb7a0c5006eb743e41e48369b31558d4692f36871feab403dcc8", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
