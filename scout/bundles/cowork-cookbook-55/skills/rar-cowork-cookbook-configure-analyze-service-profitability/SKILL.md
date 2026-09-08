---
name: "rar-cowork-cookbook-configure-analyze-service-profitability"
description: "Runs a validated bulk configuration change for analyze service profitability in Dynamics 365 F&SCM from an attached Excel file: returns a validation workbook, pauses for approval, then applies changes and returns a befor"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_service_profitability", "rar_sha256": "1bd581547616ebc1ed31cecf13a6d8e34dad4720db41c1599c17163aa2297915", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_analyze_service_profitability`. The original RAPP
agent is preserved byte-for-byte in `configure_analyze_service_profitability_agent.py` and in the RCI capsule.

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

Analyze service profitability Configuration Bulk Setup — Runs a validated bulk configuration change for analyze service profitability in Dynamics 365 F&SCM from an attached Excel file: returns a validation workbook, pauses for approval, then applies changes and returns a befor

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-service-profitability
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
      "description": "Explicit user approval after reviewing the validation workbook, required before any changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per analyze service profitability target and the new field values.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_analyze_service_profitability_agent.py` and embedded as the fenced Python below (sha256 1bd581547616ebc1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_analyze_service_profitability_agent.py` first:

```bash
python3 configure_analyze_service_profitability_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_analyze_service_profitability_agent.py   # or on stdin
python3 configure_analyze_service_profitability_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze service profitability Configuration Bulk Setup — Runs a validated bulk configuration change for analyze service profitability in Dynamics 365 F&SCM from an attached Excel file: returns a validation workbook, pauses for approval, then applies changes and returns a befor

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-service-profitability
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_analyze_service_profitability',
    "version": '3.0.3',
    "display_name": 'Analyze service profitability Configuration Bulk Setup',
    "description": 'Runs a validated bulk configuration change for analyze service profitability in Dynamics 365 F&SCM from an attached Excel file: returns a validation workbook, pauses for approval, then applies changes and returns a befor',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-analyze-service-profitability',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-analyze-service-profitability',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'afe37d345cef33aa',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/analyze-service-performance/analyze-service-profitability'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/configure-analyze-service-profitability', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the validation workbook, required before any changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per analyze service profitability target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; run sandbox first before production.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for analyze service profitability, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per analyze service profitability target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a validated bulk configuration change for analyze service profitability in Dynamics 365 F&SCM from an attached Excel file: returns a validation workbook, pauses for approval, then applies changes and returns a befor', 'example_request': 'Bulk-update analyze service profitability config in USMF sandbox from my attached Excel — validate first, then ask me before applying.', 'inputs': [{'description': 'Attached Excel file with one row per analyze service profitability target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target environment; run sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit user approval after reviewing the validation workbook, required before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-update analyze service profitability configuration in D365 F&SCM from a spreadsheet, with row validation and an approval gate before writes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureAnalyzeServiceProfitability(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAnalyzeServiceProfitability'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the validation workbook, required before any changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per analyze service profitability target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; run sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureAnalyzeServiceProfitability().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
