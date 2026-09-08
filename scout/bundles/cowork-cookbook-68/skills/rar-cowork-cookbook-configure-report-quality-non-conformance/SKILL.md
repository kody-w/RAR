---
name: "rar-cowork-cookbook-configure-report-quality-non-conformance"
description: "Reads an attached configuration Excel file of report quality non-conformance rows, validates each row, returns a validation workbook, waits for your approval, then applies the changes in Dynamics 365 F&SCM and returns a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_report_quality_non_conformance", "rar_sha256": "a982b9ff9b2739e0d2b015fbb9701eb5f37c74904e89fd215ca4dc819ff487a2", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
