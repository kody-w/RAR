---
name: "rar-cowork-cookbook-configure-report-quality-non-conformance"
description: "Reads an attached configuration Excel file of report quality non-conformance rows, validates each row, returns a validation workbook, waits for your approval, then applies the changes in Dynamics 365 F&SCM and returns a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_report_quality_non_conformance", "rar_sha256": "a982b9ff9b2739e0d2b015fbb9701eb5f37c74904e89fd215ca4dc819ff487a2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_report_quality_non_conformance`. The original RAPP
agent is preserved byte-for-byte in `configure_report_quality_non_conformance_agent.py` and in the RCI capsule.

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

Report quality non-conformance Configuration Bulk Setup — Reads an attached configuration Excel file of report quality non-conformance rows, validates each row, returns a validation workbook, waits for your approval, then applies the changes in Dynamics 365 F&SCM and returns a

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-report-quality-non-conformance
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
    "configuration_excel": {
      "description": "Attached Excel file with one row per report quality non-conformance target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (e.g. USMF); use a sandbox first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_report_quality_non_conformance_agent.py` and embedded as the fenced Python below (sha256 a982b9ff9b2739e0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_report_quality_non_conformance_agent.py` first:

```bash
python3 configure_report_quality_non_conformance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_report_quality_non_conformance_agent.py   # or on stdin
python3 configure_report_quality_non_conformance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report quality non-conformance Configuration Bulk Setup — Reads an attached configuration Excel file of report quality non-conformance rows, validates each row, returns a validation workbook, waits for your approval, then applies the changes in Dynamics 365 F&SCM and returns a

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-report-quality-non-conformance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_report_quality_non_conformance',
    "version": '3.0.3',
    "display_name": 'Report quality non-conformance Configuration Bulk Setup',
    "description": 'Reads an attached configuration Excel file of report quality non-conformance rows, validates each row, returns a validation workbook, waits for your approval, then applies the changes in Dynamics 365 F&SCM and returns a',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-report-quality-non-conformance',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-report-quality-non-conformance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ab0cb8093b10cfc9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/report-quality-non-conformance'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/configure-report-quality-non-conformance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'configuration_excel': 'Attached Excel file with one row per report quality non-conformance target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); use a sandbox first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for report quality non-conformance, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per report quality non-conformance target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached configuration Excel file of report quality non-conformance rows, validates each row, returns a validation workbook, waits for your approval, then applies the changes in Dynamics 365 F&SCM and returns a', 'example_request': 'Bulk-update report quality non-conformance config in USMF sandbox from this Excel file — validate first and show me the dry run.', 'inputs': [{'description': 'Attached Excel file with one row per report quality non-conformance target and the new field values.', 'name': 'configuration_excel'}, {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox first.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when bulk-updating report quality non-conformance configuration in Dynamics 365 F&SCM from a spreadsheet, with dry-run validation and approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureReportQualityNonConformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureReportQualityNonConformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_excel': {'description': 'Attached Excel file with one row per report quality non-conformance target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureReportQualityNonConformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
