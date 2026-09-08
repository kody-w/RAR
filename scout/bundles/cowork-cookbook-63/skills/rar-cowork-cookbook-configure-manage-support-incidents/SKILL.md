---
name: "rar-cowork-cookbook-configure-manage-support-incidents"
description: "Reads an attached configuration Excel file of support-incident targets in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, pauses for approval, then applies changes and emits a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_support_incidents", "rar_sha256": "31d2c99e9fd7e2c755dbea5253f9ea63b327316ceb702927a18eae79df0cf7fe", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_manage_support_incidents`. The original RAPP
agent is preserved byte-for-byte in `configure_manage_support_incidents_agent.py` and in the RCI capsule.

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

Manage support incidents Configuration Bulk Setup — Reads an attached configuration Excel file of support-incident targets in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, pauses for approval, then applies changes and emits a

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-support-incidents
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
      "description": "Explicit user approval after reviewing the validation workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_file": {
      "description": "Excel file with one row per manage-support-incidents target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Target environment \u2014 sandbox first before production.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against; defaults to USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_support_incidents_agent.py` and embedded as the fenced Python below (sha256 31d2c99e9fd7e2c7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_support_incidents_agent.py` first:

```bash
python3 configure_manage_support_incidents_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_manage_support_incidents_agent.py   # or on stdin
python3 configure_manage_support_incidents_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage support incidents Configuration Bulk Setup — Reads an attached configuration Excel file of support-incident targets in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, pauses for approval, then applies changes and emits a

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-support-incidents
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_manage_support_incidents',
    "version": '3.0.3',
    "display_name": 'Manage support incidents Configuration Bulk Setup',
    "description": 'Reads an attached configuration Excel file of support-incident targets in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, pauses for approval, then applies changes and emits a',
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
        "upstream_slug": 'configure-manage-support-incidents',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-manage-support-incidents',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '274ad33d1ee7b8e3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/support-systems/manage-support-incidents'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-manage-support-incidents', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'configuration_file': 'Excel file with one row per manage-support-incidents target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment — sandbox first before production.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for manage support incidents, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per manage support incidents target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached configuration Excel file of support-incident targets in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, pauses for approval, then applies changes and emits a', 'example_request': 'Bulk-update our support incident config in USMF sandbox from this Excel file — validate first and show me the dry run.', 'inputs': [{'description': 'Excel file with one row per manage-support-incidents target and the new field values.', 'name': 'configuration_file'}, {'description': 'D365 legal entity to run against; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Target environment — sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when the user wants to bulk-apply support incident configuration changes from a spreadsheet in D365 F&SCM with dry-run validation and approval before writing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureManageSupportIncidents(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureManageSupportIncidents'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_file': {'description': 'Excel file with one row per manage-support-incidents target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment — sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureManageSupportIncidents().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
