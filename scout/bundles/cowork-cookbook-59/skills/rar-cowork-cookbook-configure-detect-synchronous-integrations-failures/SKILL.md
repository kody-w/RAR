---
name: "rar-cowork-cookbook-configure-detect-synchronous-integrations-failures"
description: "Bulk-applies configuration changes for detecting synchronous integrations failures in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies c"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_detect_synchronous_integrations_failures", "rar_sha256": "f6f5e0e56cece700f7c77d4ac5177646fd8b24d39f49e973239c615f3c9fcc31", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
