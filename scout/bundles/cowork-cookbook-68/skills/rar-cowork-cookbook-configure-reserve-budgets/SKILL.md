---
name: "rar-cowork-cookbook-configure-reserve-budgets"
description: "Bulk-updates reserve budget records in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/after confirma"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_reserve_budgets", "rar_sha256": "c27fba8d1f0b5d8793bd281115191fdc0fa45b70630ba1367bbe13f82ded091d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_reserve_budgets`. The original RAPP
agent is preserved byte-for-byte in `configure_reserve_budgets_agent.py` and in the RCI capsule.

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

Reserve budgets Configuration Bulk Setup — Bulk-updates reserve budget records in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/after confirma

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-reserve-budgets
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
      "description": "Explicit user approval after reviewing the validation workbook, before changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per reserve budget target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Sandbox or production target; sandbox first is required.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (e.g. USMF).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_reserve_budgets_agent.py` and embedded as the fenced Python below (sha256 c27fba8d1f0b5d87…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_reserve_budgets_agent.py` first:

```bash
python3 configure_reserve_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_reserve_budgets_agent.py   # or on stdin
python3 configure_reserve_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reserve budgets Configuration Bulk Setup — Bulk-updates reserve budget records in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/after confirma

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-reserve-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_reserve_budgets',
    "version": '3.0.3',
    "display_name": 'Reserve budgets Configuration Bulk Setup',
    "description": 'Bulk-updates reserve budget records in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/after confirma',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-reserve-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-reserve-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bb0a940d0ff3a014',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/reserve-budgets'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/configure-reserve-budgets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the validation workbook, before changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per reserve budget target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Sandbox or production target; sandbox first is required.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for reserve budgets, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per reserve budgets target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Bulk-updates reserve budget records in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/after confirma', 'example_request': 'Run the reserve budget bulk setup on USMF sandbox using my attached config spreadsheet — validate first.', 'inputs': [{'description': 'Attached Excel file with one row per reserve budget target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Sandbox or production target; sandbox first is required.', 'name': 'environment'}, {'description': 'Explicit user approval after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to apply reserve budget configuration changes in bulk from a spreadsheet, with row-level validation and an approval gate before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureReserveBudgets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureReserveBudgets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per reserve budget target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Sandbox or production target; sandbox first is required.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureReserveBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
