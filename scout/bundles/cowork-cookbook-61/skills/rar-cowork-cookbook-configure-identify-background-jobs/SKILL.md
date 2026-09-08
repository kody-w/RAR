---
name: "rar-cowork-cookbook-configure-identify-background-jobs"
description: "Applies bulk background-job configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a before/af"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_identify_background_jobs", "rar_sha256": "4db637e0436139408a91c97150f2317470be7fa33b754a9fb72592ee2e86c5c6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
