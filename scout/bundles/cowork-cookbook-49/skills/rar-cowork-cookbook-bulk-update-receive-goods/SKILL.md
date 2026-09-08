---
name: "rar-cowork-cookbook-bulk-update-receive-goods"
description: "Applies a bulk field update to Dynamics 365 F&SCM receive goods records in legal entity USMF via the Cowork ERP plugin, returning a dry-run preview workbook for approval before committing changes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_receive_goods", "rar_sha256": "edd847dea41fb65943c57ddb5949829443864071a82b0942d1d3acfe00090abc", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_receive_goods`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_receive_goods_agent.py` and in the RCI capsule.

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

Receive goods Bulk Field Update — Applies a bulk field update to Dynamics 365 F&SCM receive goods records in legal entity USMF via the Cowork ERP plugin, returning a dry-run preview workbook for approval before committing changes.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-receive-goods
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
      "description": "D365 legal entity to run against; USMF sandbox by default.",
      "type": "string"
    },
    "new_values": {
      "description": "The new field value(s) to apply to those records.",
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
      "description": "List of receive goods record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_receive_goods_agent.py` and embedded as the fenced Python below (sha256 edd847dea41fb659…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_receive_goods_agent.py` first:

```bash
python3 bulk_update_receive_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_receive_goods_agent.py   # or on stdin
python3 bulk_update_receive_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Receive goods Bulk Field Update — Applies a bulk field update to Dynamics 365 F&SCM receive goods records in legal entity USMF via the Cowork ERP plugin, returning a dry-run preview workbook for approval before committing changes.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-receive-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_receive_goods',
    "version": '3.0.3',
    "display_name": 'Receive goods Bulk Field Update',
    "description": 'Applies a bulk field update to Dynamics 365 F&SCM receive goods records in legal entity USMF via the Cowork ERP plugin, returning a dry-run preview workbook for approval before committing changes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-receive-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-receive-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '954411628e83abce',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-inbound-goods/receive-goods'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/bulk-update-receive-goods', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; USMF sandbox by default.', 'new_values': 'The new field value(s) to apply to those records.', 'record_ids': 'List of receive goods record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when receive goods records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to receive goods records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to Dynamics 365 F&SCM receive goods records in legal entity USMF via the Cowork ERP plugin, returning a dry-run preview workbook for approval before committing changes.', 'example_request': 'Bulk update these receive goods record IDs in USMF sandbox with the new value - show me a dry-run preview first.', 'inputs': [{'description': 'List of receive goods record IDs to update.', 'name': 'record_ids'}, {'description': 'The new field value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; USMF sandbox by default.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you have a list of receive goods record IDs and new field values to update in bulk in a D365 sandbox, and want a reviewable preview first.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateReceiveGoods(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateReceiveGoods'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; USMF sandbox by default.', 'type': 'string'}, 'new_values': {'description': 'The new field value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of receive goods record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateReceiveGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abOjSJblX9G8NpvMbCICJAQSUVZmwy5AQqwSKKMskh3EvkqQXf99HEkvMrMqsrrabD6NwsLY3K/f9ZzrD359c/ouLpu3z2964BQL3smyJA6ahVP4C7q8lU0KDmXqgv8Lryy6JnH7rmzatw9vftB6TVJ1SVmA6WRVZUnQLpyF22fpIkyCzF/0le90waIrF8xYOHnitQsUxxbc/9bpw6IJvCAZgkVUln47X5UNOCbFIgsiJ1sERZd048LUD9xiSJxFFwfvGrGasqiyPkqKD2Be1zdFUkRgZb8ZPzZ9saiaYEiC22Ie/NA8LIFFVdWUAxDsBuAyANbkedJ180wvdoooaD8Bo4K7k1dZ0L59/vlvH94ScP72+dc3L3NacOuNAqaZD5u0p/L8rDuYlgEB4Hk1AmcW4LoKGrBIDm75Qbh4Xf3YBln4YfGf/5nenCZqf/r8pVi8fl/e5n8a0H02syudtgv8hedUjptkwA2fFmR2c8b2Ze7s5hbEoog+PWf+JqmsFn+dn/34XORTFHQ/fnkrgQrOHKkvbz8tgDO+vAE/gfNPs5Tqx58+ZeUtaH786Tc5be9eA6+bhQGtP319Xb/EgoG/DU3CxVddYenXWiCSSRUA4b+zb/49VX+Je7nk63Pwj2X1YfF9ybM9fwX6PrPNBXK/Lxb4AMx8+3Qtk+LH1xog3kHhFF7w409/JtaLAy/Nkrb7t+T+/BQcB44PvPVyyU8fHuH72wJ62fZN5p8vW4GE+Z9YAoa/L/fNUX8m+xHZfxCdJQWozfdYflfc9yZAf138/Ke2/asJHxbhlzcmyECJNI6bBZ8Xvz5S5Ocf/N9u/vC3vwPR/60Yvewb7yHha+4USRi03devP//QPm7/8Leff+grkMWBk3/tm+x7Mr/n18c6f/Dga9SPf5wL1jeLtChvxeJbDS1+Lav/1fz90+LkZIn/2/328+L3lTj/oMVsxPuiTxf8rhpboOvv/PjT298B5hTAmt57PAb48R//sTgkXlO2ZdgtdK/suwUIcJfkway8EScAMtsHagDQC5o2AY59jQP5P0d41rgMF7/8H++Bnh+9F57DM1B/fUL01xcYf32A8S+fFgYQWDYJgFiAmBqpKF8KJwKQPC8G4LUNmgEAlDt2wUdQxx/nkxm6f/lTmV8f0z9V4y8PbkmeSKfRwoxybZ8Fn2Z7znFQvLT3AB0F98DrgeSs9IAaYQKAeUb8tswAb3Sz7W2aZNnCT8BagJbGh2zgn8+zsF9++cV12vhL8YRldPHkqxYGA76ps/j4EdgTZkkUd1+KwIvLxQ+//v2HxX8t/tWsh/B5DQUQw8v7QENRP8oLUE19DobNXAZg3PEf3v/17y+vAjEFIFgQqyScCXOeDLIxDfx3F+s78uMKw9+JCpBQ2Tx4Kuk+LYRw8U1fsOj8aGaDuGy7hR9UQeEHhTcCqQ4w55sni7JbtCDl2nD8sOjb4LHqL27jPFTMQVk73S+LA60A7imzmbCbFxeByWWRAPd/S4DnfSCk+aFdUO8iPi3kOf8WldM4Vdw4rzVC5xmXmYBf04FwZ1EEty/FTK/B7KpHMTzdAwYBz3ivkH6cY/6gahDY9n3txxhnZkjjwZTNl6J9JbrTBI9WAqgyLqI+8Wf4/8srpdq47EFXMvsPaDpLekXBf0XlkYPaH/qSmfIX3KObeTL/4ku/Qpbrxf8PDc9sLsnzGsuTBsssWNnQ7GcY5l5vDtezPZz1mkU+Su63ruQded4B+EuRJSCnmvEvz5GP4L3GPEGtb4CvNVJ7yAeZA8Iwy30k9pyoTfNw6ZfiHek/ACsfsAZiC1AAVMns3PcF56fvmsag1Ofr31j/5eIZE0DyLqrezUBihUHgu46XAq2auThf4QRZHsyFeosTL/6DVXNgQDIB+QugRALKDbDBp2/o+3z6rvofJj6bm3nKo/HrQW02DwFAj2BWcEarW9IBiHK6Z2sN7Pz8EALMyKtutt0F1QEsfd4MmqDukzbpZiR8+jWoAPx+nI9PS+e7wb0CBQGcBdK+6oF3H4Uyhz4HrQvQAWAFqJs8KQCVA6e8nPAQ6ORz1QNUffWaT4mP2y+Dgkd1zRz0PnE2ZJ4z0/oiBKqDO+PvwcH4XpoAefk84rHuP2bat9Vm2TNAtgDkwIrvT5/8/+lJ4c8eYfEu9/M/7V1+/J9tbx6kbP4xAT4v4q6r2s8w/CTSdx79BAoLfuraPjj14xMFPr7q/eOj3v8g8Gnr58X/TKk/iHgVxefF8hPyCZkf7V9J9foBH9AfKfvjen46o9pvqAmWL3OQVXPERkDi3yjufQjguagBoAQGPymvnZnyBsj5gfHA/V+K32f5XGUvTPkAAvO76n9wPcj4Z7S+URF4VHRgbX/uBaNg3nk9aqIN3j4XfZZ9eAPoGfyrHdfMM/mcw+28QQPVAnqqLgkeV+/IN5//cZfK3gFoeyD9v4GjEwIZiyd+zvUxp9afweqHb1D6tPXBNi9YDfzZiG6sZq2fe7O5m3ug0737Z02OjxMn+7RgAoCEWfv7lH8R1UzUv6vMp6OBgz1g7IfF7JR2Jlbg6NkPc1U7LSgToOJ3dXnQzNcnzfyzQsxMVH9golcX4ESPKv7Lk5laEFG3vM9ZA7a2Tp91310L8PtX4N7+GZA/rjRjAXj+oszHqB/bn+blQFSyx7qgPNp3g9vvLvCth/5n+WfQzMxC/PLzbMCHF5aCI9j3fFh828IAF742lY+df9GD/frP8/ZpTq/HlPkEzAGHb5O+/eHDDd7+9h29njp/TfzvGL4H82eO+V4jsBCY9kltc1y/Y/JDNsB+wKCzmr/Z/5sW5WNHN2sBtO6ef4D49Q1UiQNkOq86eW0JwHAAlR/buTGCAYaABcH1s9rBs39/s/Ca2MYO6FnBzMD3t+uNHzjrZejiGLFGPWzj+y44I7YrYr1Gt/ga2Syd7cpFiPXKX/qo44UBgiAE4rgekPcEi6/PygIiZ02ADz4CvAl+ewxu+S8rnlrPLvq2N3ngwNOYX99cfA1G7tatQD5/NAwt3WAFu+Pegi2MSMZItMyk0qDx7mDBJWG3nsjw4xhdlM7uWYlOz8eKywxR9JlVzB5IGFFh2yBEZeUfJnmbuJLv7r0BpWlS3O3zSSwmSER3VwZVeGzam1LZSMal4vPi3gi34a622RqJtwVyogTPCuFBtLaGsbeT85I+6BJaw1h4LgIOz9ZDCtGFWi8hZY9a69aCYWWFiZZwXhp3aYvea03QRgRRaSw16y7ZbwgIChK+P9G01GhqgVtnx1o3xnbykmTby3ri2CdMw8pKkE/lZoQNdWCxXbZNG9FBeOa0SiW3Ez2Ky8/V0osGcb+WzLO9KZxa4uO8J1f61TcgW2EQzBsmBPMVFEMgDg8GFENhXOjQ8712OJ7aUfz5blhKkkTR+YyfOJ43KL21EGYPCfdpb2g6zqA6da6nSSDWsHzbn6VK62nybApdbqZTBQUHOCNFQyzaurndTyl1K4rjNp7aKNW7Sl/nqyN/mvYnSXAEZDhoLS3bnbba+gXRkS6Uou4pylVNlKTlWhNllpy23alhpXt2FR0qYLOAlLhEPtuVkJr4qfLc5XkNkmPHifshcW2SxBvyjpp06q6u6CVDr314lqWxPaSpcdmPQcJI4uWwMW62kC5b2ug5l/Nj0tQc7HyxWXmqUh6SiYw6L3FOU6XzpCoXHYP31ekc+6ohIdDFOIUbyUJHrs9jWGTEVqBVpNkLenRdWlpVngavT4QoZL2Mxq79SWJuxyD0D3s5ptYI650JRY+gukLtklXRlorLKWPhLaJkMXVb9bcr7W+2+rjT2506VbG6HCvSQTwmOOS9dTIbNshs8eI7LndssW5Td4c7Q/vpfntxYDr1l5tsSineVaorgUtrmR1IDXaigWK3Vs8ygssVo4NPXBl28Bni7m0y7o0tkbaYkMdFEDLRyuFNA7lW2NbxMcK5Y/hoT2GVW+jx7gX3paRFG2vbK4MHbyeYyVdQx/oZvFJgkZBzBcHhG9vQyzSk60i4kTrubXiKrZyEOAf4jrH4M1c0aTyu6GlU2S0vjMNqX6zaCfVICbpLQkYgjFZ5ib3n70pZQrtrRyGjix/SM+volWCpgWiaZ6amL4ogZ0ePOpPhvgqVHjsJW9bwmFWpF7dx1d6wdr+/+bVxyX3eclvDu29UqWBXEItqCWdU99351omlfc6XLa92zHF5kCYIONJMIem02SW5f/c4CNevYQRfTzJfsA5bQPJWJbvpdK03enPdyGd5sxXkuJ72a7tOzMaeLLxCsOTuGpF2W54rMoyd/ZZTEpbAL2CVQUJNnSFOZKzuNuFq1MVAux5yetop9P6eV052i+UNlfXIJb27K7YXvXFa2/txWQtbrVfLLbLEMr2Flzeek+lzfBFaUhT1PKBFfsusc6QnskN62liclpuHnAwIkaaP0Yzxlz00nRzq5IiT1CIyLBGY2XqptVmh0Tm1JSm5BjdUipJpAq5bxrLAiwrv7mKxu9jXQV1nV5Xea9gmXNq2UXPG+mwJ1KpcyZSXqWCjcorO2LnyIdldrviBGnYcZ9/K06FnsH4zmilc+7xLmKnGmeN9tYuhoxeiZlvzfpp7HrIlN6VrYuM2y+qeNOTjutkNrtJb0D0ojlC2WpMu1U+5QG7gVXplbMtVAlyKI1ol2jTcivlZb8tLL++pMxPxHjY6ZF/eBKKgRqHaENKeFvhj1qVUHzG1QNLqJdvhkhbad9lgt1e51qwLRGxTPLwQrM3rwuqgCq4jJrnhZhjd23F+rJZsxVYFUznLyNZvbJVKlL4ceZVFkMmuaF7abHLZdu97DqlvJCu6Nmw4WcsdWGhb+SG5Xa9ZlRHVrat3WERYe27sTmQvIFwvZ6IO59PpMvaXSp+TijhOGQGHjlnSZwugH8EmGsFm58RU1RBJDH93YsqDgdnniZrW8CqUFabrcnbnhmoUwc11uSQIIiyKAYYTBhYU6+Y0yMFsjtu8EcSsCJOrHUVUkNJL7OjGGOtpDls6NXGquYs6tfl9S7vRbXkKHYzi/GmrNdiB2LSAi6+EKKx3y4ahPHEaaFFiqr64He3KdhUqvJXcOI3crvRyn7tGxd2tluQOLq+8GbWTlhqHjVPX+kmtmoO1xh106KLmJIrNCbHPOzsuiVhx9vYF0ryrGZ8CqzxzXHstY4zfRKScyrSabjDTM+9ur+W8ya5wHhVt1lQEuzU3ioKoYxe3aFrc17ltx9TU6ZKkEpR4F5a1Ux3YW7AJVXcMk0gw5KKKhEJBIDoaVJ4qDZrJpX3Pk5qTYT6Ft/QqqAbIHEng/Mi7Xyu4k+pRJO0y2bJ4dm7KrqKVwwgPyymxJWYsWxG/Hqzt0s5udJJYZFEjO7EvYxiyVhBDDpmxNqlrub2eVTMOBRS+Q8x5NAs2X9fU4VavMgqSj+yFHDld9sNTb6Zmw02SiR9gdkXtbpSR3mOHHC74CnEO44YSXZ6sPP2m+dlk+Ul/4aiblV7JcVuvAtxp96QBB33FqpBBNyq6y9zbOrPqzOETfH9NGH9/c7gk3/QacqASEsc2ec5ej5eQPjDsubYqK42Ljge2a6nAc05CSgNSJwcs6JGA3QVe1RQSd7bTjGOVMxeo5jZdriRMI88isVumeNZLW+p4V1dR4t0by4bSkAm5itqJBHSNt7h+SSKllwytuHpnPt5cs4PGoXEpuRh2lWSiUxoA1WvHdotL10MBXbWCEJNTdh4JzO1OLuns1IuY2Yy+7UHnih32021CuRKKL4cQMOJS3e4NS6VuvtcHpJajxig7yIFNWcwcaYExw5LdhgAg06xwWu7OZ8IpuZ7EVd4razbf3GCbxsuIKvmjJhDUUl3pB5k7hu10VoCvnGsRmieRpcQ2H5gDZmQnxoz52p5EO6TYBkHZoM2mMmMtsYvw43nJrjfbqdW2mcRcte2qmrr2pJ3Ci8CpsRQLp2N+hXV7FSm7TGnyQvSY0JcB34YKAjNeGvBuq7QTrzotHCJE07FKS1DjKrzFbN9zjlWKFJxeKOOK12feOm622ym9lgcolRBZ0M0YX11NLaXpiqNSBmmu7DqsJtFcerQiRpeVJNSwXCq4F5qiztd1sldwchQOhRmvNKXbL6+X4JhK8UkO9YTu8ztrGywi1GYadS5+TYdYUFzOA8giVy02HgipLoNls6vkqqooNPYT6C5TqRoe08vBvDlSLoLy2k9mFV3CpO4i/sjVCuNgJykCB22g4qZTrghaNRJ/PIU1JZCSwOm0b59rceAweldbqcOaQjQGK6cPC4TeavGRSqpo3C1trNr4A0vKhAZfadHF2fO2g6A6wz3FD3ILyTcEXayOg59eLR5zLSOUmvjSnc7YxE8a6AwGM5kkNRpjNO1qGGYtZy8d5E6PeIzVsLQK2bSto0uJQIJSbbZBHh7vg5Lo+iGHS35PmLf00vk0lO+EadPQJuImy9WZptd3ym9kKtlwy65MjWU5QUuSrdqGvrj8LsQ5t/fo/Z67XdA4u6zu5lEaK+NmKAFEjabRQlJTDF2oaMu8lgPftQO04oVViDnbugyvx+DMtRBSM7WsxmFBmyyq61kpJvt2ZFMDiWiePMf9/oJdIOuot4lbUDC2VGhBzyt0tyI0UmftlB2ZPFD5EB8O7kqXndymXPpyqNMcIRHhtM/jZU8cOBXaURfYEX1ajCaUtzUAMteW4r3dGF19oYpWyoGbtlvFAtw01JlhCF1JszcTOl8p3WuRW5VLx7uSH6NVLwmyCm3vu0lVk50sj515zwkK5Y1J40u96qscIMrpuAId5srT9dUUIKi1dLA0ieSd6a6kTWgeN4aXxBJFQO4OXvdBDo+oTZ9OLFUrx8GTgJVLF8tG1DX2QyQu7Zxy1onTeiIfmYFSxMWSZ7LpMO0vCdR6UyIergZ/Pzieog733ZW49jRUi5xz5ZqKvKfLw7GGa5on5BYP1lgVintMxDQnYbYW6bDJ6c7LJDr6CKk01p5P1MYjPB3snLujn/JrXo5AW7xpGwkV3ZhakgIu0ejYHakyNsb19WiuJpCL8C5zBtpO+KqV+r61GBir+oPNYe2hS5wmuRpXRVrbDra6lXQ03QK25QgJuVg3Lo8pND1HoDvxbjAD9tAQHm5ovTGrZOp1uErWxi6lpPjoKu4QTdVpjKGyENXx6CcKiksKQd8Pbo9EjRVUwHOhwmhIcTJFXEfWx7Wo3Zutr1qp6IctiQ0GFNvI9XgCwMuk6BXaaKIunzSDVbjLbtd6lIoZ6riyr7odaqiqu96JvBCVn4/yjoMaxhe9HK8mWbxatQugynMm+BbiAkIPI3FSRpK3PJceu5yRksNaawUL5jzQXyRi7fkxRO200uiV1vaX+7aUNdRxboMaKtvt5uKFVGkOprph8mV92K6OHVIW220RYK13dS58i7P3zdEvj8z1vN7HVWfAXn2+cF4nQqiRJ66Ie1ajhfumnM54YBZ2LvvEErM4Rt+pO/8INnxodrQiFatMwknlKfVUPfcmsIvYyXatwzBmHjVcqB3xlmHeCV/vNsrkZOebImNoQsRbj0XLsyufwcjrbdnI0tK/lmdI3eHFSJmVcXT03oCuqpiHIns6rI6JRXdMJY/i0epN0Bkr+riqhzjMr0sE9+EVJJiEKmzW6T7STdmj+EkenDtZHawbQmS9cFHohDGYa3Re7mBoNYRbDm4vp7tWXcpwwHYwD0fNDbG6NtsGNuJZk3/LhT1f+XfDoAjMT6Z6L0CGOlRJEu2huCkhAkCPcwFcUvOuo8sMeghvrJkcR7slXGg0lEbReuYkNx56gGxeMi5ih0ZrnFn21MXuHUotl9BG8mTset2yySE3vIPkb2CxztcHGy2M+O6jokSZHKLBF9iyrLADHZNnagF62DmB33XpKOyTg1lcTzbOroV8fVY0Ed24jKHD+nk7bta1GBsYLuhpsEtrZXk67SVr6cGXuIVK9pYjaqKTeq5TNwgmvIu/uhR3xmA1ZK8vl8mxzffVSqSH1cQ21qnt9yrOO5655rIOj1oNmdoGCdttM7TCfUcVWHJpIYJSmzDZmMWdXK7ubJNgcqCeyfFo7Aimwi9gD9eqOFUwhKx3+9W67NwTkhnFcIFq8tKuC42wzSN54DvQvfL3gTeG+JyLO7YNEI/MfSVtdis0I3GHTQnIUrDV2Q/D424zDBm93t91VKT0kAupjYAyuULhCWfK99XhiBX++rzT5DjMhmOl7jUfTREbh7cizvsksyOWYH9mLhn/7ifCGaMlKLitz2Je7X1bFlZjn2lIKl1zwRubIhwu/YTvVfTgd/xpRLASdWnHjZnkWm/XZAAh3GZr+7ZlniCFSjtGvm8uqCmvYQzn7wEoV4iM5MnKQ6dm1lSd2AhTAuqVg6RWoX61FFOeLz1kEjzLVQ+D1VxsyD5GUsyW1sBtt87RVnfpFcaU2qx4ADr3YEcr5X2U8GQUMdJ3CTE6uTmpHI4obsb2KrzSXagSKytdNlbV4x6GbzZjiRM5H+yQTef1G63RFW469gwOuR6Ohzw7hTjk1dXxJBITmWFnCD5l+v0Ow8trsDm5JovJBGFUYOszIL1cF72rE2dVa46gFaILM2C0y0EL7Ks3SMPpskyo+NR39ro8XRBbrqYjs6xQchrQownlaYD14zrcQZpP9RKdHQYhKEVzj99RAV+7lHQYUazSCJy93F0itHKSc+lat+G9TJuWw928o2ok8Ja8nW5DdM1NcVe429J2olEbSx+yojThj5fThiuDdBt4urE9a7Yrjx4kGa4vuvvGtWtUPl1zqrK63GmYi4KVzUoYjhrcllpLTmdU6t2oYDlhIvfSBmw/TDdAqdVBvl1Y91KPqRkW00a+oVNA8CsuzDKj31F6NzjWpSKqI5oJvBXy8e4s3mM+uQao4XfSYbvJmst55XrT6VgQx4YTHSof/Nsk7oj+fM9dk5fNZa4cMZdn8vVyFTqFFECY1pcXaYPW9FK+s0vI1LZcOVH1eNRKqBuE0O9FF12neICcktEiHFUqzba7mgPVNpjrYIQKOlsT7Sy1UuhwYJgc9CbrfNslp+YMKmKgN4SlKuN1LAZ8TKxh7Q14kwlh2F9UxoakbXUgvMMxEUYVHzWdIlhmSNjU3F3b4x6CHYjYQZEXoRXnc8WdytT+3Ho+RXT9vjMxe9NtetdClyJO1zdJ2eND1if+0h8xsHE4BKUcTX1KBnd0QozC4WOt4+M6ifele14GILhEFp6naLCHA5OuNn4JOtwhGqbDYTfomrDJSVtKp9S1Ap+fVLlrWihYc+7uEEQUaSveNqYpfc8EB41Fpg06cBHp9dfT2jOTlWP4w0TtdOkoM6KxXuMDuSzi4djnG4uGrru0xPIE39WmdfNqGZ9uCdTUx20+DE6wRAMNr+spsNHbblgt99fCw7Yd3FZeWPdTyO+YDWiKhyj179uRJx09UPrm5HtVpnonddl4JzkfkDyGNhB3UOu6gpmJqDGjOTqdKg0U2u+D/tSvicorD8ituTPwAUzL1/BFO05auT4gE4XtuQZF8z7DV+j5toQwxWPNaNqxdIGUOBtpJOrVhXepIikBGya8FLa9guTpGuzNJlMOeQB5F9CdXXsjzEC3ixSVsDR9hbmVu1uanO88tsTGOywlJNoQVz9d3TqL6OENFzR71Ubv07S5GvsAzwJjLFF2VzkCavVYSFn6bhLUBO1FmT55OiLgZBWvnf1t0+R2uEPR2zGkevW4O1jVhDnxnqhTvbrs68mAxi2qpVor2QREqYgFJ9bO2AbMUA12fFthNEmSf3378Da/B369zf3vvw6bX+/8P3uT9Hwh9P45yOPlXuD4nx9rff43dPnbh7fGS4Amz/djbdZHrxdO//B27OOfvvafp43PT6ze3wQ/3293TjR/ZPyWFH7fds34tS2zx+cfYIbbt/Pnie38BasHjr9/H/k7td/mjwWBcfMHVl+78uvr08rH7fnjjsBP3kd1QfR6W/jhzX99mfQVxbGvQVPNZr6+JgDWoZ+QT+jb3/8vKac17BkuAAA= -->
