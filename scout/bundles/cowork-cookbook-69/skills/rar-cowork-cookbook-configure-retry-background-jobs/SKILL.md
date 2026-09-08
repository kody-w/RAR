---
name: "rar-cowork-cookbook-configure-retry-background-jobs"
description: "Bulk-applies retry background job configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies and returns before/after"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_retry_background_jobs", "rar_sha256": "50c0436795ca109478e390778e53d2ae93c78a87b9e8157ea758a7062ae6ec0f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
