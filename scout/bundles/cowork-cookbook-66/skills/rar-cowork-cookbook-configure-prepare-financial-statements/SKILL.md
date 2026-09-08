---
name: "rar-cowork-cookbook-configure-prepare-financial-statements"
description: "Reads an attached configuration Excel file of prepare-financial-statements changes in Dynamics 365 F&SCM, validates every row, returns a validation workbook, then after your approval applies changes and returns a before/"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_prepare_financial_statements", "rar_sha256": "5f24b0111b691d554654229ab6133364dede483102b7416656a61494c312288b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_prepare_financial_statements`. The original RAPP
agent is preserved byte-for-byte in `configure_prepare_financial_statements_agent.py` and in the RCI capsule.

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

Prepare financial statements Configuration Bulk Setup — Reads an attached configuration Excel file of prepare-financial-statements changes in Dynamics 365 F&SCM, validates every row, returns a validation workbook, then after your approval applies changes and returns a before/

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-prepare-financial-statements
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
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per prepare financial statements target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Target environment; run sandbox first before production.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_prepare_financial_statements_agent.py` and embedded as the fenced Python below (sha256 5f24b0111b691d55…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_prepare_financial_statements_agent.py` first:

```bash
python3 configure_prepare_financial_statements_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_prepare_financial_statements_agent.py   # or on stdin
python3 configure_prepare_financial_statements_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Prepare financial statements Configuration Bulk Setup — Reads an attached configuration Excel file of prepare-financial-statements changes in Dynamics 365 F&SCM, validates every row, returns a validation workbook, then after your approval applies changes and returns a before/

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-prepare-financial-statements
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_prepare_financial_statements',
    "version": '3.0.3',
    "display_name": 'Prepare financial statements Configuration Bulk Setup',
    "description": 'Reads an attached configuration Excel file of prepare-financial-statements changes in Dynamics 365 F&SCM, validates every row, returns a validation workbook, then after your approval applies changes and returns a before/',
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
        "upstream_slug": 'configure-prepare-financial-statements',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-prepare-financial-statements',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '892e4f720300cac6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/prepare-financial-statements'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/configure-prepare-financial-statements', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per prepare financial statements target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; run sandbox first before production.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for prepare financial statements, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per prepare financial statements target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached configuration Excel file of prepare-financial-statements changes in Dynamics 365 F&SCM, validates every row, returns a validation workbook, then after your approval applies changes and returns a before/', 'example_request': 'Bulk-apply the attached financial statement config sheet in USMF sandbox — validate rows first and wait for my approval.', 'inputs': [{'description': 'Attached Excel file with one row per prepare financial statements target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target environment; run sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to bulk-apply prepare financial statements configuration changes in D365 F&SCM from a spreadsheet, with row validation and an approval gate.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigurePrepareFinancialStatements(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePrepareFinancialStatements'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per prepare financial statements target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; run sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigurePrepareFinancialStatements().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
