---
name: "rar-cowork-cookbook-bulk-update-nurture-trust-relationship-regularly-with-customer"
description: "Applies a bulk field update to customer nurture-trust records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied list of record IDs, producing a dry-run preview workbook for approval before committing cha"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_nurture_trust_relationship_regularly_with_customer", "rar_sha256": "4830f429eac5a9453543d94ebd9b454fe7da67f8c620026d3055d44dacf30530", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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
