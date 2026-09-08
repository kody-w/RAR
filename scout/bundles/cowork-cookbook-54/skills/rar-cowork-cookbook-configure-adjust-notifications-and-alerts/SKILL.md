---
name: "rar-cowork-cookbook-configure-adjust-notifications-and-alerts"
description: "Bulk-applies notification and alert configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then emits a before/after confirma"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_adjust_notifications_and_alerts", "rar_sha256": "c5784944d696630205c789c25232134370e6701587771ca90e244399409c4a43", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
