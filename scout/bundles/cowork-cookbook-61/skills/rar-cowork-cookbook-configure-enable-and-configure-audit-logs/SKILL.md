---
name: "rar-cowork-cookbook-configure-enable-and-configure-audit-logs"
description: "Reads an attached Excel file of audit log configuration rows for a D365 F&SCM legal entity, validates each row, returns a validation workbook, then after your approval applies the changes and returns a before/after confi"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_enable_and_configure_audit_logs", "rar_sha256": "9fca41361d79ae408f87a57844d9c66704b259a0b7f52cee096ac6a2c17c059c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
