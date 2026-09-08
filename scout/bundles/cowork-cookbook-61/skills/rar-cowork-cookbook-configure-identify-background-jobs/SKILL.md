---
name: "rar-cowork-cookbook-configure-identify-background-jobs"
description: "Applies bulk background-job configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a before/af"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_identify_background_jobs", "rar_sha256": "4db637e0436139408a91c97150f2317470be7fa33b754a9fb72592ee2e86c5c6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_identify_background_jobs`. The original RAPP
agent is preserved byte-for-byte in `configure_identify_background_jobs_agent.py` and in the RCI capsule.

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

Identify background jobs Configuration Bulk Setup — Applies bulk background-job configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a before/af

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-identify-background-jobs
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
      "description": "Attached Excel file with one row per identify background jobs target and the new field values.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_identify_background_jobs_agent.py` and embedded as the fenced Python below (sha256 4db637e043613940…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_identify_background_jobs_agent.py` first:

```bash
python3 configure_identify_background_jobs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_identify_background_jobs_agent.py   # or on stdin
python3 configure_identify_background_jobs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify background jobs Configuration Bulk Setup — Applies bulk background-job configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a before/af

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-identify-background-jobs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_identify_background_jobs',
    "version": '3.0.3',
    "display_name": 'Identify background jobs Configuration Bulk Setup',
    "description": 'Applies bulk background-job configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a before/af',
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
        "upstream_slug": 'configure-identify-background-jobs',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-identify-background-jobs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e7b0a01c32344bcd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/identify-background-jobs'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-identify-background-jobs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per identify background jobs target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; run sandbox first before production.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for identify background jobs, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per identify background jobs target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies bulk background-job configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a before/af', 'example_request': 'Bulk-update the background job config in USMF sandbox from this Excel file — validate first and show me the dry run.', 'inputs': [{'description': 'Attached Excel file with one row per identify background jobs target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target environment; run sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to bulk-update identify background jobs config in D365 F&SCM from a spreadsheet, with dry-run validation and approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureIdentifyBackgroundJobs(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureIdentifyBackgroundJobs'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per identify background jobs target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; run sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureIdentifyBackgroundJobs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
