---
name: "rar-cowork-cookbook-configure-analyze-supply-purchase-plan"
description: "Applies a bulk configuration change to analyze supply purchase plan records in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies chang"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_supply_purchase_plan", "rar_sha256": "a6f2e536cd3a6369fb8433179fee521ca510c5844a54c7648f03ff47d13f95d1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
