---
name: "rar-cowork-cookbook-bulk-update-cross-dock-produced-goods"
description: "Applies a bulk field update to cross dock produced goods records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, returning a dry-run preview workbook, then a c"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_cross_dock_produced_goods", "rar_sha256": "de73bf1bee5e4353ae7a00269a790a9c86c57cdcd0902746947e1d8aca415b55", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_cross_dock_produced_goods`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_cross_dock_produced_goods_agent.py` and in the RCI capsule.

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

Cross dock produced goods Bulk Field Update — Applies a bulk field update to cross dock produced goods records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, returning a dry-run preview workbook, then a c

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-cross-dock-produced-goods
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
      "description": "Explicit go-ahead after reviewing the dry-run preview workbook, before any write.",
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
      "description": "The field(s) and new value(s) to apply to those records.",
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
      "description": "List of cross dock produced goods record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_cross_dock_produced_goods_agent.py` and embedded as the fenced Python below (sha256 de73bf1bee5e4353…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_cross_dock_produced_goods_agent.py` first:

```bash
python3 bulk_update_cross_dock_produced_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_cross_dock_produced_goods_agent.py   # or on stdin
python3 bulk_update_cross_dock_produced_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Cross dock produced goods Bulk Field Update — Applies a bulk field update to cross dock produced goods records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, returning a dry-run preview workbook, then a c

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-cross-dock-produced-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_cross_dock_produced_goods',
    "version": '3.0.3',
    "display_name": 'Cross dock produced goods Bulk Field Update',
    "description": 'Applies a bulk field update to cross dock produced goods records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, returning a dry-run preview workbook, then a c',
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
        "upstream_slug": 'bulk-update-cross-dock-produced-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-cross-dock-produced-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9e2323ec11e328c4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/cross-dock-produced-goods'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/bulk-update-cross-dock-produced-goods', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the dry-run preview workbook, before any write.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; USMF sandbox by default.', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of cross dock produced goods record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when cross dock produced goods records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to cross dock produced goods records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to cross dock produced goods records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, returning a dry-run preview workbook, then a c', 'example_request': 'Bulk update these cross dock produced goods records in USMF sandbox to the new value — show me a dry-run first.', 'inputs': [{'description': 'List of cross dock produced goods record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; USMF sandbox by default.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook, before any write.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change a field on many cross dock produced goods records at once in a D365 sandbox and want a before/after preview to approve first.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateCrossDockProducedGoods(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateCrossDockProducedGoods'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook, before any write.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; USMF sandbox by default.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of cross dock produced goods record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateCrossDockProducedGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abObWLblX1HfF9GZ+WSbSQxyRUU0EjOSQEKARLrCyQxiHgVk53/vg6TrzKxyvVfV0Z/6Ohy6gnP22eNae1/49c3u2qio3z6/ab6dL3g7TePIrxd27i22xb2oE/BRJA74v3CLvK1jp2uLunn78Ob5jVvHZRsXOdhOl2Ua+83CXjhdmiyC2E+9RVd6dusv2mLh1kXTLLzCTRZlXXid63uLsCi8ZlH7blGDzzhfMGNuZ7HbLDACX3D/U9vuFz+mfminCz9v43Zc6Nqe+7BogHJOMfy0COoiAwe6QGm//th0DxW8RRo37aIIXpIXItM8zMn9+6K3085vPoBbbVfncR6C7V49fqy7HOjl9zFYMxs92/th0UZ+PssHxvqDnZWp37x9/vlvH95i8Pvb51/f3NRuwKW3DTBZf9i6ne1kgJnqy0p+NhIISO08BCvLEbg7B99Lvw6KOgOXPD9YvL792Php8GHxn/+Z3O06bH76/CVfvH6+vM3/TkBPoBXwqN20wFTXLm0nToFvPi3o9G6Pzcu0ORANiFYefnru/F1SUS7+Ot/78XnIp9Bvf/zyVgAV7DmWX95+WhQ1OA/4BPz+aZZS/vjTp7S4+/WPP/0up+mcm++2szCg9aevr+8vsWDh70vjYPFVU9nt6ywQmLj0gfA/2Df/PFV/iXu55Otz8Y9F+WHxfcmzPX8F+j7z0QFyvy8W+ADsfPt0K+L8x9cZddH7uZ27/o8//TOxbuS7yZxS/5Lcn5+CI9/2gLdeLvnpwyN8f1ssX7Z9k/nPjy1Bwvw7loDl78d9c9Q/k/2I7N+JTuMcVO97LL8r7nsbln9d/PxPbfuvNnxYBF/eGD+Ne5B3Tup/Xvz6SJGff/B+v/jD334Dov9bMVrR1e5DwtfMzuPAb9qvX3/+oXlc/uFvP//QlSCLfTv72tXp92R+z6+Pc/7kwdeqH/+8F5yv50le3PPFtxpa/FqU/6P+7dPCsNPY+/1683nxx0qcf5aL2Yj3Q58u+EM1NkDXP/jxp7ffAPrkwJrOfdwG+PEf/7HYxzO+FkG70NyiaxcgwG2c+bPy5ygG2No8UAMAnF83MXDsax3I/znCs8YAL3/5X+4D8T+6L8SHZij/+gTxrw8E/zoj+Nd3BP/6QPBfPi3OQHhRx2GcA6w+0ar6JbdDgNnzwQBWG7/uAVg5Y+t/BDX9cf5lxvtf/iX5Xx+iPpXjLw8Yj58IeNqKM/o1Xep/mu00Z6x+WuUCIvMH3+3AKWkB2AGwUfpE/aZIe4Ces0+aJE7ThRcDfAGENj5kA799noX98ssvjt1EX/InXGOLJ9M1EFjwTZ3Fx4/AtiCNw6j9kvtuVCx++PW3Hxb/e/Ff7XoIn89QAXW8ogI0lDTlsABV1mVg2UyGAN5t7xGVX397eRiIyQE1gxjGwUy182aQpYnvvbtbE+iPKE4sHB+4Gbg4K4u6nVkubj8txGDxTV9w6HxrZomoAGzp+aWfe37ujkCqDcz55sm8aAHhtnETjB8WXeM/Tv3Fqe2Hihkod7v9ZbHfqoCTinSm+vrFUWBzkcfA/d+S4XkdCKl/aBabdxGfFoc5LxelXdtlVNuvMwL7GRfARe/bgXB7pvEv+UzA/uyqR5E83QMWAc+4r5B+nGMOWpYMIMKzu2jf19gzc54fDFp/yZtXAdi1/+gYgCrjIuxib6aFv7xSqomKDvQzs/+AprOkVxS8V1QeObj9p03O3CAsuEdP9OwTFl86FEZWi/+f26bZJTTPn1iePrPMgj2cT9dnqOZOcg7ps/mcVQT5+izL3zuad9R6B+8veRqDvKvHvzxXPgL8WvMExK4GZpzo00M+yC4QqlnuI/nnZK7rh6u/5O8s8QGo+YBEEH+AFKCSZqe/Hzjffdc0AnAwf/+9Y3j3E/ARSPBF2TkpSL7A9z3HBuFqo3ou4FeYQSX4s2/vUexGf7JqjhFIOCB/AZSIQUkCJvn0Dbmfd99V/9PGZ2M0b3k0jR2o3/ohAOjhzwrO0bvHLYAxu3027sDOzw8hwIysbGfbHVBB2YfXRb/2qy5u4nYO9tOvfgng+uP8+bR0vuoPJSga4CxQGmUHvPsopjktMtD2AB0AnoDayuIcpBRwyssJD4F25j8y771PfUp8XH4Z5D8qcOav942zIfOeuSV4ZW8+/hFAzt9LEyAvm1c8zv37TPt22ix7BtEGACE48f3us3f49KT/Z3+xeJf7+R8mox//veHpQej6nxPg8yJq27L5DEFPEn7n4E8AwqCnrs2Djz8+0eHjAxo+ztDw8R0aPj6g4U/Cn3Z/Xvx7Cv5JxKtAPi+QT/AneL61eyXY6wf4Y/txc/24mu9+yU/+7ygLji8ykGFz9EbQAHyjxPclgBfDGmAVWPykyGZm1jtAkAcngFB8yf+Y8XPFAcrJwzlDm+IPSPDoDUD2PyP3jbrArbwFZ3tzTxn6n+ZRbFa/8d8+512afngD4On/azPczFDZnNnNPPwBr4MurY39xze7nKHBfoyFf56M2QHgqwuKIiw+2vNgsLADIGPxxM25auaE++dw+iLzOeXvIIMfJrRjOev8nPDmnvCBU0P7j6crj1/s9NOC8QEmps0fk/9FazOt/6FGn24G7nWBgR8Ws0uamYaBm2fb5/q2G1AwQK3v6vLgnq9P7vlHhZiZpf5ET6+ewQ4f9fyXB129s9WcM2BAtru0/e5ZgJ2+PtnpH0+aUeFBqD82P/2ZyuYLczMBmO9xPKiR5t3u5rvnfGvI//EYE3RAsxCv+Dzb8eEFruATDFEfFt/mIeDJ14Q6n+DnHRj+f55nsTmzHlvmX8Ae8PFt07e/szj+29++o9dT56+x9x37dy9C/++aiAfVP3hvDvV3zH+cA4gB0Ous8u+++F2j4jEqzhoBC9rnXzZ+fQPFYgOZ9qtcXrMGWA5w9GMzd1YQABVwIPj+LH9w7/9uCnkJaSIbNMCPv6qQmBMgju/j/grDMdsnbRhGibVNrmF77VKEi5Ou53rwGkbJFbFekT7iUbZrrxDcwXEg74kkX+ceMp4Vm7UC/vgIwMj//Ta45L0selowu+vb0POAhqdhv745xAqsFFaNSD9/ttAScSCTdE61A11gahjvZlfKA9u6eTcYWIpXsrK6H3n0drrDMSzX1OaIszFo9ySLiVJhT0/NcXk/k6XakPhoFXosNyUKYxrkiiKduJ2zzwJ1UAZqWt+G3uXKxCyaVUzg7CU7DZybXuvdvkE6CU+NUUrhImuCsLtRBy2uoTVuQ7G0p86So4uDtfNrKFpbHnHJrrGSxG2Sbi4rQ05Xjd4z9bWCfXUXBAPdQ8u+Jc5enO4jJKNjK61qN/YhP+gPo5hr16HpmxUCOo1s3G3s/V0zjwNyMidWbFnCkBIZbq18R9EGmjRgum7V4iRJgc7WVFVpnEkMvbZCWXQnh0ZAFeo2U7qm48oM9Qw23XQW22OblXI2qlU3GWPQTykhNuug3+XkfXC6A8fxZtpt9hFn4uOxjF1JNzJZh/19zZR6XfAXYsPyWjTCMo/CfJwmxpWUCDvUOkNjXJYmCvHGsyo3upczg+uVNl7rbbl2DWLrcvw9pwNnz+l15TaSqd7DLYGOxvZ43PMWs+JXuN/1K0w8EUdyGYVHamS8g6hE6UYN91SN21LcnOQxD61jqqab6BQb2dIuLSnxa+QE2zYirKVDo6k2HY4FG0GX6kxde1n1souv4OsrXMvDqJ0OSVNWolwg6d1TN2F8NjU+uFTtfX+vxQbZiVXjsjh8ZyCUHJOzBjF6Bufrim1wdmnAVZEwpxYf85HAWKxMSE9klhfhwl7TSDoZloFvKmU56pKXbNvmLuU4u2Nby+F0eb8SYVv19rvDIB9uRq0K5VElDScxN4VEbY/U8RbnlC1o6O2a8RXBUtSu2hz3zhWWPBvetrsrHEpBg6bmmi05xRCqdNAcxu6IdqqKOCm3a5aH8Arb6PhShEWy50+Uw+90q7esWDaWG9XRNquiDb1j5jBhQ8nq0TmQ68LOV+3B9C1CLVtOZfiRgu4FSq32BVbyV4ZG9swmZaRQ2yR3D/y3aLyCJ4sE29Srjcj3/kZfLlAZLDkonLzALJQ7NCoSvOxHgfChwc3pCBlEnyulzVVJm+1qD7gWY93Ygw05phBmj0n07ULcpVW0F1bbOC3UNbSRAtqOcVHeJNgkNb58yHhCynvddNXAPrcJkVhRI4nwpFcRpRVtc9GaI786nC4FvUrYo8JSKt1ze4weChYnlENN685IUGIzTbKzn+4A5OJLokqSsVKgSZb5oGr3e3t7HXi6tcQjCE3OXrdIczvqNT9KrKSKezgn86zxJILtqG1LhfmpiK/R7RK2ywBKlgqPOvzoeH1bIh2WpUvOvkJOqsvGsDn3zuZc7viNL7AT5xpRvaH7ig23EgXfFCZVrLa+OERlSCx9YPyNqZsDI0bxpKrboE1qpRxKY2LWHWw3lnGn6URomljYUq0dqVydyOrh4Dt6ra716HTch4gkcSF9v6Zd6isivxeuFz10R0jfkJfDKUuSjo1u2tb1NhM5duN6nYzIthjP3c0qHMpwltUKL3rs0IVcc91Bqb+O9AvDijFEYyabhCURNLHK7DR02JnRIPAJS5iyyqVRpBS6ekrdULBrFuYGc5vZO2UTXuz0QiDpxRopnnIN5La9mdpKzciilM/QuZnUdDuwxnkXXH1hhRaBw7XHiYorjb+FgsN4uXJO2GWcmK1CbVAO360uJAcRiX/gyVOoVLwaO+EUpzBryUzfkli0P2z8cwkf05FOxVG+CAVYN+Enmg54fts03Xjd+nm53OHMXd7FkuBHor6BGFpJnNPxFO9t3sWuOJ1aE+2gU5CQ2PK0PGSmJnpiK+Jj1Ba5Wkp9rQv4bS9XZ+xwLOGGHw8xfWrjHVn4G6GONfq6LjI+42IEg+UKJm8nqTDoQ6F1wPHcjpRdzicTn9oI+FAU6iY6Lrm65lat6bH2uPPRO+MCYsy3jpQm45ClKqn0Ewypl5pai1QI4BCP8vvJyGHTsKVzNIzToQ1d3Q/vpzQKFEy4Qac75nYodj2eWmOUmaW8oQAJDewpXS9li6KgEirWa7sjt1ofZZW/dLhke5eLo+MkkM9klhUVmhdXRtwYxjG5u5eVONC5bhzanJbJbHUzRreeLCO+8KI4MhTBIpctDeWcc6o21VRSTCObPBofG10sxDgcCEGqzteQoduGSHZbsed1ulie4EAh5bAkecK6G+O+oAilg7ZbQ+9Rzrld9+ZwmwQaKtopxfns4HI2GZwIkx+VXqhWfry9huXI0YFtapFqrfarMWzQO4kzYRJFjJbU3nJ947XY4mV2CaXTebtXmFGrZH5Li2zGJNP2eoohc+gA1HP0vbLyM30s3M2S25jh/mYirCBcGZ+3LPuEe5Hca1mw6TsfwGNqx9bhVvW3qmMkDhdrjptSp3BBvZPFdIMQLeoqzrYKKYbpi2QBTw7VsVhSgGyk9h4H0CUjaT3W7l5W3Q3lyIqE2STqhoBOYBqdEl0zsgxuglO4PiWxKa80fH/ox7E0MyvGMT7MsMS+75bbfaVLLXIZ1+NJ5HdqWHH1Vuf3oEPw1hdYb6y0HEI2lqemQ/3qshrxjmOPSy2+XbGgde6rNVTysLdpjItsEpcQ2XEi4THNlWE38JQfDlGWypHuyGJ7RKdVqamyJ0jQKRF5zgZhD+6MeF6ei/qCi5f8pHN2zGfWRhvyadvvtcwErR0rc95JWA37vQ6Xd/3UsI4q5nuHbAJNjfoQphudDU7j0tvsh7uAcWUxDZ0QDw4GLuwI9tgKMGLoJkk4l/1g3a/i9WK13VLZsOixOYY4VWc+1rDe6egIuqWmV0mjVOeA+llqrSwyJrxjkx2orDKL6lDW4p5WOh3ZFJNlOTSY17da7Gn4JmEKD5Z9dZ8eRw3pze2gh1cRG4OyjrOYa6ieoDublp1TaI703bMPecGcgtQ78DQhtfxGgjBOw6OTEFWrm4PRubTid9KlKlyZZ6aTDbrSSy9vbWnwetBt7Z0N4rbVdcjXdRLu9A4YNC37A3rBZUy3aCbhjmI87uF+PAnJgaSkeF2DTgDJmSBVMQi6Nk1VWwnBOMspucv7vFUdcn3Ar822Fe78mbwlWsopZ0jaNImzcUhIT5TuFkxDvlE13BP0nXzMLX3XiXQkJ60ml2dFs2O6t8rzaRC1aVtfk6hmWP2204JmRRU77WAUme1FUVtVIW/QepZZ2xNZdDAY6LULyLUjxm4J0Ny0eGtlHHuGTIK43anjZQePMdrdTdHI6kq6mU2Gg82ioJlbdqdT7OnUrE6gCaWRzu6ybdS3YuJzhFyhoYPw4fpQS6Z9xFypdZiD42N5LpekVrZhaIaGeHOjKouSEN9LOgpvORP0m26GrnRUPW68LbOLNv62Rnu+C6wmWDGtLNkO3GqYS6KN6bK5qho7u2OpCBWSUl6RO4/fb2td9g7GeEHde7y79KN43DO7gyuaNRGn8QEKdbn2WeRwPwlthTBE3EZn+azld62hroyLWn6whq6Irpe24opWIGc6eaDgdG+a5fqUHi1m8Jwdd/VFvUeK1d2LXVRnRBK5kk6inRRjWrFDoi5jiyyuMTG4fMBawboxWKVpXYiFsebo7QSBTk9rDM3ztsIMvlea3SpmuEirjl1zleFqDG6Kb256CFPsy47Cz8fc1kzupgxBcjRjBqbdaktIPM/1gr9mzICPIxa6EhlXsNIKN0qv3O9XloLIV6IJXRhMMyg76hrohEN6EPU7BkbqkWaTm3gV8nWTg7GKUd0C1lkE6UbDZaP70pYP8KpjrxR1waTB7ydkCTW3rBjOJOvY1bVVNpSVFjc20zl2tIntGTpGGctsT2uC3VvTzm2Ng9Wf2ymhkE0lVJ5thefOOFNp2aYrMDW1m/aAeEZ0EevphMjejcfAQkQQuzFygmyAlocc7+GOP6bGaWvfpvoex2zZYetJcsiywe7iqriEy/vx4Cv8TcirAg5U5zREykUl4UTXr3p1jI+IFFyYWMVqFkwr2o1AWDS4brZnHSd2dKeS4QD4oM9TJRNGGrmdFWYduWLQliavowy0QY8nudvur0qDYYZNeiWBwQl2MS7OrrHV2tERwpQax3BNlOOPoU2lm5FIYENvSiT1CT8Jot6o6cqMKneq6/58V8lVfb6CIaw/sJtCC+A4PvCQ1cX30KcynnT2F3Kfdcx26XrRZhC7TUftgxovG3hPrc0sV4hiJSgMAEar4vFm0xHjRiZQZeypnD6zO48T7aAyl2DoSVI0Sa8XZBcodSml3fpcBb2mH+kdI5cH/yZLy0i/X2jVgaFSO5ynnKXDrb0TXWqgNBnehaaIHeRqjTd2XGt7pt8XfVmK5PXM45QeCW7gBO60x1sYvWli2d9ujIjdjjaYWlDfIQVGzZbYFFxD/4b1SyEc1ejIBTsBZ5FNkq3ajRUR5U4pHP3AJo1Cx3FTses4G0paEPbouPdFbSP3zlbU+nHn3SDLY9a9TDFTH5awcBstRKNkv7n2a1Sv8s6/TL5Z9hNxPolojp5WDkadr66gdC62OxNyt6La+Lq0HagT5BCdsHuPjiDJrax112dl2NskeRs7Q8myECW88+HSVxdkM1CNZa99RxCJEGcpszxnV3ttktAQhW4ImzDORc6auAy020CHAnTbFJbbNc6tVmC269Bt1waHPQk4+4ppUG0uS4KwbVq3MNWGzRPkiRfYjwESNyXbqbYk68zZ7ju8tlyfS/s2NKixWcad5/U3obdYZWmdCaS8Xs7rZtpN3hXOuJWtDNhKLOihbfNNojq7nnQwaL2FiN1NH8Z9Qk7UGoqDu3J0NG04+2NtD0epC4U9xy47XMS3EBVPV4QvfOtOwZF3NoIttuP8E4KmVIacYd5AJ37IY7Ww1aMg7W8dgl9xCM6uEF+baWWZjsIgp4bKsMlrNzgqFnAkRMfqkF1wZ9oIrKdcm5G6WucBugWHQURKR/C2pCKZnVyHEDl1XdyrZ18KOzLmVoECo6PFcLGvaqeq33ZHeaLOaZFARNsinV9i/rVdGdwdIdfJpCu3ShdktIeTetn1xYBC9Mae5MMJp/eaxFK+GreHJSlPxdDHYkqXBIoIGZsiYEo1HS5H6go105W7bc29O1b3NW0fSCs+kQF6NS6EYJ3vI8XtJ3+5anUmDerbPXJq+mZEu3woHPYKHL+MGqIu0PpYSPQ0xFmJ4mtXP1g1YdYTqzNlSFzx9DRZLLpJ0AOdQfHYmEITyUuE1xMXzPuRqzoJH/c9Y5py2mqTinhBoAqrxodIPOw2FCINJ7gfpGM2He54ee+ayMjd/jZlV2zJRfBZN/AaKvXtqvGcg6RApKas8iIUqR6zyqkQnW7XGFuMPZlTKjCDO4gOyRV8ZqzHZQImUzjOOJfcONrlNthgmiqLcallBxO6Tkwiufo1UEIVtL0dxWOAVY1LeMdUbWo0wyMr6NQgggsdwLzd3A43Jvds+7COvf0a4EZhKA7uIMU6DG6OlowMYyrhKVN2acdfaqjZX/bCkdMmeHspfVMVGpoZTxAknGXzljXRSt3dBP2Ic55F8lSltGFzlw8kLWSqs0yjEA1u2zawU+ySrGusRQkXJ8hm2xDrjPcFmGzdjjx5WsBNSsd00IFyWdqTbytkxXQT3txQ2Q8Kx8EuHiWwkOWX5BlBjmaCXpwq309LSFtRu8Aqdx6BcJ18NunzllNKNzsC1mwwYepav2Ii/nZuXVtabmUmO5FMTeU3s+/ya1+eoH3hEVAGrxRqhDduIoiWqS+PRHFBnOaEhOhGx9NmIm4ruIBulxEENwTc7CbjcmNz4hIFo9kxvKQ4ER2jCJI4tajUQy4dBwRPboYkLXtX6vBbcjn7kCyKS0Ft2niVBZzV+EmXGEi/rycvRI1IPyQ+civ3eAGhAGXNtcv6AA+OF0VxY6zZioEuiLvGodh9i26IvXocBKvU1stkFw2kBxUMD3Eo4iQGZXIbomllzLOCJEfT1Ubv7Zb1BTD5nETKt1HbaK2pzqjWk9Gbk9o4tSwNvd5dZYQ0FUfsb3e0Wdth2WT7AYN34j3AlsnoUGsNC1TTmFTdb0Ev1m2Tbr0MZFm82/tbZkM3a8QwJzaHQfLznrsmKZSHTIWo8pVjJmeoLkslN1XjkB52BgzwIyGPYOYfdqOkClZKIJ1H3BnPrwvBMshjvkpPDbZULtBlTARQLiEHMN3XM7PZCyfeEj1LLGkq3mDTdpQ3Q5YLEJQG/ho7H48OHHfhgNNjdakD5RiiMJYuC3do0TW2L8jGDYqqOd8qrMLJUvBzvbNd0hVk1XadapVvLchLcCRaXe2TaFbFSHBIe84hW3VsriF2qDrRJddjlWIiu3VCnVWaTJqjWRbC1trjPEJmFQVvHYLc593BGBihpO/bLaayx5CtBuxMnw8hpJCb41ZwQsQXJKlFG9hxyQIe+4yK3aWu5OMBX9lT3fYI3VdDKavWtYpITqL4qvcbSt1XRN1JNXm/ABg8LIlq8nVsEPo5EXIXp1qoqd2c6KaAFxiyTC59mHgDNfK0rflqVxueXxqaaxyx2gVR6ZdZqJBLbnutsNtSyEljys0rYt/NpbC8t+u4xfh1kIUZofj2ZdWi6RXFpr2UyaoQock1sN2mG9cHGMFwm2TyiwWdx2F7va7OS+mmJRpNE+l1efP2rH5nT+rB4BJpnSDYiaCUbVwXKVY72pGlvMGhylxEQ1I00aQoFGGz1G+aeZyU3tcU/HoRPKZ2qBFlTTLol21Qb92d6l6x9epOYr7kZ43PjBGq31pr1V8aC9voo7CS7vEE2kHW2Ct32XazeKXIQy1EFgRNl7utM92d412oW9nLSjpUt6NYH3arM5wKawT3ebVRpK4y8igThCO0ZPooNMmhPN5p+u3D2/yA+fWY+N97ZW1+TPT/7InU88HS+/snj4eHvu19fpz1+d/U628f3mo3Blo9n781aRe+HmL93dO3j//SOweziPH5Ptj7g+jnw/XWDud3pt/i3Ouath6/NkX6eA8F7HC6Zn7HspmVdMHnH5+D/sGct/mNR2D0/DbY17b4+no/9HF5fsvE9+L3Va0fvp5MfnjzXm9FfcUI/Ktfl7PJr1cZgKXYJ/gT9vbb/wE9LdlbAC8AAA== -->
