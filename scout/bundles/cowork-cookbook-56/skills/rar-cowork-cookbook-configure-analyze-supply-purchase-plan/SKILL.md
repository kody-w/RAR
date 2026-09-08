---
name: "rar-cowork-cookbook-configure-analyze-supply-purchase-plan"
description: "Applies a bulk configuration change to analyze supply purchase plan records in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies chang"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_supply_purchase_plan", "rar_sha256": "a6f2e536cd3a6369fb8433179fee521ca510c5844a54c7648f03ff47d13f95d1", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_analyze_supply_purchase_plan`. The original RAPP
agent is preserved byte-for-byte in `configure_analyze_supply_purchase_plan_agent.py` and in the RCI capsule.

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

Analyze supply purchase plan Configuration Bulk Setup — Applies a bulk configuration change to analyze supply purchase plan records in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies chang

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-supply-purchase-plan
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
      "description": "Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per analyze supply purchase plan target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF; use a sandbox environment first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_analyze_supply_purchase_plan_agent.py` and embedded as the fenced Python below (sha256 a6f2e536cd3a6369…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_analyze_supply_purchase_plan_agent.py` first:

```bash
python3 configure_analyze_supply_purchase_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_analyze_supply_purchase_plan_agent.py   # or on stdin
python3 configure_analyze_supply_purchase_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze supply purchase plan Configuration Bulk Setup — Applies a bulk configuration change to analyze supply purchase plan records in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies chang

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-supply-purchase-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_analyze_supply_purchase_plan',
    "version": '3.0.3',
    "display_name": 'Analyze supply purchase plan Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to analyze supply purchase plan records in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies chang',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-analyze-supply-purchase-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-analyze-supply-purchase-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b9749790fae46716',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/procure-goods-and-services/analyze-supply-purchase-plan'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/configure-analyze-supply-purchase-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per analyze supply purchase plan target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for analyze supply purchase plan, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per analyze supply purchase plan target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk configuration change to analyze supply purchase plan records in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies chang', 'example_request': 'Bulk-update our analyze supply purchase plan config in USMF sandbox from this Excel file — validate first and show me before applying.', 'inputs': [{'description': 'Attached Excel file with one row per analyze supply purchase plan target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.', 'name': 'legal_entity'}, {'description': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-update analyze supply purchase plan configuration in D365 F&SCM from a spreadsheet, with dry-run validation and explicit approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureAnalyzeSupplyPurchasePlan(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAnalyzeSupplyPurchasePlan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per analyze supply purchase plan target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureAnalyzeSupplyPurchasePlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
