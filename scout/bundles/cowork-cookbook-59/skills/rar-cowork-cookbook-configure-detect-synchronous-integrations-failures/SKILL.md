---
name: "rar-cowork-cookbook-configure-detect-synchronous-integrations-failures"
description: "Bulk-applies configuration changes for detecting synchronous integrations failures in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies c"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_detect_synchronous_integrations_failures", "rar_sha256": "f6f5e0e56cece700f7c77d4ac5177646fd8b24d39f49e973239c615f3c9fcc31", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_detect_synchronous_integrations_failures`. The original RAPP
agent is preserved byte-for-byte in `configure_detect_synchronous_integrations_failures_agent.py` and in the RCI capsule.

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

Detect synchronous integrations failures Configuration Bulk Setup — Bulk-applies configuration changes for detecting synchronous integrations failures in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies c

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-detect-synchronous-integrations-failures
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
      "description": "Explicit approval after reviewing the validation workbook, before changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per target record and the new field values.",
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
      "description": "D365 legal entity to run against (e.g. USMF).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_detect_synchronous_integrations_failures_agent.py` and embedded as the fenced Python below (sha256 f6f5e0e56cece700…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_detect_synchronous_integrations_failures_agent.py` first:

```bash
python3 configure_detect_synchronous_integrations_failures_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_detect_synchronous_integrations_failures_agent.py   # or on stdin
python3 configure_detect_synchronous_integrations_failures_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Detect synchronous integrations failures Configuration Bulk Setup — Bulk-applies configuration changes for detecting synchronous integrations failures in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies c

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-detect-synchronous-integrations-failures
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_detect_synchronous_integrations_failures',
    "version": '3.0.3',
    "display_name": 'Detect synchronous integrations failures Configuration Bulk Setup',
    "description": 'Bulk-applies configuration changes for detecting synchronous integrations failures in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies c',
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
        "upstream_slug": 'configure-detect-synchronous-integrations-failures',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-detect-synchronous-integrations-failures',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b4006460ad68a378',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/detect-synchronous-integrations-failures'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-detect-synchronous-integrations-failures', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the validation workbook, before changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per target record and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; sandbox first before production.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for detect synchronous integrations failures, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per detect synchronous integrations failures target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Bulk-applies configuration changes for detecting synchronous integrations failures in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies c', 'example_request': 'Use my attached config Excel to bulk update sync integration failure detection in USMF sandbox — validate first, then ask me.', 'inputs': [{'description': 'Attached Excel file with one row per target record and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Target environment; sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit approval after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to change synchronous integration failure detection settings for many records at once from a spreadsheet, with dry-run validation and approval before writes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureDetectSynchronousIntegrationsFailures(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDetectSynchronousIntegrationsFailures'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per target record and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureDetectSynchronousIntegrationsFailures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
