---
name: "rar-cowork-cookbook-configure-comply-with-customer-data-regulations"
description: "Reads an attached configuration Excel file of customer-data-regulation compliance changes for a Dynamics 365 legal entity, validates every row, returns a validation workbook, and after your approval applies the changes w"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_comply_with_customer_data_regulations", "rar_sha256": "9f6b6a1414432343857da3e6363438c3bcc9cdeeecbfda4473044323f9a83562", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_comply_with_customer_data_regulations`. The original RAPP
agent is preserved byte-for-byte in `configure_comply_with_customer_data_regulations_agent.py` and in the RCI capsule.

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

Comply with customer data regulations Configuration Bulk Setup — Reads an attached configuration Excel file of customer-data-regulation compliance changes for a Dynamics 365 legal entity, validates every row, returns a validation workbook, and after your approval applies the changes w

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-comply-with-customer-data-regulations
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
      "description": "Explicit go-ahead after reviewing the validation workbook, before changes are applied.",
      "type": "string"
    },
    "configuration_workbook": {
      "description": "Excel file with one row per compliance target and the new field values.",
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
      "description": "Dynamics 365 legal entity to run against, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_comply_with_customer_data_regulations_agent.py` and embedded as the fenced Python below (sha256 9f6b6a1414432343…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_comply_with_customer_data_regulations_agent.py` first:

```bash
python3 configure_comply_with_customer_data_regulations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_comply_with_customer_data_regulations_agent.py   # or on stdin
python3 configure_comply_with_customer_data_regulations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Comply with customer data regulations Configuration Bulk Setup — Reads an attached configuration Excel file of customer-data-regulation compliance changes for a Dynamics 365 legal entity, validates every row, returns a validation workbook, and after your approval applies the changes w

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-comply-with-customer-data-regulations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_comply_with_customer_data_regulations',
    "version": '3.0.3',
    "display_name": 'Comply with customer data regulations Configuration Bulk Setup',
    "description": 'Reads an attached configuration Excel file of customer-data-regulation compliance changes for a Dynamics 365 legal entity, validates every row, returns a validation workbook, and after your approval applies the changes w',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-comply-with-customer-data-regulations',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-comply-with-customer-data-regulations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a90b5bb378aecb6e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/comply-with-customer-data-regulations'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/configure-comply-with-customer-data-regulations', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'configuration_workbook': 'Excel file with one row per compliance target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; sandbox first before production.', 'legal_entity': 'Dynamics 365 legal entity to run against, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for comply with customer data regulations, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per comply with customer data regulations target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached configuration Excel file of customer-data-regulation compliance changes for a Dynamics 365 legal entity, validates every row, returns a validation workbook, and after your approval applies the changes w', 'example_request': 'Run the compliance config bulk setup on USMF sandbox using my attached spreadsheet — validate first, then wait for my approval.', 'inputs': [{'description': 'Excel file with one row per compliance target and the new field values.', 'name': 'configuration_workbook'}, {'description': 'Dynamics 365 legal entity to run against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target environment; sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-apply customer data regulation configuration changes in Dynamics 365 F&SCM from a spreadsheet, with validation and approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureComplyWithCustomerDataRegulations(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureComplyWithCustomerDataRegulations'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_workbook': {'description': 'Excel file with one row per compliance target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureComplyWithCustomerDataRegulations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
