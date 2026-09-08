---
name: "rar-cowork-cookbook-configure-adjust-notifications-and-alerts"
description: "Bulk-applies notification and alert configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then emits a before/after confirma"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_adjust_notifications_and_alerts", "rar_sha256": "c5784944d696630205c789c25232134370e6701587771ca90e244399409c4a43", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_adjust_notifications_and_alerts`. The original RAPP
agent is preserved byte-for-byte in `configure_adjust_notifications_and_alerts_agent.py` and in the RCI capsule.

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

Adjust notifications and alerts Configuration Bulk Setup — Bulk-applies notification and alert configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then emits a before/after confirma

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-adjust-notifications-and-alerts
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
      "description": "Excel file with one row per notification/alert target and the new field values.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_adjust_notifications_and_alerts_agent.py` and embedded as the fenced Python below (sha256 c5784944d6966302…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_adjust_notifications_and_alerts_agent.py` first:

```bash
python3 configure_adjust_notifications_and_alerts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_adjust_notifications_and_alerts_agent.py   # or on stdin
python3 configure_adjust_notifications_and_alerts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Adjust notifications and alerts Configuration Bulk Setup — Bulk-applies notification and alert configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then emits a before/after confirma

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-adjust-notifications-and-alerts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_adjust_notifications_and_alerts',
    "version": '3.0.3',
    "display_name": 'Adjust notifications and alerts Configuration Bulk Setup',
    "description": 'Bulk-applies notification and alert configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then emits a before/after confirma',
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
        "upstream_slug": 'configure-adjust-notifications-and-alerts',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-adjust-notifications-and-alerts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '88ad3b179e22ff30',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-notifications-alerts/adjust-notifications-and-alerts'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-adjust-notifications-and-alerts', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'configuration_excel': 'Excel file with one row per notification/alert target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF; use a sandbox first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for adjust notifications and alerts, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per adjust notifications and alerts target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Bulk-applies notification and alert configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then emits a before/after confirma', 'example_request': "Here's my alerts config spreadsheet — validate it against USMF sandbox and show me what would change before applying.", 'inputs': [{'description': 'Excel file with one row per notification/alert target and the new field values.', 'name': 'configuration_excel'}, {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox first.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change notification/alert settings for many D365 records at once from a spreadsheet, with a dry-run preview and approval before any writes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureAdjustNotificationsAndAlerts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAdjustNotificationsAndAlerts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_excel': {'description': 'Excel file with one row per notification/alert target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureAdjustNotificationsAndAlerts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
