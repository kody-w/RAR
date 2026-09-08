---
name: "rar-cowork-cookbook-configure-nurture-trust-relationship-regularly-with-customer"
description: "Reads an attached configuration Excel file of customer trust-relationship nurture rows against a D365 F&SCM legal entity, returns a validation workbook of pass/fail rows, and after your approval applies the changes with"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_nurture_trust_relationship_regularly_with_customer", "rar_sha256": "f62948f750a4ca4513c1b0bd0b69ca948841dcca704c19ca5f3ccff4bda59c2c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1: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t1tKYWO3aZd56xvuVQYTXVInk4m6KxRXXSRu8e11uc/PR84wGAJxqDss3M7JjSechGwaCEEG18J52YNie4l4A4nkV491e58cLbdwO9k5u2f1IK0syDioDsEf8s353uPsWj7AwcEOVr6zL2EfzjDavu239xKPzNVlf0zZkqcynOhzcn0TcCntotwW/TQvGMzryGxcOaS1LbhECZDDcgPvXNbJjSSiul2lq6K47XwFz3wwLyk37owRcSsgk3FftmHNenvVu2A0DqbWQAzyJuDGCDWvrY3fz42NMceRwsV+HJoK2ZwOSr+/eXmCq9JQU7ENQVPROybX9VveC8tGCf1NjtMGdvX3OEJJ14AmeP6wagLZqFV626kMteImcyzwu6it1+u3D2/zs9XX0+V/y2tz8xOof9uDsOczq/eXXB7PGAPH//zg9fnfI+5fP7zVXgKEfT4kbLIuej02+7tHhB//lfcdZsrj8w2290fPzwf7rRPNb4q/JYUPltbj16bMHq/GgB1u18zvkDbza8Ye+P7+4eo3YZ4Xm/kdmK9t+fXWle18LSnmd14CP3G+nUavB6of3vwReDzxmq8YSXwN6mo2wusNCqA79gn+hL397f8AN0bv5vAvAAA= -->
