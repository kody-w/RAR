---
name: "rar-cowork-cookbook-configure-analyze-product-quality-data"
description: "Runs a bulk product-quality-data configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies changes and returns a before/a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_product_quality_data", "rar_sha256": "70d767e7f61f0a4a914e63ec2b5869507299c503ce364e18b470a38764e9216c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
