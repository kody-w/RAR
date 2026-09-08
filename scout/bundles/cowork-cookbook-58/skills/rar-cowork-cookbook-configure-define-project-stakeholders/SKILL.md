---
name: "rar-cowork-cookbook-configure-define-project-stakeholders"
description: "Bulk-applies project stakeholder configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then emits a before/after confirmation wo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_project_stakeholders", "rar_sha256": "f7fbcfd00c663b9328084c1eb21572a5cc73eea67f024d47fbfca7d850cd2987", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_define_project_stakeholders`. The original RAPP
agent is preserved byte-for-byte in `configure_define_project_stakeholders_agent.py` and in the RCI capsule.

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

Define project stakeholders Configuration Bulk Setup — Bulk-applies project stakeholder configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then emits a before/after confirmation wo

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-project-stakeholders
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
      "description": "Explicit go-ahead after reviewing the validation workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_excel": {
      "description": "Attached Excel file with one row per define-project-stakeholders target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF; use a sandbox environment first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_define_project_stakeholders_agent.py` and embedded as the fenced Python below (sha256 f7fbcfd00c663b93…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_define_project_stakeholders_agent.py` first:

```bash
python3 configure_define_project_stakeholders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_define_project_stakeholders_agent.py   # or on stdin
python3 configure_define_project_stakeholders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define project stakeholders Configuration Bulk Setup — Bulk-applies project stakeholder configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then emits a before/after confirmation wo

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-project-stakeholders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_define_project_stakeholders',
    "version": '3.0.3',
    "display_name": 'Define project stakeholders Configuration Bulk Setup',
    "description": 'Bulk-applies project stakeholder configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then emits a before/after confirmation wo',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-define-project-stakeholders',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-define-project-stakeholders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'aa26369efc01f75c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-contracts/define-project-stakeholders'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/configure-define-project-stakeholders', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_excel': 'Attached Excel file with one row per define-project-stakeholders target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for define project stakeholders, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per define project stakeholders target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Bulk-applies project stakeholder configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then emits a before/after confirmation wo', 'example_request': 'Bulk-define project stakeholders in USMF sandbox from this Excel file — validate first and show me the dry run before applying.', 'inputs': [{'description': 'Attached Excel file with one row per define-project-stakeholders target and the new field values.', 'name': 'configuration_excel'}, {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to define project stakeholders for many records at once from a spreadsheet, with pre-apply validation and an approval checkpoint.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureDefineProjectStakeholders(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDefineProjectStakeholders'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel': {'description': 'Attached Excel file with one row per define-project-stakeholders target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureDefineProjectStakeholders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
