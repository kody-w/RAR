---
name: "rar-cowork-cookbook-configure-configure-monitor-and-send-emails"
description: "Applies a bulk email-configuration change in Dynamics 365 F&SCM from an Excel file: validates each row, emits a validation workbook, waits for your approval, then applies changes and emits a before/after confirmation wor"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_configure_monitor_and_send_emails", "rar_sha256": "3dc0f56b3d6296e911544e2b4d0f30579d2ca70ebbb141579a6a157ecec66b24", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_configure_monitor_and_send_emails`. The original RAPP
agent is preserved byte-for-byte in `configure_configure_monitor_and_send_emails_agent.py` and in the RCI capsule.

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

Configure, monitor, and send emails Configuration Bulk Setup — Applies a bulk email-configuration change in Dynamics 365 F&SCM from an Excel file: validates each row, emits a validation workbook, waits for your approval, then applies changes and emits a before/after confirmation wor

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-configure-monitor-and-send-emails
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
      "description": "Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per email-configuration target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF; use a sandbox first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_configure_monitor_and_send_emails_agent.py` and embedded as the fenced Python below (sha256 3dc0f56b3d6296e9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_configure_monitor_and_send_emails_agent.py` first:

```bash
python3 configure_configure_monitor_and_send_emails_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_configure_monitor_and_send_emails_agent.py   # or on stdin
python3 configure_configure_monitor_and_send_emails_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure, monitor, and send emails Configuration Bulk Setup — Applies a bulk email-configuration change in Dynamics 365 F&SCM from an Excel file: validates each row, emits a validation workbook, waits for your approval, then applies changes and emits a before/after confirmation wor

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-configure-monitor-and-send-emails
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_configure_monitor_and_send_emails',
    "version": '3.0.3',
    "display_name": 'Configure, monitor, and send emails Configuration Bulk Setup',
    "description": 'Applies a bulk email-configuration change in Dynamics 365 F&SCM from an Excel file: validates each row, emits a validation workbook, waits for your approval, then applies changes and emits a before/after confirmation wor',
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
        "upstream_slug": 'configure-configure-monitor-and-send-emails',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-configure-monitor-and-send-emails',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9a48d0ffc758c6d3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-monitor-and-send-emails'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-configure-monitor-and-send-emails', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per email-configuration target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF; use a sandbox first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for configure, monitor, and send emails, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per configure, monitor, and send emails target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk email-configuration change in Dynamics 365 F&SCM from an Excel file: validates each row, emits a validation workbook, waits for your approval, then applies changes and emits a before/after confirmation wor', 'example_request': 'Bulk-update email configuration in USMF sandbox from this attached Excel file — validate first and show me the dry run.', 'inputs': [{'description': 'Attached Excel file with one row per email-configuration target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox first.', 'name': 'legal_entity'}, {'description': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you have an Excel file of per-target email configuration field values to bulk-apply in D365 F&SCM, with dry-run validation and approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureConfigureMonitorAndSendEmails(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureConfigureMonitorAndSendEmails'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per email-configuration target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureConfigureMonitorAndSendEmails().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
