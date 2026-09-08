---
name: "rar-cowork-cookbook-configure-analyze-product-quality-data"
description: "Runs a bulk product-quality-data configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies changes and returns a before/a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_product_quality_data", "rar_sha256": "70d767e7f61f0a4a914e63ec2b5869507299c503ce364e18b470a38764e9216c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_analyze_product_quality_data`. The original RAPP
agent is preserved byte-for-byte in `configure_analyze_product_quality_data_agent.py` and in the RCI capsule.

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

Analyze product quality data Configuration Bulk Setup — Runs a bulk product-quality-data configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies changes and returns a before/a

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-product-quality-data
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
      "description": "Explicit user approval after reviewing the validation workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per analyze product quality data target and the new field values.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_analyze_product_quality_data_agent.py` and embedded as the fenced Python below (sha256 70d767e7f61f0a4a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_analyze_product_quality_data_agent.py` first:

```bash
python3 configure_analyze_product_quality_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_analyze_product_quality_data_agent.py   # or on stdin
python3 configure_analyze_product_quality_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze product quality data Configuration Bulk Setup — Runs a bulk product-quality-data configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies changes and returns a before/a

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-product-quality-data
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_analyze_product_quality_data',
    "version": '3.0.3',
    "display_name": 'Analyze product quality data Configuration Bulk Setup',
    "description": 'Runs a bulk product-quality-data configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies changes and returns a before/a',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-analyze-product-quality-data',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-analyze-product-quality-data',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4c4a95e51b9b9113',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/analyze-product-performance/analyze-product-quality-data'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/configure-analyze-product-quality-data', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per analyze product quality data target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; run sandbox first before production.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for analyze product quality data, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per analyze product quality data target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a bulk product-quality-data configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies changes and returns a before/a', 'example_request': "Here's my config spreadsheet - bulk update the product quality data settings in USMF sandbox, validate first.", 'inputs': [{'description': 'Attached Excel file with one row per analyze product quality data target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target environment; run sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when the user wants to bulk-update analyze product quality data configuration in D365 F&SCM from a spreadsheet, with dry-run validation and approval before writes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureAnalyzeProductQualityData(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAnalyzeProductQualityData'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per analyze product quality data target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; run sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureAnalyzeProductQualityData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
