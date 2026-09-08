---
name: "rar-cowork-cookbook-configure-configure-monitor-and-send-emails"
description: "Applies a bulk email-configuration change in Dynamics 365 F&SCM from an Excel file: validates each row, emits a validation workbook, waits for your approval, then applies changes and emits a before/after confirmation wor"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_configure_monitor_and_send_emails", "rar_sha256": "3dc0f56b3d6296e911544e2b4d0f30579d2ca70ebbb141579a6a157ecec66b24", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
