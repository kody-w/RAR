---
name: "rar-cowork-cookbook-configure-re-assign-case-to-another-team-individual"
description: "Reads an attached Excel file of case re-assignment targets, validates every row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, and after your approval applies the changes with a before/aft"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_re_assign_case_to_another_team_individual", "rar_sha256": "963b4901d88a2e5a7dc705ba7d874756fc2cbf96561ef259ce6dc6a6a77e979a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
