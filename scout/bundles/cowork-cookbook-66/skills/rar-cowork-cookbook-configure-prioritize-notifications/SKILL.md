---
name: "rar-cowork-cookbook-configure-prioritize-notifications"
description: "Runs a bulk prioritize-notifications configuration update in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies changes and returns a befo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_prioritize_notifications", "rar_sha256": "0af3951043d81bb2c8f73b020d5f55e44597850d543a1e1ad8a479ee1252bd0c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_prioritize_notifications`. The original RAPP
agent is preserved byte-for-byte in `configure_prioritize_notifications_agent.py` and in the RCI capsule.

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

Prioritize notifications Configuration Bulk Setup — Runs a bulk prioritize-notifications configuration update in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies changes and returns a befo

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-prioritize-notifications
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
    "configuration_excel_file": {
      "description": "Attached workbook with one row per prioritize notifications target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Which environment to target; sandbox first before production.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_prioritize_notifications_agent.py` and embedded as the fenced Python below (sha256 0af3951043d81bb2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_prioritize_notifications_agent.py` first:

```bash
python3 configure_prioritize_notifications_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_prioritize_notifications_agent.py   # or on stdin
python3 configure_prioritize_notifications_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Prioritize notifications Configuration Bulk Setup — Runs a bulk prioritize-notifications configuration update in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies changes and returns a befo

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-prioritize-notifications
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_prioritize_notifications',
    "version": '3.0.3',
    "display_name": 'Prioritize notifications Configuration Bulk Setup',
    "description": 'Runs a bulk prioritize-notifications configuration update in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies changes and returns a befo',
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
        "upstream_slug": 'configure-prioritize-notifications',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-prioritize-notifications',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '089ea2869c4f84ba',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-notifications-alerts/prioritize-notifications'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-prioritize-notifications', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'configuration_excel_file': 'Attached workbook with one row per prioritize notifications target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Which environment to target; sandbox first before production.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for prioritize notifications, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per prioritize notifications target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a bulk prioritize-notifications configuration update in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies changes and returns a befo', 'example_request': 'Bulk-update prioritize notifications in USMF sandbox from this Excel file — validate first and show me the results before applying.', 'inputs': [{'description': 'Attached workbook with one row per prioritize notifications target and the new field values.', 'name': 'configuration Excel file'}, {'description': 'D365 legal entity to run against, e.g. USMF.', 'name': 'legal entity'}, {'description': 'Which environment to target; sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to bulk-update prioritize notifications settings in D365 F&SCM from a spreadsheet, with row validation and an approval gate before any writes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigurePrioritizeNotifications(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePrioritizeNotifications'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached workbook with one row per prioritize notifications target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Which environment to target; sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigurePrioritizeNotifications().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
