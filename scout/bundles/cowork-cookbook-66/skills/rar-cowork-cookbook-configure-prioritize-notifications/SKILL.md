---
name: "rar-cowork-cookbook-configure-prioritize-notifications"
description: "Runs a bulk prioritize-notifications configuration update in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies changes and returns a befo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_prioritize_notifications", "rar_sha256": "0af3951043d81bb2c8f73b020d5f55e44597850d543a1e1ad8a479ee1252bd0c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
