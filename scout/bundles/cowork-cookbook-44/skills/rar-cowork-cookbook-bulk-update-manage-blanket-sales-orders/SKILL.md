---
name: "rar-cowork-cookbook-bulk-update-manage-blanket-sales-orders"
description: "Applies a bulk field update to blanket sales order records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval be"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_blanket_sales_orders", "rar_sha256": "a99dd73758c2c1e20a4099c566ff1ab2409a7cf376b2fdf3de07438f9dde125d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_manage_blanket_sales_orders`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_manage_blanket_sales_orders_agent.py` and in the RCI capsule.

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

Manage blanket sales orders Bulk Field Update — Applies a bulk field update to blanket sales order records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval be

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-blanket-sales-orders
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
      "description": "Explicit approval after reviewing the dry-run preview workbook, before changes are committed.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to run against; defaults to USMF sandbox.",
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
      "description": "List of blanket sales order record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_manage_blanket_sales_orders_agent.py` and embedded as the fenced Python below (sha256 a99dd73758c2c1e2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_manage_blanket_sales_orders_agent.py` first:

```bash
python3 bulk_update_manage_blanket_sales_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_manage_blanket_sales_orders_agent.py   # or on stdin
python3 bulk_update_manage_blanket_sales_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage blanket sales orders Bulk Field Update — Applies a bulk field update to blanket sales order records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval be

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-blanket-sales-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_manage_blanket_sales_orders',
    "version": '3.0.3',
    "display_name": 'Manage blanket sales orders Bulk Field Update',
    "description": 'Applies a bulk field update to blanket sales order records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval be',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-manage-blanket-sales-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-manage-blanket-sales-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1ea2ca1b97eb6df2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/manage-blanket-sales-orders'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/bulk-update-manage-blanket-sales-orders', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of blanket sales order record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when manage blanket sales orders records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to manage blanket sales orders records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to blanket sales order records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval be', 'example_request': 'Bulk update these blanket sales orders in USMF sandbox to the new value — show me the dry-run first.', 'inputs': [{'description': 'List of blanket sales order record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across many blanket sales order records at once and want a reviewable before/after preview prior to writing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateManageBlanketSalesOrders(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateManageBlanketSalesOrders'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of blanket sales order record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateManageBlanketSalesOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
