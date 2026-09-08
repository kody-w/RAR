---
name: "rar-cowork-cookbook-configure-analyze-service-profitability"
description: "Runs a validated bulk configuration change for analyze service profitability in Dynamics 365 F&SCM from an attached Excel file: returns a validation workbook, pauses for approval, then applies changes and returns a befor"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_service_profitability", "rar_sha256": "1bd581547616ebc1ed31cecf13a6d8e34dad4720db41c1599c17163aa2297915", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
