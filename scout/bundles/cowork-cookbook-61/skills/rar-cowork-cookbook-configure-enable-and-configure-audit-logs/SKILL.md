---
name: "rar-cowork-cookbook-configure-enable-and-configure-audit-logs"
description: "Reads an attached Excel file of audit log configuration rows for a D365 F&SCM legal entity, validates each row, returns a validation workbook, then after your approval applies the changes and returns a before/after confi"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_enable_and_configure_audit_logs", "rar_sha256": "9fca41361d79ae408f87a57844d9c66704b259a0b7f52cee096ac6a2c17c059c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_enable_and_configure_audit_logs`. The original RAPP
agent is preserved byte-for-byte in `configure_enable_and_configure_audit_logs_agent.py` and in the RCI capsule.

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

Enable and configure audit logs Configuration Bulk Setup — Reads an attached Excel file of audit log configuration rows for a D365 F&SCM legal entity, validates each row, returns a validation workbook, then after your approval applies the changes and returns a before/after confi

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-enable-and-configure-audit-logs
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
    "configuration_workbook": {
      "description": "Attached Excel file with one row per audit log target and the new field values.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_enable_and_configure_audit_logs_agent.py` and embedded as the fenced Python below (sha256 9fca41361d79ae40…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_enable_and_configure_audit_logs_agent.py` first:

```bash
python3 configure_enable_and_configure_audit_logs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_enable_and_configure_audit_logs_agent.py   # or on stdin
python3 configure_enable_and_configure_audit_logs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Enable and configure audit logs Configuration Bulk Setup — Reads an attached Excel file of audit log configuration rows for a D365 F&SCM legal entity, validates each row, returns a validation workbook, then after your approval applies the changes and returns a before/after confi

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-enable-and-configure-audit-logs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_enable_and_configure_audit_logs',
    "version": '3.0.3',
    "display_name": 'Enable and configure audit logs Configuration Bulk Setup',
    "description": 'Reads an attached Excel file of audit log configuration rows for a D365 F&SCM legal entity, validates each row, returns a validation workbook, then after your approval applies the changes and returns a before/after confi',
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
        "upstream_slug": 'configure-enable-and-configure-audit-logs',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-enable-and-configure-audit-logs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e6b066271e5e6ec9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/enable-and-configure-audit-logs'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-enable-and-configure-audit-logs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'configuration_workbook': 'Attached Excel file with one row per audit log target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; sandbox first before production.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for enable and configure audit logs, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per enable and configure audit logs target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached Excel file of audit log configuration rows for a D365 F&SCM legal entity, validates each row, returns a validation workbook, then after your approval applies the changes and returns a before/after confi', 'example_request': 'Bulk enable audit logs in USMF sandbox from this config spreadsheet — validate first and show me the dry run.', 'inputs': [{'description': 'Attached Excel file with one row per audit log target and the new field values.', 'name': 'configuration_workbook'}, {'description': 'D365 legal entity to run against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target environment; sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk enable and configure audit logs in Dynamics 365 F&SCM from a spreadsheet, with dry-run validation and approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureEnableAndConfigureAuditLogs(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureEnableAndConfigureAuditLogs'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_workbook': {'description': 'Attached Excel file with one row per audit log target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureEnableAndConfigureAuditLogs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
