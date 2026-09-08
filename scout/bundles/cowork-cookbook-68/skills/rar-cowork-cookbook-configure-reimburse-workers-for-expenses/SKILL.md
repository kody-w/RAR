---
name: "rar-cowork-cookbook-configure-reimburse-workers-for-expenses"
description: "Bulk-applies reimburse-workers-for-expenses configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for approval, then applies and reports before/a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_reimburse_workers_for_expenses", "rar_sha256": "ea65849707869ec739db51bff3b65d49a2a585380bc3320cd4412de0678c40ec", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
