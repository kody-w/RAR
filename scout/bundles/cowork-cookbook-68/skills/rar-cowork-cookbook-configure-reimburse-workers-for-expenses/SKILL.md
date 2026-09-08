---
name: "rar-cowork-cookbook-configure-reimburse-workers-for-expenses"
description: "Bulk-applies reimburse-workers-for-expenses configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for approval, then applies and reports before/a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_reimburse_workers_for_expenses", "rar_sha256": "ea65849707869ec739db51bff3b65d49a2a585380bc3320cd4412de0678c40ec", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_reimburse_workers_for_expenses`. The original RAPP
agent is preserved byte-for-byte in `configure_reimburse_workers_for_expenses_agent.py` and in the RCI capsule.

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

Reimburse workers for expenses Configuration Bulk Setup — Bulk-applies reimburse-workers-for-expenses configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for approval, then applies and reports before/a

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-reimburse-workers-for-expenses
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
      "description": "Attached Excel file with one row per reimburse-workers-for-expenses target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (e.g. USMF); use a sandbox environment first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_reimburse_workers_for_expenses_agent.py` and embedded as the fenced Python below (sha256 ea65849707869ec7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_reimburse_workers_for_expenses_agent.py` first:

```bash
python3 configure_reimburse_workers_for_expenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_reimburse_workers_for_expenses_agent.py   # or on stdin
python3 configure_reimburse_workers_for_expenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reimburse workers for expenses Configuration Bulk Setup — Bulk-applies reimburse-workers-for-expenses configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for approval, then applies and reports before/a

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-reimburse-workers-for-expenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_reimburse_workers_for_expenses',
    "version": '3.0.3',
    "display_name": 'Reimburse workers for expenses Configuration Bulk Setup',
    "description": 'Bulk-applies reimburse-workers-for-expenses configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for approval, then applies and reports before/a',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-reimburse-workers-for-expenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-reimburse-workers-for-expenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '359ae912a15fbb58',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-compensation-and-benefits/reimburse-workers-for-expenses'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/configure-reimburse-workers-for-expenses', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_excel': 'Attached Excel file with one row per reimburse-workers-for-expenses target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for reimburse workers for expenses, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per reimburse workers for expenses target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Bulk-applies reimburse-workers-for-expenses configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for approval, then applies and reports before/a', 'example_request': 'Run the bulk reimburse-workers-for-expenses config update in USMF sandbox from this Excel file — validate first.', 'inputs': [{'description': 'Attached Excel file with one row per reimburse-workers-for-expenses target and the new field values.', 'name': 'configuration_excel'}, {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change reimburse-workers-for-expenses config for many records at once from a spreadsheet, with dry-run validation and approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureReimburseWorkersForExpenses(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureReimburseWorkersForExpenses'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel': {'description': 'Attached Excel file with one row per reimburse-workers-for-expenses target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureReimburseWorkersForExpenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
