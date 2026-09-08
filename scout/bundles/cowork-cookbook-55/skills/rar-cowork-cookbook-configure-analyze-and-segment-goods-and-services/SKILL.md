---
name: "rar-cowork-cookbook-configure-analyze-and-segment-goods-and-services"
description: "Validates a configuration Excel file of analyze-and-segment goods and services changes against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then applies approved rows with a before/after confirm"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_and_segment_goods_and_services", "rar_sha256": "9b8e1a6312e1a4f049b81eabc80cf04c107a9adc293693199b5614d76ff9a5d2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_analyze_and_segment_goods_and_services`. The original RAPP
agent is preserved byte-for-byte in `configure_analyze_and_segment_goods_and_services_agent.py` and in the RCI capsule.

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

Analyze and segment goods and services Configuration Bulk Setup — Validates a configuration Excel file of analyze-and-segment goods and services changes against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then applies approved rows with a before/after confirm

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-and-segment-goods-and-services
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
    "configuration_file": {
      "description": "Excel file with one row per analyze and segment goods and services target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Target environment; sandbox first before production.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against; defaults to USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_analyze_and_segment_goods_and_services_agent.py` and embedded as the fenced Python below (sha256 9b8e1a6312e1a4f0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_analyze_and_segment_goods_and_services_agent.py` first:

```bash
python3 configure_analyze_and_segment_goods_and_services_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_analyze_and_segment_goods_and_services_agent.py   # or on stdin
python3 configure_analyze_and_segment_goods_and_services_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze and segment goods and services Configuration Bulk Setup — Validates a configuration Excel file of analyze-and-segment goods and services changes against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then applies approved rows with a before/after confirm

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-and-segment-goods-and-services
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_analyze_and_segment_goods_and_services',
    "version": '3.0.3',
    "display_name": 'Analyze and segment goods and services Configuration Bulk Setup',
    "description": 'Validates a configuration Excel file of analyze-and-segment goods and services changes against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then applies approved rows with a before/after confirm',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-analyze-and-segment-goods-and-services',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-analyze-and-segment-goods-and-services',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3fbf265451ad87aa',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/analyze-and-segment-goods-and-services'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/configure-analyze-and-segment-goods-and-services', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'configuration_file': 'Excel file with one row per analyze and segment goods and services target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; sandbox first before production.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for analyze and segment goods and services, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per analyze and segment goods and services target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Validates a configuration Excel file of analyze-and-segment goods and services changes against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then applies approved rows with a before/after confirm', 'example_request': 'Bulk-update analyze and segment goods and services in USMF sandbox from my attached config spreadsheet - validate first.', 'inputs': [{'description': 'Excel file with one row per analyze and segment goods and services target and the new field values.', 'name': 'configuration_file'}, {'description': 'D365 legal entity to run against; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Target environment; sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants to bulk-apply analyze-and-segment goods and services config changes from an Excel file in D365 F&SCM with dry-run validation and approval.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureAnalyzeAndSegmentGoodsAndServices(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAnalyzeAndSegmentGoodsAndServices'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_file': {'description': 'Excel file with one row per analyze and segment goods and services target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureAnalyzeAndSegmentGoodsAndServices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
