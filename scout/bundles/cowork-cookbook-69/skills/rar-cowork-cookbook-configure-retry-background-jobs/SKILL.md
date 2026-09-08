---
name: "rar-cowork-cookbook-configure-retry-background-jobs"
description: "Bulk-applies retry background job configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies and returns before/after"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_retry_background_jobs", "rar_sha256": "50c0436795ca109478e390778e53d2ae93c78a87b9e8157ea758a7062ae6ec0f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_retry_background_jobs`. The original RAPP
agent is preserved byte-for-byte in `configure_retry_background_jobs_agent.py` and in the RCI capsule.

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

Retry background jobs Configuration Bulk Setup — Bulk-applies retry background job configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies and returns before/after

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-retry-background-jobs
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
    "configuration_excel": {
      "description": "Excel file with one row per retry background jobs target and the new field values.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_retry_background_jobs_agent.py` and embedded as the fenced Python below (sha256 50c0436795ca1094…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_retry_background_jobs_agent.py` first:

```bash
python3 configure_retry_background_jobs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_retry_background_jobs_agent.py   # or on stdin
python3 configure_retry_background_jobs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Retry background jobs Configuration Bulk Setup — Bulk-applies retry background job configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies and returns before/after

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-retry-background-jobs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_retry_background_jobs',
    "version": '3.0.3',
    "display_name": 'Retry background jobs Configuration Bulk Setup',
    "description": 'Bulk-applies retry background job configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies and returns before/after',
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
        "upstream_slug": 'configure-retry-background-jobs',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-retry-background-jobs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9e8ddef6e7d053b5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/retry-background-jobs'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-retry-background-jobs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'configuration_excel': 'Excel file with one row per retry background jobs target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for retry background jobs, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per retry background jobs target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Bulk-applies retry background job configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies and returns before/after', 'example_request': 'Run the retry background jobs bulk config update in USMF sandbox using my attached Excel — validate first and wait for my approval.', 'inputs': [{'description': 'Excel file with one row per retry background jobs target and the new field values.', 'name': 'configuration_excel'}, {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to update retry background job settings in bulk for a D365 legal entity from a spreadsheet, with dry-run validation and approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureRetryBackgroundJobs(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureRetryBackgroundJobs'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_excel': {'description': 'Excel file with one row per retry background jobs target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureRetryBackgroundJobs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
