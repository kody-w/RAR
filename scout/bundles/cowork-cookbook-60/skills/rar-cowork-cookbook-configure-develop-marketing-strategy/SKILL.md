---
name: "rar-cowork-cookbook-configure-develop-marketing-strategy"
description: "Validates an attached configuration Excel file of marketing-strategy target rows against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then after your approval applies the changes and returns a b"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_marketing_strategy", "rar_sha256": "f599d96e0960f22d26c03da283670ecb7a37a5d1a2e13523a0ceeb1c7f64e72e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_develop_marketing_strategy`. The original RAPP
agent is preserved byte-for-byte in `configure_develop_marketing_strategy_agent.py` and in the RCI capsule.

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

Develop marketing strategy Configuration Bulk Setup — Validates an attached configuration Excel file of marketing-strategy target rows against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then after your approval applies the changes and returns a b

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-marketing-strategy
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
      "description": "Explicit go-ahead after reviewing the validation workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per develop-marketing-strategy target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Target environment \u2014 run sandbox first before production.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against; USMF sandbox by default.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_develop_marketing_strategy_agent.py` and embedded as the fenced Python below (sha256 f599d96e0960f22d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_develop_marketing_strategy_agent.py` first:

```bash
python3 configure_develop_marketing_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_develop_marketing_strategy_agent.py   # or on stdin
python3 configure_develop_marketing_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop marketing strategy Configuration Bulk Setup — Validates an attached configuration Excel file of marketing-strategy target rows against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then after your approval applies the changes and returns a b

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-marketing-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_develop_marketing_strategy',
    "version": '3.0.3',
    "display_name": 'Develop marketing strategy Configuration Bulk Setup',
    "description": 'Validates an attached configuration Excel file of marketing-strategy target rows against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then after your approval applies the changes and returns a b',
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
        "upstream_slug": 'configure-develop-marketing-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-develop-marketing-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '936172b37740ab8e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/develop-marketing-strategy'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/configure-develop-marketing-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per develop-marketing-strategy target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment — run sandbox first before production.', 'legal_entity': 'D365 legal entity to run against; USMF sandbox by default.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for develop marketing strategy, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per develop marketing strategy target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Validates an attached configuration Excel file of marketing-strategy target rows against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then after your approval applies the changes and returns a b', 'example_request': 'Run the bulk marketing strategy config update in USMF sandbox from this Excel file — validate first and show me the results.', 'inputs': [{'description': 'Attached Excel file with one row per develop-marketing-strategy target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against; USMF sandbox by default.', 'name': 'legal_entity'}, {'description': 'Target environment — run sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to bulk-apply configuration field changes to marketing strategy records in D365 F&SCM from a spreadsheet, with dry-run validation and explicit approval first.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureDevelopMarketingStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDevelopMarketingStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per develop-marketing-strategy target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment — run sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; USMF sandbox by default.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureDevelopMarketingStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
