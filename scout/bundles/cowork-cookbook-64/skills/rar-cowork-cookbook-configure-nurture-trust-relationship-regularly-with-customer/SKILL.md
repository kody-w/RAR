---
name: "rar-cowork-cookbook-configure-nurture-trust-relationship-regularly-with-customer"
description: "Reads an attached configuration Excel file of customer trust-relationship nurture rows against a D365 F&SCM legal entity, returns a validation workbook of pass/fail rows, and after your approval applies the changes with"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_nurture_trust_relationship_regularly_with_customer", "rar_sha256": "f62948f750a4ca4513c1b0bd0b69ca948841dcca704c19ca5f3ccff4bda59c2c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_nurture_trust_relationship_regularly_with_customer`. The original RAPP
agent is preserved byte-for-byte in `configure_nurture_trust_relationship_regularly_with_customer_agent.py` and in the RCI capsule.

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

Nurture trust relationship regularly with customer Configuration Bulk Setup — Reads an attached configuration Excel file of customer trust-relationship nurture rows against a D365 F&SCM legal entity, returns a validation workbook of pass/fail rows, and after your approval applies the changes with

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-nurture-trust-relationship-regularly-with-customer
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
      "description": "Explicit go-ahead after reviewing the validation workbook, before any writes.",
      "type": "string"
    },
    "config_workbook": {
      "description": "Excel file with one row per target record and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF; use sandbox first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_nurture_trust_relationship_regularly_with_customer_agent.py` and embedded as the fenced Python below (sha256 f62948f750a4ca45…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_nurture_trust_relationship_regularly_with_customer_agent.py` first:

```bash
python3 configure_nurture_trust_relationship_regularly_with_customer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_nurture_trust_relationship_regularly_with_customer_agent.py   # or on stdin
python3 configure_nurture_trust_relationship_regularly_with_customer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Nurture trust relationship regularly with customer Configuration Bulk Setup — Reads an attached configuration Excel file of customer trust-relationship nurture rows against a D365 F&SCM legal entity, returns a validation workbook of pass/fail rows, and after your approval applies the changes with

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-nurture-trust-relationship-regularly-with-customer
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_nurture_trust_relationship_regularly_with_customer',
    "version": '3.0.3',
    "display_name": 'Nurture trust relationship regularly with customer Configuration Bulk Setup',
    "description": 'Reads an attached configuration Excel file of customer trust-relationship nurture rows against a D365 F&SCM legal entity, returns a validation workbook of pass/fail rows, and after your approval applies the changes with',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-nurture-trust-relationship-regularly-with-customer',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-nurture-trust-relationship-regularly-with-customer',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5824c25b4d13723e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/nurture-trust-relationship-regularly-with-customer'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/configure-nurture-trust-relationship-regularly-with-customer', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before any writes.', 'config_workbook': 'Excel file with one row per target record and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF; use sandbox first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for nurture trust relationship regularly with customer, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per nurture trust relationship regularly with customer target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached configuration Excel file of customer trust-relationship nurture rows against a D365 F&SCM legal entity, returns a validation workbook of pass/fail rows, and after your approval applies the changes with', 'example_request': 'Run the customer trust nurture bulk config update on USMF sandbox from this Excel file — validate first.', 'inputs': [{'description': 'Excel file with one row per target record and the new field values.', 'name': 'config_workbook'}, {'description': 'D365 legal entity to run against, e.g. USMF; use sandbox first.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before any writes.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-apply customer trust-relationship nurture configuration changes from an Excel file in D365 F&SCM, with validation and approval first.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureNurtureTrustRelationshipRegularlyWithCustomer(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureNurtureTrustRelationshipRegularlyWithCustomer'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before any writes.', 'type': 'string'}, 'config_workbook': {'description': 'Excel file with one row per target record and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF; use sandbox first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureNurtureTrustRelationshipRegularlyWithCustomer().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
