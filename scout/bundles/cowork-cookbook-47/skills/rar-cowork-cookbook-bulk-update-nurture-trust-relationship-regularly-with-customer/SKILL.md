---
name: "rar-cowork-cookbook-bulk-update-nurture-trust-relationship-regularly-with-customer"
description: "Applies a bulk field update to customer nurture-trust records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied list of record IDs, producing a dry-run preview workbook for approval before committing cha"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_nurture_trust_relationship_regularly_with_customer", "rar_sha256": "4830f429eac5a9453543d94ebd9b454fe7da67f8c620026d3055d44dacf30530", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_nurture_trust_relationship_regularly_with_customer`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_nurture_trust_relationship_regularly_with_customer_agent.py` and in the RCI capsule.

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

Nurture trust relationship regularly with customer Bulk Field Update — Applies a bulk field update to customer nurture-trust records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied list of record IDs, producing a dry-run preview workbook for approval before committing cha

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-nurture-trust-relationship-regularly-with-customer
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
      "description": "Explicit approval after reviewing the dry-run preview workbook.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (e.g. USMF); sandbox only.",
      "type": "string"
    },
    "new_values": {
      "description": "The field(s) and new value(s) to apply to each record.",
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
    },
    "record_ids": {
      "description": "List of record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_nurture_trust_relationship_regularly_with_customer_agent.py` and embedded as the fenced Python below (sha256 4830f429eac5a945…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_nurture_trust_relationship_regularly_with_customer_agent.py` first:

```bash
python3 bulk_update_nurture_trust_relationship_regularly_with_customer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_nurture_trust_relationship_regularly_with_customer_agent.py   # or on stdin
python3 bulk_update_nurture_trust_relationship_regularly_with_customer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Nurture trust relationship regularly with customer Bulk Field Update — Applies a bulk field update to customer nurture-trust records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied list of record IDs, producing a dry-run preview workbook for approval before committing cha

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-nurture-trust-relationship-regularly-with-customer
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_nurture_trust_relationship_regularly_with_customer',
    "version": '3.0.3',
    "display_name": 'Nurture trust relationship regularly with customer Bulk Field Update',
    "description": 'Applies a bulk field update to customer nurture-trust records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied list of record IDs, producing a dry-run preview workbook for approval before committing cha',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-nurture-trust-relationship-regularly-with-customer',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-nurture-trust-relationship-regularly-with-customer',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '467b1d6a5fe72a26',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/nurture-trust-relationship-regularly-with-customer'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/bulk-update-nurture-trust-relationship-regularly-with-customer', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); sandbox only.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when nurture trust relationship regularly with customer records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to nurture trust relationship regularly with customer records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to customer nurture-trust records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied list of record IDs, producing a dry-run preview workbook for approval before committing cha', 'example_request': 'Bulk update these customer records in USMF sandbox with the new value — show me a dry-run preview first.', 'inputs': [{'description': 'List of record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against (e.g. USMF); sandbox only.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across many D365 customer nurture-trust records at once and want a reviewable dry-run before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateNurtureTrustRelationshipRegularlyWithCustomer(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateNurtureTrustRelationshipRegularlyWithCustomer'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); sandbox only.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateNurtureTrustRelationshipRegularlyWithCustomer().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
