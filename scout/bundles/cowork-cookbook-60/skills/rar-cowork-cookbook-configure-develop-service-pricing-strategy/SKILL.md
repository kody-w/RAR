---
name: "rar-cowork-cookbook-configure-develop-service-pricing-strategy"
description: "Applies a bulk service pricing strategy configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and confirms befor"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_service_pricing_strategy", "rar_sha256": "15e61b24a2c29705bb1a76096863cee51ccc35f9e3573083b1aceaed7c99fe85", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
