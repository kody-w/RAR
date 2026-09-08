---
name: "rar-cowork-cookbook-configure-re-assign-case-to-another-team-individual"
description: "Reads an attached Excel file of case re-assignment targets, validates every row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, and after your approval applies the changes with a before/aft"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_re_assign_case_to_another_team_individual", "rar_sha256": "963b4901d88a2e5a7dc705ba7d874756fc2cbf96561ef259ce6dc6a6a77e979a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_re_assign_case_to_another_team_individual`. The original RAPP
agent is preserved byte-for-byte in `configure_re_assign_case_to_another_team_individual_agent.py` and in the RCI capsule.

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

Re-assign case to another team/individual Configuration Bulk Setup — Reads an attached Excel file of case re-assignment targets, validates every row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, and after your approval applies the changes with a before/aft

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-re-assign-case-to-another-team-individual
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
      "description": "Excel file with one row per case re-assignment target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to run against (e.g. USMF); sandbox first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_re_assign_case_to_another_team_individual_agent.py` and embedded as the fenced Python below (sha256 963b4901d88a2e5a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_re_assign_case_to_another_team_individual_agent.py` first:

```bash
python3 configure_re_assign_case_to_another_team_individual_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_re_assign_case_to_another_team_individual_agent.py   # or on stdin
python3 configure_re_assign_case_to_another_team_individual_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Re-assign case to another team/individual Configuration Bulk Setup — Reads an attached Excel file of case re-assignment targets, validates every row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, and after your approval applies the changes with a before/aft

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-re-assign-case-to-another-team-individual
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_re_assign_case_to_another_team_individual',
    "version": '3.0.3',
    "display_name": 'Re-assign case to another team/individual Configuration Bulk Setup',
    "description": 'Reads an attached Excel file of case re-assignment targets, validates every row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, and after your approval applies the changes with a before/aft',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-re-assign-case-to-another-team-individual',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-re-assign-case-to-another-team-individual',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '077475467d08273f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/re-assign-case-to-another-team-individual'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/configure-re-assign-case-to-another-team-individual', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'configuration_excel_file': 'Excel file with one row per case re-assignment target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against (e.g. USMF); sandbox first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for re-assign case to another team/individual, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per re-assign case to another team/individual target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached Excel file of case re-assignment targets, validates every row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, and after your approval applies the changes with a before/aft', 'example_request': 'Bulk re-assign these cases to new owners from my attached Excel in USMF sandbox — validate first, then ask me before applying.', 'inputs': [{'description': 'Excel file with one row per case re-assignment target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'Dynamics 365 legal entity to run against (e.g. USMF); sandbox first.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to bulk re-assign cases to another team or individual in Dynamics 365 from a spreadsheet, with dry-run validation and approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureReAssignCaseToAnotherTeamIndividual(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureReAssignCaseToAnotherTeamIndividual'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Excel file with one row per case re-assignment target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against (e.g. USMF); sandbox first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureReAssignCaseToAnotherTeamIndividual().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
