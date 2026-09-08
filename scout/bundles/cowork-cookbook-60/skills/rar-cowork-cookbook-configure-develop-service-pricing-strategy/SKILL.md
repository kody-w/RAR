---
name: "rar-cowork-cookbook-configure-develop-service-pricing-strategy"
description: "Applies a bulk service pricing strategy configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and confirms befor"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_service_pricing_strategy", "rar_sha256": "15e61b24a2c29705bb1a76096863cee51ccc35f9e3573083b1aceaed7c99fe85", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_develop_service_pricing_strategy`. The original RAPP
agent is preserved byte-for-byte in `configure_develop_service_pricing_strategy_agent.py` and in the RCI capsule.

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

Develop service pricing strategy Configuration Bulk Setup — Applies a bulk service pricing strategy configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and confirms befor

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-service-pricing-strategy
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
      "description": "Attached workbook with one row per develop service pricing strategy target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF; use a sandbox first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_develop_service_pricing_strategy_agent.py` and embedded as the fenced Python below (sha256 15e61b24a2c29705…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_develop_service_pricing_strategy_agent.py` first:

```bash
python3 configure_develop_service_pricing_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_develop_service_pricing_strategy_agent.py   # or on stdin
python3 configure_develop_service_pricing_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop service pricing strategy Configuration Bulk Setup — Applies a bulk service pricing strategy configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and confirms befor

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-service-pricing-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_develop_service_pricing_strategy',
    "version": '3.0.3',
    "display_name": 'Develop service pricing strategy Configuration Bulk Setup',
    "description": 'Applies a bulk service pricing strategy configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and confirms befor',
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
        "upstream_slug": 'configure-develop-service-pricing-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-develop-service-pricing-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a5669737373e6bd0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/develop-service-pricing-strategy'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/configure-develop-service-pricing-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_excel_file': 'Attached workbook with one row per develop service pricing strategy target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF; use a sandbox first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for develop service pricing strategy, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per develop service pricing strategy target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk service pricing strategy configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and confirms befor', 'example_request': 'Bulk-apply the service pricing strategy config in this Excel to USMF sandbox — validate first and ask before writing.', 'inputs': [{'description': 'Attached workbook with one row per develop service pricing strategy target and the new field values.', 'name': 'configuration Excel file'}, {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox first.', 'name': 'legal entity'}, {'description': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you have an Excel file of service pricing strategy config rows to bulk-apply in D365 F&SCM and want row validation plus an approval step before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureDevelopServicePricingStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDevelopServicePricingStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached workbook with one row per develop service pricing strategy target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureDevelopServicePricingStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
