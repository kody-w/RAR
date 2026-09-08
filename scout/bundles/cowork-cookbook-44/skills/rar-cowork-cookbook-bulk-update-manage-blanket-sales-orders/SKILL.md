---
name: "rar-cowork-cookbook-bulk-update-manage-blanket-sales-orders"
description: "Applies a bulk field update to blanket sales order records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval be"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_blanket_sales_orders", "rar_sha256": "a99dd73758c2c1e20a4099c566ff1ab2409a7cf376b2fdf3de07438f9dde125d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adObSLbmX9G8N2LKdbEtFiHAHR0xQoAQi0AsQqhc4WLfF7EIUN3675NIsquq23Wne2I+jRwOiSTzbHnO85x84dc3p+/iqnn79KYHTrnYOXmexEGzcEp/sa2GqsnAV5W54P/Cq8quSdy+q5r27f2bH7Rek9RdUpVg+aau8yRoF87C7fNsESZB7i/62ne6YNFVCzd3yizoFq2Tg0lV4wMdTeCBH+0iKRfMVDpF4rULbI0vuP+pb+XFuzyInHwRlF3STQtTl7n3YHXpu9X44yJsqgKo8oC5QfOh7R/K/UWetN2iCl+SF3umfThSBsPi5uR90L5f1E3l915SRmC530wfmr4EY8EtAXNmdx+ehhWIQA2mglULNwDOBqNT1MD0t08//fz+LQG/3z79+ublTguG3mjgsvnwVXZKJwrop7f67Kwy+zrHC4xFYG49gYCX4LoOGqCnAEN+EC5eV+/aIA/fL/7zP7PBaaL2x0+fy8Xr8/lt/qcBe7t4jqnTdsBlz6kdN8lBjD4uNvngTC3wvuubct6KFuxXGX18rvxdUlUv/j7fe/dU8jEKunef3ypggjPv5ue3H8EOAX0gNuD3x1lK/e7Hj3k1BM27H3+X0/ZuGnjdLAxY/fHL6/olFkz8fWoSLr7oKrt96QIblNQBEP4H/+bP0/SXuFdIvjwnv6vq94vvS579+Tuw95mRLpD7fbEgBmDl28e0Ssp3Lx1gj4PSKb3g3Y9/JdaLAy+bU+tfkvvTU3AcOGDf371C8uP7x/b9vIBevn2T+ddqa5Aw/44nYPpXdd8C9VeyHzv7D6LzpASl+XUvvyvuewugvy9++kvf/rsF7xfh5zcmyJMbyDs3Dz4tfn2kyE8/+L8P/vDzb0D0/1GMXvWN95DwpXDKJAza7suXn35oH8M//PzTD30Nsjhwii99k39P5vfi+tDzpwi+Zr3781qg3yyzshrKxbcaWvxa1f+j+e3j4uTkif/7ePtp8cdKnD/QYnbiq9JnCP5QjS2w9Q9x/PHtN4A/JfCm9x63AX78x38s5MRrqrYKu4XuVX23ABvcJUUwG2/ECcDY9oEaAOgAGCUgsK95IP/nHZ4tBrj5y//yHpj/wXth/nIG8y9PGJ8jC7DtywvKvzyg/MsDyttfPi4MIL5qkigpAWZqG1X9PM8uu1k1ANg2aG4ArtypCz6Aqv4w/5iR/5d/UcOXh7CP9fTLA9KTJwpq2/2MgG2fBx9nX604KF+eeYDOgjHweqAnrwBTAE7KZwYAtlT5DSDoHJc2S/J84ScAYwCtTQ/ZIHafZmG//PKL67Tx5/IJ2djiyXftEkz4Zs7iwwfgXZgnUdx9LgMvrhY//PrbD4v/Wvx3qx7CZx0qIJDXzgALBV05LECl9QWYNhMjgHjHf+zMr7+9YgzElIA8wT4m4Uy482KQqVngfw24zm8+oPgaEBcINAhyUVdNNzNe0n1c7MPFN3uB0vnWzBRxBZjTD+qg9IPSm4BUB7jzLZJlNVN3l7Th9H7Rt8FD6y9u4zxMLEDJO90vC3mrAl6q8pnwmxdPgcVVmYDwf0uH5zgQ0vzQLuivIj4uDnNuLmqnceq4cV46Que5LzMhv5YD4c5M6Z/LmYaDOVSPQnmGB0wCkfFeW/ph3nPQuBQgs56dRvd1jjOzp/Fg0eZz2b6KwGmCR/cATJkWUZ/4MzX87ZVSbVz1oKuZ4wcsnSW9dsF/7cojB58twPc6HuDu3Btxj97o2S8sPvcojKwW/z+3T3NQNrudxu42Bsss2IOh2c/NmjvKeVOfTehs6Lz0UZi/9zVfsesrhH8u8wRkXjP97TnzscWvOU9Y7BvgjLbRHvJBfoFgzXIf6T+nc9M8Qv25/MoV74E3D2AEGQCwAtTSHPSvCue7Xy2NASDM17/3DV+jBSIFUnxR924O0i8MAt91vAxY1cwl/NpmUAvBHOEhTrz4T17NOwVSDshfACMSUJSATz5+w+/n3a+m/2nhsz2alzxax76ck2MWAOwIZgPnPRySDgCZ0z0beODnp4cQ4EZRd7PvLqgh4OlzMGiCa5+0STdv+TOuQQ0g+8P8/fR0Hg3GGpQNCBYojroH0X2U05wcBWh+gA0AUUB1FUkJEgsE5RWEh0CnCB7597VbfUp8DL8cCh41OLPY14WzI/OauTF45XA5/RFCjO+lCZBXzDMeev8x075pm2XPMNoCKAQav959dhAfn03As8tYfJX76Z9OSO/+vUPUg9bNPyfAp0XcdXX7abl8UvFXJv4IQGz5tLV9sPKHJzp8eHLmhxdCfHggxIcn3PxJ/NPzT4t/z8Q/iXiVyKcF8hH+CM+3pFeKvT4gItsPtP1hNd/9XGrB70gL1FcFyLF5/ybQBnyjxa9TADdGDcAsMPlJk+3MrgMg9AcvgM34XP4x5+eaA7RTRnOOttUfsODRH4D8f+7dN/oCt8oO6Pbn3jIKPs5Hstn8Nnj7VPZ5/v4NgGjwr57mZp4q5uxu54MgqCPQr3VJ8Lj6in3z7z+fktkRIK0HCuMbPDph98DyGUHnypmT7q+A9f1XSn/5/WCrmdySDkRtdqib6tmD57lv7hQfuDV2/2yJ8vjh5B8XTAAwMm//WAwvopuJ/g81+ww6CLYHnH2/mAM0c9Ec9DkOc707LSggYOJ3bXkw0pcnI/2zQX/isD+R16ubcKJHnf8NgEro9DnYYHBjJravvPZdpYC8vjzJ659VznDxYNp37Y9/Zrp5YO4zADE+9AcOgOun/9/V8q1b/2clFmiNZhF+9Wl24/0Lc8E3SKv3i2+HJRDQ1/F11hCUffH26af5oDYn22PJ/AOsAV/fFn37M4wbvP38HbueJn9J/O94L73Y/q97i0cH8CDCea+/4/hDA2AKwLezsb9H4XdbqscJcrYF2N49/+Dx6xuoHAfIdF618zqCgOkAWD+0c7O1BBgDFILrJxqAe/+3h5OXmDZ2QFcM5DgU5fsERuCkh3pIgMLOCqYoD1+vwxBxXBRcOYQXYsTaRUM/xPwAJlYYGYJVAYLiPpD3hJYvz9oDIme7QEQ+AHQKfr8NhvyXT08f5oB9Ows9kOLp2q9v7noFZvKrdr95frZLCAGDhDsJZ6hZB5Us06KXaFcpyyxxTZ5tInS1SE23REXtjsN6k8OJjggHc9J5jgg4LTrgCTPGZaEvvfVV3CfFtYdQuYWLIY444XKwahMKp9LsTgG+woKtafSnS7LzbpleW0kmsVdNqHkxWbLtdIXYBIKTRB2PoyuYgIuWgXVbFYU1alem5lIdGq1lQ94JuUdTgd+fVlkb+1sxIEYRRyw2vt2wlCd1aUlEq0A/7dpTI1likiHKSVnyzLhuTbbFD1VxXnkJYgVuw5micrBxX0lWrZmyQZ9wSima8aW8k5zKVjl7tltVvuKmrHGXMrucroKM1FmIu3V93l7WNTPWadOppFMXxYohDrE3DJyksmYE7wwEglSGoqDQ8NfnwwjdGh8yISiQfG2fTQZ7GwTrYrmHrYc6lojDR3M1QZo+Lo/yDa7kphGTu3D2mEKk7jsLCtBh15R6i9Eb+SqL09TsDHIdlgZHXGlhn7RNA4+nTBjKUvFivL04wvmaRCUqZ7zIgkbUTg1yc73vz1uMlxAk3OFZ6/Bhx+xO01YzjVw8whGjXlGrPRKcLuaNSG4qMjIldp1huiZwWXP31phkoMexEX1Yc6MN5696eU0eA8YnjgRJEiMmXHf52SqcvSiexoMmWEf9QMOtuBMPBz7oJhLZ5IXV54glMN76Qt/S8JKcuiDJpVRHnXiqzzdEX8Pbc416sXHx1dzNruGNPa2vDF6IyRDX0vHaDvU2vIRilegMKl/3EL3TxNyCkGMhb30xwgx57E+n1lM2npJdxWOImW5m0dUF3hxJO0140pHw8NgyvH3ZBgF+2tS7Q+WwUO3QVtw5x80Nda0mSMyED27ZNd66nNjjHXxycGe3JfbWaiUut+YFlTJcb3cjVMshr8UXUQg2JURtnK2wavy9dUQlNYIl0okg8+CuMGUUvb4tZKrYm6RMGMPSkLz7gEbj/r61d3Fiu3Fu1rEt1tHAmYN8NYK6QDB1dI4DKp7iW7Hvb0tnSTZLpgjQTqdiKPMMgaI6FaawCFc4v6E1yLjQgq102LZm404heC/RJdk/2ZZ897JM6RAmBwr5ieM31RIl2ZqkQfnH+51xlEtkqDA5LwxNu9QDdKgV1Gi1whqySRMiG1/lFw3I3kfdyr6qNjPuN4nXDAEdbIWebo5CM0RYS59uUjN4FnPK/cK1W8MbidWu2hYQj40lYggIZG0DGjbzyAe2lke9zUimuuzS2tpl+tUi4zu69Ek4Olv6iEWnW5mhws4wjxfWb7lljabJoZ9aa+kQjn/phQ4AjkWjF58pzePJ3cFnblfKawY0RcpuEuPNlCTSpk9YaH0paX2poKcUoy6bbHfRrmyyucPHrceGeqP7EUOdW3WQQn6/TZNNtFFOF1LhcL1kId5yCDQ+p0aG3AnKzAohNncNpww+64ota1DDJu5XXncNdIbQcc2Cw8IUMp0VbNrAsFtySMsJyStTTaPLyofy29hFeHMr45uNrI6OEYeQti7o7VJux7vHH+1kUtgxuHMkHEtuFDt8Zjry/eYfI80qzHscBZuzbrbBDm8kveUCdtDT85USsRCQBdM7B2ys3OuOZe/UMs8vTYvh5RjZa7nirpByHzycmm72vaL265asKw6r+Ms9qw+qKRunorcpVq5BiKcltfV26QE/7bKUmw6kN3I5Z+tGPkjLUvX5YyTAwU3fdHvWMvbgMH9gaZex+Q0+2X0PH6WuFKZ9TVCCtN3vaNMttBub4xyLZYKQWlF2sBRDvB61HVUAIwNID6kWuR4zOVmlZcHFwFDhQKExJ4eb0zZYXl0li9BTp22FSDsKLGwvPf3IiNsaHHcOSQ+NiVWaOtu7xy3LdTGF9+Yq92qfMBtIWw1Dle3EmERPErFbd5Z+OsEbqrMtyrJL6aTYUnCAFUeWHdWlUK+s16vOiGrEu+gluj3fcVWs2Qo/hvBk+HzOVLJ5tst6wsmQUIHnt65gedfSYhtRpwKhoVs43ZaIIamw07jr0UfNPEh9mSRRVeAiLYrQQdh4zGE7ZufkRp8axF43Oyla3YZjulOqq+uqG+5+GK0+w8/JvTEBGxylJNxFB47YqCNlwtfW7cQzTehN3EWRxMUTrVaeF4+aija74mKkmSPRdSoqR4+p88sSva/xYOhLBB2ktog2gMjiAol2Ac7nUi+fxVa77arlHdXx6uR3bryWeZE2j1zK5Taeop17kPcaBPfocTUQ+7q3dB+7reWTPrL20cCD88Hc2x6TFS3LB5uB3nNCQw7qgewgvxeULR17d7bYVNAyJffbw97dMdleaYcd2YqDyNeYdApKmXJ9z05oQcR3orvvofaKmjqjaKO+x6dVN+1aaZcK6tK87uzKF/Koa1TaO+X5SdnW2/KiH1vkALHack1ibayPYoxMDWNe1E10Qsi4Vfn1gefAGeUUW7qbjNSOiUVdsOpCzm6jn3NBbt65AfCZfN4bG7nYiaKRt9kZXeqFzAphlXHS9ryT2oaj4PPdbAtdhvPtGXFQzFDzi86vpPVFObDHHjvEq7PXS9l6PBeVU1xx0dBB52ZfeL2kbrS92SYejjdsVhvcXdM5cYdZl+t5FWdUkNUqHV2L+MQM2yLPGm5d4nZrbvjewaeYLARBG3lie5OdUBcRlhU3a81gB7kx7/VxY7TmidyXskOQoa6OTQIPscnctBE6CIdxw2DcpZ3G/pAMxDqUNZ4IouwEl/7ZcXX33FL2sGcvZd11ECTW7YGNNml+Fvyly16jFOmjwewrNt+LUrf2yhxfXYgEDo5koZCgLaj48dqsuEjp9Z7eY04t7Loc3emJPAEY5q4uuw3VolZGfQTVSCZ6pgxakUHGeUcx9wsekrRnMhmaM9l0tP3zIZcYzciog5TiXbzrcAxBkmgQHBaV8U4M19EluyLGCmfoVdV5hd1gmeKzK/VMNsxOiNaQDrM2srQBg3ESKG0hPReE2mVE3UT8RFcb3eJO6kUPD/yopU5Ehq1vIoK34THDT5fYnVIHtJbiAk8Jb8p2hIpR6uVQ1URZKeY9kPf5Ca+nQNirbCqLvtrncT7sl4GM79eMmoudobPlPjw0J7beRFftJJx0/nzkprGq72m/pe+9YY4jd1p3wtJI11F2RLB+ukOR3AXX03anA9xF09hSWHhz1kTaW4MWJ+J4rmb7q7q/7GpBE2CuvvV8YrU6FBSDjqB6vM0AidMntOorKp9iOAunHaqOrBk4iSkkhXUSKwMhT6ej2US1m2y6aKcgRXtx1/2arl3D73VHQSZ162SZVxfbc87kxLG+CVV3VVLmdKDZ/KpwCQ/VHUfd4I0qx5MQn71DNlA947obLjR1eCwDqluf16TpMbkKnHECD7T7atleR05q1wfVNUQPuWDn03B3CCOCB7LOC5eOcwbnXNOFjj1swafGiRLFYSBcuq738gXZ+EdrFTO3dry6BXYgNIXn/dTUAMiummEL+e0hAxBMG3kehKp93pGeaU1k1oQSV8QuS7T2LkA9H8X2Q2a6jQhqXiGxZVVsVyw7dBhd0CgC2/HIN4TBJxSNbM4BGm+G0GdWLkCkU52Wpcl4/nZzzLhquWGmo0cgxZJnrVug1Z3H3GX5fBlyWvVyOS8P46E6Bls+2/QTTdQix2FMSN1FT9FzTVsvkZU59PshoouigzNN17edsVOafXmQFOYQs/khce2MU/bXfpdiY7FBVTWV1RyMKOOJiZS6O8C6sikUgdA05cYNqVomIzhHNCQV3AhNuB5PG5rfX/OhobceATqtbXTY8VuNCacNCtunmLkDE2k1DqYzJ96PLiasxLOlslN9j+7e9UyIp05FlNz1mLXUEd3+qpHCydz32yYcOtysOmotwaSL4SsLSqnJXubXKWNB+28F/m5vaB2BFiiSelRcU9pdi1cxKGLFupuBalTFaadmhoJJuOL3MhErrWQKtOxWy2oznpdwIqFRvb24iSb1m7vQeh0Xn21qsPB7h6VoiTDUpomvOd2Xaq7rJC6JqXPZLje4bSpFaO7VW+gjNU5YUqhNpCCvTx2nqDzSXR1ghk9D6wqWmXN2lc9kX13NToavq6bmVy7irMS80ktpjREweYAgHkaPEuFfmo2wNXeWOV6RdQdbbDqp+wiCEfteC9XKLMsdebS2TO3GmRHh+K1o+wH19iaioXiIVV6NH7eIjR0GDhGHwwmNl26Jj3UfmW4PN+Gmwc0Y9U/O9pSGQQ5aCUz3kG3ZSx67qbgzdzNwDhxDwKmIGdYhLPCXeqojeX8QMnAKaVOtRPd97oFu3Dap8oIpcXrtiCMk4BeY2VHYfRP0l1y+74cCu8AaORW0HqfDfkxotvLDfYnCh2HHpbcrSUv8MJAqstSYSGft+goZB32ctpaOtnqdEnXJ3VxF4jNlTycJVpVdx9Iww/IR0E1eSg0arHp5hJl7kYZbgj0w7fJ+74oLuYv1w9S0R/dmlwQNW/kK4tcl6ud7p7wcCgTVVioWMoO7U6YMbTBor1ys25Qt3eZe51cSYrD2hkzwBbsoWQrKZiLXJJFua7tXab1j181adU1kvR/wyxEhMlLW8o1yvTFH3hfhNURD6klcCTZRocQBI8xbsSl1yldu/gCvi+KGGO2aK/DTmVkm2W68rIt1A/pvuFqawUbxRQEz4sQl2AlZIaZh3sAB3RNgy8SHAgkv9/5+pCTJdeiGUqCO83HX5U/QMPqkxoNzqN1nxKXgC4LGbXGA/fS2Otl0pjoVIweoQKywJbHmlsN5N57Ki4AVOLFkl4MNoRSdKBRyRqbIS0AZmastbqadqMFBwNu35B6oXtasbb1SlvUlU24mjmGKfjWg9Ip50ZECZw4atOZkcVd3yz67owPsZpgh3g/38Eon3r2UbzQC8429vQ8Ox9LalSpM3L0zfHU52jJK2pfmvjRyYbSJJiwvCdHTVn++RWFD3PqpVAxFrXq34CdVQVHQBXBToejjtfUmTzY8t6wyguimS7+7SoHtkyduwFck61oKk5z4NdRnZk5ZKmq7ak/Lgs/us4its8hTb8vz7uyD3DnCI+tPcOfbaSOkTrw9NlQ7OgjiSgmsxEXJKfTFDSqJ9WVCpHhCFQliK2vDBbILV70dreva608CeTz4rSaa12NyRPejwkiUpGGollv9UaRL5qAaHbFeVYZhw925wCPOoGH6TqTFVLfMRb7Sh/CA2TLvbjkKlYU93uHjZhWMopqHgWVmvrRui/C6hiCot11sGR64iVAP5wA/HCBH5m+puXVIvhAQY6nY0TLz+fjimygPFQORb/I91rtGKhFoub/AWzI7eR6SmvABza194sJyhQOPAatlHZehaSOSEK/rU3BM704fMFTm6quO9mgUvWCSUTCXVhC3vLJmD2UkoZsIC9O02a635biKuuulVwWFyoMGCsf+XHRtOKx4vLkr3YGHduI1gJnk4jQKyZEYRElDp9lOPObZOFBcPlFMk9+Rgoi2ez1O1gqD3Ag6so4qUS3x+/XCHY2dTfLUPRUrJ1WyLKY61tKsgN1REWNgOekPpK3WjXmDWqJxPKw586HiIf5K8zzorqrM9YQpqtssa6HEV/0GUjWyNA+BeB+lFXeFcQTDZP1cu8TynMs8v6StjvAR5Bhm8JkM8ghWlvqKvIZ4J1HOtDuTzG3LKXUR5ZfYxSrMLVTM6szY7oza6hX7fFBq1yMFyNFGykXuVohUfH/usfO4znjvAjooXUrUZnsSqfawPvS71TGVa9KBXT9GbXOJjTg4zw9Xs1cmwyu5XRme04hdhXddRo771YrKtjGCLHNYOOIwDpewopZqTJdHP1kDQqU5fqipvD1z1Io4JDACJz21zgKp5SdqitoUY/1LKvMQciJorI3uCLxZb3Hknp2pQds6Mb3x0zCKxyusajGx2xOyyLfLuBVVd0lVNra6oY2d3MiqVrm4tohOamEIvmlTRnBtOtzQMRH45G5hRteJsoflTW3BrkeclXJUmlxwadD3DHeBowJrLBqTO2RjoULjZcf0oC8y3PKq+SSHuzKlrZHaLlaTvsRqEq5SupqUSwMdSin0e9Hl4XwdkKdEP0MAXhuTrCNTPdzOtb0iOhuBURNU4LFRJ6NjjF72bnZG+sW5sXBE2nTIuo/8vOyUMM15IlzhIRWKx2AZQBvrTupkI3e2riTycHQmQ6dxllELLoOZNOz55VKEKF65XaNzzPuFNNC5d7O2Xkl3dSf5R6IicrzHDRTRoH49KkoTNGUv+5Cv43XaH72Kqqa+bb2xhAKjtPg4rtnY6VOpOluIElKV32XWvbrZS3mbWcsAFK15w+6jTDK9PtJOEXlCds/cc+9J96Nwa9opWCFnVg4yZrOXPFLbbvSG92VaxhhKarnN3u+Z08rLCsy5n7o7xhgitNmKDJ6twz1Wxo3So0tzCzW7DBwFkivfmuXgXKn1fQDUYfrjIQy8JYbgGHqywrvUyxRU3PxSStV8CVADMUzUJceV6nYJteJSSCqOA2MYMY44xC0Tr3xy3eFOgs/ZAitYiAhj2jjqKgi7swJS8tTQ7iokthgqYp4L+hDLXV3wOkzOzil1Q3ko7IoMeEcDIJBMhIR4hhFWTW/1Hk+lkngcxiEnnT7fsxsaEfHlzpn/fLpJgnUi7VPq0CgpsvI4/jxKnWW1ibAiIgykmdYJ6BGcIbXBUxiyZrM2LvyAzPxp1Spr1cQuXbvvoGVI6UsrW5nBCu+IsUZ6T18eVjAPjqE17xD34Ha899s6U49uypWacd1fbX9jwviBG2YIVhNiueTVCN7zYSSy+DI5IhSsXxAWFLwT3rEaoDu2s21oWFXrxgp2guczy9XZOTS+XnHMZrP5+9v7t/kJ9Os58r/7Ztv84Oj/2TOq56Omry+pPB4lBo7/6aHr079t2c/v3xovAXY9n8q1eR+9Hmz9wzO5D//iqwmzkOn56tjXJ9TPZ/CdE80vWb8lpd+3XTN9aav88cIKWOH27fxKZju/teuB7z8+Gf2DS+DqoeRLV33xnDZ+m1+YnN9DCfzkeXu+jF6PKt+/+a8nz1+wNf4laOrZ29erDsBJ7CP8EXv77X8D5Hr/qiovAAA= -->
