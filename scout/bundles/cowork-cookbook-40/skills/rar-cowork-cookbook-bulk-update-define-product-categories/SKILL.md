---
name: "rar-cowork-cookbook-bulk-update-define-product-categories"
description: "Applies a bulk field update to product category records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, waits for approval, th"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_product_categories", "rar_sha256": "e9b88c1f6f9160d0b5b1142f1d3557b46b4b223192a0997bdcfb27c3ac18186f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_define_product_categories`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_define_product_categories_agent.py` and in the RCI capsule.

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

Define product categories Bulk Field Update — Applies a bulk field update to product category records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, waits for approval, th

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-product-categories
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
      "description": "Explicit approval after reviewing the dry-run preview, before changes are committed.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against; defaults to USMF sandbox.",
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
      "description": "List of product category record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_product_categories_agent.py` and embedded as the fenced Python below (sha256 e9b88c1f6f9160d0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_product_categories_agent.py` first:

```bash
python3 bulk_update_define_product_categories_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_define_product_categories_agent.py   # or on stdin
python3 bulk_update_define_product_categories_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define product categories Bulk Field Update — Applies a bulk field update to product category records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, waits for approval, th

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-product-categories
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_define_product_categories',
    "version": '3.0.3',
    "display_name": 'Define product categories Bulk Field Update',
    "description": 'Applies a bulk field update to product category records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, waits for approval, th',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-define-product-categories',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-define-product-categories',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9e094df810d44fca',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/define-product-categories'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/bulk-update-define-product-categories', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of product category record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when define product categories records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to define product categories records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to product category records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, waits for approval, th', 'example_request': 'Bulk update these product category records in USMF sandbox to the new value — show me the dry-run first.', 'inputs': [{'description': 'List of product category record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants to change a field on many product category records at once in D365 and needs a reviewable dry-run before the write is committed.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateDefineProductCategories(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDefineProductCategories'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of product category record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateDefineProductCategories().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916a9OiWLbmX3HeEzFVdchMEAQ0OzpiQBAVuYMolR1Z3EGucoc69d9no+alurPPdE/Mp3krKlTYe93X86yd8Pub3TZRUb19fNN8O19wdprGkV8t7NxbbIu+qBLwUSQO+H/hFnlTxU7bFFX99u7N82u3issmLnKwnSrLNPbrhb1w2jRZBLGfeou29OzGXzTFoqwKr3WbhQt+h0U1LirfLSqvXsT5ghlzO4vdeoER+GL3P7WtsPg59UM7Xfh5EzfjwtCE3btFDWxyiuGXRRfbiybyv9jHzNtYVV6UaRvG+UcgummrfDbFq8b3VZsD7X4X+/1iXv9wpQgWjh8UlQ/bQeNXcN3YTVu/W/R23NQLcGNhl8Dkzk7fAVXAWX+wszL167ePv/7t3VsMvr99/P3NTe0aXHqjgcvGw1fGD+Lcl5/ebp/OgrAACamdh2BpOYJ45+B36VdATwYueX6weP36ufbT4N3iP/8z6e0qrH/5+ClfvP4+vc3/qcCb2femsOvG90A8S9uJUxClDwsq7e2x/s79GqQrDz88d36TVJSLv873fn4q+RD6zc+f3gpggj0n89PbLwsQgE9vIHLg+4dZSvnzLx/Sovern3/5JqdunZsPcgqEAas/fH79fokFC78tjYPFZ01mty9dIPlx6QPh3/k3/z1Nf4l7heTzc/HPRflu8WPJsz9/BfY+C9IBcn8sFsQA7Hz7cCvi/OeXDpBjP7dz1//5l38m1o18N0njuvmX5P76FBz5tgei9QrJL+8e6fvbAnr59lXmP1dbgoL5dzwBy7+o+xqofyb7kdm/E52Cuq2/5vKH4n60Afrr4td/6tt/t+HdIvj0xvhp3IG6c1L/4+L3R4n8+pP37eJPf/sDiP4/itGKtnIfEj5ndh4Hft18/vzrT/Xj8k9/+/WntgRV7NvZ57ZKfyTzR3F96PlTBF+rfv7zXqDfyJO86PPF1x5a/F6U/6P648PibKex9+16/XHxfSfOf9BiduKL0mcIvuvGGtj6XRx/efsDwE8OvAH4Mt8G+PEf/7EQYrcq6iJoFppbtM0CJLiJM382Xo9igLL1AzUADPpVHYPAvtaB+p8zPFsMIPG3/+U+IPW9+4J8eMbyz08U/+w9oO3zC8k/u1/B7bcPCx0IB98B/ALUVilZ/pTbIUDvWTEA39qvOgBWztj470FPv5+/zMj/278k//ND1Idy/O1BS/ETAdXtYUa/uk39D7OfZuTnL69cwGT+4Lst0JIWLjApiAF2vwP+10XaAfScY1IncZouvBjgSzMz0iwbxO3jLOy3335z7Dr6lD/hGls8qa6GwYKv5izevwe+BWkcRs2n3HejYvHT73/8tPivxX+36yF81iED7nhlBVh41CRxAbqszcCymRYBvNveIyu///GKMBCTA24GOYyDmWvnzaBKE9/7Em5tT71HceJFbgvAU0XVAA5YxM2HxSFYfLUXKJ1vzSwRFXWz8PzSzz0/d0cg1QbufI1kXjSAepu4DsZ3i7b2H1p/cyr7YWIG2t1uflsIWxlwUpHOXF+9OApsLvIYhP9rMTyvAyHVT/WC/iLiw0Kc63JR2pVdRpX90hHYz7zMZPzaDoTbi9zvP+UzA/tzqB5N8gwPWAQi475S+n7OOZhZMoAIzzmj+bLGnplTfzBo9SmvXw1gV/5jKgGmjIuwjb2ZFv7yKqk6Klow0MzxA5bOkl5Z8F5ZedTgk/3/ftiZUzVPCIvdYyh6DgqLTy2KLFeL/5/npjkkFMepLEfpLLNgRV29PlM1j5JzSp/T52zrvPfRlt8mmi+o9QW8P+VpDOquGv/yXPlI8GvNExDbCuRDpdSHfFBdIFWz3EfxzzGsHrmwP+VfWOIdcPYBiSD/AClAJ81B/6JwvvvF0gjAwfz728TwSsWMG6DAF2XrpKD4At/3HNtNgFXV3MCvNINO8Ofo9VHsRn/yak4WyCuQvwBGzGEETPLhK3I/734x/U8bn4PRvOUxNLagf6uHAGCHPxs4I1ofz3mwm+fkDvz8+BAC3MjKZvbdAR2UvXtd9Cv/3sZ13Mxo+YyrXwK4fj9/Pj2dr/pDCZoGBAu0RtmC6D6aacaZDIw9wAaAJ6A8sjgHYwAIyisID4F2NiMDQN5XuT0lPi6/HPIfHTjz15eNsyPznnkkWATAdHBl/B5A9B+VCZCXzSseev++0r5qm2XPIFoDIAQav9x9zg4fnvT/nC8WX+R+/Iej0c//3unpQejGnwvg4yJqmrL+CMNPEv7CwR8AhMFPW+sHH79/osP7J1++fyHE+29g8yfhT78/Lv49A/8k4tUgHxfLD8gHZL51ehXY6w/EY/uevr5fzXc/5ar/DWWB+iIDFTZnbwQDwFdK/LIE8GJYAdACi58UWc/M2gMyf3ACSMWn/PuKnzsOUE4ezhVaF98hwWM2ANX/zNxX6gK38gbo9uaZMvQ/zEex2fzaf/uYt2n67g2gqP8vHuJmisrm0q7n4x8IPRjTmvkW+PUF+ebvfz4bswPAeBd0xZcliwd6Lp7oOrfNXHF/B7rvvpD4y9sHP810FjcgVrMbzVjOdj9PefNc+MCqoflHA6THFzv9sGB8gItp/X0DvKhtpvbv+vQZahBiF/j4bjGHpZ6pGIR6dn/ucbtOHpj/Q1seRPT5SUT/aNCDe/7EVa+5wQ4fPf0XACCB3aYgneDGzGNfaOyHysBI8BmEtX0m4s+qZmh4sOrP9S+PGgGLF4/F84V5ogAM/NAPGqX+4nj9Qz1fp/J/VGOCMWgW4hUfZ0fevRAWfIKT1LvF10MRCOXrmDpr8PM2e/v463wgm6vrsWX+AvaAj6+bvv5ri+O//e0Hdj1t/hx7P/D/BPbPzPNPJonFgamfnDen+AdeP8QDUgDUOlv6LQTfDCkex8TZEGB48/xXjd/fQJ/YQKb96pTXOQMsBxj6vp6nKhgAClAIfj9bH9z7vzuBvITUkQ2GXyDF3zjrtbsMiGCzJBAPcXBnuVyhwdLDcJx0VoSzclAUW25QG9lsSMdzAwclXcx2l+vlmgiAvCeKfH42HBA5WwXi8R4Akf/tNrjkvTx6ejCH6+uB54EKT8d+f3OIFVi5X9UH6vm3haGl46NrRyQd+IJDW6lvXO2clilHkDuy4yfD8NA+EUQuD8tdbVwSLrLi+LQxo0wK12SY7UJ5rUJ9hyQbzJXGS1paDCDkEXYPLFMfLunKpwl4PTI33yNDlV8uK1azjyZr7ba8EjmlINyX49rmhapWT5V9VIKjz0FbEoIbH45tAbmZkRFHplhh2VqUxB1yNycWT/gknoToSu5GjTDNAUtWdQfDhbiCznB3S6GTYSutpanGRYriI4mTG7hKVUkZmTQ4DiS3WqYHgxtNKcHrpB0OeSNNCMwvDwV81AZMUk51UR9TZ+swgThGMXlH28YJdfEyXo6pcTOv94up2VbmpmjhHK+XOr5NsROrbR3u6EIV+oBf3rbO1b5RK7+73GFZPyNBp7PYnsA7DGdIfMX09va4JamipNP6uqv7bdacmCsxTKneegc1cMVu4FALT8wM318V4mxk9QaZBIxrDpCZXaljcuau953k7XFk8JUwsZKNuTut8UNIp5WiEKjQWMBxV9/Lqm05qXSN2LRXz6YC0a00lMuAw5Puvg8IU7mnORdWdMGqTEdtsMOZMLZ1qpQXoQq3OkEpdV7daOFK3b1l7Z3oMr/6Br1Ht01IMccTmRy76z6EPUS6yZnPrZp+vSLODhiH/fbIS6JiOb172kYxo49HrsfKkTgdNnxRuwKFIz0Do6QWKsQmKRxXh5a7lLh7Gk6WCuTqvEFc9KWJ8zB8UAlbJjL+HobHrVYn0WkrnzeHTtwOuBfziByrK4U/Vvtz7Tp5yMLyICkmV3oqLg2VsUeX6nIX2tuASmT2sCrhbBwMpKOcE3Q66KeJL3bU0NyUdFkpPNLcNLqBJvvsGHpyxZHgaJ7068nDOADpuyw87OsI6zi5TzlPQl086syJXk0+r2anM0TLzkiviib2lMxhwgQaA2q0MdJYypHvFMltgszeXAsnquokxmLq6SZdJ6qQyvC6K8cjNTZnqq80LtUA4vjaCro5SEb79cmFuR28UeG43HUVu7dknNmtA33HbKROYMLVGXf5fewcDyd6WRdnOvGO6LUydN9iykaIcqcutUuKZ9TWEoYCUpSWyCUyZKOKLe8mo4jcZqw46rZC2nGYhhJiai9CJo+nBpOtvePhchAGxUSZ2+VwMXh1X9CretcT+nLdDhdxkAia8fdZH9rnlQvt0pAvynqSmdhBj5ziJ3zRS93k8JleNTVrm2osngqcS5duPC7rm2JU3Hhkj4FSlkHbQtHUiAeytNoUgQ67yDharlqNwTof+g1mcbLjiaVcowTWlduLdLYCZm+4abWdMP0oH2pntzIU4Ywa0t5X8LsuUx2siwfesCpPlTrkREC3o7+rE63cGFawEYaVteIba8l0S3hLxtgGOZT49pI0Z+sq7fBrUw4CYXKiOASWXNoq1W5HZFULzJ600tt201KtiJYdn8Z3uAwOHa/u+F1NU3uBmggyX4rNDXfGc78fQnYjwSa2ypAzgk1Dr9hry75F/trYm7TkCmw9uSc3iEyamzbxcWXxJkrbiHS4IlSumof+jGYsGQVr9qyBxHDWvTJqMWEVmdH59QkjAWFO8VVE8Wri6S17GeAcP9+NArIgA6xPuOVl76/kNYxf1h4BTiymaSg6udrXeHzIcxCznKCXt/VpuISF7MDDsbaP2K23BMEPsSPGEolal5I3dZzm2tz9pheDnFCEmhjtSZkUy7+Pe2qz6Vnr6EW9QUi3tXna9wrK2uL6MAnM5sYb2i4ssoETHc4C1KwkFiWSQeD4IpYFuuUbKl+mESMLjneYCP+Kp2KX6Lyvozu9RDwCFaNQreLTVLj0vooVyjulopCpgJcQ7r4iGe2YeJQY8uVmnexOBd/anTvKPsUgK8SQ474I6BO5I1pTZHFDgrWwIeuWMw710gSlaBtQPUKSXkNBILfplsoNNNu6/dGRi/Ud0W7JMKpSk9eGH/ZqGnu5U5HwtSfdFu2uitqcR56ByiMJEXbTw67b5YUF3DOk8mRU7TqursfyEsTTNQzpe7Jd4jIZ4bwtuqzj3DfnYm8pqpBLa8ZVlOU5sHF6501rxcEl1kaPykEOj8Jqv6wY2i+nw1bkmUrKe6kvr4593KqKn6bJVlZWZX6MQmGLancF4eL1Fdne7psavUZ1uSo0rc6H8/6oX/ypXxPklTc1wBlJCCxey0Mk2/K19NUbgERTuvR39nzJryWUq+jhoEmGYmJEWqwiUAq1UPBpIkF6cVhdlelayEFQDMaRU6NBvg/+UqFBJcQKewiKtOnvl6OoTPoG6kInPqGaGLO3Q3plWuhWU1uxcLhDeJAbJFNCmWkYvT0IG9JzLY2+8PjWcGQJGu8oIHdTHePjacT4w9azMkxGc7YzhLO21tP9uhV5nNeYbdJQzTh5F5dm83Xn5Qcl0e4uHY13N0cULYaVa3Vb65R2ubDZAZBi7zpaSCB5vGvLW0nR3djxxtaL8YqPskt4oQSUOt3BwXV/GScw3nC8ExbejTKyg1GstHVVNhctsl0jOkg1eWoyLWW2axqWczM+XE70kDiNlhKu42CmyJytHT6EUroSY1xhMZAnath662WpE8c8Lo5csT0txYTolRN009kLYvHH0AzrY2VyfoLF+m7sQcLxMr3viWuS7tjOpP2DygrmOF74Ha2y10GAjPHYsyqA3vyQC87yIpeMgY12GPA03CSBR9VDH6AHZchv7pmLnSwV1B2CFMZEQMAKbyM5nNKsbNvK8SaGJPqAngolxPsqpcl6e/Z7m3Q9YX+VtXWDOQgknCZkwnY1FFpCsBIPqaqQF0zZhZ6bSVsrQzXk6AgCm7PETqMPsoEW7DqIbC9OK7veDWxGnePbJqQa10dkMU/hfjcoum4bXHCk6WWIWrW4k4wEWcsZyjpBHujmiaGiTnf0jCjX962k1Wdqlwr7OF6OjnZZMyEhacjBxeDlXdneuYrWdKJjMpfkd5cbGK8YRUlqnjjZycaW1zcOoVdQ6Rlo6VIkdvNyWMb7RHGSVCE91UOv2m2T7LkOQc+xa9lyIuQ5c2xsS8hbjdkdkCrh7tXh7LEwdpO2UqTjdnE2ouNY7B2L3moHHjlzIaM6Mr9DLl6y4nUJF/U9u7wMCBhS5TvnMpeztiskGrBXxCfteLw1bilsffSeqw2FcCvVN7XT/VZzdHk04pI2sek0OJIQ7Hex0KhZ3EeWmSRnjyfuTGmXnsVsaP22VHcMFRqb5MgMfZrKlQZZl8uJHM/pwKBkxEEk5zVKWSmMN5xGCC9hUwjZJI7dtAwPZXvGhKk937zTltsbOQDPTI8OEWzjXMxc3T2zofbVwfEP3moL4wWJY6cApy44l7ia0RU7c9wjckPdWNRIW+5+RK5HKK4wUVlG+QVnHbKy72567s5LobfIi4XkJh2kmUvR540a4Ds43JKn9fFAhFuB0O/W5ERywdHVqdd4IZhc1DMtMKN0cRvdh6JS3HvtdVJ21cXxGpXxWO+bOhJaMOYVnYjTZ6g+2Wyrt0N4OVk55rj+qJRtXka2Nd1yKGZPTa9tYZczMUdUu5wxu0bg9wgl0+6S4RkBGnFs33R25ewlqGCu9jRGDKNKlJyEHVyJPncUIWSbE8j+thbOls7TElvKu8uxFwvlsuUoqo5Zx9yrlUmOY0aYB8gzxj4k792kGMrVDsfcRLXDeRyE2lRFZ2tFDig2NikQ68rKuwnvQ9SGderKGGuoXkIG23tkCuCTz3wsYv3toXe9lF9he06CIJksYAGzsqWLwo52jXBaPJ4PrXQ0LalT1JSmhUyKuEsj0VdFUDGMUrq9PIyZgWQbCeP1yeAKt5xwMKLiZ9k309FXk5LsYMW9eMdM45bjPWl63YHSio/TXFSL7kbD0rHr+3XG4nZdUkdttbzkaswhlXydzA3kdDUv33eAUxLZuNE1ajADvq75YljH1pK9YczkWnvWvxKZGBdLNsjlSM4rSt6JqlFsnF68HEu3oaPzJe13+NhgOZof99CxYlSBEeKAR9LrqJw5ZKThIxH14xBOo1yK5jFedYFEOOeVckkqh1tfOxNtqnvU+Htnq69X+mmnuLUl0umdt45m6+hyP1ZXhU8LLd/dBwdZMxBEG4AfSK8sjzZgnKK4Od1EFuDo0Fa+MVlMW+QCY0yReBAoakzRkaCum3zSjYPj4XebJesbxK6EVakKhcWNI2kd6NO9J6P9RspbDrU5pQ3O3Ro7TQeyOfINXKGQcwZ07lGpQ/qJLzD67mIQiGn0G0aktK0/FHCpl/rEJXl5LIqEs9obegujSqtprnJZRfFERjpflchb4jsqMQihVTUZTfbjhUjwKz655tK/+Z0OJmVlt4xQNXGxWmI7gWhIL+x1BoPhCKZkeHI744bUanrcBeae7WmkyrQm3UWDHcuHoiQOlU1T13AQMThLmm2yd89D6vkCEdl78tys8jyQyEKUE6KCrzysqJflBmnTBLoMHtrUoa2rbFajyuoqC4zi76FYwyqN4FsUau4sbPc4ckIg2yOTM+mKOw91ipzUhvq2v1zc85I/Dfm4bJe6aJDitiogPY1hLFNhuj2TfNwJ+Lmt2g7dK5Zc3QHXMqcGuShM5wa7ardWNtheveO7NSF2eo1u77dgs+uXpGgtVbIEJpBEuVEH6yQQRqxDRcGbwZk9b1E9vlAiuxSxob2Ak2PdyNqIZiEHKztSxXy+HSa5ji6XQ7rhz7dT0aK7CD+vxUPsZ7fag7bHlXB1rqHFoEMAQRsYGjtAzShv3I78GmrhwVtznFj316o7nye32AYHjt8JfXs+kHHX36Y1vjN9axiSEM7o+zZASm1/iT2mCo7KEda35F09+PgNCsNkgHQlvwWoZsGlLQ522XgZfhnkQbvSIiExU+2ZqZiFw2G3nZykxnssk7heu6I2i7gXMp9CtSFsBrtmXTzVI7stmb6Dl23XtjLghAOExUznSCOYkJldupa3aslw58PuSJxixAw23DLAdGXZueaaHwl70434fa8hpym3L2s/hfLL8roiI2q9NPaHVchZVOwHDCKhsJtaqIUNlH41lo49Ydv4fsNV8hhPxIA4jrlGaf+e+Z5xlRKRq91B2HRgJOrWTNOsLInZW93FNQla6tKIVJopVvk+0QtEjN1L2Ms85nFrJy2TbWitcJ2FA8jnTSPFT2e8wWgAuIQw4Hgd21QWAG53BtWXKYnKYJORNGmvuYHP1Joum1ja8OyIlji2LvOJ3MD+ZoNNLswycSfKfieeIFrggpu2tdf77HiuYF4J4cTbRxYYSfZQ1pNpkbJYQuoToO1byJEjxKBNG9AlIeHbk6A2V8kALTAJk6yYMWGp5wK6bqqTeTrQeOMIMERaRW1CbUhagpN2VVQvkWSgc09ErSuoiSs3uezZuoTXjaxO9Wm5wQfY4G0SYrLUde7tpPQ4Zpo3/16VXEmvMLucLocm6wqu2y530X3PBRrMIMblhPAdvb+JGMXqy221hPObJzFUHQawCut7ZX0vYnAQF/Z77hycOW+4M6S9rW+1SzVkyOWX25ru16dlSgY+sUZLa43mZueDCllOaq3AU3DZlCkmyZebWFo3sGpw5GWvGzfoQFL5SrIhPMuxXYs1Frnx1JMsDxJ6A0crXPURrCHaZppaWFuNd3+5OQz2SF/Wt9t2B5VKJvjWvYa5om38+ybiblrj2ucNajspTjpVkt/UoM71IKdhodhgtwxZSesRod1kf7BMA1KI4rJ0anWZoLSB371suV/Wasd16eBdKauN8SO9FhBe3YQtG6iMdLoNTKQzkMI7iuEHshbF9+m49y2ZbuKij9OzOdhySe1zNoR3ickh616OaxTT/DFD0C2iFrWwkvlNVplX/QQjG3In32++hAgYBc6eWS4PynabdCGdeH0D3WXYDsk9uXJvQp1tXF6eVptu40/0hkWXTnIesh09No2NeUeoyNB0xRl73Yir7Xp9o9WOxO9oamvuuKwrx2uvd+wCsWmbNtRktoWX3trpdJ3ESjfv9rS/uc20G10elhsmlQNwPjbXqbtf0g5bdA7J85AKht3lkTn2gYYlQYuyG7hWxJPDA2CFOoE1eNOMCD1EVbI9xRluE9rJyarSyCMJi9KR64Kb7muDtOwCIp0gD+rKfangRbCm1QyDpAtRNUXgttD6cJUkuKwHV4ZiaqTGQY35zW7KQxa5crdLK0RrCN5URM735H3ncdWwbJTWvHmR1HstmZ5xqGrgFjOxktuIoruT080ZxYxuLZEeko6obACrYaWXr9WqLMmaoWvsRg2qslwLld2JkOVlMYpF3eEmMshIBMrGvnTNcfIFthvFo8OxNs9OmbPXvGjK5OaUQP7q6OxdO1R7RXDrZkNvT7RfeCxy6rNuuaZc6WbiggGBCvU65nzRCMk44d1KuefMEotaSWqJiwaFe6QggHLungSDbTNET63giuChHL7ZEpEFgnc+W7CwWYUyYZPo0RfiC4xOgZbqVjftw03V8liIyKvWulGi0O7zc9XC4b1s+cJO7yd01De64njwOeWk+wj3a9huDWLKKmNbjR4ZY1XutLLdCapY2yvQxVfRxlsZNfR6tKSNKEy+odobhtBLyxtFTDJFb5gyCcALTyNH6k63uCetdJ06s8JOPys6blyOTNP78qm9277o8dspHfaynwWMvW0iWVPjgvD3gyKXNCveRYCdKeN7rN8FJOfQXUR0uAej143ph1FXpTkmJeZmc1jvd3pbXLR+aOvNCG2hRE6u0a5zNYK9X5tCRY4q06/P0CWQVpDcdqGxZtzQl1adGtzvbCfdNSlF2kqUiaC4S/vLSAjB1dWXZ0e+ub5Ew+s9coF0MC0wFEX99e3d2/yg+fW4+N97dW1+ZPT/7OnU8yHTl/dQHs8Pfdv7+ND18d+062/v3io3BlY9n8XVaRu+Hmj93ZO49//SuweziPH5XtiXh9HPh+yNHc4vT7/FudfWTTV+rov08T4K2OG09fyuZT0b6oLP7x+FfufO8yloHOafm+Jz5TdxNV+K8/lNE9+Lnyvmn+HrCSVY/3pF6jNG4J/9qpzdfb3OALzEPiAfsLc//jelxuCfBS8AAA== -->
