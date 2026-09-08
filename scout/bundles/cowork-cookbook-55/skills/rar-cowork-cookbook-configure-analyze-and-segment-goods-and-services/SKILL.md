---
name: "rar-cowork-cookbook-configure-analyze-and-segment-goods-and-services"
description: "Validates a configuration Excel file of analyze-and-segment goods and services changes against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then applies approved rows with a before/after confirm"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_and_segment_goods_and_services", "rar_sha256": "9b8e1a6312e1a4f049b81eabc80cf04c107a9adc293693199b5614d76ff9a5d2", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
