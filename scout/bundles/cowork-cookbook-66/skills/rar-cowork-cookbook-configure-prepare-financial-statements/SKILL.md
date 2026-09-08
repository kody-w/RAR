---
name: "rar-cowork-cookbook-configure-prepare-financial-statements"
description: "Reads an attached configuration Excel file of prepare-financial-statements changes in Dynamics 365 F&SCM, validates every row, returns a validation workbook, then after your approval applies changes and returns a before/"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_prepare_financial_statements", "rar_sha256": "5f24b0111b691d554654229ab6133364dede483102b7416656a61494c312288b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
