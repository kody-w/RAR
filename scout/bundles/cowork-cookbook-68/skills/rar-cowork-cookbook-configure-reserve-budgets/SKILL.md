---
name: "rar-cowork-cookbook-configure-reserve-budgets"
description: "Bulk-updates reserve budget records in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/after confirma"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_reserve_budgets", "rar_sha256": "c27fba8d1f0b5d8793bd281115191fdc0fa45b70630ba1367bbe13f82ded091d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
