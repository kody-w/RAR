---
name: "rar-cowork-cookbook-configure-manage-support-incidents"
description: "Reads an attached configuration Excel file of support-incident targets in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, pauses for approval, then applies changes and emits a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_support_incidents", "rar_sha256": "31d2c99e9fd7e2c755dbea5253f9ea63b327316ceb702927a18eae79df0cf7fe", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
