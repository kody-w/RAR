---
name: "rar-cowork-cookbook-configure-comply-with-customer-data-regulations"
description: "Reads an attached configuration Excel file of customer-data-regulation compliance changes for a Dynamics 365 legal entity, validates every row, returns a validation workbook, and after your approval applies the changes w"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_comply_with_customer_data_regulations", "rar_sha256": "9f6b6a1414432343857da3e6363438c3bcc9cdeeecbfda4473044323f9a83562", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
