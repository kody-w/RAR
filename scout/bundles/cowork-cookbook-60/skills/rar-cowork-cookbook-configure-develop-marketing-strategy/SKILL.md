---
name: "rar-cowork-cookbook-configure-develop-marketing-strategy"
description: "Validates an attached configuration Excel file of marketing-strategy target rows against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then after your approval applies the changes and returns a b"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_marketing_strategy", "rar_sha256": "f599d96e0960f22d26c03da283670ecb7a37a5d1a2e13523a0ceeb1c7f64e72e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
